.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/virtio_scsi.c

.. _`virtscsi_complete_cmd`:

virtscsi_complete_cmd
=====================

.. c:function:: void virtscsi_complete_cmd(struct virtio_scsi *vscsi, void *buf)

    finish a scsi_cmd and invoke scsi_done

    :param struct virtio_scsi \*vscsi:
        *undescribed*

    :param void \*buf:
        *undescribed*

.. _`virtscsi_complete_cmd.description`:

Description
-----------

Called with vq_lock held.

.. _`virtscsi_add_cmd`:

virtscsi_add_cmd
================

.. c:function:: int virtscsi_add_cmd(struct virtqueue *vq, struct virtio_scsi_cmd *cmd, size_t req_size, size_t resp_size)

    add a virtio_scsi_cmd to a virtqueue

    :param struct virtqueue \*vq:
        the struct virtqueue we're talking about

    :param struct virtio_scsi_cmd \*cmd:
        command structure

    :param size_t req_size:
        size of the request buffer

    :param size_t resp_size:
        size of the response buffer

.. _`virtscsi_change_queue_depth`:

virtscsi_change_queue_depth
===========================

.. c:function:: int virtscsi_change_queue_depth(struct scsi_device *sdev, int qdepth)

    Change a virtscsi target's queue depth

    :param struct scsi_device \*sdev:
        Virtscsi target whose queue depth to change

    :param int qdepth:
        New queue depth

.. This file was automatic generated / don't edit.

