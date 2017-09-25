.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/bfq-iosched.h

.. _`bfq_service_tree`:

struct bfq_service_tree
=======================

.. c:type:: struct bfq_service_tree

    per ioprio_class service tree.

.. _`bfq_service_tree.definition`:

Definition
----------

.. code-block:: c

    struct bfq_service_tree {
        struct rb_root active;
        struct rb_root idle;
        struct bfq_entity *first_idle;
        struct bfq_entity *last_idle;
        u64 vtime;
        unsigned long wsum;
    }

.. _`bfq_service_tree.members`:

Members
-------

active
    *undescribed*

idle
    *undescribed*

first_idle
    *undescribed*

last_idle
    *undescribed*

vtime
    *undescribed*

wsum
    *undescribed*

.. _`bfq_service_tree.description`:

Description
-----------

Each service tree represents a B-WF2Q+ scheduler on its own.  Each
ioprio_class has its own independent scheduler, and so its own
bfq_service_tree.  All the fields are protected by the queue lock
of the containing bfqd.

.. _`bfq_sched_data`:

struct bfq_sched_data
=====================

.. c:type:: struct bfq_sched_data

    multi-class scheduler.

.. _`bfq_sched_data.definition`:

Definition
----------

.. code-block:: c

    struct bfq_sched_data {
        struct bfq_entity *in_service_entity;
        struct bfq_entity *next_in_service;
        struct bfq_service_tree service_tree[BFQ_IOPRIO_CLASSES];
        unsigned long bfq_class_idle_last_service;
    }

.. _`bfq_sched_data.members`:

Members
-------

in_service_entity
    *undescribed*

next_in_service
    *undescribed*

service_tree
    *undescribed*

bfq_class_idle_last_service
    *undescribed*

.. _`bfq_sched_data.description`:

Description
-----------

bfq_sched_data is the basic scheduler queue.  It supports three
ioprio_classes, and can be used either as a toplevel queue or as an
intermediate queue in a hierarchical setup.

The supported ioprio_classes are the same as in CFQ, in descending
priority order, IOPRIO_CLASS_RT, IOPRIO_CLASS_BE, IOPRIO_CLASS_IDLE.
Requests from higher priority queues are served before all the
requests from lower priority queues; among requests of the same
queue requests are served according to B-WF2Q+.

The schedule is implemented by the service trees, plus the field
\ ``next_in_service``\ , which points to the entity on the active trees
that will be served next, if 1) no changes in the schedule occurs
before the current in-service entity is expired, 2) the in-service
queue becomes idle when it expires, and 3) if the entity pointed by
in_service_entity is not a queue, then the in-service child entity
of the entity pointed by in_service_entity becomes idle on
expiration. This peculiar definition allows for the following
optimization, not yet exploited: while a given entity is still in
service, we already know which is the best candidate for next
service among the other active entitities in the same parent
entity. We can then quickly compare the timestamps of the
in-service entity with those of such best candidate.

All fields are protected by the lock of the containing bfqd.

.. _`bfq_weight_counter`:

struct bfq_weight_counter
=========================

.. c:type:: struct bfq_weight_counter

    counter of the number of all active entities with a given weight.

.. _`bfq_weight_counter.definition`:

Definition
----------

.. code-block:: c

    struct bfq_weight_counter {
        unsigned int weight;
        unsigned int num_active;
        struct rb_node weights_node;
    }

.. _`bfq_weight_counter.members`:

Members
-------

weight
    *undescribed*

num_active
    *undescribed*

weights_node
    *undescribed*

.. _`bfq_entity`:

struct bfq_entity
=================

.. c:type:: struct bfq_entity

    schedulable entity.

.. _`bfq_entity.definition`:

Definition
----------

.. code-block:: c

    struct bfq_entity {
        struct rb_node rb_node;
        struct bfq_weight_counter *weight_counter;
        bool on_st;
        u64 start, finish;
        struct rb_root *tree;
        u64 min_start;
        int service;
        int budget;
        int weight;
        int new_weight;
        int orig_weight;
        struct bfq_entity *parent;
        struct bfq_sched_data *my_sched_data;
        struct bfq_sched_data *sched_data;
        int prio_changed;
    }

.. _`bfq_entity.members`:

Members
-------

rb_node
    *undescribed*

weight_counter
    *undescribed*

on_st
    *undescribed*

start
    *undescribed*

finish
    *undescribed*

tree
    *undescribed*

min_start
    *undescribed*

service
    *undescribed*

budget
    *undescribed*

weight
    *undescribed*

new_weight
    *undescribed*

orig_weight
    *undescribed*

