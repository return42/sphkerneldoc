.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_serverworks.c

.. _`oem_cable`:

oem_cable
=========

.. c:function:: int oem_cable(struct ata_port *ap)

    Dell/Sun serverworks cable detection

    :param ap:
        ATA port to do cable detect
    :type ap: struct ata_port \*

.. _`oem_cable.description`:

Description
-----------

Dell PowerEdge and Sun Cobalt 'Alpine' hide the 40/80 pin select
for their interfaces in the top two bits of the subsystem ID.

.. _`serverworks_cable_detect`:

serverworks_cable_detect
========================

.. c:function:: int serverworks_cable_detect(struct ata_port *ap)

    cable detection

    :param ap:
        ATA port
    :type ap: struct ata_port \*

.. _`serverworks_cable_detect.description`:

Description
-----------

Perform cable detection according to the device and subvendor
identifications

.. _`serverworks_is_csb`:

serverworks_is_csb
==================

.. c:function:: u8 serverworks_is_csb(struct pci_dev *pdev)

    Check for CSB or OSB

    :param pdev:
        PCI device to check
    :type pdev: struct pci_dev \*

.. _`serverworks_is_csb.description`:

Description
-----------

Returns true if the device being checked is known to be a CSB
series device.

.. _`serverworks_osb4_filter`:

serverworks_osb4_filter
=======================

.. c:function:: unsigned long serverworks_osb4_filter(struct ata_device *adev, unsigned long mask)

    mode selection filter

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param mask:
        Mask of proposed modes
    :type mask: unsigned long

.. _`serverworks_osb4_filter.description`:

Description
-----------

Filter the offered modes for the device to apply controller
specific rules. OSB4 requires no UDMA for disks due to a FIFO
bug we hit.

.. _`serverworks_csb_filter`:

serverworks_csb_filter
======================

.. c:function:: unsigned long serverworks_csb_filter(struct ata_device *adev, unsigned long mask)

    mode selection filter

    :param adev:
        ATA device
    :type adev: struct ata_device \*

    :param mask:
        Mask of proposed modes
    :type mask: unsigned long

.. _`serverworks_csb_filter.description`:

Description
-----------

Check the blacklist and disable UDMA5 if matched

.. _`serverworks_set_piomode`:

serverworks_set_piomode
=======================

.. c:function:: void serverworks_set_piomode(struct ata_port *ap, struct ata_device *adev)

    set initial PIO mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`serverworks_set_piomode.description`:

Description
-----------

Program the OSB4/CSB5 timing registers for PIO. The PIO register
load is done as a simple lookup.

.. _`serverworks_set_dmamode`:

serverworks_set_dmamode
=======================

.. c:function:: void serverworks_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    set initial DMA mode data

    :param ap:
        ATA interface
    :type ap: struct ata_port \*

    :param adev:
        ATA device
    :type adev: struct ata_device \*

.. _`serverworks_set_dmamode.description`:

Description
-----------

Program the MWDMA/UDMA modes for the serverworks OSB4/CSB5
chipset. The MWDMA mode values are pulled from a lookup table
while the chipset uses mode number for UDMA.

.. This file was automatic generated / don't edit.

