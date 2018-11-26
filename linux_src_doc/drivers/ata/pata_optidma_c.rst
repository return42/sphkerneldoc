.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_optidma.c

.. _`optidma_pre_reset`:

optidma_pre_reset
=================

.. c:function:: int optidma_pre_reset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param link:
        ATA link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`optidma_pre_reset.description`:

Description
-----------

Set up cable type and use generic probe init

.. _`optidma_unlock`:

optidma_unlock
==============

.. c:function:: void optidma_unlock(struct ata_port *ap)

    unlock control registers

    :param ap:
        ATA port
    :type ap: struct ata_port \*

.. _`optidma_unlock.description`:

Description
-----------

Unlock the control register block for this adapter. Registers must not
be unlocked in a situation where libata might look at them.

.. _`optidma_lock`:

optidma_lock
============

.. c:function:: void optidma_lock(struct ata_port *ap)

    issue temporary relock

    :param ap:
        ATA port
    :type ap: struct ata_port \*

.. _`optidma_lock.description`:

Description
-----------

Re-lock the configuration register settings.

.. _`optidma_mode_setup`:

optidma_mode_setup
==================

.. c:function:: void optidma_mode_setup(struct ata_port *ap, struct ata_device *adev, u8 mode)

    set mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param mode:
        Mode to set
    :type mode: u8

.. _`optidma_mode_setup.description`:

Description
-----------

Called to do the DMA or PIO mode setup. Timing numbers are all
pre computed to keep the code clean. There are two tables depending
on the hardware clock speed.

.. _`optidma_mode_setup.warning`:

WARNING
-------

While we do this the IDE registers vanish. If we take an
IRQ here we depend on the host set locking to avoid catastrophe.

.. _`optiplus_mode_setup`:

optiplus_mode_setup
===================

.. c:function:: void optiplus_mode_setup(struct ata_port *ap, struct ata_device *adev, u8 mode)

    DMA setup for Firestar Plus

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        device
    :type adev: struct ata_device \*

    :param mode:
        desired mode
    :type mode: u8

.. _`optiplus_mode_setup.description`:

Description
-----------

The Firestar plus has additional UDMA functionality for UDMA0-2 and
requires we do some additional work. Because the base work we must do
is mostly shared we wrap the Firestar setup functionality in this
one

.. _`optidma_set_pio_mode`:

optidma_set_pio_mode
====================

.. c:function:: void optidma_set_pio_mode(struct ata_port *ap, struct ata_device *adev)

    PIO setup callback

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        Device
    :type adev: struct ata_device \*

.. _`optidma_set_pio_mode.description`:

Description
-----------

The libata core provides separate functions for handling PIO and
DMA programming. The architecture of the Firestar makes it easier
for us to have a common function so we provide wrappers

.. _`optidma_set_dma_mode`:

optidma_set_dma_mode
====================

.. c:function:: void optidma_set_dma_mode(struct ata_port *ap, struct ata_device *adev)

    DMA setup callback

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        Device
    :type adev: struct ata_device \*

.. _`optidma_set_dma_mode.description`:

Description
-----------

The libata core provides separate functions for handling PIO and
DMA programming. The architecture of the Firestar makes it easier
for us to have a common function so we provide wrappers

.. _`optiplus_set_pio_mode`:

optiplus_set_pio_mode
=====================

.. c:function:: void optiplus_set_pio_mode(struct ata_port *ap, struct ata_device *adev)

    PIO setup callback

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        Device
    :type adev: struct ata_device \*

.. _`optiplus_set_pio_mode.description`:

Description
-----------

The libata core provides separate functions for handling PIO and
DMA programming. The architecture of the Firestar makes it easier
for us to have a common function so we provide wrappers

.. _`optiplus_set_dma_mode`:

optiplus_set_dma_mode
=====================

.. c:function:: void optiplus_set_dma_mode(struct ata_port *ap, struct ata_device *adev)

    DMA setup callback

    :param ap:
        ATA port
    :type ap: struct ata_port \*

    :param adev:
        Device
    :type adev: struct ata_device \*

.. _`optiplus_set_dma_mode.description`:

Description
-----------

The libata core provides separate functions for handling PIO and
DMA programming. The architecture of the Firestar makes it easier
for us to have a common function so we provide wrappers

.. _`optidma_make_bits43`:

optidma_make_bits43
===================

.. c:function:: u8 optidma_make_bits43(struct ata_device *adev)

    PCI setup helper

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`optidma_make_bits43.description`:

Description
-----------

Turn the ATA device setup into PCI configuration bits
for register 0x43 and return the two bits needed.

.. _`optidma_set_mode`:

optidma_set_mode
================

.. c:function:: int optidma_set_mode(struct ata_link *link, struct ata_device **r_failed)

    mode setup

    :param link:
        link to set up
    :type link: struct ata_link \*

    :param r_failed:
        *undescribed*
    :type r_failed: struct ata_device \*\*

.. _`optidma_set_mode.description`:

Description
-----------

Use the standard setup to tune the chipset and then finalise the
configuration by writing the nibble of extra bits of data into
the chip.

.. _`optiplus_with_udma`:

optiplus_with_udma
==================

.. c:function:: int optiplus_with_udma(struct pci_dev *pdev)

    Look for UDMA capable setup \ ``pdev``\ ; ATA controller

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. This file was automatic generated / don't edit.

