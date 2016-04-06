
.. _API-driver-remove-file:

==================
driver_remove_file
==================

*man driver_remove_file(9)*

*4.6.0-rc1*

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
