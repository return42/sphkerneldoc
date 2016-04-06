
.. _API-pci-try-reset-bus:

=================
pci_try_reset_bus
=================

*man pci_try_reset_bus(9)*

*4.6.0-rc1*

Try to reset a PCI bus


Synopsis
========

.. c:function:: int pci_try_reset_bus( struct pci_bus * bus )

Arguments
=========

``bus``
    top level PCI bus to reset


Description
===========

Same as above except return -EAGAIN if the bus cannot be locked
