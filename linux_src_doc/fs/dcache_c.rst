.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/dcache.c

.. _`___d_drop`:

___d_drop
=========

.. c:function:: void ___d_drop(struct dentry *dentry)

    drop a dentry

    :param dentry:
        dentry to drop
    :type dentry: struct dentry \*

.. _`___d_drop.description`:

Description
-----------

\ :c:func:`d_drop`\  unhashes the entry from the parent dentry hashes, so that it won't
be found through a VFS lookup any more. Note that this is different from
deleting the dentry - d_delete will try to mark the dentry negative if
possible, giving a successful _negative_ lookup, while d_drop will
just make the cache lookup fail.

\ :c:func:`d_drop`\  is used mainly for stuff that wants to invalidate a dentry for some
reason (NFS timeouts or autofs deletes).

__d_drop requires dentry->d_lock
___d_drop doesn't mark dentry as "unhashed"
  (dentry->d_hash.pprev will be LIST_POISON2, not NULL).

.. _`d_find_any_alias`:

d_find_any_alias
================

.. c:function:: struct dentry *d_find_any_alias(struct inode *inode)

    find any alias for a given inode

    :param inode:
        inode to find an alias for
    :type inode: struct inode \*

.. _`d_find_any_alias.description`:

Description
-----------

If any aliases exist for the given inode, take and return a
reference for one of them.  If no aliases exist, return \ ``NULL``\ .

.. _`__d_find_alias`:

__d_find_alias
==============

.. c:function:: struct dentry *__d_find_alias(struct inode *inode)

    grab a hashed alias of inode

    :param inode:
        inode in question
    :type inode: struct inode \*

.. _`__d_find_alias.description`:

Description
-----------

If inode has a hashed alias, or is a directory and has any alias,
acquire the reference to alias and return it. Otherwise return NULL.
Notice that if inode is a directory there can be only one alias and
it can be unhashed only if it has no children, or if it is the root
of a filesystem, or if the directory was renamed and d_revalidate
was the first vfs operation to notice.

If the inode has an IS_ROOT, DCACHE_DISCONNECTED alias, then prefer
any other hashed alias over that one.

.. _`prune_dcache_sb`:

prune_dcache_sb
===============

.. c:function:: long prune_dcache_sb(struct super_block *sb, struct shrink_control *sc)

    shrink the dcache

    :param sb:
        superblock
    :type sb: struct super_block \*

    :param sc:
        shrink control, passed to \ :c:func:`list_lru_shrink_walk`\ 
    :type sc: struct shrink_control \*

.. _`prune_dcache_sb.description`:

Description
-----------

Attempt to shrink the superblock dcache LRU by \ ``sc->nr_to_scan``\  entries. This
is done when we need more memory and called from the superblock shrinker
function.

This function may fail to free any resources if all the dentries are in
use.

.. _`shrink_dcache_sb`:

shrink_dcache_sb
================

.. c:function:: void shrink_dcache_sb(struct super_block *sb)

    shrink dcache for a superblock

    :param sb:
        superblock
    :type sb: struct super_block \*

.. _`shrink_dcache_sb.description`:

Description
-----------

Shrink the dcache for the specified super block. This is used to free
the dcache before unmounting a file system.

.. _`d_walk_ret`:

enum d_walk_ret
===============

.. c:type:: enum d_walk_ret

    action to talke during tree walk

.. _`d_walk_ret.definition`:

Definition
----------

.. code-block:: c

    enum d_walk_ret {
        D_WALK_CONTINUE,
        D_WALK_QUIT,
        D_WALK_NORETRY,
        D_WALK_SKIP
    };

.. _`d_walk_ret.constants`:

Constants
---------

D_WALK_CONTINUE
    contrinue walk

D_WALK_QUIT
    quit walk

D_WALK_NORETRY
    quit when retry is needed

D_WALK_SKIP
    skip this dentry and its children

.. _`d_walk`:

d_walk
======

.. c:function:: void d_walk(struct dentry *parent, void *data, enum d_walk_ret (*enter)(void *, struct dentry *))

    walk the dentry tree

    :param parent:
        start of walk
    :type parent: struct dentry \*

    :param data:
        data passed to \ ``enter``\ () and \ ``finish``\ ()
    :type data: void \*

    :param enum d_walk_ret (\*enter)(void \*, struct dentry \*):
        callback when first entering the dentry

.. _`d_walk.description`:

Description
-----------

The \ ``enter``\ () callbacks are called with d_lock held.

