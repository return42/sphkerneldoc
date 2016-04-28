.. -*- coding: utf-8; mode: rst -*-

.. _API-input-free-polled-device:

========================
input_free_polled_device
========================

*man input_free_polled_device(9)*

*4.6.0-rc5*

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

The function frees memory allocated for polling device and drops
reference to the associated input device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
