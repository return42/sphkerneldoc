.. -*- coding: utf-8; mode: rst -*-

.. _API-pcix-get-max-mmrbc:

==================
pcix_get_max_mmrbc
==================

*man pcix_get_max_mmrbc(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
