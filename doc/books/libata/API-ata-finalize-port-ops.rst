.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-finalize-port-ops:

=====================
ata_finalize_port_ops
=====================

*man ata_finalize_port_ops(9)*

*4.6.0-rc5*

finalize ata_port_operations


Synopsis
========

.. c:function:: void ata_finalize_port_ops( struct ata_port_operations * ops )

Arguments
=========

``ops``
    ata_port_operations to finalize


Description
===========

An ata_port_operations can inherit from another ops and that ops can
again inherit from another. This can go on as many times as necessary as
long as there is no loop in the inheritance chain.

Ops tables are finalized when the host is started. NULL or unspecified
entries are inherited from the closet ancestor which has the method and
the entry is populated with it. After finalization, the ops table
directly points to all the methods and ->inherits is no longer necessary
and cleared.

Using ATA_OP_NULL, inheriting ops can force a method to NULL.


LOCKING
=======

None.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
