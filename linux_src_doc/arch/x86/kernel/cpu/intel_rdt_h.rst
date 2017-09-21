.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/cpu/intel_rdt.h

.. _`mon_evt`:

struct mon_evt
==============

.. c:type:: struct mon_evt

    Entry in the event list of a resource

.. _`mon_evt.definition`:

Definition
----------

.. code-block:: c

    struct mon_evt {
        u32 evtid;
        char *name;
        struct list_head list;
    }

.. _`mon_evt.members`:

Members
-------

evtid
    event id

name
    name of the event

list
    *undescribed*

.. _`mongroup`:

struct mongroup
===============

.. c:type:: struct mongroup

    store mon group's data in resctrl fs. \ ``mon_data_kn``\          kernlfs node for the mon_data directory

.. _`mongroup.definition`:

Definition
----------

.. code-block:: c

    struct mongroup {
        struct kernfs_node *mon_data_kn;
        struct rdtgroup *parent;
        struct list_head crdtgrp_list;
        u32 rmid;
    }

.. _`mongroup.members`:

Members
-------

mon_data_kn
    *undescribed*

parent
    parent rdtgrp

crdtgrp_list
    child rdtgroup node list

rmid
    rmid for this rdtgroup

.. _`rdtgroup`:

struct rdtgroup
===============

.. c:type:: struct rdtgroup

    store rdtgroup's data in resctrl file system.

.. _`rdtgroup.definition`:

Definition
----------

.. code-block:: c

    struct rdtgroup {
        struct kernfs_node *kn;
        struct list_head rdtgroup_list;
        u32 closid;
        struct cpumask cpu_mask;
        int flags;
        atomic_t waitcount;
        enum rdt_group_type type;
        struct mongroup mon;
    }

.. _`rdtgroup.members`:

Members
-------

kn
    kernfs node

rdtgroup_list
    linked list for all rdtgroups

closid
    closid for this rdtgroup

cpu_mask
    CPUs assigned to this rdtgroup

flags
    status bits

waitcount
    how many cpus expect to find this
    group when they acquire rdtgroup_mutex

type
    indicates type of this rdtgroup - either
    monitor only or ctrl_mon group

mon
    mongroup related data

.. _`rftype`:

struct rftype
=============

.. c:type:: struct rftype

    describe each file in the resctrl file system

.. _`rftype.definition`:

Definition
----------

.. code-block:: c

    struct rftype {
        char *name;
        umode_t mode;
        struct kernfs_ops *kf_ops;
        unsigned long flags;
        unsigned long fflags;
        int (*seq_show)(struct kernfs_open_file *of, struct seq_file *sf, void *v);
        ssize_t (*write)(struct kernfs_open_file *of, char *buf, size_t nbytes, loff_t off);
    }

.. _`rftype.members`:

Members
-------

name
    File name

mode
    Access mode

kf_ops
    File operations

flags
    File specific RFTYPE_FLAGS\_\* flags

fflags
    File specific RF\_\* or RFTYPE\_\* flags

seq_show
    Show content of the file

write
    Write to the file

.. _`mbm_state`:

struct mbm_state
================

.. c:type:: struct mbm_state

    status for each MBM counter in each domain

.. _`mbm_state.definition`:

Definition
----------

.. code-block:: c

    struct mbm_state {
        u64 chunks;
        u64 prev_msr;
    }

.. _`mbm_state.members`:

Members
-------

chunks
    Total data moved (multiply by rdt_group.mon_scale to get bytes)
    \ ``prev_msr``\     Value of IA32_QM_CTR for this RMID last time we read it

prev_msr
    *undescribed*

.. _`rdt_domain`:

struct rdt_domain
=================

.. c:type:: struct rdt_domain

    group of cpus sharing an RDT resource

.. _`rdt_domain.definition`:

Definition
----------

.. code-block:: c

    struct rdt_domain {
        struct list_head list;
        int id;
        struct cpumask cpu_mask;
        unsigned long *rmid_busy_llc;
        struct mbm_state *mbm_total;
        struct mbm_state *mbm_local;
        struct delayed_work mbm_over;
        struct delayed_work cqm_limbo;
        int mbm_work_cpu;
        int cqm_work_cpu;
        u32 *ctrl_val;
        u32 new_ctrl;
        bool have_new_ctrl;
    }

.. _`rdt_domain.members`:

Members
-------

list
    all instances of this resource

id
    unique id for this instance

cpu_mask
    which cpus share this resource

rmid_busy_llc
    bitmap of which limbo RMIDs are above threshold

mbm_total
    saved state for MBM total bandwidth

