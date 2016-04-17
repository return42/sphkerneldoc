.. -*- coding: utf-8; mode: rst -*-

============
i2c-octeon.c
============


.. _`octeon_i2c_write_sw`:

octeon_i2c_write_sw
===================

.. c:function:: void octeon_i2c_write_sw (struct octeon_i2c *i2c, u64 eop_reg, u8 data)

    write an I2C core register

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

    :param u64 eop_reg:
        Register selector

    :param u8 data:
        Value to be written



.. _`octeon_i2c_write_sw.description`:

Description
-----------

The I2C core registers are accessed indirectly via the SW_TWSI CSR.



.. _`octeon_i2c_read_sw`:

octeon_i2c_read_sw
==================

.. c:function:: u8 octeon_i2c_read_sw (struct octeon_i2c *i2c, u64 eop_reg)

    read lower bits of an I2C core register

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

    :param u64 eop_reg:
        Register selector



.. _`octeon_i2c_read_sw.description`:

Description
-----------

Returns the data.

The I2C core registers are accessed indirectly via the SW_TWSI CSR.



.. _`octeon_i2c_write_int`:

octeon_i2c_write_int
====================

.. c:function:: void octeon_i2c_write_int (struct octeon_i2c *i2c, u64 data)

    write the TWSI_INT register

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

    :param u64 data:
        Value to be written



.. _`octeon_i2c_int_enable`:

octeon_i2c_int_enable
=====================

.. c:function:: void octeon_i2c_int_enable (struct octeon_i2c *i2c)

    enable the CORE interrupt

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c



.. _`octeon_i2c_int_enable.description`:

Description
-----------

The interrupt will be asserted when there is non-STAT_IDLE state in
the SW_TWSI_EOP_TWSI_STAT register.



.. _`octeon_i2c_unblock`:

octeon_i2c_unblock
==================

.. c:function:: void octeon_i2c_unblock (struct octeon_i2c *i2c)

    unblock the bus

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c



.. _`octeon_i2c_unblock.description`:

Description
-----------

If there was a reset while a device was driving 0 to bus, bus is blocked.
We toggle it free manually by some clock cycles and send a stop.



.. _`octeon_i2c_wait`:

octeon_i2c_wait
===============

.. c:function:: int octeon_i2c_wait (struct octeon_i2c *i2c)

    wait for the IFLG to be set

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c



.. _`octeon_i2c_wait.description`:

Description
-----------

Returns 0 on success, otherwise a negative errno.



.. _`octeon_i2c_start`:

octeon_i2c_start
================

.. c:function:: int octeon_i2c_start (struct octeon_i2c *i2c)

    send START to the bus

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c



.. _`octeon_i2c_start.description`:

Description
-----------

Returns 0 on success, otherwise a negative errno.



.. _`octeon_i2c_write`:

octeon_i2c_write
================

.. c:function:: int octeon_i2c_write (struct octeon_i2c *i2c, int target, const u8 *data, int length)

    send data to the bus via low-level controller

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

    :param int target:
        Target address

    :param const u8 \*data:
        Pointer to the data to be sent

    :param int length:
        Length of the data



.. _`octeon_i2c_write.description`:

Description
-----------

The address is sent over the bus, then the data.

Returns 0 on success, otherwise a negative errno.



.. _`octeon_i2c_read`:

octeon_i2c_read
===============

.. c:function:: int octeon_i2c_read (struct octeon_i2c *i2c, int target, u8 *data, u16 *rlength, bool recv_len)

    receive data from the bus via low-level controller

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

    :param int target:
        Target address

    :param u8 \*data:
        Pointer to the location to store the data

    :param u16 \*rlength:
        Length of the data

    :param bool recv_len:
        flag for length byte



.. _`octeon_i2c_read.description`:

Description
-----------

The address is sent over the bus, then the data is read.

Returns 0 on success, otherwise a negative errno.



.. _`octeon_i2c_xfer`:

octeon_i2c_xfer
===============

.. c:function:: int octeon_i2c_xfer (struct i2c_adapter *adap, struct i2c_msg *msgs, int num)

    The driver's master_xfer function

    :param struct i2c_adapter \*adap:
        Pointer to the i2c_adapter structure

    :param struct i2c_msg \*msgs:
        Pointer to the messages to be processed

    :param int num:
        Length of the MSGS array



.. _`octeon_i2c_xfer.description`:

Description
-----------

Returns the number of messages processed, or a negative errno on failure.

