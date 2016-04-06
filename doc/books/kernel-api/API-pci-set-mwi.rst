
.. _API-pci-set-mwi:

===========
pci_set_mwi
===========

*man pci_set_mwi(9)*

*4.6.0-rc1*

enables memory-write-invalidate PCI transaction


Synopsis
========

.. c:function:: int pci_set_mwi( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device for which MWI is enabled


Description
===========

Enables the Memory-Write-Invalidate transaction in ``PCI_COMMAND``.


RETURNS
=======

An appropriate -ERRNO error value on error, or zero for success.
