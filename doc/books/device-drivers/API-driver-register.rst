
.. _API-driver-register:

===============
driver_register
===============

*man driver_register(9)*

*4.6.0-rc1*

register driver with bus


Synopsis
========

.. c:function:: int driver_register( struct device_driver * drv )

Arguments
=========

``drv``
    driver to register


Description
===========

We pass off most of the work to the ``bus_add_driver`` call, since most of the things we have to do deal with the bus structures.
