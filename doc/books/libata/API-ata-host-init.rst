
.. _API-ata-host-init:

=============
ata_host_init
=============

*man ata_host_init(9)*

*4.6.0-rc1*

Initialize a host struct for sas (ipr, libsas)


Synopsis
========

.. c:function:: void ata_host_init( struct ata_host * host, struct device * dev, struct ata_port_operations * ops )

Arguments
=========

``host``
    host to initialize

``dev``
    device host is attached to

``ops``
    port_ops
