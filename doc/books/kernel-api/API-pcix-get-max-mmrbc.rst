
.. _API-pcix-get-max-mmrbc:

==================
pcix_get_max_mmrbc
==================

*man pcix_get_max_mmrbc(9)*

*4.6.0-rc1*

get PCI-X maximum designed memory read byte count


Synopsis
========

.. c:function:: int pcix_get_max_mmrbc( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to query


Returns mmrbc
=============

maximum designed memory read count in bytes or appropriate error value.
