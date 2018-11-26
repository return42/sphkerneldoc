.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/journal.c

.. _`zero_ino_node_unused`:

zero_ino_node_unused
====================

.. c:function:: void zero_ino_node_unused(struct ubifs_ino_node *ino)

    zero out unused fields of an on-flash inode node.

    :param ino:
        the inode to zero out
    :type ino: struct ubifs_ino_node \*

.. _`zero_dent_node_unused`:

zero_dent_node_unused
=====================

.. c:function:: void zero_dent_node_unused(struct ubifs_dent_node *dent)

    zero out unused fields of an on-flash directory entry node.

    :param dent:
        the directory entry to zero out
    :type dent: struct ubifs_dent_node \*

.. _`zero_trun_node_unused`:

zero_trun_node_unused
=====================

.. c:function:: void zero_trun_node_unused(struct ubifs_trun_node *trun)

    zero out unused fields of an on-flash truncation node.

    :param trun:
        the truncation node to zero out
    :type trun: struct ubifs_trun_node \*

.. _`reserve_space`:

reserve_space
=============

.. c:function:: int reserve_space(struct ubifs_info *c, int jhead, int len)

    reserve space in the journal.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param jhead:
        journal head number
    :type jhead: int

    :param len:
        node length
    :type len: int

.. _`reserve_space.description`:

Description
-----------

This function reserves space in journal head \ ``head``\ . If the reservation
succeeded, the journal head stays locked and later has to be unlocked using
'release_head()'. Returns zero in case of success, \ ``-EAGAIN``\  if commit has to
be done, and other negative error codes in case of other failures.

.. _`write_head`:

write_head
==========

.. c:function:: int write_head(struct ubifs_info *c, int jhead, void *buf, int len, int *lnum, int *offs, int sync)

    write data to a journal head.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param jhead:
        journal head
    :type jhead: int

    :param buf:
        buffer to write
    :type buf: void \*

    :param len:
        length to write
    :type len: int

    :param lnum:
        LEB number written is returned here
    :type lnum: int \*

    :param offs:
        offset written is returned here
    :type offs: int \*

    :param sync:
        non-zero if the write-buffer has to by synchronized
    :type sync: int

.. _`write_head.description`:

Description
-----------

This function writes data to the reserved space of journal head \ ``jhead``\ .
Returns zero in case of success and a negative error code in case of
failure.

.. _`make_reservation`:

make_reservation
================

.. c:function:: int make_reservation(struct ubifs_info *c, int jhead, int len)

    reserve journal space.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param jhead:
        journal head
    :type jhead: int

    :param len:
        how many bytes to reserve
    :type len: int

.. _`make_reservation.description`:

Description
-----------

This function makes space reservation in journal head \ ``jhead``\ . The function
takes the commit lock and locks the journal head, and the caller has to
unlock the head and finish the reservation with 'finish_reservation()'.
Returns zero in case of success and a negative error code in case of
failure.

Note, the journal head may be unlocked as soon as the data is written, while
the commit lock has to be released after the data has been added to the
TNC.

.. _`release_head`:

release_head
============

.. c:function:: void release_head(struct ubifs_info *c, int jhead)

    release a journal head.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param jhead:
        journal head
    :type jhead: int

.. _`release_head.description`:

Description
-----------

This function releases journal head \ ``jhead``\  which was locked by
the 'make_reservation()' function. It has to be called after each successful
'make_reservation()' invocation.

.. _`finish_reservation`:

finish_reservation
==================

.. c:function:: void finish_reservation(struct ubifs_info *c)

    finish a reservation.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

.. _`finish_reservation.description`:

Description
-----------

This function finishes journal space reservation. It must be called after
'make_reservation()'.

.. _`get_dent_type`:

get_dent_type
=============

.. c:function:: int get_dent_type(int mode)

    translate VFS inode mode to UBIFS directory entry type.

    :param mode:
        inode mode
    :type mode: int

.. _`pack_inode`:

pack_inode
==========

.. c:function:: void pack_inode(struct ubifs_info *c, struct ubifs_ino_node *ino, const struct inode *inode, int last)

    pack an inode node.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param ino:
        buffer in which to pack inode node
    :type ino: struct ubifs_ino_node \*

    :param inode:
        inode to pack
    :type inode: const struct inode \*

    :param last:
        indicates the last node of the group
    :type last: int

.. _`mark_inode_clean`:

mark_inode_clean
================

.. c:function:: void mark_inode_clean(struct ubifs_info *c, struct ubifs_inode *ui)

    mark UBIFS inode as clean.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param ui:
        UBIFS inode to mark as clean
    :type ui: struct ubifs_inode \*

.. _`mark_inode_clean.description`:

Description
-----------

This helper function marks UBIFS inode \ ``ui``\  as clean by cleaning the
\ ``ui->dirty``\  flag and releasing its budget. Note, VFS may still treat the
inode as dirty and try to write it back, but 'ubifs_write_inode()' would
just do nothing.

.. _`ubifs_jnl_update`:

ubifs_jnl_update
================

