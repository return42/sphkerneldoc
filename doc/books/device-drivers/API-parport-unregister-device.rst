.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-unregister-device:

=========================
parport_unregister_device
=========================

*man parport_unregister_device(9)*

*4.6.0-rc5*

deregister a device on a parallel port


Synopsis
========

.. c:function:: void parport_unregister_device( struct pardevice * dev )

Arguments
=========

``dev``
    pointer to structure representing device


Description
===========

This undoes the effect of ``parport_register_device``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
