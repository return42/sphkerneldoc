.. -*- coding: utf-8; mode: rst -*-

.. _API-input-register-device:

=====================
input_register_device
=====================

*man input_register_device(9)*

*4.6.0-rc5*

register device with input core


Synopsis
========

.. c:function:: int input_register_device( struct input_dev * dev )

Arguments
=========

``dev``
    device to be registered


Description
===========

This function registers device with input core. The device must be
allocated with ``input_allocate_device`` and all it's capabilities set
up before registering. If function fails the device must be freed with
``input_free_device``. Once device has been successfully registered it
can be unregistered with ``input_unregister_device``;
``input_free_device`` should not be called in this case.

Note that this function is also used to register managed input devices
(ones allocated with ``devm_input_allocate_device``). Such managed input
devices need not be explicitly unregistered or freed, their tear down is
controlled by the devres infrastructure. It is also worth noting that
tear down of managed input devices is internally a 2-step process:
registered managed input device is first unregistered, but stays in
memory and can still handle ``input_event`` calls (although events will
not be delivered anywhere). The freeing of managed input device will
happen later, when devres stack is unwound to the point where device
allocation was made.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
