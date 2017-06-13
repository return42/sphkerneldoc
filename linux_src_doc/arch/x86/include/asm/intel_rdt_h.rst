.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/intel_rdt.h

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
        int closid;
        struct cpumask cpu_mask;
        int flags;
        atomic_t waitcount;
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
        int (*seq_show)(struct kernfs_open_file *of,struct seq_file *sf, void *v);
        ssize_t (*write)(struct kernfs_open_file *of,char *buf, size_t nbytes, loff_t off);
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

seq_show
    Show content of the file

write
    Write to the file

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
        bool enabled;
        bool capable;
        char *name;
        int num_closid;
        int cache_level;
        u32 default_ctrl;
        unsigned int msr_base;
        void (*msr_update)(struct rdt_domain *d, struct msr_param *m,struct rdt_resource *r);
        int data_width;
        struct list_head domains;
        struct rdt_cache cache;
        struct rdt_membw membw;
        struct rftype *info_files;
        int nr_info_files;
        const char *format_str;
        int (*parse_ctrlval)(char *buf, struct rdt_resource *r,struct rdt_domain *d);
    }

.. _`rdt_resource.members`:

Members
-------

enabled
    Is this feature enabled on this machine

capable
    Is this feature available on this machine

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

info_files
    resctrl info files for the resource

nr_info_files
    Number of info files

format_str
    Per resource format string to show domain value

parse_ctrlval
    Per resource function pointer to parse control values

.. This file was automatic generated / don't edit.

