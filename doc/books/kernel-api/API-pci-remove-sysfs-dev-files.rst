.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-remove-sysfs-dev-files:

==========================
pci_remove_sysfs_dev_files
==========================

*man pci_remove_sysfs_dev_files(9)*

*4.6.0-rc5*

cleanup PCI specific sysfs files


Synopsis
========

.. c:function:: void pci_remove_sysfs_dev_files( struct pci_dev * pdev )

Arguments
=========

``pdev``
    device whose entries we should free


Description
===========

Cleanup when ``pdev`` is removed from sysfs.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
