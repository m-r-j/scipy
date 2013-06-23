# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_csc', [dirname(__file__)])
        except ImportError:
            import _csc
            return _csc
        if fp is not None:
            try:
                _mod = imp.load_module('_csc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _csc = swig_import_helper()
    del swig_import_helper
else:
    import _csc
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
    if (not static):
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



def csc_matmat_pass1(*args):
  """
    csc_matmat_pass1(int const n_row, int const n_col, int const [] Ap, int const [] Ai, int const [] Bp, 
        int const [] Bi, int [] Cp)
    """
  return _csc.csc_matmat_pass1(*args)

def csc_diagonal(*args):
  """
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, npy_bool_wrapper const [] Ax, 
        npy_bool_wrapper [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, signed char const [] Ax, 
        signed char [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, unsigned char const [] Ax, 
        unsigned char [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, short const [] Ax, 
        short [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, unsigned short const [] Ax, 
        unsigned short [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, int const [] Ax, 
        int [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, unsigned int const [] Ax, 
        unsigned int [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, long long const [] Ax, 
        long long [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, unsigned long long const [] Ax, 
        unsigned long long [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, float const [] Ax, 
        float [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, double const [] Ax, 
        double [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, long double const [] Ax, 
        long double [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, 
        npy_cfloat_wrapper [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, 
        npy_cdouble_wrapper [] Yx)
    csc_diagonal(int const n_row, int const n_col, int const [] Ap, int const [] Aj, npy_clongdouble_wrapper const [] Ax, 
        npy_clongdouble_wrapper [] Yx)
    """
  return _csc.csc_diagonal(*args)

def csc_tocsr(*args):
  """
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_bool_wrapper const [] Ax, 
        int [] Bp, int [] Bj, npy_bool_wrapper [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, signed char const [] Ax, 
        int [] Bp, int [] Bj, signed char [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned char const [] Ax, 
        int [] Bp, int [] Bj, unsigned char [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, short const [] Ax, 
        int [] Bp, int [] Bj, short [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned short const [] Ax, 
        int [] Bp, int [] Bj, unsigned short [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, int const [] Ax, 
        int [] Bp, int [] Bj, int [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned int const [] Ax, 
        int [] Bp, int [] Bj, unsigned int [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long long const [] Ax, 
        int [] Bp, int [] Bj, long long [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned long long const [] Ax, 
        int [] Bp, int [] Bj, unsigned long long [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, float const [] Ax, 
        int [] Bp, int [] Bj, float [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, double const [] Ax, 
        int [] Bp, int [] Bj, double [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long double const [] Ax, 
        int [] Bp, int [] Bj, long double [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cfloat_wrapper const [] Ax, 
        int [] Bp, int [] Bj, npy_cfloat_wrapper [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cdouble_wrapper const [] Ax, 
        int [] Bp, int [] Bj, npy_cdouble_wrapper [] Bx)
    csc_tocsr(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_clongdouble_wrapper const [] Ax, 
        int [] Bp, int [] Bj, npy_clongdouble_wrapper [] Bx)
    """
  return _csc.csc_tocsr(*args)

def csc_matmat_pass2(*args):
  """
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_bool_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_bool_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, signed char const [] Ax, 
        int const [] Bp, int const [] Bi, signed char const [] Bx, int [] Cp, 
        int [] Ci, signed char [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned char const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned char const [] Bx, 
        int [] Cp, int [] Ci, unsigned char [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, short const [] Ax, 
        int const [] Bp, int const [] Bi, short const [] Bx, int [] Cp, int [] Ci, 
        short [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned short const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned short const [] Bx, 
        int [] Cp, int [] Ci, unsigned short [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, int const [] Ax, 
        int const [] Bp, int const [] Bi, int const [] Bx, int [] Cp, int [] Ci, 
        int [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned int const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned int const [] Bx, int [] Cp, 
        int [] Ci, unsigned int [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long long const [] Ax, 
        int const [] Bp, int const [] Bi, long long const [] Bx, int [] Cp, 
        int [] Ci, long long [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned long long const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned long long const [] Bx, 
        int [] Cp, int [] Ci, unsigned long long [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, float const [] Ax, 
        int const [] Bp, int const [] Bi, float const [] Bx, int [] Cp, int [] Ci, 
        float [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, double const [] Ax, 
        int const [] Bp, int const [] Bi, double const [] Bx, int [] Cp, int [] Ci, 
        double [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long double const [] Ax, 
        int const [] Bp, int const [] Bi, long double const [] Bx, int [] Cp, 
        int [] Ci, long double [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cfloat_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cfloat_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cfloat_wrapper [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cdouble_wrapper [] Cx)
    csc_matmat_pass2(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_clongdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_clongdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_clongdouble_wrapper [] Cx)
    """
  return _csc.csc_matmat_pass2(*args)

def csc_matvec(*args):
  """
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_bool_wrapper const [] Ax, 
        npy_bool_wrapper const [] Xx, npy_bool_wrapper [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, signed char const [] Ax, 
        signed char const [] Xx, signed char [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned char const [] Ax, 
        unsigned char const [] Xx, unsigned char [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, short const [] Ax, 
        short const [] Xx, short [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned short const [] Ax, 
        unsigned short const [] Xx, unsigned short [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, int const [] Ax, 
        int const [] Xx, int [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned int const [] Ax, 
        unsigned int const [] Xx, unsigned int [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long long const [] Ax, 
        long long const [] Xx, long long [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned long long const [] Ax, 
        unsigned long long const [] Xx, unsigned long long [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, float const [] Ax, 
        float const [] Xx, float [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, double const [] Ax, 
        double const [] Xx, double [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long double const [] Ax, 
        long double const [] Xx, long double [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cfloat_wrapper const [] Ax, 
        npy_cfloat_wrapper const [] Xx, npy_cfloat_wrapper [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cdouble_wrapper const [] Ax, 
        npy_cdouble_wrapper const [] Xx, npy_cdouble_wrapper [] Yx)
    csc_matvec(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_clongdouble_wrapper const [] Ax, 
        npy_clongdouble_wrapper const [] Xx, npy_clongdouble_wrapper [] Yx)
    """
  return _csc.csc_matvec(*args)

def csc_matvecs(*args):
  """
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        npy_bool_wrapper const [] Ax, npy_bool_wrapper const [] Xx, npy_bool_wrapper [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        signed char const [] Ax, signed char const [] Xx, signed char [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        unsigned char const [] Ax, unsigned char const [] Xx, unsigned char [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        short const [] Ax, short const [] Xx, short [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        unsigned short const [] Ax, unsigned short const [] Xx, unsigned short [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        int const [] Ax, int const [] Xx, int [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        unsigned int const [] Ax, unsigned int const [] Xx, unsigned int [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        long long const [] Ax, long long const [] Xx, long long [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        unsigned long long const [] Ax, unsigned long long const [] Xx, unsigned long long [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        float const [] Ax, float const [] Xx, float [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        double const [] Ax, double const [] Xx, double [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        long double const [] Ax, long double const [] Xx, long double [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper const [] Xx, npy_cfloat_wrapper [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper const [] Xx, npy_cdouble_wrapper [] Yx)
    csc_matvecs(int const n_row, int const n_col, int const n_vecs, int const [] Ap, int const [] Ai, 
        npy_clongdouble_wrapper const [] Ax, npy_clongdouble_wrapper const [] Xx, 
        npy_clongdouble_wrapper [] Yx)
    """
  return _csc.csc_matvecs(*args)

def csc_elmul_csc(*args):
  """
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_bool_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_bool_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, signed char const [] Ax, 
        int const [] Bp, int const [] Bi, signed char const [] Bx, int [] Cp, 
        int [] Ci, signed char [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned char const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned char const [] Bx, 
        int [] Cp, int [] Ci, unsigned char [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, short const [] Ax, 
        int const [] Bp, int const [] Bi, short const [] Bx, int [] Cp, int [] Ci, 
        short [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned short const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned short const [] Bx, 
        int [] Cp, int [] Ci, unsigned short [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, int const [] Ax, 
        int const [] Bp, int const [] Bi, int const [] Bx, int [] Cp, int [] Ci, 
        int [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned int const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned int const [] Bx, int [] Cp, 
        int [] Ci, unsigned int [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long long const [] Ax, 
        int const [] Bp, int const [] Bi, long long const [] Bx, int [] Cp, 
        int [] Ci, long long [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned long long const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned long long const [] Bx, 
        int [] Cp, int [] Ci, unsigned long long [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, float const [] Ax, 
        int const [] Bp, int const [] Bi, float const [] Bx, int [] Cp, int [] Ci, 
        float [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, double const [] Ax, 
        int const [] Bp, int const [] Bi, double const [] Bx, int [] Cp, int [] Ci, 
        double [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long double const [] Ax, 
        int const [] Bp, int const [] Bi, long double const [] Bx, int [] Cp, 
        int [] Ci, long double [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cfloat_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cfloat_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cfloat_wrapper [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cdouble_wrapper [] Cx)
    csc_elmul_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_clongdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_clongdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_clongdouble_wrapper [] Cx)
    """
  return _csc.csc_elmul_csc(*args)

def csc_eldiv_csc(*args):
  """
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_bool_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_bool_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, signed char const [] Ax, 
        int const [] Bp, int const [] Bi, signed char const [] Bx, int [] Cp, 
        int [] Ci, signed char [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned char const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned char const [] Bx, 
        int [] Cp, int [] Ci, unsigned char [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, short const [] Ax, 
        int const [] Bp, int const [] Bi, short const [] Bx, int [] Cp, int [] Ci, 
        short [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned short const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned short const [] Bx, 
        int [] Cp, int [] Ci, unsigned short [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, int const [] Ax, 
        int const [] Bp, int const [] Bi, int const [] Bx, int [] Cp, int [] Ci, 
        int [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned int const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned int const [] Bx, int [] Cp, 
        int [] Ci, unsigned int [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long long const [] Ax, 
        int const [] Bp, int const [] Bi, long long const [] Bx, int [] Cp, 
        int [] Ci, long long [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned long long const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned long long const [] Bx, 
        int [] Cp, int [] Ci, unsigned long long [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, float const [] Ax, 
        int const [] Bp, int const [] Bi, float const [] Bx, int [] Cp, int [] Ci, 
        float [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, double const [] Ax, 
        int const [] Bp, int const [] Bi, double const [] Bx, int [] Cp, int [] Ci, 
        double [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long double const [] Ax, 
        int const [] Bp, int const [] Bi, long double const [] Bx, int [] Cp, 
        int [] Ci, long double [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cfloat_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cfloat_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cfloat_wrapper [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cdouble_wrapper [] Cx)
    csc_eldiv_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_clongdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_clongdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_clongdouble_wrapper [] Cx)
    """
  return _csc.csc_eldiv_csc(*args)

def csc_plus_csc(*args):
  """
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_bool_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_bool_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, signed char const [] Ax, 
        int const [] Bp, int const [] Bi, signed char const [] Bx, int [] Cp, 
        int [] Ci, signed char [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned char const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned char const [] Bx, 
        int [] Cp, int [] Ci, unsigned char [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, short const [] Ax, 
        int const [] Bp, int const [] Bi, short const [] Bx, int [] Cp, int [] Ci, 
        short [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned short const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned short const [] Bx, 
        int [] Cp, int [] Ci, unsigned short [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, int const [] Ax, 
        int const [] Bp, int const [] Bi, int const [] Bx, int [] Cp, int [] Ci, 
        int [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned int const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned int const [] Bx, int [] Cp, 
        int [] Ci, unsigned int [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long long const [] Ax, 
        int const [] Bp, int const [] Bi, long long const [] Bx, int [] Cp, 
        int [] Ci, long long [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned long long const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned long long const [] Bx, 
        int [] Cp, int [] Ci, unsigned long long [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, float const [] Ax, 
        int const [] Bp, int const [] Bi, float const [] Bx, int [] Cp, int [] Ci, 
        float [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, double const [] Ax, 
        int const [] Bp, int const [] Bi, double const [] Bx, int [] Cp, int [] Ci, 
        double [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long double const [] Ax, 
        int const [] Bp, int const [] Bi, long double const [] Bx, int [] Cp, 
        int [] Ci, long double [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cfloat_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cfloat_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cfloat_wrapper [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cdouble_wrapper [] Cx)
    csc_plus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_clongdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_clongdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_clongdouble_wrapper [] Cx)
    """
  return _csc.csc_plus_csc(*args)

def csc_minus_csc(*args):
  """
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_bool_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_bool_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, signed char const [] Ax, 
        int const [] Bp, int const [] Bi, signed char const [] Bx, int [] Cp, 
        int [] Ci, signed char [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned char const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned char const [] Bx, 
        int [] Cp, int [] Ci, unsigned char [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, short const [] Ax, 
        int const [] Bp, int const [] Bi, short const [] Bx, int [] Cp, int [] Ci, 
        short [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned short const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned short const [] Bx, 
        int [] Cp, int [] Ci, unsigned short [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, int const [] Ax, 
        int const [] Bp, int const [] Bi, int const [] Bx, int [] Cp, int [] Ci, 
        int [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned int const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned int const [] Bx, int [] Cp, 
        int [] Ci, unsigned int [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long long const [] Ax, 
        int const [] Bp, int const [] Bi, long long const [] Bx, int [] Cp, 
        int [] Ci, long long [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned long long const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned long long const [] Bx, 
        int [] Cp, int [] Ci, unsigned long long [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, float const [] Ax, 
        int const [] Bp, int const [] Bi, float const [] Bx, int [] Cp, int [] Ci, 
        float [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, double const [] Ax, 
        int const [] Bp, int const [] Bi, double const [] Bx, int [] Cp, int [] Ci, 
        double [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long double const [] Ax, 
        int const [] Bp, int const [] Bi, long double const [] Bx, int [] Cp, 
        int [] Ci, long double [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cfloat_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cfloat_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cfloat_wrapper [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_cdouble_wrapper [] Cx)
    csc_minus_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_clongdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_clongdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_clongdouble_wrapper [] Cx)
    """
  return _csc.csc_minus_csc(*args)

def csc_ne_csc(*args):
  """
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_bool_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_bool_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, signed char const [] Ax, 
        int const [] Bp, int const [] Bi, signed char const [] Bx, int [] Cp, 
        int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned char const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned char const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, short const [] Ax, 
        int const [] Bp, int const [] Bi, short const [] Bx, int [] Cp, int [] Ci, 
        npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned short const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned short const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, int const [] Ax, 
        int const [] Bp, int const [] Bi, int const [] Bx, int [] Cp, int [] Ci, 
        npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned int const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned int const [] Bx, int [] Cp, 
        int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long long const [] Ax, 
        int const [] Bp, int const [] Bi, long long const [] Bx, int [] Cp, 
        int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, unsigned long long const [] Ax, 
        int const [] Bp, int const [] Bi, unsigned long long const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, float const [] Ax, 
        int const [] Bp, int const [] Bi, float const [] Bx, int [] Cp, int [] Ci, 
        npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, double const [] Ax, 
        int const [] Bp, int const [] Bi, double const [] Bx, int [] Cp, int [] Ci, 
        npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, long double const [] Ax, 
        int const [] Bp, int const [] Bi, long double const [] Bx, int [] Cp, 
        int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cfloat_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cfloat_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_cdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_cdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    csc_ne_csc(int const n_row, int const n_col, int const [] Ap, int const [] Ai, npy_clongdouble_wrapper const [] Ax, 
        int const [] Bp, int const [] Bi, npy_clongdouble_wrapper const [] Bx, 
        int [] Cp, int [] Ci, npy_bool_wrapper [] Cx)
    """
  return _csc.csc_ne_csc(*args)
# This file is compatible with both classic and new-style classes.


