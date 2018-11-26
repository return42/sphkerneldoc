.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/radix-tree.c

.. _`radix_tree_find_next_bit`:

radix_tree_find_next_bit
========================

.. c:function:: unsigned long radix_tree_find_next_bit(struct radix_tree_node *node, unsigned int tag, unsigned long offset)

    find the next set bit in a memory region

    :param node:
        *undescribed*
    :type node: struct radix_tree_node \*

    :param tag:
        *undescribed*
    :type tag: unsigned int

    :param offset:
        The bitnumber to start searching at
    :type offset: unsigned long

.. _`radix_tree_find_next_bit.description`:

Description
-----------

Unrollable variant of \ :c:func:`find_next_bit`\  for constant size arrays.
Tail bits starting from size to roundup(size, BITS_PER_LONG) must be zero.
Returns next bit offset, or size if nothing found.

.. _`radix_tree_shrink`:

radix_tree_shrink
=================

.. c:function:: bool radix_tree_shrink(struct radix_tree_root *root)

    shrink radix tree to minimum height \ ``root``\            radix tree root

    :param root:
        *undescribed*
    :type root: struct radix_tree_root \*

.. _`__radix_tree_create`:

\__radix_tree_create
====================

.. c:function:: int __radix_tree_create(struct radix_tree_root *root, unsigned long index, struct radix_tree_node **nodep, void __rcu ***slotp)

    create a slot in a radix tree

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

    :param nodep:
        returns node
    :type nodep: struct radix_tree_node \*\*

    :param slotp:
        returns slot
    :type slotp: void __rcu \*\*\*

.. _`__radix_tree_create.description`:

Description
-----------

Create, if necessary, and return the node and slot for an item
at position \ ``index``\  in the radix tree \ ``root``\ .

Until there is more than one item in the tree, no nodes are
allocated and \ ``root->xa_head``\  is used as a direct slot instead of
pointing to a node, in which case \*@nodep will be NULL.

Returns -ENOMEM, or 0 for success.

.. _`radix_tree_insert`:

radix_tree_insert
=================

.. c:function:: int radix_tree_insert(struct radix_tree_root *root, unsigned long index, void *item)

    insert into a radix tree

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

    :param item:
        item to insert
    :type item: void \*

.. _`radix_tree_insert.description`:

Description
-----------

Insert an item into the radix tree at position \ ``index``\ .

.. _`__radix_tree_lookup`:

\__radix_tree_lookup
====================

.. c:function:: void *__radix_tree_lookup(const struct radix_tree_root *root, unsigned long index, struct radix_tree_node **nodep, void __rcu ***slotp)

    lookup an item in a radix tree

    :param root:
        radix tree root
    :type root: const struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

    :param nodep:
        returns node
    :type nodep: struct radix_tree_node \*\*

    :param slotp:
        returns slot
    :type slotp: void __rcu \*\*\*

.. _`__radix_tree_lookup.description`:

Description
-----------

Lookup and return the item at position \ ``index``\  in the radix
tree \ ``root``\ .

Until there is more than one item in the tree, no nodes are
allocated and \ ``root->xa_head``\  is used as a direct slot instead of
pointing to a node, in which case \*@nodep will be NULL.

.. _`radix_tree_lookup_slot`:

radix_tree_lookup_slot
======================

.. c:function:: void __rcu **radix_tree_lookup_slot(const struct radix_tree_root *root, unsigned long index)

    lookup a slot in a radix tree

    :param root:
        radix tree root
    :type root: const struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

.. _`radix_tree_lookup_slot.return`:

Return
------

the slot corresponding to the position \ ``index``\  in the
radix tree \ ``root``\ . This is useful for update-if-exists operations.

This function can be called under rcu_read_lock iff the slot is not
modified by radix_tree_replace_slot, otherwise it must be called
exclusive from other writers. Any dereference of the slot must be done
using radix_tree_deref_slot.

.. _`radix_tree_lookup`:

radix_tree_lookup
=================

.. c:function:: void *radix_tree_lookup(const struct radix_tree_root *root, unsigned long index)

    perform lookup operation on a radix tree

    :param root:
        radix tree root
    :type root: const struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

