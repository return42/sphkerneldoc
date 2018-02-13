.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/radix-tree.h

.. _`radix_tree_iter`:

struct radix_tree_iter
======================

.. c:type:: struct radix_tree_iter

    radix tree iterator state

.. _`radix_tree_iter.definition`:

Definition
----------

.. code-block:: c

    struct radix_tree_iter {
        unsigned long index;
        unsigned long next_index;
        unsigned long tags;
        struct radix_tree_node *node;
    #ifdef CONFIG_RADIX_TREE_MULTIORDER
        unsigned int shift;
    #endif
    }

.. _`radix_tree_iter.members`:

Members
-------

index
    index of current slot

next_index
    one beyond the last index for this chunk

tags
    bit-mask for tag-iterating

node
    node that contains current slot

shift
    shift for the node that holds our slots

.. _`radix_tree_iter.description`:

Description
-----------

This radix tree iterator works in terms of "chunks" of slots.  A chunk is a
subinterval of slots contained within one radix tree leaf node.  It is
described by a pointer to its first slot and a struct radix_tree_iter
which holds the chunk's position in the tree and its size.  For tagged
iteration radix_tree_iter also holds the slots' bit-mask for one chosen
radix tree tag.

.. _`radix_tree_deref_slot`:

radix_tree_deref_slot
=====================

.. c:function:: void *radix_tree_deref_slot(void __rcu **slot)

    tree synchronization

    :param void __rcu \*\*slot:
        *undescribed*

.. _`radix_tree_deref_slot.description`:

Description
-----------

The radix-tree API requires that users provide all synchronisation (with
specific exceptions, noted below).

Synchronization of access to the data items being stored in the tree, and
management of their lifetimes must be completely managed by API users.

For API usage, in general,
- any function \_modifying\_ the tree or tags (inserting or deleting
items, setting or clearing tags) must exclude other modifications, and
exclude any functions reading the tree.
- any function \_reading\_ the tree or tags (looking up items or tags,
gang lookups) must exclude modifications to the tree, but may occur
concurrently with other readers.

.. _`radix_tree_deref_slot.the-notable-exceptions-to-this-rule-are-the-following-functions`:

The notable exceptions to this rule are the following functions
---------------------------------------------------------------

\__radix_tree_lookup
radix_tree_lookup
radix_tree_lookup_slot
radix_tree_tag_get
radix_tree_gang_lookup
radix_tree_gang_lookup_slot
radix_tree_gang_lookup_tag
radix_tree_gang_lookup_tag_slot
radix_tree_tagged

The first 8 functions are able to be called locklessly, using RCU. The
caller must ensure calls to these functions are made within \ :c:func:`rcu_read_lock`\ 
regions. Other readers (lock-free or otherwise) and modifications may be
running concurrently.

It is still required that the caller manage the synchronization and lifetimes
of the items. So if RCU lock-free lookups are used, typically this would mean
that the items have their own locks, or are amenable to lock-free access; and
that the items are freed by RCU (or only freed after having been deleted from
the radix tree \*and\* a \ :c:func:`synchronize_rcu`\  grace period).

(Note, rcu_assign_pointer and rcu_dereference are not needed to control
access to data items when inserting into or looking up from the radix tree)

Note that the value returned by \ :c:func:`radix_tree_tag_get`\  may not be relied upon
if only the RCU read lock is held.  Functions to set/clear tags and to
delete nodes running concurrently with it may affect its result such that
two consecutive reads in the same locked section may return different
values.  If reliability is required, modification functions must also be
excluded from concurrency.

radix_tree_tagged is able to be called without locking or RCU.

.. _`radix_tree_deref_slot_protected`:

radix_tree_deref_slot_protected
===============================

.. c:function:: void *radix_tree_deref_slot_protected(void __rcu **slot, spinlock_t *treelock)

    dereference a slot with tree lock held

    :param void __rcu \*\*slot:
        slot pointer, returned by radix_tree_lookup_slot

    :param spinlock_t \*treelock:
        *undescribed*

.. _`radix_tree_deref_slot_protected.description`:

Description
-----------

Similar to radix_tree_deref_slot.  The caller does not hold the RCU read
lock but it must hold the tree lock to prevent parallel updates.

.. _`radix_tree_deref_slot_protected.return`:

