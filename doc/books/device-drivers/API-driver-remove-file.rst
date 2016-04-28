.. -*- coding: utf-8; mode: rst -*-

.. _API-driver-remove-file:

==================
driver_remove_file
==================

*man driver_remove_file(9)*

*4.6.0-rc5*

remove sysfs file for driver.


Synopsis
========

.. c:function:: void driver_remove_file( struct device_driver * drv, const struct driver_attribute * attr )

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
