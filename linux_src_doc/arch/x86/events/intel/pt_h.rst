.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/events/intel/pt.h

.. _`pt_buffer`:

struct pt_buffer
================

.. c:type:: struct pt_buffer

    buffer configuration; one buffer per task_struct or cpu, depending on perf event configuration

.. _`pt_buffer.definition`:

Definition
----------

.. code-block:: c

    struct pt_buffer {
        int cpu;
        struct list_head tables;
        struct topa *first, *last, *cur;
        unsigned int cur_idx;
        size_t output_off;
        unsigned long nr_pages;
        local_t data_size;
        local64_t head;
        bool snapshot;
        unsigned long stop_pos, intr_pos;
        void **data_pages;
        struct topa_entry *topa_index[0];
    }

.. _`pt_buffer.members`:

Members
-------

cpu
    cpu for per-cpu allocation

tables
    list of ToPA tables in this buffer

first
    shorthand for first topa table

last
    shorthand for last topa table

cur
    current topa table

cur_idx
    current output region's index within \ ``cur``\  table

output_off
    offset within the current output region

nr_pages
    buffer size in pages

data_size
    running total of the amount of data in this buffer

head
    logical write offset inside the buffer

snapshot
    if this is for a snapshot/overwrite counter

stop_pos
    STOP topa entry in the buffer

intr_pos
    INT topa entry in the buffer

data_pages
    array of pages from perf

topa_index
    table of topa entries indexed by page offset

.. _`pt_filter`:

struct pt_filter
================

.. c:type:: struct pt_filter

    IP range filter configuration

.. _`pt_filter.definition`:

Definition
----------

.. code-block:: c

    struct pt_filter {
        unsigned long msr_a;
        unsigned long msr_b;
        unsigned long config;
    }

.. _`pt_filter.members`:

Members
-------

msr_a
    range start, goes to RTIT_ADDRn_A

msr_b
    range end, goes to RTIT_ADDRn_B

config
    4-bit field in RTIT_CTL

.. _`pt_filters`:

struct pt_filters
=================

.. c:type:: struct pt_filters

    IP range filtering context

.. _`pt_filters.definition`:

Definition
----------

.. code-block:: c

    struct pt_filters {
        struct pt_filter filter[PT_FILTERS_NUM];
        unsigned int nr_filters;
    }

.. _`pt_filters.members`:

Members
-------

filter
    filters defined for this context

nr_filters
    number of defined filters in the \ ``filter``\  array

.. _`pt`:

struct pt
=========

.. c:type:: struct pt

    per-cpu pt context

.. _`pt.definition`:

Definition
----------

.. code-block:: c

    struct pt {
        struct perf_output_handle handle;
        struct pt_filters filters;
        int handle_nmi;
        int vmx_on;
    }

.. _`pt.members`:

Members
-------

handle
    perf output handle

filters
    last configured filters

handle_nmi
    do handle PT PMI on this cpu, there's an active event

vmx_on
    1 if VMX is ON on this cpu

.. This file was automatic generated / don't edit.

