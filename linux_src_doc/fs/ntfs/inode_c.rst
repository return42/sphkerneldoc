.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/inode.c

.. _`ntfs_test_inode`:

ntfs_test_inode
===============

.. c:function:: int ntfs_test_inode(struct inode *vi, ntfs_attr *na)

    NTFS kernel inode handling.

    :param vi:
        *undescribed*
    :type vi: struct inode \*

    :param na:
        *undescribed*
    :type na: ntfs_attr \*

.. _`ntfs_test_inode.description`:

Description
-----------

Copyright (c) 2001-2014 Anton Altaparmakov and Tuxera Inc.

This program/include file is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program/include file is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (in the main directory of the Linux-NTFS
distribution in the file COPYING); if not, write to the Free Software
Foundation,Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

.. _`ntfs_init_locked_inode`:

ntfs_init_locked_inode
======================

.. c:function:: int ntfs_init_locked_inode(struct inode *vi, ntfs_attr *na)

    initialize an inode

    :param vi:
        vfs inode to initialize
    :type vi: struct inode \*

    :param na:
        ntfs attribute which to initialize \ ``vi``\  to
    :type na: ntfs_attr \*

.. _`ntfs_init_locked_inode.description`:

Description
-----------

Initialize the vfs inode \ ``vi``\  with the values from the ntfs attribute \ ``na``\  in
order to enable \ :c:func:`ntfs_test_inode`\  to do its work.

If initializing the normal file/directory inode, set \ ``na->type``\  to AT_UNUSED.
In that case, \ ``na->name``\  and \ ``na->name_len``\  should be set to NULL and 0,
respectively. Although that is not strictly necessary as
\ :c:func:`ntfs_read_locked_inode`\  will fill them in later.

Return 0 on success and -errno on error.

.. _`ntfs_init_locked_inode.note`:

NOTE
----

This function runs with the inode->i_lock spin lock held so it is not
allowed to sleep. (Hence the GFP_ATOMIC allocation.)

.. _`ntfs_iget`:

ntfs_iget
=========

.. c:function:: struct inode *ntfs_iget(struct super_block *sb, unsigned long mft_no)

    obtain a struct inode corresponding to a specific normal inode

    :param sb:
        super block of mounted volume
    :type sb: struct super_block \*

    :param mft_no:
        mft record number / inode number to obtain
    :type mft_no: unsigned long

.. _`ntfs_iget.description`:

Description
-----------

Obtain the struct inode corresponding to a specific normal inode (i.e. a
file or directory).

If the inode is in the cache, it is just returned with an increased
reference count. Otherwise, a new struct inode is allocated and initialized,
and finally \ :c:func:`ntfs_read_locked_inode`\  is called to read in the inode and
fill in the remainder of the inode structure.

Return the struct inode on success. Check the return value with \ :c:func:`IS_ERR`\  and
if true, the function failed and the error code is obtained from \ :c:func:`PTR_ERR`\ .

.. _`ntfs_attr_iget`:

ntfs_attr_iget
==============

.. c:function:: struct inode *ntfs_attr_iget(struct inode *base_vi, ATTR_TYPE type, ntfschar *name, u32 name_len)

    obtain a struct inode corresponding to an attribute

    :param base_vi:
        vfs base inode containing the attribute
    :type base_vi: struct inode \*

    :param type:
        attribute type
    :type type: ATTR_TYPE

    :param name:
        Unicode name of the attribute (NULL if unnamed)
    :type name: ntfschar \*

    :param name_len:
        length of \ ``name``\  in Unicode characters (0 if unnamed)
    :type name_len: u32

.. _`ntfs_attr_iget.description`:

Description
-----------

Obtain the (fake) struct inode corresponding to the attribute specified by
\ ``type``\ , \ ``name``\ , and \ ``name_len``\ , which is present in the base mft record
specified by the vfs inode \ ``base_vi``\ .

If the attribute inode is in the cache, it is just returned with an
increased reference count. Otherwise, a new struct inode is allocated and
initialized, and finally \ :c:func:`ntfs_read_locked_attr_inode`\  is called to read the
attribute and fill in the inode structure.

Note, for index allocation attributes, you need to use \ :c:func:`ntfs_index_iget`\ 
instead of \ :c:func:`ntfs_attr_iget`\  as working with indices is a lot more complex.

Return the struct inode of the attribute inode on success. Check the return
value with \ :c:func:`IS_ERR`\  and if true, the function failed and the error code is
obtained from \ :c:func:`PTR_ERR`\ .

