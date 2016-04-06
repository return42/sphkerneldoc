
.. _API-usb-ifnum-to-if:

===============
usb_ifnum_to_if
===============

*man usb_ifnum_to_if(9)*

*4.6.0-rc1*

get the interface object with a given interface number


Synopsis
========

.. c:function:: struct usb_interface ⋆ usb_ifnum_to_if( const struct usb_device * dev, unsigned ifnum )

Arguments
=========

``dev``
    the device whose current configuration is considered

``ifnum``
    the desired interface


Description
===========

This walks the device descriptor for the currently active configuration to find the interface object with the particular interface number.

Note that configuration descriptors are not required to assign interface numbers sequentially, so that it would be incorrect to assume that the first interface in that descriptor
corresponds to interface zero. This routine helps device drivers avoid such mistakes. However, you should make sure that you do the right thing with any alternate settings
available for this interfaces.

Don't call this function unless you are bound to one of the interfaces on this device or you have locked the device!


Return
======

A pointer to the interface that has ``ifnum`` as interface number, if found. ``NULL`` otherwise.
