.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/aer/ecrc.c

.. _`enable_ecrc_checking`:

enable_ecrc_checking
====================

.. c:function:: int enable_ecrc_checking(struct pci_dev *dev)

    enable PCIe ECRC checking for a device

    :param struct pci_dev \*dev:
        the PCI device

.. _`enable_ecrc_checking.description`:

Description
-----------

Returns 0 on success, or negative on failure.

.. _`disable_ecrc_checking`:

disable_ecrc_checking
=====================

.. c:function:: int disable_ecrc_checking(struct pci_dev *dev)

    disables PCIe ECRC checking for a device

    :param struct pci_dev \*dev:
        the PCI device

.. _`disable_ecrc_checking.description`:

Description
-----------

Returns 0 on success, or negative on failure.

.. _`pcie_set_ecrc_checking`:

pcie_set_ecrc_checking
======================

.. c:function:: void pcie_set_ecrc_checking(struct pci_dev *dev)

    set/unset PCIe ECRC checking for a device based on global policy

    :param struct pci_dev \*dev:
        the PCI device

.. _`pcie_ecrc_get_policy`:

pcie_ecrc_get_policy
====================

.. c:function:: void pcie_ecrc_get_policy(char *str)

    parse kernel command-line ecrc option

    :param char \*str:
        *undescribed*

.. This file was automatic generated / don't edit.

