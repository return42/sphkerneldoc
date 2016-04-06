
.. _API-devm-kasprintf:

==============
devm_kasprintf
==============

*man devm_kasprintf(9)*

*4.6.0-rc1*

Allocate resource managed space and format a string into that.


Synopsis
========

.. c:function:: char ⋆ devm_kasprintf( struct device * dev, gfp_t gfp, const char * fmt, ... )

Arguments
=========

``dev``
    Device to allocate memory for

``gfp``
    the GFP mask used in the ``devm_kmalloc`` call when allocating memory

``fmt``
    The ``printf``-style format string @...: Arguments for the format string

``...``
    variable arguments


RETURNS
=======

Pointer to allocated string on success, NULL on failure.
