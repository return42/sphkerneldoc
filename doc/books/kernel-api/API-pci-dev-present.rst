.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-dev-present:

===============
pci_dev_present
===============

*man pci_dev_present(9)*

*4.6.0-rc5*

Returns 1 if device matching the device list is present, 0 if not.


Synopsis
========

.. c:function:: int pci_dev_present( const struct pci_device_id * ids )

Arguments
=========

``ids``
    A pointer to a null terminated list of struct pci_device_id
    structures that describe the type of PCI device the caller is trying
    to find.


Obvious fact
============

You do not have a reference to any device that might be found by this
function, so if that device is removed from the system right after this
function is finished, the value will be stale. Use this function to find
devices that are usually built into a system, or for a general hint as
to if another device happens to be present at this specific moment in
time.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
