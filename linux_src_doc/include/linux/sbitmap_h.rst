.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sbitmap.h

.. _`sbitmap_word`:

struct sbitmap_word
===================

.. c:type:: struct sbitmap_word

    Word in a \ :c:type:`struct sbitmap <sbitmap>`\ .

.. _`sbitmap_word.definition`:

Definition
----------

.. code-block:: c

    struct sbitmap_word {
        unsigned long word;
        unsigned long depth;
    }

.. _`sbitmap_word.members`:

Members
-------

word
    The bitmap word itself.

depth
    Number of bits being used in \ ``word``\ .

.. _`sbitmap`:

struct sbitmap
==============

.. c:type:: struct sbitmap

    Scalable bitmap.

.. _`sbitmap.definition`:

Definition
----------

.. code-block:: c

    struct sbitmap {
        unsigned int depth;
        unsigned int shift;
        unsigned int map_nr;
        struct sbitmap_word *map;
    }

.. _`sbitmap.members`:

Members
-------

depth
    Number of bits used in the whole bitmap.

shift
    log2(number of bits used per word)

map_nr
    Number of words (cachelines) being used for the bitmap.

map
    Allocated bitmap.

.. _`sbitmap.description`:

Description
-----------

A \ :c:type:`struct sbitmap <sbitmap>`\  is spread over multiple cachelines to avoid ping-pong. This
trades off higher memory usage for better scalability.

.. _`sbq_wait_state`:

struct sbq_wait_state
=====================

.. c:type:: struct sbq_wait_state

    Wait queue in a \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\ .

.. _`sbq_wait_state.definition`:

Definition
----------

.. code-block:: c

    struct sbq_wait_state {
        atomic_t wait_cnt;
        wait_queue_head_t wait;
    }

.. _`sbq_wait_state.members`:

Members
-------

wait_cnt
    Number of frees remaining before we wake up.

wait
    Wait queue.

.. _`sbitmap_queue`:

struct sbitmap_queue
====================

.. c:type:: struct sbitmap_queue

    Scalable bitmap with the added ability to wait on free bits.

.. _`sbitmap_queue.definition`:

Definition
----------

.. code-block:: c

    struct sbitmap_queue {
        struct sbitmap sb;
        unsigned int __percpu *alloc_hint;
        unsigned int wake_batch;
        atomic_t wake_index;
        struct sbq_wait_state *ws;
        bool round_robin;
    }

.. _`sbitmap_queue.members`:

Members
-------

sb
    Scalable bitmap.

alloc_hint
    *undescribed*

wake_batch
    Number of bits which must be freed before we wake up anywaiters.

wake_index
    Next wait queue in \ ``ws``\  to wake up.

ws
    Wait queues.

round_robin
    Allocate bits in strict round-robin order.

.. _`sbitmap_queue.description`:

Description
-----------

A \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\  uses multiple wait queues and rolling wakeups to
avoid contention on the wait queue spinlock. This ensures that we don't hit a
scalability wall when we run out of free bits and have to start putting tasks
to sleep.

.. _`sbitmap_init_node`:

sbitmap_init_node
=================

.. c:function:: int sbitmap_init_node(struct sbitmap *sb, unsigned int depth, int shift, gfp_t flags, int node)

    Initialize a \ :c:type:`struct sbitmap <sbitmap>`\  on a specific memory node.

    :param struct sbitmap \*sb:
        Bitmap to initialize.

    :param unsigned int depth:
        Number of bits to allocate.

    :param int shift:
        Use 2^@shift bits per word in the bitmap; if a negative number if
        given, a good default is chosen.

    :param gfp_t flags:
        Allocation flags.

    :param int node:
        Memory node to allocate on.

.. _`sbitmap_init_node.return`:

Return
------

Zero on success or negative errno on failure.

.. _`sbitmap_free`:

sbitmap_free
============

.. c:function:: void sbitmap_free(struct sbitmap *sb)

    Free memory used by a \ :c:type:`struct sbitmap <sbitmap>`\ .

    :param struct sbitmap \*sb:
        Bitmap to free.

.. _`sbitmap_resize`:

sbitmap_resize
==============

.. c:function:: void sbitmap_resize(struct sbitmap *sb, unsigned int depth)

    Resize a \ :c:type:`struct sbitmap <sbitmap>`\ .

    :param struct sbitmap \*sb:
        Bitmap to resize.

    :param unsigned int depth:
        New number of bits to resize to.

.. _`sbitmap_resize.description`:

Description
-----------

Doesn't reallocate anything. It's up to the caller to ensure that the new
depth doesn't exceed the depth that the sb was initialized with.

.. _`sbitmap_get`:

sbitmap_get
===========

.. c:function:: int sbitmap_get(struct sbitmap *sb, unsigned int alloc_hint, bool round_robin)

    Try to allocate a free bit from a \ :c:type:`struct sbitmap <sbitmap>`\ .

    :param struct sbitmap \*sb:
        Bitmap to allocate from.

    :param unsigned int alloc_hint:
        Hint for where to start searching for a free bit.

    :param bool round_robin:
        If true, be stricter about allocation order; always allocate
        starting from the last allocated bit. This is less efficient
        than the default behavior (false).

.. _`sbitmap_get.return`:

Return
------

Non-negative allocated bit number if successful, -1 otherwise.

.. _`sbitmap_any_bit_set`:

sbitmap_any_bit_set
===================

.. c:function:: bool sbitmap_any_bit_set(const struct sbitmap *sb)

    Check for a set bit in a \ :c:type:`struct sbitmap <sbitmap>`\ .

    :param const struct sbitmap \*sb:
        Bitmap to check.

