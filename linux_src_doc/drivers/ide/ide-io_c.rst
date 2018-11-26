.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-io.c

.. _`do_special`:

do_special
==========

.. c:function:: ide_startstop_t do_special(ide_drive_t *drive)

    issue some special commands

    :param drive:
        drive the command is for
    :type drive: ide_drive_t \*

.. _`do_special.description`:

Description
-----------

\ :c:func:`do_special`\  is used to issue ATA_CMD_INIT_DEV_PARAMS,
ATA_CMD_RESTORE and ATA_CMD_SET_MULTI commands to a drive.

.. _`execute_drive_cmd`:

execute_drive_cmd
=================

.. c:function:: ide_startstop_t execute_drive_cmd(ide_drive_t *drive, struct request *rq)

    issue special drive command

    :param drive:
        the drive to issue the command on
    :type drive: ide_drive_t \*

    :param rq:
        the request structure holding the command
    :type rq: struct request \*

.. _`execute_drive_cmd.description`:

Description
-----------

\ :c:func:`execute_drive_cmd`\  issues a special drive command,  usually
initiated by \ :c:func:`ioctl`\  from the external hdparm program. The
command can be a drive command, drive task or taskfile
operation. Weirdly you can call it with NULL to wait for
all commands to finish. Don't do this as that is due to change

.. _`start_request`:

start_request
=============

.. c:function:: ide_startstop_t start_request(ide_drive_t *drive, struct request *rq)

    start of I/O and command issuing for IDE

    :param drive:
        *undescribed*
    :type drive: ide_drive_t \*

    :param rq:
        *undescribed*
    :type rq: struct request \*

.. _`start_request.description`:

Description
-----------

\ :c:func:`start_request`\  initiates handling of a new I/O request. It
accepts commands and I/O (read/write) requests.

.. _`start_request.fixme`:

FIXME
-----

this function needs a rename

.. _`ide_stall_queue`:

ide_stall_queue
===============

.. c:function:: void ide_stall_queue(ide_drive_t *drive, unsigned long timeout)

    pause an IDE device

    :param drive:
        drive to stall
    :type drive: ide_drive_t \*

    :param timeout:
        time to stall for (jiffies)
    :type timeout: unsigned long

.. _`ide_stall_queue.description`:

Description
-----------

\ :c:func:`ide_stall_queue`\  can be used by a drive to give excess bandwidth back
to the port by sleeping for timeout jiffies.

.. _`ide_timer_expiry`:

ide_timer_expiry
================

.. c:function:: void ide_timer_expiry(struct timer_list *t)

    handle lack of an IDE interrupt

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`ide_timer_expiry.description`:

Description
-----------

An IDE command has timed out before the expected drive return
occurred. At this point we attempt to clean up the current
mess. If the current handler includes an expiry handler then
we invoke the expiry handler, and providing it is happy the
work is done. If that fails we apply generic recovery rules
invoking the handler and checking the drive DMA status. We
have an excessively incestuous relationship with the DMA
logic that wants cleaning up.

.. _`unexpected_intr`:

unexpected_intr
===============

.. c:function:: void unexpected_intr(int irq, ide_hwif_t *hwif)

    handle an unexpected IDE interrupt

    :param irq:
        interrupt line
    :type irq: int

    :param hwif:
        port being processed
    :type hwif: ide_hwif_t \*

.. _`unexpected_intr.description`:

Description
-----------

There's nothing really useful we can do with an unexpected interrupt,
other than reading the status register (to clear it), and logging it.
There should be no way that an irq can happen before we're ready for it,
so we needn't worry much about losing an "important" interrupt here.

On laptops (and "green" PCs), an unexpected interrupt occurs whenever
the drive enters "idle", "standby", or "sleep" mode, so if the status
looks "good", we just ignore the interrupt completely.

This routine assumes \__cli() is in effect when called.

If an unexpected interrupt happens on irq15 while we are handling irq14
and if the two interfaces are "serialized" (CMD640), then it looks like
we could screw up by interfering with a new request being set up for
irq15.

In reality, this is a non-issue.  The new command is not sent unless
the drive is ready to accept one, in which case we know the drive is
not trying to interrupt us.  And \ :c:func:`ide_set_handler`\  is always invoked
before completing the issuance of any new drive command, so we will not
be accidentally invoked as a result of any valid command completion
interrupt.

.. _`ide_intr`:

ide_intr
========

.. c:function:: irqreturn_t ide_intr(int irq, void *dev_id)

    default IDE interrupt handler

    :param irq:
        interrupt number
    :type irq: int

    :param dev_id:
        hwif
    :type dev_id: void \*

.. _`ide_intr.description`:

Description
-----------

This is the default IRQ handler for the IDE layer. You should
not need to override it. If you do be aware it is subtle in
places

hwif is the interface in the group currently performing
a command. hwif->cur_dev is the drive and hwif->handler is
the IRQ handler to call. As we issue a command the handlers
step through multiple states, reassigning the handler to the
next step in the process. Unlike a smart SCSI controller IDE
expects the main processor to sequence the various transfer
stages. We also manage a poll timer to catch up with most
timeout situations. There are still a few where the handlers
don't ever decide to give up.

The handler eventually returns ide_stopped to indicate the
request completed. At this point we issue the next request
on the port and the process begins again.

.. This file was automatic generated / don't edit.

