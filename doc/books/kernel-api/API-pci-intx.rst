.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-intx:

========
pci_intx
========

*man pci_intx(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
