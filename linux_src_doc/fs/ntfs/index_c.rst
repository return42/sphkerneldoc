.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/index.c

.. _`ntfs_index_ctx_get`:

ntfs_index_ctx_get
==================

.. c:function:: ntfs_index_context *ntfs_index_ctx_get(ntfs_inode *idx_ni)

    allocate and initialize a new index context

    :param ntfs_inode \*idx_ni:
        ntfs index inode with which to initialize the context

.. _`ntfs_index_ctx_get.description`:

Description
-----------

Allocate a new index context, initialize it with \ ``idx_ni``\  and return it.
Return NULL if allocation failed.

.. _`ntfs_index_ctx_get.locking`:

Locking
-------

Caller must hold i_mutex on the index inode.

.. _`ntfs_index_ctx_put`:

ntfs_index_ctx_put
==================

.. c:function:: void ntfs_index_ctx_put(ntfs_index_context *ictx)

    release an index context

    :param ntfs_index_context \*ictx:
        index context to free

.. _`ntfs_index_ctx_put.description`:

Description
-----------

Release the index context \ ``ictx``\ , releasing all associated resources.

.. _`ntfs_index_ctx_put.locking`:

Locking
-------

Caller must hold i_mutex on the index inode.

.. _`ntfs_index_lookup`:

ntfs_index_lookup
=================

.. c:function:: int ntfs_index_lookup(const void *key, const int key_len, ntfs_index_context *ictx)

    find a key in an index and return its index entry

    :param const void \*key:
        [IN] key for which to search in the index

    :param const int key_len:
        [IN] length of \ ``key``\  in bytes

    :param ntfs_index_context \*ictx:
        [IN/OUT] context describing the index and the returned entry

.. _`ntfs_index_lookup.description`:

Description
-----------

Before calling \ :c:func:`ntfs_index_lookup`\ , \ ``ictx``\  must have been obtained from a
call to \ :c:func:`ntfs_index_ctx_get`\ .

Look for the \ ``key``\  in the index specified by the index lookup context \ ``ictx``\ .
\ :c:func:`ntfs_index_lookup`\  walks the contents of the index looking for the \ ``key``\ .

If the \ ``key``\  is found in the index, 0 is returned and \ ``ictx``\  is setup to
describe the index entry containing the matching \ ``key``\ .  \ ``ictx``\ ->entry is the
index entry and \ ``ictx``\ ->data and \ ``ictx``\ ->data_len are the index entry data and
its length in bytes, respectively.

If the \ ``key``\  is not found in the index, -ENOENT is returned and \ ``ictx``\  is
setup to describe the index entry whose key collates immediately after the
search \ ``key``\ , i.e. this is the position in the index at which an index entry
with a key of \ ``key``\  would need to be inserted.

If an error occurs return the negative error code and \ ``ictx``\  is left
untouched.

When finished with the entry and its data, call \ :c:func:`ntfs_index_ctx_put`\  to free
the context and other associated resources.

If the index entry was modified, call \ :c:func:`flush_dcache_index_entry_page`\ 
immediately after the modification and either \ :c:func:`ntfs_index_entry_mark_dirty`\ 
or \ :c:func:`ntfs_index_entry_write`\  before the call to \ :c:func:`ntfs_index_ctx_put`\  to
ensure that the changes are written to disk.

.. _`ntfs_index_lookup.locking`:

Locking
-------

- Caller must hold i_mutex on the index inode.
- Each page cache page in the index allocation mapping must be
locked whilst being accessed otherwise we may find a corrupt
page due to it being under ->writepage at the moment which
applies the mst protection fixups before writing out and then
removes them again after the write is complete after which it
unlocks the page.

.. This file was automatic generated / don't edit.

