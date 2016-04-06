
.. _API-clamp-val:

=========
clamp_val
=========

*man clamp_val(9)*

*4.6.0-rc1*

return a value clamped to a given range using val's type


Synopsis
========

.. c:function:: clamp_val( val, lo, hi )

Arguments
=========

``val``
    current value

``lo``
    minimum allowable value

``hi``
    maximum allowable value


Description
===========

This macro does no typechecking and uses temporary variables of whatever type the input argument 'val' is. This is useful when val is an unsigned type and min and max are literals
that will otherwise be assigned a signed integer type.
