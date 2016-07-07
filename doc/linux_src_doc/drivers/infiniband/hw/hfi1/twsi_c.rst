.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/twsi.c

.. _`i2c_wait_for_writes`:

i2c_wait_for_writes
===================

.. c:function:: void i2c_wait_for_writes(struct hfi1_devdata *dd, u32 target)

    wait for a write

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param u32 target:
        *undescribed*

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

.. c:function:: int i2c_ackrcv(struct hfi1_devdata *dd, u32 target)

    see if ack following write is true

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param u32 target:
        *undescribed*

.. _`rd_byte`:

rd_byte
=======

.. c:function:: int rd_byte(struct hfi1_devdata *dd, u32 target, int last)

    read a byte, sending STOP on last, else ACK

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param u32 target:
        *undescribed*

    :param int last:
        *undescribed*

.. _`rd_byte.description`:

Description
-----------

Returns byte shifted out of device

.. _`wr_byte`:

wr_byte
=======

.. c:function:: int wr_byte(struct hfi1_devdata *dd, u32 target, u8 data)

    write a byte, one bit at a time

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param u32 target:
        *undescribed*

    :param u8 data:
        the byte to write

.. _`wr_byte.description`:

Description
-----------

Returns 0 if we got the following ack, otherwise 1

.. _`stop_seq`:

stop_seq
========

.. c:function:: void stop_seq(struct hfi1_devdata *dd, u32 target)

    transmit the stop sequence

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param u32 target:
        *undescribed*

.. _`stop_seq.description`:

Description
-----------

(both clock/data low, clock high, data high while clock is high)

.. _`stop_cmd`:

stop_cmd
========

.. c:function:: void stop_cmd(struct hfi1_devdata *dd, u32 target)

    transmit the stop condition

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

    :param u32 target:
        *undescribed*

.. _`stop_cmd.description`:

Description
-----------

(both clock/data low, clock high, data high while clock is high)

.. _`hfi1_twsi_reset`:

hfi1_twsi_reset
===============

.. c:function:: int hfi1_twsi_reset(struct hfi1_devdata *dd, u32 target)

    reset I2C communication

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device
        returns 0 if ok, -EIO on error

    :param u32 target:
        *undescribed*

.. This file was automatic generated / don't edit.

