
.. _API-ipc-alloc:

=========
ipc_alloc
=========

*man ipc_alloc(9)*

*4.6.0-rc1*

allocate ipc space


Synopsis
========

.. c:function:: void ⋆ ipc_alloc( int size )

Arguments
=========

``size``
    size desired


Description
===========

Allocate memory from the appropriate pools and return a pointer to it. NULL is returned if the allocation fails
