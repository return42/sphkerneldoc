.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/siimage.c

.. _`pdev_is_sata`:

pdev_is_sata
============

.. c:function:: int pdev_is_sata(struct pci_dev *pdev)

    check if device is SATA

    :param pdev:
        PCI device to check
    :type pdev: struct pci_dev \*

.. _`pdev_is_sata.description`:

Description
-----------

Returns true if this is a SATA controller

.. _`is_sata`:

is_sata
=======

.. c:function:: int is_sata(ide_hwif_t *hwif)

    check if hwif is SATA

    :param hwif:
        interface to check
    :type hwif: ide_hwif_t \*

.. _`is_sata.description`:

Description
-----------

Returns true if this is a SATA controller

.. _`siimage_selreg`:

siimage_selreg
==============

.. c:function:: unsigned long siimage_selreg(ide_hwif_t *hwif, int r)

    return register base

    :param hwif:
        interface
    :type hwif: ide_hwif_t \*

    :param r:
        config offset
    :type r: int

.. _`siimage_selreg.description`:

Description
-----------

Turn a config register offset into the right address in either
PCI space or MMIO space to access the control register in question
Thankfully this is a configuration operation, so isn't performance
critical.

.. _`siimage_seldev`:

siimage_seldev
==============

.. c:function:: unsigned long siimage_seldev(ide_drive_t *drive, int r)

    return register base

    :param drive:
        *undescribed*
    :type drive: ide_drive_t \*

    :param r:
        config offset
    :type r: int

.. _`siimage_seldev.description`:

Description
-----------

Turn a config register offset into the right address in either
PCI space or MMIO space to access the control register in question
including accounting for the unit shift.

.. _`sil_pata_udma_filter`:

sil_pata_udma_filter
====================

.. c:function:: u8 sil_pata_udma_filter(ide_drive_t *drive)

    compute UDMA mask

    :param drive:
        IDE device
    :type drive: ide_drive_t \*

.. _`sil_pata_udma_filter.description`:

Description
-----------

Compute the available UDMA speeds for the device on the interface.

For the CMD680 this depends on the clocking mode (scsc), for the
SI3112 SATA controller life is a bit simpler.

.. _`sil_set_pio_mode`:

sil_set_pio_mode
================

.. c:function:: void sil_set_pio_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for PIO mode

    :param hwif:
        port
    :type hwif: ide_hwif_t \*

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`sil_set_pio_mode.description`:

Description
-----------

Load the timing settings for this device mode into the
controller.

.. _`sil_set_dma_mode`:

sil_set_dma_mode
================

.. c:function:: void sil_set_dma_mode(ide_hwif_t *hwif, ide_drive_t *drive)

    set host controller for DMA mode

    :param hwif:
        port
    :type hwif: ide_hwif_t \*

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`sil_set_dma_mode.description`:

Description
-----------

Tune the SiI chipset for the desired DMA mode.

.. _`siimage_mmio_dma_test_irq`:

siimage_mmio_dma_test_irq
=========================

.. c:function:: int siimage_mmio_dma_test_irq(ide_drive_t *drive)

    check we caused an IRQ

    :param drive:
        drive we are testing
    :type drive: ide_drive_t \*

.. _`siimage_mmio_dma_test_irq.description`:

Description
-----------

Check if we caused an IDE DMA interrupt. We may also have caused
SATA status interrupts, if so we clean them up and continue.

.. _`sil_sata_reset_poll`:

sil_sata_reset_poll
===================

.. c:function:: blk_status_t sil_sata_reset_poll(ide_drive_t *drive)

    wait for SATA reset

    :param drive:
        drive we are resetting
    :type drive: ide_drive_t \*

.. _`sil_sata_reset_poll.description`:

Description
-----------

Poll the SATA phy and see whether it has come back from the dead
yet.

.. _`sil_sata_pre_reset`:

sil_sata_pre_reset
==================

.. c:function:: void sil_sata_pre_reset(ide_drive_t *drive)

    reset hook

    :param drive:
        IDE device being reset
    :type drive: ide_drive_t \*

.. _`sil_sata_pre_reset.description`:

Description
-----------

For the SATA devices we need to handle recalibration/geometry
differently

.. _`init_chipset_siimage`:

init_chipset_siimage
====================

.. c:function:: int init_chipset_siimage(struct pci_dev *dev)

    set up an SI device

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`init_chipset_siimage.description`:

Description
-----------

Perform the initial PCI set up for this device. Attempt to switch
to 133 MHz clocking if the system isn't already set up to do it.

.. _`init_mmio_iops_siimage`:

init_mmio_iops_siimage
======================

.. c:function:: void init_mmio_iops_siimage(ide_hwif_t *hwif)

    set up the iops for MMIO

    :param hwif:
        interface to set up
    :type hwif: ide_hwif_t \*

.. _`init_mmio_iops_siimage.description`:

Description
-----------

The basic setup here is fairly simple, we can use standard MMIO
operations. However we do have to set the taskfile register offsets
by hand as there isn't a standard defined layout for them this time.

The hardware supports buffered taskfiles and also some rather nice
extended PRD tables. For better SI3112 support use the libata driver

.. _`sil_quirkproc`:

sil_quirkproc
=============

.. c:function:: void sil_quirkproc(ide_drive_t *drive)

    post probe fixups

    :param drive:
        drive
    :type drive: ide_drive_t \*

.. _`sil_quirkproc.description`:

Description
-----------

Called after drive probe we use this to decide whether the
Seagate fixup must be applied. This used to be in init_iops but
that can occur before we know what drives are present.

.. _`init_iops_siimage`:

init_iops_siimage
=================

.. c:function:: void init_iops_siimage(ide_hwif_t *hwif)

    set up iops

    :param hwif:
        interface to set up
    :type hwif: ide_hwif_t \*

.. _`init_iops_siimage.description`:

Description
-----------

Do the basic setup for the SIIMAGE hardware interface
and then do the MMIO setup if we can. This is the first
look in we get for setting up the hwif so that we
can get the iops right before using them.

.. _`sil_cable_detect`:

sil_cable_detect
================

.. c:function:: u8 sil_cable_detect(ide_hwif_t *hwif)

    cable detection

    :param hwif:
        interface to check
    :type hwif: ide_hwif_t \*

.. _`sil_cable_detect.description`:

Description
-----------

Check for the presence of an ATA66 capable cable on the interface.

.. _`siimage_init_one`:

siimage_init_one
================

.. c:function:: int siimage_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    PCI layer discovery entry

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

    :param id:
        ident table entry
    :type id: const struct pci_device_id \*

.. _`siimage_init_one.description`:

Description
-----------

Called by the PCI code when it finds an SiI680 or SiI3112 controller.
We then use the IDE PCI generic helper to do most of the work.

.. This file was automatic generated / don't edit.

