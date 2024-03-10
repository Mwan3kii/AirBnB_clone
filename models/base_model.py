#!/usr/bin/python3
"""
The BaseModel that defines the attributes to use.
"""

from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class defines attrubutes that will be use."""
    def __init__(self, *args, **kwargs):
        """Initializes the instance attrubutes

        Args:
            *args: Non keyworded arguments
            **kwargs: Keyworded arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at attribute with current time."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary containing all keys/values of dict

        Returns:
            obj_dict: The object dictionary
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__

        return obj_dict

    def __str__(self):
        """String representation of dictionary."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )
