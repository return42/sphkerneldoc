.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-remove-resource-files:

=========================
pci_remove_resource_files
=========================

*man pci_remove_resource_files(9)*

*4.6.0-rc5*

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

If we created resource files for ``pdev``, remove them from sysfs and
free their resources.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
