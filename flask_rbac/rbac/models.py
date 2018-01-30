# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app01.my_db import db


class Permission(db.Model):
    """
    权限表
    """
    extend_existing = True
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    url = Column(String(64))
    code = Column(String(32))
    menu_gp_id = Column(Integer, ForeignKey('permission.id'), nullable=True)
    menu_gp = relationship('Permission', backref='menu_children', remote_side=[id])
    groups_id = Column(Integer, ForeignKey('groups.id'))
    groups = relationship('Groups', backref='permission', )

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True, nullable=False)
    password = Column(String(64))
    position = relationship('Position', secondary='user2position', backref='user')

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


class Position(db.Model):
    """
    职位表
    """
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    permission = relationship('Permission', secondary='position2permission', backref='position')
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


class User2Position(db.Model):
    """
    用户职位表:M2M
    """
    __tablename__ = 'user2position'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    position_id = Column(Integer, ForeignKey('position.id'))

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


class Position2Permission(db.Model):
    """
    职位权限表:M2M
    """
    __tablename__ = 'position2permission'
    id = Column(Integer, primary_key=True)
    position_id = Column(Integer, ForeignKey('position.id'))
    permission_id = Column(Integer, ForeignKey('permission.id'))
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


class Menu(db.Model):
    """
    菜单表
    """
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


class Groups(db.Model):
    """
    分组表
    """
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    menu_id = Column(Integer, ForeignKey('menu.id'))
    menu = relationship('Menu', backref='groups')
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
