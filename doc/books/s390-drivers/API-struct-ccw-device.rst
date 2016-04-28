.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ccw-device:

=================
struct ccw_device
=================

*man struct ccw_device(9)*

*4.6.0-rc5*

channel attached device


Synopsis
========

.. code-block:: c

    struct ccw_device {
      spinlock_t * ccwlock;
      struct ccw_device_id id;
      struct ccw_driver * drv;
      struct device dev;
      int online;
      void (* handler) (struct ccw_device *, unsigned long, struct irb *);
    };


Members
=======

ccwlock
    pointer to device lock

id
    id of this device

drv
    ccw driver for this device

dev
    embedded device structure

online
    online status of device

handler
    interrupt handler


Description
===========

``handler`` is a member of the device rather than the driver since a
driver can have different interrupt handlers for different ccw devices
(multi-subchannel drivers).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
