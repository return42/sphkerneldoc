.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-device-probe:

================
rio_device_probe
================

*man rio_device_probe(9)*

*4.6.0-rc5*

Tell if a RIO device structure has a matching RIO device id structure


Synopsis
========

.. c:function:: int rio_device_probe( struct device * dev )

Arguments
=========

``dev``
    the RIO device structure to match against


Description
===========

return 0 and set rio_dev->driver when drv claims rio_dev, else error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
