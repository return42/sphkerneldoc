.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dump-id:

===========
ata_dump_id
===========

*man ata_dump_id(9)*

*4.6.0-rc5*

IDENTIFY DEVICE info debugging output


Synopsis
========

.. c:function:: void ata_dump_id( const u16 * id )

Arguments
=========

``id``
    IDENTIFY DEVICE page to dump


Description
===========

Dump selected 16-bit words from the given IDENTIFY DEVICE page.


LOCKING
=======

caller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
