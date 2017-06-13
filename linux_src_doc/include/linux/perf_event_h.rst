.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/perf_event.h

.. _`hw_perf_event`:

struct hw_perf_event
====================

.. c:type:: struct hw_perf_event

    performance event hardware details:

.. _`hw_perf_event.definition`:

Definition
----------

.. code-block:: c

    struct hw_perf_event {
    #ifdef CONFIG_PERF_EVENTS
        union {unnamed_union};
        struct task_struct *target;
        void *addr_filters;
        unsigned long addr_filters_gen;
    #define PERF_HES_STOPPED 0x01
    #define PERF_HES_UPTODATE 0x02
    #define PERF_HES_ARCH 0x04
        int state;
        local64_t prev_count;
        u64 sample_period;
        u64 last_period;
        local64_t period_left;
        u64 interrupts_seq;
        u64 interrupts;
        u64 freq_time_stamp;
        u64 freq_count_stamp;
    #endif
    }

.. _`hw_perf_event.members`:

Members
-------

{unnamed_union}
    anonymous


target
    *undescribed*

addr_filters
    *undescribed*

addr_filters_gen
    *undescribed*

state
    *undescribed*

prev_count
    *undescribed*

sample_period
    *undescribed*

last_period
    *undescribed*

period_left
    *undescribed*

interrupts_seq
    *undescribed*

interrupts
    *undescribed*

freq_time_stamp
    *undescribed*

freq_count_stamp
    *undescribed*

.. _`perf_pmu_cap_no_interrupt`:

PERF_PMU_CAP_NO_INTERRUPT
=========================

.. c:function::  PERF_PMU_CAP_NO_INTERRUPT()

    :capabilities flags

.. _`pmu`:

struct pmu
==========

.. c:type:: struct pmu

    generic performance monitoring unit

.. _`pmu.definition`:

Definition
----------

.. code-block:: c

    struct pmu {
        struct list_head entry;
        struct module *module;
        struct device *dev;
        const struct attribute_group **attr_groups;
        const char *name;
        int type;
        int capabilities;
        int * __percpu pmu_disable_count;
        struct perf_cpu_context * __percpu pmu_cpu_context;
        atomic_t exclusive_cnt;
        int task_ctx_nr;
        int hrtimer_interval_ms;
        unsigned int nr_addr_filters;
        void (*pmu_enable)(struct pmu *pmu);
        void (*pmu_disable)(struct pmu *pmu);
        int (*event_init)(struct perf_event *event);
        void (*event_mapped)(struct perf_event *event);
        void (*event_unmapped)(struct perf_event *event);
    #define PERF_EF_START 0x01
    #define PERF_EF_RELOAD 0x02
    #define PERF_EF_UPDATE 0x04
        int (*add)(struct perf_event *event, int flags);
        void (*del)(struct perf_event *event, int flags);
        void (*start)(struct perf_event *event, int flags);
        void (*stop)(struct perf_event *event, int flags);
        void (*read)(struct perf_event *event);
        void (*start_txn)(struct pmu *pmu, unsigned int txn_flags);
        int (*commit_txn)(struct pmu *pmu);
        void (*cancel_txn)(struct pmu *pmu);
        int (*event_idx)(struct perf_event *event);
        void (*sched_task)(struct perf_event_context *ctx, bool sched_in);
        size_t task_ctx_size;
        u64 (*count)(struct perf_event *event);
        void *(*setup_aux)(int cpu, void **pages, int nr_pages, bool overwrite);
        void (*free_aux)(void *aux);
        int (*addr_filters_validate)(struct list_head *filters);
        void (*addr_filters_sync)(struct perf_event *event);
        int (*filter_match)(struct perf_event *event);
    }

.. _`pmu.members`:

Members
-------

entry
    *undescribed*

module
    *undescribed*

dev
    *undescribed*

attr_groups
    *undescribed*

name
    *undescribed*

type
    *undescribed*

capabilities
    *undescribed*

pmu_disable_count
    *undescribed*

pmu_cpu_context
    *undescribed*