.. _`ntfs_index_iget`:

ntfs_index_iget
===============

.. c:function:: struct inode *ntfs_index_iget(struct inode *base_vi, ntfschar *name, u32 name_len)

    obtain a struct inode corresponding to an index

    :param base_vi:
        vfs base inode containing the index related attributes
    :type base_vi: struct inode \*

    :param name:
        Unicode name of the index
    :type name: ntfschar \*

    :param name_len:
        length of \ ``name``\  in Unicode characters
    :type name_len: u32

.. _`ntfs_index_iget.description`:

Description
-----------

Obtain the (fake) struct inode corresponding to the index specified by \ ``name``\ 
and \ ``name_len``\ , which is present in the base mft record specified by the vfs
inode \ ``base_vi``\ .

If the index inode is in the cache, it is just returned with an increased
reference count.  Otherwise, a new struct inode is allocated and
initialized, and finally \ :c:func:`ntfs_read_locked_index_inode`\  is called to read
the index related attributes and fill in the inode structure.

Return the struct inode of the index inode on success. Check the return
value with \ :c:func:`IS_ERR`\  and if true, the function failed and the error code is
obtained from \ :c:func:`PTR_ERR`\ .

.. _`__ntfs_init_inode`:

\__ntfs_init_inode
==================

.. c:function:: void __ntfs_init_inode(struct super_block *sb, ntfs_inode *ni)

    initialize ntfs specific part of an inode

    :param sb:
        super block of mounted volume
    :type sb: struct super_block \*

    :param ni:
        freshly allocated ntfs inode which to initialize
    :type ni: ntfs_inode \*

.. _`__ntfs_init_inode.description`:

Description
-----------

Initialize an ntfs inode to defaults.

.. _`__ntfs_init_inode.note`:

NOTE
----

ni->mft_no, ni->state, ni->type, ni->name, and ni->name_len are left
untouched. Make sure to initialize them elsewhere.

Return zero on success and -ENOMEM on error.

.. _`ntfs_is_extended_system_file`:

ntfs_is_extended_system_file
============================

.. c:function:: int ntfs_is_extended_system_file(ntfs_attr_search_ctx *ctx)

    check if a file is in the \ ``$Extend``\  directory

    :param ctx:
        initialized attribute search context
    :type ctx: ntfs_attr_search_ctx \*

.. _`ntfs_is_extended_system_file.description`:

Description
-----------

Search all file name attributes in the inode described by the attribute
search context \ ``ctx``\  and check if any of the names are in the \ ``$Extend``\  system
directory.

.. _`ntfs_is_extended_system_file.return-values`:

Return values
-------------

1: file is in \ ``$Extend``\  directory
0: file is not in \ ``$Extend``\  directory
-errno: failed to determine if the file is in the \ ``$Extend``\  directory

.. _`ntfs_read_locked_inode`:

ntfs_read_locked_inode
======================

.. c:function:: int ntfs_read_locked_inode(struct inode *vi)

    read an inode from its device

    :param vi:
        inode to read
    :type vi: struct inode \*

.. _`ntfs_read_locked_inode.description`:

Description
-----------

\ :c:func:`ntfs_read_locked_inode`\  is called from \ :c:func:`ntfs_iget`\  to read the inode
described by \ ``vi``\  into memory from the device.

The only fields in \ ``vi``\  that we need to/can look at when the function is
called are i_sb, pointing to the mounted device's super block, and i_ino,
the number of the inode to load.

\ :c:func:`ntfs_read_locked_inode`\  maps, pins and locks the mft record number i_ino
for reading and sets up the necessary \ ``vi``\  fields as well as initializing
the ntfs inode.

Q: What locks are held when the function is called?
A: i_state has I_NEW set, hence the inode is locked, also
i_count is set to 1, so it is not going to go away
i_flags is set to 0 and we have no business touching it.  Only an \ :c:func:`ioctl`\ 
is allowed to write to them. We should of course be honouring them but
we need to do that using the IS\_\* macros defined in include/linux/fs.h.
In any case \ :c:func:`ntfs_read_locked_inode`\  has nothing to do with i_flags.

Return 0 on success and -errno on error.  In the error case, the inode will
have had \ :c:func:`make_bad_inode`\  executed on it.

.. _`ntfs_read_locked_attr_inode`:

ntfs_read_locked_attr_inode
===========================

