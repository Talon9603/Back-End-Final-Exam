from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Employee
from departments.models import Department
from attendance.models import Attendance
from performance.models import Performance
import random
from datetime import timedelta, date

fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with fake employee data"

    def handle(self, *args, **kwargs):
        departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']
        department_objs = []

        for dept_name in departments:
            dept, _ = Department.objects.get_or_create(name=dept_name)
            department_objs.append(dept)

        for _ in range(50):
            dept = random.choice(department_objs)
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                department=dept
            )

            # Seed attendance for past 30 days
            for i in range(30):
                Attendance.objects.create(
                    employee=emp,
                    date=date.today() - timedelta(days=i),
                    status=random.choice(['PRESENT', 'ABSENT', 'LATE'])
                )

            # Seed 3 performance reviews
            for _ in range(3):
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )

        self.stdout.write(self.style.SUCCESS("Database seeded with fake employee data."))