Return
------

entry stored in that slot.

.. _`radix_tree_deref_retry`:

radix_tree_deref_retry
======================

.. c:function:: int radix_tree_deref_retry(void *arg)

    check radix_tree_deref_slot

    :param void \*arg:
        pointer returned by radix_tree_deref_slot

.. _`radix_tree_deref_retry.return`:

Return
------

0 if retry is not required, otherwise retry is required

radix_tree_deref_retry must be used with radix_tree_deref_slot.

.. _`radix_tree_exceptional_entry`:

radix_tree_exceptional_entry
============================

.. c:function:: int radix_tree_exceptional_entry(void *arg)

    radix_tree_deref_slot gave exceptional entry?

    :param void \*arg:
        value returned by radix_tree_deref_slot

.. _`radix_tree_exceptional_entry.return`:

Return
------

0 if well-aligned pointer, non-0 if exceptional entry.

.. _`radix_tree_exception`:

radix_tree_exception
====================

.. c:function:: int radix_tree_exception(void *arg)

    radix_tree_deref_slot returned either exception?

    :param void \*arg:
        value returned by radix_tree_deref_slot

.. _`radix_tree_exception.return`:

Return
------

0 if well-aligned pointer, non-0 if either kind of exception.

.. _`radix_tree_iter_init`:

radix_tree_iter_init
====================

.. c:function:: void __rcu **radix_tree_iter_init(struct radix_tree_iter *iter, unsigned long start)

    initialize radix tree iterator

    :param struct radix_tree_iter \*iter:
        pointer to iterator state

    :param unsigned long start:
        iteration starting index

.. _`radix_tree_iter_init.return`:

Return
------

NULL

.. _`radix_tree_next_chunk`:

radix_tree_next_chunk
=====================

.. c:function:: void __rcu **radix_tree_next_chunk(const struct radix_tree_root *, struct radix_tree_iter *iter, unsigned flags)

    find next chunk of slots for iteration

    :param const struct radix_tree_root \*:
        *undescribed*

    :param struct radix_tree_iter \*iter:
        iterator state

    :param unsigned flags:
        RADIX_TREE_ITER\_\* flags and tag index

.. _`radix_tree_next_chunk.return`:

Return
------

pointer to chunk first slot, or NULL if there no more left

This function looks up the next chunk in the radix tree starting from
\ ``iter``\ ->next_index.  It returns a pointer to the chunk's first slot.
Also it fills \ ``iter``\  with data about chunk: position in the tree (index),
its end (next_index), and constructs a bit mask for tagged iterating (tags).

.. _`radix_tree_iter_lookup`:

radix_tree_iter_lookup
======================

.. c:function:: void __rcu **radix_tree_iter_lookup(const struct radix_tree_root *root, struct radix_tree_iter *iter, unsigned long index)

    look up an index in the radix tree

    :param const struct radix_tree_root \*root:
        radix tree root

    :param struct radix_tree_iter \*iter:
        iterator state

    :param unsigned long index:
        key to look up

.. _`radix_tree_iter_lookup.description`:

Description
-----------

If \ ``index``\  is present in the radix tree, this function returns the slot
containing it and updates \ ``iter``\  to describe the entry.  If \ ``index``\  is not
present, it returns NULL.

.. _`radix_tree_iter_find`:

radix_tree_iter_find
====================

.. c:function:: void __rcu **radix_tree_iter_find(const struct radix_tree_root *root, struct radix_tree_iter *iter, unsigned long index)

    find a present entry

    :param const struct radix_tree_root \*root:
        radix tree root

    :param struct radix_tree_iter \*iter:
        iterator state

    :param unsigned long index:
        start location

.. _`radix_tree_iter_find.description`:

Description
-----------

This function returns the slot containing the entry with the lowest index
which is at least \ ``index``\ .  If \ ``index``\  is larger than any present entry, this
function returns NULL.  The \ ``iter``\  is updated to describe the entry found.

.. _`radix_tree_iter_retry`:

radix_tree_iter_retry
=====================

.. c:function:: void __rcu **radix_tree_iter_retry(struct radix_tree_iter *iter)

    retry this chunk of the iteration

    :param struct radix_tree_iter \*iter:
        iterator state

.. _`radix_tree_iter_retry.description`:

