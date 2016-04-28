.. -*- coding: utf-8; mode: rst -*-

.. _API-i2c-transfer:

============
i2c_transfer
============

*man i2c_transfer(9)*

*4.6.0-rc5*

execute a single or combined I2C message


Synopsis
========

.. c:function:: int i2c_transfer( struct i2c_adapter * adap, struct i2c_msg * msgs, int num )

Arguments
=========

``adap``
    Handle to I2C bus

``msgs``
    One or more messages to execute before STOP is issued to terminate
    the operation; each message begins with a START.

``num``
    Number of messages to be executed.


Description
===========

Returns negative errno, else the number of messages executed.

Note that there is no requirement that each message be sent to the same
slave address, although that is the most common model.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
