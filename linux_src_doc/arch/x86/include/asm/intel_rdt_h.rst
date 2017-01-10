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
        int (*seq_show)(struct kernfs_open_file *of,struct seq_file *sf, void *v);
        ssize_t (*write)(struct kernfs_open_file *of,char *buf, size_t nbytes, loff_t off);
    }

.. _`rftype.members`:

Members
-------

name
    file name

mode
    access mode

kf_ops
    operations

seq_show
    show content of the file

write
    write to the file

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
        int cbm_len;
        int min_cbm_bits;
        u32 max_cbm;
        struct list_head domains;
        int num_domains;
        int msr_base;
        u32 *tmp_cbms;
        int num_tmp_cbms;
        int cache_level;
        int cbm_idx_multi;
        int cbm_idx_offset;
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

cbm_len
    *undescribed*

min_cbm_bits
    Minimum number of consecutive bits to be set
    in a cache bit mask

max_cbm
    Largest Cache Bit Mask allowed

domains
    All domains for this resource

num_domains
    Number of domains active

msr_base
    Base MSR address for CBMs

tmp_cbms
    Scratch space when updating schemata

num_tmp_cbms
    Number of CBMs in tmp_cbms

cache_level
    Which cache level defines scope of this domain

cbm_idx_multi
    Multiplier of CBM index

cbm_idx_offset
    Offset of CBM index. CBM index is computed by:
    closid \* cbm_idx_multi + cbm_idx_offset

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
        u32 *cbm;
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

cbm
    array of cache bit masks (indexed by CLOSID)

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

.. This file was automatic generated / don't edit.

