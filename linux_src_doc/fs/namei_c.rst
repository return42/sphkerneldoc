.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/namei.c

.. _`generic_permission`:

generic_permission
==================

.. c:function:: int generic_permission(struct inode *inode, int mask)

    check for access rights on a Posix-like filesystem

    :param inode:
        inode to check access rights for
    :type inode: struct inode \*

    :param mask:
        right to check for (%MAY_READ, \ ``MAY_WRITE``\ , \ ``MAY_EXEC``\ , ...)
    :type mask: int

.. _`generic_permission.description`:

Description
-----------

Used to check for read/write/execute permissions on a file.
We use "fsuid" for this, letting us set arbitrary permissions
for filesystem access without changing the "normal" uids which
are used for other things.

generic_permission is rcu-walk aware. It returns -ECHILD in case an rcu-walk
request cannot be satisfied (eg. requires blocking or too much complexity).
It would then be called again in ref-walk mode.

.. _`sb_permission`:

sb_permission
=============

.. c:function:: int sb_permission(struct super_block *sb, struct inode *inode, int mask)

    Check superblock-level permissions

    :param sb:
        Superblock of inode to check permission on
    :type sb: struct super_block \*

    :param inode:
        Inode to check permission on
    :type inode: struct inode \*

    :param mask:
        Right to check for (%MAY_READ, \ ``MAY_WRITE``\ , \ ``MAY_EXEC``\ )
    :type mask: int

.. _`sb_permission.description`:

Description
-----------

Separate out file-system wide checks from inode-specific permission checks.

.. _`inode_permission`:

inode_permission
================

.. c:function:: int inode_permission(struct inode *inode, int mask)

    Check for access rights to a given inode

    :param inode:
        Inode to check permission on
    :type inode: struct inode \*

    :param mask:
        Right to check for (%MAY_READ, \ ``MAY_WRITE``\ , \ ``MAY_EXEC``\ )
    :type mask: int

.. _`inode_permission.description`:

Description
-----------

Check for read/write/execute permissions on an inode.  We use fs[ug]id for
this, letting us set arbitrary permissions for filesystem access without
changing the "normal" UIDs which are used for other things.

When checking for MAY_APPEND, MAY_WRITE must also be set in \ ``mask``\ .

.. _`path_get`:

path_get
========

.. c:function:: void path_get(const struct path *path)

    get a reference to a path

    :param path:
        path to get the reference to
    :type path: const struct path \*

.. _`path_get.description`:

Description
-----------

Given a path increment the reference count to the dentry and the vfsmount.

.. _`path_put`:

path_put
========

.. c:function:: void path_put(const struct path *path)

    put a reference to a path

    :param path:
        path to put the reference to
    :type path: const struct path \*

.. _`path_put.description`:

Description
-----------

Given a path decrement the reference count to the dentry and the vfsmount.

.. _`path_connected`:

path_connected
==============

.. c:function:: bool path_connected(const struct path *path)

    Verify that a path->dentry is below path->mnt.mnt_root

    :param path:
        nameidate to verify
    :type path: const struct path \*

.. _`path_connected.description`:

Description
-----------

Rename can sometimes move a file or directory outside of a bind
mount, path_connected allows those cases to be detected.

.. _`unlazy_walk`:

unlazy_walk
===========

.. c:function:: int unlazy_walk(struct nameidata *nd)

    try to switch to ref-walk mode.

    :param nd:
        nameidata pathwalk data
    :type nd: struct nameidata \*

.. _`unlazy_walk.return`:

Return
------

0 on success, -ECHILD on failure

unlazy_walk attempts to legitimize the current nd->path and nd->root
for ref-walk mode.
Must be called from rcu-walk context.
Nothing should touch nameidata between \ :c:func:`unlazy_walk`\  failure and
\ :c:func:`terminate_walk`\ .

.. _`unlazy_child`:

unlazy_child
============

