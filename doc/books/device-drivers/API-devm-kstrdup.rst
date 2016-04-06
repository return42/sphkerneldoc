
.. _API-devm-kstrdup:

============
devm_kstrdup
============

*man devm_kstrdup(9)*

*4.6.0-rc1*

Allocate resource managed space and copy an existing string into that.


Synopsis
========

.. c:function:: char ⋆ devm_kstrdup( struct device * dev, const char * s, gfp_t gfp )

Arguments
=========

``dev``
    Device to allocate memory for

``s``
    the string to duplicate

``gfp``
    the GFP mask used in the ``devm_kmalloc`` call when allocating memory


RETURNS
=======

Pointer to allocated string on success, NULL on failure.