.. c:function:: int ntfs_read_locked_attr_inode(struct inode *base_vi, struct inode *vi)

    read an attribute inode from its base inode

    :param base_vi:
        base inode
    :type base_vi: struct inode \*

    :param vi:
        attribute inode to read
    :type vi: struct inode \*

.. _`ntfs_read_locked_attr_inode.description`:

Description
-----------

\ :c:func:`ntfs_read_locked_attr_inode`\  is called from \ :c:func:`ntfs_attr_iget`\  to read the
attribute inode described by \ ``vi``\  into memory from the base mft record
described by \ ``base_ni``\ .

\ :c:func:`ntfs_read_locked_attr_inode`\  maps, pins and locks the base inode for
reading and looks up the attribute described by \ ``vi``\  before setting up the
necessary fields in \ ``vi``\  as well as initializing the ntfs inode.

Q: What locks are held when the function is called?
A: i_state has I_NEW set, hence the inode is locked, also
i_count is set to 1, so it is not going to go away

Return 0 on success and -errno on error.  In the error case, the inode will
have had \ :c:func:`make_bad_inode`\  executed on it.

Note this cannot be called for AT_INDEX_ALLOCATION.

.. _`ntfs_read_locked_index_inode`:

ntfs_read_locked_index_inode
============================

.. c:function:: int ntfs_read_locked_index_inode(struct inode *base_vi, struct inode *vi)

    read an index inode from its base inode

    :param base_vi:
        base inode
    :type base_vi: struct inode \*

    :param vi:
        index inode to read
    :type vi: struct inode \*

.. _`ntfs_read_locked_index_inode.description`:

Description
-----------

\ :c:func:`ntfs_read_locked_index_inode`\  is called from \ :c:func:`ntfs_index_iget`\  to read the
index inode described by \ ``vi``\  into memory from the base mft record described
by \ ``base_ni``\ .

\ :c:func:`ntfs_read_locked_index_inode`\  maps, pins and locks the base inode for
reading and looks up the attributes relating to the index described by \ ``vi``\ 
before setting up the necessary fields in \ ``vi``\  as well as initializing the
ntfs inode.

Note, index inodes are essentially attribute inodes (NInoAttr() is true)
with the attribute type set to AT_INDEX_ALLOCATION.  Apart from that, they
are setup like directory inodes since directories are a special case of
indices ao they need to be treated in much the same way.  Most importantly,
for small indices the index allocation attribute might not actually exist.
However, the index root attribute always exists but this does not need to
have an inode associated with it and this is why we define a new inode type
index.  Also, like for directories, we need to have an attribute inode for
the bitmap attribute corresponding to the index allocation attribute and we
can store this in the appropriate field of the inode, just like we do for
normal directory inodes.

Q: What locks are held when the function is called?
A: i_state has I_NEW set, hence the inode is locked, also
i_count is set to 1, so it is not going to go away

Return 0 on success and -errno on error.  In the error case, the inode will
have had \ :c:func:`make_bad_inode`\  executed on it.

.. _`ntfs_read_inode_mount`:

ntfs_read_inode_mount
=====================

.. c:function:: int ntfs_read_inode_mount(struct inode *vi)

    special read_inode for mount time use only

    :param vi:
        inode to read
    :type vi: struct inode \*

.. _`ntfs_read_inode_mount.description`:

Description
-----------

Read inode FILE_MFT at mount time, only called with super_block lock
held from within the \ :c:func:`read_super`\  code path.

This function exists because when it is called the page cache for \ ``$MFT``\ /$DATA
is not initialized and hence we cannot get at the contents of mft records
by calling map_mft_record\*().

Further it needs to cope with the circular references problem, i.e. cannot
load any attributes other than \ ``$ATTRIBUTE_LIST``\  until \ ``$DATA``\  is loaded, because
we do not know where the other extent mft records are yet and again, because
we cannot call map_mft_record\*() yet.  Obviously this applies only when an
attribute list is actually present in \ ``$MFT``\  inode.

We solve these problems by starting with the \ ``$DATA``\  attribute before anything
else and iterating using ntfs_attr_lookup($DATA) over all extents.  As each
extent is found, we \ :c:func:`ntfs_mapping_pairs_decompress`\  including the implied
\ :c:func:`ntfs_runlists_merge`\ .  Each step of the iteration necessarily provides
sufficient information for the next step to complete.

This should work but there are two possible pit falls (see inline comments
below), but only time will tell if they are real pits or just smoke...

