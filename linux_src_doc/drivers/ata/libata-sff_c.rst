.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libata-sff.c

.. _`ata_sff_check_status`:

ata_sff_check_status
====================

.. c:function:: u8 ata_sff_check_status(struct ata_port *ap)

    Read device status reg & clear interrupt

    :param struct ata_port \*ap:
        port where the device is

.. _`ata_sff_check_status.description`:

Description
-----------

Reads ATA taskfile status register for currently-selected device
and return its value. This also clears pending interrupts
from this device

.. _`ata_sff_check_status.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_altstatus`:

ata_sff_altstatus
=================

.. c:function:: u8 ata_sff_altstatus(struct ata_port *ap)

    Read device alternate status reg

    :param struct ata_port \*ap:
        port where the device is

.. _`ata_sff_altstatus.description`:

Description
-----------

Reads ATA taskfile alternate status register for
currently-selected device and return its value.

.. _`ata_sff_altstatus.note`:

Note
----

may NOT be used as the \ :c:func:`check_altstatus`\  entry in
ata_port_operations.

.. _`ata_sff_altstatus.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_irq_status`:

ata_sff_irq_status
==================

.. c:function:: u8 ata_sff_irq_status(struct ata_port *ap)

    Check if the device is busy

    :param struct ata_port \*ap:
        port where the device is

.. _`ata_sff_irq_status.description`:

Description
-----------

Determine if the port is currently busy. Uses altstatus
if available in order to avoid clearing shared IRQ status
when finding an IRQ source. Non ctl capable devices don't
share interrupt lines fortunately for us.

.. _`ata_sff_irq_status.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_sync`:

ata_sff_sync
============

.. c:function:: void ata_sff_sync(struct ata_port *ap)

    Flush writes

    :param struct ata_port \*ap:
        Port to wait for.

.. _`ata_sff_sync.caution`:

CAUTION
-------

If we have an mmio device with no ctl and no altstatus
method this will fail. No such devices are known to exist.

.. _`ata_sff_sync.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_pause`:

ata_sff_pause
=============

.. c:function:: void ata_sff_pause(struct ata_port *ap)

    Flush writes and wait 400nS

    :param struct ata_port \*ap:
        Port to pause for.

.. _`ata_sff_pause.caution`:

CAUTION
-------

If we have an mmio device with no ctl and no altstatus
method this will fail. No such devices are known to exist.

.. _`ata_sff_pause.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_dma_pause`:

ata_sff_dma_pause
=================

.. c:function:: void ata_sff_dma_pause(struct ata_port *ap)

    Pause before commencing DMA

    :param struct ata_port \*ap:
        Port to pause for.

.. _`ata_sff_dma_pause.description`:

Description
-----------

Perform I/O fencing and ensure sufficient cycle delays occur
for the HDMA1:0 transition

.. _`ata_sff_busy_sleep`:

ata_sff_busy_sleep
==================

.. c:function:: int ata_sff_busy_sleep(struct ata_port *ap, unsigned long tmout_pat, unsigned long tmout)

    sleep until BSY clears, or timeout

    :param struct ata_port \*ap:
        port containing status register to be polled

    :param unsigned long tmout_pat:
        impatience timeout in msecs

    :param unsigned long tmout:
        overall timeout in msecs

.. _`ata_sff_busy_sleep.description`:

Description
-----------

Sleep until ATA Status register bit BSY clears,
or a timeout occurs.

.. _`ata_sff_busy_sleep.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`ata_sff_busy_sleep.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_sff_wait_ready`:

ata_sff_wait_ready
==================

.. c:function:: int ata_sff_wait_ready(struct ata_link *link, unsigned long deadline)

    sleep until BSY clears, or timeout

    :param struct ata_link \*link:
        SFF link to wait ready status for

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`ata_sff_wait_ready.description`:

Description
-----------

Sleep until ATA Status register bit BSY clears, or timeout
occurs.

.. _`ata_sff_wait_ready.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`ata_sff_wait_ready.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_sff_set_devctl`:

ata_sff_set_devctl
==================

.. c:function:: void ata_sff_set_devctl(struct ata_port *ap, u8 ctl)

    Write device control reg

    :param struct ata_port \*ap:
        port where the device is

    :param u8 ctl:
        value to write

.. _`ata_sff_set_devctl.description`:

Description
-----------

Writes ATA taskfile device control register.

.. _`ata_sff_set_devctl.note`:

Note
----

may NOT be used as the \ :c:func:`sff_set_devctl`\  entry in
ata_port_operations.

.. _`ata_sff_set_devctl.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_dev_select`:

ata_sff_dev_select
==================

.. c:function:: void ata_sff_dev_select(struct ata_port *ap, unsigned int device)

    Select device 0/1 on ATA bus

    :param struct ata_port \*ap:
        ATA channel to manipulate

    :param unsigned int device:
        ATA device (numbered from zero) to select

.. _`ata_sff_dev_select.description`:

Description
-----------

Use the method defined in the ATA specification to
make either device 0, or device 1, active on the
ATA channel.  Works with both PIO and MMIO.

May be used as the \ :c:func:`dev_select`\  entry in ata_port_operations.

.. _`ata_sff_dev_select.locking`:

