
.. _API-input-allocate-polled-device:

============================
input_allocate_polled_device
============================

*man input_allocate_polled_device(9)*

*4.6.0-rc1*

allocate memory for polled device


Synopsis
========

.. c:function:: struct input_polled_dev ⋆ input_allocate_polled_device( void )

Arguments
=========

``void``
    no arguments


Description
===========

The function allocates memory for a polled device and also for an input device associated with this polled device.