.. c:function:: int ubifs_jnl_update(struct ubifs_info *c, const struct inode *dir, const struct fscrypt_name *nm, const struct inode *inode, int deletion, int xent)

    update inode.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param dir:
        parent inode or host inode in case of extended attributes
    :type dir: const struct inode \*

    :param nm:
        directory entry name
    :type nm: const struct fscrypt_name \*

    :param inode:
        inode to update
    :type inode: const struct inode \*

    :param deletion:
        indicates a directory entry deletion i.e unlink or rmdir
    :type deletion: int

    :param xent:
        non-zero if the directory entry is an extended attribute entry
    :type xent: int

.. _`ubifs_jnl_update.description`:

Description
-----------

This function updates an inode by writing a directory entry (or extended
attribute entry), the inode itself, and the parent directory inode (or the
host inode) to the journal.

The function writes the host inode \ ``dir``\  last, which is important in case of
extended attributes. Indeed, then we guarantee that if the host inode gets
synchronized (with 'fsync()'), and the write-buffer it sits in gets flushed,
the extended attribute inode gets flushed too. And this is exactly what the
user expects - synchronizing the host inode synchronizes its extended
attributes. Similarly, this guarantees that if \ ``dir``\  is synchronized, its
directory entry corresponding to \ ``nm``\  gets synchronized too.

If the inode (@inode) or the parent directory (@dir) are synchronous, this
function synchronizes the write-buffer.

This function marks the \ ``dir``\  and \ ``inode``\  inodes as clean and returns zero on
success. In case of failure, a negative error code is returned.

.. _`ubifs_jnl_write_data`:

ubifs_jnl_write_data
====================

.. c:function:: int ubifs_jnl_write_data(struct ubifs_info *c, const struct inode *inode, const union ubifs_key *key, const void *buf, int len)

    write a data node to the journal.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param inode:
        inode the data node belongs to
    :type inode: const struct inode \*

    :param key:
        node key
    :type key: const union ubifs_key \*

    :param buf:
        buffer to write
    :type buf: const void \*

    :param len:
        data length (must not exceed \ ``UBIFS_BLOCK_SIZE``\ )
    :type len: int

.. _`ubifs_jnl_write_data.description`:

Description
-----------

This function writes a data node to the journal. Returns \ ``0``\  if the data node
was successfully written, and a negative error code in case of failure.

.. _`ubifs_jnl_write_inode`:

ubifs_jnl_write_inode
=====================

.. c:function:: int ubifs_jnl_write_inode(struct ubifs_info *c, const struct inode *inode)

    flush inode to the journal.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param inode:
        inode to flush
    :type inode: const struct inode \*

.. _`ubifs_jnl_write_inode.description`:

Description
-----------

This function writes inode \ ``inode``\  to the journal. If the inode is
synchronous, it also synchronizes the write-buffer. Returns zero in case of
success and a negative error code in case of failure.

.. _`ubifs_jnl_delete_inode`:

ubifs_jnl_delete_inode
======================

.. c:function:: int ubifs_jnl_delete_inode(struct ubifs_info *c, const struct inode *inode)

    delete an inode.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param inode:
        inode to delete
    :type inode: const struct inode \*

.. _`ubifs_jnl_delete_inode.description`:

Description
-----------

This function deletes inode \ ``inode``\  which includes removing it from orphans,
deleting it from TNC and, in some cases, writing a deletion inode to the
journal.

When regular file inodes are unlinked or a directory inode is removed, the
'ubifs_jnl_update()' function writes a corresponding deletion inode and
direntry to the media, and adds the inode to orphans. After this, when the
last reference to this inode has been dropped, this function is called. In
general, it has to write one more deletion inode to the media, because if
a commit happened between 'ubifs_jnl_update()' and
'ubifs_jnl_delete_inode()', the deletion inode is not in the journal
anymore, and in fact it might not be on the flash anymore, because it might
have been garbage-collected already. And for optimization reasons UBIFS does
not read the orphan area if it has been unmounted cleanly, so it would have
no indication in the journal that there is a deleted inode which has to be
removed from TNC.

However, if there was no commit between 'ubifs_jnl_update()' and
'ubifs_jnl_delete_inode()', then there is no need to write the deletion
inode to the media for the second time. And this is quite a typical case.

This function returns zero in case of success and a negative error code in
case of failure.

.. _`ubifs_jnl_xrename`:

ubifs_jnl_xrename
=================

.. c:function:: int ubifs_jnl_xrename(struct ubifs_info *c, const struct inode *fst_dir, const struct inode *fst_inode, const struct fscrypt_name *fst_nm, const struct inode *snd_dir, const struct inode *snd_inode, const struct fscrypt_name *snd_nm, int sync)

    cross rename two directory entries.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param fst_dir:
        parent inode of 1st directory entry to exchange
    :type fst_dir: const struct inode \*

    :param fst_inode:
        1st inode to exchange
    :type fst_inode: const struct inode \*

    :param fst_nm:
        name of 1st inode to exchange
    :type fst_nm: const struct fscrypt_name \*

    :param snd_dir:
        parent inode of 2nd directory entry to exchange
    :type snd_dir: const struct inode \*

    :param snd_inode:
        2nd inode to exchange
    :type snd_inode: const struct inode \*

    :param snd_nm:
        name of 2nd inode to exchange
    :type snd_nm: const struct fscrypt_name \*

    :param sync:
        non-zero if the write-buffer has to be synchronized
    :type sync: int

