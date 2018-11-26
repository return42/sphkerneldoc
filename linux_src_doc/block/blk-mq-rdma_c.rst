.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-mq-rdma.c

.. _`blk_mq_rdma_map_queues`:

blk_mq_rdma_map_queues
======================

.. c:function:: int blk_mq_rdma_map_queues(struct blk_mq_tag_set *set, struct ib_device *dev, int first_vec)

    provide a default queue mapping for rdma device

    :param set:
        tagset to provide the mapping for
    :type set: struct blk_mq_tag_set \*

    :param dev:
        rdma device associated with \ ``set``\ .
    :type dev: struct ib_device \*

    :param first_vec:
        first interrupt vectors to use for queues (usually 0)
    :type first_vec: int

.. _`blk_mq_rdma_map_queues.description`:

Description
-----------

This function assumes the rdma device \ ``dev``\  has at least as many available
interrupt vetors as \ ``set``\  has queues.  It will then query it's affinity mask
and built queue mapping that maps a queue to the CPUs that have irq affinity
for the corresponding vector.

In case either the driver passed a \ ``dev``\  with less vectors than
\ ``set->nr_hw_queues``\ , or \ ``dev``\  does not provide an affinity mask for a
vector, we fallback to the naive mapping.

.. This file was automatic generated / don't edit.

