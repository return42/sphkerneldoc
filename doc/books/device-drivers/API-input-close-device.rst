.. -*- coding: utf-8; mode: rst -*-

.. _API-input-close-device:

==================
input_close_device
==================

*man input_close_device(9)*

*4.6.0-rc5*

close input device


Synopsis
========

.. c:function:: void input_close_device( struct input_handle * handle )

Arguments
=========

``handle``
    handle through which device is being accessed


Description
===========

This function should be called by input handlers when they want to stop
receive events from given input device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
