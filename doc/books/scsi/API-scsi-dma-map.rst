.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-dma-map:

============
scsi_dma_map
============

*man scsi_dma_map(9)*

*4.6.0-rc5*

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

Returns the number of sg lists actually used, zero if the sg lists is
NULL, or -ENOMEM if the mapping failed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
