.. -*- coding: utf-8; mode: rst -*-

.. _API-kfree:

=====
kfree
=====

*man kfree(9)*

*4.6.0-rc5*

free previously allocated memory


Synopsis
========

.. c:function:: void kfree( const void * objp )

Arguments
=========

``objp``
    pointer returned by kmalloc.


Description
===========

If ``objp`` is NULL, no operation is performed.

Don't free memory not originally allocated by ``kmalloc`` or you will
run into trouble.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
