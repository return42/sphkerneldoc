.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libata-acpi.c

.. _`ata_dev_acpi_handle`:

ata_dev_acpi_handle
===================

.. c:function:: acpi_handle ata_dev_acpi_handle(struct ata_device *dev)

    provide the acpi_handle for an ata_device

    :param struct ata_device \*dev:
        the acpi_handle returned will correspond to this device

.. _`ata_dev_acpi_handle.description`:

Description
-----------

Returns the acpi_handle for the ACPI namespace object corresponding to
the ata_device passed into the function, or NULL if no such object exists
or ACPI is disabled for this device due to consecutive errors.

.. _`ata_acpi_handle_hotplug`:

ata_acpi_handle_hotplug
=======================

.. c:function:: void ata_acpi_handle_hotplug(struct ata_port *ap, struct ata_device *dev, u32 event)

    ACPI event handler backend

    :param struct ata_port \*ap:
        ATA port ACPI event occurred

    :param struct ata_device \*dev:
        ATA device ACPI event occurred (can be NULL)

    :param u32 event:
        ACPI event which occurred

.. _`ata_acpi_handle_hotplug.description`:

Description
-----------

All ACPI bay / device realted events end up in this function.  If
the event is port-wide \ ``dev``\  is NULL.  If the event is specific to a
device, \ ``dev``\  points to it.

Hotplug (as opposed to unplug) notification is always handled as
port-wide while unplug only kills the target device on device-wide
event.

.. _`ata_acpi_handle_hotplug.locking`:

LOCKING
-------

ACPI notify handler context.  May sleep.

.. _`ata_acpi_dissociate`:

ata_acpi_dissociate
===================

.. c:function:: void ata_acpi_dissociate(struct ata_host *host)

    dissociate ATA host from ACPI objects

    :param struct ata_host \*host:
        target ATA host

.. _`ata_acpi_dissociate.description`:

Description
-----------

This function is called during driver detach after the whole host
is shut down.

.. _`ata_acpi_dissociate.locking`:

LOCKING
-------

EH context.

.. _`ata_acpi_gtm`:

ata_acpi_gtm
============

.. c:function:: int ata_acpi_gtm(struct ata_port *ap, struct ata_acpi_gtm *gtm)

    execute \_GTM

    :param struct ata_port \*ap:
        target ATA port

    :param struct ata_acpi_gtm \*gtm:
        out parameter for \_GTM result

.. _`ata_acpi_gtm.description`:

Description
-----------

Evaluate \_GTM and store the result in \ ``gtm``\ .

.. _`ata_acpi_gtm.locking`:

LOCKING
-------

EH context.

.. _`ata_acpi_gtm.return`:

Return
------

0 on success, -ENOENT if \_GTM doesn't exist, -errno on failure.

.. _`ata_acpi_stm`:

ata_acpi_stm
============

.. c:function:: int ata_acpi_stm(struct ata_port *ap, const struct ata_acpi_gtm *stm)

    execute \_STM

    :param struct ata_port \*ap:
        target ATA port

    :param const struct ata_acpi_gtm \*stm:
        timing parameter to \_STM

.. _`ata_acpi_stm.description`:

Description
-----------

Evaluate \_STM with timing parameter \ ``stm``\ .

.. _`ata_acpi_stm.locking`:

LOCKING
-------

EH context.

.. _`ata_acpi_stm.return`:

Return
------

0 on success, -ENOENT if \_STM doesn't exist, -errno on failure.

.. _`ata_dev_get_gtf`:

ata_dev_get_GTF
===============

.. c:function:: int ata_dev_get_GTF(struct ata_device *dev, struct ata_acpi_gtf **gtf)

    get the drive bootup default taskfile settings

    :param struct ata_device \*dev:
        target ATA device

    :param struct ata_acpi_gtf \*\*gtf:
        output parameter for buffer containing \_GTF taskfile arrays

.. _`ata_dev_get_gtf.description`:

Description
-----------

This applies to both PATA and SATA drives.

The \_GTF method has no input parameters.
It returns a variable number of register set values (registers
hex 1F1..1F7, taskfiles).
The <variable number> is not known in advance, so have ACPI-CA
allocate the buffer as needed and return it, then free it later.

.. _`ata_dev_get_gtf.locking`:

LOCKING
-------

EH context.

.. _`ata_dev_get_gtf.return`:

Return
------

Number of taskfiles on success, 0 if \_GTF doesn't exist.  -EINVAL
if \_GTF is invalid.

.. _`ata_acpi_gtm_xfermask`:

ata_acpi_gtm_xfermask
=====================

.. c:function:: unsigned long ata_acpi_gtm_xfermask(struct ata_device *dev, const struct ata_acpi_gtm *gtm)

    determine xfermode from GTM parameter

    :param struct ata_device \*dev:
        target device

    :param const struct ata_acpi_gtm \*gtm:
        GTM parameter to use

.. _`ata_acpi_gtm_xfermask.description`:

Description
-----------

Determine xfermask for \ ``dev``\  from \ ``gtm``\ .

.. _`ata_acpi_gtm_xfermask.locking`:

LOCKING
-------

None.

.. _`ata_acpi_gtm_xfermask.return`:

Return
------

Determined xfermask.

.. _`ata_acpi_cbl_80wire`:

ata_acpi_cbl_80wire
===================

.. c:function:: int ata_acpi_cbl_80wire(struct ata_port *ap, const struct ata_acpi_gtm *gtm)

    Check for 80 wire cable

    :param struct ata_port \*ap:
        Port to check

    :param const struct ata_acpi_gtm \*gtm:
        GTM data to use

.. _`ata_acpi_cbl_80wire.description`:

Description
-----------

