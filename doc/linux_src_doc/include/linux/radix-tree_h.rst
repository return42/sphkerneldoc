.. -*- coding: utf-8; mode: rst -*-

============
radix-tree.h
============


.. _`radix_tree_deref_slot`:

radix_tree_deref_slot
=====================

.. c:function:: void *radix_tree_deref_slot (void **pslot)

    tree synchronization

    :param void \*\*pslot:

        *undescribed*



.. _`radix_tree_deref_slot.description`:

Description
-----------


The radix-tree API requires that users provide all synchronisation (with
specific exceptions, noted below).

Synchronization of access to the data items being stored in the tree, and
management of their lifetimes must be completely managed by API users.

For API usage, in general,
- any function _modifying_ the tree or tags (inserting or deleting

  items, setting or clearing tags) must exclude other modifications, and
  exclude any functions reading the tree.

- any function _reading_ the tree or tags (looking up items or tags,

  gang lookups) must exclude modifications to the tree, but may occur
  concurrently with other readers.



.. _`radix_tree_deref_slot.the-notable-exceptions-to-this-rule-are-the-following-functions`:

The notable exceptions to this rule are the following functions
---------------------------------------------------------------

__radix_tree_lookup
radix_tree_lookup
radix_tree_lookup_slot
radix_tree_tag_get
radix_tree_gang_lookup
radix_tree_gang_lookup_slot
radix_tree_gang_lookup_tag
radix_tree_gang_lookup_tag_slot
radix_tree_tagged

The first 8 functions are able to be called locklessly, using RCU. The
caller must ensure calls to these functions are made within :c:func:`rcu_read_lock`
regions. Other readers (lock-free or otherwise) and modifications may be
running concurrently.

It is still required that the caller manage the synchronization and lifetimes
of the items. So if RCU lock-free lookups are used, typically this would mean
that the items have their own locks, or are amenable to lock-free access; and
that the items are freed by RCU (or only freed after having been deleted from
the radix tree \*and\* a :c:func:`synchronize_rcu` grace period).

(Note, rcu_assign_pointer and rcu_dereference are not needed to control
access to data items when inserting into or looking up from the radix tree)

Note that the value returned by :c:func:`radix_tree_tag_get` may not be relied upon
if only the RCU read lock is held.  Functions to set/clear tags and to
delete nodes running concurrently with it may affect its result such that
two consecutive reads in the same locked section may return different
values.  If reliability is required, modification functions must also be
excluded from concurrency.

radix_tree_tagged is able to be called without locking or RCU.



.. _`radix_tree_deref_slot_protected`:

radix_tree_deref_slot_protected
===============================

.. c:function:: void *radix_tree_deref_slot_protected (void **pslot, spinlock_t *treelock)

    dereference a slot without RCU lock but with tree lock held

    :param void \*\*pslot:
        pointer to slot, returned by radix_tree_lookup_slot

    :param spinlock_t \*treelock:

        *undescribed*



.. _`radix_tree_deref_slot_protected.returns`:

Returns
-------

item that was stored in that slot with any direct pointer flag
removed.

Similar to radix_tree_deref_slot but only used during migration when a pages
mapping is being moved. The caller does not hold the RCU read lock but it
must hold the tree lock to prevent parallel updates.



.. _`radix_tree_deref_retry`:

radix_tree_deref_retry
======================

.. c:function:: int radix_tree_deref_retry (void *arg)

    check radix_tree_deref_slot

    :param void \*arg:
        pointer returned by radix_tree_deref_slot



.. _`radix_tree_deref_retry.returns`:

Returns
-------

0 if retry is not required, otherwise retry is required

radix_tree_deref_retry must be used with radix_tree_deref_slot.



.. _`radix_tree_exceptional_entry`:

radix_tree_exceptional_entry
============================

.. c:function:: int radix_tree_exceptional_entry (void *arg)

    radix_tree_deref_slot gave exceptional entry?

    :param void \*arg:
        value returned by radix_tree_deref_slot



.. _`radix_tree_exceptional_entry.returns`:

Returns
-------

0 if well-aligned pointer, non-0 if exceptional entry.



.. _`radix_tree_exception`:

radix_tree_exception
====================

.. c:function:: int radix_tree_exception (void *arg)

    radix_tree_deref_slot returned either exception?

    :param void \*arg:
        value returned by radix_tree_deref_slot



.. _`radix_tree_exception.returns`:

Returns
-------

0 if well-aligned pointer, non-0 if either kind of exception.



.. _`radix_tree_replace_slot`:

radix_tree_replace_slot
=======================

