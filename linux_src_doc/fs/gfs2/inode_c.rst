.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/inode.c

.. _`gfs2_set_iop`:

gfs2_set_iop
============

.. c:function:: void gfs2_set_iop(struct inode *inode)

    Sets inode operations

    :param inode:
        The inode with correct i_mode filled in
    :type inode: struct inode \*

.. _`gfs2_set_iop.description`:

Description
-----------

GFS2 lookup code fills in vfs inode contents based on info obtained
from directory entry inside \ :c:func:`gfs2_inode_lookup`\ .

.. _`gfs2_inode_lookup`:

gfs2_inode_lookup
=================

.. c:function:: struct inode *gfs2_inode_lookup(struct super_block *sb, unsigned int type, u64 no_addr, u64 no_formal_ino, unsigned int blktype)

    Lookup an inode

    :param sb:
        The super block
    :type sb: struct super_block \*

    :param type:
        The type of the inode
    :type type: unsigned int

    :param no_addr:
        The inode number
    :type no_addr: u64

    :param no_formal_ino:
        The inode generation number
    :type no_formal_ino: u64

    :param blktype:
        Requested block type (GFS2_BLKST_DINODE or GFS2_BLKST_UNLINKED;
        GFS2_BLKST_FREE to indicate not to verify)
    :type blktype: unsigned int

.. _`gfs2_inode_lookup.description`:

Description
-----------

If \ ``type``\  is DT_UNKNOWN, the inode type is fetched from disk.

