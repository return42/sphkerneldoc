.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/i2c-core-smbus.c

.. _`i2c_smbus_read_byte`:

i2c_smbus_read_byte
===================

.. c:function:: s32 i2c_smbus_read_byte(const struct i2c_client *client)

    SMBus "receive byte" protocol

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

.. _`i2c_smbus_read_byte.description`:

Description
-----------

This executes the SMBus "receive byte" protocol, returning negative errno
else the byte received from the device.

.. _`i2c_smbus_write_byte`:

i2c_smbus_write_byte
====================

.. c:function:: s32 i2c_smbus_write_byte(const struct i2c_client *client, u8 value)

    SMBus "send byte" protocol

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param value:
        Byte to be sent
    :type value: u8

.. _`i2c_smbus_write_byte.description`:

Description
-----------

This executes the SMBus "send byte" protocol, returning negative errno
else zero on success.

.. _`i2c_smbus_read_byte_data`:

i2c_smbus_read_byte_data
========================

.. c:function:: s32 i2c_smbus_read_byte_data(const struct i2c_client *client, u8 command)

    SMBus "read byte" protocol

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param command:
        Byte interpreted by slave
    :type command: u8

.. _`i2c_smbus_read_byte_data.description`:

Description
-----------

This executes the SMBus "read byte" protocol, returning negative errno
else a data byte received from the device.

.. _`i2c_smbus_write_byte_data`:

i2c_smbus_write_byte_data
=========================

.. c:function:: s32 i2c_smbus_write_byte_data(const struct i2c_client *client, u8 command, u8 value)

    SMBus "write byte" protocol

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param command:
        Byte interpreted by slave
    :type command: u8

    :param value:
        Byte being written
    :type value: u8

.. _`i2c_smbus_write_byte_data.description`:

Description
-----------

This executes the SMBus "write byte" protocol, returning negative errno
else zero on success.

.. _`i2c_smbus_read_word_data`:

i2c_smbus_read_word_data
========================

.. c:function:: s32 i2c_smbus_read_word_data(const struct i2c_client *client, u8 command)

    SMBus "read word" protocol

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param command:
        Byte interpreted by slave
    :type command: u8

.. _`i2c_smbus_read_word_data.description`:

Description
-----------

This executes the SMBus "read word" protocol, returning negative errno
else a 16-bit unsigned "word" received from the device.

.. _`i2c_smbus_write_word_data`:

i2c_smbus_write_word_data
=========================

.. c:function:: s32 i2c_smbus_write_word_data(const struct i2c_client *client, u8 command, u16 value)

    SMBus "write word" protocol

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param command:
        Byte interpreted by slave
    :type command: u8

    :param value:
        16-bit "word" being written
    :type value: u16

.. _`i2c_smbus_write_word_data.description`:

Description
-----------

This executes the SMBus "write word" protocol, returning negative errno
else zero on success.

.. _`i2c_smbus_read_block_data`:

i2c_smbus_read_block_data
=========================

.. c:function:: s32 i2c_smbus_read_block_data(const struct i2c_client *client, u8 command, u8 *values)

    SMBus "block read" protocol

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param command:
        Byte interpreted by slave
    :type command: u8

    :param values:
        Byte array into which data will be read; big enough to hold
        the data returned by the slave.  SMBus allows at most 32 bytes.
    :type values: u8 \*

.. _`i2c_smbus_read_block_data.description`:

Description
-----------

This executes the SMBus "block read" protocol, returning negative errno
else the number of data bytes in the slave's response.

Note that using this function requires that the client's adapter support
the I2C_FUNC_SMBUS_READ_BLOCK_DATA functionality.  Not all adapter drivers
support this; its emulation through I2C messaging relies on a specific
mechanism (I2C_M_RECV_LEN) which may not be implemented.

.. _`i2c_smbus_write_block_data`:

i2c_smbus_write_block_data
==========================

.. c:function:: s32 i2c_smbus_write_block_data(const struct i2c_client *client, u8 command, u8 length, const u8 *values)

    SMBus "block write" protocol

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param command:
        Byte interpreted by slave
    :type command: u8

    :param length:
        Size of data block; SMBus allows at most 32 bytes
    :type length: u8

    :param values:
        Byte array which will be written.
    :type values: const u8 \*