LOCKING
-------

caller.

.. _`ata_dev_select`:

ata_dev_select
==============

.. c:function:: void ata_dev_select(struct ata_port *ap, unsigned int device, unsigned int wait, unsigned int can_sleep)

    Select device 0/1 on ATA bus

    :param struct ata_port \*ap:
        ATA channel to manipulate

    :param unsigned int device:
        ATA device (numbered from zero) to select

    :param unsigned int wait:
        non-zero to wait for Status register BSY bit to clear

    :param unsigned int can_sleep:
        non-zero if context allows sleeping

.. _`ata_dev_select.description`:

Description
-----------

Use the method defined in the ATA specification to
make either device 0, or device 1, active on the
ATA channel.

This is a high-level version of \ :c:func:`ata_sff_dev_select`\ , which
additionally provides the services of inserting the proper
pauses and status polling, where needed.

.. _`ata_dev_select.locking`:

LOCKING
-------

caller.

.. _`ata_sff_irq_on`:

ata_sff_irq_on
==============

.. c:function:: void ata_sff_irq_on(struct ata_port *ap)

    Enable interrupts on a port.

    :param struct ata_port \*ap:
        Port on which interrupts are enabled.

.. _`ata_sff_irq_on.description`:

Description
-----------

Enable interrupts on a legacy IDE device using MMIO or PIO,
wait for idle, clear any pending interrupts.

.. _`ata_sff_irq_on.note`:

Note
----

may NOT be used as the \ :c:func:`sff_irq_on`\  entry in
ata_port_operations.

.. _`ata_sff_irq_on.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_tf_load`:

ata_sff_tf_load
===============

.. c:function:: void ata_sff_tf_load(struct ata_port *ap, const struct ata_taskfile *tf)

    send taskfile registers to host controller

    :param struct ata_port \*ap:
        Port to which output is sent

    :param const struct ata_taskfile \*tf:
        ATA taskfile register set

.. _`ata_sff_tf_load.description`:

Description
-----------

Outputs ATA taskfile to standard ATA host controller.

.. _`ata_sff_tf_load.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_tf_read`:

ata_sff_tf_read
===============

.. c:function:: void ata_sff_tf_read(struct ata_port *ap, struct ata_taskfile *tf)

    input device's ATA taskfile shadow registers

    :param struct ata_port \*ap:
        Port from which input is read

    :param struct ata_taskfile \*tf:
        ATA taskfile register set for storing input

.. _`ata_sff_tf_read.description`:

Description
-----------

Reads ATA taskfile registers for currently-selected device
into \ ``tf``\ . Assumes the device has a fully SFF compliant task file
layout and behaviour. If you device does not (eg has a different
status method) then you will need to provide a replacement tf_read

.. _`ata_sff_tf_read.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_exec_command`:

ata_sff_exec_command
====================

.. c:function:: void ata_sff_exec_command(struct ata_port *ap, const struct ata_taskfile *tf)

    issue ATA command to host controller

    :param struct ata_port \*ap:
        port to which command is being issued

    :param const struct ata_taskfile \*tf:
        ATA taskfile register set

.. _`ata_sff_exec_command.description`:

Description
-----------

Issues ATA command, with proper synchronization with interrupt
handler / other threads.

.. _`ata_sff_exec_command.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_tf_to_host`:

ata_tf_to_host
==============

.. c:function:: void ata_tf_to_host(struct ata_port *ap, const struct ata_taskfile *tf)

    issue ATA taskfile to host controller

    :param struct ata_port \*ap:
        port to which command is being issued

    :param const struct ata_taskfile \*tf:
        ATA taskfile register set

.. _`ata_tf_to_host.description`:

Description
-----------

Issues ATA taskfile register set to ATA host controller,
with proper synchronization with interrupt handler and
other threads.

.. _`ata_tf_to_host.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_sff_data_xfer`:

ata_sff_data_xfer
=================

.. c:function:: unsigned int ata_sff_data_xfer(struct ata_queued_cmd *qc, unsigned char *buf, unsigned int buflen, int rw)

    Transfer data by PIO

    :param struct ata_queued_cmd \*qc:
        queued command

    :param unsigned char \*buf:
        data buffer

    :param unsigned int buflen:
        buffer length

    :param int rw:
        read/write

.. _`ata_sff_data_xfer.description`:

Description
-----------

Transfer data from/to the device data register by PIO.

.. _`ata_sff_data_xfer.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_data_xfer.return`:

Return
------

Bytes consumed.

.. _`ata_sff_data_xfer32`:

ata_sff_data_xfer32
===================

.. c:function:: unsigned int ata_sff_data_xfer32(struct ata_queued_cmd *qc, unsigned char *buf, unsigned int buflen, int rw)

    Transfer data by PIO

    :param struct ata_queued_cmd \*qc:
        queued command

    :param unsigned char \*buf:
        data buffer

    :param unsigned int buflen:
        buffer length

    :param int rw:
        read/write

.. _`ata_sff_data_xfer32.description`:

Description
-----------

Transfer data from/to the device data register by PIO using 32bit
I/O operations.

.. _`ata_sff_data_xfer32.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_data_xfer32.return`:

Return
------

Bytes consumed.

