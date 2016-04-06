
.. _API-parport-unregister-device:

=========================
parport_unregister_device
=========================

*man parport_unregister_device(9)*

*4.6.0-rc1*

deregister a device on a parallel port


Synopsis
========

.. c:function:: void parport_unregister_device( struct pardevice * dev )

Arguments
=========

``dev``
    pointer to structure representing device


Description
===========

This undoes the effect of ``parport_register_device``.
