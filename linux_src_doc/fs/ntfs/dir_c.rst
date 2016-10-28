.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/dir.c

.. _`ntfs_lookup_inode_by_name`:

ntfs_lookup_inode_by_name
=========================

.. c:function:: MFT_REF ntfs_lookup_inode_by_name(ntfs_inode *dir_ni, const ntfschar *uname, const int uname_len, ntfs_name **res)

    find an inode in a directory given its name

    :param ntfs_inode \*dir_ni:
        ntfs inode of the directory in which to search for the name

    :param const ntfschar \*uname:
        Unicode name for which to search in the directory

    :param const int uname_len:
        length of the name \ ``uname``\  in Unicode characters

    :param ntfs_name \*\*res:
        return the found file name if necessary (see below)

.. _`ntfs_lookup_inode_by_name.description`:

Description
-----------

Look for an inode with name \ ``uname``\  in the directory with inode \ ``dir_ni``\ .
\ :c:func:`ntfs_lookup_inode_by_name`\  walks the contents of the directory looking for
the Unicode name. If the name is found in the directory, the corresponding
inode number (>= 0) is returned as a mft reference in cpu format, i.e. it
is a 64-bit number containing the sequence number.

On error, a negative value is returned corresponding to the error code. In
particular if the inode is not found -ENOENT is returned. Note that you
can't just check the return value for being negative, you have to check the
inode number for being negative which you can extract using MREC(return
value).

Note, \ ``uname_len``\  does not include the (optional) terminating NULL character.

Note, we look for a case sensitive match first but we also look for a case
insensitive match at the same time. If we find a case insensitive match, we
save that for the case that we don't find an exact match, where we return
the case insensitive match and setup \ ``res``\  (which we allocate!) with the mft
reference, the file name type, length and with a copy of the little endian
Unicode file name itself. If we match a file name which is in the DOS name
space, we only return the mft reference and file name type in \ ``res``\ .
\ :c:func:`ntfs_lookup`\  then uses this to find the long file name in the inode itself.
This is to avoid polluting the dcache with short file names. We want them to
work but we don't care for how quickly one can access them. This also fixes
the dcache aliasing issues.

.. _`ntfs_lookup_inode_by_name.locking`:

Locking
-------

- Caller must hold i_mutex on the directory.
- Each page cache page in the index allocation mapping must be
locked whilst being accessed otherwise we may find a corrupt
page due to it being under ->writepage at the moment which
applies the mst protection fixups before writing out and then
removes them again after the write is complete after which it
unlocks the page.

.. _`ntfs_lookup_inode_by_name`:

ntfs_lookup_inode_by_name
=========================

.. c:function:: u64 ntfs_lookup_inode_by_name(ntfs_inode *dir_ni, const ntfschar *uname, const int uname_len)

    find an inode in a directory given its name

    :param ntfs_inode \*dir_ni:
        ntfs inode of the directory in which to search for the name

    :param const ntfschar \*uname:
        Unicode name for which to search in the directory

    :param const int uname_len:
        length of the name \ ``uname``\  in Unicode characters

.. _`ntfs_lookup_inode_by_name.description`:

Description
-----------

Look for an inode with name \ ``uname``\  in the directory with inode \ ``dir_ni``\ .
\ :c:func:`ntfs_lookup_inode_by_name`\  walks the contents of the directory looking for
the Unicode name. If the name is found in the directory, the corresponding
inode number (>= 0) is returned as a mft reference in cpu format, i.e. it
is a 64-bit number containing the sequence number.

On error, a negative value is returned corresponding to the error code. In
particular if the inode is not found -ENOENT is returned. Note that you
can't just check the return value for being negative, you have to check the
inode number for being negative which you can extract using MREC(return
value).

Note, \ ``uname_len``\  does not include the (optional) terminating NULL character.

.. _`ntfs_filldir`:

ntfs_filldir
============

.. c:function:: int ntfs_filldir(ntfs_volume *vol, ntfs_inode *ndir, struct page *ia_page, INDEX_ENTRY *ie, u8 *name, struct dir_context *actor)

    ntfs specific filldir method

    :param ntfs_volume \*vol:
        current ntfs volume

    :param ntfs_inode \*ndir:
        ntfs inode of current directory

    :param struct page \*ia_page:
        page in which the index allocation buffer \ ``ie``\  is in resides

    :param INDEX_ENTRY \*ie:
        current index entry

    :param u8 \*name:
        buffer to use for the converted name

    :param struct dir_context \*actor:
        what to feed the entries to

.. _`ntfs_filldir.description`:

Description
-----------

Convert the Unicode \ ``name``\  to the loaded NLS and pass it to the \ ``filldir``\ 
callback.

If \ ``ia_page``\  is not NULL it is the locked page containing the index
allocation block containing the index entry \ ``ie``\ .

Note, we drop (and then reacquire) the page lock on \ ``ia_page``\  across the
@\ :c:func:`filldir`\  call otherwise we would deadlock with NFSd when it calls ->lookup
since \ :c:func:`ntfs_lookup`\  will lock the same page.  As an optimization, we do not
retake the lock if we are returning a non-zero value as \ :c:func:`ntfs_readdir`\ 
would need to drop the lock immediately anyway.

.. _`ntfs_dir_open`:

ntfs_dir_open
=============

.. c:function:: int ntfs_dir_open(struct inode *vi, struct file *filp)

    called when an inode is about to be opened

    :param struct inode \*vi:
        inode to be opened

    :param struct file \*filp:
        file structure describing the inode

.. _`ntfs_dir_open.description`:

Description
-----------

Limit directory size to the page cache limit on architectures where unsigned
long is 32-bits. This is the most we can do for now without overflowing the
page cache page index. Doing it this way means we don't run into problems
because of existing too large directories. It would be better to allow the
user to read the accessible part of the directory but I doubt very much
anyone is going to hit this check on a 32-bit architecture, so there is no
point in adding the extra complexity required to support this.

On 64-bit architectures, the check is hopefully optimized away by the
compiler.

.. _`ntfs_dir_fsync`:

ntfs_dir_fsync
==============

.. c:function:: int ntfs_dir_fsync(struct file *filp, loff_t start, loff_t end, int datasync)

    sync a directory to disk

    :param struct file \*filp:
        directory to be synced

    :param loff_t start:
        *undescribed*

    :param loff_t end:
        *undescribed*

    :param int datasync:
        if non-zero only flush user data and not metadata

.. _`ntfs_dir_fsync.description`:

Description
-----------

Data integrity sync of a directory to disk.  Used for fsync, fdatasync, and
msync system calls.  This function is based on file.c::\ :c:func:`ntfs_file_fsync`\ .

Write the mft record and all associated extent mft records as well as the
\ ``$INDEX_ALLOCATION``\  and \ ``$BITMAP``\  attributes and then sync the block device.

If \ ``datasync``\  is true, we do not wait on the inode(s) to be written out
but we always wait on the page cache pages to be written out.

.. _`ntfs_dir_fsync.note`:

Note
----

In the past \ ``filp``\  could be NULL so we ignore it as we don't need it
anyway.

.. _`ntfs_dir_fsync.locking`:

Locking
-------

Caller must hold i_mutex on the inode.

.. _`ntfs_dir_fsync.todo`:

TODO
----

We should probably also write all attribute/index inodes associated
with this inode but since we have no simple way of getting to them we ignore
this problem for now.  We do write the \ ``$BITMAP``\  attribute if it is present
which is the important one for a directory so things are not too bad.

.. This file was automatic generated / don't edit.

