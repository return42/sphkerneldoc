.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-build-rw-tf:

===============
ata_build_rw_tf
===============

*man ata_build_rw_tf(9)*

*4.6.0-rc5*

Build ATA taskfile for given read/write request


Synopsis
========

.. c:function:: int ata_build_rw_tf( struct ata_taskfile * tf, struct ata_device * dev, u64 block, u32 n_block, unsigned int tf_flags, unsigned int tag )

Arguments
=========

``tf``
    Target ATA taskfile

``dev``
    ATA device ``tf`` belongs to

``block``
    Block address

``n_block``
    Number of blocks

``tf_flags``
    RW/FUA etc...

``tag``
    tag


LOCKING
=======

None.

Build ATA taskfile ``tf`` for read/write request described by ``block``,
``n_block``, ``tf_flags`` and ``tag`` on ``dev``.


RETURNS
=======

0 on success, -ERANGE if the request is too large for ``dev``, -EINVAL
if the request is invalid.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
