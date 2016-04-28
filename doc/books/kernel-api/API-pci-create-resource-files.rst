.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-create-resource-files:

=========================
pci_create_resource_files
=========================

*man pci_create_resource_files(9)*

*4.6.0-rc5*

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

Walk the resources in ``pdev`` creating files for each resource
available.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
