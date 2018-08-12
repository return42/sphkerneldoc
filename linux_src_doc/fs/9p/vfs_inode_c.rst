.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_inode.c

.. _`unixmode2p9mode`:

unixmode2p9mode
===============

.. c:function:: u32 unixmode2p9mode(struct v9fs_session_info *v9ses, umode_t mode)

    convert unix mode bits to plan 9

    :param struct v9fs_session_info \*v9ses:
        v9fs session information

    :param umode_t mode:
        mode to convert

.. _`p9mode2perm`:

p9mode2perm
===========

.. c:function:: int p9mode2perm(struct v9fs_session_info *v9ses, struct p9_wstat *stat)

    convert plan9 mode bits to unix permission bits

    :param struct v9fs_session_info \*v9ses:
        v9fs session information

    :param struct p9_wstat \*stat:
        p9_wstat from which mode need to be derived

.. _`p9mode2unixmode`:

p9mode2unixmode
===============

.. c:function:: umode_t p9mode2unixmode(struct v9fs_session_info *v9ses, struct p9_wstat *stat, dev_t *rdev)

    convert plan9 mode bits to unix mode bits

    :param struct v9fs_session_info \*v9ses:
        v9fs session information

    :param struct p9_wstat \*stat:
        p9_wstat from which mode need to be derived

    :param dev_t \*rdev:
        major number, minor number in case of device files.

.. _`v9fs_uflags2omode`:

v9fs_uflags2omode
=================

.. c:function:: int v9fs_uflags2omode(int uflags, int extended)

    convert posix open flags to plan 9 mode bits

    :param int uflags:
        flags to convert

    :param int extended:
        if .u extensions are active

.. _`v9fs_blank_wstat`:

v9fs_blank_wstat
================

.. c:function:: void v9fs_blank_wstat(struct p9_wstat *wstat)

    helper function to setup a 9P stat structure

    :param struct p9_wstat \*wstat:
        structure to initialize

.. _`v9fs_alloc_inode`:

v9fs_alloc_inode
================

.. c:function:: struct inode *v9fs_alloc_inode(struct super_block *sb)

    helper function to allocate an inode

    :param struct super_block \*sb:
        *undescribed*

.. _`v9fs_i_callback`:

v9fs_i_callback
===============

.. c:function:: void v9fs_i_callback(struct rcu_head *head)

    destroy an inode

    :param struct rcu_head \*head:
        *undescribed*

.. _`v9fs_get_inode`:

v9fs_get_inode
==============

.. c:function:: struct inode *v9fs_get_inode(struct super_block *sb, umode_t mode, dev_t rdev)

    helper function to setup an inode

    :param struct super_block \*sb:
        superblock

    :param umode_t mode:
        mode to setup inode with

    :param dev_t rdev:
        *undescribed*

.. _`v9fs_evict_inode`:

v9fs_evict_inode
================

.. c:function:: void v9fs_evict_inode(struct inode *inode)

    release an inode

    :param struct inode \*inode:
        inode to release

.. _`v9fs_at_to_dotl_flags`:

v9fs_at_to_dotl_flags
=====================

.. c:function:: int v9fs_at_to_dotl_flags(int flags)

    convert Linux specific AT flags to plan 9 AT flag.

    :param int flags:
        flags to convert

.. _`v9fs_dec_count`:

v9fs_dec_count
==============

.. c:function:: void v9fs_dec_count(struct inode *inode)

    helper functon to drop i_nlink.

    :param struct inode \*inode:
        inode whose nlink is being dropped

.. _`v9fs_dec_count.description`:

Description
-----------

If a directory had nlink <= 2 (including . and ..), then we should not drop
the link count, which indicates the underlying exported fs doesn't maintain
nlink accurately. e.g.
- overlayfs sets nlink to 1 for merged dir
- ext4 (with dir_nlink feature enabled) sets nlink to 1 if a dir has more
than EXT4_LINK_MAX (65000) links.

