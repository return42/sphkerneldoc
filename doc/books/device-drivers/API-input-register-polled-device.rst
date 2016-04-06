
.. _API-input-register-polled-device:

============================
input_register_polled_device
============================

*man input_register_polled_device(9)*

*4.6.0-rc1*

register polled device


Synopsis
========

.. c:function:: int input_register_polled_device( struct input_polled_dev * dev )

Arguments
=========

``dev``
    device to register


Description
===========

The function registers previously initialized polled input device with input layer. The device should be allocated with call to ``input_allocate_polled_device``. Callers should
also set up ``poll`` method and set up capabilities (id, name, phys, bits) of the corresponding input_dev structure.
