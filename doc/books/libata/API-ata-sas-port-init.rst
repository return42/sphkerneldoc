
.. _API-ata-sas-port-init:

=================
ata_sas_port_init
=================

*man ata_sas_port_init(9)*

*4.6.0-rc1*

Initialize a SATA device


Synopsis
========

.. c:function:: int ata_sas_port_init( struct ata_port * ap )

Arguments
=========

``ap``
    SATA port to initialize


LOCKING
=======

PCI/etc. bus probe sem.


RETURNS
=======

Zero on success, non-zero on error.
