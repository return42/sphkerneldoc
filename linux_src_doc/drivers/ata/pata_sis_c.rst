.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_sis.c

.. _`sis_old_port_base`:

sis_old_port_base
=================

.. c:function:: int sis_old_port_base(struct ata_device *adev)

    return PCI configuration base for dev

    :param struct ata_device \*adev:
        device

.. _`sis_old_port_base.description`:

Description
-----------

Returns the base of the PCI configuration registers for this port
number.

.. _`sis_port_base`:

sis_port_base
=============

.. c:function:: int sis_port_base(struct ata_device *adev)

    return PCI configuration base for dev

    :param struct ata_device \*adev:
        device

.. _`sis_port_base.description`:

Description
-----------

Returns the base of the PCI configuration registers for this port
number.

.. _`sis_133_cable_detect`:

sis_133_cable_detect
====================

.. c:function:: int sis_133_cable_detect(struct ata_port *ap)

    check for 40/80 pin

    :param struct ata_port \*ap:
        Port

.. _`sis_133_cable_detect.description`:

Description
-----------

Perform cable detection for the later UDMA133 capable
SiS chipset.

.. _`sis_66_cable_detect`:

sis_66_cable_detect
===================

.. c:function:: int sis_66_cable_detect(struct ata_port *ap)

    check for 40/80 pin

    :param struct ata_port \*ap:
        Port

.. _`sis_66_cable_detect.description`:

Description
-----------

Perform cable detection on the UDMA66, UDMA100 and early UDMA133
SiS IDE controllers.

.. _`sis_pre_reset`:

sis_pre_reset
=============

.. c:function:: int sis_pre_reset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param struct ata_link \*link:
        ATA link

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`sis_pre_reset.description`:

Description
-----------

Set up cable type and use generic probe init

.. _`sis_set_fifo`:

sis_set_fifo
============

.. c:function:: void sis_set_fifo(struct ata_port *ap, struct ata_device *adev)

    Set RWP fifo bits for this device

    :param struct ata_port \*ap:
        Port

    :param struct ata_device \*adev:
        Device

.. _`sis_set_fifo.description`:

Description
-----------

SIS chipsets implement prefetch/postwrite bits for each device
on both channels. This functionality is not ATAPI compatible and
must be configured according to the class of device present

.. _`sis_old_set_piomode`:

sis_old_set_piomode
===================

.. c:function:: void sis_old_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device we are configuring for.

.. _`sis_old_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space. This
function handles PIO set up for all chips that are pre ATA100 and
also early ATA100 devices.

.. _`sis_old_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sis_100_set_piomode`:

sis_100_set_piomode
===================

.. c:function:: void sis_100_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device we are configuring for.

.. _`sis_100_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space. This
function handles PIO set up for ATA100 devices and early ATA133.

.. _`sis_100_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sis_133_set_piomode`:

sis_133_set_piomode
===================

.. c:function:: void sis_133_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device we are configuring for.

.. _`sis_133_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space. This
function handles PIO set up for the later ATA133 devices.

.. _`sis_133_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sis_old_set_dmamode`:

sis_old_set_dmamode
===================

.. c:function:: void sis_old_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device to program

.. _`sis_old_set_dmamode.description`:

Description
-----------

Set UDMA/MWDMA mode for device, in host controller PCI config space.
Handles pre UDMA and UDMA33 devices. Supports MWDMA as well unlike
the old ide/pci driver.

.. _`sis_old_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sis_66_set_dmamode`:

sis_66_set_dmamode
==================

.. c:function:: void sis_66_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device to program

.. _`sis_66_set_dmamode.description`:

Description
-----------

Set UDMA/MWDMA mode for device, in host controller PCI config space.
Handles UDMA66 and early UDMA100 devices. Supports MWDMA as well unlike
the old ide/pci driver.

.. _`sis_66_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sis_100_set_dmamode`:

sis_100_set_dmamode
===================

.. c:function:: void sis_100_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device to program

.. _`sis_100_set_dmamode.description`:

Description
-----------

Set UDMA/MWDMA mode for device, in host controller PCI config space.
Handles UDMA66 and early UDMA100 devices.

.. _`sis_100_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sis_133_early_set_dmamode`:

sis_133_early_set_dmamode
=========================

.. c:function:: void sis_133_early_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device to program

.. _`sis_133_early_set_dmamode.description`:

Description
-----------

Set UDMA/MWDMA mode for device, in host controller PCI config space.
Handles early SiS 961 bridges.

.. _`sis_133_early_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sis_133_set_dmamode`:

sis_133_set_dmamode
===================

.. c:function:: void sis_133_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device to program

.. _`sis_133_set_dmamode.description`:

Description
-----------

Set UDMA/MWDMA mode for device, in host controller PCI config space.

.. _`sis_133_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sis_133_mode_filter`:

sis_133_mode_filter
===================

.. c:function:: unsigned long sis_133_mode_filter(struct ata_device *adev, unsigned long mask)

    mode selection filter

    :param struct ata_device \*adev:
        ATA device

    :param unsigned long mask:
        *undescribed*

.. _`sis_133_mode_filter.description`:

Description
-----------

Block UDMA6 on devices that do not support it.

.. _`sis_init_one`:

sis_init_one
============

.. c:function:: int sis_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register SiS ATA PCI device with kernel services

    :param struct pci_dev \*pdev:
        PCI device to register

    :param const struct pci_device_id \*ent:
        Entry in sis_pci_tbl matching with \ ``pdev``\ 

.. _`sis_init_one.description`:

Description
-----------

Called from kernel PCI layer. We probe for combined mode (sigh),
and then hand over control to libata, for it to do the rest.

.. _`sis_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`sis_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

