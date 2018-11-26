.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/lib/chash.c

.. _`chash_table_alloc`:

chash_table_alloc
=================

.. c:function:: int chash_table_alloc(struct chash_table *table, u8 bits, u8 key_size, unsigned int value_size, gfp_t gfp_mask)

    Allocate closed hash table

    :param table:
        Pointer to the table structure
    :type table: struct chash_table \*

    :param bits:
        Table size will be 2^bits entries
    :type bits: u8

    :param key_size:
        Size of hash keys in bytes, 4 or 8
    :type key_size: u8

    :param value_size:
        Size of data values in bytes, can be 0
    :type value_size: unsigned int

    :param gfp_mask:
        *undescribed*
    :type gfp_mask: gfp_t

.. _`chash_table_free`:

chash_table_free
================

.. c:function:: void chash_table_free(struct chash_table *table)

    Free closed hash table

    :param table:
        Pointer to the table structure
    :type table: struct chash_table \*

.. _`chash_table_find`:

chash_table_find
================

.. c:function:: int chash_table_find(struct chash_iter *iter, u64 key, bool for_removal)

    Helper for looking up a hash table entry

    :param iter:
        Pointer to hash table iterator
    :type iter: struct chash_iter \*

    :param key:
        Key of the entry to find
    :type key: u64

    :param for_removal:
        set to true if the element will be removed soon
    :type for_removal: bool

.. _`chash_table_find.description`:

Description
-----------

Searches for an entry in the hash table with a given key. iter must
be initialized by the caller to point to the home position of the
hypothetical entry, i.e. it must be initialized with the hash table
and the key's hash as the initial slot for the search.

This function also does some local clean-up to speed up future
look-ups by relocating entries to better slots and removing
tombstones that are no longer needed.

If \ ``for_removal``\  is true, the function avoids relocating the entry
that is being returned.

Returns 0 if the search is successful. In this case iter is updated
to point to the found entry. Otherwise \ ``-EINVAL``\  is returned and the
iter is updated to point to the first available slot for the given
key. If the table is full, the slot is set to -1.

.. _`chash_self_test`:

chash_self_test
===============

.. c:function:: int chash_self_test(u8 bits, u8 key_size, int min_fill, int max_fill, u64 iterations)

    Run a self-test of the hash table implementation

    :param bits:
        Table size will be 2^bits entries
    :type bits: u8

    :param key_size:
        Size of hash keys in bytes, 4 or 8
    :type key_size: u8

    :param min_fill:
        Minimum fill level during the test
    :type min_fill: int

    :param max_fill:
        Maximum fill level during the test
    :type max_fill: int

    :param iterations:
        Number of test iterations
    :type iterations: u64

.. _`chash_self_test.description`:

Description
-----------

The test adds and removes entries from a hash table, cycling the
fill level between min_fill and max_fill entries. Also tests lookup
and value retrieval.

.. This file was automatic generated / don't edit.

