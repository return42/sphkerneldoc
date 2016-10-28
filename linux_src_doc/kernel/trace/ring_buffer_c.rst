.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/ring_buffer.c

.. _`ring_buffer_event_length`:

ring_buffer_event_length
========================

.. c:function:: unsigned ring_buffer_event_length(struct ring_buffer_event *event)

    return the length of the event

    :param struct ring_buffer_event \*event:
        the event to get the length of

.. _`ring_buffer_event_length.description`:

Description
-----------

Returns the size of the data load of a data event.
If the event is something other than a data event, it
returns the size of the event itself. With the exception
of a TIME EXTEND, where it still returns the size of the
data load of the data event after it.

.. _`ring_buffer_event_data`:

ring_buffer_event_data
======================

.. c:function:: void *ring_buffer_event_data(struct ring_buffer_event *event)

    return the data of the event

    :param struct ring_buffer_event \*event:
        the event to get the data from

.. _`ring_buffer_page_len`:

ring_buffer_page_len
====================

.. c:function:: size_t ring_buffer_page_len(void *page)

    the size of data on the page.

    :param void \*page:
        The page to read

.. _`ring_buffer_page_len.description`:

Description
-----------

Returns the amount of data on the page, including buffer page header.

.. _`ring_buffer_wait`:

ring_buffer_wait
================

.. c:function:: int ring_buffer_wait(struct ring_buffer *buffer, int cpu, bool full)

    wait for input to the ring buffer

    :param struct ring_buffer \*buffer:
        buffer to wait on

    :param int cpu:
        the cpu buffer to wait on

    :param bool full:
        wait until a full page is available, if \ ``cpu``\  != RING_BUFFER_ALL_CPUS

.. _`ring_buffer_wait.description`:

Description
-----------

If \ ``cpu``\  == RING_BUFFER_ALL_CPUS then the task will wake up as soon
as data is added to any of the \ ``buffer``\ 's cpu buffers. Otherwise
it will wait for data to be added to a specific cpu buffer.

.. _`ring_buffer_poll_wait`:

ring_buffer_poll_wait
=====================

.. c:function:: int ring_buffer_poll_wait(struct ring_buffer *buffer, int cpu, struct file *filp, poll_table *poll_table)

    poll on buffer input

    :param struct ring_buffer \*buffer:
        buffer to wait on

    :param int cpu:
        the cpu buffer to wait on

    :param struct file \*filp:
        the file descriptor

    :param poll_table \*poll_table:
        The poll descriptor

.. _`ring_buffer_poll_wait.description`:

Description
-----------

If \ ``cpu``\  == RING_BUFFER_ALL_CPUS then the task will wake up as soon
as data is added to any of the \ ``buffer``\ 's cpu buffers. Otherwise
it will wait for data to be added to a specific cpu buffer.

Returns POLLIN \| POLLRDNORM if data exists in the buffers,
zero otherwise.

.. _`rb_check_list`:

rb_check_list
=============

.. c:function:: int rb_check_list(struct ring_buffer_per_cpu *cpu_buffer, struct list_head *list)

    make sure a pointer to a list has the last bits zero

    :param struct ring_buffer_per_cpu \*cpu_buffer:
        *undescribed*

    :param struct list_head \*list:
        *undescribed*

.. _`rb_check_pages`:

rb_check_pages
==============

.. c:function:: int rb_check_pages(struct ring_buffer_per_cpu *cpu_buffer)

    integrity check of buffer pages

    :param struct ring_buffer_per_cpu \*cpu_buffer:
        CPU buffer with pages to test

.. _`rb_check_pages.description`:

Description
-----------

As a safety measure we check to make sure the data pages have not
been corrupted.

.. _`__ring_buffer_alloc`:

__ring_buffer_alloc
===================

