
.. _API-dev-set-promiscuity:

===================
dev_set_promiscuity
===================

*man dev_set_promiscuity(9)*

*4.6.0-rc1*

update promiscuity count on a device


Synopsis
========

.. c:function:: int dev_set_promiscuity( struct net_device * dev, int inc )

Arguments
=========

``dev``
    device

``inc``
    modifier


Description
===========

Add or remove promiscuity from a device. While the count in the device remains above zero the interface remains promiscuous. Once it hits zero the device reverts back to normal
filtering operation. A negative inc value is used to drop promiscuity on the device. Return 0 if successful or a negative errno code on error.
