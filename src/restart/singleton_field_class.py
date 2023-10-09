from abc import ABC, abstractmethod


class SingletonFieldClass(ABC):
    __fields = None

    def __init__(self):
        if self.__class__.__fields is None:
            self.__class__.__fields = self.get_singleton_fields()

    @abstractmethod
    def get_singleton_fields(self):
        raise NotImplementedError

    def __getattr__(self, name: str):
        return self.__class__.__fields.get(name, super().__getattr__(name))

    def __setattr__(self, name: str, value):
        print(name)
        if name == f"{self.__class__}__fields":
            if self.__class__.__fields is None:
                return super().__setattr__(name, value)
            else:
                raise Exception("Do not modify <self.__fields> directly!!!")
        if name in (self.__class__.__fields or {}): 
            raise Exception(f"{name} is a singleton field. Do not modify it directly!!!")
        return super().__setattr__(name, value)


class A(SingletonFieldClass):
    def get_singleton_fields(self):
        return {'a': 0, 'b': 0}

class B(SingletonFieldClass):
    def get_singleton_fields(self):
        return {'a': 0, 'b': 0}

for i in range(100):
    a = A()
    a = B()
