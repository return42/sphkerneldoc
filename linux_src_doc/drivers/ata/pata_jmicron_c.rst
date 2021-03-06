.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_jmicron.c

.. _`jmicron_pre_reset`:

jmicron_pre_reset
=================

.. c:function:: int jmicron_pre_reset(struct ata_link *link, unsigned long deadline)

    check for 40/80 pin

    :param link:
        ATA link
    :type link: struct ata_link \*

    :param deadline:
        deadline jiffies for the operation
    :type deadline: unsigned long

.. _`jmicron_pre_reset.description`:

Description
-----------

Perform the PATA port setup we need.

On the Jmicron 361/363 there is a single PATA port that can be mapped
either as primary or secondary (or neither). We don't do any policy
and setup here. We assume that has been done by init_one and the
BIOS.

.. _`jmicron_init_one`:

jmicron_init_one
================

.. c:function:: int jmicron_init_one(struct pci_dev *pdev, const struct pci_device_id *id)

    Register Jmicron ATA PCI device with kernel services

    :param pdev:
        PCI device to register
    :type pdev: struct pci_dev \*

    :param id:
        *undescribed*
    :type id: const struct pci_device_id \*

.. _`jmicron_init_one.description`:

Description
-----------

Called from kernel PCI layer.

.. _`jmicron_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`jmicron_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

