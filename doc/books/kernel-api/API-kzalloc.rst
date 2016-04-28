.. -*- coding: utf-8; mode: rst -*-

.. _API-kzalloc:

=======
kzalloc
=======

*man kzalloc(9)*

*4.6.0-rc5*

allocate memory. The memory is set to zero.


Synopsis
========

.. c:function:: void * kzalloc( size_t size, gfp_t flags )

Arguments
=========

``size``
    how many bytes of memory are required.

``flags``
    the type of memory to allocate (see kmalloc).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
