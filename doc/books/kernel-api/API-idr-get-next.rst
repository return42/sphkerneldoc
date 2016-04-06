
.. _API-idr-get-next:

============
idr_get_next
============

*man idr_get_next(9)*

*4.6.0-rc1*

lookup next object of id to given id.


Synopsis
========

.. c:function:: void ⋆ idr_get_next( struct idr * idp, int * nextidp )

Arguments
=========

``idp``
    idr handle

``nextidp``
    pointer to lookup key


Description
===========

Returns pointer to registered object with id, which is next number to given id. After being looked up, ⋆\ ``nextidp`` will be updated for the next iteration.

This function can be called under ``rcu_read_lock``, given that the leaf pointers lifetimes are correctly managed.
