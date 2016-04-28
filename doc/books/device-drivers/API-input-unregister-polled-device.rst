.. -*- coding: utf-8; mode: rst -*-

.. _API-input-unregister-polled-device:

==============================
input_unregister_polled_device
==============================

*man input_unregister_polled_device(9)*

*4.6.0-rc5*

unregister polled device


Synopsis
========

.. c:function:: void input_unregister_polled_device( struct input_polled_dev * dev )

Arguments
=========

``dev``
    device to unregister


Description
===========

The function unregisters previously registered polled input device from
input layer. Polling is stopped and device is ready to be freed with
call to ``input_free_polled_device``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