.. _`ata_sff_data_xfer_noirq`:

ata_sff_data_xfer_noirq
=======================

.. c:function:: unsigned int ata_sff_data_xfer_noirq(struct ata_queued_cmd *qc, unsigned char *buf, unsigned int buflen, int rw)

    Transfer data by PIO

    :param struct ata_queued_cmd \*qc:
        queued command

    :param unsigned char \*buf:
        data buffer

    :param unsigned int buflen:
        buffer length

    :param int rw:
        read/write

.. _`ata_sff_data_xfer_noirq.description`:

Description
-----------

Transfer data from/to the device data register by PIO. Do the
transfer with interrupts disabled.

.. _`ata_sff_data_xfer_noirq.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_data_xfer_noirq.return`:

Return
------

Bytes consumed.

.. _`ata_pio_sector`:

ata_pio_sector
==============

.. c:function:: void ata_pio_sector(struct ata_queued_cmd *qc)

    Transfer a sector of data.

    :param struct ata_queued_cmd \*qc:
        Command on going

.. _`ata_pio_sector.description`:

Description
-----------

Transfer qc->sect_size bytes of data from/to the ATA device.

.. _`ata_pio_sector.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_pio_sectors`:

ata_pio_sectors
===============

.. c:function:: void ata_pio_sectors(struct ata_queued_cmd *qc)

    Transfer one or many sectors.

    :param struct ata_queued_cmd \*qc:
        Command on going

.. _`ata_pio_sectors.description`:

Description
-----------

Transfer one or many sectors of data from/to the
ATA device for the DRQ request.

.. _`ata_pio_sectors.locking`:

LOCKING
-------

Inherited from caller.

.. _`atapi_send_cdb`:

atapi_send_cdb
==============

.. c:function:: void atapi_send_cdb(struct ata_port *ap, struct ata_queued_cmd *qc)

    Write CDB bytes to hardware

    :param struct ata_port \*ap:
        Port to which ATAPI device is attached.

    :param struct ata_queued_cmd \*qc:
        Taskfile currently active

.. _`atapi_send_cdb.description`:

Description
-----------

When device has indicated its readiness to accept
a CDB, this function is called.  Send the CDB.

.. _`atapi_send_cdb.locking`:

LOCKING
-------

caller.

.. _`__atapi_pio_bytes`:

\__atapi_pio_bytes
==================

.. c:function:: int __atapi_pio_bytes(struct ata_queued_cmd *qc, unsigned int bytes)

    Transfer data from/to the ATAPI device.

    :param struct ata_queued_cmd \*qc:
        Command on going

    :param unsigned int bytes:
        number of bytes

.. _`__atapi_pio_bytes.description`:

Description
-----------

Transfer Transfer data from/to the ATAPI device.

.. _`__atapi_pio_bytes.locking`:

LOCKING
-------

Inherited from caller.

.. _`atapi_pio_bytes`:

atapi_pio_bytes
===============

.. c:function:: void atapi_pio_bytes(struct ata_queued_cmd *qc)

    Transfer data from/to the ATAPI device.

    :param struct ata_queued_cmd \*qc:
        Command on going

.. _`atapi_pio_bytes.description`:

Description
-----------

Transfer Transfer data from/to the ATAPI device.

.. _`atapi_pio_bytes.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_hsm_ok_in_wq`:

ata_hsm_ok_in_wq
================

.. c:function:: int ata_hsm_ok_in_wq(struct ata_port *ap, struct ata_queued_cmd *qc)

    Check if the qc can be handled in the workqueue.

    :param struct ata_port \*ap:
        the target ata_port

    :param struct ata_queued_cmd \*qc:
        qc on going

.. _`ata_hsm_ok_in_wq.return`:

Return
------

1 if ok in workqueue, 0 otherwise.

.. _`ata_hsm_qc_complete`:

ata_hsm_qc_complete
===================

.. c:function:: void ata_hsm_qc_complete(struct ata_queued_cmd *qc, int in_wq)

    finish a qc running on standard HSM

    :param struct ata_queued_cmd \*qc:
        Command to complete

    :param int in_wq:
        1 if called from workqueue, 0 otherwise

.. _`ata_hsm_qc_complete.description`:

Description
-----------

Finish \ ``qc``\  which is running on standard HSM.

.. _`ata_hsm_qc_complete.locking`:

LOCKING
-------

If \ ``in_wq``\  is zero, spin_lock_irqsave(host lock).
Otherwise, none on entry and grabs host lock.

.. _`ata_sff_hsm_move`:

ata_sff_hsm_move
================

.. c:function:: int ata_sff_hsm_move(struct ata_port *ap, struct ata_queued_cmd *qc, u8 status, int in_wq)

    move the HSM to the next state.

    :param struct ata_port \*ap:
        the target ata_port

    :param struct ata_queued_cmd \*qc:
        qc on going

    :param u8 status:
        current device status

    :param int in_wq:
        1 if called from workqueue, 0 otherwise

.. _`ata_sff_hsm_move.return`:

Return
------

1 when poll next status needed, 0 otherwise.

.. _`ata_sff_qc_issue`:

ata_sff_qc_issue
================

