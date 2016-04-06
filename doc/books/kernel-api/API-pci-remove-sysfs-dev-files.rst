
.. _API-pci-remove-sysfs-dev-files:

==========================
pci_remove_sysfs_dev_files
==========================

*man pci_remove_sysfs_dev_files(9)*

*4.6.0-rc1*

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
