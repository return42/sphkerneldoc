.. -*- coding: utf-8; mode: rst -*-

.. _API-cdev-add:

========
cdev_add
========

*man cdev_add(9)*

*4.6.0-rc5*

add a char device to the system


Synopsis
========

.. c:function:: int cdev_add( struct cdev * p, dev_t dev, unsigned count )

Arguments
=========

``p``
    the cdev structure for the device

``dev``
    the first device number for which this device is responsible

``count``
    the number of consecutive minor numbers corresponding to this device


Description
===========

``cdev_add`` adds the device represented by ``p`` to the system, making
it live immediately. A negative error code is returned on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