.. _`radix_tree_lookup.description`:

Description
-----------

Lookup the item at the position \ ``index``\  in the radix tree \ ``root``\ .

This function can be called under rcu_read_lock, however the caller
must manage lifetimes of leaf nodes (eg. RCU may also be used to free
them safely). No RCU barriers are required to access or modify the
returned item, however.

.. _`__radix_tree_replace`:

\__radix_tree_replace
=====================

.. c:function:: void __radix_tree_replace(struct radix_tree_root *root, struct radix_tree_node *node, void __rcu **slot, void *item)

    replace item in a slot

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param node:
        pointer to tree node
    :type node: struct radix_tree_node \*

    :param slot:
        pointer to slot in \ ``node``\ 
    :type slot: void __rcu \*\*

    :param item:
        new item to store in the slot.
    :type item: void \*

.. _`__radix_tree_replace.description`:

Description
-----------

For use with \__radix_tree_lookup().  Caller must hold tree write locked
across slot lookup and replacement.

.. _`radix_tree_replace_slot`:

radix_tree_replace_slot
=======================

.. c:function:: void radix_tree_replace_slot(struct radix_tree_root *root, void __rcu **slot, void *item)

    replace item in a slot

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param slot:
        pointer to slot
    :type slot: void __rcu \*\*

    :param item:
        new item to store in the slot.
    :type item: void \*

.. _`radix_tree_replace_slot.description`:

Description
-----------

For use with \ :c:func:`radix_tree_lookup_slot`\  and
\ :c:func:`radix_tree_gang_lookup_tag_slot`\ .  Caller must hold tree write locked
across slot lookup and replacement.

.. _`radix_tree_replace_slot.note`:

NOTE
----

This cannot be used to switch between non-entries (empty slots),
regular entries, and value entries, as that requires accounting
inside the radix tree node. When switching from one type of entry or
deleting, use \__radix_tree_lookup() and \__radix_tree_replace() or
\ :c:func:`radix_tree_iter_replace`\ .

.. _`radix_tree_iter_replace`:

radix_tree_iter_replace
=======================

.. c:function:: void radix_tree_iter_replace(struct radix_tree_root *root, const struct radix_tree_iter *iter, void __rcu **slot, void *item)

    replace item in a slot

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param iter:
        *undescribed*
    :type iter: const struct radix_tree_iter \*

    :param slot:
        pointer to slot
    :type slot: void __rcu \*\*

    :param item:
        new item to store in the slot.
    :type item: void \*

.. _`radix_tree_iter_replace.description`:

Description
-----------

For use with \ :c:func:`radix_tree_for_each_slot`\ .
Caller must hold tree write locked.

.. _`radix_tree_tag_set`:

radix_tree_tag_set
==================

.. c:function:: void *radix_tree_tag_set(struct radix_tree_root *root, unsigned long index, unsigned int tag)

    set a tag on a radix tree node

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

    :param tag:
        tag index
    :type tag: unsigned int

.. _`radix_tree_tag_set.description`:

Description
-----------

Set the search tag (which must be < RADIX_TREE_MAX_TAGS)
corresponding to \ ``index``\  in the radix tree.  From
the root all the way down to the leaf node.

Returns the address of the tagged item.  Setting a tag on a not-present
item is a bug.

.. _`radix_tree_tag_clear`:

radix_tree_tag_clear
====================

.. c:function:: void *radix_tree_tag_clear(struct radix_tree_root *root, unsigned long index, unsigned int tag)

    clear a tag on a radix tree node

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

    :param tag:
        tag index
    :type tag: unsigned int

.. _`radix_tree_tag_clear.description`:

Description
-----------

Clear the search tag (which must be < RADIX_TREE_MAX_TAGS)
corresponding to \ ``index``\  in the radix tree.  If this causes
the leaf node to have no tags set then clear the tag in the
next-to-leaf node, etc.

Returns the address of the tagged item on success, else NULL.  ie:
has the same return value and semantics as \ :c:func:`radix_tree_lookup`\ .

.. _`radix_tree_iter_tag_clear`:

radix_tree_iter_tag_clear
=========================

