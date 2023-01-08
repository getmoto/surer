# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from collections import OrderedDict

try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable

from sure.terminal import red, green, yellow


# FIXME: move FakeOrderedDict to another module since it
#        does not have anything todo with compat.
#        The safe_repr function should already get a
#        FakeOrderedDict instance. Maybe the _obj_with_safe_repr
#        function should be part of the FakeOrderedDict
#        classes __repr__ method.
class FakeOrderedDict(OrderedDict):
    """ OrderedDict that has the repr of a normal dict

    We must return a string
    """
    def __unicode__(self):
        if not self:
            return '{}'
        key_values = []
        for key, value in self.items():
            key, value = repr(key), repr(value)
            key_values.append("{0}: {1}".format(key, value))
        res = "{{{0}}}".format(", ".join(key_values))
        return res

    def __repr__(self):
        return self.__unicode__()


def _obj_with_safe_repr(obj):
    if isinstance(obj, dict):
        ret = FakeOrderedDict()
        try:
            keys = sorted(obj.keys())
        except TypeError:  # happens for obj types which are not orderable, like ``Enum``
            keys = obj.keys()
        for key in keys:
            ret[_obj_with_safe_repr(key)] = _obj_with_safe_repr(obj[key])
    elif isinstance(obj, list):
        ret = []
        for x in obj:
            if isinstance(x, dict):
                ret.append(_obj_with_safe_repr(x))
            else:
                ret.append(x)
    else:
        ret = obj
    return ret


def safe_repr(val):
    try:
        if isinstance(val, dict):
            # We special case dicts to have a sorted repr. This makes testing
            # significantly easier
            val = _obj_with_safe_repr(val)
        ret = repr(val)
    except UnicodeEncodeError:
        ret = red('a %r that cannot be represented' % type(val))
    else:
        ret = green(ret)

    return ret
