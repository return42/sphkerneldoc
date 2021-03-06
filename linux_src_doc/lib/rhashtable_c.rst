.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/rhashtable.c

.. _`rhashtable_shrink`:

rhashtable_shrink
=================

.. c:function:: int rhashtable_shrink(struct rhashtable *ht)

    Shrink hash table while allowing concurrent lookups

    :param ht:
        the hash table to shrink
    :type ht: struct rhashtable \*

.. _`rhashtable_shrink.description`:

Description
-----------

This function shrinks the hash table to fit, i.e., the smallest
size would not cause it to expand right away automatically.

The caller must ensure that no concurrent resizing occurs by holding
ht->mutex.

The caller must ensure that no concurrent table mutations take place.
It is however valid to have concurrent lookups if they are RCU protected.

It is valid to have concurrent insertions and deletions protected by per
bucket locks or concurrent RCU protected lookups and traversals.

.. _`rhashtable_walk_enter`:

rhashtable_walk_enter
=====================

.. c:function:: void rhashtable_walk_enter(struct rhashtable *ht, struct rhashtable_iter *iter)

    Initialise an iterator

    :param ht:
        Table to walk over
    :type ht: struct rhashtable \*

    :param iter:
        Hash table Iterator
    :type iter: struct rhashtable_iter \*

.. _`rhashtable_walk_enter.description`:

Description
-----------

This function prepares a hash table walk.

Note that if you restart a walk after rhashtable_walk_stop you
may see the same object twice.  Also, you may miss objects if
there are removals in between rhashtable_walk_stop and the next
call to rhashtable_walk_start.

For a completely stable walk you should construct your own data
structure outside the hash table.

This function may be called from any process context, including
non-preemptable context, but cannot be called from softirq or
hardirq context.

You must call rhashtable_walk_exit after this function returns.

.. _`rhashtable_walk_exit`:

rhashtable_walk_exit
====================

.. c:function:: void rhashtable_walk_exit(struct rhashtable_iter *iter)

    Free an iterator

    :param iter:
        Hash table Iterator
    :type iter: struct rhashtable_iter \*

.. _`rhashtable_walk_exit.description`:

Description
-----------

This function frees resources allocated by rhashtable_walk_init.

.. _`rhashtable_walk_start_check`:

rhashtable_walk_start_check
===========================

.. c:function:: int rhashtable_walk_start_check(struct rhashtable_iter *iter)

    Start a hash table walk

    :param iter:
        Hash table iterator
    :type iter: struct rhashtable_iter \*

.. _`rhashtable_walk_start_check.description`:

Description
-----------

Start a hash table walk at the current iterator position.  Note that we take
the RCU lock in all cases including when we return an error.  So you must
always call rhashtable_walk_stop to clean up.

Returns zero if successful.

Returns -EAGAIN if resize event occured.  Note that the iterator
will rewind back to the beginning and you may use it immediately
by calling rhashtable_walk_next.

rhashtable_walk_start is defined as an inline variant that returns
void. This is preferred in cases where the caller would ignore
resize events and always continue.

.. _`__rhashtable_walk_find_next`:

\__rhashtable_walk_find_next
============================

.. c:function:: void *__rhashtable_walk_find_next(struct rhashtable_iter *iter)

    Find the next element in a table (or the first one in case of a new walk).

    :param iter:
        Hash table iterator
    :type iter: struct rhashtable_iter \*

.. _`__rhashtable_walk_find_next.description`:

Description
-----------

Returns the found object or NULL when the end of the table is reached.

Returns -EAGAIN if resize event occurred.

.. _`rhashtable_walk_next`:

rhashtable_walk_next
====================

.. c:function:: void *rhashtable_walk_next(struct rhashtable_iter *iter)

    Return the next object and advance the iterator

    :param iter:
        Hash table iterator
    :type iter: struct rhashtable_iter \*

.. _`rhashtable_walk_next.description`:

Description
-----------

Note that you must call rhashtable_walk_stop when you are finished
with the walk.