exclusive_cnt
    *undescribed*

task_ctx_nr
    *undescribed*

hrtimer_interval_ms
    *undescribed*

nr_addr_filters
    *undescribed*

pmu_enable
    *undescribed*

pmu_disable
    *undescribed*

event_init
    *undescribed*

event_mapped
    *undescribed*

event_unmapped
    *undescribed*

add
    *undescribed*

del
    *undescribed*

start
    *undescribed*

stop
    *undescribed*

read
    *undescribed*

start_txn
    *undescribed*

commit_txn
    *undescribed*

cancel_txn
    *undescribed*

event_idx
    *undescribed*

sched_task
    *undescribed*

task_ctx_size
    *undescribed*

count
    *undescribed*

setup_aux
    *undescribed*

free_aux
    *undescribed*

addr_filters_validate
    *undescribed*

addr_filters_sync
    *undescribed*

filter_match
    *undescribed*

.. _`perf_addr_filter`:

struct perf_addr_filter
=======================

.. c:type:: struct perf_addr_filter

    address range filter definition

.. _`perf_addr_filter.definition`:

Definition
----------

.. code-block:: c

    struct perf_addr_filter {
        struct list_head entry;
        struct inode *inode;
        unsigned long offset;
        unsigned long size;
        unsigned int range:1;
        unsigned int filter:1:1;
    }

.. _`perf_addr_filter.members`:

Members
-------

entry
    event's filter list linkage

inode
    object file's inode for file-based filters

offset
    filter range offset

size
    filter range size

range
    1: range, 0: address

filter
    1: filter/start, 0: stop

.. _`perf_addr_filter.description`:

Description
-----------

This is a hardware-agnostic filter configuration as specified by the user.

.. _`perf_addr_filters_head`:

struct perf_addr_filters_head
=============================

.. c:type:: struct perf_addr_filters_head

    container for address range filters

.. _`perf_addr_filters_head.definition`:

Definition
----------

.. code-block:: c

    struct perf_addr_filters_head {
        struct list_head list;
        raw_spinlock_t lock;
        unsigned int nr_file_filters;
    }

.. _`perf_addr_filters_head.members`:

Members
-------

list
    list of filters for this event

