
.. _API-input-unregister-device:

=======================
input_unregister_device
=======================

*man input_unregister_device(9)*

*4.6.0-rc1*

unregister previously registered device


Synopsis
========

.. c:function:: void input_unregister_device( struct input_dev * dev )

Arguments
=========

``dev``
    device to be unregistered


Description
===========

This function unregisters an input device. Once device is unregistered the caller should not try to access it as it may get freed at any moment.
