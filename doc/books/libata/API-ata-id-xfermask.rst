.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-id-xfermask:

===============
ata_id_xfermask
===============

*man ata_id_xfermask(9)*

*4.6.0-rc5*

Compute xfermask from the given IDENTIFY data


Synopsis
========

.. c:function:: unsigned long ata_id_xfermask( const u16 * id )

Arguments
=========

``id``
    IDENTIFY data to compute xfer mask from


Description
===========

Compute the xfermask for this device. This is not as trivial as it seems
if we must consider early devices correctly.


FIXME
=====

pre IDE drive timing (do we care ?).


LOCKING
=======

None.


RETURNS
=======

Computed xfermask


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
