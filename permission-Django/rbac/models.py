from django.db import models


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=32)
    codes = models.CharField(max_length=32)
    menu_gp = models.ForeignKey('Permission', related_name='aaa', null=True)
    group = models.ForeignKey('Group')


class User(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    position = models.ManyToManyField('Position')


class Position(models.Model):
    """
    职位表
    """
    title = models.CharField(max_length=32)
    permission = models.ManyToManyField('Permission')


class Group(models.Model):
    """
    权限之Group表
    """

    title = models.CharField(max_length=32)
    menu = models.ForeignKey(to='Menu')


class Menu(models.Model):
    """
    Group之Menu表
    """
    title = models.CharField(max_length=32)
