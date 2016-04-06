
.. _API-pci-set-cacheline-size:

======================
pci_set_cacheline_size
======================

*man pci_set_cacheline_size(9)*

*4.6.0-rc1*

ensure the CACHE_LINE_SIZE register is programmed


Synopsis
========

.. c:function:: int pci_set_cacheline_size( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device for which MWI is to be enabled


Description
===========

Helper function for pci_set_mwi. Originally copied from drivers/net/acenic.c. Copyright 1998-2001 by Jes Sorensen, <jes``trained``-monkey.org>.


RETURNS
=======

An appropriate -ERRNO error value on error, or zero for success.