.. _`v9fs_remove`:

v9fs_remove
===========

.. c:function:: int v9fs_remove(struct inode *dir, struct dentry *dentry, int flags)

    helper function to remove files and directories

    :param struct inode \*dir:
        directory inode that is being deleted

    :param struct dentry \*dentry:
        dentry that is being deleted

    :param int flags:
        removing a directory

.. _`v9fs_create`:

v9fs_create
===========

.. c:function:: struct p9_fid *v9fs_create(struct v9fs_session_info *v9ses, struct inode *dir, struct dentry *dentry, char *extension, u32 perm, u8 mode)

    Create a file

    :param struct v9fs_session_info \*v9ses:
        session information

    :param struct inode \*dir:
        directory that dentry is being created in

    :param struct dentry \*dentry:
        dentry that is being created

    :param char \*extension:
        9p2000.u extension string to support devices, etc.

    :param u32 perm:
        create permissions

    :param u8 mode:
        open mode

.. _`v9fs_vfs_create`:

v9fs_vfs_create
===============

.. c:function:: int v9fs_vfs_create(struct inode *dir, struct dentry *dentry, umode_t mode, bool excl)

    VFS hook to create a regular file

    :param struct inode \*dir:
        directory inode that is being created

    :param struct dentry \*dentry:
        dentry that is being deleted

    :param umode_t mode:
        create permissions

    :param bool excl:
        *undescribed*

.. _`v9fs_vfs_create.description`:

Description
-----------

open(.., O_CREAT) is handled in \ :c:func:`v9fs_vfs_atomic_open`\ .  This is only called
for mknod(2).

.. _`v9fs_vfs_mkdir`:

v9fs_vfs_mkdir
==============

.. c:function:: int v9fs_vfs_mkdir(struct inode *dir, struct dentry *dentry, umode_t mode)

    VFS mkdir hook to create a directory

    :param struct inode \*dir:
        inode that is being unlinked

    :param struct dentry \*dentry:
        dentry that is being unlinked

    :param umode_t mode:
        mode for new directory

.. _`v9fs_vfs_lookup`:

v9fs_vfs_lookup
===============

.. c:function:: struct dentry *v9fs_vfs_lookup(struct inode *dir, struct dentry *dentry, unsigned int flags)

    VFS lookup hook to "walk" to a new inode

    :param struct inode \*dir:
        inode that is being walked from

    :param struct dentry \*dentry:
        dentry that is being walked to?

    :param unsigned int flags:
        lookup flags (unused)

.. _`v9fs_vfs_unlink`:

v9fs_vfs_unlink
===============

.. c:function:: int v9fs_vfs_unlink(struct inode *i, struct dentry *d)

    VFS unlink hook to delete an inode

    :param struct inode \*i:
        inode that is being unlinked

    :param struct dentry \*d:
        dentry that is being unlinked

.. _`v9fs_vfs_rmdir`:

v9fs_vfs_rmdir
==============

.. c:function:: int v9fs_vfs_rmdir(struct inode *i, struct dentry *d)

    VFS unlink hook to delete a directory

    :param struct inode \*i:
        inode that is being unlinked

    :param struct dentry \*d:
        dentry that is being unlinked

.. _`v9fs_vfs_rename`:

v9fs_vfs_rename
===============

.. c:function:: int v9fs_vfs_rename(struct inode *old_dir, struct dentry *old_dentry, struct inode *new_dir, struct dentry *new_dentry, unsigned int flags)

    VFS hook to rename an inode

    :param struct inode \*old_dir:
        old dir inode

    :param struct dentry \*old_dentry:
        old dentry

    :param struct inode \*new_dir:
        new dir inode

    :param struct dentry \*new_dentry:
        new dentry

    :param unsigned int flags:
        *undescribed*

.. _`v9fs_vfs_getattr`:

