.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_hpt366.c

.. _`hpt36x_find_mode`:

hpt36x_find_mode
================

.. c:function:: u32 hpt36x_find_mode(struct ata_port *ap, int speed)

    find the hpt36x timing

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param speed:
        transfer mode
    :type speed: int

.. _`hpt36x_find_mode.description`:

Description
-----------

Return the 32bit register programming information for this channel
that matches the speed provided.

.. _`hpt366_filter`:

hpt366_filter
=============

.. c:function:: unsigned long hpt366_filter(struct ata_device *adev, unsigned long mask)

    mode selection filter

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param mask:
        *undescribed*
    :type mask: unsigned long

.. _`hpt366_filter.description`:

Description
-----------

Block UDMA on devices that cause trouble with this controller.

.. _`hpt366_set_piomode`:

hpt366_set_piomode
==================

.. c:function:: void hpt366_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        device on the interface
    :type adev: struct ata_device \*

.. _`hpt366_set_piomode.description`:

Description
-----------

Perform PIO mode setup.

.. _`hpt366_set_dmamode`:

hpt366_set_dmamode
==================

.. c:function:: void hpt366_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        Device being configured
    :type adev: struct ata_device \*

.. _`hpt366_set_dmamode.description`:

Description
-----------

Set up the channel for MWDMA or UDMA modes. Much the same as with
PIO, load the mode number and then set MWDMA or UDMA flag.

.. _`hpt36x_init_chipset`:

hpt36x_init_chipset
===================

.. c:function:: void hpt36x_init_chipset(struct pci_dev *dev)

    common chip setup

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`hpt36x_init_chipset.description`:

Description
-----------

Perform the chip setup work that must be done at both init and
resume time

.. _`hpt36x_init_one`:

hpt36x_init_one
===============

.. c:function:: int hpt36x_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    Initialise an HPT366/368

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

    :param id:
        Entry in match table
    :type id: const struct pci_device_id \*

.. _`hpt36x_init_one.description`:

Description
-----------

Initialise an HPT36x device. There are some interesting complications
here. Firstly the chip may report 366 and be one of several variants.
Secondly all the timings depend on the clock for the chip which we must
detect and look up

This is the known chip mappings. It may be missing a couple of later
releases.

Chip version            PCI             Rev     Notes
HPT366                  4 (HPT366)      0       UDMA66
HPT366                  4 (HPT366)      1       UDMA66
HPT368                  4 (HPT366)      2       UDMA66
HPT37x/30x              4 (HPT366)      3+      Other driver

.. This file was automatic generated / don't edit.

