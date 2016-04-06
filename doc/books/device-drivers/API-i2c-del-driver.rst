
.. _API-i2c-del-driver:

==============
i2c_del_driver
==============

*man i2c_del_driver(9)*

*4.6.0-rc1*

unregister I2C driver


Synopsis
========

.. c:function:: void i2c_del_driver( struct i2c_driver * driver )

Arguments
=========

``driver``
    the driver being unregistered


Context
=======

can sleep
