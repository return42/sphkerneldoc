.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-master-recv:

===============
i2c_master_recv
===============

*man i2c_master_recv(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
