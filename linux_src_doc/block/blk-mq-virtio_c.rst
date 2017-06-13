.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-mq-virtio.c

.. _`blk_mq_virtio_map_queues`:

blk_mq_virtio_map_queues
========================

.. c:function:: int blk_mq_virtio_map_queues(struct blk_mq_tag_set *set, struct virtio_device *vdev, int first_vec)

    provide a default queue mapping for virtio device

    :param struct blk_mq_tag_set \*set:
        tagset to provide the mapping for

    :param struct virtio_device \*vdev:
        virtio device associated with \ ``set``\ .

    :param int first_vec:
        first interrupt vectors to use for queues (usually 0)

.. _`blk_mq_virtio_map_queues.description`:

Description
-----------

This function assumes the virtio device \ ``vdev``\  has at least as many available
interrupt vetors as \ ``set``\  has queues.  It will then queuery the vector
corresponding to each queue for it's affinity mask and built queue mapping
that maps a queue to the CPUs that have irq affinity for the corresponding
vector.

.. This file was automatic generated / don't edit.

