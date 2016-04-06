
.. _API-driver-create-file:

==================
driver_create_file
==================

*man driver_create_file(9)*

*4.6.0-rc1*

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
