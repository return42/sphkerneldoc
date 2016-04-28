.. -*- coding: utf-8; mode: rst -*-

.. _API-input-free-device:

=================
input_free_device
=================

*man input_free_device(9)*

*4.6.0-rc5*

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

This function should only be used if ``input_register_device`` was not
called yet or if it failed. Once device was registered use
``input_unregister_device`` and memory will be freed once last reference
to the device is dropped.

Device should be allocated by ``input_allocate_device``.


NOTE
====

If there are references to the input device then memory will not be
freed until last reference is dropped.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
