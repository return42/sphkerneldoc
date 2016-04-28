.. -*- coding: utf-8; mode: rst -*-

.. _API-input-open-device:

=================
input_open_device
=================

*man input_open_device(9)*

*4.6.0-rc5*

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

This function should be called by input handlers when they want to start
receive events from given input device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
