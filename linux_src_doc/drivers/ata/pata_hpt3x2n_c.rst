.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_hpt3x2n.c

.. _`hpt3x2n_find_mode`:

hpt3x2n_find_mode
=================

.. c:function:: u32 hpt3x2n_find_mode(struct ata_port *ap, int speed)

    reset the hpt3x2n bus

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param speed:
        transfer mode
    :type speed: int

.. _`hpt3x2n_find_mode.description`:

Description
-----------

Return the 32bit register programming information for this channel
that matches the speed provided. For the moment the clocks table
is hard coded but easy to change. This will be needed if we use
different DPLLs

.. _`hpt372n_filter`:

hpt372n_filter
==============

.. c:function:: unsigned long hpt372n_filter(struct ata_device *adev, unsigned long mask)

    mode selection filter

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param mask:
        mode mask
    :type mask: unsigned long

.. _`hpt372n_filter.description`:

Description
-----------

The Marvell bridge chips used on the HighPoint SATA cards do not seem
to support the UltraDMA modes 1, 2, and 3 as well as any MWDMA modes...

.. _`hpt3x2n_cable_detect`:

hpt3x2n_cable_detect
====================

.. c:function:: int hpt3x2n_cable_detect(struct ata_port *ap)

    Detect the cable type

    :param ap:
        ATA port to detect on
    :type ap: struct ata_port \*

.. _`hpt3x2n_cable_detect.description`:

Description
-----------

Return the cable type attached to this port

.. _`hpt3x2n_pre_reset`:

hpt3x2n_pre_reset
=================

.. c:function:: int hpt3x2n_pre_reset(struct ata_link *link, unsigned long deadline)

    reset the hpt3x2n bus

    :param link:
        ATA link to reset
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`hpt3x2n_pre_reset.description`:

Description
-----------

Perform the initial reset handling for the 3x2n series controllers.
Reset the hardware and state machine,

.. _`hpt3x2n_set_piomode`:

hpt3x2n_set_piomode
===================

.. c:function:: void hpt3x2n_set_piomode(struct ata_port *ap, struct ata_device *adev)

    PIO setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        device on the interface
    :type adev: struct ata_device \*

.. _`hpt3x2n_set_piomode.description`:

Description
-----------

Perform PIO mode setup.

.. _`hpt3x2n_set_dmamode`:

hpt3x2n_set_dmamode
===================

.. c:function:: void hpt3x2n_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    DMA timing setup

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        Device being configured
    :type adev: struct ata_device \*

.. _`hpt3x2n_set_dmamode.description`:

Description
-----------

Set up the channel for MWDMA or UDMA modes.

.. _`hpt3x2n_bmdma_stop`:

hpt3x2n_bmdma_stop
==================

.. c:function:: void hpt3x2n_bmdma_stop(struct ata_queued_cmd *qc)

    DMA engine stop

    :param qc:
        ATA command
    :type qc: struct ata_queued_cmd \*

.. _`hpt3x2n_bmdma_stop.description`:

Description
-----------

Clean up after the HPT3x2n and later DMA engine

.. _`hpt3x2n_set_clock`:

hpt3x2n_set_clock
=================

.. c:function:: void hpt3x2n_set_clock(struct ata_port *ap, int source)

    clock control

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param source:
        0x21 or 0x23 for PLL or PCI sourced clock
    :type source: int

.. _`hpt3x2n_set_clock.description`:

Description
-----------

Switch the ATA bus clock between the PLL and PCI clock sources
while correctly isolating the bus and resetting internal logic

We must use the DPLL for
-       writing
-       second channel UDMA7 (SATA ports) or higher
-       66MHz PCI

or we will underclock the device and get reduced performance.

.. _`hpt3xn_calibrate_dpll`:

hpt3xn_calibrate_dpll
=====================

.. c:function:: int hpt3xn_calibrate_dpll(struct pci_dev *dev)

    Calibrate the DPLL loop

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`hpt3xn_calibrate_dpll.description`:

Description
-----------

Perform a calibration cycle on the HPT3xN DPLL. Returns 1 if this
succeeds

.. _`hpt3x2n_init_one`:

hpt3x2n_init_one
================

.. c:function:: int hpt3x2n_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    Initialise an HPT37X/302

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

    :param id:
        Entry in match table
    :type id: const struct pci_device_id \*

.. _`hpt3x2n_init_one.description`:

Description
-----------

Initialise an HPT3x2n device. There are some interesting complications
here. Firstly the chip may report 366 and be one of several variants.
Secondly all the timings depend on the clock for the chip which we must
detect and look up

This is the known chip mappings. It may be missing a couple of later
releases.

Chip version            PCI             Rev     Notes
HPT372                  4 (HPT366)      5       Other driver
HPT372N                 4 (HPT366)      6       UDMA133
HPT372                  5 (HPT372)      1       Other driver
HPT372N                 5 (HPT372)      2       UDMA133
HPT302                  6 (HPT302)      \*       Other driver
HPT302N                 6 (HPT302)      > 1     UDMA133
HPT371                  7 (HPT371)      \*       Other driver
HPT371N                 7 (HPT371)      > 1     UDMA133
HPT374                  8 (HPT374)      \*       Other driver
HPT372N                 9 (HPT372N)     \*       UDMA133

(1) UDMA133 support depends on the bus clock

.. This file was automatic generated / don't edit.