.. _`ntfs_evict_big_inode`:

ntfs_evict_big_inode
====================

.. c:function:: void ntfs_evict_big_inode(struct inode *vi)

    clean up the ntfs specific part of an inode

    :param vi:
        vfs inode pending annihilation
    :type vi: struct inode \*

.. _`ntfs_evict_big_inode.description`:

Description
-----------

When the VFS is going to remove an inode from memory, \ :c:func:`ntfs_clear_big_inode`\ 
is called, which deallocates all memory belonging to the NTFS specific part
of the inode and returns.

If the MFT record is dirty, we commit it before doing anything else.

.. _`ntfs_show_options`:

ntfs_show_options
=================

.. c:function:: int ntfs_show_options(struct seq_file *sf, struct dentry *root)

    show mount options in /proc/mounts

    :param sf:
        seq_file in which to write our mount options
    :type sf: struct seq_file \*

    :param root:
        root of the mounted tree whose mount options to display
    :type root: struct dentry \*

.. _`ntfs_show_options.description`:

Description
-----------

Called by the VFS once for each mounted ntfs volume when someone reads
/proc/mounts in order to display the NTFS specific mount options of each
mount. The mount options of fs specified by \ ``root``\  are written to the seq file
\ ``sf``\  and success is returned.

.. _`ntfs_truncate`:

ntfs_truncate
=============

.. c:function:: int ntfs_truncate(struct inode *vi)

    called when the i_size of an ntfs inode is changed

    :param vi:
        inode for which the i_size was changed
    :type vi: struct inode \*

.. _`ntfs_truncate.description`:

Description
-----------

We only support i_size changes for normal files at present, i.e. not
compressed and not encrypted.  This is enforced in \ :c:func:`ntfs_setattr`\ , see
below.

The kernel guarantees that \ ``vi``\  is a regular file (S_ISREG() is true) and
that the change is allowed.

This implies for us that \ ``vi``\  is a file inode rather than a directory, index,
or attribute inode as well as that \ ``vi``\  is a base inode.

Returns 0 on success or -errno on error.

Called with ->i_mutex held.

.. _`ntfs_truncate_vfs`:

ntfs_truncate_vfs
=================

.. c:function:: void ntfs_truncate_vfs(struct inode *vi)

    wrapper for \ :c:func:`ntfs_truncate`\  that has no return value

    :param vi:
        inode for which the i_size was changed
    :type vi: struct inode \*

.. _`ntfs_truncate_vfs.description`:

Description
-----------

Wrapper for \ :c:func:`ntfs_truncate`\  that has no return value.

See \ :c:func:`ntfs_truncate`\  description above for details.

.. _`ntfs_setattr`:

ntfs_setattr
============

.. c:function:: int ntfs_setattr(struct dentry *dentry, struct iattr *attr)

    called from \ :c:func:`notify_change`\  when an attribute is being changed

    :param dentry:
        dentry whose attributes to change
    :type dentry: struct dentry \*

    :param attr:
        structure describing the attributes and the changes
    :type attr: struct iattr \*

.. _`ntfs_setattr.description`:

Description
-----------

We have to trap VFS attempts to truncate the file described by \ ``dentry``\  as
soon as possible, because we do not implement changes in i_size yet.  So we
abort all i_size changes here.

We also abort all changes of user, group, and mode as we do not implement
the NTFS ACLs yet.

Called with ->i_mutex held.

.. _`__ntfs_write_inode`:

\__ntfs_write_inode
===================

.. c:function:: int __ntfs_write_inode(struct inode *vi, int sync)

    write out a dirty inode

    :param vi:
        inode to write out
    :type vi: struct inode \*

    :param sync:
        if true, write out synchronously
    :type sync: int

.. _`__ntfs_write_inode.description`:

Description
-----------

Write out a dirty inode to disk including any extent inodes if present.

If \ ``sync``\  is true, commit the inode to disk and wait for io completion.  This
is done using \ :c:func:`write_mft_record`\ .

If \ ``sync``\  is false, just schedule the write to happen but do not wait for i/o
completion.  In 2.6 kernels, scheduling usually happens just by virtue of
marking the page (and in this case mft record) dirty but we do not implement
this yet as \ :c:func:`write_mft_record`\  largely ignores the \ ``sync``\  parameter and
always performs synchronous writes.

Return 0 on success and -errno on error.

.. This file was automatic generated / don't edit.

