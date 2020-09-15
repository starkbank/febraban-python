

class Enum:

    @classmethod
    def values(cls):
        return [getattr(cls, a) for a in dir(cls) if not a.startswith('__') and not callable(getattr(cls, a))]

    @classmethod
    def isValid(cls, enum):
        return enum in cls.values()