Return 1 if the \ ``gtm``\  indicates the BIOS selected an 80wire mode.

.. _`ata_acpi_run_tf`:

ata_acpi_run_tf
===============

.. c:function:: int ata_acpi_run_tf(struct ata_device *dev, const struct ata_acpi_gtf *gtf, const struct ata_acpi_gtf *prev_gtf)

    send taskfile registers to host controller

    :param struct ata_device \*dev:
        target ATA device

    :param const struct ata_acpi_gtf \*gtf:
        raw ATA taskfile register set (0x1f1 - 0x1f7)

    :param const struct ata_acpi_gtf \*prev_gtf:
        *undescribed*

.. _`ata_acpi_run_tf.description`:

Description
-----------

Outputs ATA taskfile to standard ATA host controller.
Writes the control, feature, nsect, lbal, lbam, and lbah registers.
Optionally (ATA_TFLAG_LBA48) writes hob_feature, hob_nsect,
hob_lbal, hob_lbam, and hob_lbah.

This function waits for idle (!BUSY and !DRQ) after writing
registers.  If the control register has a new value, this
function also waits for idle after writing control and before
writing the remaining registers.

.. _`ata_acpi_run_tf.locking`:

LOCKING
-------

EH context.

.. _`ata_acpi_run_tf.return`:

Return
------

1 if command is executed successfully.  0 if ignored, rejected or
filtered out, -errno on other errors.

.. _`ata_acpi_exec_tfs`:

ata_acpi_exec_tfs
=================

.. c:function:: int ata_acpi_exec_tfs(struct ata_device *dev, int *nr_executed)

    get then write drive taskfile settings

    :param struct ata_device \*dev:
        target ATA device

    :param int \*nr_executed:
        out parameter for the number of executed commands

.. _`ata_acpi_exec_tfs.description`:

Description
-----------

Evaluate \_GTF and execute returned taskfiles.

.. _`ata_acpi_exec_tfs.locking`:

LOCKING
-------

EH context.

.. _`ata_acpi_exec_tfs.return`:

Return
------

Number of executed taskfiles on success, 0 if \_GTF doesn't exist.
-errno on other errors.

.. _`ata_acpi_push_id`:

ata_acpi_push_id
================

.. c:function:: int ata_acpi_push_id(struct ata_device *dev)

    send Identify data to drive

    :param struct ata_device \*dev:
        target ATA device

.. _`ata_acpi_push_id._sdd-acpi-object`:

\_SDD ACPI object
-----------------

for SATA mode only
Must be after Identify (Packet) Device -- uses its data
ATM this function never returns a failure.  It is an optional
method and if it fails for whatever reason, we should still
just keep going.

.. _`ata_acpi_push_id.locking`:

LOCKING
-------

EH context.

.. _`ata_acpi_push_id.return`:

Return
------

0 on success, -ENOENT if \_SDD doesn't exist, -errno on failure.

.. _`ata_acpi_on_suspend`:

ata_acpi_on_suspend
===================

.. c:function:: int ata_acpi_on_suspend(struct ata_port *ap)

    ATA ACPI hook called on suspend

    :param struct ata_port \*ap:
        target ATA port

.. _`ata_acpi_on_suspend.description`:

Description
-----------

This function is called when \ ``ap``\  is about to be suspended.  All
devices are already put to sleep but the \ :c:func:`port_suspend`\  callback
hasn't been executed yet.  Error return from this function aborts
suspend.

.. _`ata_acpi_on_suspend.locking`:

LOCKING
-------

EH context.

.. _`ata_acpi_on_suspend.return`:

Return
------

0 on success, -errno on failure.

.. _`ata_acpi_on_resume`:

ata_acpi_on_resume
==================

.. c:function:: void ata_acpi_on_resume(struct ata_port *ap)

    ATA ACPI hook called on resume

    :param struct ata_port \*ap:
        target ATA port

.. _`ata_acpi_on_resume.description`:

Description
-----------

This function is called when \ ``ap``\  is resumed - right after port
itself is resumed but before any EH action is taken.

.. _`ata_acpi_on_resume.locking`:

LOCKING
-------

EH context.

.. _`ata_acpi_set_state`:

ata_acpi_set_state
==================

.. c:function:: void ata_acpi_set_state(struct ata_port *ap, pm_message_t state)

    set the port power state

    :param struct ata_port \*ap:
        target ATA port

    :param pm_message_t state:
        state, on/off

.. _`ata_acpi_set_state.description`:

Description
-----------

This function sets a proper ACPI D state for the device on
system and runtime PM operations.

.. _`ata_acpi_on_devcfg`:

ata_acpi_on_devcfg
==================

.. c:function:: int ata_acpi_on_devcfg(struct ata_device *dev)

    ATA ACPI hook called on device donfiguration

    :param struct ata_device \*dev:
        target ATA device

.. _`ata_acpi_on_devcfg.description`:

Description
-----------

This function is called when \ ``dev``\  is about to be configured.
IDENTIFY data might have been modified after this hook is run.

.. _`ata_acpi_on_devcfg.locking`:

LOCKING
-------

EH context.

.. _`ata_acpi_on_devcfg.return`:

Return
------

Positive number if IDENTIFY data needs to be refreshed, 0 if not,
-errno on failure.

.. _`ata_acpi_on_disable`:

ata_acpi_on_disable
===================

.. c:function:: void ata_acpi_on_disable(struct ata_device *dev)

    ATA ACPI hook called when a device is disabled

    :param struct ata_device \*dev:
        target ATA device

.. _`ata_acpi_on_disable.description`:

Description
-----------

This function is called when \ ``dev``\  is about to be disabled.

.. _`ata_acpi_on_disable.locking`:

LOCKING
-------

EH context.

.. This file was automatic generated / don't edit.

