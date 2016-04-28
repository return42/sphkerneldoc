.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-unregister-device:

=====================
snd_unregister_device
=====================

*man snd_unregister_device(9)*

*4.6.0-rc5*

unregister the device on the given card


Synopsis
========

.. c:function:: int snd_unregister_device( struct device * dev )

Arguments
=========

``dev``
    the device instance


Description
===========

Unregisters the device file already registered via
``snd_register_device``.


Return
======

Zero if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
