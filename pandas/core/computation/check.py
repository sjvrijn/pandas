from pandas.compat._optional import import_optional_dependency

ne = import_optional_dependency("numexpr", raise_on_missing=False, on_version="warn")
_NUMEXPR_INSTALLED = ne is not None
_NUMEXPR_VERSION = ne.__version__ if _NUMEXPR_INSTALLED else None
__all__ = ["_NUMEXPR_INSTALLED", "_NUMEXPR_VERSION"]
