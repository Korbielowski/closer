# from django.contrib.auth.base_user import BaseUserManager


# class CloserUserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fiels):
#         user = self.model(email=email, password=password, **extra_fiels)
#         user.set_password(password)
#         user.is_staff = False
#         user.is_superuser = False
#         user.sava(using=self._db)
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         user = self.model(email=email, password=password, **extra_fields)
#         user.is_active = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# def create_user(self, email, passoword, **extra_fields):
#     if not email:
#         raise ValueError("Email must be set")
#     email = self.normalize_email(email)
#     user = self.model(email=email, **extra_fields)
#     user.set_password(passoword)
#     user.save()
#     return user

# def create_superuser(self, email, password, **extra_fields):
#     extra_fields.setdefault("is_staff", True)
#     extra_fields.setdefault("is_superuser", True)
#     extra_fields.setdefault("is_active", True)

#     if extra_fields.get("is_staff") is not True:
#         raise ValueError(("Superuser must have is_staff=True."))
#     if extra_fields.get("is_superuser") is not True:
#         raise ValueError(("Superuser must have is_superuser=True."))
#     return self.create_user(email, password, **extra_fields)
