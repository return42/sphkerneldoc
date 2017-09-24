.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/sort.h

.. _`hist_entry`:

struct hist_entry
=================

.. c:type:: struct hist_entry

    histogram entry

.. _`hist_entry.definition`:

Definition
----------

.. code-block:: c

    struct hist_entry {
        struct rb_node rb_node_in;
        struct rb_node rb_node;
        union pairs;
        struct he_stat stat;
        struct he_stat *stat_acc;
        struct map_symbol ms;
        struct thread *thread;
        struct comm *comm;
        struct namespace_id cgroup_id;
        u64 ip;
        u64 transaction;
        s32 socket;
        s32 cpu;
        u8 cpumode;
        u8 depth;
        bool dummy;
        bool leaf;
        char level;
        u8 filtered;
        union {unnamed_union};
        char *srcline;
        char *srcfile;
        struct inline_node *inline_node;
        struct symbol *parent;
        struct branch_info *branch_info;
        struct hists *hists;
        struct mem_info *mem_info;
        void *raw_data;
        u32 raw_size;
        void *trace_output;
        struct perf_hpp_list *hpp_list;
        struct hist_entry *parent_he;
        struct hist_entry_ops *ops;
        union {unnamed_union};
        struct callchain_root callchain;
    }

.. _`hist_entry.members`:

Members
-------

rb_node_in
    *undescribed*

rb_node
    *undescribed*

pairs
    *undescribed*

stat
    *undescribed*

stat_acc
    *undescribed*

ms
    *undescribed*

thread
    *undescribed*

comm
    *undescribed*

cgroup_id
    *undescribed*

ip
    *undescribed*

transaction
    *undescribed*

socket
    *undescribed*

cpu
    *undescribed*

cpumode
    *undescribed*

depth
    *undescribed*

dummy
    *undescribed*

leaf
    *undescribed*

level
    *undescribed*

filtered
    *undescribed*

{unnamed_union}
    anonymous


srcline
    *undescribed*

srcfile
    *undescribed*

inline_node
    *undescribed*

parent
    *undescribed*

branch_info
    *undescribed*

hists
    *undescribed*

mem_info
    *undescribed*

raw_data
    *undescribed*

raw_size
    *undescribed*

trace_output
    *undescribed*

hpp_list
    *undescribed*

parent_he
    *undescribed*

ops
    *undescribed*

{unnamed_union}
    anonymous


callchain
    *undescribed*

.. _`hist_entry.description`:

Description
-----------

@row_offset - offset from the first callchain expanded to appear on screen
\ ``nr_rows``\  - rows expanded in callchain, recalculated on folding/unfolding

.. This file was automatic generated / don't edit.

