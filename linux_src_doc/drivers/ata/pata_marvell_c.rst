.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_marvell.c

.. _`marvell_pata_active`:

marvell_pata_active
===================

.. c:function:: int marvell_pata_active(struct pci_dev *pdev)

    check if PATA is active

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

.. _`marvell_pata_active.description`:

Description
-----------

Returns 1 if the PATA port may be active. We know how to check this
for the 6145 but not the other devices

.. _`marvell_pre_reset`:

marvell_pre_reset
=================

.. c:function:: int marvell_pre_reset(struct ata_link *link, unsigned long deadline)

    probe begin

    :param link:
        link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`marvell_pre_reset.description`:

Description
-----------

Perform the PATA port setup we need.

.. _`marvell_init_one`:

marvell_init_one
================

.. c:function:: int marvell_init_one(struct pci_dev *pdev, const struct pci_device_id *id)

    Register Marvell ATA PCI device with kernel services

    :param pdev:
        PCI device to register
    :type pdev: struct pci_dev \*

    :param id:
        *undescribed*
    :type id: const struct pci_device_id \*

.. _`marvell_init_one.description`:

Description
-----------

Called from kernel PCI layer.

.. _`marvell_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`marvell_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

