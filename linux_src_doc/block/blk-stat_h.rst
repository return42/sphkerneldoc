.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-stat.h

.. _`blk_stat_callback`:

struct blk_stat_callback
========================

.. c:type:: struct blk_stat_callback

    Block statistics callback.

.. _`blk_stat_callback.definition`:

Definition
----------

.. code-block:: c

    struct blk_stat_callback {
        struct list_head list;
        struct timer_list timer;
        struct blk_rq_stat __percpu *cpu_stat;
        int (*bucket_fn)(const struct request *);
        unsigned int buckets;
        struct blk_rq_stat *stat;
        void (*timer_fn)(struct blk_stat_callback *);
        void *data;
        struct rcu_head rcu;
    }

.. _`blk_stat_callback.members`:

Members
-------

list
    *undescribed*

timer
    Timer for the next callback invocation.

cpu_stat
    Per-cpu statistics buckets.

bucket_fn
    Given a request, returns which statistics bucket itshould be accounted under. Return -1 for no bucket for this
    request.

buckets
    Number of statistics buckets.

stat
    Array of statistics buckets.

timer_fn
    *undescribed*

data
    Private pointer for the user.

rcu
    *undescribed*

.. _`blk_stat_callback.description`:

Description
-----------

A \ :c:type:`struct blk_stat_callback <blk_stat_callback>`\  is associated with a \ :c:type:`struct request_queue <request_queue>`\ . While
\ ``timer``\  is active, that queue's request completion latencies are sorted into
buckets by \ ``bucket_fn``\  and added to a per-cpu buffer, \ ``cpu_stat``\ . When the
timer fires, \ ``cpu_stat``\  is flushed to \ ``stat``\  and \ ``timer_fn``\  is invoked.

.. _`blk_stat_alloc_callback`:

blk_stat_alloc_callback
=======================

.. c:function:: struct blk_stat_callback *blk_stat_alloc_callback(void (*timer_fn)(struct blk_stat_callback *), int (*bucket_fn)(const struct request *), unsigned int buckets, void *data)

    Allocate a block statistics callback.

    :param void (\*timer_fn)(struct blk_stat_callback \*):
        Timer callback function.

    :param int (\*bucket_fn)(const struct request \*):
        Bucket callback function.

    :param unsigned int buckets:
        Number of statistics buckets.

    :param void \*data:
        Value for the \ ``data``\  field of the \ :c:type:`struct blk_stat_callback <blk_stat_callback>`\ .

.. _`blk_stat_alloc_callback.description`:

Description
-----------

See \ :c:type:`struct blk_stat_callback <blk_stat_callback>`\  for details on the callback functions.

.. _`blk_stat_alloc_callback.return`:

Return
------

&struct blk_stat_callback on success or NULL on ENOMEM.

.. _`blk_stat_add_callback`:

blk_stat_add_callback
=====================

.. c:function:: void blk_stat_add_callback(struct request_queue *q, struct blk_stat_callback *cb)

    Add a block statistics callback to be run on a request queue.

    :param struct request_queue \*q:
        The request queue.

    :param struct blk_stat_callback \*cb:
        The callback.

.. _`blk_stat_add_callback.description`:

Description
-----------

Note that a single \ :c:type:`struct blk_stat_callback <blk_stat_callback>`\  can only be added to a single
\ :c:type:`struct request_queue <request_queue>`\ .

.. _`blk_stat_remove_callback`:

blk_stat_remove_callback
========================

.. c:function:: void blk_stat_remove_callback(struct request_queue *q, struct blk_stat_callback *cb)

    Remove a block statistics callback from a request queue.

    :param struct request_queue \*q:
        The request queue.

    :param struct blk_stat_callback \*cb:
        The callback.

.. _`blk_stat_remove_callback.description`:

Description
-----------

When this returns, the callback is not running on any CPUs and will not be
called again unless readded.

.. _`blk_stat_free_callback`:

blk_stat_free_callback
======================

.. c:function:: void blk_stat_free_callback(struct blk_stat_callback *cb)

    Free a block statistics callback.

    :param struct blk_stat_callback \*cb:
        The callback.

.. _`blk_stat_free_callback.description`:

Description
-----------

@cb may be NULL, in which case this does nothing. If it is not NULL, \ ``cb``\  must
not be associated with a request queue. I.e., if it was previously added with
\ :c:func:`blk_stat_add_callback`\ , it must also have been removed since then with
\ :c:func:`blk_stat_remove_callback`\ .

.. _`blk_stat_is_active`:

blk_stat_is_active
==================

.. c:function:: bool blk_stat_is_active(struct blk_stat_callback *cb)

    Check if a block statistics callback is currently gathering statistics.

    :param struct blk_stat_callback \*cb:
        The callback.

.. _`blk_stat_activate_nsecs`:

blk_stat_activate_nsecs
=======================

.. c:function:: void blk_stat_activate_nsecs(struct blk_stat_callback *cb, u64 nsecs)

    Gather block statistics during a time window in nanoseconds.

    :param struct blk_stat_callback \*cb:
        The callback.

    :param u64 nsecs:
        Number of nanoseconds to gather statistics for.

.. _`blk_stat_activate_nsecs.description`:

Description
-----------

The timer callback will be called when the window expires.

.. _`blk_stat_activate_msecs`:

blk_stat_activate_msecs
=======================

.. c:function:: void blk_stat_activate_msecs(struct blk_stat_callback *cb, unsigned int msecs)

    Gather block statistics during a time window in milliseconds.

    :param struct blk_stat_callback \*cb:
        The callback.

    :param unsigned int msecs:
        Number of milliseconds to gather statistics for.

.. _`blk_stat_activate_msecs.description`:

Description
-----------

The timer callback will be called when the window expires.

.. This file was automatic generated / don't edit.

