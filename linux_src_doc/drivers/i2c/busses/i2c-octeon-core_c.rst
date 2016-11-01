.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-octeon-core.c

.. _`octeon_i2c_wait`:

octeon_i2c_wait
===============

.. c:function:: int octeon_i2c_wait(struct octeon_i2c *i2c)

    wait for the IFLG to be set

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

.. _`octeon_i2c_wait.description`:

Description
-----------

Returns 0 on success, otherwise a negative errno.

.. _`octeon_i2c_hlc_wait`:

octeon_i2c_hlc_wait
===================

.. c:function:: int octeon_i2c_hlc_wait(struct octeon_i2c *i2c)

    wait for an HLC operation to complete

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

.. _`octeon_i2c_hlc_wait.description`:

Description
-----------

Returns 0 on success, otherwise -ETIMEDOUT.

.. _`octeon_i2c_start`:

octeon_i2c_start
================

.. c:function:: int octeon_i2c_start(struct octeon_i2c *i2c)

    send START to the bus

    :param struct octeon_i2c \*i2c:
        The struct octeon_i2c

.. _`octeon_i2c_start.description`:

Description
-----------

Returns 0 on success, otherwise a negative errno.

.. _`octeon_i2c_read`:

octeon_i2c_read
===============

.. c:function:: int octeon_i2c_read(struct octeon_i2c *i2c, int target, u8 *data, u16 *rlength, bool recv_len)

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

.. _`octeon_i2c_write`:

octeon_i2c_write
================

.. c:function:: int octeon_i2c_write(struct octeon_i2c *i2c, int target, const u8 *data, int length)

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

.. _`octeon_i2c_xfer`:

octeon_i2c_xfer
===============

.. c:function:: int octeon_i2c_xfer(struct i2c_adapter *adap, struct i2c_msg *msgs, int num)

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

.. This file was automatic generated / don't edit.

