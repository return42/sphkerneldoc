
.. _API-i2c-master-send:

===============
i2c_master_send
===============

*man i2c_master_send(9)*

*4.6.0-rc1*

issue a single I2C message in master transmit mode


Synopsis
========

.. c:function:: int i2c_master_send( const struct i2c_client * client, const char * buf, int count )

Arguments
=========

``client``
    Handle to slave device

``buf``
    Data that will be written to the slave

``count``
    How many bytes to write, must be less than 64k since msg.len is u16


Description
===========

Returns negative errno, or else the number of bytes written.
