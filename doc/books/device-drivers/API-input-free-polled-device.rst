
.. _API-input-free-polled-device:

========================
input_free_polled_device
========================

*man input_free_polled_device(9)*

*4.6.0-rc1*

free memory allocated for polled device


Synopsis
========

.. c:function:: void input_free_polled_device( struct input_polled_dev * dev )

Arguments
=========

``dev``
    device to free


Description
===========

The function frees memory allocated for polling device and drops reference to the associated input device.
