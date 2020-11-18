#!/usr/bin/env python3
"""
DB create user
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """database class
    """

    def __init__(self):
        """Initialize
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """create session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """save the user
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """find user
        """
        if not kwargs:
            raise InvalidRequestError
        users_fields = [
            'id', 'email', 'hashed_password', 'session_id', 'reset_token'
        ]
        for key in kwargs.keys():
            if key not in users_fields:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """updates an user
        """
        if user_id is None:
            return None

        if not kwargs:
            raise ValueError

        users_fields = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
        ]

        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if key not in users_fields:
                raise ValueError
            setattr(user, key, value)

        self._session.commit()
