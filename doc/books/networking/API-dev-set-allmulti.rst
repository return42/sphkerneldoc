
.. _API-dev-set-allmulti:

================
dev_set_allmulti
================

*man dev_set_allmulti(9)*

*4.6.0-rc1*

update allmulti count on a device


Synopsis
========

.. c:function:: int dev_set_allmulti( struct net_device * dev, int inc )

Arguments
=========

``dev``
    device

``inc``
    modifier


Description
===========

Add or remove reception of all multicast frames to a device. While the count in the device remains above zero the interface remains listening to all interfaces. Once it hits zero
the device reverts back to normal filtering operation. A negative ``inc`` value is used to drop the counter when releasing a resource needing all multicasts. Return 0 if successful
or a negative errno code on error.