Returns the next object or NULL when the end of the table is reached.

Returns -EAGAIN if resize event occurred.  Note that the iterator
will rewind back to the beginning and you may continue to use it.

.. _`rhashtable_walk_peek`:

rhashtable_walk_peek
====================

.. c:function:: void *rhashtable_walk_peek(struct rhashtable_iter *iter)

    Return the next object but don't advance the iterator

    :param iter:
        Hash table iterator
    :type iter: struct rhashtable_iter \*

.. _`rhashtable_walk_peek.description`:

Description
-----------

Returns the next object or NULL when the end of the table is reached.

Returns -EAGAIN if resize event occurred.  Note that the iterator
will rewind back to the beginning and you may continue to use it.

.. _`rhashtable_walk_stop`:

rhashtable_walk_stop
====================

.. c:function:: void rhashtable_walk_stop(struct rhashtable_iter *iter)

    Finish a hash table walk

    :param iter:
        Hash table iterator
    :type iter: struct rhashtable_iter \*

.. _`rhashtable_walk_stop.description`:

Description
-----------

Finish a hash table walk.  Does not reset the iterator to the start of the
hash table.

.. _`rhashtable_init`:

rhashtable_init
===============

.. c:function:: int rhashtable_init(struct rhashtable *ht, const struct rhashtable_params *params)

    initialize a new hash table

    :param ht:
        hash table to be initialized
    :type ht: struct rhashtable \*

    :param params:
        configuration parameters
    :type params: const struct rhashtable_params \*

.. _`rhashtable_init.description`:

Description
-----------

Initializes a new hash table based on the provided configuration
parameters. A table can be configured either with a variable or

.. _`rhashtable_init.configuration-example-1`:

Configuration Example 1
-----------------------

Fixed length keys
struct test_obj {
int                     key;
void \*                  my_member;
struct rhash_head       node;
};

struct rhashtable_params params = {
.head_offset = offsetof(struct test_obj, node),
.key_offset = offsetof(struct test_obj, key),
.key_len = sizeof(int),
.hashfn = jhash,
};

.. _`rhashtable_init.configuration-example-2`:

Configuration Example 2
-----------------------

Variable length keys
struct test_obj {
[...]
struct rhash_head       node;
};

u32 my_hash_fn(const void \*data, u32 len, u32 seed)
{
struct test_obj \*obj = data;

return [... hash ...];
}

struct rhashtable_params params = {
.head_offset = offsetof(struct test_obj, node),
.hashfn = jhash,
.obj_hashfn = my_hash_fn,
};

.. _`rhltable_init`:

rhltable_init
=============

.. c:function:: int rhltable_init(struct rhltable *hlt, const struct rhashtable_params *params)

    initialize a new hash list table

    :param hlt:
        hash list table to be initialized
    :type hlt: struct rhltable \*

    :param params:
        configuration parameters
    :type params: const struct rhashtable_params \*

.. _`rhltable_init.description`:

Description
-----------

Initializes a new hash list table.

See documentation for rhashtable_init.

.. _`rhashtable_free_and_destroy`:

rhashtable_free_and_destroy
===========================

.. c:function:: void rhashtable_free_and_destroy(struct rhashtable *ht, void (*free_fn)(void *ptr, void *arg), void *arg)

    free elements and destroy hash table

    :param ht:
        the hash table to destroy
    :type ht: struct rhashtable \*

    :param void (\*free_fn)(void \*ptr, void \*arg):
        callback to release resources of element

    :param arg:
        pointer passed to free_fn
    :type arg: void \*

.. _`rhashtable_free_and_destroy.description`:

Description
-----------

Stops an eventual async resize. If defined, invokes free_fn for each
element to releasal resources. Please note that RCU protected
readers may still be accessing the elements. Releasing of resources
must occur in a compatible manner. Then frees the bucket array.

This function will eventually sleep to wait for an async resize
to complete. The caller is responsible that no further write operations
occurs in parallel.

.. This file was automatic generated / don't edit.

