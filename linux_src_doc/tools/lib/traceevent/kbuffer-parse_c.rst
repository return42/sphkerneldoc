.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/traceevent/kbuffer-parse.c

.. _`kbuffer_alloc`:

kbuffer_alloc
=============

.. c:function:: struct kbuffer *kbuffer_alloc(enum kbuffer_long_size size, enum kbuffer_endian endian)

    allocat a new kbuffer \ ``size``\ ;       enum to denote size of word

    :param size:
        *undescribed*
    :type size: enum kbuffer_long_size

    :param endian:
        enum to denote endianness
    :type endian: enum kbuffer_endian

.. _`kbuffer_alloc.description`:

Description
-----------

Allocates and returns a new kbuffer.

.. _`kbuffer_translate_data`:

kbuffer_translate_data
======================

.. c:function:: void *kbuffer_translate_data(int swap, void *data, unsigned int *size)

    read raw data to get a record

    :param swap:
        Set to 1 if bytes in words need to be swapped when read
    :type swap: int

    :param data:
        The raw data to read
    :type data: void \*

    :param size:
        Address to store the size of the event data.
    :type size: unsigned int \*

.. _`kbuffer_translate_data.description`:

Description
-----------

Returns a pointer to the event data. To determine the entire
record size (record metadata + data) just add the difference between
\ ``data``\  and the returned value to \ ``size``\ .

.. _`kbuffer_next_event`:

kbuffer_next_event
==================

.. c:function:: void *kbuffer_next_event(struct kbuffer *kbuf, unsigned long long *ts)

    increment the current pointer

    :param kbuf:
        The kbuffer to read
    :type kbuf: struct kbuffer \*

    :param ts:
        Address to store the next record's timestamp (may be NULL to ignore)
    :type ts: unsigned long long \*

.. _`kbuffer_next_event.description`:

Description
-----------

Increments the pointers into the subbuffer of the kbuffer to point to the
next event so that the next \ :c:func:`kbuffer_read_event`\  will return a
new event.

Returns the data of the next event if a new event exists on the subbuffer,
NULL otherwise.

.. _`kbuffer_load_subbuffer`:

kbuffer_load_subbuffer
======================

.. c:function:: int kbuffer_load_subbuffer(struct kbuffer *kbuf, void *subbuffer)

    load a new subbuffer into the kbuffer

    :param kbuf:
        The kbuffer to load
    :type kbuf: struct kbuffer \*

    :param subbuffer:
        The subbuffer to load into \ ``kbuf``\ .
    :type subbuffer: void \*

.. _`kbuffer_load_subbuffer.description`:

Description
-----------

Load a new subbuffer (page) into \ ``kbuf``\ . This will reset all
the pointers and update the \ ``kbuf``\  timestamp. The next read will
return the first event on \ ``subbuffer``\ .

Returns 0 on succes, -1 otherwise.

.. _`kbuffer_read_event`:

kbuffer_read_event
==================

.. c:function:: void *kbuffer_read_event(struct kbuffer *kbuf, unsigned long long *ts)

    read the next event in the kbuffer subbuffer

    :param kbuf:
        The kbuffer to read from
    :type kbuf: struct kbuffer \*

    :param ts:
        The address to store the timestamp of the event (may be NULL to ignore)
    :type ts: unsigned long long \*

.. _`kbuffer_read_event.description`:

Description
-----------

Returns a pointer to the data part of the current event.
NULL if no event is left on the subbuffer.

.. _`kbuffer_timestamp`:

kbuffer_timestamp
=================

.. c:function:: unsigned long long kbuffer_timestamp(struct kbuffer *kbuf)

    Return the timestamp of the current event

    :param kbuf:
        The kbuffer to read from
    :type kbuf: struct kbuffer \*

.. _`kbuffer_timestamp.description`:

Description
-----------

Returns the timestamp of the current (next) event.

.. _`kbuffer_read_at_offset`:

kbuffer_read_at_offset
======================

.. c:function:: void *kbuffer_read_at_offset(struct kbuffer *kbuf, int offset, unsigned long long *ts)

    read the event that is at offset

    :param kbuf:
        The kbuffer to read from
    :type kbuf: struct kbuffer \*

    :param offset:
        The offset into the subbuffer
    :type offset: int

    :param ts:
        The address to store the timestamp of the event (may be NULL to ignore)
    :type ts: unsigned long long \*

.. _`kbuffer_read_at_offset.description`:

Description
-----------

