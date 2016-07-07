.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/stmicro/stmmac/stmmac_pci.c

.. _`stmmac_pci_probe`:

stmmac_pci_probe
================

.. c:function:: int stmmac_pci_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    :param struct pci_dev \*pdev:
        pci device pointer

    :param const struct pci_device_id \*id:
        pointer to table of device id/id's.

.. _`stmmac_pci_probe.description`:

Description
-----------

This probing function gets called for all PCI devices which
match the ID table and are not "owned" by other driver yet. This function
gets passed a "struct pci_dev \*" for each device whose entry in the ID table
matches the device. The probe functions returns zero when the driver choose
to take "ownership" of the device or an error code(-ve no) otherwise.

.. _`stmmac_pci_remove`:

stmmac_pci_remove
=================

.. c:function:: void stmmac_pci_remove(struct pci_dev *pdev)

    :param struct pci_dev \*pdev:
        platform device pointer

.. _`stmmac_pci_remove.description`:

Description
-----------

this function calls the main to free the net resources
and releases the PCI resources.

.. This file was automatic generated / don't edit.