.. c:function:: int unlazy_child(struct nameidata *nd, struct dentry *dentry, unsigned seq)

    try to switch to ref-walk mode.

    :param nd:
        nameidata pathwalk data
    :type nd: struct nameidata \*

    :param dentry:
        child of nd->path.dentry
    :type dentry: struct dentry \*

    :param seq:
        seq number to check dentry against
    :type seq: unsigned

.. _`unlazy_child.return`:

Return
------

0 on success, -ECHILD on failure

unlazy_child attempts to legitimize the current nd->path, nd->root and dentry
for ref-walk mode.  \ ``dentry``\  must be a path found by a do_lookup call on
\ ``nd``\ .  Must be called from rcu-walk context.
Nothing should touch nameidata between \ :c:func:`unlazy_child`\  failure and
\ :c:func:`terminate_walk`\ .

.. _`complete_walk`:

complete_walk
=============

.. c:function:: int complete_walk(struct nameidata *nd)

    successful completion of path walk

    :param nd:
        pointer nameidata
    :type nd: struct nameidata \*

.. _`complete_walk.description`:

Description
-----------

If we had been in RCU mode, drop out of it and legitimize nd->path.
Revalidate the final result, unless we'd already done that during
the path walk or the filesystem doesn't ask for it.  Return 0 on
success, -error on failure.  In case of failure caller does not
need to drop nd->path.

.. _`may_follow_link`:

may_follow_link
===============

.. c:function:: int may_follow_link(struct nameidata *nd)

    Check symlink following for unsafe situations

    :param nd:
        nameidata pathwalk data
    :type nd: struct nameidata \*

.. _`may_follow_link.description`:

Description
-----------

In the case of the sysctl_protected_symlinks sysctl being enabled,
CAP_DAC_OVERRIDE needs to be specifically ignored if the symlink is
in a sticky world-writable directory. This is to protect privileged
processes from failing races against path names that may change out
from under them by way of other users creating malicious symlinks.
It will permit symlinks to be followed only when outside a sticky
world-writable directory, or when the uid of the symlink and follower
match, or when the directory owner matches the symlink's owner.

Returns 0 if following the symlink is allowed, -ve on error.

.. _`safe_hardlink_source`:

safe_hardlink_source
====================

.. c:function:: bool safe_hardlink_source(struct inode *inode)

    Check for safe hardlink conditions

    :param inode:
        the source inode to hardlink from
    :type inode: struct inode \*

.. _`safe_hardlink_source.return-false-if-at-least-one-of-the-following-conditions`:

Return false if at least one of the following conditions
--------------------------------------------------------

   - inode is not a regular file
   - inode is setuid
   - inode is setgid and group-exec
   - access failure for read and write

Otherwise returns true.

.. _`may_linkat`:

may_linkat
==========

.. c:function:: int may_linkat(struct path *link)

    Check permissions for creating a hardlink

    :param link:
        the source to hardlink from
    :type link: struct path \*

.. _`may_linkat.block-hardlink-when-all-of`:

Block hardlink when all of
--------------------------

 - sysctl_protected_hardlinks enabled
 - fsuid does not match inode
 - hardlink source is unsafe (see \ :c:func:`safe_hardlink_source`\  above)
 - not CAP_FOWNER in a namespace with the inode owner uid mapped

Returns 0 if successful, -ve on error.

.. _`may_create_in_sticky`:

may_create_in_sticky
====================

.. c:function:: int may_create_in_sticky(struct dentry * const dir, struct inode * const inode)

    Check whether an O_CREAT open in a sticky directory should be allowed, or not, on files that already exist.

    :param dir:
        the sticky parent directory
    :type dir: struct dentry \* const

    :param inode:
        the inode of the file to open
    :type inode: struct inode \* const

.. _`may_create_in_sticky.description`:

Description
-----------

