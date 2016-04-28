.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-port-alloc:

==============
ata_port_alloc
==============

*man ata_port_alloc(9)*

*4.6.0-rc5*

allocate and initialize basic ATA port resources


Synopsis
========

.. c:function:: struct ata_port * ata_port_alloc( struct ata_host * host )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