.. c:function:: unsigned int ata_sff_qc_issue(struct ata_queued_cmd *qc)

    issue taskfile to a SFF controller

    :param struct ata_queued_cmd \*qc:
        command to issue to device

.. _`ata_sff_qc_issue.description`:

Description
-----------

This function issues a PIO or NODATA command to a SFF
controller.

.. _`ata_sff_qc_issue.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_sff_qc_issue.return`:

Return
------

Zero on success, AC_ERR\_\* mask on failure

.. _`ata_sff_qc_fill_rtf`:

ata_sff_qc_fill_rtf
===================

.. c:function:: bool ata_sff_qc_fill_rtf(struct ata_queued_cmd *qc)

    fill result TF using ->sff_tf_read

    :param struct ata_queued_cmd \*qc:
        qc to fill result TF for

.. _`ata_sff_qc_fill_rtf.description`:

Description
-----------

\ ``qc``\  is finished and result TF needs to be filled.  Fill it
using ->sff_tf_read.

.. _`ata_sff_qc_fill_rtf.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_sff_qc_fill_rtf.return`:

Return
------

true indicating that result TF is successfully filled.

.. _`ata_sff_port_intr`:

ata_sff_port_intr
=================

.. c:function:: unsigned int ata_sff_port_intr(struct ata_port *ap, struct ata_queued_cmd *qc)

    Handle SFF port interrupt

    :param struct ata_port \*ap:
        Port on which interrupt arrived (possibly...)

    :param struct ata_queued_cmd \*qc:
        Taskfile currently active in engine

.. _`ata_sff_port_intr.description`:

Description
-----------

Handle port interrupt for given queued command.

.. _`ata_sff_port_intr.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_sff_port_intr.return`:

Return
------

One if interrupt was handled, zero if not (shared irq).

.. _`ata_sff_interrupt`:

ata_sff_interrupt
=================

.. c:function:: irqreturn_t ata_sff_interrupt(int irq, void *dev_instance)

    Default SFF ATA host interrupt handler

    :param int irq:
        irq line (unused)

    :param void \*dev_instance:
        pointer to our ata_host information structure

.. _`ata_sff_interrupt.description`:

Description
-----------

Default interrupt handler for PCI IDE devices.  Calls
\ :c:func:`ata_sff_port_intr`\  for each port that is not disabled.

.. _`ata_sff_interrupt.locking`:

LOCKING
-------

Obtains host lock during operation.

.. _`ata_sff_interrupt.return`:

Return
------

IRQ_NONE or IRQ_HANDLED.

.. _`ata_sff_lost_interrupt`:

ata_sff_lost_interrupt
======================

.. c:function:: void ata_sff_lost_interrupt(struct ata_port *ap)

    Check for an apparent lost interrupt

    :param struct ata_port \*ap:
        port that appears to have timed out

.. _`ata_sff_lost_interrupt.description`:

Description
-----------

Called from the libata error handlers when the core code suspects
an interrupt has been lost. If it has complete anything we can and
then return. Interface must support altstatus for this faster
recovery to occur.

.. _`ata_sff_lost_interrupt.locking`:

Locking
-------

Caller holds host lock

.. _`ata_sff_freeze`:

ata_sff_freeze
==============

.. c:function:: void ata_sff_freeze(struct ata_port *ap)

    Freeze SFF controller port

    :param struct ata_port \*ap:
        port to freeze

.. _`ata_sff_freeze.description`:

Description
-----------

Freeze SFF controller port.

.. _`ata_sff_freeze.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_thaw`:

ata_sff_thaw
============

.. c:function:: void ata_sff_thaw(struct ata_port *ap)

    Thaw SFF controller port

    :param struct ata_port \*ap:
        port to thaw

.. _`ata_sff_thaw.description`:

Description
-----------

Thaw SFF controller port.

.. _`ata_sff_thaw.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_sff_prereset`:

ata_sff_prereset
================

.. c:function:: int ata_sff_prereset(struct ata_link *link, unsigned long deadline)

    prepare SFF link for reset

    :param struct ata_link \*link:
        SFF link to be reset

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`ata_sff_prereset.description`:

Description
-----------

SFF link \ ``link``\  is about to be reset.  Initialize it.  It first
calls \ :c:func:`ata_std_prereset`\  and wait for !BSY if the port is
being softreset.

.. _`ata_sff_prereset.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_sff_prereset.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_devchk`:

ata_devchk
==========

.. c:function:: unsigned int ata_devchk(struct ata_port *ap, unsigned int device)

    PATA device presence detection

    :param struct ata_port \*ap:
        ATA channel to examine

    :param unsigned int device:
        Device to examine (starting at zero)

.. _`ata_devchk.description`:

Description
-----------

This technique was originally described in
Hale Landis's ATADRVR (www.ata-atapi.com), and
later found its way into the ATA/ATAPI spec.

Write a pattern to the ATA shadow registers,
and if a device is present, it will respond by
correctly storing and echoing back the
ATA shadow register contents.

.. _`ata_devchk.locking`:

LOCKING
-------

caller.

.. _`ata_sff_dev_classify`:

ata_sff_dev_classify
====================

