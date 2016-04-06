
.. _API-input-open-device:

=================
input_open_device
=================

*man input_open_device(9)*

*4.6.0-rc1*

open input device


Synopsis
========

.. c:function:: int input_open_device( struct input_handle * handle )

Arguments
=========

``handle``
    handle through which device is being accessed


Description
===========

This function should be called by input handlers when they want to start receive events from given input device.
