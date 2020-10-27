from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.



class AbstractModels(models.Model):
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     abstract = True



class CustomUserManager(BaseUserManager):
        """
        Custom user model manager where email is the unique identifiers
        for authentication instead of usernames.
        """
        def create_user(self, email, password, **extra_fields):
                """
                        Create and save a User with the given email and password.
                """
                if not email:
                        raise ValueError("Email must be set")
                email = self.normalize_email(email)
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save()
                return user

        def create_superuser(self, email, password, **extra_fields):
                """
                        Create and save a SuperUser with the given email and password.
                """
                extra_fields.setdefault('is_staff', True)
                extra_fields.setdefault('is_superuser', True)
                extra_fields.setdefault('is_active', True)

                if extra_fields.get('is_staff') is not True:
                        raise ValueError('Superuser must have is_staff=True.')
                if extra_fields.get('is_superuser') is not True:
                        raise ValueError('Superuser must have is_superuser=True.')
                return self.create_user(email, password, **extra_fields)


ROLE = [('patient', 'patient'),('physician', 'physician'),('researcher', 'researcher'),('junior researcher', 'junior researcher')]
class User(AbstractUser):
        '''
                Extending User model
        '''
        organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True, blank=True)
        lat = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
        lon = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
        role = models.CharField(max_length=100, choices=ROLE, default='', null=True, blank=True)
        

        USERNAME_FIELD = 'username'
        REQUIRED_FIELDS = []

        # objects = CustomUserManager()

        def __str__(self):
                return str(f'{self.first_name} { self.last_name}')
        
        def full_name(self):
                return '{0} {1}'.format(self.first_name, self.last_name)


class Organization(AbstractModels):
    org_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.org_name)


class Medicine(AbstractModels):
    med_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.med_name)

class Note(AbstractModels):
    test_session = models.ForeignKey('TestSession', related_name='notes', on_delete=models.CASCADE)
    medicines = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    notes = models.TextField(max_length=50)


    def __str__(self):
        return str(self.test_session)


class Test(AbstractModels):
    datetime = models.DateTimeField()
    therapys = models.ForeignKey('Therapy', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.therapys)

class TestSession(AbstractModels):
    tests = models.ForeignKey('Test', on_delete=models.CASCADE)
    test_type = models.PositiveIntegerField()
    data_url = models.CharField(max_length=200)

    def __str__(self):
        return str(self.tests)



class Therapy(AbstractModels):
    patient = models.ForeignKey('User', on_delete=models.CASCADE)
    medicines = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    therapy_list = models.ForeignKey('TherapyList', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.therapy_list)


class TherapyList(AbstractModels):
    therapy_name = models.CharField(max_length=200)
    medicines = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    dosage = models.CharField(max_length=200)

    def __str__(self):
        return str(self.therapy_name)


class News(AbstractModels):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    link = models.CharField(max_length=300)
    comments = models.CharField(max_length=300)
    guid = models.CharField(max_length=300)
    pubdate = models.CharField(max_length=300)
    media = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.title)



class DataFileOne(models.Model):
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    time = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Data File A'

    def __str__(self):
        return str(self.filename)


class DataFileTwo(models.Model):
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    time = models.CharField(max_length=50)
    filename = models.CharField(max_length=50)
    button = models.PositiveIntegerField()
    correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Data File B'

    def __str__(self):
        return str(self.filename)