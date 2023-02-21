from typing import List

class Tensor:
    def __init__(self, *args, **kwargs):
        self.args_ = args
        self.kwargs_ = kwargs

class TensorList:
    def __init__(self, params, **kwargs):
        self.params_ = params
        self.input_tensor_ : List[Tensor] = []
        self.output_tensor_: List[Tensor] = []

class TensorListFactory:

    registry = {}

    @classmethod
    def register(cls, name : str, register_cls : TensorList):
        if name not in cls.registry:
            cls.registry[name] = register_cls
        else:
            raise Exception("op name is invalid")

    @classmethod
    def factory(cls, name : str) -> TensorList:
        if name in cls.registry:
            return cls.registry[name]
        else:
            return TensorList

    @classmethod
    def print(cls):
        print(cls.registry)



def registerTensorList(op_name=""):
    def register(cls : TensorList):
        if op_name:
            TensorListFactory.register(op_name, cls)
        else:
            raise Exception("op name is invalid")
        return cls
    return register