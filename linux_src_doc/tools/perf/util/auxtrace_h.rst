.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/auxtrace.h

.. _`itrace_synth_opts`:

struct itrace_synth_opts
========================

.. c:type:: struct itrace_synth_opts

    AUX area tracing synthesis options.

.. _`itrace_synth_opts.definition`:

Definition
----------

.. code-block:: c

    struct itrace_synth_opts {
        bool set;
        bool inject;
        bool instructions;
        bool branches;
        bool transactions;
        bool ptwrites;
        bool pwr_events;
        bool errors;
        bool dont_decode;
        bool log;
        bool calls;
        bool returns;
        bool callchain;
        bool thread_stack;
        bool last_branch;
        unsigned int callchain_sz;
        unsigned int last_branch_sz;
        unsigned long long period;
        enum itrace_period_type period_type;
        unsigned long initial_skip;
        unsigned long *cpu_bitmap;
    }

.. _`itrace_synth_opts.members`:

Members
-------

set
    indicates whether or not options have been set

inject
    indicates the event (not just the sample) must be fully synthesized
    because 'perf inject' will write it out

instructions
    whether to synthesize 'instructions' events

branches
    whether to synthesize 'branches' events

transactions
    whether to synthesize events for transactions

ptwrites
    whether to synthesize events for ptwrites

pwr_events
    whether to synthesize power events

errors
    whether to synthesize decoder error events

dont_decode
    whether to skip decoding entirely

log
    write a decoding log

calls
    limit branch samples to calls (can be combined with \ ``returns``\ )

returns
    limit branch samples to returns (can be combined with \ ``calls``\ )

callchain
    add callchain to 'instructions' events

thread_stack
    feed branches to the thread_stack

last_branch
    add branch context to 'instruction' events

callchain_sz
    maximum callchain size

last_branch_sz
    branch context size

period
    'instructions' events period

period_type
    'instructions' events period type

initial_skip
    skip N events at the beginning.

cpu_bitmap
    CPUs for which to synthesize events, or NULL for all

.. _`auxtrace_index_entry`:

struct auxtrace_index_entry
===========================

.. c:type:: struct auxtrace_index_entry

    indexes a AUX area tracing event within a perf.data file.

.. _`auxtrace_index_entry.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_index_entry {
        u64 file_offset;
        u64 sz;
    }

.. _`auxtrace_index_entry.members`:

Members
-------

file_offset
    offset within the perf.data file

sz
    size of the event

.. _`auxtrace_index`:

struct auxtrace_index
=====================

.. c:type:: struct auxtrace_index

    index of AUX area tracing events within a perf.data file.

.. _`auxtrace_index.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_index {
        struct list_head list;
        size_t nr;
        struct auxtrace_index_entry entries[PERF_AUXTRACE_INDEX_ENTRY_COUNT];
    }

.. _`auxtrace_index.members`:

Members
-------

list
    linking a number of arrays of entries

nr
    number of entries

entries
    array of entries

.. _`auxtrace`:

struct auxtrace
===============

.. c:type:: struct auxtrace

    session callbacks to allow AUX area data decoding.

.. _`auxtrace.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace {
        int (*process_event)(struct perf_session *session,union perf_event *event,struct perf_sample *sample, struct perf_tool *tool);
        int (*process_auxtrace_event)(struct perf_session *session,union perf_event *event, struct perf_tool *tool);
        int (*flush_events)(struct perf_session *session, struct perf_tool *tool);
        void (*free_events)(struct perf_session *session);
        void (*free)(struct perf_session *session);
    }

.. _`auxtrace.members`:

Members
-------

process_event
    lets the decoder see all session events

process_auxtrace_event
    *undescribed*

flush_events
    process any remaining data

free_events
    free resources associated with event processing

free
    free resources associated with the session

.. _`auxtrace_buffer`:

struct auxtrace_buffer
======================

.. c:type:: struct auxtrace_buffer

    a buffer containing AUX area tracing data.

.. _`auxtrace_buffer.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_buffer {
        struct list_head list;
        size_t size;
        pid_t pid;
        pid_t tid;
        int cpu;
        void *data;
        off_t data_offset;
        void *mmap_addr;
        size_t mmap_size;
        bool data_needs_freeing;
        bool consecutive;
        u64 offset;
        u64 reference;
        u64 buffer_nr;
        size_t use_size;
        void *use_data;
    }

