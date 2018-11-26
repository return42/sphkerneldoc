.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/ti/knav_qmss.h

.. _`knav_queue_stats`:

struct knav_queue_stats
=======================

.. c:type:: struct knav_queue_stats

    queue statistics

.. _`knav_queue_stats.definition`:

Definition
----------

.. code-block:: c

    struct knav_queue_stats {
        unsigned int pushes;
        unsigned int pops;
        unsigned int push_errors;
        unsigned int pop_errors;
        unsigned int notifies;
    }

.. _`knav_queue_stats.members`:

Members
-------

pushes
    *undescribed*

pops
    *undescribed*

push_errors
    *undescribed*

pop_errors
    *undescribed*

notifies
    *undescribed*

.. _`knav_queue_stats.pushes`:

pushes
------

number of push operations

.. _`knav_queue_stats.pops`:

pops
----

number of pop operations

.. _`knav_queue_stats.push_errors`:

push_errors
-----------

number of push errors

.. _`knav_queue_stats.pop_errors`:

pop_errors
----------

number of pop errors

.. _`knav_queue_stats.notifies`:

notifies
--------

notifier counts

.. _`knav_reg_queue`:

struct knav_reg_queue
=====================

.. c:type:: struct knav_reg_queue

    queue registers

.. _`knav_reg_queue.definition`:

Definition
----------

.. code-block:: c

    struct knav_reg_queue {
        u32 entry_count;
        u32 byte_count;
        u32 packet_size;
        u32 ptr_size_thresh;
    }

.. _`knav_reg_queue.members`:

Members
-------

entry_count
    valid entries in the queue

byte_count
    total byte count in thhe queue

packet_size
    packet size for the queue

ptr_size_thresh
    packet pointer size threshold

.. _`knav_region`:

struct knav_region
==================

.. c:type:: struct knav_region

    qmss region info

.. _`knav_region.definition`:

Definition
----------

.. code-block:: c

    struct knav_region {
        dma_addr_t dma_start, dma_end;
        void *virt_start, *virt_end;
        unsigned desc_size;
        unsigned used_desc;
        unsigned id;
        unsigned num_desc;
        unsigned link_index;
        const char *name;
        struct list_head list;
        struct list_head pools;
    }

.. _`knav_region.members`:

Members
-------

dma_start
    start and end dma address

dma_end
    *undescribed*

virt_start
    start and end virtual address

virt_end
    *undescribed*

desc_size
    descriptor size

used_desc
    consumed descriptors

id
    region number

num_desc
    total descriptors

link_index
    index of the first descriptor

name
    region name

list
    instance in the device's region list

pools
    list of descriptor pools in the region

.. _`knav_pool`:

struct knav_pool
================

.. c:type:: struct knav_pool

    qmss pools

.. _`knav_pool.definition`:

Definition
----------

.. code-block:: c

    struct knav_pool {
        struct device *dev;
        struct knav_region *region;
        struct knav_queue *queue;
        struct knav_device *kdev;
        int region_offset;
        int num_desc;
        int desc_size;
        int region_id;
        const char *name;
        struct list_head list;
        struct list_head region_inst;
    }

.. _`knav_pool.members`:

Members
-------

dev
    device pointer

region
    qmss region info

queue
    queue registers

kdev
    qmss device pointer

region_offset
    offset from the base

num_desc
    total descriptors

desc_size
    descriptor size

region_id
    region number

name
    pool name

list
    list head

region_inst
    instance in the region's pool list

.. _`knav_queue_inst`:

struct knav_queue_inst
======================

.. c:type:: struct knav_queue_inst

    qmss queue instance properties

.. _`knav_queue_inst.definition`:

Definition
----------

.. code-block:: c

    struct knav_queue_inst {
        u32 *descs;
        atomic_t desc_head, desc_tail, desc_count;
        struct knav_acc_channel *acc;
        struct knav_device *kdev;
        struct knav_range_info *range;
        struct knav_qmgr_info *qmgr;
        u32 id;
        int irq_num;
        int notify_needed;
        atomic_t num_notifiers;
        struct list_head handles;
        const char *name;
        const char *irq_name;
    }

.. _`knav_queue_inst.members`:

Members
-------

descs
    descriptor pointer

desc_head
    descriptor counters

desc_tail
    *undescribed*

desc_count
    *undescribed*

acc
    accumulator channel pointer

kdev
    qmss device pointer

range
    range info

qmgr
    queue manager info

id
    queue instance id

irq_num
    irq line number

notify_needed
    notifier needed based on queue type

num_notifiers
    total notifiers

handles
    list head

name
    queue instance name

irq_name
    irq line name

.. _`knav_queue`:

struct knav_queue
=================

.. c:type:: struct knav_queue

    qmss queue properties

.. _`knav_queue.definition`:

Definition
----------

.. code-block:: c

    struct knav_queue {
        struct knav_reg_queue __iomem *reg_push, *reg_pop, *reg_peek;
        struct knav_queue_inst *inst;
        struct knav_queue_stats __percpu *stats;
        knav_queue_notify_fn notifier_fn;
        void *notifier_fn_arg;
        atomic_t notifier_enabled;
        struct rcu_head rcu;
        unsigned flags;
        struct list_head list;
    }

.. _`knav_queue.members`:

Members
-------

reg_push
    push, pop queue registers

reg_pop
    *undescribed*

reg_peek
    *undescribed*

inst
    qmss queue instance properties

stats
    *undescribed*

notifier_fn
    notifier function

notifier_fn_arg
    notifier function argument

notifier_enabled
    notier enabled for a give queue

rcu
    rcu head

flags
    queue flags

list
    list head

.. This file was automatic generated / don't edit.

