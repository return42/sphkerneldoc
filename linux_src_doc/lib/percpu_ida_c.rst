.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/percpu_ida.c

.. _`percpu_ida_alloc`:

percpu_ida_alloc
================

.. c:function:: int percpu_ida_alloc(struct percpu_ida *pool, int state)

    allocate a tag

    :param struct percpu_ida \*pool:
        pool to allocate from

    :param int state:
        task state for prepare_to_wait

.. _`percpu_ida_alloc.description`:

Description
-----------

Returns a tag - an integer in the range [0..nr_tags) (passed to
\ :c:func:`tag_pool_init`\ ), or otherwise -ENOSPC on allocation failure.

Safe to be called from interrupt context (assuming it isn't passed
TASK_UNINTERRUPTIBLE \| TASK_INTERRUPTIBLE, of course).

\ ``gfp``\  indicates whether or not to wait until a free id is available (it's not
used for internal memory allocations); thus if passed \__GFP_RECLAIM we may sleep
however long it takes until another thread frees an id (same semantics as a
mempool).

Will not fail if passed TASK_UNINTERRUPTIBLE \| TASK_INTERRUPTIBLE.

.. _`percpu_ida_free`:

percpu_ida_free
===============

.. c:function:: void percpu_ida_free(struct percpu_ida *pool, unsigned tag)

    free a tag

    :param struct percpu_ida \*pool:
        pool \ ``tag``\  was allocated from

    :param unsigned tag:
        a tag previously allocated with \ :c:func:`percpu_ida_alloc`\ 

.. _`percpu_ida_free.description`:

Description
-----------

Safe to be called from interrupt context.

.. _`percpu_ida_destroy`:

percpu_ida_destroy
==================

.. c:function:: void percpu_ida_destroy(struct percpu_ida *pool)

    release a tag pool's resources

    :param struct percpu_ida \*pool:
        pool to free

.. _`percpu_ida_destroy.description`:

Description
-----------

Frees the resources allocated by \ :c:func:`percpu_ida_init`\ .

.. _`__percpu_ida_init`:

__percpu_ida_init
=================

.. c:function:: int __percpu_ida_init(struct percpu_ida *pool, unsigned long nr_tags, unsigned long max_size, unsigned long batch_size)

    initialize a percpu tag pool

    :param struct percpu_ida \*pool:
        pool to initialize

    :param unsigned long nr_tags:
        number of tags that will be available for allocation

    :param unsigned long max_size:
        *undescribed*

    :param unsigned long batch_size:
        *undescribed*

.. _`__percpu_ida_init.description`:

Description
-----------

Initializes \ ``pool``\  so that it can be used to allocate tags - integers in the
range [0, nr_tags). Typically, they'll be used by driver code to refer to a
preallocated array of tag structures.

Allocation is percpu, but sharding is limited by nr_tags - for best
performance, the workload should not span more cpus than nr_tags / 128.

.. _`percpu_ida_for_each_free`:

percpu_ida_for_each_free
========================

.. c:function:: int percpu_ida_for_each_free(struct percpu_ida *pool, percpu_ida_cb fn, void *data)

    iterate free ids of a pool

    :param struct percpu_ida \*pool:
        pool to iterate

    :param percpu_ida_cb fn:
        interate callback function

    :param void \*data:
        parameter for \ ``fn``\ 

.. _`percpu_ida_for_each_free.description`:

Description
-----------

Note, this doesn't guarantee to iterate all free ids restrictly. Some free
ids might be missed, some might be iterated duplicated, and some might
be iterated and not free soon.

.. _`percpu_ida_free_tags`:

percpu_ida_free_tags
====================

.. c:function:: unsigned percpu_ida_free_tags(struct percpu_ida *pool, int cpu)

    return free tags number of a specific cpu or global pool

    :param struct percpu_ida \*pool:
        pool related

    :param int cpu:
        specific cpu or global pool if \ ``cpu``\  == nr_cpu_ids

.. _`percpu_ida_free_tags.note`:

Note
----

this just returns a snapshot of free tags number.

.. This file was automatic generated / don't edit.

