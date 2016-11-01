.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/seqlock.h

.. _`__read_seqcount_begin`:

__read_seqcount_begin
=====================

.. c:function:: unsigned __read_seqcount_begin(const seqcount_t *s)

    begin a seq-read critical section (without barrier)

    :param const seqcount_t \*s:
        pointer to seqcount_t

.. _`__read_seqcount_begin.return`:

Return
------

count to be passed to read_seqcount_retry

\__read_seqcount_begin is like read_seqcount_begin, but has no \ :c:func:`smp_rmb`\ 
barrier. Callers should ensure that \ :c:func:`smp_rmb`\  or equivalent ordering is
provided before actually loading any of the variables that are to be
protected in this critical section.

Use carefully, only in critical code, and comment how the barrier is
provided.

.. _`raw_read_seqcount`:

raw_read_seqcount
=================

.. c:function:: unsigned raw_read_seqcount(const seqcount_t *s)

    Read the raw seqcount

    :param const seqcount_t \*s:
        pointer to seqcount_t

.. _`raw_read_seqcount.return`:

Return
------

count to be passed to read_seqcount_retry

raw_read_seqcount opens a read critical section of the given
seqcount without any lockdep checking and without checking or
masking the LSB. Calling code is responsible for handling that.

.. _`raw_read_seqcount_begin`:

raw_read_seqcount_begin
=======================

.. c:function:: unsigned raw_read_seqcount_begin(const seqcount_t *s)

    start seq-read critical section w/o lockdep

    :param const seqcount_t \*s:
        pointer to seqcount_t

.. _`raw_read_seqcount_begin.return`:

Return
------

count to be passed to read_seqcount_retry

raw_read_seqcount_begin opens a read critical section of the given
seqcount, but without any lockdep checking. Validity of the critical
section is tested by checking read_seqcount_retry function.

.. _`read_seqcount_begin`:

read_seqcount_begin
===================

.. c:function:: unsigned read_seqcount_begin(const seqcount_t *s)

    begin a seq-read critical section

    :param const seqcount_t \*s:
        pointer to seqcount_t

.. _`read_seqcount_begin.return`:

Return
------

count to be passed to read_seqcount_retry

read_seqcount_begin opens a read critical section of the given seqcount.
Validity of the critical section is tested by checking read_seqcount_retry
function.

.. _`raw_seqcount_begin`:

raw_seqcount_begin
==================

.. c:function:: unsigned raw_seqcount_begin(const seqcount_t *s)

    begin a seq-read critical section

    :param const seqcount_t \*s:
        pointer to seqcount_t

.. _`raw_seqcount_begin.return`:

Return
------

count to be passed to read_seqcount_retry

raw_seqcount_begin opens a read critical section of the given seqcount.
Validity of the critical section is tested by checking read_seqcount_retry
function.

Unlike \ :c:func:`read_seqcount_begin`\ , this function will not wait for the count
to stabilize. If a writer is active when we begin, we will fail the
\ :c:func:`read_seqcount_retry`\  instead of stabilizing at the beginning of the
critical section.

.. _`__read_seqcount_retry`:

__read_seqcount_retry
=====================

.. c:function:: int __read_seqcount_retry(const seqcount_t *s, unsigned start)

    end a seq-read critical section (without barrier)

    :param const seqcount_t \*s:
        pointer to seqcount_t

    :param unsigned start:
        count, from read_seqcount_begin

.. _`__read_seqcount_retry.return`:

Return
------

1 if retry is required, else 0

\__read_seqcount_retry is like read_seqcount_retry, but has no \ :c:func:`smp_rmb`\ 
barrier. Callers should ensure that \ :c:func:`smp_rmb`\  or equivalent ordering is
provided before actually loading any of the variables that are to be
protected in this critical section.

Use carefully, only in critical code, and comment how the barrier is
provided.

.. _`read_seqcount_retry`:

read_seqcount_retry
===================

.. c:function:: int read_seqcount_retry(const seqcount_t *s, unsigned start)

    end a seq-read critical section

    :param const seqcount_t \*s:
        pointer to seqcount_t

    :param unsigned start:
        count, from read_seqcount_begin

.. _`read_seqcount_retry.return`:

Return
------

1 if retry is required, else 0

read_seqcount_retry closes a read critical section of the given seqcount.
If the critical section was invalid, it must be ignored (and typically
retried).

.. _`raw_write_seqcount_barrier`:

raw_write_seqcount_barrier
==========================

.. c:function:: void raw_write_seqcount_barrier(seqcount_t *s)

    do a seq write barrier

    :param seqcount_t \*s:
        pointer to seqcount_t

