.. -*- coding: utf-8; mode: rst -*-

.. _API-input-unregister-device:

=======================
input_unregister_device
=======================

*man input_unregister_device(9)*

*4.6.0-rc5*

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

This function unregisters an input device. Once device is unregistered
the caller should not try to access it as it may get freed at any
moment.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
