.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_inode.c

.. _`unixmode2p9mode`:

unixmode2p9mode
===============

.. c:function:: u32 unixmode2p9mode(struct v9fs_session_info *v9ses, umode_t mode)

    convert unix mode bits to plan 9

    :param v9ses:
        v9fs session information
    :type v9ses: struct v9fs_session_info \*

    :param mode:
        mode to convert
    :type mode: umode_t

.. _`p9mode2perm`:

p9mode2perm
===========

.. c:function:: int p9mode2perm(struct v9fs_session_info *v9ses, struct p9_wstat *stat)

    convert plan9 mode bits to unix permission bits

    :param v9ses:
        v9fs session information
    :type v9ses: struct v9fs_session_info \*

    :param stat:
        p9_wstat from which mode need to be derived
    :type stat: struct p9_wstat \*

.. _`p9mode2unixmode`:

p9mode2unixmode
===============

.. c:function:: umode_t p9mode2unixmode(struct v9fs_session_info *v9ses, struct p9_wstat *stat, dev_t *rdev)

    convert plan9 mode bits to unix mode bits

    :param v9ses:
        v9fs session information
    :type v9ses: struct v9fs_session_info \*

    :param stat:
        p9_wstat from which mode need to be derived
    :type stat: struct p9_wstat \*

    :param rdev:
        major number, minor number in case of device files.
    :type rdev: dev_t \*

.. _`v9fs_uflags2omode`:

v9fs_uflags2omode
=================

.. c:function:: int v9fs_uflags2omode(int uflags, int extended)

    convert posix open flags to plan 9 mode bits

    :param uflags:
        flags to convert
    :type uflags: int

    :param extended:
        if .u extensions are active
    :type extended: int

.. _`v9fs_blank_wstat`:

v9fs_blank_wstat
================

.. c:function:: void v9fs_blank_wstat(struct p9_wstat *wstat)

    helper function to setup a 9P stat structure

    :param wstat:
        structure to initialize
    :type wstat: struct p9_wstat \*

.. _`v9fs_alloc_inode`:

v9fs_alloc_inode
================

.. c:function:: struct inode *v9fs_alloc_inode(struct super_block *sb)

    helper function to allocate an inode

    :param sb:
        *undescribed*
    :type sb: struct super_block \*

.. _`v9fs_i_callback`:

v9fs_i_callback
===============

.. c:function:: void v9fs_i_callback(struct rcu_head *head)

    destroy an inode

    :param head:
        *undescribed*
    :type head: struct rcu_head \*

.. _`v9fs_get_inode`:

v9fs_get_inode
==============

.. c:function:: struct inode *v9fs_get_inode(struct super_block *sb, umode_t mode, dev_t rdev)

    helper function to setup an inode

    :param sb:
        superblock
    :type sb: struct super_block \*

    :param mode:
        mode to setup inode with
    :type mode: umode_t

    :param rdev:
        *undescribed*
    :type rdev: dev_t

.. _`v9fs_evict_inode`:

v9fs_evict_inode
================

.. c:function:: void v9fs_evict_inode(struct inode *inode)

    release an inode

    :param inode:
        inode to release
    :type inode: struct inode \*

.. _`v9fs_at_to_dotl_flags`:

v9fs_at_to_dotl_flags
=====================

.. c:function:: int v9fs_at_to_dotl_flags(int flags)

    convert Linux specific AT flags to plan 9 AT flag.

    :param flags:
        flags to convert
    :type flags: int

.. _`v9fs_dec_count`:

v9fs_dec_count
==============

.. c:function:: void v9fs_dec_count(struct inode *inode)

    helper functon to drop i_nlink.

    :param inode:
        inode whose nlink is being dropped
    :type inode: struct inode \*

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

    :param dir:
        directory inode that is being deleted
    :type dir: struct inode \*

    :param dentry:
        dentry that is being deleted
    :type dentry: struct dentry \*

    :param flags:
        removing a directory
    :type flags: int

