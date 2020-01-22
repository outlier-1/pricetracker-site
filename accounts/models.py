from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, birth_date, is_active=True,
                    is_staff=False, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not password:
            raise ValueError("Users must have a password.")
        if not name or not surname:
            raise ValueError("Users must have both name and surname.")
        if not birth_date:
            raise ValueError("Users must have a valid birth date.")

        user_obj = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            birth_date=birth_date
        )
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, name, surname, birth_date, password=None):
        user = self.create_user(email, name, surname, birth_date, password=password,
                                is_staff=True)
        return user

    def create_superuser(self, email, name, surname, birth_date, password=None):
        user = self.create_user(email, name, surname, birth_date, password=password,
                                is_staff=True, is_admin=True)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    surname = models.CharField(max_length=50, blank=False, null=False)
    birth_date = models.DateField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    confirmed_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'birth_date']

    def __str__(self):
        return self.fullname

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
