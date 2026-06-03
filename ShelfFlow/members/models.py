from django.db import models

class Member(models.Model):
    full_name = models.CharField(max_length=100)
    member_code = models.PositiveIntegerField(unique=True, null=True, blank= True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    join_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
        
        if self.member_code is None:
            self.member_code = self.pk  + 1000
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name} ( {self.member_code} )'