.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/events/intel/pt.c

.. _`topa`:

struct topa
===========

.. c:type:: struct topa

    page-sized ToPA table with metadata at the top

.. _`topa.definition`:

Definition
----------

.. code-block:: c

    struct topa {
        struct topa_entry table[TENTS_PER_PAGE];
        struct list_head list;
        u64 phys;
        u64 offset;
        size_t size;
        int last;
    }

.. _`topa.members`:

Members
-------

table
    actual ToPA table entries, as understood by PT hardware

list
    linkage to struct pt_buffer's list of tables

phys
    physical address of this page

offset
    offset of the first entry in this table in the buffer

size
    total size of all entries in this table

last
    index of the last initialized entry in this table

.. _`topa_alloc`:

topa_alloc
==========

.. c:function:: struct topa *topa_alloc(int cpu, gfp_t gfp)

    allocate page-sized ToPA table

    :param cpu:
        CPU on which to allocate.
    :type cpu: int

    :param gfp:
        Allocation flags.
    :type gfp: gfp_t

.. _`topa_alloc.return`:

Return
------

On success, return the pointer to ToPA table page.

.. _`topa_free`:

topa_free
=========

.. c:function:: void topa_free(struct topa *topa)

    free a page-sized ToPA table

    :param topa:
        Table to deallocate.
    :type topa: struct topa \*

.. _`topa_insert_table`:

topa_insert_table
=================

.. c:function:: void topa_insert_table(struct pt_buffer *buf, struct topa *topa)

    insert a ToPA table into a buffer

    :param buf:
        PT buffer that's being extended.
    :type buf: struct pt_buffer \*

    :param topa:
        New topa table to be inserted.
    :type topa: struct topa \*

.. _`topa_insert_table.description`:

Description
-----------

If it's the first table in this buffer, set up buffer's pointers
accordingly; otherwise, add a END=1 link entry to \ ``topa``\  to the current
"last" table and adjust the last table pointer to \ ``topa``\ .

.. _`topa_table_full`:

topa_table_full
===============

.. c:function:: bool topa_table_full(struct topa *topa)

    check if a ToPA table is filled up

    :param topa:
        ToPA table.
    :type topa: struct topa \*

.. _`topa_insert_pages`:

topa_insert_pages
=================

.. c:function:: int topa_insert_pages(struct pt_buffer *buf, gfp_t gfp)

    create a list of ToPA tables

    :param buf:
        PT buffer being initialized.
    :type buf: struct pt_buffer \*

    :param gfp:
        Allocation flags.
    :type gfp: gfp_t

.. _`topa_insert_pages.description`:

Description
-----------

This initializes a list of ToPA tables with entries from
the data_pages provided by \ :c:func:`rb_alloc_aux`\ .

.. _`topa_insert_pages.return`:

Return
------

0 on success or error code.

.. _`pt_topa_dump`:

pt_topa_dump
============

.. c:function:: void pt_topa_dump(struct pt_buffer *buf)

    print ToPA tables and their entries

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

.. _`pt_buffer_advance`:

pt_buffer_advance
=================

.. c:function:: void pt_buffer_advance(struct pt_buffer *buf)

    advance to the next output region

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

.. _`pt_buffer_advance.description`:

Description
-----------

Advance the current pointers in the buffer to the next ToPA entry.

.. _`pt_update_head`:

pt_update_head
==============

.. c:function:: void pt_update_head(struct pt *pt)

    calculate current offsets and sizes

    :param pt:
        Per-cpu pt context.
    :type pt: struct pt \*

.. _`pt_update_head.description`:

Description
-----------

Update buffer's current write pointer position and data size.

.. _`pt_buffer_region`:

pt_buffer_region
================

.. c:function:: void *pt_buffer_region(struct pt_buffer *buf)

    obtain current output region's address

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

.. _`pt_buffer_region_size`:

pt_buffer_region_size
=====================

.. c:function:: size_t pt_buffer_region_size(struct pt_buffer *buf)

    obtain current output region's size

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

.. _`pt_handle_status`:

pt_handle_status
================

.. c:function:: void pt_handle_status(struct pt *pt)

    take care of possible status conditions

    :param pt:
        Per-cpu pt context.
    :type pt: struct pt \*

.. _`pt_read_offset`:

pt_read_offset
==============

.. c:function:: void pt_read_offset(struct pt_buffer *buf)

    translate registers into buffer pointers

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

.. _`pt_read_offset.description`:

Description
-----------

Set buffer's output pointers from MSR values.

.. _`pt_topa_next_entry`:

pt_topa_next_entry
==================

