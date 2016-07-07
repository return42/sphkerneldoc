.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_efar.c

.. _`efar_pre_reset`:

efar_pre_reset
==============

.. c:function:: int efar_pre_reset(struct ata_link *link, unsigned long deadline)

    Enable bits

    :param struct ata_link \*link:
        ATA link

    :param unsigned long deadline:
        deadline jiffies for the operation

.. _`efar_pre_reset.description`:

Description
-----------

Perform cable detection for the EFAR ATA interface. This is
different to the PIIX arrangement

.. _`efar_cable_detect`:

efar_cable_detect
=================

.. c:function:: int efar_cable_detect(struct ata_port *ap)

    check for 40/80 pin

    :param struct ata_port \*ap:
        Port

.. _`efar_cable_detect.description`:

Description
-----------

Perform cable detection for the EFAR ATA interface. This is
different to the PIIX arrangement

.. _`efar_set_piomode`:

efar_set_piomode
================

.. c:function:: void efar_set_piomode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA PIO timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device to program

.. _`efar_set_piomode.description`:

Description
-----------

Set PIO mode for device, in host controller PCI config space.

.. _`efar_set_piomode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`efar_set_dmamode`:

efar_set_dmamode
================

.. c:function:: void efar_set_dmamode(struct ata_port *ap, struct ata_device *adev)

    Initialize host controller PATA DMA timings

    :param struct ata_port \*ap:
        Port whose timings we are configuring

    :param struct ata_device \*adev:
        Device to program

.. _`efar_set_dmamode.description`:

Description
-----------

Set UDMA/MWDMA mode for device, in host controller PCI config space.

.. _`efar_set_dmamode.locking`:

LOCKING
-------

None (inherited from caller).

.. _`efar_init_one`:

efar_init_one
=============

.. c:function:: int efar_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register EFAR ATA PCI device with kernel services

    :param struct pci_dev \*pdev:
        PCI device to register

    :param const struct pci_device_id \*ent:
        Entry in efar_pci_tbl matching with \ ``pdev``\ 

.. _`efar_init_one.description`:

Description
-----------

Called from kernel PCI layer.

.. _`efar_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`efar_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

