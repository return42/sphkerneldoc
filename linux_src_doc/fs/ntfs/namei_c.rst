.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/namei.c

.. _`ntfs_lookup`:

ntfs_lookup
===========

.. c:function:: struct dentry *ntfs_lookup(struct inode *dir_ino, struct dentry *dent, unsigned int flags)

    find the inode represented by a dentry in a directory inode

    :param struct inode \*dir_ino:
        directory inode in which to look for the inode

    :param struct dentry \*dent:
        dentry representing the inode to look for

    :param unsigned int flags:
        lookup flags

.. _`ntfs_lookup.description`:

Description
-----------

In short, \ :c:func:`ntfs_lookup`\  looks for the inode represented by the dentry \ ``dent``\ 
in the directory inode \ ``dir_ino``\  and if found attaches the inode to the
dentry \ ``dent``\ .

In more detail, the dentry \ ``dent``\  specifies which inode to look for by
supplying the name of the inode in \ ``dent``\ ->d_name.name. \ :c:func:`ntfs_lookup`\ 
converts the name to Unicode and walks the contents of the directory inode
\ ``dir_ino``\  looking for the converted Unicode name. If the name is found in the
directory, the corresponding inode is loaded by calling \ :c:func:`ntfs_iget`\  on its
inode number and the inode is associated with the dentry \ ``dent``\  via a call to
\ :c:func:`d_splice_alias`\ .

If the name is not found in the directory, a NULL inode is inserted into the
dentry \ ``dent``\  via a call to \ :c:func:`d_add`\ . The dentry is then termed a negative
dentry.

Only if an actual error occurs, do we return an error via \ :c:func:`ERR_PTR`\ .

In order to handle the case insensitivity issues of NTFS with regards to the
dcache and the dcache requiring only one dentry per directory, we deal with
dentry aliases that only differ in case in ->ntfs_lookup() while maintaining
a case sensitive dcache. This means that we get the full benefit of dcache
speed when the file/directory is looked up with the same case as returned by
->ntfs_readdir() but that a lookup for any other case (or for the short file
name) will not find anything in dcache and will enter ->ntfs_lookup()
instead, where we search the directory for a fully matching file name
(including case) and if that is not found, we search for a file name that
matches with different case and if that has non-POSIX semantics we return
that. We actually do only one search (case sensitive) and keep tabs on
whether we have found a case insensitive match in the process.

To simplify matters for us, we do not treat the short vs long filenames as
two hard links but instead if the lookup matches a short filename, we
return the dentry for the corresponding long filename instead.

.. _`ntfs_lookup.there-are-three-cases-we-need-to-distinguish-here`:

There are three cases we need to distinguish here
-------------------------------------------------


1) \ ``dent``\  perfectly matches (i.e. including case) a directory entry with a
file name in the WIN32 or POSIX namespaces. In this case
\ :c:func:`ntfs_lookup_inode_by_name`\  will return with name set to NULL and we
just \ :c:func:`d_splice_alias`\  \ ``dent``\ .
2) \ ``dent``\  matches (not including case) a directory entry with a file name in
the WIN32 namespace. In this case \ :c:func:`ntfs_lookup_inode_by_name`\  will return
with name set to point to a \ :c:func:`kmalloc`\ ed ntfs_name structure containing
the properly cased little endian Unicode name. We convert the name to the
current NLS code page, search if a dentry with this name already exists
and if so return that instead of \ ``dent``\ .  At this point things are
complicated by the possibility of 'disconnected' dentries due to NFS
which we deal with appropriately (see the code comments).  The VFS will
then destroy the old \ ``dent``\  and use the one we returned.  If a dentry is
not found, we allocate a new one, \ :c:func:`d_splice_alias`\  it, and return it as
above.
3) \ ``dent``\  matches either perfectly or not (i.e. we don't care about case) a
directory entry with a file name in the DOS namespace. In this case
\ :c:func:`ntfs_lookup_inode_by_name`\  will return with name set to point to a
\ :c:func:`kmalloc`\ ed ntfs_name structure containing the mft reference (cpu endian)
of the inode. We use the mft reference to read the inode and to find the
file name in the WIN32 namespace corresponding to the matched short file
name. We then convert the name to the current NLS code page, and proceed
searching for a dentry with this name, etc, as in case 2), above.

.. _`ntfs_lookup.locking`:

Locking
-------

Caller must hold i_mutex on the directory.

.. _`ntfs_get_parent`:

ntfs_get_parent
===============

.. c:function:: struct dentry *ntfs_get_parent(struct dentry *child_dent)

    find the dentry of the parent of a given directory dentry

    :param struct dentry \*child_dent:
        dentry of the directory whose parent directory to find

.. _`ntfs_get_parent.description`:

Description
-----------

Find the dentry for the parent directory of the directory specified by the
dentry \ ``child_dent``\ .  This function is called from
fs/exportfs/expfs.c::find_exported_dentry() which in turn is called from the
default ->decode_fh() which is \ :c:func:`export_decode_fh`\  in the same file.

The code is based on the ext3 ->get_parent() implementation found in
fs/ext3/namei.c::ext3_get_parent().

.. _`ntfs_get_parent.note`:

Note
----

ntfs_get_parent() is called with \ ``d_inode``\ (child_dent)->i_mutex down.

Return the dentry of the parent directory on success or the error code on
error (IS_ERR() is true).

.. This file was automatic generated / don't edit.

