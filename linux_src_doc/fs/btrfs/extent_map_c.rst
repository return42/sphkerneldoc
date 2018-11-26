.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/extent_map.c

.. _`extent_map_tree_init`:

extent_map_tree_init
====================

.. c:function:: void extent_map_tree_init(struct extent_map_tree *tree)

    initialize extent map tree

    :param tree:
        tree to initialize
    :type tree: struct extent_map_tree \*

.. _`extent_map_tree_init.description`:

Description
-----------

Initialize the extent tree \ ``tree``\ .  Should be called for each new inode
or other user of the extent_map interface.

.. _`alloc_extent_map`:

alloc_extent_map
================

.. c:function:: struct extent_map *alloc_extent_map( void)

    allocate new extent map structure

    :param void:
        no arguments
    :type void: 

.. _`alloc_extent_map.description`:

Description
-----------

Allocate a new extent_map structure.  The new structure is
returned with a reference count of one and needs to be
freed using \ :c:func:`free_extent_map`\ 

.. _`free_extent_map`:

free_extent_map
===============

.. c:function:: void free_extent_map(struct extent_map *em)

    drop reference count of an extent_map

    :param em:
        extent map being released
    :type em: struct extent_map \*

.. _`free_extent_map.description`:

Description
-----------

Drops the reference out on \ ``em``\  by one and free the structure
if the reference count hits zero.

.. _`unpin_extent_cache`:

unpin_extent_cache
==================

.. c:function:: int unpin_extent_cache(struct extent_map_tree *tree, u64 start, u64 len, u64 gen)

    unpin an extent from the cache

    :param tree:
        tree to unpin the extent in
    :type tree: struct extent_map_tree \*

    :param start:
        logical offset in the file
    :type start: u64

    :param len:
        length of the extent
    :type len: u64

    :param gen:
        generation that this extent has been modified in
    :type gen: u64

.. _`unpin_extent_cache.description`:

Description
-----------

Called after an extent has been written to disk properly.  Set the generation
to the generation that actually added the file item to the inode so we know
we need to sync this extent when we call \ :c:func:`fsync`\ .

.. _`add_extent_mapping`:

add_extent_mapping
==================

.. c:function:: int add_extent_mapping(struct extent_map_tree *tree, struct extent_map *em, int modified)

    add new extent map to the extent tree

    :param tree:
        tree to insert new map in
    :type tree: struct extent_map_tree \*

    :param em:
        map to insert
    :type em: struct extent_map \*

    :param modified:
        *undescribed*
    :type modified: int

.. _`add_extent_mapping.description`:

Description
-----------

Insert \ ``em``\  into \ ``tree``\  or perform a simple forward/backward merge with
existing mappings.  The extent_map struct passed in will be inserted
into the tree directly, with an additional reference taken, or a
reference dropped if the merge attempt was successful.

.. _`lookup_extent_mapping`:

lookup_extent_mapping
=====================

.. c:function:: struct extent_map *lookup_extent_mapping(struct extent_map_tree *tree, u64 start, u64 len)

    lookup extent_map

    :param tree:
        tree to lookup in
    :type tree: struct extent_map_tree \*

    :param start:
        byte offset to start the search
    :type start: u64

    :param len:
        length of the lookup range
    :type len: u64

.. _`lookup_extent_mapping.description`:

Description
-----------

Find and return the first extent_map struct in \ ``tree``\  that intersects the
[start, len] range.  There may be additional objects in the tree that
intersect, so check the object returned carefully to make sure that no
additional lookups are needed.

.. _`search_extent_mapping`:

search_extent_mapping
=====================

.. c:function:: struct extent_map *search_extent_mapping(struct extent_map_tree *tree, u64 start, u64 len)

    find a nearby extent map

    :param tree:
        tree to lookup in
    :type tree: struct extent_map_tree \*

    :param start:
        byte offset to start the search
    :type start: u64

    :param len:
        length of the lookup range
    :type len: u64

.. _`search_extent_mapping.description`:

Description
-----------

Find and return the first extent_map struct in \ ``tree``\  that intersects the
[start, len] range.

If one can't be found, any nearby extent may be returned

.. _`remove_extent_mapping`:

remove_extent_mapping
=====================

.. c:function:: void remove_extent_mapping(struct extent_map_tree *tree, struct extent_map *em)

    removes an extent_map from the extent tree

    :param tree:
        extent tree to remove from
    :type tree: struct extent_map_tree \*

    :param em:
        extent map being removed
    :type em: struct extent_map \*

.. _`remove_extent_mapping.description`:

Description
-----------

Removes \ ``em``\  from \ ``tree``\ .  No reference counts are dropped, and no checks
are done to see if the range is in use

.. _`btrfs_add_extent_mapping`:

btrfs_add_extent_mapping
========================

.. c:function:: int btrfs_add_extent_mapping(struct btrfs_fs_info *fs_info, struct extent_map_tree *em_tree, struct extent_map **em_in, u64 start, u64 len)

    add extent mapping into em_tree \ ``fs_info``\  - used for tracepoint \ ``em_tree``\  - the extent tree into which we want to insert the extent mapping \ ``em_in``\    - extent we are inserting \ ``start``\    - start of the logical range \ :c:func:`btrfs_get_extent`\  is requesting \ ``len``\      - length of the logical range \ :c:func:`btrfs_get_extent`\  is requesting

    :param fs_info:
        *undescribed*
    :type fs_info: struct btrfs_fs_info \*

    :param em_tree:
        *undescribed*
    :type em_tree: struct extent_map_tree \*

    :param em_in:
        *undescribed*
    :type em_in: struct extent_map \*\*

    :param start:
        *undescribed*
    :type start: u64

    :param len:
        *undescribed*
    :type len: u64

.. _`btrfs_add_extent_mapping.description`:

Description
-----------

Note that \ ``em_in``\ 's range may be different from [start, start+len),
but they must be overlapped.

Insert \ ``em_in``\  into \ ``em_tree``\ . In case there is an overlapping range, handle
the -EEXIST by either:
a) Returning the existing extent in \ ``em_in``\  if \ ``start``\  is within the
existing em.
b) Merge the existing extent with \ ``em_in``\  passed in.

Return 0 on success, otherwise -EEXIST.

.. This file was automatic generated / don't edit.

