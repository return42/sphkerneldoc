.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dump-status:

===============
ata_dump_status
===============

*man ata_dump_status(9)*

*4.6.0-rc5*

user friendly display of error info


Synopsis
========

.. c:function:: void ata_dump_status( unsigned id, struct ata_taskfile * tf )

Arguments
=========

``id``
    id of the port in question

``tf``
    ptr to filled out taskfile


Description
===========

Decode and dump the ATA error/status registers for the user so that they
have some idea what really happened at the non make-believe layer.


LOCKING
=======

inherited from caller


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