.. _`raw_write_seqcount_barrier.description`:

Description
-----------

This can be used to provide an ordering guarantee instead of the
usual consistency guarantee. It is one wmb cheaper, because we can
collapse the two back-to-back \ :c:func:`wmb`\ s.

seqcount_t seq;
bool X = true, Y = false;

void read(void)
{
bool x, y;

do {
int s = read_seqcount_begin(&seq);

x = X; y = Y;

} while (read_seqcount_retry(&seq, s));

BUG_ON(!x && !y);
}

void write(void)
{
Y = true;

raw_write_seqcount_barrier(seq);

X = false;
}

.. _`raw_write_seqcount_latch`:

raw_write_seqcount_latch
========================

.. c:function:: void raw_write_seqcount_latch(seqcount_t *s)

    redirect readers to even/odd copy

    :param seqcount_t \*s:
        pointer to seqcount_t

.. _`raw_write_seqcount_latch.description`:

Description
-----------

The latch technique is a multiversion concurrency control method that allows
queries during non-atomic modifications. If you can guarantee queries never
interrupt the modification -- e.g. the concurrency is strictly between CPUs
-- you most likely do not need this.

Where the traditional RCU/lockless data structures rely on atomic
modifications to ensure queries observe either the old or the new state the
latch allows the same for non-atomic updates. The trade-off is doubling the
cost of storage; we have to maintain two copies of the entire data
structure.

.. _`raw_write_seqcount_latch.very-simply-put`:

Very simply put
---------------

we first modify one copy and then the other. This ensures
there is always one copy in a stable state, ready to give us an answer.

.. _`raw_write_seqcount_latch.the-basic-form-is-a-data-structure-like`:

The basic form is a data structure like
---------------------------------------


struct latch_struct {
seqcount_t              seq;
struct data_struct      data[2];
};

Where a modification, which is assumed to be externally serialized, does the

.. _`raw_write_seqcount_latch.following`:

following
---------


void latch_modify(struct latch_struct \*latch, ...)
{
\ :c:func:`smp_wmb`\ ;      <- Ensure that the last data[1] update is visible
latch->seq++;
\ :c:func:`smp_wmb`\ ;      <- Ensure that the seqcount update is visible

modify(latch->data[0], ...);

\ :c:func:`smp_wmb`\ ;      <- Ensure that the data[0] update is visible
latch->seq++;
\ :c:func:`smp_wmb`\ ;      <- Ensure that the seqcount update is visible

modify(latch->data[1], ...);
}

.. _`raw_write_seqcount_latch.the-query-will-have-a-form-like`:

The query will have a form like
-------------------------------


struct entry \*latch_query(struct latch_struct \*latch, ...)
{
struct entry \*entry;
unsigned seq, idx;

do {
seq = raw_read_seqcount_latch(&latch->seq);

idx = seq & 0x01;
entry = data_query(latch->data[idx], ...);

\ :c:func:`smp_rmb`\ ;
} while (seq != latch->seq);

return entry;
}

So during the modification, queries are first redirected to data[1]. Then we
modify data[0]. When that is complete, we redirect queries back to data[0]
and we can modify data[1].

.. _`raw_write_seqcount_latch.note`:

NOTE
----

The non-requirement for atomic modifications does \_NOT\_ include
the publishing of new entries in the case where data is a dynamic
data structure.

An iteration might start in data[0] and get suspended long enough
to miss an entire modification sequence, once it resumes it might
observe the new entry.

When data is a dynamic data structure; one should use regular RCU
patterns to manage the lifetimes of the objects within.

.. _`write_seqcount_invalidate`:

write_seqcount_invalidate
=========================

.. c:function:: void write_seqcount_invalidate(seqcount_t *s)

    invalidate in-progress read-side seq operations

    :param seqcount_t \*s:
        pointer to seqcount_t

.. _`write_seqcount_invalidate.description`:

Description
-----------

After write_seqcount_invalidate, no read-side seq operations will complete
successfully and see data older than this.

.. _`read_seqbegin_or_lock`:

read_seqbegin_or_lock
=====================

.. c:function:: void read_seqbegin_or_lock(seqlock_t *lock, int *seq)

    begin a sequence number check or locking block

    :param seqlock_t \*lock:
        sequence lock

    :param int \*seq:
        sequence number to be checked

.. _`read_seqbegin_or_lock.description`:

Description
-----------

First try it once optimistically without taking the lock. If that fails,
take the lock. The sequence number is also used as a marker for deciding
whether to be a reader (even) or writer (odd).
N.B. seq must be initialized to an even number to begin with.

.. This file was automatic generated / don't edit.

