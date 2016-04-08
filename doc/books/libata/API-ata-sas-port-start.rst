
.. _API-ata-sas-port-start:

==================
ata_sas_port_start
==================

*man ata_sas_port_start(9)*

*4.6.0-rc1*

Set port up for dma.


Synopsis
========

.. c:function:: int ata_sas_port_start( struct ata_port * ap )

Arguments
=========

``ap``
    Port to initialize


Description
===========

Called just after data structures for each port are initialized.

May be used as the ``port_start`` entry in ata_port_operations.


LOCKING
=======

Inherited from caller.
