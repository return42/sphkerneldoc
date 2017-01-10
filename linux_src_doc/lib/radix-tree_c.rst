.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/radix-tree.c

.. _`radix_tree_find_next_bit`:

radix_tree_find_next_bit
========================

.. c:function:: unsigned long radix_tree_find_next_bit(struct radix_tree_node *node, unsigned int tag, unsigned long offset)

    find the next set bit in a memory region

    :param struct radix_tree_node \*node:
        *undescribed*

    :param unsigned int tag:
        *undescribed*

    :param unsigned long offset:
        The bitnumber to start searching at

.. _`radix_tree_find_next_bit.description`:

Description
-----------

Unrollable variant of \ :c:func:`find_next_bit`\  for constant size arrays.
Tail bits starting from size to roundup(size, BITS_PER_LONG) must be zero.
Returns next bit offset, or size if nothing found.

.. _`radix_tree_shrink`:

radix_tree_shrink
=================

.. c:function:: void radix_tree_shrink(struct radix_tree_root *root, radix_tree_update_node_t update_node, void *private)

    shrink radix tree to minimum height \ ``root``\            radix tree root

    :param struct radix_tree_root \*root:
        *undescribed*

    :param radix_tree_update_node_t update_node:
        *undescribed*

    :param void \*private:
        *undescribed*

.. _`__radix_tree_create`:

__radix_tree_create
===================

.. c:function:: int __radix_tree_create(struct radix_tree_root *root, unsigned long index, unsigned order, struct radix_tree_node **nodep, void ***slotp)

    create a slot in a radix tree

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        index key

    :param unsigned order:
        index occupies 2^order aligned slots

    :param struct radix_tree_node \*\*nodep:
        returns node

    :param void \*\*\*slotp:
        returns slot

.. _`__radix_tree_create.description`:

Description
-----------

Create, if necessary, and return the node and slot for an item
at position \ ``index``\  in the radix tree \ ``root``\ .

Until there is more than one item in the tree, no nodes are
allocated and \ ``root``\ ->rnode is used as a direct slot instead of
pointing to a node, in which case \*@nodep will be NULL.

Returns -ENOMEM, or 0 for success.

.. _`__radix_tree_insert`:

__radix_tree_insert
===================

.. c:function:: int __radix_tree_insert(struct radix_tree_root *root, unsigned long index, unsigned order, void *item)

    insert into a radix tree

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        index key

    :param unsigned order:
        key covers the 2^order indices around index

    :param void \*item:
        item to insert

.. _`__radix_tree_insert.description`:

Description
-----------

Insert an item into the radix tree at position \ ``index``\ .

.. _`__radix_tree_lookup`:

__radix_tree_lookup
===================

.. c:function:: void *__radix_tree_lookup(struct radix_tree_root *root, unsigned long index, struct radix_tree_node **nodep, void ***slotp)

    lookup an item in a radix tree

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        index key

    :param struct radix_tree_node \*\*nodep:
        returns node

    :param void \*\*\*slotp:
        returns slot

.. _`__radix_tree_lookup.description`:

Description
-----------

Lookup and return the item at position \ ``index``\  in the radix
tree \ ``root``\ .

Until there is more than one item in the tree, no nodes are
allocated and \ ``root``\ ->rnode is used as a direct slot instead of
pointing to a node, in which case \*@nodep will be NULL.

.. _`radix_tree_lookup`:

radix_tree_lookup
=================

.. c:function:: void *radix_tree_lookup(struct radix_tree_root *root, unsigned long index)

    perform lookup operation on a radix tree

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        index key

.. _`radix_tree_lookup.description`:

Description
-----------

Lookup the item at the position \ ``index``\  in the radix tree \ ``root``\ .

This function can be called under rcu_read_lock, however the caller
must manage lifetimes of leaf nodes (eg. RCU may also be used to free
them safely). No RCU barriers are required to access or modify the
returned item, however.

.. _`__radix_tree_replace`:

