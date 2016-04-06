
.. _API-pci-intx:

========
pci_intx
========

*man pci_intx(9)*

*4.6.0-rc1*

enables/disables PCI INTx for device dev


Synopsis
========

.. c:function:: void pci_intx( struct pci_dev * pdev, int enable )

Arguments
=========

``pdev``
    the PCI device to operate on

``enable``
    boolean: whether to enable or disable PCI INTx


Description
===========

Enables/disables PCI INTx for device dev
