
.. _API-ata-sas-async-probe:

===================
ata_sas_async_probe
===================

*man ata_sas_async_probe(9)*

*4.6.0-rc1*

simply schedule probing and return


Synopsis
========

.. c:function:: void ata_sas_async_probe( struct ata_port * ap )

Arguments
=========

``ap``
    Port to probe


Description
===========

For batch scheduling of probe for sas attached ata devices, assumes the port has already been through ``ata_sas_port_init``
