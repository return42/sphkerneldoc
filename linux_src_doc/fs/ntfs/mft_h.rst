.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/mft.h

.. _`flush_dcache_mft_record_page`:

flush_dcache_mft_record_page
============================

.. c:function:: void flush_dcache_mft_record_page(ntfs_inode *ni)

    \ :c:func:`flush_dcache_page`\  for mft records

    :param ni:
        ntfs inode structure of mft record
    :type ni: ntfs_inode \*

.. _`flush_dcache_mft_record_page.description`:

Description
-----------

Call \ :c:func:`flush_dcache_page`\  for the page in which an mft record resides.

This must be called every time an mft record is modified, just after the
modification.

.. _`mark_mft_record_dirty`:

mark_mft_record_dirty
=====================

.. c:function:: void mark_mft_record_dirty(ntfs_inode *ni)

    set the mft record and the page containing it dirty

    :param ni:
        ntfs inode describing the mapped mft record
    :type ni: ntfs_inode \*

.. _`mark_mft_record_dirty.description`:

Description
-----------

Set the mapped (extent) mft record of the (base or extent) ntfs inode \ ``ni``\ ,
as well as the page containing the mft record, dirty.  Also, mark the base
vfs inode dirty.  This ensures that any changes to the mft record are
written out to disk.

.. _`mark_mft_record_dirty.note`:

NOTE
----

Do not do anything if the mft record is already marked dirty.

.. _`write_mft_record`:

write_mft_record
================

.. c:function:: int write_mft_record(ntfs_inode *ni, MFT_RECORD *m, int sync)

    write out a mapped (extent) mft record

    :param ni:
        ntfs inode describing the mapped (extent) mft record
    :type ni: ntfs_inode \*

    :param m:
        mapped (extent) mft record to write
    :type m: MFT_RECORD \*

    :param sync:
        if true, wait for i/o completion
    :type sync: int

.. _`write_mft_record.description`:

Description
-----------

This is just a wrapper for \ :c:func:`write_mft_record_nolock`\  (see mft.c), which
locks the page for the duration of the write.  This ensures that there are
no race conditions between writing the mft record via the dirty inode code
paths and via the page cache write back code paths or between writing
neighbouring mft records residing in the same page.

Locking the page also serializes us against ->readpage() if the page is not
uptodate.

On success, clean the mft record and return 0.  On error, leave the mft
record dirty and return -errno.

.. This file was automatic generated / don't edit.