.. _`auxtrace_buffer.members`:

Members
-------

list
    buffers are queued in a list held by struct auxtrace_queue

size
    size of the buffer in bytes

pid
    in per-thread mode, the pid this buffer is associated with

tid
    in per-thread mode, the tid this buffer is associated with

cpu
    in per-cpu mode, the cpu this buffer is associated with

data
    actual buffer data (can be null if the data has not been loaded)

data_offset
    file offset at which the buffer can be read

mmap_addr
    mmap address at which the buffer can be read

mmap_size
    size of the mmap at \ ``mmap_addr``\ 

data_needs_freeing
    \ ``data``\  was malloc'd so free it when it is no longer
    needed

consecutive
    the original data was split up and this buffer is consecutive
    to the previous buffer

offset
    offset as determined by aux_head / aux_tail members of struct
    perf_event_mmap_page

reference
    an implementation-specific reference determined when the data is
    recorded

buffer_nr
    used to number each buffer

use_size
    implementation actually only uses this number of bytes

use_data
    implementation actually only uses data starting at this address

.. _`auxtrace_queue`:

struct auxtrace_queue
=====================

.. c:type:: struct auxtrace_queue

    a queue of AUX area tracing data buffers.

.. _`auxtrace_queue.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_queue {
        struct list_head head;
        pid_t tid;
        int cpu;
        bool set;
        void *priv;
    }

.. _`auxtrace_queue.members`:

Members
-------

head
    head of buffer list

tid
    in per-thread mode, the tid this queue is associated with

cpu
    in per-cpu mode, the cpu this queue is associated with

set
    \ ``true``\  once this queue has been dedicated to a specific thread or cpu

priv
    implementation-specific data

.. _`auxtrace_queues`:

struct auxtrace_queues
======================

.. c:type:: struct auxtrace_queues

    an array of AUX area tracing queues.

.. _`auxtrace_queues.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_queues {
        struct auxtrace_queue *queue_array;
        unsigned int nr_queues;
        bool new_data;
        bool populated;
        u64 next_buffer_nr;
    }

.. _`auxtrace_queues.members`:

Members
-------

queue_array
    array of queues

nr_queues
    number of queues

new_data
    set whenever new data is queued

populated
    queues have been fully populated using the auxtrace_index

next_buffer_nr
    used to number each buffer

.. _`auxtrace_heap_item`:

struct auxtrace_heap_item
=========================

.. c:type:: struct auxtrace_heap_item

    element of struct auxtrace_heap.

.. _`auxtrace_heap_item.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_heap_item {
        unsigned int queue_nr;
        u64 ordinal;
    }

.. _`auxtrace_heap_item.members`:

Members
-------

queue_nr
    queue number

ordinal
    value used for sorting (lowest ordinal is top of the heap) expected
    to be a timestamp

.. _`auxtrace_heap`:

struct auxtrace_heap
====================

.. c:type:: struct auxtrace_heap

    a heap suitable for sorting AUX area tracing queues.

.. _`auxtrace_heap.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_heap {
        struct auxtrace_heap_item *heap_array;
        unsigned int heap_cnt;
        unsigned int heap_sz;
    }

.. _`auxtrace_heap.members`:

Members
-------

heap_array
    the heap

heap_cnt
    the number of elements in the heap

heap_sz
    maximum number of elements (grows as needed)

.. _`auxtrace_mmap`:

struct auxtrace_mmap
====================

.. c:type:: struct auxtrace_mmap

    records an mmap of the auxtrace buffer.

.. _`auxtrace_mmap.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_mmap {
        void *base;
        void *userpg;
        size_t mask;
        size_t len;
        u64 prev;
        int idx;
        pid_t tid;
        int cpu;
    }

.. _`auxtrace_mmap.members`:

Members
-------

base
    address of mapped area

userpg
    pointer to buffer's perf_event_mmap_page

mask
    \ ``0``\  if \ ``len``\  is not a power of two, otherwise (@len - \ ``1``\ )

len
    size of mapped area

prev
    previous aux_head

idx
    index of this mmap

tid
    tid for a per-thread mmap (also set if there is only 1 tid on a per-cpu
    mmap) otherwise \ ``0``\ 

cpu
    cpu number for a per-cpu mmap otherwise \ ``-1``\ 

.. _`auxtrace_mmap_params`:

struct auxtrace_mmap_params
===========================

.. c:type:: struct auxtrace_mmap_params

    parameters to set up struct auxtrace_mmap.

.. _`auxtrace_mmap_params.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_mmap_params {
        size_t mask;
        off_t offset;
        size_t len;
        int prot;
        int idx;
        pid_t tid;
        int cpu;
    }

