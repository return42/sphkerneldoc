
.. _API-ipc-rcu-alloc:

=============
ipc_rcu_alloc
=============

*man ipc_rcu_alloc(9)*

*4.6.0-rc1*

allocate ipc and rcu space


Synopsis
========

.. c:function:: void ⋆ ipc_rcu_alloc( int size )

Arguments
=========

``size``
    size desired


Description
===========

Allocate memory for the rcu header structure + the object. Returns the pointer to the object or NULL upon failure.