.. c:function:: struct ring_buffer *__ring_buffer_alloc(unsigned long size, unsigned flags, struct lock_class_key *key)

    allocate a new ring_buffer

    :param unsigned long size:
        the size in bytes per cpu that is needed.

    :param unsigned flags:
        attributes to set for the ring buffer.

    :param struct lock_class_key \*key:
        *undescribed*

.. _`__ring_buffer_alloc.description`:

Description
-----------

Currently the only flag that is available is the RB_FL_OVERWRITE
flag. This flag means that the buffer will overwrite old data
when the buffer wraps. If this flag is not set, the buffer will
drop data when the tail hits the head.

.. _`ring_buffer_free`:

ring_buffer_free
================

.. c:function:: void ring_buffer_free(struct ring_buffer *buffer)

    free a ring buffer.

    :param struct ring_buffer \*buffer:
        the buffer to free.

.. _`ring_buffer_resize`:

ring_buffer_resize
==================

.. c:function:: int ring_buffer_resize(struct ring_buffer *buffer, unsigned long size, int cpu_id)

    resize the ring buffer

    :param struct ring_buffer \*buffer:
        the buffer to resize.

    :param unsigned long size:
        the new size.

    :param int cpu_id:
        the cpu buffer to resize

.. _`ring_buffer_resize.description`:

Description
-----------

Minimum size is 2 \* BUF_PAGE_SIZE.

Returns 0 on success and < 0 on failure.

.. _`rb_update_event`:

rb_update_event
===============

.. c:function:: void rb_update_event(struct ring_buffer_per_cpu *cpu_buffer, struct ring_buffer_event *event, struct rb_event_info *info)

    update event type and data

    :param struct ring_buffer_per_cpu \*cpu_buffer:
        *undescribed*

    :param struct ring_buffer_event \*event:
        the event to update

    :param struct rb_event_info \*info:
        *undescribed*

.. _`rb_update_event.description`:

Description
-----------

Update the type and data fields of the event. The length
is the actual size that is written to the ring buffer,
and with this, we can determine what to place into the
data field.

.. _`ring_buffer_unlock_commit`:

ring_buffer_unlock_commit
=========================

.. c:function:: int ring_buffer_unlock_commit(struct ring_buffer *buffer, struct ring_buffer_event *event)

    commit a reserved

    :param struct ring_buffer \*buffer:
        The buffer to commit to

    :param struct ring_buffer_event \*event:
        The event pointer to commit.

.. _`ring_buffer_unlock_commit.description`:

Description
-----------

This commits the data to the ring buffer, and releases any locks held.

Must be paired with ring_buffer_lock_reserve.

.. _`ring_buffer_lock_reserve`:

ring_buffer_lock_reserve
========================

.. c:function:: struct ring_buffer_event *ring_buffer_lock_reserve(struct ring_buffer *buffer, unsigned long length)

    reserve a part of the buffer

    :param struct ring_buffer \*buffer:
        the ring buffer to reserve from

    :param unsigned long length:
        the length of the data to reserve (excluding event header)

.. _`ring_buffer_lock_reserve.description`:

Description
-----------

Returns a reseverd event on the ring buffer to copy directly to.
The user of this interface will need to get the body to write into
and can use the \ :c:func:`ring_buffer_event_data`\  interface.

The length is the length of the data needed, not the event length
which also includes the event header.

Must be paired with ring_buffer_unlock_commit, unless NULL is returned.
If NULL is returned, then nothing has been allocated or locked.

.. _`ring_buffer_discard_commit`:

ring_buffer_discard_commit
==========================

.. c:function:: void ring_buffer_discard_commit(struct ring_buffer *buffer, struct ring_buffer_event *event)

    discard an event that has not been committed

    :param struct ring_buffer \*buffer:
        the ring buffer

    :param struct ring_buffer_event \*event:
        non committed event to discard

.. _`ring_buffer_discard_commit.description`:

Description
-----------

Sometimes an event that is in the ring buffer needs to be ignored.
This function lets the user discard an event in the ring buffer
and then that event will not be read later.

