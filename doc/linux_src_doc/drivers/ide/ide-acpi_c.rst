.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-acpi.c

.. _`ide_get_dev_handle`:

ide_get_dev_handle
==================

.. c:function:: int ide_get_dev_handle(struct device *dev, acpi_handle *handle, u64 *pcidevfn)

    finds acpi_handle and PCI device.function

    :param struct device \*dev:
        device to locate

    :param acpi_handle \*handle:
        returned acpi_handle for \ ``dev``\ 

    :param u64 \*pcidevfn:
        return PCI device.func for \ ``dev``\ 

.. _`ide_get_dev_handle.description`:

Description
-----------

Returns the ACPI object handle to the corresponding PCI device.

Returns 0 on success, <0 on error.

.. _`ide_acpi_hwif_get_handle`:

ide_acpi_hwif_get_handle
========================

.. c:function:: acpi_handle ide_acpi_hwif_get_handle(ide_hwif_t *hwif)

    Get ACPI object handle for a given hwif

    :param ide_hwif_t \*hwif:
        device to locate

.. _`ide_acpi_hwif_get_handle.description`:

Description
-----------

Retrieves the object handle for a given hwif.

Returns handle on success, 0 on error.

.. _`do_drive_get_gtf`:

do_drive_get_GTF
================

.. c:function:: int do_drive_get_GTF(ide_drive_t *drive, unsigned int *gtf_length, unsigned long *gtf_address, unsigned long *obj_loc)

    get the drive bootup default taskfile settings

    :param ide_drive_t \*drive:
        the drive for which the taskfile settings should be retrieved

    :param unsigned int \*gtf_length:
        number of bytes of \_GTF data returned at \ ``gtf_address``\ 

    :param unsigned long \*gtf_address:
        buffer containing \_GTF taskfile arrays

    :param unsigned long \*obj_loc:
        *undescribed*

.. _`do_drive_get_gtf.description`:

Description
-----------

The \_GTF method has no input parameters.
It returns a variable number of register set values (registers
hex 1F1..1F7, taskfiles).
The <variable number> is not known in advance, so have ACPI-CA
allocate the buffer as needed and return it, then free it later.

The returned \ ``gtf_length``\  and \ ``gtf_address``\  are only valid if the
function return value is 0.

.. _`do_drive_set_taskfiles`:

do_drive_set_taskfiles
======================

.. c:function:: int do_drive_set_taskfiles(ide_drive_t *drive, unsigned int gtf_length, unsigned long gtf_address)

    write the drive taskfile settings from \_GTF

    :param ide_drive_t \*drive:
        the drive to which the taskfile command should be sent

    :param unsigned int gtf_length:
        total number of bytes of \_GTF taskfiles

    :param unsigned long gtf_address:
        location of \_GTF taskfile arrays

.. _`do_drive_set_taskfiles.description`:

Description
-----------

Write {gtf_address, length gtf_length} in groups of
REGS_PER_GTF bytes.

.. _`ide_acpi_exec_tfs`:

ide_acpi_exec_tfs
=================

.. c:function:: int ide_acpi_exec_tfs(ide_drive_t *drive)

    get then write drive taskfile settings

    :param ide_drive_t \*drive:
        the drive for which the taskfile settings should be
        written.

.. _`ide_acpi_exec_tfs.description`:

Description
-----------

According to the ACPI spec this should be called after \_STM
has been evaluated for the interface. Some ACPI vendors interpret
that as a hard requirement and modify the taskfile according
to the Identify Drive information passed down with \_STM.
So one should really make sure to call this only after \_STM has
been executed.

.. _`ide_acpi_get_timing`:

ide_acpi_get_timing
===================

.. c:function:: void ide_acpi_get_timing(ide_hwif_t *hwif)

    get the channel (controller) timings

    :param ide_hwif_t \*hwif:
        target IDE interface (channel)

.. _`ide_acpi_get_timing.description`:

Description
-----------

This function executes the \_GTM ACPI method for the target channel.

.. _`ide_acpi_push_timing`:

ide_acpi_push_timing
====================

.. c:function:: void ide_acpi_push_timing(ide_hwif_t *hwif)

    set the channel (controller) timings

    :param ide_hwif_t \*hwif:
        target IDE interface (channel)

.. _`ide_acpi_push_timing.description`:

Description
-----------

This function executes the \_STM ACPI method for the target channel.

\_STM requires Identify Drive data, which has to passed as an argument.
Unfortunately drive->id is a mangled version which we can't readily
use; hence we'll get the information afresh.

.. _`ide_acpi_set_state`:

ide_acpi_set_state
==================

.. c:function:: void ide_acpi_set_state(ide_hwif_t *hwif, int on)

    set the channel power state

    :param ide_hwif_t \*hwif:
        target IDE interface

    :param int on:
        state, on/off

.. _`ide_acpi_set_state.description`:

Description
-----------

This function executes the \_PS0/_PS3 ACPI method to set the power state.
ACPI spec requires \_PS0 when IDE power on and \_PS3 when power off

.. _`ide_acpi_init_port`:

ide_acpi_init_port
==================

.. c:function:: void ide_acpi_init_port(ide_hwif_t *hwif)

    initialize the ACPI link for an IDE interface

    :param ide_hwif_t \*hwif:
        target IDE interface (channel)

.. _`ide_acpi_init_port.description`:

Description
-----------

The ACPI spec is not quite clear when the drive identify buffer
should be obtained. Calling IDENTIFY DEVICE during shutdown
is not the best of ideas as the drive might already being put to
sleep. And obviously we can't call it during resume.
So we get the information during startup; but this means that
any changes during run-time will be lost after resume.

.. This file was automatic generated / don't edit.

