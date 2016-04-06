
.. _API-scsi-dma-map:

============
scsi_dma_map
============

*man scsi_dma_map(9)*

*4.6.0-rc1*

perform DMA mapping against command's sg lists


Synopsis
========

.. c:function:: int scsi_dma_map( struct scsi_cmnd * cmd )

Arguments
=========

``cmd``
    scsi command


Description
===========

Returns the number of sg lists actually used, zero if the sg lists is NULL, or -ENOMEM if the mapping failed.
