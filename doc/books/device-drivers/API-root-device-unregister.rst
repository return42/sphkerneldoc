.. -*- coding: utf-8; mode: rst -*-

.. _API-root-device-unregister:

======================
root_device_unregister
======================

*man root_device_unregister(9)*

*4.6.0-rc5*

unregister and free a root device


Synopsis
========

.. c:function:: void root_device_unregister( struct device * dev )

Arguments
=========

``dev``
    device going away


Description
===========

This function unregisters and cleans up a device that was created by
``root_device_register``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
