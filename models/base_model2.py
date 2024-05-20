#!/usr/bin/python3
"""
Base Model
"""
from datetime import datetime
import uuid


class BaseModel:
    """

    """
    def __init__(self, *args, **kwargs):
        """
        method initialies the attribute
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        Method update the update_at attribute in the base class
        """
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """set how object are to be printed
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """method returns the dictionary representation of an instance
        """
        att_dict = self.__dict__.copy()
        att_dict["__class__"] = self.__class__.__name__
        att_dict["created_at"] = self.created_at.isoformat()
        att_dict["updated_at"] = self.updated_at.isoformat()
        return att_dict
    
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), 
                                       my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
