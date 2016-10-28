.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_ali.c

.. _`ali_c2_cable_detect`:

ali_c2_cable_detect
===================

.. c:function:: int ali_c2_cable_detect(struct ata_port *ap)

    cable detection

    :param struct ata_port \*ap:
        ATA port

.. _`ali_c2_cable_detect.description`:

Description
-----------

Perform cable detection for C2 and later revisions

.. _`ali_20_filter`:

ali_20_filter
=============

.. c:function:: unsigned long ali_20_filter(struct ata_device *adev, unsigned long mask)

    filter for earlier ALI DMA

    :param struct ata_device \*adev:
        attached device

    :param unsigned long mask:
        *undescribed*

.. _`ali_20_filter.description`:

Description
-----------

Ensure that we do not do DMA on CD devices. We may be able to
fix that later on. Also ensure we do not do UDMA on WDC drives

.. _`ali_fifo_control`:

ali_fifo_control
================

.. c:function:: void ali_fifo_control(struct ata_port *ap, struct ata_device *adev, int on)

    FIFO manager

    :param struct ata_port \*ap:
        ALi channel to control

    :param struct ata_device \*adev:
        device for FIFO control

    :param int on:
        0 for off 1 for on

.. _`ali_fifo_control.description`:

Description
-----------

Enable or disable the FIFO on a given device. Because of the way the
ALi FIFO works it provides a boost on ATA disk but can be confused by
ATAPI and we must therefore manage it.

.. _`ali_program_modes`:

ali_program_modes
=================

.. c:function:: void ali_program_modes(struct ata_port *ap, struct ata_device *adev, struct ata_timing *t, u8 ultra)

    load mode registers

    :param struct ata_port \*ap:
        ALi channel to load

    :param struct ata_device \*adev:
        Device the timing is for

    :param struct ata_timing \*t:
        timing data

    :param u8 ultra:
        UDMA timing or zero for off

.. _`ali_program_modes.description`:

Description
-----------

Loads the timing registers for cmd/data and disable UDMA if
ultra is zero. If ultra is set then load and enable the UDMA
timing but do not touch the command/data timing.

.. _`ali_set_piomode`:

ali_set_piomode
===============

.. c:function:: void ali_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`ali_set_piomode.description`:

Description
-----------

Program the ALi registers for PIO mode.

.. _`ali_set_dmamode`:

ali_set_dmamode
===============

.. c:function:: void ali_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param struct ata_port \*ap:
        ATA interface

    :param struct ata_device \*adev:
        ATA device

.. _`ali_set_dmamode.description`:

Description
-----------

Program the ALi registers for DMA mode.

.. _`ali_warn_atapi_dma`:

ali_warn_atapi_dma
==================

.. c:function:: void ali_warn_atapi_dma(struct ata_device *adev)

    Warn about ATAPI DMA disablement

    :param struct ata_device \*adev:
        Device

.. _`ali_warn_atapi_dma.description`:

Description
-----------

Whine about ATAPI DMA disablement if \ ``adev``\  is an ATAPI device.
Can be used as ->dev_config.

.. _`ali_lock_sectors`:

ali_lock_sectors
================

.. c:function:: void ali_lock_sectors(struct ata_device *adev)

    Keep older devices to 255 sector mode

    :param struct ata_device \*adev:
        Device

.. _`ali_lock_sectors.description`:

Description
-----------

Called during the bus probe for each device that is found. We use
this call to lock the sector count of the device to 255 or less on
older ALi controllers. If we didn't do this then large I/O's would
require LBA48 commands which the older ALi requires are issued by
slower PIO methods

.. _`ali_check_atapi_dma`:

ali_check_atapi_dma
===================

.. c:function:: int ali_check_atapi_dma(struct ata_queued_cmd *qc)

    DMA check for most ALi controllers

    :param struct ata_queued_cmd \*qc:
        *undescribed*

.. _`ali_check_atapi_dma.description`:

Description
-----------

Called to decide whether commands should be sent by DMA or PIO

.. _`ali_init_chipset`:

ali_init_chipset
================

.. c:function:: void ali_init_chipset(struct pci_dev *pdev)

    chip setup function

    :param struct pci_dev \*pdev:
        PCI device of ATA controller

.. _`ali_init_chipset.description`:

Description
-----------

Perform the setup on the device that must be done both at boot
and at resume time.

.. _`ali_init_one`:

ali_init_one
============

.. c:function:: int ali_init_one(struct pci_dev *pdev, const struct pci_device_id *id)

    discovery callback

    :param struct pci_dev \*pdev:
        PCI device ID

    :param const struct pci_device_id \*id:
        PCI table info

.. _`ali_init_one.description`:

Description
-----------

An ALi IDE interface has been discovered. Figure out what revision
and perform configuration work before handing it to the ATA layer

.. This file was automatic generated / don't edit.

