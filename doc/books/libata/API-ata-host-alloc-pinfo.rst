.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-host-alloc-pinfo:

====================
ata_host_alloc_pinfo
====================

*man ata_host_alloc_pinfo(9)*

*4.6.0-rc5*

alloc host and init with port_info array


Synopsis
========

.. c:function:: struct ata_host * ata_host_alloc_pinfo( struct device * dev, const struct ata_port_info *const * ppi, int n_ports )

Arguments
=========

``dev``
    generic device this host is associated with

``ppi``
    array of ATA port_info to initialize host with

``n_ports``
    number of ATA ports attached to this host


Description
===========

Allocate ATA host and initialize with info from ``ppi``. If NULL
terminated, ``ppi`` may contain fewer entries than ``n_ports``. The last
entry will be used for the remaining ports.


RETURNS
=======

Allocate ATA host on success, NULL on failure.


LOCKING
=======

Inherited from calling layer (may sleep).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