.. c:function:: void radix_tree_iter_tag_clear(struct radix_tree_root *root, const struct radix_tree_iter *iter, unsigned int tag)

    clear a tag on the current iterator entry

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param iter:
        iterator state
    :type iter: const struct radix_tree_iter \*

    :param tag:
        tag to clear
    :type tag: unsigned int

.. _`radix_tree_tag_get`:

radix_tree_tag_get
==================

.. c:function:: int radix_tree_tag_get(const struct radix_tree_root *root, unsigned long index, unsigned int tag)

    get a tag on a radix tree node

    :param root:
        radix tree root
    :type root: const struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

    :param tag:
        tag index (< RADIX_TREE_MAX_TAGS)
    :type tag: unsigned int

.. _`radix_tree_tag_get.return-values`:

Return values
-------------


0: tag not present or not set
1: tag set

Note that the return value of this function may not be relied on, even if
the RCU lock is held, unless tag modification and node deletion are excluded
from concurrency.

.. _`radix_tree_next_chunk`:

radix_tree_next_chunk
=====================

.. c:function:: void __rcu **radix_tree_next_chunk(const struct radix_tree_root *root, struct radix_tree_iter *iter, unsigned flags)

    find next chunk of slots for iteration

    :param root:
        radix tree root
    :type root: const struct radix_tree_root \*

    :param iter:
        iterator state
    :type iter: struct radix_tree_iter \*

    :param flags:
        RADIX_TREE_ITER\_\* flags and tag index
    :type flags: unsigned

.. _`radix_tree_next_chunk.return`:

Return
------

pointer to chunk first slot, or NULL if iteration is over

.. _`radix_tree_gang_lookup`:

radix_tree_gang_lookup
======================

.. c:function:: unsigned int radix_tree_gang_lookup(const struct radix_tree_root *root, void **results, unsigned long first_index, unsigned int max_items)

    perform multiple lookup on a radix tree

    :param root:
        radix tree root
    :type root: const struct radix_tree_root \*

    :param results:
        where the results of the lookup are placed
    :type results: void \*\*

    :param first_index:
        start the lookup from this key
    :type first_index: unsigned long

    :param max_items:
        place up to this many items at \*results
    :type max_items: unsigned int

.. _`radix_tree_gang_lookup.description`:

Description
-----------

Performs an index-ascending scan of the tree for present items.  Places
them at \*@results and returns the number of items which were placed at
\*@results.

The implementation is naive.

Like radix_tree_lookup, radix_tree_gang_lookup may be called under
rcu_read_lock. In this case, rather than the returned results being
an atomic snapshot of the tree at a single point in time, the
semantics of an RCU protected gang lookup are as though multiple
radix_tree_lookups have been issued in individual locks, and results
stored in 'results'.

.. _`radix_tree_gang_lookup_tag`:

radix_tree_gang_lookup_tag
==========================

.. c:function:: unsigned int radix_tree_gang_lookup_tag(const struct radix_tree_root *root, void **results, unsigned long first_index, unsigned int max_items, unsigned int tag)

    perform multiple lookup on a radix tree based on a tag

    :param root:
        radix tree root
    :type root: const struct radix_tree_root \*

    :param results:
        where the results of the lookup are placed
    :type results: void \*\*

    :param first_index:
        start the lookup from this key
    :type first_index: unsigned long

    :param max_items:
        place up to this many items at \*results
    :type max_items: unsigned int

    :param tag:
        the tag index (< RADIX_TREE_MAX_TAGS)
    :type tag: unsigned int

.. _`radix_tree_gang_lookup_tag.description`:

Description
-----------

Performs an index-ascending scan of the tree for present items which
have the tag indexed by \ ``tag``\  set.  Places the items at \*@results and
returns the number of items which were placed at \*@results.

.. _`radix_tree_gang_lookup_tag_slot`:

radix_tree_gang_lookup_tag_slot
===============================

