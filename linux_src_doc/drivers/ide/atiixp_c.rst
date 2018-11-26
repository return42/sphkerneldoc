.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/atiixp.c

.. _`atiixp_set_pio_mode`:

atiixp_set_pio_mode
===================

.. c:function:: void atiixp_set_pio_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for PIO mode

    :param hwif:
        port
    :type hwif: ide_hwif_t \*

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`atiixp_set_pio_mode.description`:

Description
-----------

Set the interface PIO mode.

.. _`atiixp_set_dma_mode`:

atiixp_set_dma_mode
===================

.. c:function:: void atiixp_set_dma_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for DMA mode

    :param hwif:
        port
    :type hwif: ide_hwif_t \*

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`atiixp_set_dma_mode.description`:

Description
-----------

Set a ATIIXP host controller to the desired DMA mode.  This involves
programming the right timing data into the PCI configuration space.

.. _`atiixp_init_one`:

atiixp_init_one
===============

.. c:function:: int atiixp_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    called when a ATIIXP is found

    :param dev:
        the atiixp device
    :type dev: struct pci_dev \*

    :param id:
        the matching pci id
    :type id: const struct pci_device_id \*

.. _`atiixp_init_one.description`:

Description
-----------

Called when the PCI registration layer (or the IDE initialization)
finds a device matching our IDE device tables.

.. This file was automatic generated / don't edit.