This function only works if it is called before the the item has been
committed. It will try to free the event from the ring buffer
if another event has not been added behind it.

If another event has been added behind it, it will set the event
up as discarded, and perform the commit.

If this function is called, do not call ring_buffer_unlock_commit on
the event.

.. _`ring_buffer_write`:

ring_buffer_write
=================

.. c:function:: int ring_buffer_write(struct ring_buffer *buffer, unsigned long length, void *data)

    write data to the buffer without reserving

    :param struct ring_buffer \*buffer:
        The ring buffer to write to.

    :param unsigned long length:
        The length of the data being written (excluding the event header)

    :param void \*data:
        The data to write to the buffer.

.. _`ring_buffer_write.description`:

Description
-----------

This is like ring_buffer_lock_reserve and ring_buffer_unlock_commit as
one function. If you already have the data to write to the buffer, it
may be easier to simply call this function.

Note, like ring_buffer_lock_reserve, the length is the length of the data
and not the length of the event which would hold the header.

.. _`ring_buffer_record_disable`:

ring_buffer_record_disable
==========================

.. c:function:: void ring_buffer_record_disable(struct ring_buffer *buffer)

    stop all writes into the buffer

    :param struct ring_buffer \*buffer:
        The ring buffer to stop writes to.

.. _`ring_buffer_record_disable.description`:

Description
-----------

This prevents all writes to the buffer. Any attempt to write
to the buffer after this will fail and return NULL.

The caller should call \ :c:func:`synchronize_sched`\  after this.

.. _`ring_buffer_record_enable`:

ring_buffer_record_enable
=========================

.. c:function:: void ring_buffer_record_enable(struct ring_buffer *buffer)

    enable writes to the buffer

    :param struct ring_buffer \*buffer:
        The ring buffer to enable writes

.. _`ring_buffer_record_enable.description`:

Description
-----------

Note, multiple disables will need the same number of enables
to truly enable the writing (much like preempt_disable).

.. _`ring_buffer_record_off`:

ring_buffer_record_off
======================

.. c:function:: void ring_buffer_record_off(struct ring_buffer *buffer)

    stop all writes into the buffer

    :param struct ring_buffer \*buffer:
        The ring buffer to stop writes to.

.. _`ring_buffer_record_off.description`:

Description
-----------

This prevents all writes to the buffer. Any attempt to write
to the buffer after this will fail and return NULL.

This is different than \ :c:func:`ring_buffer_record_disable`\  as
it works like an on/off switch, where as the \ :c:func:`disable`\  version
must be paired with a \ :c:func:`enable`\ .

.. _`ring_buffer_record_on`:

ring_buffer_record_on
=====================

.. c:function:: void ring_buffer_record_on(struct ring_buffer *buffer)

    restart writes into the buffer

    :param struct ring_buffer \*buffer:
        The ring buffer to start writes to.

.. _`ring_buffer_record_on.description`:

Description
-----------

This enables all writes to the buffer that was disabled by
\ :c:func:`ring_buffer_record_off`\ .

This is different than \ :c:func:`ring_buffer_record_enable`\  as
it works like an on/off switch, where as the \ :c:func:`enable`\  version
must be paired with a \ :c:func:`disable`\ .

.. _`ring_buffer_record_is_on`:

ring_buffer_record_is_on
========================

.. c:function:: int ring_buffer_record_is_on(struct ring_buffer *buffer)

    return true if the ring buffer can write

    :param struct ring_buffer \*buffer:
        The ring buffer to see if write is enabled

.. _`ring_buffer_record_is_on.description`:

Description
-----------

Returns true if the ring buffer is in a state that it accepts writes.

.. _`ring_buffer_record_disable_cpu`:

ring_buffer_record_disable_cpu
==============================

.. c:function:: void ring_buffer_record_disable_cpu(struct ring_buffer *buffer, int cpu)

    stop all writes into the cpu_buffer

    :param struct ring_buffer \*buffer:
        The ring buffer to stop writes to.

    :param int cpu:
        The CPU buffer to stop

