.. -*- coding: utf-8; mode: rst -*-

.. _API-fence-context-alloc:

===================
fence_context_alloc
===================

*man fence_context_alloc(9)*

*4.6.0-rc5*

allocate an array of fence contexts


Synopsis
========

.. c:function:: unsigned fence_context_alloc( unsigned num )

Arguments
=========

``num``
    [in] amount of contexts to allocate


Description
===========

This function will return the first index of the number of fences
allocated. The fence context is used for setting fence->context to a
unique number.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
