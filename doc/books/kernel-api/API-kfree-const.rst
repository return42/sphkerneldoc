.. -*- coding: utf-8; mode: rst -*-

.. _API-kfree-const:

===========
kfree_const
===========

*man kfree_const(9)*

*4.6.0-rc5*

conditionally free memory


Synopsis
========

.. c:function:: void kfree_const( const void * x )

Arguments
=========

``x``
    pointer to the memory


Description
===========

Function calls kfree only if ``x`` is not in .rodata section.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