.. c:function:: unsigned int ata_sff_dev_classify(struct ata_device *dev, int present, u8 *r_err)

    Parse returned ATA device signature

    :param struct ata_device \*dev:
        ATA device to classify (starting at zero)

    :param int present:
        device seems present

    :param u8 \*r_err:
        Value of error register on completion

.. _`ata_sff_dev_classify.description`:

Description
-----------

After an event -- SRST, E.D.D., or SATA COMRESET -- occurs,
an ATA/ATAPI-defined set of values is placed in the ATA
shadow registers, indicating the results of device detection
and diagnostics.

Select the ATA device, and read the values from the ATA shadow
registers.  Then parse according to the Error register value,
and the spec-defined values examined by \ :c:func:`ata_dev_classify`\ .

.. _`ata_sff_dev_classify.locking`:

LOCKING
-------

caller.

.. _`ata_sff_dev_classify.return`:

Return
------

Device type - \ ``ATA_DEV_ATA``\ , \ ``ATA_DEV_ATAPI``\  or \ ``ATA_DEV_NONE``\ .

.. _`ata_sff_wait_after_reset`:

ata_sff_wait_after_reset
========================

.. c:function:: int ata_sff_wait_after_reset(struct ata_link *link, unsigned int devmask, unsigned long deadline)

    wait for devices to become ready after reset

    :param struct ata_link \*link:
        SFF link which is just reset

    :param unsigned int devmask:
        mask of present devices

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`ata_sff_wait_after_reset.description`:

Description
-----------

Wait devices attached to SFF \ ``link``\  to become ready after
reset.  It contains preceding 150ms wait to avoid accessing TF
status register too early.

.. _`ata_sff_wait_after_reset.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`ata_sff_wait_after_reset.return`:

Return
------

0 on success, -ENODEV if some or all of devices in \ ``devmask``\ 
don't seem to exist.  -errno on other errors.

.. _`ata_sff_softreset`:

ata_sff_softreset
=================

.. c:function:: int ata_sff_softreset(struct ata_link *link, unsigned int *classes, unsigned long deadline)

    reset host port via ATA SRST

    :param struct ata_link \*link:
        ATA link to reset

    :param unsigned int \*classes:
        resulting classes of attached devices

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`ata_sff_softreset.description`:

Description
-----------

Reset host port using ATA SRST.

.. _`ata_sff_softreset.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_sff_softreset.return`:

Return
------

0 on success, -errno otherwise.

.. _`sata_sff_hardreset`:

sata_sff_hardreset
==================

.. c:function:: int sata_sff_hardreset(struct ata_link *link, unsigned int *class, unsigned long deadline)

    reset host port via SATA phy reset

    :param struct ata_link \*link:
        link to reset

    :param unsigned int \*class:
        resulting class of attached device

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`sata_sff_hardreset.description`:

Description
-----------

SATA phy-reset host port using DET bits of SControl register,
wait for !BSY and classify the attached device.

.. _`sata_sff_hardreset.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`sata_sff_hardreset.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_sff_postreset`:

ata_sff_postreset
=================

.. c:function:: void ata_sff_postreset(struct ata_link *link, unsigned int *classes)

    SFF postreset callback

    :param struct ata_link \*link:
        the target SFF ata_link

    :param unsigned int \*classes:
        classes of attached devices

.. _`ata_sff_postreset.description`:

Description
-----------

This function is invoked after a successful reset.  It first
calls \ :c:func:`ata_std_postreset`\  and performs SFF specific postreset
processing.

.. _`ata_sff_postreset.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_sff_drain_fifo`:

ata_sff_drain_fifo
==================

.. c:function:: void ata_sff_drain_fifo(struct ata_queued_cmd *qc)

    Stock FIFO drain logic for SFF controllers

    :param struct ata_queued_cmd \*qc:
        command

.. _`ata_sff_drain_fifo.description`:

Description
-----------

Drain the FIFO and device of any stuck data following a command
failing to complete. In some cases this is necessary before a
reset will recover the device.

.. _`ata_sff_error_handler`:

ata_sff_error_handler
=====================

.. c:function:: void ata_sff_error_handler(struct ata_port *ap)

    Stock error handler for SFF controller

    :param struct ata_port \*ap:
        port to handle error for

.. _`ata_sff_error_handler.description`:

Description
-----------

Stock error handler for SFF controller.  It can handle both
PATA and SATA controllers.  Many controllers should be able to
use this EH as-is or with some added handling before and
after.

.. _`ata_sff_error_handler.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_sff_std_ports`:

ata_sff_std_ports
=================

.. c:function:: void ata_sff_std_ports(struct ata_ioports *ioaddr)

    initialize ioaddr with standard port offsets.

    :param struct ata_ioports \*ioaddr:
        IO address structure to be initialized

.. _`ata_sff_std_ports.description`:

Description
-----------

Utility function which initializes data_addr, error_addr,
feature_addr, nsect_addr, lbal_addr, lbam_addr, lbah_addr,
device_addr, status_addr, and command_addr to standard offsets
relative to cmd_addr.

Does not set ctl_addr, altstatus_addr, bmdma_addr, or scr_addr.

.. _`ata_pci_sff_init_host`:

ata_pci_sff_init_host
=====================