Block an O_CREAT open of a FIFO (or a regular file) when:
  - sysctl_protected_fifos (or sysctl_protected_regular) is enabled
  - the file already exists
  - we are in a sticky directory
  - we don't own the file
  - the owner of the directory doesn't own the file
  - the directory is world writable
If the sysctl_protected_fifos (or sysctl_protected_regular) is set to 2
the directory doesn't have to be world writable: being group writable will
be enough.

Returns 0 if the open is allowed, -ve on error.

.. _`vfs_path_lookup`:

vfs_path_lookup
===============

.. c:function:: int vfs_path_lookup(struct dentry *dentry, struct vfsmount *mnt, const char *name, unsigned int flags, struct path *path)

    lookup a file path relative to a dentry-vfsmount pair

    :param dentry:
        pointer to dentry of the base directory
    :type dentry: struct dentry \*

    :param mnt:
        pointer to vfs mount of the base directory
    :type mnt: struct vfsmount \*

    :param name:
        pointer to file name
    :type name: const char \*

    :param flags:
        lookup flags
    :type flags: unsigned int

    :param path:
        pointer to struct path to fill
    :type path: struct path \*

.. _`try_lookup_one_len`:

try_lookup_one_len
==================

.. c:function:: struct dentry *try_lookup_one_len(const char *name, struct dentry *base, int len)

    filesystem helper to lookup single pathname component

    :param name:
        pathname component to lookup
    :type name: const char \*

    :param base:
        base directory to lookup from
    :type base: struct dentry \*

    :param len:
        maximum length \ ``len``\  should be interpreted to
    :type len: int

.. _`try_lookup_one_len.description`:

Description
-----------

Look up a dentry by name in the dcache, returning NULL if it does not
currently exist.  The function does not try to create a dentry.

Note that this routine is purely a helper for filesystem usage and should
not be called by generic code.

The caller must hold base->i_mutex.

.. _`lookup_one_len`:

lookup_one_len
==============

.. c:function:: struct dentry *lookup_one_len(const char *name, struct dentry *base, int len)

    filesystem helper to lookup single pathname component

    :param name:
        pathname component to lookup
    :type name: const char \*

    :param base:
        base directory to lookup from
    :type base: struct dentry \*

    :param len:
        maximum length \ ``len``\  should be interpreted to
    :type len: int

.. _`lookup_one_len.description`:

Description
-----------

Note that this routine is purely a helper for filesystem usage and should
not be called by generic code.

The caller must hold base->i_mutex.

.. _`lookup_one_len_unlocked`:

lookup_one_len_unlocked
=======================

.. c:function:: struct dentry *lookup_one_len_unlocked(const char *name, struct dentry *base, int len)

    filesystem helper to lookup single pathname component

    :param name:
        pathname component to lookup
    :type name: const char \*

    :param base:
        base directory to lookup from
    :type base: struct dentry \*

    :param len:
        maximum length \ ``len``\  should be interpreted to
    :type len: int

.. _`lookup_one_len_unlocked.description`:

Description
-----------

Note that this routine is purely a helper for filesystem usage and should
not be called by generic code.

Unlike lookup_one_len, it should be called without the parent
i_mutex held, and will take the i_mutex itself if necessary.

.. _`mountpoint_last`:

mountpoint_last
===============

.. c:function:: int mountpoint_last(struct nameidata *nd)

    look up last component for umount

    :param nd:
        pathwalk nameidata - currently pointing at parent directory of "last"
    :type nd: struct nameidata \*

.. _`mountpoint_last.description`:

Description
-----------

This is a special lookup_last function just for umount. In this case, we
need to resolve the path without doing any revalidation.

The nameidata should be the result of doing a LOOKUP_PARENT pathwalk. Since
mountpoints are always pinned in the dcache, their ancestors are too. Thus,
in almost all cases, this lookup will be served out of the dcache. The only
cases where it won't are if nd->last refers to a symlink or the path is
bogus and it doesn't exist.

