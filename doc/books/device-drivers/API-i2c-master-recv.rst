
.. _API-i2c-master-recv:

===============
i2c_master_recv
===============

*man i2c_master_recv(9)*

*4.6.0-rc1*

issue a single I2C message in master receive mode


Synopsis
========

.. c:function:: int i2c_master_recv( const struct i2c_client * client, char * buf, int count )

Arguments
=========

``client``
    Handle to slave device

``buf``
    Where to store data read from slave

``count``
    How many bytes to read, must be less than 64k since msg.len is u16


Description
===========

Returns negative errno, or else the number of bytes read.
