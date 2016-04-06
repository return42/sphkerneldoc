
.. _API-pci-find-ext-capability:

=======================
pci_find_ext_capability
=======================

*man pci_find_ext_capability(9)*

*4.6.0-rc1*

Find an extended capability


Synopsis
========

.. c:function:: int pci_find_ext_capability( struct pci_dev * dev, int cap )

Arguments
=========

``dev``
    PCI device to query

``cap``
    capability code


Description
===========

Returns the address of the requested extended capability structure within the device's PCI configuration space or 0 if the device does not support it. Possible values for ``cap``:

``PCI_EXT_CAP_ID_ERR`` Advanced Error Reporting ``PCI_EXT_CAP_ID_VC`` Virtual Channel ``PCI_EXT_CAP_ID_DSN`` Device Serial Number ``PCI_EXT_CAP_ID_PWR`` Power Budgeting
