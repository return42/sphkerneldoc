
.. _API-ata-host-start:

==============
ata_host_start
==============

*man ata_host_start(9)*

*4.6.0-rc1*

start and freeze ports of an ATA host


Synopsis
========

.. c:function:: int ata_host_start( struct ata_host * host )

Arguments
=========

``host``
    ATA host to start ports for


Description
===========

Start and then freeze ports of ``host``. Started status is recorded in host->flags, so this function can be called multiple times. Ports are guaranteed to get started only once. If
host->ops isn't initialized yet, its set to the first non-dummy port ops.


LOCKING
=======

Inherited from calling layer (may sleep).


RETURNS
=======

0 if all ports are started successfully, -errno otherwise.
