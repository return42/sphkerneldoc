
.. _API-i2c-unregister-device:

=====================
i2c_unregister_device
=====================

*man i2c_unregister_device(9)*

*4.6.0-rc1*

reverse effect of ``i2c_new_device``


Synopsis
========

.. c:function:: void i2c_unregister_device( struct i2c_client * client )

Arguments
=========

``client``
    value returned from ``i2c_new_device``


Context
=======

can sleep