.. _`v9fs_create`:

v9fs_create
===========

.. c:function:: struct p9_fid *v9fs_create(struct v9fs_session_info *v9ses, struct inode *dir, struct dentry *dentry, char *extension, u32 perm, u8 mode)

    Create a file

    :param v9ses:
        session information
    :type v9ses: struct v9fs_session_info \*

    :param dir:
        directory that dentry is being created in
    :type dir: struct inode \*

    :param dentry:
        dentry that is being created
    :type dentry: struct dentry \*

    :param extension:
        9p2000.u extension string to support devices, etc.
    :type extension: char \*

    :param perm:
        create permissions
    :type perm: u32

    :param mode:
        open mode
    :type mode: u8

.. _`v9fs_vfs_create`:

v9fs_vfs_create
===============

.. c:function:: int v9fs_vfs_create(struct inode *dir, struct dentry *dentry, umode_t mode, bool excl)

    VFS hook to create a regular file

    :param dir:
        directory inode that is being created
    :type dir: struct inode \*

    :param dentry:
        dentry that is being deleted
    :type dentry: struct dentry \*

    :param mode:
        create permissions
    :type mode: umode_t

    :param excl:
        *undescribed*
    :type excl: bool

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

    :param dir:
        inode that is being unlinked
    :type dir: struct inode \*

    :param dentry:
        dentry that is being unlinked
    :type dentry: struct dentry \*

    :param mode:
        mode for new directory
    :type mode: umode_t

.. _`v9fs_vfs_lookup`:

v9fs_vfs_lookup
===============

.. c:function:: struct dentry *v9fs_vfs_lookup(struct inode *dir, struct dentry *dentry, unsigned int flags)

    VFS lookup hook to "walk" to a new inode

    :param dir:
        inode that is being walked from
    :type dir: struct inode \*

    :param dentry:
        dentry that is being walked to?
    :type dentry: struct dentry \*

    :param flags:
        lookup flags (unused)
    :type flags: unsigned int

.. _`v9fs_vfs_unlink`:

v9fs_vfs_unlink
===============

.. c:function:: int v9fs_vfs_unlink(struct inode *i, struct dentry *d)

    VFS unlink hook to delete an inode

    :param i:
        inode that is being unlinked
    :type i: struct inode \*

    :param d:
        dentry that is being unlinked
    :type d: struct dentry \*

.. _`v9fs_vfs_rmdir`:

v9fs_vfs_rmdir
==============

.. c:function:: int v9fs_vfs_rmdir(struct inode *i, struct dentry *d)

    VFS unlink hook to delete a directory

    :param i:
        inode that is being unlinked
    :type i: struct inode \*

    :param d:
        dentry that is being unlinked
    :type d: struct dentry \*

.. _`v9fs_vfs_rename`:

v9fs_vfs_rename
===============

.. c:function:: int v9fs_vfs_rename(struct inode *old_dir, struct dentry *old_dentry, struct inode *new_dir, struct dentry *new_dentry, unsigned int flags)

    VFS hook to rename an inode

    :param old_dir:
        old dir inode
    :type old_dir: struct inode \*

    :param old_dentry:
        old dentry
    :type old_dentry: struct dentry \*

    :param new_dir:
        new dir inode
    :type new_dir: struct inode \*

    :param new_dentry:
        new dentry
    :type new_dentry: struct dentry \*

    :param flags:
        *undescribed*
    :type flags: unsigned int

.. _`v9fs_vfs_getattr`:

v9fs_vfs_getattr
================

.. c:function:: int v9fs_vfs_getattr(const struct path *path, struct kstat *stat, u32 request_mask, unsigned int flags)

    retrieve file metadata

    :param path:
        Object to query
    :type path: const struct path \*

    :param stat:
        metadata structure to populate
    :type stat: struct kstat \*

    :param request_mask:
        Mask of STATX_xxx flags indicating the caller's interests
    :type request_mask: u32

    :param flags:
        AT_STATX_xxx setting
    :type flags: unsigned int

