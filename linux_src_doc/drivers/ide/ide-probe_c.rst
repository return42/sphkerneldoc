.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-probe.c

.. _`generic_id`:

generic_id
==========

.. c:function:: void generic_id(ide_drive_t *drive)

    add a generic drive id

    :param ide_drive_t \*drive:
        drive to make an ID block for

.. _`generic_id.description`:

Description
-----------

Add a fake id field to the drive we are passed. This allows
use to skip a ton of NULL checks (which people always miss)
and make drive properties unconditional outside of this file

.. _`do_identify`:

do_identify
===========

.. c:function:: void do_identify(ide_drive_t *drive, u8 cmd, u16 *id)

    identify a drive

    :param ide_drive_t \*drive:
        drive to identify

    :param u8 cmd:
        command used

    :param u16 \*id:
        buffer for IDENTIFY data

.. _`do_identify.description`:

Description
-----------

Called when we have issued a drive identify command to
read and parse the results. This function is run with
interrupts disabled.

.. _`ide_dev_read_id`:

ide_dev_read_id
===============

.. c:function:: int ide_dev_read_id(ide_drive_t *drive, u8 cmd, u16 *id, int irq_ctx)

    send ATA/ATAPI IDENTIFY command

    :param ide_drive_t \*drive:
        drive to identify

    :param u8 cmd:
        command to use

    :param u16 \*id:
        buffer for IDENTIFY data

    :param int irq_ctx:
        flag set when called from the IRQ context

.. _`ide_dev_read_id.description`:

Description
-----------

Sends an ATA(PI) IDENTIFY request to a drive and waits for a response.

.. _`ide_dev_read_id.return`:

Return
------

0  device was identified
1  device timed-out (no response to identify request)
2  device aborted the command (refused to identify itself)

.. _`do_probe`:

do_probe
========

.. c:function:: int do_probe(ide_drive_t *drive, u8 cmd)

    probe an IDE device

    :param ide_drive_t \*drive:
        drive to probe

    :param u8 cmd:
        command to use

.. _`do_probe.description`:

Description
-----------

\ :c:func:`do_probe`\  has the difficult job of finding a drive if it exists,
without getting hung up if it doesn't exist, without trampling on
ethernet cards, and without leaving any IRQs dangling to haunt us later.

If a drive is "known" to exist (from CMOS or kernel parameters),
but does not respond right away, the probe will "hang in there"
for the maximum wait time (about 30 seconds), otherwise it will
exit much more quickly.

.. _`do_probe.return`:

Return
------

0  device was identified
1  device timed-out (no response to identify request)
2  device aborted the command (refused to identify itself)
3  bad status from device (possible for ATAPI drives)
4  probe was not attempted because failure was obvious

.. _`probe_for_drive`:

probe_for_drive
===============

.. c:function:: u8 probe_for_drive(ide_drive_t *drive)

    upper level drive probe

    :param ide_drive_t \*drive:
        drive to probe for

.. _`probe_for_drive.description`:

Description
-----------

\ :c:func:`probe_for_drive`\  tests for existence of a given drive using \ :c:func:`do_probe`\ 
and presents things to the user as needed.

.. _`probe_for_drive.return`:

Return
------

0  no device was found
1  device was found
(note: IDE_DFLAG_PRESENT might still be not set)

.. _`ide_port_wait_ready`:

ide_port_wait_ready
===================

.. c:function:: int ide_port_wait_ready(ide_hwif_t *hwif)

    wait for port to become ready

    :param ide_hwif_t \*hwif:
        IDE port

.. _`ide_port_wait_ready.description`:

Description
-----------

This is needed on some PPCs and a bunch of BIOS-less embedded
platforms.  Typical cases are:

- The firmware hard reset the disk before booting the kernel,
the drive is still doing it's poweron-reset sequence, that
can take up to 30 seconds.

- The firmware does nothing (or no firmware), the device is
still in POST state (same as above actually).

- Some CD/DVD/Writer combo drives tend to drive the bus during
their reset sequence even when they are non-selected slave
devices, thus preventing discovery of the main HD.

Doing this wait-for-non-busy should not harm any existing
configuration and fix some issues like the above.

BenH.

Returns 0 on success, error code (< 0) otherwise.

.. _`ide_undecoded_slave`:

ide_undecoded_slave
===================

.. c:function:: void ide_undecoded_slave(ide_drive_t *dev1)

    look for bad CF adapters

    :param ide_drive_t \*dev1:
        slave device

.. _`ide_undecoded_slave.description`:

Description
-----------

Analyse the drives on the interface and attempt to decide if we
have the same drive viewed twice. This occurs with crap CF adapters
and PCMCIA sometimes.

.. _`ide_find_port_slot`:

ide_find_port_slot
==================

.. c:function:: int ide_find_port_slot(const struct ide_port_info *d)

    find free port slot

    :param const struct ide_port_info \*d:
        IDE port info

.. _`ide_find_port_slot.description`:

Description
-----------

Return the new port slot index or -ENOENT if we are out of free slots.

.. _`ide_unregister`:

ide_unregister
==============

.. c:function:: void ide_unregister(ide_hwif_t *hwif)

    free an IDE interface

    :param ide_hwif_t \*hwif:
        IDE interface

.. _`ide_unregister.description`:

Description
-----------

Perform the final unregister of an IDE interface.

.. _`ide_unregister.locking`:

Locking
-------

The caller must not hold the IDE locks.

It is up to the caller to be sure there is no pending I/O here,
and that the interface will not be reopened (present/vanishing
locking isn't yet done BTW).

.. This file was automatic generated / don't edit.

