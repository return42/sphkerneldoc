.. -*- coding: utf-8; mode: rst -*-

.. _API-pcix-set-mmrbc:

==============
pcix_set_mmrbc
==============

*man pcix_set_mmrbc(9)*

*4.6.0-rc5*

set PCI-X maximum memory read byte count


Synopsis
========

.. c:function:: int pcix_set_mmrbc( struct pci_dev * dev, int mmrbc )

Arguments
=========

``dev``
    PCI device to query

``mmrbc``
    maximum memory read count in bytes valid values are 512, 1024, 2048,
    4096


Description
===========

If possible sets maximum memory read byte count, some bridges have
erratas that prevent this.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
