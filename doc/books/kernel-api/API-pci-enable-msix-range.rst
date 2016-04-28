.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-enable-msix-range:

=====================
pci_enable_msix_range
=====================

*man pci_enable_msix_range(9)*

*4.6.0-rc5*

configure device's MSI-X capability structure


Synopsis
========

.. c:function:: int pci_enable_msix_range( struct pci_dev * dev, struct msix_entry * entries, int minvec, int maxvec )

Arguments
=========

``dev``
    pointer to the pci_dev data structure of MSI-X device function

``entries``
    pointer to an array of MSI-X entries

``minvec``
    minimum number of MSI-X irqs requested

``maxvec``
    maximum number of MSI-X irqs requested


Description
===========

Setup the MSI-X capability structure of device function with a maximum
possible number of interrupts in the range between ``minvec`` and
``maxvec`` upon its software driver call to request for MSI-X mode
enabled on its hardware device function. It returns a negative errno if
an error occurs. If it succeeds, it returns the actual number of
interrupts allocated and indicates the successful configuration of MSI-X
capability structure with new allocated MSI-X interrupts.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
