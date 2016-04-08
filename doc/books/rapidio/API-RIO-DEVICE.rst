
.. _API-RIO-DEVICE:

==========
RIO_DEVICE
==========

*man RIO_DEVICE(9)*

*4.6.0-rc1*

macro used to describe a specific RIO device


Synopsis
========

.. c:function:: RIO_DEVICE( dev, ven )

Arguments
=========

``dev``
    the 16 bit RIO device ID

``ven``
    the 16 bit RIO vendor ID


Description
===========

This macro is used to create a struct rio_device_id that matches a specific device. The assembly vendor and assembly device fields will be set to ``RIO_ANY_ID``.
