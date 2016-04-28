.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-host-detach:

===============
ata_host_detach
===============

*man ata_host_detach(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
