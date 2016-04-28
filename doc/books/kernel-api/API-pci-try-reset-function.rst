.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-try-reset-function:

======================
pci_try_reset_function
======================

*man pci_try_reset_function(9)*

*4.6.0-rc5*

quiesce and reset a PCI device function


Synopsis
========

.. c:function:: int pci_try_reset_function( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to reset


Description
===========

Same as above, except return -EAGAIN if unable to lock device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
