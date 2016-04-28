.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-lost-interrupt:

==================
pci_lost_interrupt
==================

*man pci_lost_interrupt(9)*

*4.6.0-rc5*

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

The primary function of this routine is to report a lost interrupt in a
standard way which users can recognise (instead of blaming the driver).


Returns
=======

a suggestion for fixing it (although the driver is not required to act
on this).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
