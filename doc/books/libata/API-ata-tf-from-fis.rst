.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-tf-from-fis:

===============
ata_tf_from_fis
===============

*man ata_tf_from_fis(9)*

*4.6.0-rc5*

Convert SATA FIS to ATA taskfile


Synopsis
========

.. c:function:: void ata_tf_from_fis( const u8 * fis, struct ata_taskfile * tf )

Arguments
=========

``fis``
    Buffer from which data will be input

``tf``
    Taskfile to output


Description
===========

Converts a serial ATA FIS structure to a standard ATA taskfile.


LOCKING
=======

Inherited from caller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