.. _`ring_buffer_record_disable_cpu.description`:

Description
-----------

This prevents all writes to the buffer. Any attempt to write
to the buffer after this will fail and return NULL.

The caller should call \ :c:func:`synchronize_sched`\  after this.

.. _`ring_buffer_record_enable_cpu`:

ring_buffer_record_enable_cpu
=============================

.. c:function:: void ring_buffer_record_enable_cpu(struct ring_buffer *buffer, int cpu)

    enable writes to the buffer

    :param struct ring_buffer \*buffer:
        The ring buffer to enable writes

    :param int cpu:
        The CPU to enable.

.. _`ring_buffer_record_enable_cpu.description`:

Description
-----------

Note, multiple disables will need the same number of enables
to truly enable the writing (much like preempt_disable).

.. _`ring_buffer_oldest_event_ts`:

ring_buffer_oldest_event_ts
===========================

.. c:function:: u64 ring_buffer_oldest_event_ts(struct ring_buffer *buffer, int cpu)

    get the oldest event timestamp from the buffer

    :param struct ring_buffer \*buffer:
        The ring buffer

    :param int cpu:
        The per CPU buffer to read from.

.. _`ring_buffer_bytes_cpu`:

ring_buffer_bytes_cpu
=====================

.. c:function:: unsigned long ring_buffer_bytes_cpu(struct ring_buffer *buffer, int cpu)

    get the number of bytes consumed in a cpu buffer

    :param struct ring_buffer \*buffer:
        The ring buffer

    :param int cpu:
        The per CPU buffer to read from.

.. _`ring_buffer_entries_cpu`:

ring_buffer_entries_cpu
=======================

.. c:function:: unsigned long ring_buffer_entries_cpu(struct ring_buffer *buffer, int cpu)

    get the number of entries in a cpu buffer

    :param struct ring_buffer \*buffer:
        The ring buffer

    :param int cpu:
        The per CPU buffer to get the entries from.

.. _`ring_buffer_overrun_cpu`:

ring_buffer_overrun_cpu
=======================

.. c:function:: unsigned long ring_buffer_overrun_cpu(struct ring_buffer *buffer, int cpu)

    get the number of overruns caused by the ring buffer wrapping around (only if RB_FL_OVERWRITE is on).

    :param struct ring_buffer \*buffer:
        The ring buffer

    :param int cpu:
        The per CPU buffer to get the number of overruns from

.. _`ring_buffer_commit_overrun_cpu`:

ring_buffer_commit_overrun_cpu
==============================

.. c:function:: unsigned long ring_buffer_commit_overrun_cpu(struct ring_buffer *buffer, int cpu)

    get the number of overruns caused by commits failing due to the buffer wrapping around while there are uncommitted events, such as during an interrupt storm.

    :param struct ring_buffer \*buffer:
        The ring buffer

    :param int cpu:
        The per CPU buffer to get the number of overruns from

.. _`ring_buffer_dropped_events_cpu`:

ring_buffer_dropped_events_cpu
==============================

.. c:function:: unsigned long ring_buffer_dropped_events_cpu(struct ring_buffer *buffer, int cpu)

    get the number of dropped events caused by the ring buffer filling up (only if RB_FL_OVERWRITE is off).

    :param struct ring_buffer \*buffer:
        The ring buffer

    :param int cpu:
        The per CPU buffer to get the number of overruns from

.. _`ring_buffer_read_events_cpu`:

ring_buffer_read_events_cpu
===========================

.. c:function:: unsigned long ring_buffer_read_events_cpu(struct ring_buffer *buffer, int cpu)

    get the number of events successfully read

    :param struct ring_buffer \*buffer:
        The ring buffer

    :param int cpu:
        The per CPU buffer to get the number of events read

.. _`ring_buffer_entries`:

ring_buffer_entries
===================

