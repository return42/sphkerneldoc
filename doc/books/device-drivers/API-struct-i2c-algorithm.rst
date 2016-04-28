.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-i2c-algorithm:

====================
struct i2c_algorithm
====================

*man struct i2c_algorithm(9)*

*4.6.0-rc5*

represent I2C transfer method


Synopsis
========

.. code-block:: c

    struct i2c_algorithm {
      int (* master_xfer) (struct i2c_adapter *adap, struct i2c_msg *msgs,int num);
      int (* smbus_xfer) (struct i2c_adapter *adap, u16 addr,unsigned short flags, char read_write,u8 command, int size, union i2c_smbus_data *data);
      u32 (* functionality) (struct i2c_adapter *);
    #if IS_ENABLED(CONFIG_I2C_SLAVE)
      int (* reg_slave) (struct i2c_client *client);
      int (* unreg_slave) (struct i2c_client *client);
    #endif
    };


Members
=======

master_xfer
    Issue a set of i2c transactions to the given I2C adapter defined by
    the msgs array, with num messages available to transfer via the
    adapter specified by adap.

smbus_xfer
    Issue smbus transactions to the given I2C adapter. If this is not
    present, then the bus layer will try and convert the SMBus calls
    into I2C transfers instead.

functionality
    Return the flags that this algorithm/adapter pair supports from the
    I2C_FUNC_* flags.

reg_slave
    Register given client to I2C slave mode of this adapter

unreg_slave
    Unregister given client from I2C slave mode of this adapter


The following structs are for those who like to implement new bus drivers
=========================================================================

i2c_algorithm is the interface to a class of hardware solutions which
can be addressed using the same bus algorithms - i.e. bit-banging or the
PCF8584 to name two of the most common.

The return codes from the ``master_xfer`` field should indicate the type
of error code that occurred during the transfer, as documented in the
kernel Documentation file Documentation/i2c/fault-codes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
