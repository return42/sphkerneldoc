.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/w1/w1_io.c

.. _`w1_touch_bit`:

w1_touch_bit
============

.. c:function:: u8 w1_touch_bit(struct w1_master *dev, int bit)

    Generates a write-0 or write-1 cycle and samples the level.

    :param struct w1_master \*dev:
        the master device

    :param int bit:
        0 - write a 0, 1 - write a 0 read the level

.. _`w1_write_bit`:

w1_write_bit
============

.. c:function:: void w1_write_bit(struct w1_master *dev, int bit)

    Generates a write-0 or write-1 cycle.

    :param struct w1_master \*dev:
        the master device

    :param int bit:
        bit to write

.. _`w1_write_bit.description`:

Description
-----------

Only call if dev->bus_master->touch_bit is NULL

.. _`w1_pre_write`:

w1_pre_write
============

.. c:function:: void w1_pre_write(struct w1_master *dev)

    pre-write operations

    :param struct w1_master \*dev:
        the master device

.. _`w1_pre_write.description`:

Description
-----------

Pre-write operation, currently only supporting strong pullups.
Program the hardware for a strong pullup, if one has been requested and
the hardware supports it.

.. _`w1_post_write`:

w1_post_write
=============

.. c:function:: void w1_post_write(struct w1_master *dev)

    post-write options

    :param struct w1_master \*dev:
        the master device

.. _`w1_post_write.description`:

Description
-----------

Post-write operation, currently only supporting strong pullups.
If a strong pullup was requested, clear it if the hardware supports
them, or execute the delay otherwise, in either case clear the request.

.. _`w1_write_8`:

w1_write_8
==========

.. c:function:: void w1_write_8(struct w1_master *dev, u8 byte)

    Writes 8 bits.

    :param struct w1_master \*dev:
        the master device

    :param u8 byte:
        the byte to write

.. _`w1_read_bit`:

w1_read_bit
===========

.. c:function:: u8 w1_read_bit(struct w1_master *dev)

    Generates a write-1 cycle and samples the level.

    :param struct w1_master \*dev:
        the master device

.. _`w1_read_bit.description`:

Description
-----------

Only call if dev->bus_master->touch_bit is NULL

.. _`w1_triplet`:

w1_triplet
==========

.. c:function:: u8 w1_triplet(struct w1_master *dev, int bdir)

    * Does a triplet - used for searching ROM addresses.

    :param struct w1_master \*dev:
        the master device

    :param int bdir:
        the bit to write if both id_bit and comp_bit are 0

.. _`w1_triplet.return-bits`:

Return bits
-----------

 bit 0 = id_bit
 bit 1 = comp_bit
 bit 2 = dir_taken
If both bits 0 & 1 are set, the search should be restarted.

.. _`w1_triplet.return`:

Return
------

bit fields - see above

.. _`w1_read_8`:

w1_read_8
=========

.. c:function:: u8 w1_read_8(struct w1_master *dev)

    Reads 8 bits.

    :param struct w1_master \*dev:
        the master device

.. _`w1_read_8.return`:

Return
------

the byte read

.. _`w1_write_block`:

w1_write_block
==============

.. c:function:: void w1_write_block(struct w1_master *dev, const u8 *buf, int len)

    Writes a series of bytes.

    :param struct w1_master \*dev:
        the master device

    :param const u8 \*buf:
        pointer to the data to write

    :param int len:
        the number of bytes to write

.. _`w1_touch_block`:

w1_touch_block
==============

.. c:function:: void w1_touch_block(struct w1_master *dev, u8 *buf, int len)

    Touches a series of bytes.

    :param struct w1_master \*dev:
        the master device

    :param u8 \*buf:
        pointer to the data to write

    :param int len:
        the number of bytes to write

.. _`w1_read_block`:

w1_read_block
=============

.. c:function:: u8 w1_read_block(struct w1_master *dev, u8 *buf, int len)

    Reads a series of bytes.

    :param struct w1_master \*dev:
        the master device

    :param u8 \*buf:
        pointer to the buffer to fill

    :param int len:
        the number of bytes to read

.. _`w1_read_block.return`:

Return
------

the number of bytes read

.. _`w1_reset_bus`:

w1_reset_bus
============

.. c:function:: int w1_reset_bus(struct w1_master *dev)

    Issues a reset bus sequence.

    :param struct w1_master \*dev:
        the master device

.. _`w1_reset_bus.return`:

Return
------

0=Device present, 1=No device present or error

.. _`w1_reset_select_slave`:

w1_reset_select_slave
=====================

.. c:function:: int w1_reset_select_slave(struct w1_slave *sl)

    reset and select a slave

    :param struct w1_slave \*sl:
        the slave to select

.. _`w1_reset_select_slave.description`:

Description
-----------

Resets the bus and then selects the slave by sending either a skip rom
or a rom match.  A skip rom is issued if there is only one device
registered on the bus.
The w1 master lock must be held.

.. _`w1_reset_select_slave.return`:

Return
------

0=success, anything else=error

.. _`w1_reset_resume_command`:

w1_reset_resume_command
=======================

.. c:function:: int w1_reset_resume_command(struct w1_master *dev)

    resume instead of another match ROM

    :param struct w1_master \*dev:
        the master device

.. _`w1_reset_resume_command.description`:

Description
-----------

When the workflow with a slave amongst many requires several
successive commands a reset between each, this function is similar
to doing a reset then a match ROM for the last matched ROM. The
advantage being that the matched ROM step is skipped in favor of the
resume command. The slave must support the command of course.

If the bus has only one slave, traditionnaly the match ROM is skipped
and a "SKIP ROM" is done for efficiency. On multi-slave busses, this
doesn't work of course, but the resume command is the next best thing.

The w1 master lock must be held.

.. _`w1_next_pullup`:

w1_next_pullup
==============

.. c:function:: void w1_next_pullup(struct w1_master *dev, int delay)

    register for a strong pullup

    :param struct w1_master \*dev:
        the master device

    :param int delay:
        time in milliseconds

.. _`w1_next_pullup.description`:

Description
-----------

Put out a strong pull-up of the specified duration after the next write
operation.  Not all hardware supports strong pullups.  Hardware that
doesn't support strong pullups will sleep for the given time after the
write operation without a strong pullup.  This is a one shot request for
the next write, specifying zero will clear a previous request.
The w1 master lock must be held.

.. _`w1_next_pullup.return`:

Return
------

0=success, anything else=error

.. This file was automatic generated / don't edit.

