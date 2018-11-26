.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_inode_dotl.c

.. _`v9fs_get_fsgid_for_create`:

v9fs_get_fsgid_for_create
=========================

.. c:function:: kgid_t v9fs_get_fsgid_for_create(struct inode *dir_inode)

    Helper function to get the gid for creating a new file system object. This checks the S_ISGID to determine the owning group of the new file system object.

    :param dir_inode:
        *undescribed*
    :type dir_inode: struct inode \*

.. _`v9fs_open_to_dotl_flags`:

v9fs_open_to_dotl_flags
=======================

.. c:function:: int v9fs_open_to_dotl_flags(int flags)

    convert Linux specific open flags to plan 9 open flag.

    :param flags:
        flags to convert
    :type flags: int

.. _`v9fs_vfs_create_dotl`:

v9fs_vfs_create_dotl
====================

.. c:function:: int v9fs_vfs_create_dotl(struct inode *dir, struct dentry *dentry, umode_t omode, bool excl)

    VFS hook to create files for 9P2000.L protocol.

    :param dir:
        directory inode that is being created
    :type dir: struct inode \*

    :param dentry:
        dentry that is being deleted
    :type dentry: struct dentry \*

    :param omode:
        create permissions
    :type omode: umode_t

    :param excl:
        *undescribed*
    :type excl: bool

.. _`v9fs_vfs_mkdir_dotl`:

v9fs_vfs_mkdir_dotl
===================

.. c:function:: int v9fs_vfs_mkdir_dotl(struct inode *dir, struct dentry *dentry, umode_t omode)

    VFS mkdir hook to create a directory

    :param dir:
        inode that is being unlinked
    :type dir: struct inode \*

    :param dentry:
        dentry that is being unlinked
    :type dentry: struct dentry \*

    :param omode:
        mode for new directory
    :type omode: umode_t

.. _`v9fs_vfs_setattr_dotl`:

v9fs_vfs_setattr_dotl
=====================

.. c:function:: int v9fs_vfs_setattr_dotl(struct dentry *dentry, struct iattr *iattr)

    set file metadata

    :param dentry:
        file whose metadata to set
    :type dentry: struct dentry \*

    :param iattr:
        metadata assignment structure
    :type iattr: struct iattr \*

.. _`v9fs_stat2inode_dotl`:

v9fs_stat2inode_dotl
====================

.. c:function:: void v9fs_stat2inode_dotl(struct p9_stat_dotl *stat, struct inode *inode)

    populate an inode structure with stat info

    :param stat:
        stat structure
    :type stat: struct p9_stat_dotl \*

    :param inode:
        inode to populate
    :type inode: struct inode \*

.. _`v9fs_vfs_link_dotl`:

v9fs_vfs_link_dotl
==================

.. c:function:: int v9fs_vfs_link_dotl(struct dentry *old_dentry, struct inode *dir, struct dentry *dentry)

    create a hardlink for dotl

    :param old_dentry:
        dentry for file to link to
    :type old_dentry: struct dentry \*

    :param dir:
        inode destination for new link
    :type dir: struct inode \*

    :param dentry:
        dentry for link
    :type dentry: struct dentry \*

.. _`v9fs_vfs_mknod_dotl`:

v9fs_vfs_mknod_dotl
===================

.. c:function:: int v9fs_vfs_mknod_dotl(struct inode *dir, struct dentry *dentry, umode_t omode, dev_t rdev)

    create a special file

    :param dir:
        inode destination for new link
    :type dir: struct inode \*

    :param dentry:
        dentry for file
    :type dentry: struct dentry \*

    :param omode:
        mode for creation
    :type omode: umode_t

    :param rdev:
        device associated with special file
    :type rdev: dev_t

.. _`v9fs_vfs_get_link_dotl`:

v9fs_vfs_get_link_dotl
======================

.. c:function:: const char *v9fs_vfs_get_link_dotl(struct dentry *dentry, struct inode *inode, struct delayed_call *done)

    follow a symlink path

    :param dentry:
        dentry for symlink
    :type dentry: struct dentry \*

    :param inode:
        inode for symlink
    :type inode: struct inode \*

    :param done:
        destructor for return value
    :type done: struct delayed_call \*

.. This file was automatic generated / don't edit.