parent
    *undescribed*

my_sched_data
    *undescribed*

sched_data
    *undescribed*

prio_changed
    *undescribed*

.. _`bfq_entity.description`:

Description
-----------

A bfq_entity is used to represent either a bfq_queue (leaf node in the
cgroup hierarchy) or a bfq_group into the upper level scheduler.  Each
entity belongs to the sched_data of the parent group in the cgroup
hierarchy.  Non-leaf entities have also their own sched_data, stored
in \ ``my_sched_data``\ .

Each entity stores independently its priority values; this would
allow different weights on different devices, but this
functionality is not exported to userspace by now.  Priorities and
weights are updated lazily, first storing the new values into the
new\_\* fields, then setting the \ ``prio_changed``\  flag.  As soon as
there is a transition in the entity state that allows the priority
update to take place the effective and the requested priority
values are synchronized.

Unless cgroups are used, the weight value is calculated from the
ioprio to export the same interface as CFQ.  When dealing with
\`\`well-behaved'' queues (i.e., queues that do not spend too much
time to consume their budget and have true sequential behavior, and
when there are no external factors breaking anticipation) the
relative weights at each level of the cgroups hierarchy should be
guaranteed.  All the fields are protected by the queue lock of the
containing bfqd.

.. _`bfq_ttime`:

struct bfq_ttime
================

.. c:type:: struct bfq_ttime

    per process thinktime stats.

.. _`bfq_ttime.definition`:

Definition
----------

.. code-block:: c

    struct bfq_ttime {
        u64 last_end_request;
        u64 ttime_total;
        unsigned long ttime_samples;
        u64 ttime_mean;
    }

.. _`bfq_ttime.members`:

Members
-------

last_end_request
    *undescribed*

ttime_total
    *undescribed*

ttime_samples
    *undescribed*

ttime_mean
    *undescribed*

.. _`bfq_queue`:

struct bfq_queue
================

.. c:type:: struct bfq_queue

    leaf schedulable entity.

.. _`bfq_queue.definition`:

Definition
----------

.. code-block:: c

    struct bfq_queue {
        int ref;
        struct bfq_data *bfqd;
        unsigned short ioprio, ioprio_class;
        unsigned short new_ioprio, new_ioprio_class;
        struct bfq_queue *new_bfqq;
        struct rb_node pos_node;
        struct rb_root *pos_root;
        struct rb_root sort_list;
        struct request *next_rq;
        int queued[2];
        int allocated;
        int meta_pending;
        struct list_head fifo;
        struct bfq_entity entity;
        int max_budget;
        unsigned long budget_timeout;
        int dispatched;
        unsigned long flags;
        struct list_head bfqq_list;
        struct bfq_ttime ttime;
        u32 seek_history;
        struct hlist_node burst_list_node;
        sector_t last_request_pos;
        unsigned int requests_within_timer;
        pid_t pid;
        struct bfq_io_cq *bic;
        unsigned long wr_cur_max_time;
        unsigned long soft_rt_next_start;
        unsigned long last_wr_start_finish;
        unsigned int wr_coeff;
        unsigned long last_idle_bklogged;
        unsigned long service_from_backlogged;
        unsigned long wr_start_at_switch_to_srt;
        unsigned long split_time;
    }

.. _`bfq_queue.members`:

Members
-------

ref
    *undescribed*

bfqd
    *undescribed*

ioprio
    *undescribed*

ioprio_class
    *undescribed*

new_ioprio
    *undescribed*

new_ioprio_class
    *undescribed*

new_bfqq
    *undescribed*

pos_node
    *undescribed*

pos_root
    *undescribed*

sort_list
    *undescribed*

next_rq
    *undescribed*

queued
    *undescribed*

allocated
    *undescribed*

meta_pending
    *undescribed*

fifo
    *undescribed*

entity
    *undescribed*

max_budget
    *undescribed*

budget_timeout
    *undescribed*

dispatched
    *undescribed*

flags
    *undescribed*

bfqq_list
    *undescribed*

ttime
    *undescribed*

seek_history
    *undescribed*

burst_list_node
    *undescribed*

last_request_pos
    *undescribed*

requests_within_timer
    *undescribed*

pid
    *undescribed*

bic
    *undescribed*

wr_cur_max_time
    *undescribed*

soft_rt_next_start
    *undescribed*

last_wr_start_finish
    *undescribed*

wr_coeff
    *undescribed*

last_idle_bklogged
    *undescribed*

service_from_backlogged
    *undescribed*

wr_start_at_switch_to_srt
    *undescribed*

split_time
    *undescribed*

.. _`bfq_queue.description`:

Description
-----------

A bfq_queue is a leaf request queue; it can be associated with an
io_context or more, if it  is  async or shared  between  cooperating
processes. \ ``cgroup``\  holds a reference to the cgroup, to be sure that it
does not disappear while a bfqq still references it (mostly to avoid
races between request issuing and task migration followed by cgroup
destruction).
All the fields are protected by the queue lock of the containing bfqd.

.. _`bfq_io_cq`:

struct bfq_io_cq
================

.. c:type:: struct bfq_io_cq

    per (request_queue, io_context) structure.

.. _`bfq_io_cq.definition`:

Definition
----------

.. code-block:: c

    struct bfq_io_cq {
        struct io_cq icq;
        struct bfq_queue *bfqq[2];
        int ioprio;
    #ifdef CONFIG_BFQ_GROUP_IOSCHED
        uint64_t blkcg_serial_nr;
    #endif
        bool saved_has_short_ttime;
        bool saved_IO_bound;
        bool saved_in_large_burst;
        bool was_in_burst_list;
        unsigned long saved_wr_coeff;
        unsigned long saved_last_wr_start_finish;
        unsigned long saved_wr_start_at_switch_to_srt;
        unsigned int saved_wr_cur_max_time;
        struct bfq_ttime saved_ttime;
    }

.. _`bfq_io_cq.members`:

Members
-------

icq
    *undescribed*

bfqq
    *undescribed*

ioprio
    *undescribed*

blkcg_serial_nr
    *undescribed*

saved_has_short_ttime
    *undescribed*

saved_IO_bound
    *undescribed*

saved_in_large_burst
    *undescribed*

was_in_burst_list
    *undescribed*

saved_wr_coeff
    *undescribed*

saved_last_wr_start_finish
    *undescribed*

saved_wr_start_at_switch_to_srt
    *undescribed*

saved_wr_cur_max_time
    *undescribed*

saved_ttime
    *undescribed*

.. _`bfq_data`:

struct bfq_data
===============

.. c:type:: struct bfq_data

    per-device data structure.

.. _`bfq_data.definition`:

Definition
----------

.. code-block:: c

    struct bfq_data {
        struct request_queue *queue;
        struct list_head dispatch;
        struct bfq_group *root_group;
        struct rb_root queue_weights_tree;
        struct rb_root group_weights_tree;
        int busy_queues;
        int wr_busy_queues;
        int queued;
        int rq_in_driver;
        int max_rq_in_driver;
        int hw_tag_samples;
        int hw_tag;
        int budgets_assigned;
        struct hrtimer idle_slice_timer;
        struct bfq_queue *in_service_queue;
        sector_t last_position;
        u64 last_completion;
        u64 first_dispatch;
        u64 last_dispatch;
        ktime_t last_budget_start;
        ktime_t last_idling_start;
        int peak_rate_samples;
        u32 sequential_samples;
        u64 tot_sectors_dispatched;
        u32 last_rq_max_size;
        u64 delta_from_first;
        u32 peak_rate;
        int bfq_max_budget;
        struct list_head active_list;
        struct list_head idle_list;
        u64 bfq_fifo_expire[2];
        unsigned int bfq_back_penalty;
        unsigned int bfq_back_max;
        u32 bfq_slice_idle;
        int bfq_user_max_budget;
        unsigned int bfq_timeout;
        unsigned int bfq_requests_within_timer;
        bool strict_guarantees;
        unsigned long last_ins_in_burst;
        unsigned long bfq_burst_interval;
        int burst_size;
        struct bfq_entity *burst_parent_entity;
        unsigned long bfq_large_burst_thresh;
        bool large_burst;
        struct hlist_head burst_list;
        bool low_latency;
        unsigned int bfq_wr_coeff;
        unsigned int bfq_wr_max_time;
        unsigned int bfq_wr_rt_max_time;
        unsigned int bfq_wr_min_idle_time;
        unsigned long bfq_wr_min_inter_arr_async;
        unsigned int bfq_wr_max_softrt_rate;
        u64 RT_prod;
        enum bfq_device_speed device_speed;
        struct bfq_queue oom_bfqq;
        spinlock_t lock;
        struct bfq_io_cq *bio_bic;
        struct bfq_queue *bio_bfqq;
    }

.. _`bfq_data.members`:

Members
-------

queue
    *undescribed*

dispatch
    *undescribed*

root_group
    *undescribed*

queue_weights_tree
    *undescribed*

group_weights_tree
    *undescribed*

busy_queues
    *undescribed*

wr_busy_queues
    *undescribed*

queued
    *undescribed*

rq_in_driver
    *undescribed*

max_rq_in_driver
    *undescribed*

hw_tag_samples
    *undescribed*

hw_tag
    *undescribed*

budgets_assigned
    *undescribed*

idle_slice_timer
    *undescribed*

in_service_queue
    *undescribed*

last_position
    *undescribed*

last_completion
    *undescribed*

first_dispatch
    *undescribed*

last_dispatch
    *undescribed*

last_budget_start
    *undescribed*

last_idling_start
    *undescribed*

peak_rate_samples
    *undescribed*

sequential_samples
    *undescribed*

tot_sectors_dispatched
    *undescribed*

last_rq_max_size
    *undescribed*

delta_from_first
    *undescribed*

peak_rate
    *undescribed*

bfq_max_budget
    *undescribed*

active_list
    *undescribed*

idle_list
    *undescribed*

bfq_fifo_expire
    *undescribed*

bfq_back_penalty
    *undescribed*

bfq_back_max
    *undescribed*

bfq_slice_idle
    *undescribed*

bfq_user_max_budget
    *undescribed*

bfq_timeout
    *undescribed*

bfq_requests_within_timer
    *undescribed*

strict_guarantees
    *undescribed*

last_ins_in_burst
    *undescribed*

bfq_burst_interval
    *undescribed*

burst_size
    *undescribed*

burst_parent_entity
    *undescribed*

bfq_large_burst_thresh
    *undescribed*

large_burst
    *undescribed*

burst_list
    *undescribed*

low_latency
    *undescribed*

bfq_wr_coeff
    *undescribed*

bfq_wr_max_time
    *undescribed*

bfq_wr_rt_max_time
    *undescribed*

bfq_wr_min_idle_time
    *undescribed*

bfq_wr_min_inter_arr_async
    *undescribed*

bfq_wr_max_softrt_rate
    *undescribed*

RT_prod
    *undescribed*

device_speed
    *undescribed*

oom_bfqq
    *undescribed*

lock
    *undescribed*

bio_bic
    *undescribed*

bio_bfqq
    *undescribed*

.. _`bfq_data.description`:

Description
-----------

All the fields are protected by \ ``lock``\ .

.. _`bfq_group`:

struct bfq_group
================

.. c:type:: struct bfq_group

    per (device, cgroup) data structure.

.. _`bfq_group.definition`:

Definition
----------

.. code-block:: c

    struct bfq_group {
        struct blkg_policy_data pd;
        char blkg_path[128];
        int ref;
        struct bfq_entity entity;
        struct bfq_sched_data sched_data;
        void *bfqd;
        struct bfq_queue *async_bfqq[2][IOPRIO_BE_NR];
        struct bfq_queue *async_idle_bfqq;
        struct bfq_entity *my_entity;
        int active_entities;
        struct rb_root rq_pos_tree;
        struct bfqg_stats stats;
    }

.. _`bfq_group.members`:

Members
-------

pd
    *undescribed*

blkg_path
    *undescribed*

ref
    *undescribed*

entity
    schedulable entity to insert into the parent group sched_data.

sched_data
    own sched_data, to contain child entities (they may be
    both bfq_queues and bfq_groups).

bfqd
    the bfq_data for the device this group acts upon.

async_bfqq
    array of async queues for all the tasks belonging to
    the group, one queue per ioprio value per ioprio_class,
    except for the idle class that has only one queue.

async_idle_bfqq
    async queue for the idle class (ioprio is ignored).

my_entity
    pointer to \ ``entity``\ , \ ``NULL``\  for the toplevel group; used
    to avoid too many special cases during group creation/
    migration.

active_entities
    number of active entities belonging to the group;
    unused for the root group. Used to know whether there
    are groups with more than one active \ ``bfq_entity``\ 
    (see the comments to the function
    \ :c:func:`bfq_bfqq_may_idle`\ ).

rq_pos_tree
    rbtree sorted by next_request position, used when
    determining if two or more queues have interleaving
    requests (see \ :c:func:`bfq_find_close_cooperator`\ ).

stats
    stats for this bfqg.

.. _`bfq_group.description`:

Description
-----------

Each (device, cgroup) pair has its own bfq_group, i.e., for each cgroup
there is a set of bfq_groups, each one collecting the lower-level
entities belonging to the group that are acting on the same device.

.. _`bfq_group.locking-works-as-follows`:

Locking works as follows
------------------------

o \ ``bfqd``\  is protected by the queue lock, RCU is used to access it
from the readers.
o All the other fields are protected by the \ ``bfqd``\  queue lock.

.. This file was automatic generated / don't edit.