.. c:function:: unsigned long ring_buffer_entries(struct ring_buffer *buffer)

    get the number of entries in a buffer

    :param struct ring_buffer \*buffer:
        The ring buffer

.. _`ring_buffer_entries.description`:

Description
-----------

Returns the total number of entries in the ring buffer
(all CPU entries)

.. _`ring_buffer_overruns`:

ring_buffer_overruns
====================

.. c:function:: unsigned long ring_buffer_overruns(struct ring_buffer *buffer)

    get the number of overruns in buffer

    :param struct ring_buffer \*buffer:
        The ring buffer

.. _`ring_buffer_overruns.description`:

Description
-----------

Returns the total number of overruns in the ring buffer
(all CPU entries)

.. _`ring_buffer_iter_reset`:

ring_buffer_iter_reset
======================

.. c:function:: void ring_buffer_iter_reset(struct ring_buffer_iter *iter)

    reset an iterator

    :param struct ring_buffer_iter \*iter:
        The iterator to reset

.. _`ring_buffer_iter_reset.description`:

Description
-----------

Resets the iterator, so that it will start from the beginning
again.

.. _`ring_buffer_iter_empty`:

ring_buffer_iter_empty
======================

.. c:function:: int ring_buffer_iter_empty(struct ring_buffer_iter *iter)

    check if an iterator has no more to read

    :param struct ring_buffer_iter \*iter:
        The iterator to check

.. _`ring_buffer_peek`:

ring_buffer_peek
================

.. c:function:: struct ring_buffer_event *ring_buffer_peek(struct ring_buffer *buffer, int cpu, u64 *ts, unsigned long *lost_events)

    peek at the next event to be read

    :param struct ring_buffer \*buffer:
        The ring buffer to read

    :param int cpu:
        The cpu to peak at

    :param u64 \*ts:
        The timestamp counter of this event.

    :param unsigned long \*lost_events:
        a variable to store if events were lost (may be NULL)

.. _`ring_buffer_peek.description`:

Description
-----------

This will return the event that will be read next, but does
not consume the data.

.. _`ring_buffer_iter_peek`:

ring_buffer_iter_peek
=====================

.. c:function:: struct ring_buffer_event *ring_buffer_iter_peek(struct ring_buffer_iter *iter, u64 *ts)

    peek at the next event to be read

    :param struct ring_buffer_iter \*iter:
        The ring buffer iterator

    :param u64 \*ts:
        The timestamp counter of this event.

.. _`ring_buffer_iter_peek.description`:

Description
-----------

This will return the event that will be read next, but does
not increment the iterator.

.. _`ring_buffer_consume`:

ring_buffer_consume
===================

.. c:function:: struct ring_buffer_event *ring_buffer_consume(struct ring_buffer *buffer, int cpu, u64 *ts, unsigned long *lost_events)

    return an event and consume it

    :param struct ring_buffer \*buffer:
        The ring buffer to get the next event from

    :param int cpu:
        the cpu to read the buffer from

    :param u64 \*ts:
        a variable to store the timestamp (may be NULL)

    :param unsigned long \*lost_events:
        a variable to store if events were lost (may be NULL)

.. _`ring_buffer_consume.description`:

Description
-----------

Returns the next event in the ring buffer, and that event is consumed.
Meaning, that sequential reads will keep returning a different event,
and eventually empty the ring buffer if the producer is slower.

.. _`ring_buffer_read_prepare`:

ring_buffer_read_prepare
========================

.. c:function:: struct ring_buffer_iter *ring_buffer_read_prepare(struct ring_buffer *buffer, int cpu)

    Prepare for a non consuming read of the buffer

    :param struct ring_buffer \*buffer:
        The ring buffer to read from

    :param int cpu:
        The cpu buffer to iterate over

.. _`ring_buffer_read_prepare.description`:

Description
-----------

This performs the initial preparations necessary to iterate
through the buffer.  Memory is allocated, buffer recording
is disabled, and the iterator pointer is returned to the caller.

