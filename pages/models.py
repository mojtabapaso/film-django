from django.contrib.auth import get_user_model
from repository.models import Film
from django.db import models

User = get_user_model()


class Command(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='command', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='command', null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    sub_command = models.ForeignKey("self", models.CASCADE, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    is_sub_command = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"user: {self.user}--sub command: {self.is_sub_command}--is_active: {self.is_active}"
