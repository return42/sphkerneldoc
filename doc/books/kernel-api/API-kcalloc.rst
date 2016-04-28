.. -*- coding: utf-8; mode: rst -*-

.. _API-kcalloc:

=======
kcalloc
=======

*man kcalloc(9)*

*4.6.0-rc5*

allocate memory for an array. The memory is set to zero.


Synopsis
========

.. c:function:: void * kcalloc( size_t n, size_t size, gfp_t flags )

Arguments
=========

``n``
    number of elements.

``size``
    element size.

``flags``
    the type of memory to allocate (see kmalloc).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
