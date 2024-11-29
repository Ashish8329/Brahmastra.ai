from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]
    
    @classmethod
    def get_choices(cls):
        return tuple(x.value for x in cls)
    
    @classmethod
    def has_value(cls, value):
        return any(value==item.value[0] for item in cls)
    
    @classmethod
    def get_help_text(cls):
        """
        Generates a dynamic help text for model choices.
        """
        return "Choices include:\n" + "\n".join(
            f"-'{item.value[0]}':{item.value[1]}" for item in cls
        )

class RoleType(ChoiceEnum):
    SUPER_USER = ("0", "Super Admin")
    RECRUITER = ("1", "Recruiter")
    USER = ("2", "User")