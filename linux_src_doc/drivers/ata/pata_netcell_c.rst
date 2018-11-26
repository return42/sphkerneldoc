.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_netcell.c

.. _`netcell_init_one`:

netcell_init_one
================

.. c:function:: int netcell_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    Register Netcell ATA PCI device with kernel services

    :param pdev:
        PCI device to register
    :type pdev: struct pci_dev \*

    :param ent:
        Entry in netcell_pci_tbl matching with \ ``pdev``\ 
    :type ent: const struct pci_device_id \*

.. _`netcell_init_one.description`:

Description
-----------

Called from kernel PCI layer.

.. _`netcell_init_one.locking`:

LOCKING
-------

Inherited from PCI layer (may sleep).

.. _`netcell_init_one.return`:

Return
------

Zero on success, or -ERRNO value.

.. This file was automatic generated / don't edit.