.. _`path_has_submounts`:

path_has_submounts
==================

.. c:function:: int path_has_submounts(const struct path *parent)

    check for mounts over a dentry in the current namespace.

    :param parent:
        path to check.
    :type parent: const struct path \*

.. _`path_has_submounts.description`:

Description
-----------

Return true if the parent or its subdirectories contain
a mount point in the current namespace.

.. _`shrink_dcache_parent`:

shrink_dcache_parent
====================

.. c:function:: void shrink_dcache_parent(struct dentry *parent)

    prune dcache

    :param parent:
        parent of entries to prune
    :type parent: struct dentry \*

.. _`shrink_dcache_parent.description`:

Description
-----------

Prune the dcache to remove unused children of the parent dentry.

.. _`d_invalidate`:

d_invalidate
============

.. c:function:: void d_invalidate(struct dentry *dentry)

    detach submounts, prune dcache, and drop

    :param dentry:
        dentry to invalidate (aka detach, prune and drop)
    :type dentry: struct dentry \*

.. _`__d_alloc`:

__d_alloc
=========

.. c:function:: struct dentry *__d_alloc(struct super_block *sb, const struct qstr *name)

    allocate a dcache entry

    :param sb:
        filesystem it will belong to
    :type sb: struct super_block \*

    :param name:
        qstr of the name
    :type name: const struct qstr \*

.. _`__d_alloc.description`:

Description
-----------

Allocates a dentry. It returns \ ``NULL``\  if there is insufficient memory
available. On a success the dentry is returned. The name passed in is
copied and the copy passed in may be reused after this call.

.. _`d_alloc`:

d_alloc
=======

.. c:function:: struct dentry *d_alloc(struct dentry *parent, const struct qstr *name)

    allocate a dcache entry

    :param parent:
        parent of entry to allocate
    :type parent: struct dentry \*

    :param name:
        qstr of the name
    :type name: const struct qstr \*

.. _`d_alloc.description`:

Description
-----------

Allocates a dentry. It returns \ ``NULL``\  if there is insufficient memory
available. On a success the dentry is returned. The name passed in is
copied and the copy passed in may be reused after this call.

.. _`d_alloc_pseudo`:

d_alloc_pseudo
==============

.. c:function:: struct dentry *d_alloc_pseudo(struct super_block *sb, const struct qstr *name)

    allocate a dentry (for lookup-less filesystems)

    :param sb:
        the superblock
    :type sb: struct super_block \*

    :param name:
        qstr of the name
    :type name: const struct qstr \*

.. _`d_alloc_pseudo.description`:

Description
-----------

For a filesystem that just pins its dentries in memory and never
performs lookups at all, return an unhashed IS_ROOT dentry.

.. _`d_instantiate`:

d_instantiate
=============

.. c:function:: void d_instantiate(struct dentry *entry, struct inode *inode)

    fill in inode information for a dentry

    :param entry:
        dentry to complete
    :type entry: struct dentry \*

    :param inode:
        inode to attach to this dentry
    :type inode: struct inode \*

.. _`d_instantiate.description`:

Description
-----------

Fill in inode information in the entry.

This turns negative dentries into productive full members
of society.

NOTE! This assumes that the inode count has been incremented
(or otherwise set) by the caller to indicate that it is now
in use by the dcache.

.. _`d_obtain_alias`:

d_obtain_alias
==============

.. c:function:: struct dentry *d_obtain_alias(struct inode *inode)

    find or allocate a DISCONNECTED dentry for a given inode

    :param inode:
        inode to allocate the dentry for
    :type inode: struct inode \*

.. _`d_obtain_alias.description`:

Description
-----------

Obtain a dentry for an inode resulting from NFS filehandle conversion or
similar open by handle operations.  The returned dentry may be anonymous,
or may have a full name (if the inode was already in the cache).

When called on a directory inode, we must ensure that the inode only ever
has one dentry.  If a dentry is found, that is returned instead of
allocating a new one.

On successful return, the reference to the inode has been transferred
to the dentry.  In case of an error the reference on the inode is released.
To make it easier to use in export operations a \ ``NULL``\  or IS_ERR inode may
be passed in and the error will be propagated to the return value,
with a \ ``NULL``\  \ ``inode``\  replaced by ERR_PTR(-ESTALE).

.. _`d_obtain_root`:

d_obtain_root
=============

