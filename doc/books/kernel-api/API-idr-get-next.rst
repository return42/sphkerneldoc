.. -*- coding: utf-8; mode: rst -*-

.. _API-idr-get-next:

============
idr_get_next
============

*man idr_get_next(9)*

*4.6.0-rc5*

lookup next object of id to given id.


Synopsis
========

.. c:function:: void * idr_get_next( struct idr * idp, int * nextidp )

Arguments
=========

``idp``
    idr handle

``nextidp``
    pointer to lookup key


Description
===========

Returns pointer to registered object with id, which is next number to
given id. After being looked up, *\ ``nextidp`` will be updated for the
next iteration.

This function can be called under ``rcu_read_lock``, given that the leaf
pointers lifetimes are correctly managed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