__radix_tree_replace
====================

.. c:function:: void __radix_tree_replace(struct radix_tree_root *root, struct radix_tree_node *node, void **slot, void *item, radix_tree_update_node_t update_node, void *private)

    replace item in a slot

    :param struct radix_tree_root \*root:
        radix tree root

    :param struct radix_tree_node \*node:
        pointer to tree node

    :param void \*\*slot:
        pointer to slot in \ ``node``\ 

    :param void \*item:
        new item to store in the slot.

    :param radix_tree_update_node_t update_node:
        callback for changing leaf nodes

    :param void \*private:
        private data to pass to \ ``update_node``\ 

.. _`__radix_tree_replace.description`:

Description
-----------

For use with \__radix_tree_lookup().  Caller must hold tree write locked
across slot lookup and replacement.

.. _`radix_tree_replace_slot`:

radix_tree_replace_slot
=======================

.. c:function:: void radix_tree_replace_slot(struct radix_tree_root *root, void **slot, void *item)

    replace item in a slot

    :param struct radix_tree_root \*root:
        radix tree root

    :param void \*\*slot:
        pointer to slot

    :param void \*item:
        new item to store in the slot.

.. _`radix_tree_replace_slot.description`:

Description
-----------

For use with \ :c:func:`radix_tree_lookup_slot`\ , \ :c:func:`radix_tree_gang_lookup_slot`\ ,
\ :c:func:`radix_tree_gang_lookup_tag_slot`\ .  Caller must hold tree write locked
across slot lookup and replacement.

.. _`radix_tree_replace_slot.note`:

NOTE
----

This cannot be used to switch between non-entries (empty slots),
regular entries, and exceptional entries, as that requires accounting
inside the radix tree node. When switching from one type of entry or
deleting, use \__radix_tree_lookup() and \__radix_tree_replace() or
\ :c:func:`radix_tree_iter_replace`\ .

.. _`radix_tree_iter_replace`:

radix_tree_iter_replace
=======================

.. c:function:: void radix_tree_iter_replace(struct radix_tree_root *root, const struct radix_tree_iter *iter, void **slot, void *item)

    replace item in a slot

    :param struct radix_tree_root \*root:
        radix tree root

    :param const struct radix_tree_iter \*iter:
        *undescribed*

    :param void \*\*slot:
        pointer to slot

    :param void \*item:
        new item to store in the slot.

.. _`radix_tree_iter_replace.description`:

Description
-----------

For use with \ :c:func:`radix_tree_split`\  and \ :c:func:`radix_tree_for_each_slot`\ .
Caller must hold tree write locked across split and replacement.

.. _`radix_tree_join`:

radix_tree_join
===============

.. c:function:: int radix_tree_join(struct radix_tree_root *root, unsigned long index, unsigned order, void *item)

    replace multiple entries with one multiorder entry

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        an index inside the new entry

    :param unsigned order:
        order of the new entry

    :param void \*item:
        new entry

.. _`radix_tree_join.description`:

Description
-----------

Call this function to replace several entries with one larger entry.
The existing entries are presumed to not need freeing as a result of
this call.

The replacement entry will have all the tags set on it that were set
on any of the entries it is replacing.

.. _`radix_tree_split`:

radix_tree_split
================

.. c:function:: int radix_tree_split(struct radix_tree_root *root, unsigned long index, unsigned order)

    Split an entry into smaller entries

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        An index within the large entry

    :param unsigned order:
        Order of new entries

.. _`radix_tree_split.description`:

Description
-----------

Call this function as the first step in replacing a multiorder entry
with several entries of lower order.  After this function returns,
loop over the relevant portion of the tree using \ :c:func:`radix_tree_for_each_slot`\ 
and call \ :c:func:`radix_tree_iter_replace`\  to set up each new entry.

The tags from this entry are replicated to all the new entries.

The radix tree should be locked against modification during the entire
replacement operation.  Lock-free lookups will see RADIX_TREE_RETRY which
should prompt RCU walkers to restart the lookup from the root.

