.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-kvasprintf:

===============
devm_kvasprintf
===============

*man devm_kvasprintf(9)*

*4.6.0-rc5*

Allocate resource managed space and format a string into that.


Synopsis
========

.. c:function:: char * devm_kvasprintf( struct device * dev, gfp_t gfp, const char * fmt, va_list ap )

Arguments
=========

``dev``
    Device to allocate memory for

``gfp``
    the GFP mask used in the ``devm_kmalloc`` call when allocating
    memory

``fmt``
    The ``printf``-style format string

``ap``
    Arguments for the format string


RETURNS
=======

Pointer to allocated string on success, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
