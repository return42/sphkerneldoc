.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_lib_dma.c

.. _`scsi_dma_map`:

scsi_dma_map
============

.. c:function:: int scsi_dma_map(struct scsi_cmnd *cmd)

    perform DMA mapping against command's sg lists

    :param cmd:
        scsi command
    :type cmd: struct scsi_cmnd \*

.. _`scsi_dma_map.description`:

Description
-----------

Returns the number of sg lists actually used, zero if the sg lists
is NULL, or -ENOMEM if the mapping failed.

.. _`scsi_dma_unmap`:

scsi_dma_unmap
==============

.. c:function:: void scsi_dma_unmap(struct scsi_cmnd *cmd)

    unmap command's sg lists mapped by scsi_dma_map

    :param cmd:
        scsi command
    :type cmd: struct scsi_cmnd \*

.. This file was automatic generated / don't edit.

