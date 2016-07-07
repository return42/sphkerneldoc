.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_hpt37x.c

.. _`hpt37x_find_mode`:

hpt37x_find_mode
================

.. c:function:: u32 hpt37x_find_mode(struct ata_port *ap, int speed)

    reset the hpt37x bus

    :param struct ata_port \*ap:
        ATA port

    :param int speed:
        transfer mode

.. _`hpt37x_find_mode.description`:

Description
-----------

Return the 32bit register programming information for this channel
that matches the speed provided.

.. _`hpt370_filter`:

hpt370_filter
=============

.. c:function:: unsigned long hpt370_filter(struct ata_device *adev, unsigned long mask)

    mode selection filter

    :param struct ata_device \*adev:
        ATA device

    :param unsigned long mask:
        *undescribed*

.. _`hpt370_filter.description`:

Description
-----------

Block UDMA on devices that cause trouble with this controller.

.. _`hpt370a_filter`:

hpt370a_filter
==============

.. c:function:: unsigned long hpt370a_filter(struct ata_device *adev, unsigned long mask)

    mode selection filter

    :param struct ata_device \*adev:
        ATA device

    :param unsigned long mask:
        *undescribed*

.. _`hpt370a_filter.description`:

Description
-----------

Block UDMA on devices that cause trouble with this controller.

.. _`hpt372_filter`:

hpt372_filter
=============

.. c:function:: unsigned long hpt372_filter(struct ata_device *adev, unsigned long mask)

    mode selection filter

    :param struct ata_device \*adev:
        ATA device

    :param unsigned long mask:
        mode mask

.. _`hpt372_filter.description`:

Description
-----------

The Marvell bridge chips used on the HighPoint SATA cards do not seem
to support the UltraDMA modes 1, 2, and 3 as well as any MWDMA modes...

.. _`hpt37x_cable_detect`:

hpt37x_cable_detect
===================

.. c:function:: int hpt37x_cable_detect(struct ata_port *ap)

    Detect the cable type

    :param struct ata_port \*ap:
        ATA port to detect on

.. _`hpt37x_cable_detect.description`:

Description
-----------

Return the cable type attached to this port

.. _`hpt374_fn1_cable_detect`:

hpt374_fn1_cable_detect
=======================

.. c:function:: int hpt374_fn1_cable_detect(struct ata_port *ap)

    Detect the cable type

    :param struct ata_port \*ap:
        ATA port to detect on

.. _`hpt374_fn1_cable_detect.description`:

Description
-----------

Return the cable type attached to this port

.. _`hpt37x_pre_reset`:

hpt37x_pre_reset
================

.. c:function:: int hpt37x_pre_reset(struct ata_link *link, unsigned long deadline)

    reset the hpt37x bus

    :param struct ata_link \*link:
        ATA link to reset

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`hpt37x_pre_reset.description`:

Description
-----------

Perform the initial reset handling for the HPT37x.

.. _`hpt370_set_piomode`:

hpt370_set_piomode
==================

.. c:function:: void hpt370_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        device on the interface

.. _`hpt370_set_piomode.description`:

Description
-----------

Perform PIO mode setup.

.. _`hpt370_set_dmamode`:

hpt370_set_dmamode
==================

.. c:function:: void hpt370_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        Device being configured

.. _`hpt370_set_dmamode.description`:

Description
-----------

Set up the channel for MWDMA or UDMA modes.

.. _`hpt370_bmdma_stop`:

hpt370_bmdma_stop
=================

.. c:function:: void hpt370_bmdma_stop(struct ata_queued_cmd *qc)

    DMA engine stop

    :param struct ata_queued_cmd \*qc:
        ATA command

.. _`hpt370_bmdma_stop.description`:

Description
-----------

Work around the HPT370 DMA engine.

.. _`hpt372_set_piomode`:

hpt372_set_piomode
==================

.. c:function:: void hpt372_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        device on the interface

.. _`hpt372_set_piomode.description`:

Description
-----------

Perform PIO mode setup.

.. _`hpt372_set_dmamode`:

hpt372_set_dmamode
==================

.. c:function:: void hpt372_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        Device being configured

.. _`hpt372_set_dmamode.description`:

Description
-----------

Set up the channel for MWDMA or UDMA modes.

.. _`hpt37x_bmdma_stop`:

hpt37x_bmdma_stop
=================

.. c:function:: void hpt37x_bmdma_stop(struct ata_queued_cmd *qc)

    DMA engine stop

    :param struct ata_queued_cmd \*qc:
        ATA command

.. _`hpt37x_bmdma_stop.description`:

Description
-----------

Clean up after the HPT372 and later DMA engine

.. _`hpt37x_clock_slot`:

hpt37x_clock_slot
=================

.. c:function:: int hpt37x_clock_slot(unsigned int freq, unsigned int base)

    Turn timing to PC clock entry

    :param unsigned int freq:
        Reported frequency timing

    :param unsigned int base:
        Base timing

.. _`hpt37x_clock_slot.description`:

Description
-----------

Turn the timing data intoa clock slot (0 for 33, 1 for 40, 2 for 50
and 3 for 66Mhz)

.. _`hpt37x_calibrate_dpll`:

hpt37x_calibrate_dpll
=====================

.. c:function:: int hpt37x_calibrate_dpll(struct pci_dev *dev)

    Calibrate the DPLL loop

    :param struct pci_dev \*dev:
        PCI device

.. _`hpt37x_calibrate_dpll.description`:

Description
-----------

Perform a calibration cycle on the HPT37x DPLL. Returns 1 if this
succeeds

.. _`hpt37x_init_one`:

hpt37x_init_one
===============

.. c:function:: int hpt37x_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    Initialise an HPT37X/302

    :param struct pci_dev \*dev:
        PCI device

    :param const struct pci_device_id \*id:
        Entry in match table

.. _`hpt37x_init_one.description`:

Description
-----------

Initialise an HPT37x device. There are some interesting complications
here. Firstly the chip may report 366 and be one of several variants.
Secondly all the timings depend on the clock for the chip which we must
detect and look up

This is the known chip mappings. It may be missing a couple of later
releases.

Chip version            PCI             Rev     Notes
HPT366                  4 (HPT366)      0       Other driver
HPT366                  4 (HPT366)      1       Other driver
HPT368                  4 (HPT366)      2       Other driver
HPT370                  4 (HPT366)      3       UDMA100
HPT370A                 4 (HPT366)      4       UDMA100
HPT372                  4 (HPT366)      5       UDMA133 (1)
HPT372N                 4 (HPT366)      6       Other driver
HPT372A                 5 (HPT372)      1       UDMA133 (1)
HPT372N                 5 (HPT372)      2       Other driver
HPT302                  6 (HPT302)      1       UDMA133
HPT302N                 6 (HPT302)      2       Other driver
HPT371                  7 (HPT371)      \*       UDMA133
HPT374                  8 (HPT374)      \*       UDMA133 4 channel
HPT372N                 9 (HPT372N)     \*       Other driver

(1) UDMA133 support depends on the bus clock

.. This file was automatic generated / don't edit.

