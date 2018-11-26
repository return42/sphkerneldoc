.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-octeon-core.c

.. _`octeon_i2c_wait`:

octeon_i2c_wait
===============

.. c:function:: int octeon_i2c_wait(struct octeon_i2c *i2c)

    wait for the IFLG to be set

    :param i2c:
        The struct octeon_i2c
    :type i2c: struct octeon_i2c \*

.. _`octeon_i2c_wait.description`:

Description
-----------

Returns 0 on success, otherwise a negative errno.

.. _`octeon_i2c_hlc_wait`:

octeon_i2c_hlc_wait
===================

.. c:function:: int octeon_i2c_hlc_wait(struct octeon_i2c *i2c)

    wait for an HLC operation to complete

    :param i2c:
        The struct octeon_i2c
    :type i2c: struct octeon_i2c \*

.. _`octeon_i2c_hlc_wait.description`:

Description
-----------

Returns 0 on success, otherwise -ETIMEDOUT.

.. _`octeon_i2c_start`:

octeon_i2c_start
================

.. c:function:: int octeon_i2c_start(struct octeon_i2c *i2c)

    send START to the bus

    :param i2c:
        The struct octeon_i2c
    :type i2c: struct octeon_i2c \*

.. _`octeon_i2c_start.description`:

Description
-----------

Returns 0 on success, otherwise a negative errno.

.. _`octeon_i2c_read`:

octeon_i2c_read
===============

.. c:function:: int octeon_i2c_read(struct octeon_i2c *i2c, int target, u8 *data, u16 *rlength, bool recv_len)

    receive data from the bus via low-level controller

    :param i2c:
        The struct octeon_i2c
    :type i2c: struct octeon_i2c \*

    :param target:
        Target address
    :type target: int

    :param data:
        Pointer to the location to store the data
    :type data: u8 \*

    :param rlength:
        Length of the data
    :type rlength: u16 \*

    :param recv_len:
        flag for length byte
    :type recv_len: bool

.. _`octeon_i2c_read.description`:

Description
-----------

The address is sent over the bus, then the data is read.

Returns 0 on success, otherwise a negative errno.

.. _`octeon_i2c_write`:

octeon_i2c_write
================

.. c:function:: int octeon_i2c_write(struct octeon_i2c *i2c, int target, const u8 *data, int length)

    send data to the bus via low-level controller

    :param i2c:
        The struct octeon_i2c
    :type i2c: struct octeon_i2c \*

    :param target:
        Target address
    :type target: int

    :param data:
        Pointer to the data to be sent
    :type data: const u8 \*

    :param length:
        Length of the data
    :type length: int

.. _`octeon_i2c_write.description`:

Description
-----------

The address is sent over the bus, then the data.

Returns 0 on success, otherwise a negative errno.

.. _`octeon_i2c_xfer`:

octeon_i2c_xfer
===============

.. c:function:: int octeon_i2c_xfer(struct i2c_adapter *adap, struct i2c_msg *msgs, int num)

    The driver's master_xfer function

    :param adap:
        Pointer to the i2c_adapter structure
    :type adap: struct i2c_adapter \*

    :param msgs:
        Pointer to the messages to be processed
    :type msgs: struct i2c_msg \*

    :param num:
        Length of the MSGS array
    :type num: int

.. _`octeon_i2c_xfer.description`:

Description
-----------

Returns the number of messages processed, or a negative errno on failure.

.. This file was automatic generated / don't edit.

