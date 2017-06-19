# encoding: utf-8
# module torch._C
# from /Users/rook/anaconda/lib/python3.6/site-packages/torch/_C.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import torch._C._functions as _functions # <module 'torch._C._functions'>

from .object import object

class CudaDoubleStorageBase(object):
    # no doc
    def copy_(self, *args, **kwargs): # real signature unknown
        pass

    def data_ptr(self, *args, **kwargs): # real signature unknown
        pass

    def element_size(self, *args, **kwargs): # real signature unknown
        pass

    def fill_(self, *args, **kwargs): # real signature unknown
        pass

    def get_device(self, *args, **kwargs): # real signature unknown
        pass

    def is_pinned(self, *args, **kwargs): # real signature unknown
        pass

    def is_shared(self, *args, **kwargs): # real signature unknown
        pass

    def new(self, *args, **kwargs): # real signature unknown
        pass

    def resize_(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def _get_shared_fd(self, *args, **kwargs): # real signature unknown
        pass

    def _new_shared_cuda(self, *args, **kwargs): # real signature unknown
        pass

    def _new_view(self, *args, **kwargs): # real signature unknown
        pass

    def _new_with_file(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _new_with_weak_ptr(cls, *args, **kwargs): # real signature unknown
        pass

    def _root_storage(self, *args, **kwargs): # real signature unknown
        pass

    def _set_cdata(self, *args, **kwargs): # real signature unknown
        pass

    def _set_from_file(self, *args, **kwargs): # real signature unknown
        pass

    def _shared_decref(self, *args, **kwargs): # real signature unknown
        pass

    def _shared_incref(self, *args, **kwargs): # real signature unknown
        pass

    def _share_cuda_(self, *args, **kwargs): # real signature unknown
        pass

    def _weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _write_file(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    _cdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



