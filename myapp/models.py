from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.auth.models import User  as AuthUser

class User(models.Model):
    GENDER_CHOICES = [("male","Male"),("female","Female"),("others","Others")]
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Enter a valid email address.")])
    gender  = models.CharField(max_length=15, choices=GENDER_CHOICES, default='male')
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Age must be between 0 and 100.", null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="created_users", null=True)

    def __str__(self):
        return f"{self.name}"
