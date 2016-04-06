
.. _API-scsi-kmap-atomic-sg:

===================
scsi_kmap_atomic_sg
===================

*man scsi_kmap_atomic_sg(9)*

*4.6.0-rc1*

find and atomically map an sg-elemnt


Synopsis
========

.. c:function:: void ⋆ scsi_kmap_atomic_sg( struct scatterlist * sgl, int sg_count, size_t * offset, size_t * len )

Arguments
=========

``sgl``
    scatter-gather list

``sg_count``
    number of segments in sg

``offset``
    offset in bytes into sg, on return offset into the mapped area

``len``
    bytes to map, on return number of bytes mapped


Description
===========

Returns virtual address of the start of the mapped page
