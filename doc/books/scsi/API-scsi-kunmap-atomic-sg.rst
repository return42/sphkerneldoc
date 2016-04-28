.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-kunmap-atomic-sg:

=====================
scsi_kunmap_atomic_sg
=====================

*man scsi_kunmap_atomic_sg(9)*

*4.6.0-rc5*

atomically unmap a virtual address, previously mapped with
scsi_kmap_atomic_sg


Synopsis
========

.. c:function:: void scsi_kunmap_atomic_sg( void * virt )

Arguments
=========

``virt``
    virtual address to be unmapped


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
