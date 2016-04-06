
.. _API-fence-get-rcu:

=============
fence_get_rcu
=============

*man fence_get_rcu(9)*

*4.6.0-rc1*

get a fence from a reservation_object_list with rcu read lock


Synopsis
========

.. c:function:: struct fence ⋆ fence_get_rcu( struct fence * fence )

Arguments
=========

``fence``
    [in] fence to increase refcount of


Description
===========

Function returns NULL if no refcount could be obtained, or the fence.
