.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-probe-reset-slot:

====================
pci_probe_reset_slot
====================

*man pci_probe_reset_slot(9)*

*4.6.0-rc5*

probe whether a PCI slot can be reset


Synopsis
========

.. c:function:: int pci_probe_reset_slot( struct pci_slot * slot )

Arguments
=========

``slot``
    PCI slot to probe


Description
===========

Return 0 if slot can be reset, negative if a slot reset is not
supported.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
