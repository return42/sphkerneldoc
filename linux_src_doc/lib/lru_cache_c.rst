.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/lru_cache.c

.. _`lc_create`:

lc_create
=========

.. c:function:: struct lru_cache *lc_create(const char *name, struct kmem_cache *cache, unsigned max_pending_changes, unsigned e_count, size_t e_size, size_t e_off)

    prepares to track objects in an active set

    :param const char \*name:
        descriptive name only used in lc_seq_printf_stats and lc_seq_dump_details

    :param struct kmem_cache \*cache:
        *undescribed*

    :param unsigned max_pending_changes:
        maximum changes to accumulate until a transaction is required

    :param unsigned e_count:
        number of elements allowed to be active simultaneously

    :param size_t e_size:
        size of the tracked objects

    :param size_t e_off:
        offset to the \ :c:type:`struct lc_element <lc_element>`\  member in a tracked object

.. _`lc_create.description`:

Description
-----------

Returns a pointer to a newly initialized struct lru_cache on success,
or NULL on (allocation) failure.

.. _`lc_destroy`:

lc_destroy
==========

.. c:function:: void lc_destroy(struct lru_cache *lc)

    frees memory allocated by \ :c:func:`lc_create`\ 

    :param struct lru_cache \*lc:
        the lru cache to destroy

.. _`lc_reset`:

lc_reset
========

.. c:function:: void lc_reset(struct lru_cache *lc)

    does a full reset for \ ``lc``\  and the hash table slots.

    :param struct lru_cache \*lc:
        the lru cache to operate on

.. _`lc_reset.description`:

Description
-----------

It is roughly the equivalent of re-allocating a fresh lru_cache object,
basically a short cut to lc_destroy(lc); lc = lc_create(...);

.. _`lc_seq_printf_stats`:

lc_seq_printf_stats
===================

.. c:function:: void lc_seq_printf_stats(struct seq_file *seq, struct lru_cache *lc)

    print stats about \ ``lc``\  into \ ``seq``\ 

    :param struct seq_file \*seq:
        the seq_file to print into

    :param struct lru_cache \*lc:
        the lru cache to print statistics of

.. _`lc_find`:

lc_find
=======

.. c:function:: struct lc_element *lc_find(struct lru_cache *lc, unsigned int enr)

    find element by label, if present in the hash table

    :param struct lru_cache \*lc:
        The lru_cache object

    :param unsigned int enr:
        element number

.. _`lc_find.description`:

Description
-----------

Returns the pointer to an element, if the element with the requested
"label" or element number is present in the hash table,
or NULL if not found. Does not change the refcnt.
Ignores elements that are "about to be used", i.e. not yet in the active
set, but still pending transaction commit.

.. _`lc_is_used`:

lc_is_used
==========

.. c:function:: bool lc_is_used(struct lru_cache *lc, unsigned int enr)

    find element by label

    :param struct lru_cache \*lc:
        The lru_cache object

    :param unsigned int enr:
        element number

.. _`lc_is_used.description`:

Description
-----------

Returns true, if the element with the requested "label" or element number is
present in the hash table, and is used (refcnt > 0).
Also finds elements that are not \_currently\_ used but only "about to be
used", i.e. on the "to_be_changed" list, pending transaction commit.

.. _`lc_del`:

lc_del
======

.. c:function:: void lc_del(struct lru_cache *lc, struct lc_element *e)

    removes an element from the cache

    :param struct lru_cache \*lc:
        The lru_cache object

    :param struct lc_element \*e:
        The element to remove

.. _`lc_del.description`:

Description
-----------

\ ``e``\  must be unused (refcnt == 0). Moves \ ``e``\  from "lru" to "free" list,
sets \ ``e``\ ->enr to \ ``LC_FREE``\ .

.. _`lc_get`:

lc_get
======

.. c:function:: struct lc_element *lc_get(struct lru_cache *lc, unsigned int enr)

    get element by label, maybe change the active set

    :param struct lru_cache \*lc:
        the lru cache to operate on

    :param unsigned int enr:
        the label to look up

.. _`lc_get.description`:

Description
-----------

Finds an element in the cache, increases its usage count,
"touches" and returns it.

In case the requested number is not present, it needs to be added to the
cache. Therefore it is possible that an other element becomes evicted from
the cache. In either case, the user is notified so he is able to e.g. keep
a persistent log of the cache changes, and therefore the objects in use.

.. _`lc_get.return-values`:

Return values
-------------

NULL
The cache was marked \ ``LC_STARVING``\ ,
or the requested label was not in the active set
and a changing transaction is still pending (@lc was marked \ ``LC_DIRTY``\ ).
Or no unused or free element could be recycled (@lc will be marked as
\ ``LC_STARVING``\ , blocking further \ :c:func:`lc_get`\  operations).

pointer to the element with the REQUESTED element number.
In this case, it can be used right away

pointer to an UNUSED element with some different element number,
where that different number may also be \ ``LC_FREE``\ .

