from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core import validators
from django.core.exceptions import ValidationError

def profile_img_path(instance, filename):
    return 'user_{0}/profile_image/{1}'.format(instance.username, instance.profile_image.name)

def phone_validate(arg):
    if not len(arg)==10:
        raise ValidationError('Please input a valid 10 digit telephone number')
    if not arg.startswith('0'):
        raise ValidationError('Please input a valid telephone number')

class CUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username, password=password, email=email,)

        user.is_admin = True
        user.save(using=self._db)
        return user


class CUser(AbstractBaseUser):

    username=models.CharField(max_length=40, unique=True)
    first_name=models.CharField(max_length=40, blank=True)
    last_name=models.CharField(max_length=40, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    phone=models.CharField(verbose_name='contact number', default='', max_length=10, blank=True, validators=[phone_validate])
    city=models.CharField(default='', max_length=100, blank=True)
    website=models.URLField(default='', blank=True)
    date_of_birth = models.DateField(default='1901-01-01', blank=True)
    profile_image=models.ImageField(upload_to=profile_img_path, blank=True)
    bio=models.TextField(verbose_name='description', blank=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    objects = CUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
