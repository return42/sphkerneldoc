.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/blk-mq.h

.. _`blk_mq_hw_ctx`:

struct blk_mq_hw_ctx
====================

.. c:type:: struct blk_mq_hw_ctx

    State for a hardware queue facing the hardware block device

.. _`blk_mq_hw_ctx.definition`:

Definition
----------

.. code-block:: c

    struct blk_mq_hw_ctx {
        struct {
            spinlock_t lock;
            struct list_head dispatch;
            unsigned long state;
        } ____cacheline_aligned_in_smp;
        struct delayed_work run_work;
        cpumask_var_t cpumask;
        int next_cpu;
        int next_cpu_batch;
        unsigned long flags;
        void *sched_data;
        struct request_queue *queue;
        struct blk_flush_queue *fq;
        void *driver_data;
        struct sbitmap ctx_map;
        struct blk_mq_ctx *dispatch_from;
        struct blk_mq_ctx **ctxs;
        unsigned int nr_ctx;
        wait_queue_entry_t dispatch_wait;
        atomic_t wait_index;
        struct blk_mq_tags *tags;
        struct blk_mq_tags *sched_tags;
        unsigned long queued;
        unsigned long run;
    #define BLK_MQ_MAX_DISPATCH_ORDER 7
        unsigned long dispatched[BLK_MQ_MAX_DISPATCH_ORDER];
        unsigned int numa_node;
        unsigned int queue_num;
        atomic_t nr_active;
        unsigned int nr_expired;
        struct hlist_node cpuhp_dead;
        struct kobject kobj;
        unsigned long poll_considered;
        unsigned long poll_invoked;
        unsigned long poll_success;
    #ifdef CONFIG_BLK_DEBUG_FS
        struct dentry *debugfs_dir;
        struct dentry *sched_debugfs_dir;
    #endif
        struct srcu_struct srcu[0];
    }

.. _`blk_mq_hw_ctx.members`:

Members
-------

\____cacheline_aligned_in_smp
    *undescribed*

run_work
    *undescribed*

cpumask
    *undescribed*

next_cpu
    *undescribed*

next_cpu_batch
    *undescribed*

flags
    *undescribed*

sched_data
    *undescribed*

queue
    *undescribed*

fq
    *undescribed*

driver_data
    *undescribed*

ctx_map
    *undescribed*

dispatch_from
    *undescribed*

ctxs
    *undescribed*

nr_ctx
    *undescribed*

dispatch_wait
    *undescribed*

wait_index
    *undescribed*

tags
    *undescribed*

sched_tags
    *undescribed*

queued
    *undescribed*

run
    *undescribed*

dispatched
    *undescribed*

numa_node
    *undescribed*

queue_num
    *undescribed*

nr_active
    *undescribed*

nr_expired
    *undescribed*

cpuhp_dead
    *undescribed*

kobj
    *undescribed*

poll_considered
    *undescribed*

poll_invoked
    *undescribed*

poll_success
    *undescribed*

debugfs_dir
    *undescribed*

sched_debugfs_dir
    *undescribed*

srcu
    *undescribed*

.. _`blk_mq_mark_complete`:

blk_mq_mark_complete
====================

.. c:function:: bool blk_mq_mark_complete(struct request *rq)

    Set request state to complete

    :param struct request \*rq:
        request to set to complete state

.. _`blk_mq_mark_complete.description`:

Description
-----------

Returns true if request state was successfully set to complete. If
successful, the caller is responsibile for seeing this request is ended, as
blk_mq_complete_request will not work again.

.. This file was automatic generated / don't edit.

