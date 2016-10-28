.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/alim15x3.c

.. _`ali_set_pio_mode`:

ali_set_pio_mode
================

.. c:function:: void ali_set_pio_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for PIO mode

    :param ide_hwif_t \*hwif:
        port

    :param ide_drive_t \*drive:
        drive

.. _`ali_set_pio_mode.description`:

Description
-----------

Program the controller for the given PIO mode.

.. _`ali_udma_filter`:

ali_udma_filter
===============

.. c:function:: u8 ali_udma_filter(ide_drive_t *drive)

    compute UDMA mask

    :param ide_drive_t \*drive:
        IDE device

.. _`ali_udma_filter.description`:

Description
-----------

Return available UDMA modes.

.. _`ali_udma_filter.the-actual-rules-for-the-ali-are`:

The actual rules for the ALi are
--------------------------------

No UDMA on revisions <= 0x20
Disk only for revisions < 0xC2
Not WDC drives on M1543C-E (?)

.. _`ali_set_dma_mode`:

ali_set_dma_mode
================

.. c:function:: void ali_set_dma_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for DMA mode

    :param ide_hwif_t \*hwif:
        port

    :param ide_drive_t \*drive:
        drive

.. _`ali_set_dma_mode.description`:

Description
-----------

Configure the hardware for the desired IDE transfer mode.

.. _`ali_dma_check`:

ali_dma_check
=============

.. c:function:: int ali_dma_check(ide_drive_t *drive, struct ide_cmd *cmd)

    DMA check

    :param ide_drive_t \*drive:
        target device

    :param struct ide_cmd \*cmd:
        command

.. _`ali_dma_check.description`:

Description
-----------

Returns 1 if the DMA cannot be performed, zero on success.

.. _`init_chipset_ali15x3`:

init_chipset_ali15x3
====================

.. c:function:: int init_chipset_ali15x3(struct pci_dev *dev)

    Initialise an ALi IDE controller

    :param struct pci_dev \*dev:
        PCI device

.. _`init_chipset_ali15x3.description`:

Description
-----------

This function initializes the ALI IDE controller and where
appropriate also sets up the 1533 southbridge.

.. _`ali_cable_detect`:

ali_cable_detect
================

.. c:function:: u8 ali_cable_detect(ide_hwif_t *hwif)

    cable detection

    :param ide_hwif_t \*hwif:
        IDE interface

.. _`ali_cable_detect.description`:

Description
-----------

This checks if the controller and the cable are capable
of UDMA66 transfers. It doesn't check the drives.

.. _`init_hwif_ali15x3`:

init_hwif_ali15x3
=================

.. c:function:: void init_hwif_ali15x3(ide_hwif_t *hwif)

    Initialize the ALI IDE x86 stuff

    :param ide_hwif_t \*hwif:
        interface to configure

.. _`init_hwif_ali15x3.description`:

Description
-----------

Obtain the IRQ tables for an ALi based IDE solution on the PC
class platforms. This part of the code isn't applicable to the
Sparc systems.

.. _`init_dma_ali15x3`:

init_dma_ali15x3
================

.. c:function:: int init_dma_ali15x3(ide_hwif_t *hwif, const struct ide_port_info *d)

    set up DMA on ALi15x3

    :param ide_hwif_t \*hwif:
        IDE interface

    :param const struct ide_port_info \*d:
        IDE port info

.. _`init_dma_ali15x3.description`:

Description
-----------

Set up the DMA functionality on the ALi 15x3.

.. _`alim15x3_init_one`:

alim15x3_init_one
=================

.. c:function:: int alim15x3_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    set up an ALi15x3 IDE controller

    :param struct pci_dev \*dev:
        PCI device to set up

    :param const struct pci_device_id \*id:
        *undescribed*

.. _`alim15x3_init_one.description`:

Description
-----------

Perform the actual set up for an ALi15x3 that has been found by the
hot plug layer.

.. This file was automatic generated / don't edit.

