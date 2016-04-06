
.. _API-pcix-get-mmrbc:

==============
pcix_get_mmrbc
==============

*man pcix_get_mmrbc(9)*

*4.6.0-rc1*

get PCI-X maximum memory read byte count


Synopsis
========

.. c:function:: int pcix_get_mmrbc( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to query


Returns mmrbc
=============

maximum memory read count in bytes or appropriate error value.
