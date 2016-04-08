
.. _API-maple-driver-unregister:

=======================
maple_driver_unregister
=======================

*man maple_driver_unregister(9)*

*4.6.0-rc1*

unregister a maple driver.


Synopsis
========

.. c:function:: void maple_driver_unregister( struct maple_driver * drv )

Arguments
=========

``drv``
    maple driver to unregister.


Description
===========

Cleans up after ``maple_driver_register``. To be invoked in the exit path of any module drivers.
