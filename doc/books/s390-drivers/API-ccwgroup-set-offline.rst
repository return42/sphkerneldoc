
.. _API-ccwgroup-set-offline:

====================
ccwgroup_set_offline
====================

*man ccwgroup_set_offline(9)*

*4.6.0-rc1*

disable a ccwgroup device


Synopsis
========

.. c:function:: int ccwgroup_set_offline( struct ccwgroup_device * gdev )

Arguments
=========

``gdev``
    target ccwgroup device


Description
===========

This function attempts to put the ccwgroup device into the offline state.


Returns
=======

``0`` on success and a negative error value on failure.
