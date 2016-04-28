.. -*- coding: utf-8; mode: rst -*-

.. _API-get-device:

==========
get_device
==========

*man get_device(9)*

*4.6.0-rc5*

increment reference count for device.


Synopsis
========

.. c:function:: struct device * get_device( struct device * dev )

Arguments
=========

``dev``
    device.


Description
===========

This simply forwards the call to ``kobject_get``, though we do take care
to provide for the case that we get a NULL pointer passed in.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
