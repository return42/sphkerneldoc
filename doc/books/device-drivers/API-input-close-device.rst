
.. _API-input-close-device:

==================
input_close_device
==================

*man input_close_device(9)*

*4.6.0-rc1*

close input device


Synopsis
========

.. c:function:: void input_close_device( struct input_handle * handle )

Arguments
=========

``handle``
    handle through which device is being accessed


Description
===========

This function should be called by input handlers when they want to stop receive events from given input device.
