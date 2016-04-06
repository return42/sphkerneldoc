
.. _API-kfree-const:

===========
kfree_const
===========

*man kfree_const(9)*

*4.6.0-rc1*

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