.. _`mountpoint_last.return`:

Return
------

-error: if there was an error during lookup. This includes -ENOENT if the
        lookup found a negative dentry.

0:      if we successfully resolved nd->last and found it to not to be a
        symlink that needs to be followed.

1:      if we successfully resolved nd->last and found it to be a symlink
        that needs to be followed.

.. _`path_mountpoint`:

path_mountpoint
===============

.. c:function:: int path_mountpoint(struct nameidata *nd, unsigned flags, struct path *path)

    look up a path to be umounted

    :param nd:
        lookup context
    :type nd: struct nameidata \*

    :param flags:
        lookup flags
    :type flags: unsigned

    :param path:
        pointer to container for result
    :type path: struct path \*

.. _`path_mountpoint.description`:

Description
-----------

Look up the given name, but don't attempt to revalidate the last component.
Returns 0 and "path" will be valid on success; Returns error otherwise.

.. _`user_path_mountpoint_at`:

user_path_mountpoint_at
=======================

.. c:function:: int user_path_mountpoint_at(int dfd, const char __user *name, unsigned int flags, struct path *path)

    lookup a path from userland in order to umount it

    :param dfd:
        directory file descriptor
    :type dfd: int

    :param name:
        pathname from userland
    :type name: const char __user \*

    :param flags:
        lookup flags
    :type flags: unsigned int

    :param path:
        pointer to container to hold result
    :type path: struct path \*

.. _`user_path_mountpoint_at.description`:

Description
-----------

A umount is a special case for path walking. We're not actually interested
in the inode in this situation, and ESTALE errors can be a problem. We
simply want track down the dentry and vfsmount attached at the mountpoint
and avoid revalidating the last component.

Returns 0 and populates "path" on success.

.. _`vfs_unlink`:

vfs_unlink
==========

.. c:function:: int vfs_unlink(struct inode *dir, struct dentry *dentry, struct inode **delegated_inode)

    unlink a filesystem object

    :param dir:
        parent directory
    :type dir: struct inode \*

    :param dentry:
        victim
    :type dentry: struct dentry \*

    :param delegated_inode:
        returns victim inode, if the inode is delegated.
    :type delegated_inode: struct inode \*\*

.. _`vfs_unlink.description`:

Description
-----------

The caller must hold dir->i_mutex.

If vfs_unlink discovers a delegation, it will return -EWOULDBLOCK and
return a reference to the inode in delegated_inode.  The caller
should then break the delegation on that inode and retry.  Because
breaking a delegation may take a long time, the caller should drop
dir->i_mutex before doing so.

Alternatively, a caller may pass NULL for delegated_inode.  This may
be appropriate for callers that expect the underlying filesystem not
to be NFS exported.

.. _`vfs_link`:

vfs_link
========

.. c:function:: int vfs_link(struct dentry *old_dentry, struct inode *dir, struct dentry *new_dentry, struct inode **delegated_inode)

    create a new link

    :param old_dentry:
        object to be linked
    :type old_dentry: struct dentry \*

    :param dir:
        new parent
    :type dir: struct inode \*

    :param new_dentry:
        where to create the new link
    :type new_dentry: struct dentry \*

    :param delegated_inode:
        returns inode needing a delegation break
    :type delegated_inode: struct inode \*\*

.. _`vfs_link.description`:

Description
-----------

The caller must hold dir->i_mutex

If vfs_link discovers a delegation on the to-be-linked file in need
of breaking, it will return -EWOULDBLOCK and return a reference to the
inode in delegated_inode.  The caller should then break the delegation
and retry.  Because breaking a delegation may take a long time, the
caller should drop the i_mutex before doing so.

Alternatively, a caller may pass NULL for delegated_inode.  This may
be appropriate for callers that expect the underlying filesystem not
to be NFS exported.

.. _`vfs_rename`:

vfs_rename
==========