.. _`v9fs_vfs_setattr`:

v9fs_vfs_setattr
================

.. c:function:: int v9fs_vfs_setattr(struct dentry *dentry, struct iattr *iattr)

    set file metadata

    :param dentry:
        file whose metadata to set
    :type dentry: struct dentry \*

    :param iattr:
        metadata assignment structure
    :type iattr: struct iattr \*

.. _`v9fs_stat2inode`:

v9fs_stat2inode
===============

.. c:function:: void v9fs_stat2inode(struct p9_wstat *stat, struct inode *inode, struct super_block *sb)

    populate an inode structure with mistat info

    :param stat:
        Plan 9 metadata (mistat) structure
    :type stat: struct p9_wstat \*

    :param inode:
        inode to populate
    :type inode: struct inode \*

    :param sb:
        superblock of filesystem
    :type sb: struct super_block \*

.. _`v9fs_qid2ino`:

v9fs_qid2ino
============

.. c:function:: ino_t v9fs_qid2ino(struct p9_qid *qid)

    convert qid into inode number

    :param qid:
        qid to hash
    :type qid: struct p9_qid \*

.. _`v9fs_qid2ino.bug`:

BUG
---

potential for inode number collisions?

.. _`v9fs_vfs_get_link`:

v9fs_vfs_get_link
=================

.. c:function:: const char *v9fs_vfs_get_link(struct dentry *dentry, struct inode *inode, struct delayed_call *done)

    follow a symlink path

    :param dentry:
        dentry for symlink
    :type dentry: struct dentry \*

    :param inode:
        inode for symlink
    :type inode: struct inode \*

    :param done:
        delayed call for when we are done with the return value
    :type done: struct delayed_call \*

.. _`v9fs_vfs_mkspecial`:

v9fs_vfs_mkspecial
==================

.. c:function:: int v9fs_vfs_mkspecial(struct inode *dir, struct dentry *dentry, u32 perm, const char *extension)

    create a special file

    :param dir:
        inode to create special file in
    :type dir: struct inode \*

    :param dentry:
        dentry to create
    :type dentry: struct dentry \*

    :param perm:
        mode to create special file
    :type perm: u32

    :param extension:
        9p2000.u format extension string representing special file
    :type extension: const char \*

.. _`v9fs_vfs_symlink`:

v9fs_vfs_symlink
================

.. c:function:: int v9fs_vfs_symlink(struct inode *dir, struct dentry *dentry, const char *symname)

    helper function to create symlinks

    :param dir:
        directory inode containing symlink
    :type dir: struct inode \*

    :param dentry:
        dentry for symlink
    :type dentry: struct dentry \*

    :param symname:
        symlink data
    :type symname: const char \*

.. _`v9fs_vfs_symlink.see-also`:

See Also
--------

9P2000.u RFC for more information

.. _`v9fs_vfs_link`:

v9fs_vfs_link
=============

.. c:function:: int v9fs_vfs_link(struct dentry *old_dentry, struct inode *dir, struct dentry *dentry)

    create a hardlink

    :param old_dentry:
        dentry for file to link to
    :type old_dentry: struct dentry \*

    :param dir:
        inode destination for new link
    :type dir: struct inode \*

    :param dentry:
        dentry for link
    :type dentry: struct dentry \*

.. _`v9fs_vfs_mknod`:

v9fs_vfs_mknod
==============

.. c:function:: int v9fs_vfs_mknod(struct inode *dir, struct dentry *dentry, umode_t mode, dev_t rdev)

    create a special file

    :param dir:
        inode destination for new link
    :type dir: struct inode \*

    :param dentry:
        dentry for file
    :type dentry: struct dentry \*

    :param mode:
        mode for creation
    :type mode: umode_t

    :param rdev:
        device associated with special file
    :type rdev: dev_t

.. This file was automatic generated / don't edit.

