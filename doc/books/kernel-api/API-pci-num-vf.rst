
.. _API-pci-num-vf:

==========
pci_num_vf
==========

*man pci_num_vf(9)*

*4.6.0-rc1*

return number of VFs associated with a PF device_release_driver


Synopsis
========

.. c:function:: int pci_num_vf( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device


Description
===========

Returns number of VFs, or 0 if SR-IOV is not enabled.
