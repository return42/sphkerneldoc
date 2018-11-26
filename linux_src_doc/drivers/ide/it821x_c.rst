.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/it821x.c

.. _`it821x_program`:

it821x_program
==============

.. c:function:: void it821x_program(ide_drive_t *drive, u16 timing)

    program the PIO/MWDMA registers

    :param drive:
        drive to tune
    :type drive: ide_drive_t \*

    :param timing:
        timing info
    :type timing: u16

.. _`it821x_program.description`:

Description
-----------

Program the PIO/MWDMA timing for this channel according to the
current clock.

.. _`it821x_program_udma`:

it821x_program_udma
===================

.. c:function:: void it821x_program_udma(ide_drive_t *drive, u16 timing)

    program the UDMA registers

    :param drive:
        drive to tune
    :type drive: ide_drive_t \*

    :param timing:
        timing info
    :type timing: u16

.. _`it821x_program_udma.description`:

Description
-----------

Program the UDMA timing for this drive according to the
current clock.

.. _`it821x_clock_strategy`:

it821x_clock_strategy
=====================

.. c:function:: void it821x_clock_strategy(ide_drive_t *drive)

    :param drive:
        drive to set up
    :type drive: ide_drive_t \*

.. _`it821x_clock_strategy.description`:

Description
-----------

Select between the 50 and 66Mhz base clocks to get the best
results for this interface.

.. _`it821x_set_pio_mode`:

it821x_set_pio_mode
===================

.. c:function:: void it821x_set_pio_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for PIO mode

    :param hwif:
        port
    :type hwif: ide_hwif_t \*

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`it821x_set_pio_mode.description`:

Description
-----------

Tune the host to the desired PIO mode taking into the consideration
the maximum PIO mode supported by the other device on the cable.

.. _`it821x_tune_mwdma`:

it821x_tune_mwdma
=================

.. c:function:: void it821x_tune_mwdma(ide_drive_t *drive, u8 mode_wanted)

    tune a channel for MWDMA

    :param drive:
        drive to set up
    :type drive: ide_drive_t \*

    :param mode_wanted:
        the target operating mode
    :type mode_wanted: u8

.. _`it821x_tune_mwdma.description`:

Description
-----------

Load the timing settings for this device mode into the
controller when doing MWDMA in pass through mode. The caller
must manage the whole lack of per device MWDMA/PIO timings and
the shared MWDMA/PIO timing register.

.. _`it821x_tune_udma`:

it821x_tune_udma
================

.. c:function:: void it821x_tune_udma(ide_drive_t *drive, u8 mode_wanted)

    tune a channel for UDMA

    :param drive:
        drive to set up
    :type drive: ide_drive_t \*

    :param mode_wanted:
        the target operating mode
    :type mode_wanted: u8

.. _`it821x_tune_udma.description`:

Description
-----------

Load the timing settings for this device mode into the
controller when doing UDMA modes in pass through.

.. _`it821x_dma_start`:

it821x_dma_start
================

.. c:function:: void it821x_dma_start(ide_drive_t *drive)

    DMA hook

    :param drive:
        drive for DMA
    :type drive: ide_drive_t \*

.. _`it821x_dma_start.description`:

Description
-----------

The IT821x has a single timing register for MWDMA and for PIO
operations. As we flip back and forth we have to reload the
clock. In addition the rev 0x10 device only works if the same
timing value is loaded into the master and slave UDMA clock
so we must also reload that.

.. _`it821x_dma_start.fixme`:

FIXME
-----

we could figure out in advance if we need to do reloads

.. _`it821x_dma_end`:

it821x_dma_end
==============

.. c:function:: int it821x_dma_end(ide_drive_t *drive)

    DMA hook

    :param drive:
        drive for DMA stop
    :type drive: ide_drive_t \*

.. _`it821x_dma_end.description`:

Description
-----------

The IT821x has a single timing register for MWDMA and for PIO
operations. As we flip back and forth we have to reload the
clock.

.. _`it821x_set_dma_mode`:

it821x_set_dma_mode
===================

.. c:function:: void it821x_set_dma_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for DMA mode

    :param hwif:
        port
    :type hwif: ide_hwif_t \*

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`it821x_set_dma_mode.description`:

Description
-----------

Tune the ITE chipset for the desired DMA mode.

.. _`it821x_cable_detect`:

it821x_cable_detect
===================

.. c:function:: u8 it821x_cable_detect(ide_hwif_t *hwif)

    cable detection

    :param hwif:
        interface to check
    :type hwif: ide_hwif_t \*

.. _`it821x_cable_detect.description`:

Description
-----------

Check for the presence of an ATA66 capable cable on the
interface. Problematic as it seems some cards don't have
the needed logic onboard.

.. _`it821x_quirkproc`:

it821x_quirkproc
================

.. c:function:: void it821x_quirkproc(ide_drive_t *drive)

    post init callback

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`it821x_quirkproc.description`:

Description
-----------

This callback is run after the drive has been probed but
before anything gets attached. It allows drivers to do any
final tuning that is needed, or fixups to work around bugs.

.. _`init_hwif_it821x`:

init_hwif_it821x
================

.. c:function:: void init_hwif_it821x(ide_hwif_t *hwif)

    set up hwif structs

    :param hwif:
        interface to set up
    :type hwif: ide_hwif_t \*

.. _`init_hwif_it821x.description`:

Description
-----------

We do the basic set up of the interface structure. The IT8212
requires several custom handlers so we override the default
ide DMA handlers appropriately

.. _`it821x_init_one`:

it821x_init_one
===============

.. c:function:: int it821x_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    pci layer discovery entry

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

    :param id:
        ident table entry
    :type id: const struct pci_device_id \*

.. _`it821x_init_one.description`:

Description
-----------

Called by the PCI code when it finds an ITE821x controller.
We then use the IDE PCI generic helper to do most of the work.

.. This file was automatic generated / don't edit.

