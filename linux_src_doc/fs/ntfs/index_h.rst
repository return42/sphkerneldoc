.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/index.h

.. _`ntfs_index_entry_flush_dcache_page`:

ntfs_index_entry_flush_dcache_page
==================================

.. c:function:: void ntfs_index_entry_flush_dcache_page(ntfs_index_context *ictx)

    flush_dcache_page() for index entries

    :param ntfs_index_context \*ictx:
        ntfs index context describing the index entry

.. _`ntfs_index_entry_flush_dcache_page.description`:

Description
-----------

Call \ :c:func:`flush_dcache_page`\  for the page in which an index entry resides.

This must be called every time an index entry is modified, just after the
modification.

If the index entry is in the index root attribute, simply flush the page
containing the mft record containing the index root attribute.

If the index entry is in an index block belonging to the index allocation
attribute, simply flush the page cache page containing the index block.

.. _`ntfs_index_entry_mark_dirty`:

ntfs_index_entry_mark_dirty
===========================

.. c:function:: void ntfs_index_entry_mark_dirty(ntfs_index_context *ictx)

    mark an index entry dirty

    :param ntfs_index_context \*ictx:
        ntfs index context describing the index entry

.. _`ntfs_index_entry_mark_dirty.description`:

Description
-----------

Mark the index entry described by the index entry context \ ``ictx``\  dirty.

If the index entry is in the index root attribute, simply mark the mft
record containing the index root attribute dirty.  This ensures the mft
record, and hence the index root attribute, will be written out to disk
later.

If the index entry is in an index block belonging to the index allocation
attribute, mark the buffers belonging to the index record as well as the
page cache page the index block is in dirty.  This automatically marks the
VFS inode of the ntfs index inode to which the index entry belongs dirty,
too (I_DIRTY_PAGES) and this in turn ensures the page buffers, and hence the
dirty index block, will be written out to disk later.

.. This file was automatic generated / don't edit.

