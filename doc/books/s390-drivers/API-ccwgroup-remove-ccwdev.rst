
.. _API-ccwgroup-remove-ccwdev:

======================
ccwgroup_remove_ccwdev
======================

*man ccwgroup_remove_ccwdev(9)*

*4.6.0-rc1*

remove function for slave devices


Synopsis
========

.. c:function:: void ccwgroup_remove_ccwdev( struct ccw_device * cdev )

Arguments
=========

``cdev``
    ccw device to be removed


Description
===========

This is a remove function for ccw devices that are slave devices in a ccw group device. It sets the ccw device offline and also deregisters the embedding ccw group device.