.. c:function:: int ata_pci_sff_init_host(struct ata_host *host)

    acquire native PCI ATA resources and init host

    :param struct ata_host \*host:
        target ATA host

.. _`ata_pci_sff_init_host.description`:

Description
-----------

Acquire native PCI ATA resources for \ ``host``\  and initialize the
first two ports of \ ``host``\  accordingly.  Ports marked dummy are
skipped and allocation failure makes the port dummy.

Note that native PCI resources are valid even for legacy hosts
as we fix up pdev resources array early in boot, so this
function can be used for both native and legacy SFF hosts.

.. _`ata_pci_sff_init_host.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_pci_sff_init_host.return`:

Return
------

0 if at least one port is initialized, -ENODEV if no port is
available.

.. _`ata_pci_sff_prepare_host`:

ata_pci_sff_prepare_host
========================

.. c:function:: int ata_pci_sff_prepare_host(struct pci_dev *pdev, const struct ata_port_info * const *ppi, struct ata_host **r_host)

    helper to prepare PCI PIO-only SFF ATA host

    :param struct pci_dev \*pdev:
        target PCI device

    :param const struct ata_port_info \* const \*ppi:
        array of port_info, must be enough for two ports

    :param struct ata_host \*\*r_host:
        out argument for the initialized ATA host

.. _`ata_pci_sff_prepare_host.description`:

Description
-----------

Helper to allocate PIO-only SFF ATA host for \ ``pdev``\ , acquire
all PCI resources and initialize it accordingly in one go.

.. _`ata_pci_sff_prepare_host.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_pci_sff_prepare_host.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_pci_sff_activate_host`:

ata_pci_sff_activate_host
=========================

.. c:function:: int ata_pci_sff_activate_host(struct ata_host *host, irq_handler_t irq_handler, struct scsi_host_template *sht)

    start SFF host, request IRQ and register it

    :param struct ata_host \*host:
        target SFF ATA host

    :param irq_handler_t irq_handler:
        irq_handler used when requesting IRQ(s)

    :param struct scsi_host_template \*sht:
        scsi_host_template to use when registering the host

.. _`ata_pci_sff_activate_host.description`:

Description
-----------

This is the counterpart of \ :c:func:`ata_host_activate`\  for SFF ATA
hosts.  This separate helper is necessary because SFF hosts
use two separate interrupts in legacy mode.

.. _`ata_pci_sff_activate_host.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_pci_sff_activate_host.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_pci_sff_init_one`:

ata_pci_sff_init_one
====================

.. c:function:: int ata_pci_sff_init_one(struct pci_dev *pdev, const struct ata_port_info * const *ppi, struct scsi_host_template *sht, void *host_priv, int hflag)

    Initialize/register PIO-only PCI IDE controller

    :param struct pci_dev \*pdev:
        Controller to be initialized

    :param const struct ata_port_info \* const \*ppi:
        array of port_info, must be enough for two ports

    :param struct scsi_host_template \*sht:
        scsi_host_template to use when registering the host

    :param void \*host_priv:
        host private_data

    :param int hflag:
        host flags

.. _`ata_pci_sff_init_one.description`:

Description
-----------

This is a helper function which can be called from a driver's
\ :c:func:`xxx_init_one`\  probe function if the hardware uses traditional
IDE taskfile registers and is PIO only.

.. _`ata_pci_sff_init_one.assumption`:

ASSUMPTION
----------

Nobody makes a single channel controller that appears solely as
the secondary legacy port on PCI.

