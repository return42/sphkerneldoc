
.. _API-transport-destroy-device:

========================
transport_destroy_device
========================

*man transport_destroy_device(9)*

*4.6.0-rc1*

destroy a removed device


Synopsis
========

.. c:function:: void transport_destroy_device( struct device * dev )

Arguments
=========

``dev``
    device to eliminate from the transport class.


Description
===========

This call triggers the elimination of storage associated with the transport classdev. Note: all it really does is relinquish a reference to the classdev. The memory will not be
freed until the last reference goes to zero. Note also that the classdev retains a reference count on dev, so dev too will remain for as long as the transport class device remains
around.
