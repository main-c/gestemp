from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Used to create and save a Collaborator with the given email and password
        """

        if not email:
            raise ValueError(_("Email must be set."))
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """
        Used to create and save superuser with the given email and password
        """

        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={"unique": _(
            "A user with that email address already exists.")},
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(
        _("last name"), max_length=150, blank=True, null=True)

    # profile_photo = models.ImageField(
    #     null=True, blank=True, upload_to="collaborators/profile"
    # )
    joined_at = models.DateField(auto_now_add=True)
    is_staff = models.BooleanField(
        _("admin status"),
        default=False,
        help_text=_(
            "Designates wheter the user is an admin and can log into this admin site or not."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates wheter a this user should be treated as active or not."
            " You can unckeck it instead of delete the user."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_responsable = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="users",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="users",
        related_query_name="user",
    )

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.is_staff

    def get_full_name(self):
        return f'{self.first_name} {self.last_name or ""}'.strip()

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        constraints = [
            models.CheckConstraint(
                check=models.Q(is_responsable=True, is_teacher=True,
                               is_student=False)
                | models.Q(is_responsable=False, is_teacher=False, is_student=True)
                | models.Q(is_responsable=False, is_teacher=False, is_student=False)
                | models.Q(is_responsable=True, is_teacher=False, is_student=False),

                name="student_not_responsable_and_teacher",
            )
        ]
