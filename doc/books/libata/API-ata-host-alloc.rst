
.. _API-ata-host-alloc:

==============
ata_host_alloc
==============

*man ata_host_alloc(9)*

*4.6.0-rc1*

allocate and init basic ATA host resources


Synopsis
========

.. c:function:: struct ata_host ⋆ ata_host_alloc( struct device * dev, int max_ports )

Arguments
=========

``dev``
    generic device this host is associated with

``max_ports``
    maximum number of ATA ports associated with this host


Description
===========

Allocate and initialize basic ATA host resources. LLD calls this function to allocate a host, initializes it fully and attaches it using ``ata_host_register``.

``max_ports`` ports are allocated and host->n_ports is initialized to ``max_ports``. The caller is allowed to decrease host->n_ports before calling ``ata_host_register``. The
unused ports will be automatically freed on registration.


RETURNS
=======

Allocate ATA host on success, NULL on failure.


LOCKING
=======

Inherited from calling layer (may sleep).
