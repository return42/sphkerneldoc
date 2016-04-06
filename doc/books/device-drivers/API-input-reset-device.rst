
.. _API-input-reset-device:

==================
input_reset_device
==================

*man input_reset_device(9)*

*4.6.0-rc1*

reset/restore the state of input device


Synopsis
========

.. c:function:: void input_reset_device( struct input_dev * dev )

Arguments
=========

``dev``
    input device whose state needs to be reset


Description
===========

This function tries to reset the state of an opened input device and bring internal state and state if the hardware in sync with each other. We mark all keys as released, restore
LED state, repeat rate, etc.
