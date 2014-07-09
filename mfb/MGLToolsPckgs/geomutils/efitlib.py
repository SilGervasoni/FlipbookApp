# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _efitlib
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
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
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class ellipsoid(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ellipsoid, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ellipsoid, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _efitlib.ellipsoid_name_set
    __swig_getmethods__["name"] = _efitlib.ellipsoid_name_get
    if _newclass:name = _swig_property(_efitlib.ellipsoid_name_get, _efitlib.ellipsoid_name_set)
    __swig_setmethods__["position"] = _efitlib.ellipsoid_position_set
    __swig_getmethods__["position"] = _efitlib.ellipsoid_position_get
    if _newclass:position = _swig_property(_efitlib.ellipsoid_position_get, _efitlib.ellipsoid_position_set)
    __swig_setmethods__["axis"] = _efitlib.ellipsoid_axis_set
    __swig_getmethods__["axis"] = _efitlib.ellipsoid_axis_get
    if _newclass:axis = _swig_property(_efitlib.ellipsoid_axis_get, _efitlib.ellipsoid_axis_set)
    __swig_setmethods__["orientation"] = _efitlib.ellipsoid_orientation_set
    __swig_getmethods__["orientation"] = _efitlib.ellipsoid_orientation_get
    if _newclass:orientation = _swig_property(_efitlib.ellipsoid_orientation_get, _efitlib.ellipsoid_orientation_set)
    __swig_setmethods__["inv_orientation"] = _efitlib.ellipsoid_inv_orientation_set
    __swig_getmethods__["inv_orientation"] = _efitlib.ellipsoid_inv_orientation_get
    if _newclass:inv_orientation = _swig_property(_efitlib.ellipsoid_inv_orientation_get, _efitlib.ellipsoid_inv_orientation_set)
    __swig_setmethods__["tensor"] = _efitlib.ellipsoid_tensor_set
    __swig_getmethods__["tensor"] = _efitlib.ellipsoid_tensor_get
    if _newclass:tensor = _swig_property(_efitlib.ellipsoid_tensor_get, _efitlib.ellipsoid_tensor_set)
    def getPosition(*args): return _efitlib.ellipsoid_getPosition(*args)
    def getAxis(*args): return _efitlib.ellipsoid_getAxis(*args)
    def getOrientation(*args): return _efitlib.ellipsoid_getOrientation(*args)
    def __init__(self, *args): 
        this = _efitlib.new_ellipsoid(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _efitlib.delete_ellipsoid
    __del__ = lambda self : None;
ellipsoid_swigregister = _efitlib.ellipsoid_swigregister
ellipsoid_swigregister(ellipsoid)

class efit_info(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, efit_info, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, efit_info, name)
    __repr__ = _swig_repr
    __swig_setmethods__["weightflag"] = _efitlib.efit_info_weightflag_set
    __swig_getmethods__["weightflag"] = _efitlib.efit_info_weightflag_get
    if _newclass:weightflag = _swig_property(_efitlib.efit_info_weightflag_get, _efitlib.efit_info_weightflag_set)
    __swig_setmethods__["covarflag"] = _efitlib.efit_info_covarflag_set
    __swig_getmethods__["covarflag"] = _efitlib.efit_info_covarflag_get
    if _newclass:covarflag = _swig_property(_efitlib.efit_info_covarflag_get, _efitlib.efit_info_covarflag_set)
    __swig_setmethods__["volumeflag"] = _efitlib.efit_info_volumeflag_set
    __swig_getmethods__["volumeflag"] = _efitlib.efit_info_volumeflag_get
    if _newclass:volumeflag = _swig_property(_efitlib.efit_info_volumeflag_get, _efitlib.efit_info_volumeflag_set)
    __swig_setmethods__["matrixflag"] = _efitlib.efit_info_matrixflag_set
    __swig_getmethods__["matrixflag"] = _efitlib.efit_info_matrixflag_get
    if _newclass:matrixflag = _swig_property(_efitlib.efit_info_matrixflag_get, _efitlib.efit_info_matrixflag_set)
    __swig_setmethods__["nocenterflag"] = _efitlib.efit_info_nocenterflag_set
    __swig_getmethods__["nocenterflag"] = _efitlib.efit_info_nocenterflag_get
    if _newclass:nocenterflag = _swig_property(_efitlib.efit_info_nocenterflag_get, _efitlib.efit_info_nocenterflag_set)
    __swig_setmethods__["noscaleflag"] = _efitlib.efit_info_noscaleflag_set
    __swig_getmethods__["noscaleflag"] = _efitlib.efit_info_noscaleflag_get
    if _newclass:noscaleflag = _swig_property(_efitlib.efit_info_noscaleflag_get, _efitlib.efit_info_noscaleflag_set)
    __swig_setmethods__["nosortflag"] = _efitlib.efit_info_nosortflag_set
    __swig_getmethods__["nosortflag"] = _efitlib.efit_info_nosortflag_get
    if _newclass:nosortflag = _swig_property(_efitlib.efit_info_nosortflag_get, _efitlib.efit_info_nosortflag_set)
    __swig_setmethods__["count"] = _efitlib.efit_info_count_set
    __swig_getmethods__["count"] = _efitlib.efit_info_count_get
    if _newclass:count = _swig_property(_efitlib.efit_info_count_get, _efitlib.efit_info_count_set)
    __swig_setmethods__["cov_scale"] = _efitlib.efit_info_cov_scale_set
    __swig_getmethods__["cov_scale"] = _efitlib.efit_info_cov_scale_get
    if _newclass:cov_scale = _swig_property(_efitlib.efit_info_cov_scale_get, _efitlib.efit_info_cov_scale_set)
    __swig_setmethods__["ell_scale"] = _efitlib.efit_info_ell_scale_set
    __swig_getmethods__["ell_scale"] = _efitlib.efit_info_ell_scale_get
    if _newclass:ell_scale = _swig_property(_efitlib.efit_info_ell_scale_get, _efitlib.efit_info_ell_scale_set)
    def __init__(self, *args): 
        this = _efitlib.new_efit_info(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _efitlib.delete_efit_info
    __del__ = lambda self : None;
efit_info_swigregister = _efitlib.efit_info_swigregister
efit_info_swigregister(efit_info)

fitEllipse = _efitlib.fitEllipse
vec_normalize = _efitlib.vec_normalize
vec_centroid = _efitlib.vec_centroid
vec_dot = _efitlib.vec_dot
vec_magsq = _efitlib.vec_magsq
vec_mag = _efitlib.vec_mag
vec_distancesq = _efitlib.vec_distancesq
vec_distance = _efitlib.vec_distance
vec_max = _efitlib.vec_max
vec_length = _efitlib.vec_length
vec_ctos = _efitlib.vec_ctos
vec_stoc = _efitlib.vec_stoc
vec_sub = _efitlib.vec_sub
vec_copy = _efitlib.vec_copy
vec_add = _efitlib.vec_add
vec_scale = _efitlib.vec_scale
vec_zero = _efitlib.vec_zero
vec_cross = _efitlib.vec_cross
vec_mult = _efitlib.vec_mult
vec_offset = _efitlib.vec_offset
vec_rand = _efitlib.vec_rand
vec_average = _efitlib.vec_average
vec_transform = _efitlib.vec_transform
vec_ftransform = _efitlib.vec_ftransform
mat_jacobi = _efitlib.mat_jacobi
quat_to_mat = _efitlib.quat_to_mat
mat_to_quat = _efitlib.mat_to_quat