.. c:function:: void radix_tree_replace_slot (void **pslot, void *item)

    replace item in a slot

    :param void \*\*pslot:
        pointer to slot, returned by radix_tree_lookup_slot

    :param void \*item:
        new item to store in the slot.



.. _`radix_tree_replace_slot.description`:

Description
-----------

For use with :c:func:`radix_tree_lookup_slot`.  Caller must hold tree write locked
across slot lookup and replacement.



.. _`radix_tree_iter`:

struct radix_tree_iter
======================

.. c:type:: radix_tree_iter

    radix tree iterator state


.. _`radix_tree_iter.definition`:

Definition
----------

.. code-block:: c

  struct radix_tree_iter {
    unsigned long index;
    unsigned long next_index;
    unsigned long tags;
  };


.. _`radix_tree_iter.members`:

Members
-------

:``index``:
    index of current slot

:``next_index``:
    next-to-last index for this chunk

:``tags``:
    bit-mask for tag-iterating




.. _`radix_tree_iter.description`:

Description
-----------

This radix tree iterator works in terms of "chunks" of slots.  A chunk is a
subinterval of slots contained within one radix tree leaf node.  It is
described by a pointer to its first slot and a struct radix_tree_iter
which holds the chunk's position in the tree and its size.  For tagged
iteration radix_tree_iter also holds the slots' bit-mask for one chosen
radix tree tag.



.. _`radix_tree_chunk_size`:

radix_tree_chunk_size
=====================

.. c:function:: long radix_tree_chunk_size (struct radix_tree_iter *iter)

    get current chunk size

    :param struct radix_tree_iter \*iter:
        pointer to radix tree iterator



.. _`radix_tree_chunk_size.returns`:

Returns
-------

current chunk size



.. _`radix_tree_for_each_chunk`:

radix_tree_for_each_chunk
=========================

.. c:function:: radix_tree_for_each_chunk ( slot,  root,  iter,  start,  flags)

    iterate over chunks

    :param slot:
        the void** variable for pointer to chunk first slot

    :param root:
        the struct radix_tree_root pointer

    :param iter:
        the struct radix_tree_iter pointer

    :param start:
        iteration starting index

    :param flags:
        RADIX_TREE_ITER\_\* and tag index



.. _`radix_tree_for_each_chunk.description`:

Description
-----------

Locks can be released and reacquired between iterations.



.. _`radix_tree_for_each_chunk_slot`:

radix_tree_for_each_chunk_slot
==============================

.. c:function:: radix_tree_for_each_chunk_slot ( slot,  iter,  flags)

    iterate over slots in one chunk

    :param slot:
        the void** variable, at the beginning points to chunk first slot

    :param iter:
        the struct radix_tree_iter pointer

    :param flags:
        RADIX_TREE_ITER\_\*, should be constant



.. _`radix_tree_for_each_chunk_slot.description`:

Description
-----------

This macro is designed to be nested inside :c:func:`radix_tree_for_each_chunk`.
``slot`` points to the radix tree slot, ``iter``\ ->index contains its index.



.. _`radix_tree_for_each_slot`:

radix_tree_for_each_slot
========================

.. c:function:: radix_tree_for_each_slot ( slot,  root,  iter,  start)

    iterate over non-empty slots

    :param slot:
        the void** variable for pointer to slot

    :param root:
        the struct radix_tree_root pointer

    :param iter:
        the struct radix_tree_iter pointer

    :param start:
        iteration starting index



.. _`radix_tree_for_each_slot.description`:

Description
-----------

``slot`` points to radix tree slot, ``iter``\ ->index contains its index.



.. _`radix_tree_for_each_contig`:

radix_tree_for_each_contig
==========================

.. c:function:: radix_tree_for_each_contig ( slot,  root,  iter,  start)

    iterate over contiguous slots

    :param slot:
        the void** variable for pointer to slot

    :param root:
        the struct radix_tree_root pointer

    :param iter:
        the struct radix_tree_iter pointer

    :param start:
        iteration starting index



.. _`radix_tree_for_each_contig.description`:

Description
-----------

``slot`` points to radix tree slot, ``iter``\ ->index contains its index.



.. _`radix_tree_for_each_tagged`:

radix_tree_for_each_tagged
==========================

.. c:function:: radix_tree_for_each_tagged ( slot,  root,  iter,  start,  tag)

    iterate over tagged slots

    :param slot:
        the void** variable for pointer to slot

    :param root:
        the struct radix_tree_root pointer

    :param iter:
        the struct radix_tree_iter pointer

    :param start:
        iteration starting index

    :param tag:
        tag index



.. _`radix_tree_for_each_tagged.description`:

Description
-----------

``slot`` points to radix tree slot, ``iter``\ ->index contains its index.

