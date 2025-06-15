from django.db import models
from employees.models import Employee

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="performance_reviews")
    rating = models.PositiveSmallIntegerField()  # 1-5
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.review_date}: {self.rating}"
