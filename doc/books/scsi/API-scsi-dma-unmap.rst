
.. _API-scsi-dma-unmap:

==============
scsi_dma_unmap
==============

*man scsi_dma_unmap(9)*

*4.6.0-rc1*

unmap command's sg lists mapped by scsi_dma_map


Synopsis
========

.. c:function:: void scsi_dma_unmap( struct scsi_cmnd * cmd )

Arguments
=========

``cmd``
    scsi command
