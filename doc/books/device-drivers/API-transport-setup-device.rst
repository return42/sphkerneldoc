
.. _API-transport-setup-device:

======================
transport_setup_device
======================

*man transport_setup_device(9)*

*4.6.0-rc1*

declare a new dev for transport class association but don't make it visible yet.


Synopsis
========

.. c:function:: void transport_setup_device( struct device * dev )

Arguments
=========

``dev``
    the generic device representing the entity being added


Description
===========

Usually, dev represents some component in the HBA system (either the HBA itself or a device remote across the HBA bus). This routine is simply a trigger point to see if any set of
transport classes wishes to associate with the added device. This allocates storage for the class device and initialises it, but does not yet add it to the system or add attributes
to it (you do this with transport_add_device). If you have no need for a separate setup and add operations, use transport_register_device (see transport_class.h).
