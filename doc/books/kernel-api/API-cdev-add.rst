
.. _API-cdev-add:

========
cdev_add
========

*man cdev_add(9)*

*4.6.0-rc1*

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

``cdev_add`` adds the device represented by ``p`` to the system, making it live immediately. A negative error code is returned on failure.
