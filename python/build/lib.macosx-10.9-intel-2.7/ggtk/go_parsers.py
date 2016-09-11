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
            fp, pathname, description = imp.find_module('_go_parsers', [dirname(__file__)])
        except ImportError:
            import _go_parsers
            return _go_parsers
        if fp is not None:
            try:
                _mod = imp.load_module('_go_parsers', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _go_parsers = swig_import_helper()
    del swig_import_helper
else:
    import _go_parsers
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
    __swig_destroy__ = _go_parsers.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _go_parsers.SwigPyIterator_value(self)
    def incr(self, n = 1): return _go_parsers.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _go_parsers.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _go_parsers.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _go_parsers.SwigPyIterator_equal(self, *args)
    def copy(self): return _go_parsers.SwigPyIterator_copy(self)
    def next(self): return _go_parsers.SwigPyIterator_next(self)
    def __next__(self): return _go_parsers.SwigPyIterator___next__(self)
    def previous(self): return _go_parsers.SwigPyIterator_previous(self)
    def advance(self, *args): return _go_parsers.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _go_parsers.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _go_parsers.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _go_parsers.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _go_parsers.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _go_parsers.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _go_parsers.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _go_parsers.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class SizeVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SizeVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SizeVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _go_parsers.SizeVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _go_parsers.SizeVector___nonzero__(self)
    def __bool__(self): return _go_parsers.SizeVector___bool__(self)
    def __len__(self): return _go_parsers.SizeVector___len__(self)
    def pop(self): return _go_parsers.SizeVector_pop(self)
    def __getslice__(self, *args): return _go_parsers.SizeVector___getslice__(self, *args)
    def __setslice__(self, *args): return _go_parsers.SizeVector___setslice__(self, *args)
    def __delslice__(self, *args): return _go_parsers.SizeVector___delslice__(self, *args)
    def __delitem__(self, *args): return _go_parsers.SizeVector___delitem__(self, *args)
    def __getitem__(self, *args): return _go_parsers.SizeVector___getitem__(self, *args)
    def __setitem__(self, *args): return _go_parsers.SizeVector___setitem__(self, *args)
    def append(self, *args): return _go_parsers.SizeVector_append(self, *args)
    def empty(self): return _go_parsers.SizeVector_empty(self)
    def size(self): return _go_parsers.SizeVector_size(self)
    def clear(self): return _go_parsers.SizeVector_clear(self)
    def swap(self, *args): return _go_parsers.SizeVector_swap(self, *args)
    def get_allocator(self): return _go_parsers.SizeVector_get_allocator(self)
    def begin(self): return _go_parsers.SizeVector_begin(self)
    def end(self): return _go_parsers.SizeVector_end(self)
    def rbegin(self): return _go_parsers.SizeVector_rbegin(self)
    def rend(self): return _go_parsers.SizeVector_rend(self)
    def pop_back(self): return _go_parsers.SizeVector_pop_back(self)
    def erase(self, *args): return _go_parsers.SizeVector_erase(self, *args)
    def __init__(self, *args): 
        this = _go_parsers.new_SizeVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _go_parsers.SizeVector_push_back(self, *args)
    def front(self): return _go_parsers.SizeVector_front(self)
    def back(self): return _go_parsers.SizeVector_back(self)
    def assign(self, *args): return _go_parsers.SizeVector_assign(self, *args)
    def resize(self, *args): return _go_parsers.SizeVector_resize(self, *args)
    def insert(self, *args): return _go_parsers.SizeVector_insert(self, *args)
    def reserve(self, *args): return _go_parsers.SizeVector_reserve(self, *args)
    def capacity(self): return _go_parsers.SizeVector_capacity(self)
    __swig_destroy__ = _go_parsers.delete_SizeVector
    __del__ = lambda self : None;
SizeVector_swigregister = _go_parsers.SizeVector_swigregister
SizeVector_swigregister(SizeVector)

class StringArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _go_parsers.new_StringArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _go_parsers.delete_StringArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _go_parsers.StringArray___getitem__(self, *args)
    def __setitem__(self, *args): return _go_parsers.StringArray___setitem__(self, *args)
    def cast(self): return _go_parsers.StringArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _go_parsers.StringArray_frompointer
    if _newclass:frompointer = staticmethod(_go_parsers.StringArray_frompointer)
StringArray_swigregister = _go_parsers.StringArray_swigregister
StringArray_swigregister(StringArray)

def StringArray_frompointer(*args):
  return _go_parsers.StringArray_frompointer(*args)
StringArray_frompointer = _go_parsers.StringArray_frompointer

class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _go_parsers.StringVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _go_parsers.StringVector___nonzero__(self)
    def __bool__(self): return _go_parsers.StringVector___bool__(self)
    def __len__(self): return _go_parsers.StringVector___len__(self)
    def pop(self): return _go_parsers.StringVector_pop(self)
    def __getslice__(self, *args): return _go_parsers.StringVector___getslice__(self, *args)
    def __setslice__(self, *args): return _go_parsers.StringVector___setslice__(self, *args)
    def __delslice__(self, *args): return _go_parsers.StringVector___delslice__(self, *args)
    def __delitem__(self, *args): return _go_parsers.StringVector___delitem__(self, *args)
    def __getitem__(self, *args): return _go_parsers.StringVector___getitem__(self, *args)
    def __setitem__(self, *args): return _go_parsers.StringVector___setitem__(self, *args)
    def append(self, *args): return _go_parsers.StringVector_append(self, *args)
    def empty(self): return _go_parsers.StringVector_empty(self)
    def size(self): return _go_parsers.StringVector_size(self)
    def clear(self): return _go_parsers.StringVector_clear(self)
    def swap(self, *args): return _go_parsers.StringVector_swap(self, *args)
    def get_allocator(self): return _go_parsers.StringVector_get_allocator(self)
    def begin(self): return _go_parsers.StringVector_begin(self)
    def end(self): return _go_parsers.StringVector_end(self)
    def rbegin(self): return _go_parsers.StringVector_rbegin(self)
    def rend(self): return _go_parsers.StringVector_rend(self)
    def pop_back(self): return _go_parsers.StringVector_pop_back(self)
    def erase(self, *args): return _go_parsers.StringVector_erase(self, *args)
    def __init__(self, *args): 
        this = _go_parsers.new_StringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _go_parsers.StringVector_push_back(self, *args)
    def front(self): return _go_parsers.StringVector_front(self)
    def back(self): return _go_parsers.StringVector_back(self)
    def assign(self, *args): return _go_parsers.StringVector_assign(self, *args)
    def resize(self, *args): return _go_parsers.StringVector_resize(self, *args)
    def insert(self, *args): return _go_parsers.StringVector_insert(self, *args)
    def reserve(self, *args): return _go_parsers.StringVector_reserve(self, *args)
    def capacity(self): return _go_parsers.StringVector_capacity(self)
    __swig_destroy__ = _go_parsers.delete_StringVector
    __del__ = lambda self : None;
StringVector_swigregister = _go_parsers.StringVector_swigregister
StringVector_swigregister(StringVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _go_parsers.DoubleVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _go_parsers.DoubleVector___nonzero__(self)
    def __bool__(self): return _go_parsers.DoubleVector___bool__(self)
    def __len__(self): return _go_parsers.DoubleVector___len__(self)
    def pop(self): return _go_parsers.DoubleVector_pop(self)
    def __getslice__(self, *args): return _go_parsers.DoubleVector___getslice__(self, *args)
    def __setslice__(self, *args): return _go_parsers.DoubleVector___setslice__(self, *args)
    def __delslice__(self, *args): return _go_parsers.DoubleVector___delslice__(self, *args)
    def __delitem__(self, *args): return _go_parsers.DoubleVector___delitem__(self, *args)
    def __getitem__(self, *args): return _go_parsers.DoubleVector___getitem__(self, *args)
    def __setitem__(self, *args): return _go_parsers.DoubleVector___setitem__(self, *args)
    def append(self, *args): return _go_parsers.DoubleVector_append(self, *args)
    def empty(self): return _go_parsers.DoubleVector_empty(self)
    def size(self): return _go_parsers.DoubleVector_size(self)
    def clear(self): return _go_parsers.DoubleVector_clear(self)
    def swap(self, *args): return _go_parsers.DoubleVector_swap(self, *args)
    def get_allocator(self): return _go_parsers.DoubleVector_get_allocator(self)
    def begin(self): return _go_parsers.DoubleVector_begin(self)
    def end(self): return _go_parsers.DoubleVector_end(self)
    def rbegin(self): return _go_parsers.DoubleVector_rbegin(self)
    def rend(self): return _go_parsers.DoubleVector_rend(self)
    def pop_back(self): return _go_parsers.DoubleVector_pop_back(self)
    def erase(self, *args): return _go_parsers.DoubleVector_erase(self, *args)
    def __init__(self, *args): 
        this = _go_parsers.new_DoubleVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _go_parsers.DoubleVector_push_back(self, *args)
    def front(self): return _go_parsers.DoubleVector_front(self)
    def back(self): return _go_parsers.DoubleVector_back(self)
    def assign(self, *args): return _go_parsers.DoubleVector_assign(self, *args)
    def resize(self, *args): return _go_parsers.DoubleVector_resize(self, *args)
    def insert(self, *args): return _go_parsers.DoubleVector_insert(self, *args)
    def reserve(self, *args): return _go_parsers.DoubleVector_reserve(self, *args)
    def capacity(self): return _go_parsers.DoubleVector_capacity(self)
    __swig_destroy__ = _go_parsers.delete_DoubleVector
    __del__ = lambda self : None;
DoubleVector_swigregister = _go_parsers.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)

class BoostSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BoostSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BoostSet, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _go_parsers.new_BoostSet()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _go_parsers.delete_BoostSet
    __del__ = lambda self : None;
BoostSet_swigregister = _go_parsers.BoostSet_swigregister
BoostSet_swigregister(BoostSet)

class RelationshipPolicyInterface(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RelationshipPolicyInterface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RelationshipPolicyInterface, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def isAllowed(self, *args): return _go_parsers.RelationshipPolicyInterface_isAllowed(self, *args)
    __swig_destroy__ = _go_parsers.delete_RelationshipPolicyInterface
    __del__ = lambda self : None;
RelationshipPolicyInterface_swigregister = _go_parsers.RelationshipPolicyInterface_swigregister
RelationshipPolicyInterface_swigregister(RelationshipPolicyInterface)

class AllowedSetRelationshipPolicy(RelationshipPolicyInterface):
    __swig_setmethods__ = {}
    for _s in [RelationshipPolicyInterface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, AllowedSetRelationshipPolicy, name, value)
    __swig_getmethods__ = {}
    for _s in [RelationshipPolicyInterface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, AllowedSetRelationshipPolicy, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _go_parsers.new_AllowedSetRelationshipPolicy(*args)
        try: self.this.append(this)
        except: self.this = this
    def isAllowed(self, *args): return _go_parsers.AllowedSetRelationshipPolicy_isAllowed(self, *args)
    def addRelationship(self, *args): return _go_parsers.AllowedSetRelationshipPolicy_addRelationship(self, *args)
    def isEmpty(self): return _go_parsers.AllowedSetRelationshipPolicy_isEmpty(self)
    __swig_destroy__ = _go_parsers.delete_AllowedSetRelationshipPolicy
    __del__ = lambda self : None;
AllowedSetRelationshipPolicy_swigregister = _go_parsers.AllowedSetRelationshipPolicy_swigregister
AllowedSetRelationshipPolicy_swigregister(AllowedSetRelationshipPolicy)

class StandardRelationshipPolicy(RelationshipPolicyInterface):
    __swig_setmethods__ = {}
    for _s in [RelationshipPolicyInterface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, StandardRelationshipPolicy, name, value)
    __swig_getmethods__ = {}
    for _s in [RelationshipPolicyInterface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, StandardRelationshipPolicy, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _go_parsers.new_StandardRelationshipPolicy(*args)
        try: self.this.append(this)
        except: self.this = this
    def isAllowed(self, *args): return _go_parsers.StandardRelationshipPolicy_isAllowed(self, *args)
    __swig_destroy__ = _go_parsers.delete_StandardRelationshipPolicy
    __del__ = lambda self : None;
StandardRelationshipPolicy_swigregister = _go_parsers.StandardRelationshipPolicy_swigregister
StandardRelationshipPolicy_swigregister(StandardRelationshipPolicy)

class GoParserInterface(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GoParserInterface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GoParserInterface, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def parseGoFile(self, *args): return _go_parsers.GoParserInterface_parseGoFile(self, *args)
    def isFileGood(self, *args): return _go_parsers.GoParserInterface_isFileGood(self, *args)
    def clone(self): return _go_parsers.GoParserInterface_clone(self)
    __swig_destroy__ = _go_parsers.delete_GoParserInterface
    __del__ = lambda self : None;
GoParserInterface_swigregister = _go_parsers.GoParserInterface_swigregister
GoParserInterface_swigregister(GoParserInterface)

class AllowedRelationshipOboGoParser(GoParserInterface):
    __swig_setmethods__ = {}
    for _s in [GoParserInterface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, AllowedRelationshipOboGoParser, name, value)
    __swig_getmethods__ = {}
    for _s in [GoParserInterface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, AllowedRelationshipOboGoParser, name)
    __repr__ = _swig_repr
    def parseGoFile(self, *args): return _go_parsers.AllowedRelationshipOboGoParser_parseGoFile(self, *args)
    def isFileGood(self, *args): return _go_parsers.AllowedRelationshipOboGoParser_isFileGood(self, *args)
    def splitWith(self, *args): return _go_parsers.AllowedRelationshipOboGoParser_splitWith(self, *args)
    def clone(self): return _go_parsers.AllowedRelationshipOboGoParser_clone(self)
    def setPolicy(self, *args): return _go_parsers.AllowedRelationshipOboGoParser_setPolicy(self, *args)
    def __init__(self, *args): 
        this = _go_parsers.new_AllowedRelationshipOboGoParser(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _go_parsers.delete_AllowedRelationshipOboGoParser
    __del__ = lambda self : None;
AllowedRelationshipOboGoParser_swigregister = _go_parsers.AllowedRelationshipOboGoParser_swigregister
AllowedRelationshipOboGoParser_swigregister(AllowedRelationshipOboGoParser)

class AllowedRelationshipXmlGoParser(GoParserInterface):
    __swig_setmethods__ = {}
    for _s in [GoParserInterface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, AllowedRelationshipXmlGoParser, name, value)
    __swig_getmethods__ = {}
    for _s in [GoParserInterface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, AllowedRelationshipXmlGoParser, name)
    __repr__ = _swig_repr
    def parseGoFile(self, *args): return _go_parsers.AllowedRelationshipXmlGoParser_parseGoFile(self, *args)
    def isFileGood(self, *args): return _go_parsers.AllowedRelationshipXmlGoParser_isFileGood(self, *args)
    def clone(self): return _go_parsers.AllowedRelationshipXmlGoParser_clone(self)
    def setPolicy(self, *args): return _go_parsers.AllowedRelationshipXmlGoParser_setPolicy(self, *args)
    def __init__(self, *args): 
        this = _go_parsers.new_AllowedRelationshipXmlGoParser(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _go_parsers.delete_AllowedRelationshipXmlGoParser
    __del__ = lambda self : None;
AllowedRelationshipXmlGoParser_swigregister = _go_parsers.AllowedRelationshipXmlGoParser_swigregister
AllowedRelationshipXmlGoParser_swigregister(AllowedRelationshipXmlGoParser)

class RapidXmlGoParser(GoParserInterface):
    __swig_setmethods__ = {}
    for _s in [GoParserInterface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RapidXmlGoParser, name, value)
    __swig_getmethods__ = {}
    for _s in [GoParserInterface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, RapidXmlGoParser, name)
    __repr__ = _swig_repr
    def parseGoFile(self, *args): return _go_parsers.RapidXmlGoParser_parseGoFile(self, *args)
    def isFileGood(self, *args): return _go_parsers.RapidXmlGoParser_isFileGood(self, *args)
    def clone(self): return _go_parsers.RapidXmlGoParser_clone(self)
    def __init__(self): 
        this = _go_parsers.new_RapidXmlGoParser()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _go_parsers.delete_RapidXmlGoParser
    __del__ = lambda self : None;
RapidXmlGoParser_swigregister = _go_parsers.RapidXmlGoParser_swigregister
RapidXmlGoParser_swigregister(RapidXmlGoParser)

class StandardOboGoParser(GoParserInterface):
    __swig_setmethods__ = {}
    for _s in [GoParserInterface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, StandardOboGoParser, name, value)
    __swig_getmethods__ = {}
    for _s in [GoParserInterface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, StandardOboGoParser, name)
    __repr__ = _swig_repr
    def parseGoFile(self, *args): return _go_parsers.StandardOboGoParser_parseGoFile(self, *args)
    def isFileGood(self, *args): return _go_parsers.StandardOboGoParser_isFileGood(self, *args)
    def clone(self): return _go_parsers.StandardOboGoParser_clone(self)
    def __init__(self): 
        this = _go_parsers.new_StandardOboGoParser()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _go_parsers.delete_StandardOboGoParser
    __del__ = lambda self : None;
StandardOboGoParser_swigregister = _go_parsers.StandardOboGoParser_swigregister
StandardOboGoParser_swigregister(StandardOboGoParser)

class StandardXmlGoParser(GoParserInterface):
    __swig_setmethods__ = {}
    for _s in [GoParserInterface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, StandardXmlGoParser, name, value)
    __swig_getmethods__ = {}
    for _s in [GoParserInterface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, StandardXmlGoParser, name)
    __repr__ = _swig_repr
    def parseGoFile(self, *args): return _go_parsers.StandardXmlGoParser_parseGoFile(self, *args)
    def isFileGood(self, *args): return _go_parsers.StandardXmlGoParser_isFileGood(self, *args)
    def clone(self): return _go_parsers.StandardXmlGoParser_clone(self)
    def __init__(self): 
        this = _go_parsers.new_StandardXmlGoParser()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _go_parsers.delete_StandardXmlGoParser
    __del__ = lambda self : None;
StandardXmlGoParser_swigregister = _go_parsers.StandardXmlGoParser_swigregister
StandardXmlGoParser_swigregister(StandardXmlGoParser)



