.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_hpt3x3.c

.. _`hpt3x3_set_piomode`:

hpt3x3_set_piomode
==================

.. c:function:: void hpt3x3_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        device on the interface
    :type adev: struct ata_device \*

.. _`hpt3x3_set_piomode.description`:

Description
-----------

Set our PIO requirements. This is fairly simple on the HPT3x3 as
all we have to do is clear the MWDMA and UDMA bits then load the
mode number.

.. _`hpt3x3_set_dmamode`:

hpt3x3_set_dmamode
==================

.. c:function:: void hpt3x3_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        Device being configured
    :type adev: struct ata_device \*

.. _`hpt3x3_set_dmamode.description`:

Description
-----------

Set up the channel for MWDMA or UDMA modes. Much the same as with
PIO, load the mode number and then set MWDMA or UDMA flag.

0x44 : bit 0-2 master mode, 3-5 slave mode, etc
0x48 : bit 4/0 DMA/UDMA bit 5/1 for slave etc

.. _`hpt3x3_freeze`:

hpt3x3_freeze
=============

.. c:function:: void hpt3x3_freeze(struct ata_port *ap)

    DMA workaround

    :param ap:
        port to freeze
    :type ap: struct ata_port \*

.. _`hpt3x3_freeze.description`:

Description
-----------

When freezing an HPT3x3 we must stop any pending DMA before
writing to the control register or the chip will hang

.. _`hpt3x3_bmdma_setup`:

hpt3x3_bmdma_setup
==================

.. c:function:: void hpt3x3_bmdma_setup(struct ata_queued_cmd *qc)

    DMA workaround

    :param qc:
        Queued command
    :type qc: struct ata_queued_cmd \*

.. _`hpt3x3_bmdma_setup.description`:

Description
-----------

When issuing BMDMA we must clean up the error/active bits in
software on this device

.. _`hpt3x3_atapi_dma`:

hpt3x3_atapi_dma
================

.. c:function:: int hpt3x3_atapi_dma(struct ata_queued_cmd *qc)

    ATAPI DMA check

    :param qc:
        Queued command
    :type qc: struct ata_queued_cmd \*

.. _`hpt3x3_atapi_dma.description`:

Description
-----------

Just say no - we don't do ATAPI DMA

.. _`hpt3x3_init_chipset`:

hpt3x3_init_chipset
===================

.. c:function:: void hpt3x3_init_chipset(struct pci_dev *dev)

    chip setup

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`hpt3x3_init_chipset.description`:

Description
-----------

Perform the setup required at boot and on resume.

.. _`hpt3x3_init_one`:

hpt3x3_init_one
===============

.. c:function:: int hpt3x3_init_one(struct pci_dev *pdev, const struct pci_device_id *id)

    Initialise an HPT343/363

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param id:
        Entry in match table
    :type id: const struct pci_device_id \*

.. _`hpt3x3_init_one.description`:

Description
-----------

Perform basic initialisation. We set the device up so we access all
ports via BAR4. This is necessary to work around errata.

.. This file was automatic generated / don't edit.

