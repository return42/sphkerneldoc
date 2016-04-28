.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-try-reset-slot:

==================
pci_try_reset_slot
==================

*man pci_try_reset_slot(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
