
.. _API-ata-link-init:

=============
ata_link_init
=============

*man ata_link_init(9)*

*4.6.0-rc1*

Initialize an ata_link structure


Synopsis
========

.. c:function:: void ata_link_init( struct ata_port * ap, struct ata_link * link, int pmp )

Arguments
=========

``ap``
    ATA port link is attached to

``link``
    Link structure to initialize

``pmp``
    Port multiplier port number


Description
===========

Initialize ``link``.


LOCKING
=======

Kernel thread context (may sleep)
