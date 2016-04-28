.. -*- coding: utf-8; mode: rst -*-

.. _API-driver-create-file:

==================
driver_create_file
==================

*man driver_create_file(9)*

*4.6.0-rc5*

create sysfs file for driver.


Synopsis
========

.. c:function:: int driver_create_file( struct device_driver * drv, const struct driver_attribute * attr )

Arguments
=========

``drv``
    driver.

``attr``
    driver attribute descriptor.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
