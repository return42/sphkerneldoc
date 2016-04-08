
.. _API-ata-host-detach:

===============
ata_host_detach
===============

*man ata_host_detach(9)*

*4.6.0-rc1*

Detach all ports of an ATA host


Synopsis
========

.. c:function:: void ata_host_detach( struct ata_host * host )

Arguments
=========

``host``
    Host to detach


Description
===========

Detach all ports of ``host``.


LOCKING
=======

Kernel thread context (may sleep).
