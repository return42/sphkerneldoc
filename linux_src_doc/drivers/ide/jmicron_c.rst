.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/jmicron.c

.. _`jmicron_cable_detect`:

jmicron_cable_detect
====================

.. c:function:: u8 jmicron_cable_detect(ide_hwif_t *hwif)

    cable detection

    :param ide_hwif_t \*hwif:
        IDE port

.. _`jmicron_cable_detect.description`:

Description
-----------

Returns the cable type.

.. _`jmicron_set_dma_mode`:

jmicron_set_dma_mode
====================

.. c:function:: void jmicron_set_dma_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for DMA mode

    :param ide_hwif_t \*hwif:
        port

    :param ide_drive_t \*drive:
        drive

.. _`jmicron_set_dma_mode.description`:

Description
-----------

As the JMicron snoops for timings we don't need to do anything here.

.. _`jmicron_init_one`:

jmicron_init_one
================

.. c:function:: int jmicron_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    pci layer discovery entry

    :param struct pci_dev \*dev:
        PCI device

    :param const struct pci_device_id \*id:
        ident table entry

.. _`jmicron_init_one.description`:

Description
-----------

Called by the PCI code when it finds a Jmicron controller.
We then use the IDE PCI generic helper to do most of the work.

.. This file was automatic generated / don't edit.

