import os
from abc import ABC, abstractmethod
from typing import Union, Dict


def load_shaders(name: str):
    vert_path = os.path.join("src", "shader", f"{name}.vert")
    frag_path = os.path.join("src", "shader", f"{name}.frag")
    with open(vert_path) as vf, open(frag_path) as ff:
        return {"vertex_shader": vf.read(), "fragment_shader": ff.read()}


class SingletonFieldClass(ABC):
    __fields: Union[Dict, None] = None

    def __init__(self, *args, **kwargs):
        if self.__class__.__fields is None:
            self.__class__.__fields = self.get_fields(*args, **kwargs)

    @abstractmethod
    def get_fields(self):
        raise NotImplementedError

    def __getattr__(self, name: str):
        return self.__class__.__fields.get(name)

    def __setattr__(self, name: str, value):
        if name == f"{self.__class__}__fields":
            if self.__class__.__fields is None:
                return super().__setattr__(name, value)
            else:
                raise Exception("Do not modify <self.__fields> directly!!!")
        if name in (self.__class__.__fields or {}):
            raise Exception(
                f"{name} is a singleton field. Do not modify it directly!!!"
            )
        return super().__setattr__(name, value)