.. _`i2c_smbus_write_block_data.description`:

Description
-----------

This executes the SMBus "block write" protocol, returning negative errno
else zero on success.

.. _`i2c_smbus_xfer`:

i2c_smbus_xfer
==============

.. c:function:: s32 i2c_smbus_xfer(struct i2c_adapter *adapter, u16 addr, unsigned short flags, char read_write, u8 command, int protocol, union i2c_smbus_data *data)

    execute SMBus protocol operations

    :param adapter:
        Handle to I2C bus
    :type adapter: struct i2c_adapter \*

    :param addr:
        Address of SMBus slave on that bus
    :type addr: u16

    :param flags:
        I2C_CLIENT_* flags (usually zero or I2C_CLIENT_PEC)
    :type flags: unsigned short

    :param read_write:
        I2C_SMBUS_READ or I2C_SMBUS_WRITE
    :type read_write: char

    :param command:
        Byte interpreted by slave, for protocols which use such bytes
    :type command: u8

    :param protocol:
        SMBus protocol operation to execute, such as I2C_SMBUS_PROC_CALL
    :type protocol: int

    :param data:
        Data to be read or written
    :type data: union i2c_smbus_data \*

.. _`i2c_smbus_xfer.description`:

Description
-----------

This executes an SMBus protocol operation, and returns a negative
errno code else zero on success.

.. _`i2c_smbus_read_i2c_block_data_or_emulated`:

i2c_smbus_read_i2c_block_data_or_emulated
=========================================

.. c:function:: s32 i2c_smbus_read_i2c_block_data_or_emulated(const struct i2c_client *client, u8 command, u8 length, u8 *values)

    read block or emulate

    :param client:
        Handle to slave device
    :type client: const struct i2c_client \*

    :param command:
        Byte interpreted by slave
    :type command: u8

    :param length:
        Size of data block; SMBus allows at most I2C_SMBUS_BLOCK_MAX bytes
    :type length: u8

    :param values:
        Byte array into which data will be read; big enough to hold
        the data returned by the slave.  SMBus allows at most
        I2C_SMBUS_BLOCK_MAX bytes.
    :type values: u8 \*

.. _`i2c_smbus_read_i2c_block_data_or_emulated.description`:

Description
-----------

This executes the SMBus "block read" protocol if supported by the adapter.
If block read is not supported, it emulates it using either word or byte
read protocols depending on availability.

The addresses of the I2C slave device that are accessed with this function
must be mapped to a linear region, so that a block read will have the same
effect as a byte read. Before using this function you must double-check
if the I2C slave does support exchanging a block transfer with a byte
transfer.

.. _`i2c_setup_smbus_alert`:

i2c_setup_smbus_alert
=====================

.. c:function:: struct i2c_client *i2c_setup_smbus_alert(struct i2c_adapter *adapter, struct i2c_smbus_alert_setup *setup)

    Setup SMBus alert support

    :param adapter:
        the target adapter
    :type adapter: struct i2c_adapter \*

    :param setup:
        setup data for the SMBus alert handler
    :type setup: struct i2c_smbus_alert_setup \*

.. _`i2c_setup_smbus_alert.context`:

Context
-------

can sleep

.. _`i2c_setup_smbus_alert.description`:

Description
-----------

Setup handling of the SMBus alert protocol on a given I2C bus segment.

Handling can be done either through our IRQ handler, or by the
adapter (from its handler, periodic polling, or whatever).

NOTE that if we manage the IRQ, we *MUST* know if it's level or
edge triggered in order to hand it to the workqueue correctly.
If triggering the alert seems to wedge the system, you probably
should have said it's level triggered.

This returns the ara client, which should be saved for later use with
\ :c:func:`i2c_handle_smbus_alert`\  and ultimately \ :c:func:`i2c_unregister_device`\ ; or NULL
to indicate an error.

.. This file was automatic generated / don't edit.

