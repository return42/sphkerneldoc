.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-dma-sff.c

.. _`config_drive_for_dma`:

config_drive_for_dma
====================

.. c:function:: int config_drive_for_dma(ide_drive_t *drive)

    attempt to activate IDE DMA

    :param ide_drive_t \*drive:
        the drive to place in DMA mode

.. _`config_drive_for_dma.description`:

Description
-----------

If the drive supports at least mode 2 DMA or UDMA of any kind
then attempt to place it into DMA mode. Drives that are known to
support DMA but predate the DMA properties or that are known
to have DMA handling bugs are also set up appropriately based
on the good/bad drive lists.

.. _`ide_dma_host_set`:

ide_dma_host_set
================

.. c:function:: void ide_dma_host_set(ide_drive_t *drive, int on)

    Enable/disable DMA on a host

    :param ide_drive_t \*drive:
        drive to control

    :param int on:
        *undescribed*

.. _`ide_dma_host_set.description`:

Description
-----------

Enable/disable DMA on an IDE controller following generic
bus-mastering IDE controller behaviour.

.. _`ide_build_dmatable`:

ide_build_dmatable
==================

.. c:function:: int ide_build_dmatable(ide_drive_t *drive, struct ide_cmd *cmd)

    build IDE DMA table

    :param ide_drive_t \*drive:
        *undescribed*

    :param struct ide_cmd \*cmd:
        *undescribed*

.. _`ide_build_dmatable.description`:

Description
-----------

ide_build_dmatable() prepares a dma request. We map the command
to get the pci bus addresses of the buffers and then build up
the PRD table that the IDE layer wants to be fed.

Most chipsets correctly interpret a length of 0x0000 as 64KB,
but at least one (e.g. CS5530) misinterprets it as zero (!).
So we break the 64KB entry into two 32KB entries instead.

Returns the number of built PRD entries if all went okay,
returns 0 otherwise.

May also be invoked from trm290.c

.. _`ide_dma_setup`:

ide_dma_setup
=============

.. c:function:: int ide_dma_setup(ide_drive_t *drive, struct ide_cmd *cmd)

    begin a DMA phase

    :param ide_drive_t \*drive:
        target device

    :param struct ide_cmd \*cmd:
        command

.. _`ide_dma_setup.description`:

Description
-----------

Build an IDE DMA PRD (IDE speak for scatter gather table)
and then set up the DMA transfer registers for a device
that follows generic IDE PCI DMA behaviour. Controllers can
override this function if they need to

Returns 0 on success. If a PIO fallback is required then 1
is returned.

.. _`ide_dma_sff_timer_expiry`:

ide_dma_sff_timer_expiry
========================

.. c:function:: int ide_dma_sff_timer_expiry(ide_drive_t *drive)

    handle a DMA timeout

    :param ide_drive_t \*drive:
        Drive that timed out

.. _`ide_dma_sff_timer_expiry.description`:

Description
-----------

An IDE DMA transfer timed out. In the event of an error we ask
the driver to resolve the problem, if a DMA transfer is still
in progress we continue to wait (arguably we need to add a
secondary 'I don't care what the drive thinks' timeout here)
Finally if we have an interrupt we let it complete the I/O.
But only one time - we clear expiry and if it's still not
completed after WAIT_CMD, we error and retry in PIO.
This can occur if an interrupt is lost or due to hang or bugs.

.. This file was automatic generated / don't edit.