.. _`radix_tree_tag_set`:

radix_tree_tag_set
==================

.. c:function:: void *radix_tree_tag_set(struct radix_tree_root *root, unsigned long index, unsigned int tag)

    set a tag on a radix tree node

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        index key

    :param unsigned int tag:
        tag index

.. _`radix_tree_tag_set.description`:

Description
-----------

Set the search tag (which must be < RADIX_TREE_MAX_TAGS)
corresponding to \ ``index``\  in the radix tree.  From
the root all the way down to the leaf node.

Returns the address of the tagged item.  Setting a tag on a not-present
item is a bug.

.. _`radix_tree_iter_tag_set`:

radix_tree_iter_tag_set
=======================

.. c:function:: void radix_tree_iter_tag_set(struct radix_tree_root *root, const struct radix_tree_iter *iter, unsigned int tag)

    set a tag on the current iterator entry

    :param struct radix_tree_root \*root:
        radix tree root

    :param const struct radix_tree_iter \*iter:
        iterator state

    :param unsigned int tag:
        tag to set

.. _`radix_tree_tag_clear`:

radix_tree_tag_clear
====================

.. c:function:: void *radix_tree_tag_clear(struct radix_tree_root *root, unsigned long index, unsigned int tag)

    clear a tag on a radix tree node

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        index key

    :param unsigned int tag:
        tag index

.. _`radix_tree_tag_clear.description`:

Description
-----------

Clear the search tag (which must be < RADIX_TREE_MAX_TAGS)
corresponding to \ ``index``\  in the radix tree.  If this causes
the leaf node to have no tags set then clear the tag in the
next-to-leaf node, etc.

Returns the address of the tagged item on success, else NULL.  ie:
has the same return value and semantics as \ :c:func:`radix_tree_lookup`\ .

.. _`radix_tree_tag_get`:

radix_tree_tag_get
==================

.. c:function:: int radix_tree_tag_get(struct radix_tree_root *root, unsigned long index, unsigned int tag)

    get a tag on a radix tree node

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        index key

    :param unsigned int tag:
        tag index (< RADIX_TREE_MAX_TAGS)

.. _`radix_tree_tag_get.return-values`:

Return values
-------------


0: tag not present or not set
1: tag set

Note that the return value of this function may not be relied on, even if
the RCU lock is held, unless tag modification and node deletion are excluded
from concurrency.

.. _`radix_tree_gang_lookup`:

radix_tree_gang_lookup
======================

.. c:function:: unsigned int radix_tree_gang_lookup(struct radix_tree_root *root, void **results, unsigned long first_index, unsigned int max_items)

    perform multiple lookup on a radix tree

    :param struct radix_tree_root \*root:
        radix tree root

    :param void \*\*results:
        where the results of the lookup are placed

    :param unsigned long first_index:
        start the lookup from this key

    :param unsigned int max_items:
        place up to this many items at \*results

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

.. _`radix_tree_gang_lookup_slot`:

radix_tree_gang_lookup_slot
===========================

.. c:function:: unsigned int radix_tree_gang_lookup_slot(struct radix_tree_root *root, void ***results, unsigned long *indices, unsigned long first_index, unsigned int max_items)

    perform multiple slot lookup on radix tree

    :param struct radix_tree_root \*root:
        radix tree root

    :param void \*\*\*results:
        where the results of the lookup are placed

    :param unsigned long \*indices:
        where their indices should be placed (but usually NULL)

    :param unsigned long first_index:
        start the lookup from this key

    :param unsigned int max_items:
        place up to this many items at \*results

.. _`radix_tree_gang_lookup_slot.description`:

Description
-----------

Performs an index-ascending scan of the tree for present items.  Places
their slots at \*@results and returns the number of items which were
placed at \*@results.

The implementation is naive.

Like radix_tree_gang_lookup as far as RCU and locking goes. Slots must
be dereferenced with radix_tree_deref_slot, and if using only RCU
protection, radix_tree_deref_slot may fail requiring a retry.