.. _`ata_pci_sff_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`ata_pci_sff_init_one.return`:

Return
------

Zero on success, negative on errno-based value on error.

.. _`ata_bmdma_fill_sg`:

ata_bmdma_fill_sg
=================

.. c:function:: void ata_bmdma_fill_sg(struct ata_queued_cmd *qc)

    Fill PCI IDE PRD table

    :param struct ata_queued_cmd \*qc:
        Metadata associated with taskfile to be transferred

.. _`ata_bmdma_fill_sg.description`:

Description
-----------

Fill PCI IDE PRD (scatter-gather) table with segments
associated with the current disk command.

.. _`ata_bmdma_fill_sg.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_fill_sg_dumb`:

ata_bmdma_fill_sg_dumb
======================

.. c:function:: void ata_bmdma_fill_sg_dumb(struct ata_queued_cmd *qc)

    Fill PCI IDE PRD table

    :param struct ata_queued_cmd \*qc:
        Metadata associated with taskfile to be transferred

.. _`ata_bmdma_fill_sg_dumb.description`:

Description
-----------

Fill PCI IDE PRD (scatter-gather) table with segments
associated with the current disk command. Perform the fill
so that we avoid writing any length 64K records for
controllers that don't follow the spec.

.. _`ata_bmdma_fill_sg_dumb.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_qc_prep`:

ata_bmdma_qc_prep
=================

.. c:function:: void ata_bmdma_qc_prep(struct ata_queued_cmd *qc)

    Prepare taskfile for submission

    :param struct ata_queued_cmd \*qc:
        Metadata associated with taskfile to be prepared

.. _`ata_bmdma_qc_prep.description`:

Description
-----------

Prepare ATA taskfile for submission.

.. _`ata_bmdma_qc_prep.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_dumb_qc_prep`:

ata_bmdma_dumb_qc_prep
======================

.. c:function:: void ata_bmdma_dumb_qc_prep(struct ata_queued_cmd *qc)

    Prepare taskfile for submission

    :param struct ata_queued_cmd \*qc:
        Metadata associated with taskfile to be prepared

.. _`ata_bmdma_dumb_qc_prep.description`:

Description
-----------

Prepare ATA taskfile for submission.

.. _`ata_bmdma_dumb_qc_prep.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_qc_issue`:

ata_bmdma_qc_issue
==================

.. c:function:: unsigned int ata_bmdma_qc_issue(struct ata_queued_cmd *qc)

    issue taskfile to a BMDMA controller

    :param struct ata_queued_cmd \*qc:
        command to issue to device

.. _`ata_bmdma_qc_issue.description`:

Description
-----------

This function issues a PIO, NODATA or DMA command to a
SFF/BMDMA controller.  PIO and NODATA are handled by
\ :c:func:`ata_sff_qc_issue`\ .

.. _`ata_bmdma_qc_issue.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_qc_issue.return`:

Return
------

Zero on success, AC_ERR\_\* mask on failure

.. _`ata_bmdma_port_intr`:

ata_bmdma_port_intr
===================

.. c:function:: unsigned int ata_bmdma_port_intr(struct ata_port *ap, struct ata_queued_cmd *qc)

    Handle BMDMA port interrupt

    :param struct ata_port \*ap:
        Port on which interrupt arrived (possibly...)

    :param struct ata_queued_cmd \*qc:
        Taskfile currently active in engine

.. _`ata_bmdma_port_intr.description`:

Description
-----------

Handle port interrupt for given queued command.

.. _`ata_bmdma_port_intr.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_port_intr.return`:

Return
------

One if interrupt was handled, zero if not (shared irq).

.. _`ata_bmdma_interrupt`:

ata_bmdma_interrupt
===================

.. c:function:: irqreturn_t ata_bmdma_interrupt(int irq, void *dev_instance)

    Default BMDMA ATA host interrupt handler

    :param int irq:
        irq line (unused)

    :param void \*dev_instance:
        pointer to our ata_host information structure

.. _`ata_bmdma_interrupt.description`:

Description
-----------

Default interrupt handler for PCI IDE devices.  Calls
\ :c:func:`ata_bmdma_port_intr`\  for each port that is not disabled.

.. _`ata_bmdma_interrupt.locking`:

LOCKING
-------

Obtains host lock during operation.

.. _`ata_bmdma_interrupt.return`:

Return
------

IRQ_NONE or IRQ_HANDLED.

.. _`ata_bmdma_error_handler`:

ata_bmdma_error_handler
=======================

.. c:function:: void ata_bmdma_error_handler(struct ata_port *ap)

    Stock error handler for BMDMA controller

    :param struct ata_port \*ap:
        port to handle error for

.. _`ata_bmdma_error_handler.description`:

Description
-----------

Stock error handler for BMDMA controller.  It can handle both
PATA and SATA controllers.  Most BMDMA controllers should be
able to use this EH as-is or with some added handling before
and after.

.. _`ata_bmdma_error_handler.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_bmdma_post_internal_cmd`:

ata_bmdma_post_internal_cmd
===========================

.. c:function:: void ata_bmdma_post_internal_cmd(struct ata_queued_cmd *qc)

    Stock post_internal_cmd for BMDMA

    :param struct ata_queued_cmd \*qc:
        internal command to clean up

.. _`ata_bmdma_post_internal_cmd.locking`:

LOCKING
-------

Kernel thread context (may sleep)

.. _`ata_bmdma_irq_clear`:

ata_bmdma_irq_clear
===================

.. c:function:: void ata_bmdma_irq_clear(struct ata_port *ap)

    Clear PCI IDE BMDMA interrupt.

    :param struct ata_port \*ap:
        Port associated with this ATA transaction.

.. _`ata_bmdma_irq_clear.description`:

Description
-----------

Clear interrupt and error flags in DMA status register.

May be used as the \ :c:func:`irq_clear`\  entry in ata_port_operations.

.. _`ata_bmdma_irq_clear.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_setup`:

ata_bmdma_setup
===============

.. c:function:: void ata_bmdma_setup(struct ata_queued_cmd *qc)

    Set up PCI IDE BMDMA transaction

    :param struct ata_queued_cmd \*qc:
        Info associated with this ATA transaction.

.. _`ata_bmdma_setup.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_start`:

ata_bmdma_start
===============

.. c:function:: void ata_bmdma_start(struct ata_queued_cmd *qc)

    Start a PCI IDE BMDMA transaction

    :param struct ata_queued_cmd \*qc:
        Info associated with this ATA transaction.

.. _`ata_bmdma_start.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_stop`:

ata_bmdma_stop
==============

.. c:function:: void ata_bmdma_stop(struct ata_queued_cmd *qc)

    Stop PCI IDE BMDMA transfer

    :param struct ata_queued_cmd \*qc:
        Command we are ending DMA for

.. _`ata_bmdma_stop.description`:

Description
-----------

Clears the ATA_DMA_START flag in the dma control register

May be used as the \ :c:func:`bmdma_stop`\  entry in ata_port_operations.

.. _`ata_bmdma_stop.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_status`:

ata_bmdma_status
================

.. c:function:: u8 ata_bmdma_status(struct ata_port *ap)

    Read PCI IDE BMDMA status

    :param struct ata_port \*ap:
        Port associated with this ATA transaction.

.. _`ata_bmdma_status.description`:

Description
-----------

Read and return BMDMA status register.

May be used as the \ :c:func:`bmdma_status`\  entry in ata_port_operations.

.. _`ata_bmdma_status.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`ata_bmdma_port_start`:

