
.. _API-ccwgroup-set-online:

===================
ccwgroup_set_online
===================

*man ccwgroup_set_online(9)*

*4.6.0-rc1*

enable a ccwgroup device


Synopsis
========

.. c:function:: int ccwgroup_set_online( struct ccwgroup_device * gdev )

Arguments
=========

``gdev``
    target ccwgroup device


Description
===========

This function attempts to put the ccwgroup device into the online state.


Returns
=======

``0`` on success and a negative error value on failure.
