.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-mq.h

.. _`blk_mq_ctx`:

struct blk_mq_ctx
=================

.. c:type:: struct blk_mq_ctx

    State for a software queue facing the submitting CPUs

.. _`blk_mq_ctx.definition`:

Definition
----------

.. code-block:: c

    struct blk_mq_ctx {
        struct {
            spinlock_t lock;
            struct list_head rq_list;
        } ____cacheline_aligned_in_smp;
        unsigned int cpu;
        unsigned int index_hw;
        unsigned long rq_dispatched[2];
        unsigned long rq_merged;
        unsigned long ____cacheline_aligned_in_smp rq_completed[2];
        struct request_queue *queue;
        struct kobject kobj;
    }

.. _`blk_mq_ctx.members`:

Members
-------

\____cacheline_aligned_in_smp
    *undescribed*

cpu
    *undescribed*

index_hw
    *undescribed*

rq_dispatched
    *undescribed*

rq_merged
    *undescribed*

rq_completed
    *undescribed*

queue
    *undescribed*

kobj
    *undescribed*

.. _`blk_mq_rq_state`:

blk_mq_rq_state
===============

.. c:function:: enum mq_rq_state blk_mq_rq_state(struct request *rq)

    read the current MQ_RQ\_\* state of a request

    :param struct request \*rq:
        target request.

.. This file was automatic generated / don't edit.

