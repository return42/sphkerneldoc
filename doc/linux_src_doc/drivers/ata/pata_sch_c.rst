.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_sch.c

.. _`sch_set_piomode`:

sch_set_piomode
===============

.. c:function:: void sch_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        ATA device

.. _`sch_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space.

.. _`sch_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sch_set_dmamode`:

sch_set_dmamode
===============

.. c:function:: void sch_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        ATA device

.. _`sch_set_dmamode.description`:

Description
-----------

Set MW/UDMA mode for device, in host controller PCI config space.

.. _`sch_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`sch_init_one`:

sch_init_one
============

.. c:function:: int sch_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register SCH ATA PCI device with kernel services

    :param struct pci_dev \*pdev:
        PCI device to register

    :param const struct pci_device_id \*ent:
        Entry in sch_pci_tbl matching with \ ``pdev``\ 

.. _`sch_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`sch_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

