
.. _API-pci-lost-interrupt:

==================
pci_lost_interrupt
==================

*man pci_lost_interrupt(9)*

*4.6.0-rc1*

reports a lost PCI interrupt


Synopsis
========

.. c:function:: enum pci_lost_interrupt_reason pci_lost_interrupt( struct pci_dev * pdev )

Arguments
=========

``pdev``
    device whose interrupt is lost


Description
===========

The primary function of this routine is to report a lost interrupt in a standard way which users can recognise (instead of blaming the driver).


Returns
=======

a suggestion for fixing it (although the driver is not required to act on this).