Description
-----------

If we iterate over a tree protected only by the RCU lock, a race
against deletion or creation may result in seeing a slot for which
\ :c:func:`radix_tree_deref_retry`\  returns true.  If so, call this function
and continue the iteration.

.. _`radix_tree_iter_resume`:

radix_tree_iter_resume
======================

.. c:function:: void __rcu **radix_tree_iter_resume(void __rcu **slot, struct radix_tree_iter *iter)

    resume iterating when the chunk may be invalid

    :param void __rcu \*\*slot:
        pointer to current slot

    :param struct radix_tree_iter \*iter:
        iterator state

.. _`radix_tree_iter_resume.return`:

Return
------

New slot pointer

If the iterator needs to release then reacquire a lock, the chunk may
have been invalidated by an insertion or deletion.  Call this function
before releasing the lock to continue the iteration from the next index.

.. _`radix_tree_chunk_size`:

radix_tree_chunk_size
=====================

.. c:function:: long radix_tree_chunk_size(struct radix_tree_iter *iter)

    get current chunk size

    :param struct radix_tree_iter \*iter:
        pointer to radix tree iterator

.. _`radix_tree_chunk_size.return`:

Return
------

current chunk size

.. _`radix_tree_next_slot`:

radix_tree_next_slot
====================

.. c:function:: void __rcu **radix_tree_next_slot(void __rcu **slot, struct radix_tree_iter *iter, unsigned flags)

    find next slot in chunk

    :param void __rcu \*\*slot:
        pointer to current slot

    :param struct radix_tree_iter \*iter:
        pointer to interator state

    :param unsigned flags:
        RADIX_TREE_ITER\_\*, should be constant

.. _`radix_tree_next_slot.return`:

Return
------

pointer to next slot, or NULL if there no more left

This function updates \ ``iter``\ ->index in the case of a successful lookup.
For tagged lookup it also eats \ ``iter``\ ->tags.

There are several cases where 'slot' can be passed in as NULL to this
function.  These cases result from the use of \ :c:func:`radix_tree_iter_resume`\  or
\ :c:func:`radix_tree_iter_retry`\ .  In these cases we don't end up dereferencing
'slot' because either:
a) we are doing tagged iteration and iter->tags has been set to 0, or
b) we are doing non-tagged iteration, and iter->index and iter->next_index
have been set up so that \ :c:func:`radix_tree_chunk_size`\  returns 1 or 0.

.. _`radix_tree_for_each_slot`:

radix_tree_for_each_slot
========================

.. c:function::  radix_tree_for_each_slot( slot,  root,  iter,  start)

    iterate over non-empty slots

    :param  slot:
        the void\*\* variable for pointer to slot

    :param  root:
        the struct radix_tree_root pointer

    :param  iter:
        the struct radix_tree_iter pointer

    :param  start:
        iteration starting index

.. _`radix_tree_for_each_slot.description`:

Description
-----------

\ ``slot``\  points to radix tree slot, \ ``iter``\ ->index contains its index.

.. _`radix_tree_for_each_contig`:

radix_tree_for_each_contig
==========================

.. c:function::  radix_tree_for_each_contig( slot,  root,  iter,  start)

    iterate over contiguous slots

    :param  slot:
        the void\*\* variable for pointer to slot

    :param  root:
        the struct radix_tree_root pointer

    :param  iter:
        the struct radix_tree_iter pointer

    :param  start:
        iteration starting index

.. _`radix_tree_for_each_contig.description`:

Description
-----------

\ ``slot``\  points to radix tree slot, \ ``iter``\ ->index contains its index.

.. _`radix_tree_for_each_tagged`:

radix_tree_for_each_tagged
==========================

.. c:function::  radix_tree_for_each_tagged( slot,  root,  iter,  start,  tag)

    iterate over tagged slots

    :param  slot:
        the void\*\* variable for pointer to slot

    :param  root:
        the struct radix_tree_root pointer

    :param  iter:
        the struct radix_tree_iter pointer

    :param  start:
        iteration starting index

    :param  tag:
        tag index

.. _`radix_tree_for_each_tagged.description`:

Description
-----------

\ ``slot``\  points to radix tree slot, \ ``iter``\ ->index contains its index.

.. This file was automatic generated / don't edit.