.. _`ubifs_jnl_xrename.description`:

Description
-----------

This function implements the cross rename operation which may involve
writing 2 inodes and 2 directory entries. It marks the written inodes as clean
and returns zero on success. In case of failure, a negative error code is
returned.

.. _`ubifs_jnl_rename`:

ubifs_jnl_rename
================

.. c:function:: int ubifs_jnl_rename(struct ubifs_info *c, const struct inode *old_dir, const struct inode *old_inode, const struct fscrypt_name *old_nm, const struct inode *new_dir, const struct inode *new_inode, const struct fscrypt_name *new_nm, const struct inode *whiteout, int sync)

    rename a directory entry.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param old_dir:
        parent inode of directory entry to rename
    :type old_dir: const struct inode \*

    :param old_inode:
        *undescribed*
    :type old_inode: const struct inode \*

    :param old_nm:
        *undescribed*
    :type old_nm: const struct fscrypt_name \*

    :param new_dir:
        parent inode of directory entry to rename
    :type new_dir: const struct inode \*

    :param new_inode:
        *undescribed*
    :type new_inode: const struct inode \*

    :param new_nm:
        *undescribed*
    :type new_nm: const struct fscrypt_name \*

    :param whiteout:
        *undescribed*
    :type whiteout: const struct inode \*

    :param sync:
        non-zero if the write-buffer has to be synchronized
    :type sync: int

.. _`ubifs_jnl_rename.description`:

Description
-----------

This function implements the re-name operation which may involve writing up
to 4 inodes and 2 directory entries. It marks the written inodes as clean
and returns zero on success. In case of failure, a negative error code is
returned.

.. _`truncate_data_node`:

truncate_data_node
==================

.. c:function:: int truncate_data_node(const struct ubifs_info *c, const struct inode *inode, unsigned int block, struct ubifs_data_node *dn, int *new_len)

    re-compress/encrypt a truncated data node.

    :param c:
        UBIFS file-system description object
    :type c: const struct ubifs_info \*

    :param inode:
        inode which referes to the data node
    :type inode: const struct inode \*

    :param block:
        data block number
    :type block: unsigned int

    :param dn:
        data node to re-compress
    :type dn: struct ubifs_data_node \*

    :param new_len:
        new length
    :type new_len: int \*

.. _`truncate_data_node.description`:

Description
-----------

This function is used when an inode is truncated and the last data node of
the inode has to be re-compressed/encrypted and re-written.

.. _`ubifs_jnl_truncate`:

ubifs_jnl_truncate
==================

.. c:function:: int ubifs_jnl_truncate(struct ubifs_info *c, const struct inode *inode, loff_t old_size, loff_t new_size)

    update the journal for a truncation.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param inode:
        inode to truncate
    :type inode: const struct inode \*

    :param old_size:
        old size
    :type old_size: loff_t

    :param new_size:
        new size
    :type new_size: loff_t

.. _`ubifs_jnl_truncate.description`:

Description
-----------

When the size of a file decreases due to truncation, a truncation node is
written, the journal tree is updated, and the last data block is re-written
if it has been affected. The inode is also updated in order to synchronize
the new inode size.

This function marks the inode as clean and returns zero on success. In case
of failure, a negative error code is returned.

.. _`ubifs_jnl_delete_xattr`:

ubifs_jnl_delete_xattr
======================

.. c:function:: int ubifs_jnl_delete_xattr(struct ubifs_info *c, const struct inode *host, const struct inode *inode, const struct fscrypt_name *nm)

    delete an extended attribute.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param host:
        host inode
    :type host: const struct inode \*

    :param inode:
        extended attribute inode
    :type inode: const struct inode \*

    :param nm:
        extended attribute entry name
    :type nm: const struct fscrypt_name \*

.. _`ubifs_jnl_delete_xattr.description`:

Description
-----------

This function delete an extended attribute which is very similar to
un-linking regular files - it writes a deletion xentry, a deletion inode and
updates the target inode. Returns zero in case of success and a negative
error code in case of failure.

.. _`ubifs_jnl_change_xattr`:

ubifs_jnl_change_xattr
======================

.. c:function:: int ubifs_jnl_change_xattr(struct ubifs_info *c, const struct inode *inode, const struct inode *host)

    change an extended attribute.

    :param c:
        UBIFS file-system description object
    :type c: struct ubifs_info \*

    :param inode:
        extended attribute inode
    :type inode: const struct inode \*

    :param host:
        host inode
    :type host: const struct inode \*

.. _`ubifs_jnl_change_xattr.description`:

Description
-----------

This function writes the updated version of an extended attribute inode and
the host inode to the journal (to the base head). The host inode is written
after the extended attribute inode in order to guarantee that the extended
attribute will be flushed when the inode is synchronized by 'fsync()' and
consequently, the write-buffer is synchronized. This function returns zero
in case of success and a negative error code in case of failure.

.. This file was automatic generated / don't edit.