.. _`auxtrace_mmap_params.members`:

Members
-------

mask
    \ ``0``\  if \ ``len``\  is not a power of two, otherwise (@len - \ ``1``\ )

offset
    file offset of mapped area

len
    size of mapped area

prot
    mmap memory protection

idx
    index of this mmap

tid
    tid for a per-thread mmap (also set if there is only 1 tid on a per-cpu
    mmap) otherwise \ ``0``\ 

cpu
    cpu number for a per-cpu mmap otherwise \ ``-1``\ 

.. _`auxtrace_record`:

struct auxtrace_record
======================

.. c:type:: struct auxtrace_record

    callbacks for recording AUX area data.

.. _`auxtrace_record.definition`:

Definition
----------

.. code-block:: c

    struct auxtrace_record {
        int (*recording_options)(struct auxtrace_record *itr,struct perf_evlist *evlist, struct record_opts *opts);
        size_t (*info_priv_size)(struct auxtrace_record *itr, struct perf_evlist *evlist);
        int (*info_fill)(struct auxtrace_record *itr,struct perf_session *session,struct auxtrace_info_event *auxtrace_info, size_t priv_size);
        void (*free)(struct auxtrace_record *itr);
        int (*snapshot_start)(struct auxtrace_record *itr);
        int (*snapshot_finish)(struct auxtrace_record *itr);
        int (*find_snapshot)(struct auxtrace_record *itr, int idx,struct auxtrace_mmap *mm, unsigned char *data, u64 *head, u64 *old);
        int (*parse_snapshot_options)(struct auxtrace_record *itr,struct record_opts *opts, const char *str);
        u64 (*reference)(struct auxtrace_record *itr);
        int (*read_finish)(struct auxtrace_record *itr, int idx);
        unsigned int alignment;
    }

.. _`auxtrace_record.members`:

Members
-------

recording_options
    validate and process recording options

info_priv_size
    return the size of the private data in auxtrace_info_event

info_fill
    fill-in the private data in auxtrace_info_event

free
    free this auxtrace record structure

snapshot_start
    starting a snapshot

snapshot_finish
    finishing a snapshot

find_snapshot
    find data to snapshot within auxtrace mmap

parse_snapshot_options
    parse snapshot options

reference
    provide a 64-bit reference number for auxtrace_event

read_finish
    called after reading from an auxtrace mmap

alignment
    *undescribed*

.. _`addr_filter`:

struct addr_filter
==================

.. c:type:: struct addr_filter

    address filter.

.. _`addr_filter.definition`:

Definition
----------

.. code-block:: c

    struct addr_filter {
        struct list_head list;
        bool range;
        bool start;
        const char *action;
        const char *sym_from;
        const char *sym_to;
        int sym_from_idx;
        int sym_to_idx;
        u64 addr;
        u64 size;
        const char *filename;
        char *str;
    }

.. _`addr_filter.members`:

Members
-------

list
    list node

range
    true if it is a range filter

start
    true if action is 'filter' or 'start'

action
    'filter', 'start' or 'stop' ('tracestop' is accepted but converted
    to 'stop')

sym_from
    symbol name for the filter address

sym_to
    symbol name that determines the filter size

sym_from_idx
    selects n'th from symbols with the same name (0 means global
    and less than 0 means symbol must be unique)

sym_to_idx
    same as \ ``sym_from_idx``\  but for \ ``sym_to``\ 

addr
    filter address

size
    filter region size (for range filters)

filename
    DSO file name or NULL for the kernel

str
    allocated string that contains the other string members

.. _`addr_filters`:

struct addr_filters
===================

.. c:type:: struct addr_filters

    list of address filters.

.. _`addr_filters.definition`:

Definition
----------

.. code-block:: c

    struct addr_filters {
        struct list_head head;
        int cnt;
    }

.. _`addr_filters.members`:

Members
-------

head
    list of address filters

cnt
    number of address filters

.. This file was automatic generated / don't edit.

