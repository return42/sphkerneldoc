
.. _API-pci-probe-reset-slot:

====================
pci_probe_reset_slot
====================

*man pci_probe_reset_slot(9)*

*4.6.0-rc1*

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

Return 0 if slot can be reset, negative if a slot reset is not supported.
