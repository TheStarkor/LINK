from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255, unique=True,)
    portal_id = models.CharField(max_length=10, unique=True, null=True,)
    name = models.CharField(max_length=30, null=True,)
    dept_major = models.CharField(max_length=50, null=True,)
    username = models.SlugField(max_length=30, null=True, unique=True,)
    reputation = models.IntegerField(blank=False, null=False, default=0,)
    password = models.CharField(max_length=130, null=True,)

    # Not active until email verification
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
