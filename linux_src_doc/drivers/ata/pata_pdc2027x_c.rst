.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_pdc2027x.c

.. _`port_mmio`:

port_mmio
=========

.. c:function:: void __iomem *port_mmio(struct ata_port *ap, unsigned int offset)

    Get the MMIO address of PDC2027x extended registers

    :param struct ata_port \*ap:
        Port

    :param unsigned int offset:
        offset from mmio base

.. _`dev_mmio`:

dev_mmio
========

.. c:function:: void __iomem *dev_mmio(struct ata_port *ap, struct ata_device *adev, unsigned int offset)

    Get the MMIO address of PDC2027x extended registers

    :param struct ata_port \*ap:
        Port

    :param struct ata_device \*adev:
        device

    :param unsigned int offset:
        offset from mmio base

.. _`pdc2027x_cable_detect`:

pdc2027x_cable_detect
=====================

.. c:function:: int pdc2027x_cable_detect(struct ata_port *ap)

    Probe host controller cable detect info

    :param struct ata_port \*ap:
        Port for which cable detect info is desired

.. _`pdc2027x_cable_detect.description`:

Description
-----------

Read 80c cable indicator from Promise extended register.
This register is latched when the system is reset.

.. _`pdc2027x_cable_detect.locking`:

LOCKING
-------

None (inherited from caller).

.. _`pdc2027x_port_enabled`:

pdc2027x_port_enabled
=====================

.. c:function:: int pdc2027x_port_enabled(struct ata_port *ap)

    Check PDC ATA control register to see whether the port is enabled.

    :param struct ata_port \*ap:
        Port to check

.. _`pdc2027x_prereset`:

pdc2027x_prereset
=================

.. c:function:: int pdc2027x_prereset(struct ata_link *link, unsigned long deadline)

    prereset for PATA host controller

    :param struct ata_link \*link:
        Target link

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`pdc2027x_prereset.description`:

Description
-----------

Probeinit including cable detection.

.. _`pdc2027x_prereset.locking`:

LOCKING
-------

None (inherited from caller).

.. _`pdc2027x_mode_filter`:

pdc2027x_mode_filter
====================

.. c:function:: unsigned long pdc2027x_mode_filter(struct ata_device *adev, unsigned long mask)

    mode selection filter

    :param struct ata_device \*adev:
        ATA device

    :param unsigned long mask:
        list of modes proposed

.. _`pdc2027x_mode_filter.description`:

Description
-----------

Block UDMA on devices that cause trouble with this controller.

.. _`pdc2027x_set_piomode`:

pdc2027x_set_piomode
====================

.. c:function:: void pdc2027x_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port to configure

    :param struct ata_device \*adev:
        um

.. _`pdc2027x_set_piomode.description`:

Description
-----------

Set PIO mode for device.

.. _`pdc2027x_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`pdc2027x_set_dmamode`:

pdc2027x_set_dmamode
====================

.. c:function:: void pdc2027x_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA UDMA timings

    :param struct ata_port \*ap:
        Port to configure

    :param struct ata_device \*adev:
        um

.. _`pdc2027x_set_dmamode.description`:

Description
-----------

Set UDMA mode for device.

.. _`pdc2027x_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`pdc2027x_set_mode`:

pdc2027x_set_mode
=================

.. c:function:: int pdc2027x_set_mode(struct ata_link *link, struct ata_device **r_failed)

    Set the timing registers back to correct values.

    :param struct ata_link \*link:
        link to configure

    :param struct ata_device \*\*r_failed:
        Returned device for failure

.. _`pdc2027x_set_mode.description`:

Description
-----------

The pdc2027x hardware will look at "SET FEATURES" and change the timing registers
automatically. The values set by the hardware might be incorrect, under 133Mhz PLL.
This function overwrites the possibly incorrect values set by the hardware to be correct.

.. _`pdc2027x_check_atapi_dma`:

pdc2027x_check_atapi_dma
========================

.. c:function:: int pdc2027x_check_atapi_dma(struct ata_queued_cmd *qc)

    Check whether ATAPI DMA can be supported for this command

    :param struct ata_queued_cmd \*qc:
        Metadata associated with taskfile to check

.. _`pdc2027x_check_atapi_dma.locking`:

LOCKING
-------

None (inherited from caller).

.. _`pdc2027x_check_atapi_dma.return`:

Return
------

0 when ATAPI DMA can be used
1 otherwise

.. _`pdc_read_counter`:

pdc_read_counter
================

.. c:function:: long pdc_read_counter(struct ata_host *host)

    Read the ctr counter

    :param struct ata_host \*host:
        target ATA host

.. _`pdc_adjust_pll`:

pdc_adjust_pll
==============

.. c:function:: void pdc_adjust_pll(struct ata_host *host, long pll_clock, unsigned int board_idx)

    Adjust the PLL input clock in Hz.

    :param struct ata_host \*host:
        target ATA host

    :param long pll_clock:
        The input of PLL in HZ

    :param unsigned int board_idx:
        *undescribed*

.. _`pdc_detect_pll_input_clock`:

pdc_detect_pll_input_clock
==========================

.. c:function:: long pdc_detect_pll_input_clock(struct ata_host *host)

    Detect the PLL input clock in Hz.

    :param struct ata_host \*host:
        target ATA host
        Ex. 16949000 on 33MHz PCI bus for pdc20275.
        Half of the PCI clock.

.. _`pdc_hardware_init`:

pdc_hardware_init
=================

.. c:function:: void pdc_hardware_init(struct ata_host *host, unsigned int board_idx)

    Initialize the hardware.

    :param struct ata_host \*host:
        target ATA host

    :param unsigned int board_idx:
        board identifier

.. _`pdc_ata_setup_port`:

pdc_ata_setup_port
==================

.. c:function:: void pdc_ata_setup_port(struct ata_ioports *port, void __iomem *base)

    setup the mmio address

    :param struct ata_ioports \*port:
        ata ioports to setup

    :param void __iomem \*base:
        base address

.. _`pdc2027x_init_one`:

pdc2027x_init_one
=================

.. c:function:: int pdc2027x_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    PCI probe function Called when an instance of PCI adapter is inserted. This function checks whether the hardware is supported, initialize hardware and register an instance of ata_host to libata.  (implements struct pci_driver.probe() )

    :param struct pci_dev \*pdev:
        instance of pci_dev found

    :param const struct pci_device_id \*ent:
        matching entry in the id_tbl[]

.. This file was automatic generated / don't edit.

