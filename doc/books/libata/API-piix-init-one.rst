.. -*- coding: utf-8; mode: rst -*-

.. _API-piix-init-one:

=============
piix_init_one
=============

*man piix_init_one(9)*

*4.6.0-rc5*

Register PIIX ATA PCI device with kernel services


Synopsis
========

.. c:function:: int piix_init_one( struct pci_dev * pdev, const struct pci_device_id * ent )

Arguments
=========

``pdev``
    PCI device to register

``ent``
    Entry in piix_pci_tbl matching with ``pdev``


Description
===========

Called from kernel PCI layer. We probe for combined mode (sigh), and
then hand over control to libata, for it to do the rest.


LOCKING
=======

Inherited from PCI layer (may sleep).


RETURNS
=======

Zero on success, or -ERRNO value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
