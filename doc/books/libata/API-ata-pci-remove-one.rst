.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-pci-remove-one:

==================
ata_pci_remove_one
==================

*man ata_pci_remove_one(9)*

*4.6.0-rc5*

PCI layer callback for device removal


Synopsis
========

.. c:function:: void ata_pci_remove_one( struct pci_dev * pdev )

Arguments
=========

``pdev``
    PCI device that was removed


Description
===========

PCI layer indicates to libata via this hook that hot-unplug or module
unload event has occurred. Detach all ports. Resource release is handled
via devres.


LOCKING
=======

Inherited from PCI layer (may sleep).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