mbm_local
    saved state for MBM local bandwidth

mbm_over
    worker to periodically read MBM h/w counters

cqm_limbo
    worker to periodically read CQM h/w counters

mbm_work_cpu
    worker cpu for MBM h/w counters

cqm_work_cpu
    worker cpu for CQM h/w counters

ctrl_val
    array of cache or mem ctrl values (indexed by CLOSID)

new_ctrl
    new ctrl value to be loaded

have_new_ctrl
    did user provide new_ctrl for this domain

.. _`msr_param`:

struct msr_param
================

.. c:type:: struct msr_param

    set a range of MSRs from a domain

.. _`msr_param.definition`:

Definition
----------

.. code-block:: c

    struct msr_param {
        struct rdt_resource *res;
        int low;
        int high;
    }

.. _`msr_param.members`:

Members
-------

res
    The resource to use

low
    Beginning index from base MSR

high
    End index

.. _`rdt_cache`:

struct rdt_cache
================

.. c:type:: struct rdt_cache

    Cache allocation related data

.. _`rdt_cache.definition`:

Definition
----------

.. code-block:: c

    struct rdt_cache {
        unsigned int cbm_len;
        unsigned int min_cbm_bits;
        unsigned int cbm_idx_mult;
        unsigned int cbm_idx_offset;
        unsigned int shareable_bits;
    }

.. _`rdt_cache.members`:

Members
-------

cbm_len
    Length of the cache bit mask

min_cbm_bits
    Minimum number of consecutive bits to be set

cbm_idx_mult
    Multiplier of CBM index

cbm_idx_offset
    Offset of CBM index. CBM index is computed by:
    closid \* cbm_idx_multi + cbm_idx_offset
    in a cache bit mask

shareable_bits
    Bitmask of shareable resource with other
    executing entities

.. _`rdt_membw`:

struct rdt_membw
================

.. c:type:: struct rdt_membw

    Memory bandwidth allocation related data

.. _`rdt_membw.definition`:

Definition
----------

.. code-block:: c

    struct rdt_membw {
        u32 max_delay;
        u32 min_bw;
        u32 bw_gran;
        u32 delay_linear;
        u32 *mb_map;
    }

.. _`rdt_membw.members`:

Members
-------

max_delay
    Max throttle delay. Delay is the hardware
    representation for memory bandwidth.

min_bw
    Minimum memory bandwidth percentage user can request

bw_gran
    Granularity at which the memory bandwidth is allocated

delay_linear
    True if memory B/W delay is in linear scale

mb_map
    Mapping of memory B/W percentage to memory B/W delay

.. _`rdt_resource`:

struct rdt_resource
===================

.. c:type:: struct rdt_resource

    attributes of an RDT resource

.. _`rdt_resource.definition`:

Definition
----------

.. code-block:: c

    struct rdt_resource {
        int rid;
        bool alloc_enabled;
        bool mon_enabled;
        bool alloc_capable;
        bool mon_capable;
        char *name;
        int num_closid;
        int cache_level;
        u32 default_ctrl;
        unsigned int msr_base;
        void (*msr_update)(struct rdt_domain *d, struct msr_param *m, struct rdt_resource *r);
        int data_width;
        struct list_head domains;
        struct rdt_cache cache;
        struct rdt_membw membw;
        const char *format_str;
        int (*parse_ctrlval)(char *buf, struct rdt_resource *r, struct rdt_domain *d);
        struct list_head evt_list;
        int num_rmid;
        unsigned int mon_scale;
        unsigned long fflags;
    }

.. _`rdt_resource.members`:

Members
-------

rid
    The index of the resource

alloc_enabled
    Is allocation enabled on this machine

mon_enabled
    Is monitoring enabled for this feature

alloc_capable
    Is allocation available on this machine

mon_capable
    Is monitor feature available on this machine

name
    Name to use in "schemata" file

num_closid
    Number of CLOSIDs available

cache_level
    Which cache level defines scope of this resource

default_ctrl
    Specifies default cache cbm or memory B/W percent.

msr_base
    Base MSR address for CBMs

msr_update
    Function pointer to update QOS MSRs

data_width
    Character width of data when displaying

domains
    All domains for this resource

cache
    Cache allocation related data

membw
    *undescribed*

format_str
    Per resource format string to show domain value

parse_ctrlval
    Per resource function pointer to parse control values

evt_list
    List of monitoring events

num_rmid
    Number of RMIDs available

mon_scale
    cqm counter \* mon_scale = occupancy in bytes

fflags
    flags to choose base and info files

.. This file was automatic generated / don't edit.

