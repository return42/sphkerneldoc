.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_twsi.c

.. _`i2c_wait_for_writes`:

i2c_wait_for_writes
===================

.. c:function:: void i2c_wait_for_writes(struct qib_devdata *dd)

    wait for a write

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`i2c_wait_for_writes.description`:

Description
-----------

We use this instead of udelay directly, so we can make sure
that previous register writes have been flushed all the way
to the chip.  Since we are delaying anyway, the cost doesn't
hurt, and makes the bit twiddling more regular

.. _`i2c_ackrcv`:

i2c_ackrcv
==========

.. c:function:: int i2c_ackrcv(struct qib_devdata *dd)

    see if ack following write is true

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`rd_byte`:

rd_byte
=======

.. c:function:: int rd_byte(struct qib_devdata *dd, int last)

    read a byte, sending STOP on last, else ACK

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param last:
        *undescribed*
    :type last: int

.. _`rd_byte.description`:

Description
-----------

Returns byte shifted out of device

.. _`wr_byte`:

wr_byte
=======

.. c:function:: int wr_byte(struct qib_devdata *dd, u8 data)

    write a byte, one bit at a time

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

    :param data:
        the byte to write
    :type data: u8

.. _`wr_byte.description`:

Description
-----------

Returns 0 if we got the following ack, otherwise 1

.. _`stop_seq`:

stop_seq
========

.. c:function:: void stop_seq(struct qib_devdata *dd)

    transmit the stop sequence

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`stop_seq.description`:

Description
-----------

(both clock/data low, clock high, data high while clock is high)

.. _`stop_cmd`:

stop_cmd
========

.. c:function:: void stop_cmd(struct qib_devdata *dd)

    transmit the stop condition

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. _`stop_cmd.description`:

Description
-----------

(both clock/data low, clock high, data high while clock is high)

.. _`qib_twsi_reset`:

qib_twsi_reset
==============

.. c:function:: int qib_twsi_reset(struct qib_devdata *dd)

    reset I2C communication

    :param dd:
        the qlogic_ib device
    :type dd: struct qib_devdata \*

.. This file was automatic generated / don't edit.