In this case, the cache is marked \ ``LC_DIRTY``\ ,
so \ :c:func:`lc_try_lock`\  will no longer succeed.
The returned element pointer is moved to the "to_be_changed" list,
and registered with the new element number on the hash collision chains,
so it is possible to pick it up from \ :c:func:`lc_is_used`\ .
Up to "max_pending_changes" (see \ :c:func:`lc_create`\ ) can be accumulated.
The user now should do whatever housekeeping is necessary,
typically serialize on \ :c:func:`lc_try_lock_for_transaction`\ , then call
lc_committed(lc) and \ :c:func:`lc_unlock`\ , to finish the change.

.. _`lc_get.note`:

NOTE
----

The user needs to check the lc_number on EACH use, so he recognizes
any cache set change.

.. _`lc_get_cumulative`:

lc_get_cumulative
=================

.. c:function:: struct lc_element *lc_get_cumulative(struct lru_cache *lc, unsigned int enr)

    like lc_get; also finds to-be-changed elements

    :param struct lru_cache \*lc:
        the lru cache to operate on

    :param unsigned int enr:
        the label to look up

.. _`lc_get_cumulative.description`:

Description
-----------

Unlike lc_get this also returns the element for \ ``enr``\ , if it is belonging to
a pending transaction, so the return values are like for \ :c:func:`lc_get`\ ,

.. _`lc_get_cumulative.plus`:

plus
----


pointer to an element already on the "to_be_changed" list.
In this case, the cache was already marked \ ``LC_DIRTY``\ .

Caller needs to make sure that the pending transaction is completed,
before proceeding to actually use this element.

.. _`lc_try_get`:

lc_try_get
==========

.. c:function:: struct lc_element *lc_try_get(struct lru_cache *lc, unsigned int enr)

    get element by label, if present; do not change the active set

    :param struct lru_cache \*lc:
        the lru cache to operate on

    :param unsigned int enr:
        the label to look up

.. _`lc_try_get.description`:

Description
-----------

Finds an element in the cache, increases its usage count,
"touches" and returns it.

.. _`lc_try_get.return-values`:

Return values
-------------

NULL
The cache was marked \ ``LC_STARVING``\ ,
or the requested label was not in the active set

pointer to the element with the REQUESTED element number.
In this case, it can be used right away

.. _`lc_committed`:

lc_committed
============

.. c:function:: void lc_committed(struct lru_cache *lc)

    tell \ ``lc``\  that pending changes have been recorded

    :param struct lru_cache \*lc:
        the lru cache to operate on

.. _`lc_committed.description`:

Description
-----------

User is expected to serialize on explicit \ :c:func:`lc_try_lock_for_transaction`\ 
before the transaction is started, and later needs to \ :c:func:`lc_unlock`\  explicitly
as well.

.. _`lc_put`:

lc_put
======

.. c:function:: unsigned int lc_put(struct lru_cache *lc, struct lc_element *e)

    give up refcnt of \ ``e``\ 

    :param struct lru_cache \*lc:
        the lru cache to operate on

    :param struct lc_element \*e:
        the element to put

.. _`lc_put.description`:

Description
-----------

If refcnt reaches zero, the element is moved to the lru list,
and a \ ``LC_STARVING``\  (if set) is cleared.
Returns the new (post-decrement) refcnt.

.. _`lc_element_by_index`:

lc_element_by_index
===================

.. c:function:: struct lc_element *lc_element_by_index(struct lru_cache *lc, unsigned i)

    :param struct lru_cache \*lc:
        the lru cache to operate on

    :param unsigned i:
        the index of the element to return

.. _`lc_index_of`:

lc_index_of
===========

.. c:function:: unsigned int lc_index_of(struct lru_cache *lc, struct lc_element *e)

    :param struct lru_cache \*lc:
        the lru cache to operate on

    :param struct lc_element \*e:
        the element to query for its index position in lc->element

.. _`lc_set`:

lc_set
======

.. c:function:: void lc_set(struct lru_cache *lc, unsigned int enr, int index)

    associate index with label

    :param struct lru_cache \*lc:
        the lru cache to operate on

    :param unsigned int enr:
        the label to set

    :param int index:
        the element index to associate label with.

.. _`lc_set.description`:

Description
-----------

Used to initialize the active set to some previously recorded state.

.. _`lc_seq_dump_details`:

lc_seq_dump_details
===================

.. c:function:: void lc_seq_dump_details(struct seq_file *seq, struct lru_cache *lc, char *utext, void (*detail)(struct seq_file *, struct lc_element *))

    Dump a complete LRU cache to seq in textual form.

    :param struct seq_file \*seq:
        the \ :c:type:`struct seq_file <seq_file>`\  pointer to seq_printf into

    :param struct lru_cache \*lc:
        the lru cache to operate on

    :param char \*utext:
        user supplied additional "heading" or other info

    :param void (\*detail)(struct seq_file \*, struct lc_element \*):
        function pointer the user may provide to dump further details
        of the object the lc_element is embedded in. May be NULL.

.. _`lc_seq_dump_details.note`:

Note
----

a leading space ' ' and trailing newline '\n' is implied.

.. This file was automatic generated / don't edit.

