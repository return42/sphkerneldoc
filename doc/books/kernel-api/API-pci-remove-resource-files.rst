
.. _API-pci-remove-resource-files:

=========================
pci_remove_resource_files
=========================

*man pci_remove_resource_files(9)*

*4.6.0-rc1*

cleanup resource files


Synopsis
========

.. c:function:: void pci_remove_resource_files( struct pci_dev * pdev )

Arguments
=========

``pdev``
    dev to cleanup


Description
===========

If we created resource files for ``pdev``, remove them from sysfs and free their resources.