v9fs_vfs_getattr
================

.. c:function:: int v9fs_vfs_getattr(const struct path *path, struct kstat *stat, u32 request_mask, unsigned int flags)

    retrieve file metadata

    :param const struct path \*path:
        Object to query

    :param struct kstat \*stat:
        metadata structure to populate

    :param u32 request_mask:
        Mask of STATX_xxx flags indicating the caller's interests

    :param unsigned int flags:
        AT_STATX_xxx setting

.. _`v9fs_vfs_setattr`:

v9fs_vfs_setattr
================

.. c:function:: int v9fs_vfs_setattr(struct dentry *dentry, struct iattr *iattr)

    set file metadata

    :param struct dentry \*dentry:
        file whose metadata to set

    :param struct iattr \*iattr:
        metadata assignment structure

.. _`v9fs_stat2inode`:

v9fs_stat2inode
===============

.. c:function:: void v9fs_stat2inode(struct p9_wstat *stat, struct inode *inode, struct super_block *sb)

    populate an inode structure with mistat info

    :param struct p9_wstat \*stat:
        Plan 9 metadata (mistat) structure

    :param struct inode \*inode:
        inode to populate

    :param struct super_block \*sb:
        superblock of filesystem

.. _`v9fs_qid2ino`:

v9fs_qid2ino
============

.. c:function:: ino_t v9fs_qid2ino(struct p9_qid *qid)

    convert qid into inode number

    :param struct p9_qid \*qid:
        qid to hash

.. _`v9fs_qid2ino.bug`:

BUG
---

potential for inode number collisions?

.. _`v9fs_vfs_get_link`:

v9fs_vfs_get_link
=================

.. c:function:: const char *v9fs_vfs_get_link(struct dentry *dentry, struct inode *inode, struct delayed_call *done)

    follow a symlink path

    :param struct dentry \*dentry:
        dentry for symlink

    :param struct inode \*inode:
        inode for symlink

    :param struct delayed_call \*done:
        delayed call for when we are done with the return value

.. _`v9fs_vfs_mkspecial`:

v9fs_vfs_mkspecial
==================

.. c:function:: int v9fs_vfs_mkspecial(struct inode *dir, struct dentry *dentry, u32 perm, const char *extension)

    create a special file

    :param struct inode \*dir:
        inode to create special file in

    :param struct dentry \*dentry:
        dentry to create

    :param u32 perm:
        mode to create special file

    :param const char \*extension:
        9p2000.u format extension string representing special file

.. _`v9fs_vfs_symlink`:

v9fs_vfs_symlink
================

.. c:function:: int v9fs_vfs_symlink(struct inode *dir, struct dentry *dentry, const char *symname)

    helper function to create symlinks

    :param struct inode \*dir:
        directory inode containing symlink

    :param struct dentry \*dentry:
        dentry for symlink

    :param const char \*symname:
        symlink data

.. _`v9fs_vfs_symlink.see-also`:

See Also
--------

9P2000.u RFC for more information

.. _`v9fs_vfs_link`:

v9fs_vfs_link
=============

.. c:function:: int v9fs_vfs_link(struct dentry *old_dentry, struct inode *dir, struct dentry *dentry)

    create a hardlink

    :param struct dentry \*old_dentry:
        dentry for file to link to

    :param struct inode \*dir:
        inode destination for new link

    :param struct dentry \*dentry:
        dentry for link

.. _`v9fs_vfs_mknod`:

v9fs_vfs_mknod
==============

.. c:function:: int v9fs_vfs_mknod(struct inode *dir, struct dentry *dentry, umode_t mode, dev_t rdev)

    create a special file

    :param struct inode \*dir:
        inode destination for new link

    :param struct dentry \*dentry:
        dentry for file

    :param umode_t mode:
        mode for creation

    :param dev_t rdev:
        device associated with special file

.. This file was automatic generated / don't edit.

