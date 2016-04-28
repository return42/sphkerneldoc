.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-num-vf:

==========
pci_num_vf
==========

*man pci_num_vf(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