.. c:function:: unsigned int radix_tree_gang_lookup_tag_slot(const struct radix_tree_root *root, void __rcu ***results, unsigned long first_index, unsigned int max_items, unsigned int tag)

    perform multiple slot lookup on a radix tree based on a tag

    :param root:
        radix tree root
    :type root: const struct radix_tree_root \*

    :param results:
        where the results of the lookup are placed
    :type results: void __rcu \*\*\*

    :param first_index:
        start the lookup from this key
    :type first_index: unsigned long

    :param max_items:
        place up to this many items at \*results
    :type max_items: unsigned int

    :param tag:
        the tag index (< RADIX_TREE_MAX_TAGS)
    :type tag: unsigned int

.. _`radix_tree_gang_lookup_tag_slot.description`:

Description
-----------

Performs an index-ascending scan of the tree for present items which
have the tag indexed by \ ``tag``\  set.  Places the slots at \*@results and
returns the number of slots which were placed at \*@results.

.. _`radix_tree_iter_delete`:

radix_tree_iter_delete
======================

.. c:function:: void radix_tree_iter_delete(struct radix_tree_root *root, struct radix_tree_iter *iter, void __rcu **slot)

    delete the entry at this iterator position

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param iter:
        iterator state
    :type iter: struct radix_tree_iter \*

    :param slot:
        pointer to slot
    :type slot: void __rcu \*\*

.. _`radix_tree_iter_delete.description`:

Description
-----------

Delete the entry at the position currently pointed to by the iterator.
This may result in the current node being freed; if it is, the iterator
is advanced so that it will not reference the freed memory.  This
function may be called without any locking if there are no other threads
which can access this tree.

.. _`radix_tree_delete_item`:

radix_tree_delete_item
======================

.. c:function:: void *radix_tree_delete_item(struct radix_tree_root *root, unsigned long index, void *item)

    delete an item from a radix tree

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

    :param item:
        expected item
    :type item: void \*

.. _`radix_tree_delete_item.description`:

Description
-----------

Remove \ ``item``\  at \ ``index``\  from the radix tree rooted at \ ``root``\ .

.. _`radix_tree_delete_item.return`:

Return
------

the deleted entry, or \ ``NULL``\  if it was not present
or the entry at the given \ ``index``\  was not \ ``item``\ .

.. _`radix_tree_delete`:

radix_tree_delete
=================

.. c:function:: void *radix_tree_delete(struct radix_tree_root *root, unsigned long index)

    delete an entry from a radix tree

    :param root:
        radix tree root
    :type root: struct radix_tree_root \*

    :param index:
        index key
    :type index: unsigned long

.. _`radix_tree_delete.description`:

Description
-----------

Remove the entry at \ ``index``\  from the radix tree rooted at \ ``root``\ .

.. _`radix_tree_delete.return`:

Return
------

The deleted entry, or \ ``NULL``\  if it was not present.

.. _`radix_tree_tagged`:

radix_tree_tagged
=================

.. c:function:: int radix_tree_tagged(const struct radix_tree_root *root, unsigned int tag)

    test whether any items in the tree are tagged

    :param root:
        radix tree root
    :type root: const struct radix_tree_root \*

    :param tag:
        tag to test
    :type tag: unsigned int

.. _`idr_preload`:

idr_preload
===========

.. c:function:: void idr_preload(gfp_t gfp_mask)

    preload for \ :c:func:`idr_alloc`\ 

    :param gfp_mask:
        allocation mask to use for preloading
    :type gfp_mask: gfp_t

.. _`idr_preload.description`:

Description
-----------

Preallocate memory to use for the next call to \ :c:func:`idr_alloc`\ .  This function
returns with preemption disabled.  It will be enabled by \ :c:func:`idr_preload_end`\ .

.. _`idr_destroy`:

idr_destroy
===========

.. c:function:: void idr_destroy(struct idr *idr)

    release all internal memory from an IDR

    :param idr:
        idr handle
    :type idr: struct idr \*

.. _`idr_destroy.description`:

Description
-----------

After this function is called, the IDR is empty, and may be reused or
the data structure containing it may be freed.

A typical clean-up sequence for objects stored in an idr tree will use
\ :c:func:`idr_for_each`\  to free all objects, if necessary, then \ :c:func:`idr_destroy`\  to
free the memory used to keep track of those objects.

.. This file was automatic generated / don't edit.

