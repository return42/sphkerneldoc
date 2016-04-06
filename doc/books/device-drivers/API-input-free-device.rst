
.. _API-input-free-device:

=================
input_free_device
=================

*man input_free_device(9)*

*4.6.0-rc1*

free memory occupied by input_dev structure


Synopsis
========

.. c:function:: void input_free_device( struct input_dev * dev )

Arguments
=========

``dev``
    input device to free


Description
===========

This function should only be used if ``input_register_device`` was not called yet or if it failed. Once device was registered use ``input_unregister_device`` and memory will be
freed once last reference to the device is dropped.

Device should be allocated by ``input_allocate_device``.


NOTE
====

If there are references to the input device then memory will not be freed until last reference is dropped.
