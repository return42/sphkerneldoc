
.. _API-kfree:

=====
kfree
=====

*man kfree(9)*

*4.6.0-rc1*

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

Don't free memory not originally allocated by ``kmalloc`` or you will run into trouble.