.. c:function:: struct dentry *d_obtain_root(struct inode *inode)

    find or allocate a dentry for a given inode

    :param inode:
        inode to allocate the dentry for
    :type inode: struct inode \*

.. _`d_obtain_root.description`:

Description
-----------

Obtain an IS_ROOT dentry for the root of a filesystem.

We must ensure that directory inodes only ever have one dentry.  If a
dentry is found, that is returned instead of allocating a new one.

On successful return, the reference to the inode has been transferred
to the dentry.  In case of an error the reference on the inode is
released.  A \ ``NULL``\  or IS_ERR inode may be passed in and will be the
error will be propagate to the return value, with a \ ``NULL``\  \ ``inode``\ 
replaced by ERR_PTR(-ESTALE).

.. _`d_add_ci`:

d_add_ci
========

.. c:function:: struct dentry *d_add_ci(struct dentry *dentry, struct inode *inode, struct qstr *name)

    lookup or allocate new dentry with case-exact name

    :param dentry:
        the negative dentry that was passed to the parent's lookup func
    :type dentry: struct dentry \*

    :param inode:
        the inode case-insensitive lookup has found
    :type inode: struct inode \*

    :param name:
        the case-exact name to be associated with the returned dentry
    :type name: struct qstr \*

.. _`d_add_ci.description`:

Description
-----------

This is to avoid filling the dcache with case-insensitive names to the
same inode, only the actual correct case is stored in the dcache for
case-insensitive filesystems.

For a case-insensitive lookup match and if the the case-exact dentry
already exists in in the dcache, use it and return it.

If no entry exists with the exact case name, allocate new dentry with
the exact case, and return the spliced entry.

.. _`__d_lookup_rcu`:

__d_lookup_rcu
==============

.. c:function:: struct dentry *__d_lookup_rcu(const struct dentry *parent, const struct qstr *name, unsigned *seqp)

    search for a dentry (racy, store-free)

    :param parent:
        parent dentry
    :type parent: const struct dentry \*

    :param name:
        qstr of name we wish to find
    :type name: const struct qstr \*

    :param seqp:
        returns d_seq value at the point where the dentry was found
    :type seqp: unsigned \*

.. _`__d_lookup_rcu.return`:

Return
------

dentry, or NULL

__d_lookup_rcu is the dcache lookup function for rcu-walk name
resolution (store-free path walking) design described in
Documentation/filesystems/path-lookup.txt.

This is not to be used outside core vfs.

__d_lookup_rcu must only be used in rcu-walk mode, ie. with vfsmount lock
held, and rcu_read_lock held. The returned dentry must not be stored into
without taking d_lock and checking d_seq sequence count against \ ``seq``\ 
returned here.

A refcount may be taken on the found dentry with the d_rcu_to_refcount
function.

Alternatively, __d_lookup_rcu may be called again to look up the child of
the returned dentry, so long as its parent's seqlock is checked after the
child is looked up. Thus, an interlocking stepping of sequence lock checks
is formed, giving integrity down the path walk.

NOTE! The caller *has* to check the resulting dentry against the sequence
number we've returned before using any of the resulting dentry state!

.. _`d_lookup`:

d_lookup
========

.. c:function:: struct dentry *d_lookup(const struct dentry *parent, const struct qstr *name)

    search for a dentry

    :param parent:
        parent dentry
    :type parent: const struct dentry \*

    :param name:
        qstr of name we wish to find
    :type name: const struct qstr \*

.. _`d_lookup.return`:

Return
------

dentry, or NULL

d_lookup searches the children of the parent dentry for the name in
question. If the dentry is found its reference count is incremented and the
dentry is returned. The caller must use dput to free the entry when it has
finished using it. \ ``NULL``\  is returned if the dentry does not exist.

.. _`__d_lookup`:

__d_lookup
==========

.. c:function:: struct dentry *__d_lookup(const struct dentry *parent, const struct qstr *name)

    search for a dentry (racy)

    :param parent:
        parent dentry
    :type parent: const struct dentry \*

    :param name:
        qstr of name we wish to find
    :type name: const struct qstr \*

.. _`__d_lookup.return`:

Return
------

dentry, or NULL

__d_lookup is like d_lookup, however it may (rarely) return a
false-negative result due to unrelated rename activity.

__d_lookup is slightly faster by avoiding rename_lock read seqlock,
however it must be used carefully, eg. with a following d_lookup in
the case of failure.

__d_lookup callers must be commented.

.. _`d_hash_and_lookup`:

d_hash_and_lookup
=================

