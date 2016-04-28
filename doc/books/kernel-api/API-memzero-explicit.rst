.. -*- coding: utf-8; mode: rst -*-

.. _API-memzero-explicit:

================
memzero_explicit
================

*man memzero_explicit(9)*

*4.6.0-rc5*

Fill a region of memory (e.g. sensitive keying data) with 0s.


Synopsis
========

.. c:function:: void memzero_explicit( void * s, size_t count )

Arguments
=========

``s``
    Pointer to the start of the area.

``count``
    The size of the area.


Note
====

usually using ``memset`` is just fine (!), but in cases where clearing
out _local_ data at the end of a scope is necessary,
``memzero_explicit`` should be used instead in order to prevent the
compiler from optimising away zeroing.

``memzero_explicit`` doesn't need an arch-specific version as it just
invokes the one of ``memset`` implicitly.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
