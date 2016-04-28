.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-detect-bound-ports:

======================
mpt_detect_bound_ports
======================

*man mpt_detect_bound_ports(9)*

*4.6.0-rc5*

Search for matching PCI bus/dev_function


Synopsis
========

.. c:function:: void mpt_detect_bound_ports( MPT_ADAPTER * ioc, struct pci_dev * pdev )

Arguments
=========

``ioc``
    Pointer to MPT adapter structure

``pdev``
    Pointer to (struct pci_dev) structure


Description
===========

Search for PCI bus/dev_function which matches PCI bus/dev_function
(+/-1) for newly discovered 929, 929X, 1030 or 1035.

If match on PCI dev_function +/-1 is found, bind the two MPT adapters
using alt_ioc pointer fields in their ``MPT_ADAPTER`` structures.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
