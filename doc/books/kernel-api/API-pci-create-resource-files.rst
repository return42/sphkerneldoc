
.. _API-pci-create-resource-files:

=========================
pci_create_resource_files
=========================

*man pci_create_resource_files(9)*

*4.6.0-rc1*

create resource files in sysfs for ``dev``


Synopsis
========

.. c:function:: int pci_create_resource_files( struct pci_dev * pdev )

Arguments
=========

``pdev``
    dev in question


Description
===========

Walk the resources in ``pdev`` creating files for each resource available.
