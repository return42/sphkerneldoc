.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_rz1000.c

.. _`rz1000_set_mode`:

rz1000_set_mode
===============

.. c:function:: int rz1000_set_mode(struct ata_link *link, struct ata_device **unused)

    mode setting function

    :param link:
        ATA link
    :type link: struct ata_link \*

    :param unused:
        returned device on set_mode failure
    :type unused: struct ata_device \*\*

.. _`rz1000_set_mode.description`:

Description
-----------

Use a non standard set_mode function. We don't want to be tuned. We
would prefer to be BIOS generic but for the fact our hardware is
whacked out.

.. _`rz1000_init_one`:

rz1000_init_one
===============

.. c:function:: int rz1000_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register RZ1000 ATA PCI device with kernel services

    :param pdev:
        PCI device to register
    :type pdev: struct pci_dev \*

    :param ent:
        Entry in rz1000_pci_tbl matching with \ ``pdev``\ 
    :type ent: const struct pci_device_id \*

.. _`rz1000_init_one.description`:

Description
-----------

Configure an RZ1000 interface. This doesn't require much special
handling except that we \*MUST\* kill the chipset readahead or the
user may experience data corruption.

.. This file was automatic generated / don't edit.

