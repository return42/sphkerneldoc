.. -*- coding: utf-8; mode: rst -*-

.. _API-fence-get-rcu:

=============
fence_get_rcu
=============

*man fence_get_rcu(9)*

*4.6.0-rc5*

get a fence from a reservation_object_list with rcu read lock


Synopsis
========

.. c:function:: struct fence * fence_get_rcu( struct fence * fence )

Arguments
=========

``fence``
    [in] fence to increase refcount of


Description
===========

Function returns NULL if no refcount could be obtained, or the fence.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
