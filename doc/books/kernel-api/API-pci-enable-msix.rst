.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-enable-msix:

===============
pci_enable_msix
===============

*man pci_enable_msix(9)*

*4.6.0-rc5*

configure device's MSI-X capability structure


Synopsis
========

.. c:function:: int pci_enable_msix( struct pci_dev * dev, struct msix_entry * entries, int nvec )

Arguments
=========

``dev``
    pointer to the pci_dev data structure of MSI-X device function

``entries``
    pointer to an array of MSI-X entries

``nvec``
    number of MSI-X irqs requested for allocation by device driver


Description
===========

Setup the MSI-X capability structure of device function with the number
of requested irqs upon its software driver call to request for MSI-X
mode enabled on its hardware device function. A return of zero indicates
the successful configuration of MSI-X capability structure with new
allocated MSI-X irqs. A return of < 0 indicates a failure. Or a return
of > 0 indicates that driver request is exceeding the number of irqs or
MSI-X vectors available. Driver should use the returned value to re-send
its request.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
