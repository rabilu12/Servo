from __future__ import unicode_literals
from django.db import models
import re
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []

        if (
            len(form_data['first_name']) < 2 or
            not(form_data['first_name'].isalpha())
        ):
            errors.append(
                'Please enter a valid first name: no fewer than two character' +
                ' and alphabetic letters only.'
            )

        if (
            len(form_data['last_name']) < 2 or
            not(form_data['last_name'].isalpha())
        ):
            errors.append(
                'Please enter a valid last name: no fewer than two character' +
                ' and alphabetic letters only '
            )

        if not EMAIL_REGEX.match(form_data['email']):
            errors.append(
                'Please enter a valid email address '
            )

        if len(form_data['password']) < 8:
            errors.append('Password must include at least eight characters.')
        if form_data['password'] != form_data['confirm']:
            errors.append('Passwords do not match.')
        return errors
        
    def verify(self, form_data):
        verification = {
            'errors': [],
            'id': None,
        }

        try:
            founduser = User.objects.get(email=form_data['email'])

            if founduser.password == bcrypt.hashpw(
                form_data['password'].encode(),
                founduser.password.encode()
            ):
                verification['id'] = founduser.id

                return verification
            else:
                verification['errors'].append(
                    'Login failed; try again.'
                )

            return verification
        except: 
            print ('what')
            verification['errors'].append(
                'Login failed; try again.'
            )
        return verification

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
# Create your models here.
