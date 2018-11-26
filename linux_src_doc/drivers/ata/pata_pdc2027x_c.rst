.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_pdc2027x.c

.. _`port_mmio`:

port_mmio
=========

.. c:function:: void __iomem *port_mmio(struct ata_port *ap, unsigned int offset)

    Get the MMIO address of PDC2027x extended registers

    :param ap:
        Port
    :type ap: struct ata_port \*

    :param offset:
        offset from mmio base
    :type offset: unsigned int

.. _`dev_mmio`:

dev_mmio
========

.. c:function:: void __iomem *dev_mmio(struct ata_port *ap, struct ata_device *adev, unsigned int offset)

    Get the MMIO address of PDC2027x extended registers

    :param ap:
        Port
    :type ap: struct ata_port \*

    :param adev:
        device
    :type adev: struct ata_device \*

    :param offset:
        offset from mmio base
    :type offset: unsigned int

.. _`pdc2027x_cable_detect`:

pdc2027x_cable_detect
=====================

.. c:function:: int pdc2027x_cable_detect(struct ata_port *ap)

    Probe host controller cable detect info

    :param ap:
        Port for which cable detect info is desired
    :type ap: struct ata_port \*

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

    :param ap:
        Port to check
    :type ap: struct ata_port \*

.. _`pdc2027x_prereset`:

pdc2027x_prereset
=================

.. c:function:: int pdc2027x_prereset(struct ata_link *link, unsigned long deadline)

    prereset for PATA host controller

    :param link:
        Target link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

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

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param mask:
        list of modes proposed
    :type mask: unsigned long

.. _`pdc2027x_mode_filter.description`:

Description
-----------

Block UDMA on devices that cause trouble with this controller.

.. _`pdc2027x_set_piomode`:

pdc2027x_set_piomode
====================

.. c:function:: void pdc2027x_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param ap:
        Port to configure
    :type ap: struct ata_port \*

    :param adev:
        um
    :type adev: struct ata_device \*

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

    :param ap:
        Port to configure
    :type ap: struct ata_port \*

    :param adev:
        um
    :type adev: struct ata_device \*

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

    :param link:
        link to configure
    :type link: struct ata_link \*

    :param r_failed:
        Returned device for failure
    :type r_failed: struct ata_device \*\*

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

    :param qc:
        Metadata associated with taskfile to check
    :type qc: struct ata_queued_cmd \*

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

    :param host:
        target ATA host
    :type host: struct ata_host \*

.. _`pdc_adjust_pll`:

pdc_adjust_pll
==============

.. c:function:: void pdc_adjust_pll(struct ata_host *host, long pll_clock, unsigned int board_idx)

    Adjust the PLL input clock in Hz.

    :param host:
        target ATA host
    :type host: struct ata_host \*

    :param pll_clock:
        The input of PLL in HZ
    :type pll_clock: long

    :param board_idx:
        *undescribed*
    :type board_idx: unsigned int

.. _`pdc_detect_pll_input_clock`:

pdc_detect_pll_input_clock
==========================

.. c:function:: long pdc_detect_pll_input_clock(struct ata_host *host)

    Detect the PLL input clock in Hz.

    :param host:
        target ATA host
        Ex. 16949000 on 33MHz PCI bus for pdc20275.
        Half of the PCI clock.
    :type host: struct ata_host \*

.. _`pdc_hardware_init`:

pdc_hardware_init
=================

.. c:function:: void pdc_hardware_init(struct ata_host *host, unsigned int board_idx)

    Initialize the hardware.

    :param host:
        target ATA host
    :type host: struct ata_host \*

    :param board_idx:
        board identifier
    :type board_idx: unsigned int

.. _`pdc_ata_setup_port`:

pdc_ata_setup_port
==================

.. c:function:: void pdc_ata_setup_port(struct ata_ioports *port, void __iomem *base)

    setup the mmio address

    :param port:
        ata ioports to setup
    :type port: struct ata_ioports \*

    :param base:
        base address
    :type base: void __iomem \*

.. _`pdc2027x_init_one`:

pdc2027x_init_one
=================

.. c:function:: int pdc2027x_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    PCI probe function Called when an instance of PCI adapter is inserted. This function checks whether the hardware is supported, initialize hardware and register an instance of ata_host to libata.  (implements struct pci_driver.probe() )

    :param pdev:
        instance of pci_dev found
    :type pdev: struct pci_dev \*

    :param ent:
        matching entry in the id_tbl[]
    :type ent: const struct pci_device_id \*

.. This file was automatic generated / don't edit.

