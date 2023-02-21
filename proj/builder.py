from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple, Iterator, Callable

class Call(ABC):

    __REGISTER = {}

    def __init__(self, *, params, **kwargs):
        # self.name = params.name
        # self.age = params.age
        self.params = params
        self.kwargs = kwargs

    def __init_subclass__(cls, *, type_):
        cls.type_ = type_
        Call.__REGISTER[type_] = cls
        super().__init_subclass__()

    @staticmethod
    def get_register():
        return Call.__REGISTER

    @staticmethod
    def get_call(type_, **kwargs) -> 'Call':
        return Call.__REGISTER[type_](**kwargs)
    
    @abstractmethod
    def __call__(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
        # print(f'{self.name}, {self.age}')
        pass


# Call("jzm", 96)()
# c = Call("moxie", 6)
# c.__call__()

class CallJson(Call, type_ = 'json'):
    def __init__(self, params):
        super().__init__(params = self.params)

class CallPrototxt(Call, type_ ='prototxt'):
    pass

class Builder(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def run(self):
        pass

class MoxieBuilder(Builder):
    def __init__(self, *args, **kwargs):
        self.args_ = args[0]
        self.arg_params_ = {}

    def run(self) -> int:
        call_manager = Call.get_call(self.args_, params = self.arg_params_, **vars(self.args_))

        for case in self.gen_cases(call_manager):
            case.run()

        return 0

    def gen_cases(self, manager : Call) -> Iterator['Generator']:
        # for case in call_manager:
        for op_name, case_param in manager():
            yield Generator(opname_register=op_name, case_param=case_param)
        


class Generator:
    def __init__(self, *,opname_register, case_param, **kwargs):
        pass

    def run(self) -> bool:
        return False