.. c:function:: int vfs_rename(struct inode *old_dir, struct dentry *old_dentry, struct inode *new_dir, struct dentry *new_dentry, struct inode **delegated_inode, unsigned int flags)

    rename a filesystem object

    :param old_dir:
        parent of source
    :type old_dir: struct inode \*

    :param old_dentry:
        source
    :type old_dentry: struct dentry \*

    :param new_dir:
        parent of destination
    :type new_dir: struct inode \*

    :param new_dentry:
        destination
    :type new_dentry: struct dentry \*

    :param delegated_inode:
        returns an inode needing a delegation break
    :type delegated_inode: struct inode \*\*

    :param flags:
        rename flags
    :type flags: unsigned int

.. _`vfs_rename.description`:

Description
-----------

The caller must hold multiple mutexes--see \ :c:func:`lock_rename`\ ).

If vfs_rename discovers a delegation in need of breaking at either
the source or destination, it will return -EWOULDBLOCK and return a
reference to the inode in delegated_inode.  The caller should then
break the delegation and retry.  Because breaking a delegation may
take a long time, the caller should drop all locks before doing
so.

Alternatively, a caller may pass NULL for delegated_inode.  This may
be appropriate for callers that expect the underlying filesystem not
to be NFS exported.

The worst of all namespace operations - renaming directory. "Perverted"
doesn't even start to describe it. Somebody in UCB had a heck of a trip...

.. _`vfs_rename.problems`:

Problems
--------


     a) we can get into loop creation.
     b) race potential - two innocent renames can create a loop together.
        That's where 4.4 screws up. Current fix: serialization on
        sb->s_vfs_rename_mutex. We might be more accurate, but that's another
        story.
     c) we have to lock _four_ objects - parents and victim (if it exists),
        and source (if it is not a directory).
        And that - after we got ->i_mutex on parents (until then we don't know
        whether the target exists).  Solution: try to be smart with locking
        order for inodes.  We rely on the fact that tree topology may change
        only under ->s_vfs_rename_mutex _and_ that parent of the object we
        move will be locked.  Thus we can rank directories by the tree
        (ancestors first) and rank all non-directories after them.
        That works since everybody except rename does "lock parent, lookup,
        lock child" and rename is under ->s_vfs_rename_mutex.
        HOWEVER, it relies on the assumption that any object with ->lookup()
        has no more than 1 dentry.  If "hybrid" objects will ever appear,
        we'd better make sure that there's no link(2) for them.
     d) conversion from fhandle to dentry may come in the wrong moment - when
        we are removing the target. Solution: we will have to grab ->i_mutex
        in the fhandle_to_dentry code. [FIXME - current nfsfh.c relies on
        ->i_mutex on parents, which works but leads to some truly excessive
        locking].

.. _`vfs_readlink`:

vfs_readlink
============

.. c:function:: int vfs_readlink(struct dentry *dentry, char __user *buffer, int buflen)

    copy symlink body into userspace buffer

    :param dentry:
        dentry on which to get symbolic link
    :type dentry: struct dentry \*

    :param buffer:
        user memory pointer
    :type buffer: char __user \*

    :param buflen:
        size of buffer
    :type buflen: int

.. _`vfs_readlink.description`:

Description
-----------

Does not touch atime.  That's up to the caller if necessary

Does not call security hook.

.. _`vfs_get_link`:

vfs_get_link
============

.. c:function:: const char *vfs_get_link(struct dentry *dentry, struct delayed_call *done)

    get symlink body

    :param dentry:
        dentry on which to get symbolic link
    :type dentry: struct dentry \*

    :param done:
        caller needs to free returned data with this
    :type done: struct delayed_call \*

.. _`vfs_get_link.description`:

Description
-----------

Calls security hook and i_op->get_link() on the supplied inode.

It does not touch atime.  That's up to the caller if necessary.

Does not work on "special" symlinks like /proc/$$/fd/N

.. This file was automatic generated / don't edit.

