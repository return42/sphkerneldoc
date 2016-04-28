.. -*- coding: utf-8; mode: rst -*-

.. _API---i2c-transfer:

==============
__i2c_transfer
==============

*man __i2c_transfer(9)*

*4.6.0-rc5*

unlocked flavor of i2c_transfer


Synopsis
========

.. c:function:: int __i2c_transfer( struct i2c_adapter * adap, struct i2c_msg * msgs, int num )

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

Adapter lock must be held when calling this function. No debug logging
takes place. adap->algo->master_xfer existence isn't checked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
