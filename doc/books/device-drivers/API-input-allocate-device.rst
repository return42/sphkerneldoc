.. -*- coding: utf-8; mode: rst -*-

.. _API-input-allocate-device:

=====================
input_allocate_device
=====================

*man input_allocate_device(9)*

*4.6.0-rc5*

allocate memory for new input device


Synopsis
========

.. c:function:: struct input_dev * input_allocate_device( void )

Arguments
=========

``void``
    no arguments


Description
===========

Returns prepared struct input_dev or ``NULL``.


NOTE
====

Use ``input_free_device`` to free devices that have not been registered;
``input_unregister_device`` should be used for already registered
devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
