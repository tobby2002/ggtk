# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_app_utilities', [dirname(__file__)])
        except ImportError:
            import _app_utilities
            return _app_utilities
        if fp is not None:
            try:
                _mod = imp.load_module('_app_utilities', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _app_utilities = swig_import_helper()
    del swig_import_helper
else:
    import _app_utilities
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _app_utilities.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _app_utilities.SwigPyIterator_value(self)
    def incr(self, n = 1): return _app_utilities.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _app_utilities.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _app_utilities.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _app_utilities.SwigPyIterator_equal(self, *args)
    def copy(self): return _app_utilities.SwigPyIterator_copy(self)
    def next(self): return _app_utilities.SwigPyIterator_next(self)
    def __next__(self): return _app_utilities.SwigPyIterator___next__(self)
    def previous(self): return _app_utilities.SwigPyIterator_previous(self)
    def advance(self, *args): return _app_utilities.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _app_utilities.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _app_utilities.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _app_utilities.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _app_utilities.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _app_utilities.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _app_utilities.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _app_utilities.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class SizeVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SizeVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SizeVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _app_utilities.SizeVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _app_utilities.SizeVector___nonzero__(self)
    def __bool__(self): return _app_utilities.SizeVector___bool__(self)
    def __len__(self): return _app_utilities.SizeVector___len__(self)
    def pop(self): return _app_utilities.SizeVector_pop(self)
    def __getslice__(self, *args): return _app_utilities.SizeVector___getslice__(self, *args)
    def __setslice__(self, *args): return _app_utilities.SizeVector___setslice__(self, *args)
    def __delslice__(self, *args): return _app_utilities.SizeVector___delslice__(self, *args)
    def __delitem__(self, *args): return _app_utilities.SizeVector___delitem__(self, *args)
    def __getitem__(self, *args): return _app_utilities.SizeVector___getitem__(self, *args)
    def __setitem__(self, *args): return _app_utilities.SizeVector___setitem__(self, *args)
    def append(self, *args): return _app_utilities.SizeVector_append(self, *args)
    def empty(self): return _app_utilities.SizeVector_empty(self)
    def size(self): return _app_utilities.SizeVector_size(self)
    def clear(self): return _app_utilities.SizeVector_clear(self)
    def swap(self, *args): return _app_utilities.SizeVector_swap(self, *args)
    def get_allocator(self): return _app_utilities.SizeVector_get_allocator(self)
    def begin(self): return _app_utilities.SizeVector_begin(self)
    def end(self): return _app_utilities.SizeVector_end(self)
    def rbegin(self): return _app_utilities.SizeVector_rbegin(self)
    def rend(self): return _app_utilities.SizeVector_rend(self)
    def pop_back(self): return _app_utilities.SizeVector_pop_back(self)
    def erase(self, *args): return _app_utilities.SizeVector_erase(self, *args)
    def __init__(self, *args): 
        this = _app_utilities.new_SizeVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _app_utilities.SizeVector_push_back(self, *args)
    def front(self): return _app_utilities.SizeVector_front(self)
    def back(self): return _app_utilities.SizeVector_back(self)
    def assign(self, *args): return _app_utilities.SizeVector_assign(self, *args)
    def resize(self, *args): return _app_utilities.SizeVector_resize(self, *args)
    def insert(self, *args): return _app_utilities.SizeVector_insert(self, *args)
    def reserve(self, *args): return _app_utilities.SizeVector_reserve(self, *args)
    def capacity(self): return _app_utilities.SizeVector_capacity(self)
    __swig_destroy__ = _app_utilities.delete_SizeVector
    __del__ = lambda self : None;
SizeVector_swigregister = _app_utilities.SizeVector_swigregister
SizeVector_swigregister(SizeVector)

class StringArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _app_utilities.new_StringArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _app_utilities.delete_StringArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _app_utilities.StringArray___getitem__(self, *args)
    def __setitem__(self, *args): return _app_utilities.StringArray___setitem__(self, *args)
    def cast(self): return _app_utilities.StringArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _app_utilities.StringArray_frompointer
    if _newclass:frompointer = staticmethod(_app_utilities.StringArray_frompointer)
StringArray_swigregister = _app_utilities.StringArray_swigregister
StringArray_swigregister(StringArray)

def StringArray_frompointer(*args):
  return _app_utilities.StringArray_frompointer(*args)
StringArray_frompointer = _app_utilities.StringArray_frompointer

class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _app_utilities.StringVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _app_utilities.StringVector___nonzero__(self)
    def __bool__(self): return _app_utilities.StringVector___bool__(self)
    def __len__(self): return _app_utilities.StringVector___len__(self)
    def pop(self): return _app_utilities.StringVector_pop(self)
    def __getslice__(self, *args): return _app_utilities.StringVector___getslice__(self, *args)
    def __setslice__(self, *args): return _app_utilities.StringVector___setslice__(self, *args)
    def __delslice__(self, *args): return _app_utilities.StringVector___delslice__(self, *args)
    def __delitem__(self, *args): return _app_utilities.StringVector___delitem__(self, *args)
    def __getitem__(self, *args): return _app_utilities.StringVector___getitem__(self, *args)
    def __setitem__(self, *args): return _app_utilities.StringVector___setitem__(self, *args)
    def append(self, *args): return _app_utilities.StringVector_append(self, *args)
    def empty(self): return _app_utilities.StringVector_empty(self)
    def size(self): return _app_utilities.StringVector_size(self)
    def clear(self): return _app_utilities.StringVector_clear(self)
    def swap(self, *args): return _app_utilities.StringVector_swap(self, *args)
    def get_allocator(self): return _app_utilities.StringVector_get_allocator(self)
    def begin(self): return _app_utilities.StringVector_begin(self)
    def end(self): return _app_utilities.StringVector_end(self)
    def rbegin(self): return _app_utilities.StringVector_rbegin(self)
    def rend(self): return _app_utilities.StringVector_rend(self)
    def pop_back(self): return _app_utilities.StringVector_pop_back(self)
    def erase(self, *args): return _app_utilities.StringVector_erase(self, *args)
    def __init__(self, *args): 
        this = _app_utilities.new_StringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _app_utilities.StringVector_push_back(self, *args)
    def front(self): return _app_utilities.StringVector_front(self)
    def back(self): return _app_utilities.StringVector_back(self)
    def assign(self, *args): return _app_utilities.StringVector_assign(self, *args)
    def resize(self, *args): return _app_utilities.StringVector_resize(self, *args)
    def insert(self, *args): return _app_utilities.StringVector_insert(self, *args)
    def reserve(self, *args): return _app_utilities.StringVector_reserve(self, *args)
    def capacity(self): return _app_utilities.StringVector_capacity(self)
    __swig_destroy__ = _app_utilities.delete_StringVector
    __del__ = lambda self : None;
StringVector_swigregister = _app_utilities.StringVector_swigregister
StringVector_swigregister(StringVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _app_utilities.DoubleVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _app_utilities.DoubleVector___nonzero__(self)
    def __bool__(self): return _app_utilities.DoubleVector___bool__(self)
    def __len__(self): return _app_utilities.DoubleVector___len__(self)
    def pop(self): return _app_utilities.DoubleVector_pop(self)
    def __getslice__(self, *args): return _app_utilities.DoubleVector___getslice__(self, *args)
    def __setslice__(self, *args): return _app_utilities.DoubleVector___setslice__(self, *args)
    def __delslice__(self, *args): return _app_utilities.DoubleVector___delslice__(self, *args)
    def __delitem__(self, *args): return _app_utilities.DoubleVector___delitem__(self, *args)
    def __getitem__(self, *args): return _app_utilities.DoubleVector___getitem__(self, *args)
    def __setitem__(self, *args): return _app_utilities.DoubleVector___setitem__(self, *args)
    def append(self, *args): return _app_utilities.DoubleVector_append(self, *args)
    def empty(self): return _app_utilities.DoubleVector_empty(self)
    def size(self): return _app_utilities.DoubleVector_size(self)
    def clear(self): return _app_utilities.DoubleVector_clear(self)
    def swap(self, *args): return _app_utilities.DoubleVector_swap(self, *args)
    def get_allocator(self): return _app_utilities.DoubleVector_get_allocator(self)
    def begin(self): return _app_utilities.DoubleVector_begin(self)
    def end(self): return _app_utilities.DoubleVector_end(self)
    def rbegin(self): return _app_utilities.DoubleVector_rbegin(self)
    def rend(self): return _app_utilities.DoubleVector_rend(self)
    def pop_back(self): return _app_utilities.DoubleVector_pop_back(self)
    def erase(self, *args): return _app_utilities.DoubleVector_erase(self, *args)
    def __init__(self, *args): 
        this = _app_utilities.new_DoubleVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _app_utilities.DoubleVector_push_back(self, *args)
    def front(self): return _app_utilities.DoubleVector_front(self)
    def back(self): return _app_utilities.DoubleVector_back(self)
    def assign(self, *args): return _app_utilities.DoubleVector_assign(self, *args)
    def resize(self, *args): return _app_utilities.DoubleVector_resize(self, *args)
    def insert(self, *args): return _app_utilities.DoubleVector_insert(self, *args)
    def reserve(self, *args): return _app_utilities.DoubleVector_reserve(self, *args)
    def capacity(self): return _app_utilities.DoubleVector_capacity(self)
    __swig_destroy__ = _app_utilities.delete_DoubleVector
    __del__ = lambda self : None;
DoubleVector_swigregister = _app_utilities.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)

class BoostSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BoostSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BoostSet, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _app_utilities.new_BoostSet()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _app_utilities.delete_BoostSet
    __del__ = lambda self : None;
BoostSet_swigregister = _app_utilities.BoostSet_swigregister
BoostSet_swigregister(BoostSet)


def parseParamFile(*args):
  return _app_utilities.parseParamFile(*args)
parseParamFile = _app_utilities.parseParamFile

def checkParams(*args):
  return _app_utilities.checkParams(*args)
checkParams = _app_utilities.checkParams

def paramList(*args):
  return _app_utilities.paramList(*args)
paramList = _app_utilities.paramList

def parseSimpleFile(*args):
  return _app_utilities.parseSimpleFile(*args)
parseSimpleFile = _app_utilities.parseSimpleFile

def splitTake(*args):
  return _app_utilities.splitTake(*args)
splitTake = _app_utilities.splitTake

def setToVec(*args):
  return _app_utilities.setToVec(*args)
setToVec = _app_utilities.setToVec

def vecToSet(*args):
  return _app_utilities.vecToSet(*args)
vecToSet = _app_utilities.vecToSet


