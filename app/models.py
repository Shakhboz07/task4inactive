from django.db import models


class UserPage(models.Model):
    avatar = models.ImageField("User image", upload_to="users_image")
    first_name = models.CharField(max_length=20)
    roles_auth = (
        ('Admin', "Admin"),
        ('Member', "Member"),
        ('Registered', "Registered"),
    )
    is_auth = models.CharField(max_length=15, choices=roles_auth, default="Registered")
    birth_date = models.DateField()
    roles_status = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
        ('Banned', 'Banned'),
        ('Pending', 'Pending'),
    )
    status = models.CharField(max_length=15, choices=roles_status, default="Banned")
    email = models.EmailField()

    def str(self):
        return self.id