If \ ``blktype``\  is anything other than GFS2_BLKST_FREE (which is used as a
placeholder because it doesn't otherwise make sense), the on-disk block type
is verified to be \ ``blktype``\ .

.. _`gfs2_inode_lookup.return`:

Return
------

A VFS inode, or an error

.. _`gfs2_lookupi`:

gfs2_lookupi
============

.. c:function:: struct inode *gfs2_lookupi(struct inode *dir, const struct qstr *name, int is_root)

    Look up a filename in a directory and return its inode

    :param dir:
        *undescribed*
    :type dir: struct inode \*

    :param name:
        The name of the inode to look for
    :type name: const struct qstr \*

    :param is_root:
        If 1, ignore the caller's permissions
    :type is_root: int

.. _`gfs2_lookupi.description`:

Description
-----------

This can be called via the VFS filldir function when NFS is doing
a readdirplus and the inode which its intending to stat isn't
already in cache. In this case we must not take the directory glock
again, since the readdir call will have already taken that lock.

.. _`gfs2_lookupi.return`:

Return
------

errno

.. _`create_ok`:

create_ok
=========

.. c:function:: int create_ok(struct gfs2_inode *dip, const struct qstr *name, umode_t mode)

    OK to create a new on-disk inode here?

    :param dip:
        Directory in which dinode is to be created
    :type dip: struct gfs2_inode \*

    :param name:
        Name of new dinode
    :type name: const struct qstr \*

    :param mode:
        *undescribed*
    :type mode: umode_t

.. _`create_ok.return`:

Return
------

errno

.. _`gfs2_init_xattr`:

gfs2_init_xattr
===============

.. c:function:: void gfs2_init_xattr(struct gfs2_inode *ip)

    Initialise an xattr block for a new inode

    :param ip:
        The inode in question
    :type ip: struct gfs2_inode \*

.. _`gfs2_init_xattr.description`:

Description
-----------

This sets up an empty xattr block for a new inode, ready to
take any ACLs, LSM xattrs, etc.

.. _`init_dinode`:

init_dinode
===========

.. c:function:: void init_dinode(struct gfs2_inode *dip, struct gfs2_inode *ip, const char *symname)

    Fill in a new dinode structure

    :param dip:
        The directory this inode is being created in
    :type dip: struct gfs2_inode \*

    :param ip:
        The inode
    :type ip: struct gfs2_inode \*

    :param symname:
        The symlink destination (if a symlink)
    :type symname: const char \*

.. _`gfs2_trans_da_blks`:

gfs2_trans_da_blks
==================

.. c:function:: unsigned gfs2_trans_da_blks(const struct gfs2_inode *dip, const struct gfs2_diradd *da, unsigned nr_inodes)

    Calculate number of blocks to link inode

    :param dip:
        The directory we are linking into
    :type dip: const struct gfs2_inode \*

    :param da:
        The dir add information
    :type da: const struct gfs2_diradd \*

    :param nr_inodes:
        The number of inodes involved
    :type nr_inodes: unsigned

.. _`gfs2_trans_da_blks.description`:

Description
-----------

This calculate the number of blocks we need to reserve in a
transaction to link \ ``nr_inodes``\  into a directory. In most cases
\ ``nr_inodes``\  will be 2 (the directory plus the inode being linked in)
but in case of rename, 4 may be required.

.. _`gfs2_trans_da_blks.return`:

Return
------

Number of blocks

.. _`gfs2_create_inode`:

gfs2_create_inode
=================

.. c:function:: int gfs2_create_inode(struct inode *dir, struct dentry *dentry, struct file *file, umode_t mode, dev_t dev, const char *symname, unsigned int size, int excl)

    Create a new inode

    :param dir:
        The parent directory
    :type dir: struct inode \*

    :param dentry:
        The new dentry
    :type dentry: struct dentry \*

    :param file:
        If non-NULL, the file which is being opened
    :type file: struct file \*

    :param mode:
        The permissions on the new inode
    :type mode: umode_t

    :param dev:
        For device nodes, this is the device number
    :type dev: dev_t

    :param symname:
        For symlinks, this is the link destination
    :type symname: const char \*

    :param size:
        The initial size of the inode (ignored for directories)
    :type size: unsigned int

    :param excl:
        *undescribed*
    :type excl: int

.. _`gfs2_create_inode.return`:

Return
------

0 on success, or error code

.. _`gfs2_create`:

gfs2_create
===========

.. c:function:: int gfs2_create(struct inode *dir, struct dentry *dentry, umode_t mode, bool excl)

    Create a file

    :param dir:
        The directory in which to create the file
    :type dir: struct inode \*

    :param dentry:
        The dentry of the new file
    :type dentry: struct dentry \*

    :param mode:
        The mode of the new file
    :type mode: umode_t

    :param excl:
        *undescribed*
    :type excl: bool

.. _`gfs2_create.return`:

Return
------

errno

.. _`__gfs2_lookup`:

\__gfs2_lookup
==============

.. c:function:: struct dentry *__gfs2_lookup(struct inode *dir, struct dentry *dentry, struct file *file)

    Look up a filename in a directory and return its inode

    :param dir:
        The directory inode
    :type dir: struct inode \*

    :param dentry:
        The dentry of the new inode
    :type dentry: struct dentry \*

    :param file:
        File to be opened
    :type file: struct file \*

.. _`__gfs2_lookup.return`:

Return
------

errno

.. _`gfs2_link`:

gfs2_link
=========

.. c:function:: int gfs2_link(struct dentry *old_dentry, struct inode *dir, struct dentry *dentry)

    Link to a file

    :param old_dentry:
        The inode to link
    :type old_dentry: struct dentry \*

    :param dir:
        Add link to this directory
    :type dir: struct inode \*

    :param dentry:
        The name of the link
    :type dentry: struct dentry \*

.. _`gfs2_link.description`:

Description
-----------

Link the inode in "old_dentry" into the directory "dir" with the
name in "dentry".

.. _`gfs2_link.return`:

Return
------

errno

.. _`gfs2_unlink_inode`:

gfs2_unlink_inode
=================

.. c:function:: int gfs2_unlink_inode(struct gfs2_inode *dip, const struct dentry *dentry)

    Removes an inode from its parent dir and unlinks it

    :param dip:
        The parent directory
    :type dip: struct gfs2_inode \*

    :param dentry:
        *undescribed*
    :type dentry: const struct dentry \*

.. _`gfs2_unlink_inode.description`:

Description
-----------

Called with all the locks and in a transaction. This will only be
called for a directory after it has been checked to ensure it is empty.

.. _`gfs2_unlink_inode.return`:

Return
------

0 on success, or an error

.. _`gfs2_unlink`:

gfs2_unlink
===========

.. c:function:: int gfs2_unlink(struct inode *dir, struct dentry *dentry)

    Unlink an inode (this does rmdir as well)

    :param dir:
        The inode of the directory containing the inode to unlink
    :type dir: struct inode \*

    :param dentry:
        The file itself
    :type dentry: struct dentry \*

.. _`gfs2_unlink.description`:

Description
-----------

This routine uses the type of the inode as a flag to figure out
whether this is an unlink or an rmdir.

.. _`gfs2_unlink.return`:

Return
------

errno

.. _`gfs2_symlink`:

gfs2_symlink
============

.. c:function:: int gfs2_symlink(struct inode *dir, struct dentry *dentry, const char *symname)

    Create a symlink

    :param dir:
        The directory to create the symlink in
    :type dir: struct inode \*

    :param dentry:
        The dentry to put the symlink in
    :type dentry: struct dentry \*

    :param symname:
        The thing which the link points to
    :type symname: const char \*

.. _`gfs2_symlink.return`:

Return
------

errno

.. _`gfs2_mkdir`:

gfs2_mkdir
==========

.. c:function:: int gfs2_mkdir(struct inode *dir, struct dentry *dentry, umode_t mode)

    Make a directory

    :param dir:
        The parent directory of the new one
    :type dir: struct inode \*

    :param dentry:
        The dentry of the new directory
    :type dentry: struct dentry \*

    :param mode:
        The mode of the new directory
    :type mode: umode_t

.. _`gfs2_mkdir.return`:

Return
------

errno

.. _`gfs2_mknod`:

gfs2_mknod
==========

.. c:function:: int gfs2_mknod(struct inode *dir, struct dentry *dentry, umode_t mode, dev_t dev)

    Make a special file

    :param dir:
        The directory in which the special file will reside
    :type dir: struct inode \*

    :param dentry:
        The dentry of the special file
    :type dentry: struct dentry \*

    :param mode:
        The mode of the special file
    :type mode: umode_t

    :param dev:
        The device specification of the special file
    :type dev: dev_t

.. _`gfs2_atomic_open`:

gfs2_atomic_open
================

.. c:function:: int gfs2_atomic_open(struct inode *dir, struct dentry *dentry, struct file *file, unsigned flags, umode_t mode)

    Atomically open a file

    :param dir:
        The directory
    :type dir: struct inode \*

    :param dentry:
        The proposed new entry
    :type dentry: struct dentry \*

    :param file:
        The proposed new struct file
    :type file: struct file \*

    :param flags:
        open flags
    :type flags: unsigned

    :param mode:
        File mode
    :type mode: umode_t

.. _`gfs2_atomic_open.return`:

Return
------

error code or 0 for success

.. _`update_moved_ino`:

update_moved_ino
================

.. c:function:: int update_moved_ino(struct gfs2_inode *ip, struct gfs2_inode *ndip, int dir_rename)

    Update an inode that's being moved

    :param ip:
        The inode being moved
    :type ip: struct gfs2_inode \*

    :param ndip:
        The parent directory of the new filename
    :type ndip: struct gfs2_inode \*

    :param dir_rename:
        True of ip is a directory
    :type dir_rename: int

.. _`update_moved_ino.return`:

Return
------

errno

.. _`gfs2_rename`:

gfs2_rename
===========

.. c:function:: int gfs2_rename(struct inode *odir, struct dentry *odentry, struct inode *ndir, struct dentry *ndentry)

    Rename a file

    :param odir:
        Parent directory of old file name
    :type odir: struct inode \*

    :param odentry:
        The old dentry of the file
    :type odentry: struct dentry \*

    :param ndir:
        Parent directory of new file name
    :type ndir: struct inode \*

    :param ndentry:
        The new dentry of the file
    :type ndentry: struct dentry \*

.. _`gfs2_rename.return`:

Return
------

errno

.. _`gfs2_exchange`:

gfs2_exchange
=============

.. c:function:: int gfs2_exchange(struct inode *odir, struct dentry *odentry, struct inode *ndir, struct dentry *ndentry, unsigned int flags)

    exchange two files

    :param odir:
        Parent directory of old file name
    :type odir: struct inode \*

    :param odentry:
        The old dentry of the file
    :type odentry: struct dentry \*

    :param ndir:
        Parent directory of new file name
    :type ndir: struct inode \*

    :param ndentry:
        The new dentry of the file
    :type ndentry: struct dentry \*

    :param flags:
        The rename flags
    :type flags: unsigned int

.. _`gfs2_exchange.return`:

Return
------

errno

.. _`gfs2_get_link`:

gfs2_get_link
=============

.. c:function:: const char *gfs2_get_link(struct dentry *dentry, struct inode *inode, struct delayed_call *done)

    Follow a symbolic link

    :param dentry:
        The dentry of the link
    :type dentry: struct dentry \*

    :param inode:
        The inode of the link
    :type inode: struct inode \*

    :param done:
        destructor for return value
    :type done: struct delayed_call \*

.. _`gfs2_get_link.description`:

Description
-----------

This can handle symlinks of any size.

.. _`gfs2_get_link.return`:

Return
------

0 on success or error code

.. _`gfs2_permission`:

gfs2_permission
===============

.. c:function:: int gfs2_permission(struct inode *inode, int mask)

    :param inode:
        The inode
    :type inode: struct inode \*

    :param mask:
        The mask to be tested
    :type mask: int

.. _`gfs2_permission.description`:

Description
-----------

This may be called from the VFS directly, or from within GFS2 with the
inode locked, so we look to see if the glock is already locked and only
lock the glock if its not already been done.

.. _`gfs2_permission.return`:

Return
------

errno

.. _`gfs2_setattr_simple`:

gfs2_setattr_simple
===================

.. c:function:: int gfs2_setattr_simple(struct inode *inode, struct iattr *attr)

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param attr:
        *undescribed*
    :type attr: struct iattr \*

.. _`gfs2_setattr_simple.return`:

Return
------

errno

.. _`gfs2_setattr`:

gfs2_setattr
============

.. c:function:: int gfs2_setattr(struct dentry *dentry, struct iattr *attr)

    Change attributes on an inode

    :param dentry:
        The dentry which is changing
    :type dentry: struct dentry \*

    :param attr:
        The structure describing the change
    :type attr: struct iattr \*

.. _`gfs2_setattr.description`:

Description
-----------

The VFS layer wants to change one or more of an inodes attributes.  Write
that change out to disk.

.. _`gfs2_setattr.return`:

Return
------

errno

.. _`gfs2_getattr`:

gfs2_getattr
============

.. c:function:: int gfs2_getattr(const struct path *path, struct kstat *stat, u32 request_mask, unsigned int flags)

    Read out an inode's attributes

    :param path:
        Object to query
    :type path: const struct path \*

    :param stat:
        The inode's stats
    :type stat: struct kstat \*

    :param request_mask:
        Mask of STATX_xxx flags indicating the caller's interests
    :type request_mask: u32

    :param flags:
        AT_STATX_xxx setting
    :type flags: unsigned int

.. _`gfs2_getattr.description`:

Description
-----------

This may be called from the VFS directly, or from within GFS2 with the
inode locked, so we look to see if the glock is already locked and only
lock the glock if its not already been done. Note that its the NFS
readdirplus operation which causes this to be called (from filldir)
with the glock already held.

.. _`gfs2_getattr.return`:

Return
------

errno

.. This file was automatic generated / don't edit.

