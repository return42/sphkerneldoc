.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-reset-function:

==================
pci_reset_function
==================

*man pci_reset_function(9)*

*4.6.0-rc5*

quiesce and reset a PCI device function


Synopsis
========

.. c:function:: int pci_reset_function( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to reset


Description
===========

Some devices allow an individual function to be reset without affecting
other functions in the same device. The PCI device must be responsive to
PCI config space in order to use this function.

This function does not just reset the PCI portion of a device, but
clears all the state associated with the device. This function differs
from __pci_reset_function in that it saves and restores device state
over the reset.

Returns 0 if the device function was successfully reset or negative if
the device doesn't support resetting a single function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
