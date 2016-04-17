.. -*- coding: utf-8; mode: rst -*-

======
aspm.c
======


.. _`pci_disable_link_state`:

pci_disable_link_state
======================

.. c:function:: void pci_disable_link_state (struct pci_dev *pdev, int state)

    Disable device's link state, so the link will never enter specific states. Note that if the BIOS didn't grant ASPM control to the OS, this does nothing because we can't touch the LNKCTL register.

    :param struct pci_dev \*pdev:
        PCI device

    :param int state:
        ASPM link state to disable

