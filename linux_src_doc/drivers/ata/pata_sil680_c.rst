.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_sil680.c

.. _`sil680_selreg`:

sil680_selreg
=============

.. c:function:: unsigned long sil680_selreg(struct ata_port *ap, int r)

    return register base

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param r:
        config offset
    :type r: int

.. _`sil680_selreg.description`:

Description
-----------

Turn a config register offset into the right address in PCI space
to access the control register in question.

Thankfully this is a configuration operation so isn't performance
criticial.

.. _`sil680_seldev`:

sil680_seldev
=============

.. c:function:: unsigned long sil680_seldev(struct ata_port *ap, struct ata_device *adev, int r)

    return register base

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        *undescribed*
    :type adev: struct ata_device \*

    :param r:
        config offset
    :type r: int

.. _`sil680_seldev.description`:

Description
-----------

Turn a config register offset into the right address in PCI space
to access the control register in question including accounting for
the unit shift.

.. _`sil680_cable_detect`:

sil680_cable_detect
===================

.. c:function:: int sil680_cable_detect(struct ata_port *ap)

    cable detection

    :param ap:
        ATA port
    :type ap: struct ata_port \*

.. _`sil680_cable_detect.description`:

Description
-----------

Perform cable detection. The SIL680 stores this in PCI config
space for us.

.. _`sil680_set_piomode`:

sil680_set_piomode
==================

.. c:function:: void sil680_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set PIO mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`sil680_set_piomode.description`:

Description
-----------

Program the SIL680 registers for PIO mode. Note that the task speed
registers are shared between the devices so we must pick the lowest
mode for command work.

.. _`sil680_set_dmamode`:

sil680_set_dmamode
==================

.. c:function:: void sil680_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set DMA mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`sil680_set_dmamode.description`:

Description
-----------

Program the MWDMA/UDMA modes for the sil680 chipset.

The MWDMA mode values are pulled from a lookup table
while the chipset uses mode number for UDMA.

.. _`sil680_sff_exec_command`:

sil680_sff_exec_command
=======================

.. c:function:: void sil680_sff_exec_command(struct ata_port *ap, const struct ata_taskfile *tf)

    issue ATA command to host controller

    :param ap:
        port to which command is being issued
    :type ap: struct ata_port \*

    :param tf:
        ATA taskfile register set
    :type tf: const struct ata_taskfile \*

.. _`sil680_sff_exec_command.description`:

Description
-----------

Issues ATA command, with proper synchronization with interrupt
handler / other threads. Use our MMIO space for PCI posting to avoid
a hideously slow cycle all the way to the device.

.. _`sil680_sff_exec_command.locking`:

LOCKING
-------

spin_lock_irqsave(host lock)

.. _`sil680_init_chip`:

sil680_init_chip
================

.. c:function:: u8 sil680_init_chip(struct pci_dev *pdev, int *try_mmio)

    chip setup

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param try_mmio:
        *undescribed*
    :type try_mmio: int \*

.. _`sil680_init_chip.description`:

Description
-----------

Perform all the chip setup which must be done both when the device
is powered up on boot and when we resume in case we resumed from RAM.
Returns the final clock settings.

.. This file was automatic generated / don't edit.

