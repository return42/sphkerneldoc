.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usbdrv-wrap:

==================
struct usbdrv_wrap
==================

*man struct usbdrv_wrap(9)*

*4.6.0-rc5*

wrapper for driver-model structure


Synopsis
========

.. code-block:: c

    struct usbdrv_wrap {
      struct device_driver driver;
      int for_devices;
    };


Members
=======

driver
    The driver-model core driver structure.

for_devices
    Non-zero for device drivers, 0 for interface drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
