#!/usr/bin/python3
"""
  Base Model
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """

    """
    def __init__(self, *args, **kwargs):
        """
        method initialies the attribute
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def save(self):
        """
        Method update the update_at attribute in the base class
        """
        models.storage.save()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """set how object are to be printed
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """method returns the dictionary representation of an instance
        """
        att_dict = self.__dict__.copy()
        att_dict["__class__"] = type(self).__name__
        att_dict["created_at"] = att_dict["created_at"].isoformat()
        att_dict["updated_at"] = att_dict["updated_at"].isoformat()
        return att_dict
