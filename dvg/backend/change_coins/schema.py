from django.conf import settings
from graphene_django import DjangoObjectType
from change_coins import models
import graphene



class UserType(DjangoObjectType):
    class Meta:
        model = settings.AUTH_USER_MODEL

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag
