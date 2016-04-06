
.. _API-fence-context-alloc:

===================
fence_context_alloc
===================

*man fence_context_alloc(9)*

*4.6.0-rc1*

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

This function will return the first index of the number of fences allocated. The fence context is used for setting fence->context to a unique number.
