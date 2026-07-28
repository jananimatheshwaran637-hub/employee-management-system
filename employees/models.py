from django.db import models


class Employee(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]


    name = models.CharField(
        max_length=100
    )


    email = models.EmailField(
        unique=True
    )


    phone = models.CharField(
        max_length=15
    )


    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )


    department = models.CharField(
        max_length=100
    )


    designation = models.CharField(
        max_length=100
    )


    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    address = models.TextField()


    photo = models.ImageField(
        upload_to='employee_photos/',
        blank=True,
        null=True
    )


    joining_date = models.DateField(
        auto_now_add=True
    )



   



    def __str__(self):

        return self.name