ata_bmdma_port_start
====================

.. c:function:: int ata_bmdma_port_start(struct ata_port *ap)

    Set port up for bmdma.

    :param struct ata_port \*ap:
        Port to initialize

.. _`ata_bmdma_port_start.description`:

Description
-----------

Called just after data structures for each port are
initialized.  Allocates space for PRD table.

May be used as the \ :c:func:`port_start`\  entry in ata_port_operations.

.. _`ata_bmdma_port_start.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_bmdma_port_start32`:

ata_bmdma_port_start32
======================

.. c:function:: int ata_bmdma_port_start32(struct ata_port *ap)

    Set port up for dma.

    :param struct ata_port \*ap:
        Port to initialize

.. _`ata_bmdma_port_start32.description`:

Description
-----------

Called just after data structures for each port are
initialized.  Enables 32bit PIO and allocates space for PRD
table.

May be used as the \ :c:func:`port_start`\  entry in ata_port_operations for
devices that are capable of 32bit PIO.

.. _`ata_bmdma_port_start32.locking`:

LOCKING
-------

Inherited from caller.

.. _`ata_pci_bmdma_clear_simplex`:

ata_pci_bmdma_clear_simplex
===========================

.. c:function:: int ata_pci_bmdma_clear_simplex(struct pci_dev *pdev)

    attempt to kick device out of simplex

    :param struct pci_dev \*pdev:
        PCI device

.. _`ata_pci_bmdma_clear_simplex.description`:

Description
-----------

Some PCI ATA devices report simplex mode but in fact can be told to
enter non simplex mode. This implements the necessary logic to
perform the task on such devices. Calling it on other devices will
have -undefined- behaviour.

.. _`ata_pci_bmdma_init`:

ata_pci_bmdma_init
==================

.. c:function:: void ata_pci_bmdma_init(struct ata_host *host)

    acquire PCI BMDMA resources and init ATA host

    :param struct ata_host \*host:
        target ATA host

.. _`ata_pci_bmdma_init.description`:

Description
-----------

Acquire PCI BMDMA resources and initialize \ ``host``\  accordingly.

.. _`ata_pci_bmdma_init.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_pci_bmdma_prepare_host`:

ata_pci_bmdma_prepare_host
==========================

.. c:function:: int ata_pci_bmdma_prepare_host(struct pci_dev *pdev, const struct ata_port_info * const *ppi, struct ata_host **r_host)

    helper to prepare PCI BMDMA ATA host

    :param struct pci_dev \*pdev:
        target PCI device

    :param const struct ata_port_info \* const \*ppi:
        array of port_info, must be enough for two ports

    :param struct ata_host \*\*r_host:
        out argument for the initialized ATA host

.. _`ata_pci_bmdma_prepare_host.description`:

Description
-----------

Helper to allocate BMDMA ATA host for \ ``pdev``\ , acquire all PCI
resources and initialize it accordingly in one go.

.. _`ata_pci_bmdma_prepare_host.locking`:

LOCKING
-------

Inherited from calling layer (may sleep).

.. _`ata_pci_bmdma_prepare_host.return`:

Return
------

0 on success, -errno otherwise.

.. _`ata_pci_bmdma_init_one`:

ata_pci_bmdma_init_one
======================

.. c:function:: int ata_pci_bmdma_init_one(struct pci_dev *pdev, const struct ata_port_info * const *ppi, struct scsi_host_template *sht, void *host_priv, int hflags)

    Initialize/register BMDMA PCI IDE controller

    :param struct pci_dev \*pdev:
        Controller to be initialized

    :param const struct ata_port_info \* const \*ppi:
        array of port_info, must be enough for two ports

    :param struct scsi_host_template \*sht:
        scsi_host_template to use when registering the host

    :param void \*host_priv:
        host private_data

    :param int hflags:
        host flags

.. _`ata_pci_bmdma_init_one.description`:

Description
-----------

This function is similar to \ :c:func:`ata_pci_sff_init_one`\  but also
takes care of BMDMA initialization.

.. _`ata_pci_bmdma_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`ata_pci_bmdma_init_one.return`:

Return
------

Zero on success, negative on errno-based value on error.

.. _`ata_sff_port_init`:

ata_sff_port_init
=================

.. c:function:: void ata_sff_port_init(struct ata_port *ap)

    Initialize SFF/BMDMA ATA port

    :param struct ata_port \*ap:
        Port to initialize

.. _`ata_sff_port_init.description`:

Description
-----------

Called on port allocation to initialize SFF/BMDMA specific
fields.

.. _`ata_sff_port_init.locking`:

LOCKING
-------

None.

.. This file was automatic generated / don't edit.

