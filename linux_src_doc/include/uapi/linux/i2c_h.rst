.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/i2c.h

.. _`i2c_msg`:

struct i2c_msg
==============

.. c:type:: struct i2c_msg

    an I2C transaction segment beginning with START

.. _`i2c_msg.definition`:

Definition
----------

.. code-block:: c

    struct i2c_msg {
        __u16 addr;
        __u16 flags;
    #define I2C_M_RD 0x0001
    #define I2C_M_TEN 0x0010
    #define I2C_M_RECV_LEN 0x0400
    #define I2C_M_NO_RD_ACK 0x0800
    #define I2C_M_IGNORE_NAK 0x1000
    #define I2C_M_REV_DIR_ADDR 0x2000
    #define I2C_M_NOSTART 0x4000
    #define I2C_M_STOP 0x8000
        __u16 len;
        __u8 *buf;
    }

.. _`i2c_msg.members`:

Members
-------

addr
    Slave address, either seven or ten bits.  When this is a ten
    bit address, I2C_M_TEN must be set in \ ``flags``\  and the adapter
    must support I2C_FUNC_10BIT_ADDR.

flags
    I2C_M_RD is handled by all adapters.  No other flags may be
    provided unless the adapter exported the relevant I2C_FUNC\_\*
    flags through \ :c:func:`i2c_check_functionality`\ .

len
    Number of data bytes in \ ``buf``\  being read from or written to the
    I2C slave address.  For read transactions where I2C_M_RECV_LEN
    is set, the caller guarantees that this buffer can hold up to
    32 bytes in addition to the initial length byte sent by the
    slave (plus, if used, the SMBus PEC); and this value will be
    incremented by the number of block data bytes received.

buf
    The buffer into which data is read, or from which it's written.

.. _`i2c_msg.description`:

Description
-----------

An i2c_msg is the low level representation of one segment of an I2C
transaction.  It is visible to drivers in the \ ``i2c_transfer``\ () procedure,
to userspace from i2c-dev, and to I2C adapter drivers through the
\ ``i2c_adapter``\ .@master_xfer() method.

Except when I2C "protocol mangling" is used, all I2C adapters implement
the standard rules for I2C transactions.  Each transaction begins with a
START.  That is followed by the slave address, and a bit encoding read
versus write.  Then follow all the data bytes, possibly including a byte
with SMBus PEC.  The transfer terminates with a NAK, or when all those
bytes have been transferred and ACKed.  If this is the last message in a
group, it is followed by a STOP.  Otherwise it is followed by the next
\ ``i2c_msg``\  transaction segment, beginning with a (repeated) START.

Alternatively, when the adapter supports I2C_FUNC_PROTOCOL_MANGLING then
passing certain \ ``flags``\  may have changed those standard protocol behaviors.
Those flags are only for use with broken/nonconforming slaves, and with
adapters which are known to support the specific mangling options they
need (one or more of IGNORE_NAK, NO_RD_ACK, NOSTART, and REV_DIR_ADDR).

.. This file was automatic generated / don't edit.