.. _`radix_tree_gang_lookup_tag`:

radix_tree_gang_lookup_tag
==========================

.. c:function:: unsigned int radix_tree_gang_lookup_tag(struct radix_tree_root *root, void **results, unsigned long first_index, unsigned int max_items, unsigned int tag)

    perform multiple lookup on a radix tree based on a tag

    :param struct radix_tree_root \*root:
        radix tree root

    :param void \*\*results:
        where the results of the lookup are placed

    :param unsigned long first_index:
        start the lookup from this key

    :param unsigned int max_items:
        place up to this many items at \*results

    :param unsigned int tag:
        the tag index (< RADIX_TREE_MAX_TAGS)

.. _`radix_tree_gang_lookup_tag.description`:

Description
-----------

Performs an index-ascending scan of the tree for present items which
have the tag indexed by \ ``tag``\  set.  Places the items at \*@results and
returns the number of items which were placed at \*@results.

.. _`radix_tree_gang_lookup_tag_slot`:

radix_tree_gang_lookup_tag_slot
===============================

.. c:function:: unsigned int radix_tree_gang_lookup_tag_slot(struct radix_tree_root *root, void ***results, unsigned long first_index, unsigned int max_items, unsigned int tag)

    perform multiple slot lookup on a radix tree based on a tag

    :param struct radix_tree_root \*root:
        radix tree root

    :param void \*\*\*results:
        where the results of the lookup are placed

    :param unsigned long first_index:
        start the lookup from this key

    :param unsigned int max_items:
        place up to this many items at \*results

    :param unsigned int tag:
        the tag index (< RADIX_TREE_MAX_TAGS)

.. _`radix_tree_gang_lookup_tag_slot.description`:

Description
-----------

Performs an index-ascending scan of the tree for present items which
have the tag indexed by \ ``tag``\  set.  Places the slots at \*@results and
returns the number of slots which were placed at \*@results.

.. _`__radix_tree_delete_node`:

__radix_tree_delete_node
========================

.. c:function:: void __radix_tree_delete_node(struct radix_tree_root *root, struct radix_tree_node *node)

    try to free node after clearing a slot

    :param struct radix_tree_root \*root:
        radix tree root

    :param struct radix_tree_node \*node:
        node containing \ ``index``\ 

.. _`__radix_tree_delete_node.description`:

Description
-----------

After clearing the slot at \ ``index``\  in \ ``node``\  from radix tree
rooted at \ ``root``\ , call this function to attempt freeing the
node and shrinking the tree.

.. _`radix_tree_delete_item`:

radix_tree_delete_item
======================

.. c:function:: void *radix_tree_delete_item(struct radix_tree_root *root, unsigned long index, void *item)

    delete an item from a radix tree

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        index key

    :param void \*item:
        expected item

.. _`radix_tree_delete_item.description`:

Description
-----------

Remove \ ``item``\  at \ ``index``\  from the radix tree rooted at \ ``root``\ .

Returns the address of the deleted item, or NULL if it was not present
or the entry at the given \ ``index``\  was not \ ``item``\ .

.. _`radix_tree_delete`:

radix_tree_delete
=================

.. c:function:: void *radix_tree_delete(struct radix_tree_root *root, unsigned long index)

    delete an item from a radix tree

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned long index:
        index key

.. _`radix_tree_delete.description`:

Description
-----------

Remove the item at \ ``index``\  from the radix tree rooted at \ ``root``\ .

Returns the address of the deleted item, or NULL if it was not present.

.. _`radix_tree_tagged`:

radix_tree_tagged
=================

.. c:function:: int radix_tree_tagged(struct radix_tree_root *root, unsigned int tag)

    test whether any items in the tree are tagged

    :param struct radix_tree_root \*root:
        radix tree root

    :param unsigned int tag:
        tag to test

.. This file was automatic generated / don't edit.