.. c:function:: unsigned int pt_topa_next_entry(struct pt_buffer *buf, unsigned int pg)

    obtain index of the first page in the next ToPA entry

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

    :param pg:
        Page offset in the buffer.
    :type pg: unsigned int

.. _`pt_topa_next_entry.description`:

Description
-----------

When advancing to the next output region (ToPA entry), given a page offset
into the buffer, we need to find the offset of the first page in the next
region.

.. _`pt_buffer_reset_markers`:

pt_buffer_reset_markers
=======================

.. c:function:: int pt_buffer_reset_markers(struct pt_buffer *buf, struct perf_output_handle *handle)

    place interrupt and stop bits in the buffer

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

    :param handle:
        Current output handle.
    :type handle: struct perf_output_handle \*

.. _`pt_buffer_reset_markers.description`:

Description
-----------

Place INT and STOP marks to prevent overwriting old data that the consumer
hasn't yet collected and waking up the consumer after a certain fraction of
the buffer has filled up. Only needed and sensible for non-snapshot counters.

This obviously relies on buf::head to figure out buffer markers, so it has
to be called after \ :c:func:`pt_buffer_reset_offsets`\  and before the hardware tracing
is enabled.

.. _`pt_buffer_setup_topa_index`:

pt_buffer_setup_topa_index
==========================

.. c:function:: void pt_buffer_setup_topa_index(struct pt_buffer *buf)

    build topa_index[] table of regions

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

.. _`pt_buffer_setup_topa_index.description`:

Description
-----------

topa_index[] references output regions indexed by offset into the
buffer for purposes of quick reverse lookup.

.. _`pt_buffer_reset_offsets`:

pt_buffer_reset_offsets
=======================

.. c:function:: void pt_buffer_reset_offsets(struct pt_buffer *buf, unsigned long head)

    adjust buffer's write pointers from aux_head

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

    :param head:
        Write pointer (aux_head) from AUX buffer.
    :type head: unsigned long

.. _`pt_buffer_reset_offsets.description`:

Description
-----------

Find the ToPA table and entry corresponding to given \ ``head``\  and set buffer's
"current" pointers accordingly. This is done after we have obtained the
current aux_head position from a successful call to \ :c:func:`perf_aux_output_begin`\ 
to make sure the hardware is writing to the right place.

This function modifies buf::{cur,cur_idx,output_off} that will be programmed
into PT msrs when the tracing is enabled and buf::head and buf::data_size,
which are used to determine INT and STOP markers' locations by a subsequent
call to \ :c:func:`pt_buffer_reset_markers`\ .

.. _`pt_buffer_fini_topa`:

pt_buffer_fini_topa
===================

.. c:function:: void pt_buffer_fini_topa(struct pt_buffer *buf)

    deallocate ToPA structure of a buffer

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

.. _`pt_buffer_init_topa`:

pt_buffer_init_topa
===================

.. c:function:: int pt_buffer_init_topa(struct pt_buffer *buf, unsigned long nr_pages, gfp_t gfp)

    initialize ToPA table for pt buffer

    :param buf:
        PT buffer.
    :type buf: struct pt_buffer \*

    :param nr_pages:
        *undescribed*
    :type nr_pages: unsigned long

    :param gfp:
        Allocation flags.
    :type gfp: gfp_t

.. _`pt_buffer_setup_aux`:

pt_buffer_setup_aux
===================

.. c:function:: void *pt_buffer_setup_aux(int cpu, void **pages, int nr_pages, bool snapshot)

    set up topa tables for a PT buffer

    :param cpu:
        Cpu on which to allocate, -1 means current.
    :type cpu: int

    :param pages:
        Array of pointers to buffer pages passed from perf core.
    :type pages: void \*\*

    :param nr_pages:
        Number of pages in the buffer.
    :type nr_pages: int

    :param snapshot:
        If this is a snapshot/overwrite counter.
    :type snapshot: bool

.. _`pt_buffer_setup_aux.description`:

Description
-----------

This is a pmu::setup_aux callback that sets up ToPA tables and all the
bookkeeping for an AUX buffer.

.. _`pt_buffer_setup_aux.return`:

Return
------

Our private PT buffer structure.

.. _`pt_buffer_free_aux`:

pt_buffer_free_aux
==================

.. c:function:: void pt_buffer_free_aux(void *data)

    perf AUX deallocation path callback

    :param data:
        PT buffer.
    :type data: void \*

.. _`intel_pt_interrupt`:

intel_pt_interrupt
==================

.. c:function:: void intel_pt_interrupt( void)

    PT PMI handler

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

