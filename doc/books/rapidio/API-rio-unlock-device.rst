
.. _API-rio-unlock-device:

=================
rio_unlock_device
=================

*man rio_unlock_device(9)*

*4.6.0-rc1*

Releases host device lock for specified device


Synopsis
========

.. c:function:: int rio_unlock_device( struct rio_mport * port, u16 destid, u8 hopcount )

Arguments
=========

``port``
    Master port to send transaction

``destid``
    Destination ID for device/switch

``hopcount``
    Hopcount to reach switch


Description
===========

Returns 0 if device lock released or EINVAL if fails.