The \ ``offset``\  must be an index from the \ ``kbuf``\  subbuffer beginning.
If \ ``offset``\  is bigger than the stored subbuffer, NULL will be returned.

Returns the data of the record that is at \ ``offset``\ . Note, \ ``offset``\  does
not need to be the start of the record, the offset just needs to be
in the record (or beginning of it).

Note, the kbuf timestamp and pointers are updated to the
returned record. That is, \ :c:func:`kbuffer_read_event`\  will return the same
data and timestamp, and \ :c:func:`kbuffer_next_event`\  will increment from
this record.

.. _`kbuffer_subbuffer_size`:

kbuffer_subbuffer_size
======================

.. c:function:: int kbuffer_subbuffer_size(struct kbuffer *kbuf)

    the size of the loaded subbuffer

    :param kbuf:
        The kbuffer to read from
    :type kbuf: struct kbuffer \*

.. _`kbuffer_subbuffer_size.description`:

Description
-----------

Returns the size of the subbuffer. Note, this size is
where the last event resides. The stored subbuffer may actually be
bigger due to padding and such.

.. _`kbuffer_curr_index`:

kbuffer_curr_index
==================

.. c:function:: int kbuffer_curr_index(struct kbuffer *kbuf)

    Return the index of the record

    :param kbuf:
        The kbuffer to read from
    :type kbuf: struct kbuffer \*

.. _`kbuffer_curr_index.description`:

Description
-----------

Returns the index from the start of the data part of
the subbuffer to the current location. Note this is not
from the start of the subbuffer. An index of zero will
point to the first record. Use \ :c:func:`kbuffer_curr_offset`\  for
the actually offset (that can be used by \ :c:func:`kbuffer_read_at_offset`\ )

.. _`kbuffer_curr_offset`:

kbuffer_curr_offset
===================

.. c:function:: int kbuffer_curr_offset(struct kbuffer *kbuf)

    Return the offset of the record

    :param kbuf:
        The kbuffer to read from
    :type kbuf: struct kbuffer \*

.. _`kbuffer_curr_offset.description`:

Description
-----------

Returns the offset from the start of the subbuffer to the
current location.

.. _`kbuffer_event_size`:

kbuffer_event_size
==================

.. c:function:: int kbuffer_event_size(struct kbuffer *kbuf)

    return the size of the event data

    :param kbuf:
        The kbuffer to read
    :type kbuf: struct kbuffer \*

.. _`kbuffer_event_size.description`:

Description
-----------

Returns the size of the event data (the payload not counting
the meta data of the record) of the current event.

.. _`kbuffer_curr_size`:

kbuffer_curr_size
=================

.. c:function:: int kbuffer_curr_size(struct kbuffer *kbuf)

    return the size of the entire record

    :param kbuf:
        The kbuffer to read
    :type kbuf: struct kbuffer \*

.. _`kbuffer_curr_size.description`:

Description
-----------

Returns the size of the entire record (meta data and payload)
of the current event.

.. _`kbuffer_missed_events`:

kbuffer_missed_events
=====================

.. c:function:: int kbuffer_missed_events(struct kbuffer *kbuf)

    return the # of missed events from last event.

    :param kbuf:
        The kbuffer to read from
    :type kbuf: struct kbuffer \*

.. _`kbuffer_missed_events.description`:

Description
-----------

Returns the # of missed events (if recorded) before the current
event. Note, only events on the beginning of a subbuffer can
have missed events, all other events within the buffer will be
zero.

.. _`kbuffer_set_old_format`:

kbuffer_set_old_format
======================

.. c:function:: void kbuffer_set_old_format(struct kbuffer *kbuf)

    set the kbuffer to use the old format parsing

    :param kbuf:
        The kbuffer to set
    :type kbuf: struct kbuffer \*

.. _`kbuffer_set_old_format.description`:

Description
-----------

This is obsolete (or should be). The first kernels to use the
new ring buffer had a slightly different ring buffer format
(2.6.30 and earlier). It is still somewhat supported by kbuffer,
but should not be counted on in the future.

.. _`kbuffer_start_of_data`:

kbuffer_start_of_data
=====================

.. c:function:: int kbuffer_start_of_data(struct kbuffer *kbuf)

    return offset of where data starts on subbuffer

    :param kbuf:
        The kbuffer
    :type kbuf: struct kbuffer \*

.. _`kbuffer_start_of_data.description`:

Description
-----------

Returns the location on the subbuffer where the data starts.

.. This file was automatic generated / don't edit.

