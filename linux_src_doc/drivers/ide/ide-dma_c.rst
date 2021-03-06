.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide-dma.c

.. _`ide_dma_intr`:

ide_dma_intr
============

.. c:function:: ide_startstop_t ide_dma_intr(ide_drive_t *drive)

    IDE DMA interrupt handler

    :param drive:
        the drive the interrupt is for
    :type drive: ide_drive_t \*

.. _`ide_dma_intr.description`:

Description
-----------

Handle an interrupt completing a read/write DMA transfer on an
IDE device

.. _`ide_dma_map_sg`:

ide_dma_map_sg
==============

.. c:function:: int ide_dma_map_sg(ide_drive_t *drive, struct ide_cmd *cmd)

    map IDE scatter gather for DMA I/O

    :param drive:
        the drive to map the DMA table for
    :type drive: ide_drive_t \*

    :param cmd:
        command
    :type cmd: struct ide_cmd \*

.. _`ide_dma_map_sg.description`:

Description
-----------

Perform the DMA mapping magic necessary to access the source or
target buffers of a request via DMA.  The lower layers of the
kernel provide the necessary cache management so that we can
operate in a portable fashion.

.. _`ide_dma_unmap_sg`:

ide_dma_unmap_sg
================

.. c:function:: void ide_dma_unmap_sg(ide_drive_t *drive, struct ide_cmd *cmd)

    clean up DMA mapping

    :param drive:
        The drive to unmap
    :type drive: ide_drive_t \*

    :param cmd:
        *undescribed*
    :type cmd: struct ide_cmd \*

.. _`ide_dma_unmap_sg.description`:

Description
-----------

Teardown mappings after DMA has completed. This must be called
after the completion of each use of ide_build_dmatable and before
the next use of ide_build_dmatable. Failure to do so will cause
an oops as only one mapping can be live for each target at a given
time.

.. _`ide_dma_off_quietly`:

ide_dma_off_quietly
===================

.. c:function:: void ide_dma_off_quietly(ide_drive_t *drive)

    Generic DMA kill

    :param drive:
        drive to control
    :type drive: ide_drive_t \*

.. _`ide_dma_off_quietly.description`:

Description
-----------

Turn off the current DMA on this IDE controller.

.. _`ide_dma_off`:

ide_dma_off
===========

.. c:function:: void ide_dma_off(ide_drive_t *drive)

    disable DMA on a device

    :param drive:
        drive to disable DMA on
    :type drive: ide_drive_t \*

.. _`ide_dma_off.description`:

Description
-----------

Disable IDE DMA for a device on this IDE controller.
Inform the user that DMA has been disabled.

.. _`ide_dma_on`:

ide_dma_on
==========

.. c:function:: void ide_dma_on(ide_drive_t *drive)

    Enable DMA on a device

    :param drive:
        drive to enable DMA on
    :type drive: ide_drive_t \*

.. _`ide_dma_on.description`:

Description
-----------

Enable IDE DMA for a device on this IDE controller.

.. _`ide_find_dma_mode`:

ide_find_dma_mode
=================

.. c:function:: u8 ide_find_dma_mode(ide_drive_t *drive, u8 req_mode)

    compute DMA speed

    :param drive:
        IDE device
    :type drive: ide_drive_t \*

    :param req_mode:
        requested mode
    :type req_mode: u8

.. _`ide_find_dma_mode.description`:

Description
-----------

Checks the drive/host capabilities and finds the speed to use for
the DMA transfer.  The speed is then limited by the requested mode.

Returns 0 if the drive/host combination is incapable of DMA transfers
or if the requested mode is not a DMA mode.

.. This file was automatic generated / don't edit.

