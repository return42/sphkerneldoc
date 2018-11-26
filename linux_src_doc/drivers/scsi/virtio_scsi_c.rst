.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/virtio_scsi.c

.. _`virtscsi_complete_cmd`:

virtscsi_complete_cmd
=====================

.. c:function:: void virtscsi_complete_cmd(struct virtio_scsi *vscsi, void *buf)

    finish a scsi_cmd and invoke scsi_done

    :param vscsi:
        *undescribed*
    :type vscsi: struct virtio_scsi \*

    :param buf:
        *undescribed*
    :type buf: void \*

.. _`virtscsi_complete_cmd.description`:

Description
-----------

Called with vq_lock held.

.. _`virtscsi_add_cmd`:

virtscsi_add_cmd
================

.. c:function:: int virtscsi_add_cmd(struct virtqueue *vq, struct virtio_scsi_cmd *cmd, size_t req_size, size_t resp_size)

    add a virtio_scsi_cmd to a virtqueue

    :param vq:
        the struct virtqueue we're talking about
    :type vq: struct virtqueue \*

    :param cmd:
        command structure
    :type cmd: struct virtio_scsi_cmd \*

    :param req_size:
        size of the request buffer
    :type req_size: size_t

    :param resp_size:
        size of the response buffer
    :type resp_size: size_t

.. _`virtscsi_change_queue_depth`:

virtscsi_change_queue_depth
===========================

.. c:function:: int virtscsi_change_queue_depth(struct scsi_device *sdev, int qdepth)

    Change a virtscsi target's queue depth

    :param sdev:
        Virtscsi target whose queue depth to change
    :type sdev: struct scsi_device \*

    :param qdepth:
        New queue depth
    :type qdepth: int

.. This file was automatic generated / don't edit.

