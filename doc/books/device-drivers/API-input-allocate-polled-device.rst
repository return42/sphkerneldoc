.. -*- coding: utf-8; mode: rst -*-

.. _API-input-allocate-polled-device:

============================
input_allocate_polled_device
============================

*man input_allocate_polled_device(9)*

*4.6.0-rc5*

allocate memory for polled device


Synopsis
========

.. c:function:: struct input_polled_dev * input_allocate_polled_device( void )

Arguments
=========

``void``
    no arguments


Description
===========

The function allocates memory for a polled device and also for an input
device associated with this polled device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
