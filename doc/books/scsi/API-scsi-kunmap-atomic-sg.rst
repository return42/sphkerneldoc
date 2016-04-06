
.. _API-scsi-kunmap-atomic-sg:

=====================
scsi_kunmap_atomic_sg
=====================

*man scsi_kunmap_atomic_sg(9)*

*4.6.0-rc1*

atomically unmap a virtual address, previously mapped with scsi_kmap_atomic_sg


Synopsis
========

.. c:function:: void scsi_kunmap_atomic_sg( void * virt )

Arguments
=========

``virt``
    virtual address to be unmapped
