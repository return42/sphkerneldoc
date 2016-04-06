
.. _API-driver-unregister:

=================
driver_unregister
=================

*man driver_unregister(9)*

*4.6.0-rc1*

remove driver from system.


Synopsis
========

.. c:function:: void driver_unregister( struct device_driver * drv )

Arguments
=========

``drv``
    driver.


Description
===========

Again, we pass off most of the work to the bus-level call.
