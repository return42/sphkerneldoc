
.. _API-mpt-attach:

==========
mpt_attach
==========

*man mpt_attach(9)*

*4.6.0-rc1*

Install a PCI intelligent MPT adapter.


Synopsis
========

.. c:function:: int mpt_attach( struct pci_dev * pdev, const struct pci_device_id * id )

Arguments
=========

``pdev``
    Pointer to pci_dev structure

``id``
    PCI device ID information


Description
===========

This routine performs all the steps necessary to bring the IOC of a MPT adapter to a OPERATIONAL state. This includes registering memory regions, registering the interrupt, and
allocating request and reply memory pools.

This routine also pre-fetches the LAN MAC address of a Fibre Channel MPT adapter.

Returns 0 for success, non-zero for failure.


TODO
====

Add support for polled controllers
