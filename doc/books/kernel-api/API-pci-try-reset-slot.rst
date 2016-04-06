
.. _API-pci-try-reset-slot:

==================
pci_try_reset_slot
==================

*man pci_try_reset_slot(9)*

*4.6.0-rc1*

Try to reset a PCI slot


Synopsis
========

.. c:function:: int pci_try_reset_slot( struct pci_slot * slot )

Arguments
=========

``slot``
    PCI slot to reset


Description
===========

Same as above except return -EAGAIN if the slot cannot be locked