Disabling buffer recordng prevents the reading from being
corrupted. This is not a consuming read, so a producer is not
expected.

After a sequence of ring_buffer_read_prepare calls, the user is
expected to make at least one call to ring_buffer_read_prepare_sync.
Afterwards, ring_buffer_read_start is invoked to get things going
for real.

This overall must be paired with ring_buffer_read_finish.

.. _`ring_buffer_read_prepare_sync`:

ring_buffer_read_prepare_sync
=============================

.. c:function:: void ring_buffer_read_prepare_sync( void)

    Synchronize a set of prepare calls

    :param  void:
        no arguments

.. _`ring_buffer_read_prepare_sync.description`:

Description
-----------

All previously invoked ring_buffer_read_prepare calls to prepare
iterators will be synchronized.  Afterwards, read_buffer_read_start
calls on those iterators are allowed.

.. _`ring_buffer_read_start`:

ring_buffer_read_start
======================

.. c:function:: void ring_buffer_read_start(struct ring_buffer_iter *iter)

    start a non consuming read of the buffer

    :param struct ring_buffer_iter \*iter:
        The iterator returned by ring_buffer_read_prepare

.. _`ring_buffer_read_start.description`:

Description
-----------

This finalizes the startup of an iteration through the buffer.
The iterator comes from a call to ring_buffer_read_prepare and
an intervening ring_buffer_read_prepare_sync must have been
performed.

Must be paired with ring_buffer_read_finish.

.. _`ring_buffer_read_finish`:

ring_buffer_read_finish
=======================

.. c:function:: void ring_buffer_read_finish(struct ring_buffer_iter *iter)

    finish reading the iterator of the buffer

    :param struct ring_buffer_iter \*iter:
        The iterator retrieved by ring_buffer_start

.. _`ring_buffer_read_finish.description`:

Description
-----------

This re-enables the recording to the buffer, and frees the
iterator.

.. _`ring_buffer_read`:

ring_buffer_read
================

.. c:function:: struct ring_buffer_event *ring_buffer_read(struct ring_buffer_iter *iter, u64 *ts)

    read the next item in the ring buffer by the iterator

    :param struct ring_buffer_iter \*iter:
        The ring buffer iterator

    :param u64 \*ts:
        The time stamp of the event read.

.. _`ring_buffer_read.description`:

Description
-----------

This reads the next event in the ring buffer and increments the iterator.

.. _`ring_buffer_size`:

ring_buffer_size
================

.. c:function:: unsigned long ring_buffer_size(struct ring_buffer *buffer, int cpu)

    return the size of the ring buffer (in bytes)

    :param struct ring_buffer \*buffer:
        The ring buffer.

    :param int cpu:
        *undescribed*

.. _`ring_buffer_reset_cpu`:

ring_buffer_reset_cpu
=====================

.. c:function:: void ring_buffer_reset_cpu(struct ring_buffer *buffer, int cpu)

    reset a ring buffer per CPU buffer

    :param struct ring_buffer \*buffer:
        The ring buffer to reset a per cpu buffer of

    :param int cpu:
        The CPU buffer to be reset

.. _`ring_buffer_reset`:

ring_buffer_reset
=================

.. c:function:: void ring_buffer_reset(struct ring_buffer *buffer)

    reset a ring buffer

    :param struct ring_buffer \*buffer:
        The ring buffer to reset all cpu buffers

.. _`ring_buffer_empty`:

ring_buffer_empty
=================

.. c:function:: bool ring_buffer_empty(struct ring_buffer *buffer)

    is the ring buffer empty?

    :param struct ring_buffer \*buffer:
        The ring buffer to test

.. _`ring_buffer_empty_cpu`:

ring_buffer_empty_cpu
=====================

.. c:function:: bool ring_buffer_empty_cpu(struct ring_buffer *buffer, int cpu)

    is a cpu buffer of a ring buffer empty?

    :param struct ring_buffer \*buffer:
        The ring buffer

    :param int cpu:
        The CPU buffer to test

