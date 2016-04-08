
.. _API-ata-port-alloc:

==============
ata_port_alloc
==============

*man ata_port_alloc(9)*

*4.6.0-rc1*

allocate and initialize basic ATA port resources


Synopsis
========

.. c:function:: struct ata_port ⋆ ata_port_alloc( struct ata_host * host )

Arguments
=========

``host``
    ATA host this allocated port belongs to


Description
===========

Allocate and initialize basic ATA port resources.


RETURNS
=======

Allocate ATA port on success, NULL on failure.


LOCKING
=======

Inherited from calling layer (may sleep).
