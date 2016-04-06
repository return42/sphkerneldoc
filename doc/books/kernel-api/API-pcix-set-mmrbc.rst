
.. _API-pcix-set-mmrbc:

==============
pcix_set_mmrbc
==============

*man pcix_set_mmrbc(9)*

*4.6.0-rc1*

set PCI-X maximum memory read byte count


Synopsis
========

.. c:function:: int pcix_set_mmrbc( struct pci_dev * dev, int mmrbc )

Arguments
=========

``dev``
    PCI device to query

``mmrbc``
    maximum memory read count in bytes valid values are 512, 1024, 2048, 4096


Description
===========

If possible sets maximum memory read byte count, some bridges have erratas that prevent this.