.. c:function:: struct dentry *d_hash_and_lookup(struct dentry *dir, struct qstr *name)

    hash the qstr then search for a dentry

    :param dir:
        Directory to search in
    :type dir: struct dentry \*

    :param name:
        qstr of name we wish to find
    :type name: struct qstr \*

.. _`d_hash_and_lookup.description`:

Description
-----------

On lookup failure NULL is returned; on bad name - ERR_PTR(-error)

.. _`d_delete`:

d_delete
========

.. c:function:: void d_delete(struct dentry *dentry)

    delete a dentry

    :param dentry:
        The dentry to delete
    :type dentry: struct dentry \*

.. _`d_delete.description`:

Description
-----------

Turn the dentry into a negative dentry if possible, otherwise
remove it from the hash queues so it can be deleted later

.. _`d_rehash`:

d_rehash
========

.. c:function:: void d_rehash(struct dentry *entry)

    add an entry back to the hash

    :param entry:
        dentry to add to the hash
    :type entry: struct dentry \*

.. _`d_rehash.description`:

Description
-----------

Adds a dentry to the hash according to its name.

.. _`d_add`:

d_add
=====

.. c:function:: void d_add(struct dentry *entry, struct inode *inode)

    add dentry to hash queues

    :param entry:
        dentry to add
    :type entry: struct dentry \*

    :param inode:
        The inode to attach to this dentry
    :type inode: struct inode \*

.. _`d_add.description`:

Description
-----------

This adds the entry to the hash queues and initializes \ ``inode``\ .
The entry was actually filled in earlier during \ :c:func:`d_alloc`\ .

.. _`d_exact_alias`:

d_exact_alias
=============

.. c:function:: struct dentry *d_exact_alias(struct dentry *entry, struct inode *inode)

    find and hash an exact unhashed alias

    :param entry:
        dentry to add
    :type entry: struct dentry \*

    :param inode:
        The inode to go with this dentry
    :type inode: struct inode \*

.. _`d_exact_alias.description`:

Description
-----------

If an unhashed dentry with the same name/parent and desired
inode already exists, hash and return it.  Otherwise, return
NULL.

Parent directory should be locked.

.. _`d_ancestor`:

d_ancestor
==========

.. c:function:: struct dentry *d_ancestor(struct dentry *p1, struct dentry *p2)

    search for an ancestor

    :param p1:
        ancestor dentry
    :type p1: struct dentry \*

    :param p2:
        child dentry
    :type p2: struct dentry \*

.. _`d_ancestor.description`:

Description
-----------

Returns the ancestor dentry of p2 which is a child of p1, if p1 is
an ancestor of p2, else NULL.

.. _`d_splice_alias`:

d_splice_alias
==============

.. c:function:: struct dentry *d_splice_alias(struct inode *inode, struct dentry *dentry)

    splice a disconnected dentry into the tree if one exists

    :param inode:
        the inode which may have a disconnected dentry
    :type inode: struct inode \*

    :param dentry:
        a negative dentry which we want to point to the inode.
    :type dentry: struct dentry \*

.. _`d_splice_alias.description`:

Description
-----------

If inode is a directory and has an IS_ROOT alias, then d_move that in
place of the given dentry and return it, else simply d_add the inode
to the dentry and return NULL.

If a non-IS_ROOT directory is found, the filesystem is corrupt, and
we should error out: directories can't have multiple aliases.

This is needed in the lookup routine of any filesystem that is exportable
(via knfsd) so that we can build dcache paths to directories effectively.

If a dentry was found and moved, then it is returned.  Otherwise NULL
is returned.  This matches the expected return value of ->lookup.

Cluster filesystems may call this function with a negative, hashed dentry.
In that case, we know that the inode will be a regular file, and also this
will only occur during atomic_open. So we need to check for the dentry
being already hashed only in the final case.

.. _`is_subdir`:

is_subdir
=========

.. c:function:: bool is_subdir(struct dentry *new_dentry, struct dentry *old_dentry)

    is new dentry a subdirectory of old_dentry

    :param new_dentry:
        new dentry
    :type new_dentry: struct dentry \*

    :param old_dentry:
        old dentry
    :type old_dentry: struct dentry \*

.. _`is_subdir.description`:

Description
-----------

Returns true if new_dentry is a subdirectory of the parent (at any depth).
Returns false otherwise.
Caller must ensure that "new_dentry" is pinned before calling \ :c:func:`is_subdir`\ 

.. This file was automatic generated / don't edit.

