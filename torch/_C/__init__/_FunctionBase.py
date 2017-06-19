# encoding: utf-8
# module torch._C
# from /Users/rook/anaconda/lib/python3.6/site-packages/torch/_C.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import torch._C._functions as _functions # <module 'torch._C._functions'>

from .object import object

class _FunctionBase(object):
    # no doc
    @classmethod
    def apply(cls, *args, **kwargs): # real signature unknown
        pass

    def register_hook(self, *args, **kwargs): # real signature unknown
        pass

    def _do_backward(self, *args, **kwargs): # real signature unknown
        pass

    def _do_forward(self, *args, **kwargs): # real signature unknown
        pass

    def _register_hook_dict(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    dirty_tensors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    needs_input_grad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_functions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    non_differentiable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    requires_grad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    saved_tensors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    saved_variables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shared_pairs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    to_save = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