.. _`ring_buffer_swap_cpu`:

ring_buffer_swap_cpu
====================

.. c:function:: int ring_buffer_swap_cpu(struct ring_buffer *buffer_a, struct ring_buffer *buffer_b, int cpu)

    swap a CPU buffer between two ring buffers

    :param struct ring_buffer \*buffer_a:
        One buffer to swap with

    :param struct ring_buffer \*buffer_b:
        The other buffer to swap with

    :param int cpu:
        *undescribed*

.. _`ring_buffer_swap_cpu.description`:

Description
-----------

This function is useful for tracers that want to take a "snapshot"
of a CPU buffer and has another back up buffer lying around.
it is expected that the tracer handles the cpu buffer not being
used at the moment.

.. _`ring_buffer_alloc_read_page`:

ring_buffer_alloc_read_page
===========================

.. c:function:: void *ring_buffer_alloc_read_page(struct ring_buffer *buffer, int cpu)

    allocate a page to read from buffer

    :param struct ring_buffer \*buffer:
        the buffer to allocate for.

    :param int cpu:
        the cpu buffer to allocate.

.. _`ring_buffer_alloc_read_page.description`:

Description
-----------

This function is used in conjunction with ring_buffer_read_page.
When reading a full page from the ring buffer, these functions
can be used to speed up the process. The calling function should
allocate a few pages first with this function. Then when it
needs to get pages from the ring buffer, it passes the result
of this function into ring_buffer_read_page, which will swap
the page that was allocated, with the read page of the buffer.

.. _`ring_buffer_alloc_read_page.return`:

Return
------

The page allocated, or NULL on error.

.. _`ring_buffer_free_read_page`:

ring_buffer_free_read_page
==========================

.. c:function:: void ring_buffer_free_read_page(struct ring_buffer *buffer, void *data)

    free an allocated read page

    :param struct ring_buffer \*buffer:
        the buffer the page was allocate for

    :param void \*data:
        the page to free

.. _`ring_buffer_free_read_page.description`:

Description
-----------

Free a page allocated from ring_buffer_alloc_read_page.

.. _`ring_buffer_read_page`:

ring_buffer_read_page
=====================

.. c:function:: int ring_buffer_read_page(struct ring_buffer *buffer, void **data_page, size_t len, int cpu, int full)

    extract a page from the ring buffer

    :param struct ring_buffer \*buffer:
        buffer to extract from

    :param void \*\*data_page:
        the page to use allocated from ring_buffer_alloc_read_page

    :param size_t len:
        amount to extract

    :param int cpu:
        the cpu of the buffer to extract

    :param int full:
        should the extraction only happen when the page is full.

.. _`ring_buffer_read_page.description`:

Description
-----------

This function will pull out a page from the ring buffer and consume it.
\ ``data_page``\  must be the address of the variable that was returned
from ring_buffer_alloc_read_page. This is because the page might be used
to swap with a page in the ring buffer.

.. _`ring_buffer_read_page.for-example`:

for example
-----------

rpage = ring_buffer_alloc_read_page(buffer, cpu);
if (!rpage)
return error;
ret = ring_buffer_read_page(buffer, \ :c:type:`struct rpage <rpage>`, len, cpu, 0);
if (ret >= 0)
process_page(rpage, ret);

When \ ``full``\  is set, the function will not return true unless
the writer is off the reader page.

.. _`ring_buffer_read_page.note`:

Note
----

it is up to the calling functions to handle sleeps and wakeups.
The ring buffer can be used anywhere in the kernel and can not
blindly call wake_up. The layer that uses the ring buffer must be
responsible for that.

.. _`ring_buffer_read_page.return`:

Return
------

>=0 if data has been transferred, returns the offset of consumed data.
<0 if no data has been transferred.

.. This file was automatic generated / don't edit.