lock
    spinlock that serializes accesses to the \ ``list``\  and event's
    (and its children's) filter generations.

nr_file_filters
    number of file-based filters

.. _`perf_addr_filters_head.description`:

Description
-----------

A child event will use parent's \ ``list``\  (and therefore \ ``lock``\ ), so they are
bundled together; see \ :c:func:`perf_event_addr_filters`\ .

.. _`perf_event_active_state`:

enum perf_event_active_state
============================

.. c:type:: enum perf_event_active_state

    the states of a event

.. _`perf_event_active_state.definition`:

Definition
----------

.. code-block:: c

    enum perf_event_active_state {
        PERF_EVENT_STATE_DEAD,
        PERF_EVENT_STATE_EXIT,
        PERF_EVENT_STATE_ERROR,
        PERF_EVENT_STATE_OFF,
        PERF_EVENT_STATE_INACTIVE,
        PERF_EVENT_STATE_ACTIVE
    };

.. _`perf_event_active_state.constants`:

Constants
---------

PERF_EVENT_STATE_DEAD
    *undescribed*

PERF_EVENT_STATE_EXIT
    *undescribed*

PERF_EVENT_STATE_ERROR
    *undescribed*

PERF_EVENT_STATE_OFF
    *undescribed*

PERF_EVENT_STATE_INACTIVE
    *undescribed*

PERF_EVENT_STATE_ACTIVE
    *undescribed*

.. _`perf_event`:

struct perf_event
=================

.. c:type:: struct perf_event

    performance event kernel representation:

.. _`perf_event.definition`:

Definition
----------

.. code-block:: c

    struct perf_event {
    #ifdef CONFIG_PERF_EVENTS
        struct list_head event_entry;
        struct list_head group_entry;
        struct list_head sibling_list;
        struct list_head migrate_entry;
        struct hlist_node hlist_entry;
        struct list_head active_entry;
        int nr_siblings;
        int event_caps;
        int group_caps;
        struct perf_event *group_leader;
        struct pmu *pmu;
        void *pmu_private;
        enum perf_event_active_state state;
        unsigned int attach_state;
        local64_t count;
        atomic64_t child_count;
        u64 total_time_enabled;
        u64 total_time_running;
        u64 tstamp_enabled;
        u64 tstamp_running;
        u64 tstamp_stopped;
        u64 shadow_ctx_time;
        struct perf_event_attr attr;
        u16 header_size;
        u16 id_header_size;
        u16 read_size;
        struct hw_perf_event hw;
        struct perf_event_context *ctx;
        atomic_long_t refcount;
        atomic64_t child_total_time_enabled;
        atomic64_t child_total_time_running;
        struct mutex child_mutex;
        struct list_head child_list;
        struct perf_event *parent;
        int oncpu;
        int cpu;
        struct list_head owner_entry;
        struct task_struct *owner;
        struct mutex mmap_mutex;
        atomic_t mmap_count;
        struct ring_buffer *rb;
        struct list_head rb_entry;
        unsigned long rcu_batches;
        int rcu_pending;
        wait_queue_head_t waitq;
        struct fasync_struct *fasync;
        int pending_wakeup;
        int pending_kill;
        int pending_disable;
        struct irq_work pending;
        atomic_t event_limit;
        struct perf_addr_filters_head addr_filters;
        unsigned long *addr_filters_offs;
        unsigned long addr_filters_gen;
        void (*destroy)(struct perf_event *);
        struct rcu_head rcu_head;
        struct pid_namespace *ns;
        u64 id;
        u64 (*clock)(void);
        perf_overflow_handler_t overflow_handler;
        void *overflow_handler_context;
    #ifdef CONFIG_BPF_SYSCALL
        perf_overflow_handler_t orig_overflow_handler;
        struct bpf_prog *prog;
    #endif
    #ifdef CONFIG_EVENT_TRACING
        struct trace_event_call *tp_event;
        struct event_filter *filter;
    #ifdef CONFIG_FUNCTION_TRACER
        struct ftrace_ops ftrace_ops;
    #endif
    #endif
    #ifdef CONFIG_CGROUP_PERF
        struct perf_cgroup *cgrp;
        int cgrp_defer_enabled;
    #endif
        struct list_head sb_list;
    #endif
    }

.. _`perf_event.members`:

Members
-------

event_entry
    *undescribed*

group_entry
    *undescribed*

sibling_list
    *undescribed*

migrate_entry
    *undescribed*

hlist_entry
    *undescribed*

active_entry
    *undescribed*

nr_siblings
    *undescribed*

event_caps
    *undescribed*

group_caps
    *undescribed*

group_leader
    *undescribed*

pmu
    *undescribed*

pmu_private
    *undescribed*

state
    *undescribed*

attach_state
    *undescribed*

count
    *undescribed*

child_count
    *undescribed*

total_time_enabled
    *undescribed*

total_time_running
    *undescribed*

tstamp_enabled
    *undescribed*

tstamp_running
    *undescribed*

tstamp_stopped
    *undescribed*

shadow_ctx_time
    *undescribed*

attr
    *undescribed*

header_size
    *undescribed*

id_header_size
    *undescribed*

read_size
    *undescribed*

hw
    *undescribed*

ctx
    *undescribed*

refcount
    *undescribed*

child_total_time_enabled
    *undescribed*

child_total_time_running
    *undescribed*

child_mutex
    *undescribed*

child_list
    *undescribed*

parent
    *undescribed*

oncpu
    *undescribed*

cpu
    *undescribed*

owner_entry
    *undescribed*

owner
    *undescribed*

mmap_mutex
    *undescribed*

mmap_count
    *undescribed*

rb
    *undescribed*

rb_entry
    *undescribed*

rcu_batches
    *undescribed*

rcu_pending
    *undescribed*

waitq
    *undescribed*

fasync
    *undescribed*

pending_wakeup
    *undescribed*

pending_kill
    *undescribed*

pending_disable
    *undescribed*

pending
    *undescribed*

event_limit
    *undescribed*

addr_filters
    *undescribed*

addr_filters_offs
    *undescribed*

addr_filters_gen
    *undescribed*

destroy
    *undescribed*

rcu_head
    *undescribed*

ns
    *undescribed*

id
    *undescribed*

clock
    *undescribed*

overflow_handler
    *undescribed*

overflow_handler_context
    *undescribed*

orig_overflow_handler
    *undescribed*

prog
    *undescribed*

tp_event
    *undescribed*

filter
    *undescribed*

ftrace_ops
    *undescribed*

cgrp
    *undescribed*

cgrp_defer_enabled
    *undescribed*

sb_list
    *undescribed*

.. _`perf_event_context`:

struct perf_event_context
=========================

.. c:type:: struct perf_event_context

    event context structure

.. _`perf_event_context.definition`:

Definition
----------

.. code-block:: c

    struct perf_event_context {
        struct pmu *pmu;
        raw_spinlock_t lock;
        struct mutex mutex;
        struct list_head active_ctx_list;
        struct list_head pinned_groups;
        struct list_head flexible_groups;
        struct list_head event_list;
        int nr_events;
        int nr_active;
        int is_active;
        int nr_stat;
        int nr_freq;
        int rotate_disable;
        atomic_t refcount;
        struct task_struct *task;
        u64 time;
        u64 timestamp;
        struct perf_event_context *parent_ctx;
        u64 parent_gen;
        u64 generation;
        int pin_count;
    #ifdef CONFIG_CGROUP_PERF
        int nr_cgroups;
    #endif
        void *task_ctx_data;
        struct rcu_head rcu_head;
    }

.. _`perf_event_context.members`:

Members
-------

pmu
    *undescribed*

lock
    *undescribed*

mutex
    *undescribed*

active_ctx_list
    *undescribed*

pinned_groups
    *undescribed*

flexible_groups
    *undescribed*

event_list
    *undescribed*

nr_events
    *undescribed*

nr_active
    *undescribed*

is_active
    *undescribed*

nr_stat
    *undescribed*

nr_freq
    *undescribed*

rotate_disable
    *undescribed*

refcount
    *undescribed*

task
    *undescribed*

time
    *undescribed*

timestamp
    *undescribed*

parent_ctx
    *undescribed*

parent_gen
    *undescribed*

generation
    *undescribed*

pin_count
    *undescribed*

nr_cgroups
    *undescribed*

task_ctx_data
    *undescribed*

rcu_head
    *undescribed*

.. _`perf_cpu_context`:

struct perf_cpu_context
=======================

.. c:type:: struct perf_cpu_context

    per cpu event context structure

.. _`perf_cpu_context.definition`:

Definition
----------

.. code-block:: c

    struct perf_cpu_context {
        struct perf_event_context ctx;
        struct perf_event_context *task_ctx;
        int active_oncpu;
        int exclusive;
        raw_spinlock_t hrtimer_lock;
        struct hrtimer hrtimer;
        ktime_t hrtimer_interval;
        unsigned int hrtimer_active;
    #ifdef CONFIG_CGROUP_PERF
        struct perf_cgroup *cgrp;
        struct list_head cgrp_cpuctx_entry;
    #endif
        struct list_head sched_cb_entry;
        int sched_cb_usage;
    }

.. _`perf_cpu_context.members`:

Members
-------

ctx
    *undescribed*

task_ctx
    *undescribed*

active_oncpu
    *undescribed*

exclusive
    *undescribed*

hrtimer_lock
    *undescribed*

hrtimer
    *undescribed*

hrtimer_interval
    *undescribed*

hrtimer_active
    *undescribed*

cgrp
    *undescribed*

cgrp_cpuctx_entry
    *undescribed*

sched_cb_entry
    *undescribed*

sched_cb_usage
    *undescribed*

.. This file was automatic generated / don't edit.