.. _`sbitmap_any_bit_set.return`:

Return
------

true if any bit in the bitmap is set, false otherwise.

.. _`sbitmap_any_bit_clear`:

sbitmap_any_bit_clear
=====================

.. c:function:: bool sbitmap_any_bit_clear(const struct sbitmap *sb)

    Check for an unset bit in a \ :c:type:`struct sbitmap <sbitmap>`\ .

    :param const struct sbitmap \*sb:
        Bitmap to check.

.. _`sbitmap_any_bit_clear.return`:

Return
------

true if any bit in the bitmap is clear, false otherwise.

.. _`sbitmap_for_each_set`:

sbitmap_for_each_set
====================

.. c:function:: void sbitmap_for_each_set(struct sbitmap *sb, sb_for_each_fn fn, void *data)

    Iterate over each set bit in a \ :c:type:`struct sbitmap <sbitmap>`\ .

    :param struct sbitmap \*sb:
        Bitmap to iterate over.

    :param sb_for_each_fn fn:
        Callback. Should return true to continue or false to break early.

    :param void \*data:
        Pointer to pass to callback.

.. _`sbitmap_for_each_set.description`:

Description
-----------

This is inline even though it's non-trivial so that the function calls to the
callback will hopefully get optimized away.

.. _`sbitmap_queue_init_node`:

sbitmap_queue_init_node
=======================

.. c:function:: int sbitmap_queue_init_node(struct sbitmap_queue *sbq, unsigned int depth, int shift, bool round_robin, gfp_t flags, int node)

    Initialize a \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\  on a specific memory node.

    :param struct sbitmap_queue \*sbq:
        Bitmap queue to initialize.

    :param unsigned int depth:
        See \ :c:func:`sbitmap_init_node`\ .

    :param int shift:
        See \ :c:func:`sbitmap_init_node`\ .

    :param bool round_robin:
        See \ :c:func:`sbitmap_get`\ .

    :param gfp_t flags:
        Allocation flags.

    :param int node:
        Memory node to allocate on.

.. _`sbitmap_queue_init_node.return`:

Return
------

Zero on success or negative errno on failure.

.. _`sbitmap_queue_free`:

sbitmap_queue_free
==================

.. c:function:: void sbitmap_queue_free(struct sbitmap_queue *sbq)

    Free memory used by a \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\ .

    :param struct sbitmap_queue \*sbq:
        Bitmap queue to free.

.. _`sbitmap_queue_resize`:

sbitmap_queue_resize
====================

.. c:function:: void sbitmap_queue_resize(struct sbitmap_queue *sbq, unsigned int depth)

    Resize a \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\ .

    :param struct sbitmap_queue \*sbq:
        Bitmap queue to resize.

    :param unsigned int depth:
        New number of bits to resize to.

.. _`sbitmap_queue_resize.description`:

Description
-----------

Like \ :c:func:`sbitmap_resize`\ , this doesn't reallocate anything. It has to do
some extra work on the \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\ , so it's not safe to just
resize the underlying \ :c:type:`struct sbitmap <sbitmap>`\ .

.. _`__sbitmap_queue_get`:

__sbitmap_queue_get
===================

.. c:function:: int __sbitmap_queue_get(struct sbitmap_queue *sbq)

    Try to allocate a free bit from a \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\  with preemption already disabled.

    :param struct sbitmap_queue \*sbq:
        Bitmap queue to allocate from.

.. _`__sbitmap_queue_get.return`:

Return
------

Non-negative allocated bit number if successful, -1 otherwise.

.. _`sbitmap_queue_get`:

sbitmap_queue_get
=================

.. c:function:: int sbitmap_queue_get(struct sbitmap_queue *sbq, unsigned int *cpu)

    Try to allocate a free bit from a \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\ .

    :param struct sbitmap_queue \*sbq:
        Bitmap queue to allocate from.

    :param unsigned int \*cpu:
        Output parameter; will contain the CPU we ran on (e.g., to be passed to
        \ :c:func:`sbitmap_queue_clear`\ ).

.. _`sbitmap_queue_get.return`:

Return
------

Non-negative allocated bit number if successful, -1 otherwise.

.. _`sbitmap_queue_clear`:

sbitmap_queue_clear
===================

.. c:function:: void sbitmap_queue_clear(struct sbitmap_queue *sbq, unsigned int nr, unsigned int cpu)

    Free an allocated bit and wake up waiters on a \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\ .

    :param struct sbitmap_queue \*sbq:
        Bitmap to free from.

    :param unsigned int nr:
        Bit number to free.

    :param unsigned int cpu:
        CPU the bit was allocated on.

.. _`sbq_wait_ptr`:

sbq_wait_ptr
============

.. c:function:: struct sbq_wait_state *sbq_wait_ptr(struct sbitmap_queue *sbq, atomic_t *wait_index)

    Get the next wait queue to use for a \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\ .

    :param struct sbitmap_queue \*sbq:
        Bitmap queue to wait on.

    :param atomic_t \*wait_index:
        A counter per "user" of \ ``sbq``\ .

.. _`sbitmap_queue_wake_all`:

sbitmap_queue_wake_all
======================

.. c:function:: void sbitmap_queue_wake_all(struct sbitmap_queue *sbq)

    Wake up everything waiting on a \ :c:type:`struct sbitmap_queue <sbitmap_queue>`\ .

    :param struct sbitmap_queue \*sbq:
        Bitmap queue to wake up.

.. This file was automatic generated / don't edit.
