.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/dcache.c

.. _`dentry_rcuwalk_invalidate`:

dentry_rcuwalk_invalidate
=========================

.. c:function:: void dentry_rcuwalk_invalidate(struct dentry *dentry)

    invalidate in-progress rcu-walk lookups

    :param struct dentry \*dentry:
        the target dentry
        After this call, in-progress rcu-walk path lookup will fail. This
        should be called after unhashing, and after changing d_inode (if
        the dentry has not already been unhashed).

.. _`__d_drop`:

__d_drop
========

.. c:function:: void __d_drop(struct dentry *dentry)

    drop a dentry

    :param struct dentry \*dentry:
        dentry to drop

.. _`__d_drop.description`:

Description
-----------

\ :c:func:`d_drop`\  unhashes the entry from the parent dentry hashes, so that it won't
be found through a VFS lookup any more. Note that this is different from
deleting the dentry - d_delete will try to mark the dentry negative if
possible, giving a successful \_negative\_ lookup, while d_drop will
just make the cache lookup fail.

\ :c:func:`d_drop`\  is used mainly for stuff that wants to invalidate a dentry for some
reason (NFS timeouts or autofs deletes).

\__d_drop requires dentry->d_lock.

.. _`__d_find_alias`:

__d_find_alias
==============

.. c:function:: struct dentry *__d_find_alias(struct inode *inode)

    grab a hashed alias of inode

    :param struct inode \*inode:
        inode in question

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

    :param struct super_block \*sb:
        superblock

    :param struct shrink_control \*sc:
        shrink control, passed to \ :c:func:`list_lru_shrink_walk`\ 

.. _`prune_dcache_sb.description`:

Description
-----------

Attempt to shrink the superblock dcache LRU by \ ``sc``\ ->nr_to_scan entries. This
is done when we need more memory and called from the superblock shrinker
function.

This function may fail to free any resources if all the dentries are in
use.

.. _`shrink_dcache_sb`:

shrink_dcache_sb
================

.. c:function:: void shrink_dcache_sb(struct super_block *sb)

    shrink dcache for a superblock

    :param struct super_block \*sb:
        superblock

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

.. c:function:: void d_walk(struct dentry *parent, void *data, enum d_walk_ret (*) enter (void *, struct dentry *, void (*) finish (void *)

    walk the dentry tree

    :param struct dentry \*parent:
        start of walk

    :param void \*data:
        data passed to @\ :c:func:`enter`\  and @\ :c:func:`finish`\ 

    :param (enum d_walk_ret (\*) enter (void \*, struct dentry \*):
        callback when first entering the dentry

    :param (void (\*) finish (void \*):
        callback when successfully finished the walk

.. _`d_walk.description`:

Description
-----------

The @\ :c:func:`enter`\  and @\ :c:func:`finish`\  callbacks are called with d_lock held.

.. _`have_submounts`:

have_submounts
==============

.. c:function:: int have_submounts(struct dentry *parent)

    check for mounts over a dentry

    :param struct dentry \*parent:
        dentry to check.

.. _`have_submounts.description`:

Description
-----------

Return true if the parent or its subdirectories contain
a mount point

.. _`shrink_dcache_parent`:

shrink_dcache_parent
====================

.. c:function:: void shrink_dcache_parent(struct dentry *parent)

    prune dcache

    :param struct dentry \*parent:
        parent of entries to prune

.. _`shrink_dcache_parent.description`:

Description
-----------

Prune the dcache to remove unused children of the parent dentry.

.. _`d_invalidate`:

d_invalidate
============

.. c:function:: void d_invalidate(struct dentry *dentry)

    detach submounts, prune dcache, and drop

    :param struct dentry \*dentry:
        dentry to invalidate (aka detach, prune and drop)

.. _`d_invalidate.description`:

Description
-----------

no dcache lock.

The final d_drop is done as an atomic operation relative to
rename_lock ensuring there are no races with d_set_mounted.  This
ensures there are no unhashed dentries on the path to a mountpoint.

.. _`__d_alloc`:

__d_alloc
=========

.. c:function:: struct dentry *__d_alloc(struct super_block *sb, const struct qstr *name)

    allocate a dcache entry

    :param struct super_block \*sb:
        filesystem it will belong to

    :param const struct qstr \*name:
        qstr of the name

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

    :param struct dentry \*parent:
        parent of entry to allocate

    :param const struct qstr \*name:
        qstr of the name

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

    :param struct super_block \*sb:
        the superblock

    :param const struct qstr \*name:
        qstr of the name

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

    :param struct dentry \*entry:
        dentry to complete

    :param struct inode \*inode:
        inode to attach to this dentry

.. _`d_instantiate.description`:

Description
-----------

Fill in inode information in the entry.

This turns negative dentries into productive full members
of society.

NOTE! This assumes that the inode count has been incremented
(or otherwise set) by the caller to indicate that it is now
in use by the dcache.

.. _`d_instantiate_no_diralias`:

d_instantiate_no_diralias
=========================

.. c:function:: int d_instantiate_no_diralias(struct dentry *entry, struct inode *inode)

    instantiate a non-aliased dentry

    :param struct dentry \*entry:
        dentry to complete

    :param struct inode \*inode:
        inode to attach to this dentry

.. _`d_instantiate_no_diralias.description`:

Description
-----------

Fill in inode information in the entry.  If a directory alias is found, then
return an error (and drop inode).  Together with \ :c:func:`d_materialise_unique`\  this
guarantees that a directory inode may never have more than one alias.

.. _`d_find_any_alias`:

d_find_any_alias
================

.. c:function:: struct dentry *d_find_any_alias(struct inode *inode)

    find any alias for a given inode

    :param struct inode \*inode:
        inode to find an alias for

.. _`d_find_any_alias.description`:

Description
-----------

If any aliases exist for the given inode, take and return a
reference for one of them.  If no aliases exist, return \ ``NULL``\ .

.. _`d_obtain_alias`:

d_obtain_alias
==============

.. c:function:: struct dentry *d_obtain_alias(struct inode *inode)

    find or allocate a DISCONNECTED dentry for a given inode

    :param struct inode \*inode:
        inode to allocate the dentry for

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

    :param struct inode \*inode:
        inode to allocate the dentry for

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

    :param struct dentry \*dentry:
        the negative dentry that was passed to the parent's lookup func

    :param struct inode \*inode:
        the inode case-insensitive lookup has found

    :param struct qstr \*name:
        the case-exact name to be associated with the returned dentry

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

    :param const struct dentry \*parent:
        parent dentry

    :param const struct qstr \*name:
        qstr of name we wish to find

    :param unsigned \*seqp:
        returns d_seq value at the point where the dentry was found

.. _`__d_lookup_rcu.return`:

Return
------

dentry, or NULL

\__d_lookup_rcu is the dcache lookup function for rcu-walk name
resolution (store-free path walking) design described in
Documentation/filesystems/path-lookup.txt.

This is not to be used outside core vfs.

\__d_lookup_rcu must only be used in rcu-walk mode, ie. with vfsmount lock
held, and rcu_read_lock held. The returned dentry must not be stored into
without taking d_lock and checking d_seq sequence count against \ ``seq``\ 
returned here.

A refcount may be taken on the found dentry with the d_rcu_to_refcount
function.

Alternatively, \__d_lookup_rcu may be called again to look up the child of
the returned dentry, so long as its parent's seqlock is checked after the
child is looked up. Thus, an interlocking stepping of sequence lock checks
is formed, giving integrity down the path walk.

NOTE! The caller \*has\* to check the resulting dentry against the sequence
number we've returned before using any of the resulting dentry state!

.. _`d_lookup`:

d_lookup
========

.. c:function:: struct dentry *d_lookup(const struct dentry *parent, const struct qstr *name)

    search for a dentry

    :param const struct dentry \*parent:
        parent dentry

    :param const struct qstr \*name:
        qstr of name we wish to find

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

    :param const struct dentry \*parent:
        parent dentry

    :param const struct qstr \*name:
        qstr of name we wish to find

.. _`__d_lookup.return`:

Return
------

dentry, or NULL

\__d_lookup is like d_lookup, however it may (rarely) return a
false-negative result due to unrelated rename activity.

\__d_lookup is slightly faster by avoiding rename_lock read seqlock,
however it must be used carefully, eg. with a following d_lookup in
the case of failure.

\__d_lookup callers must be commented.

.. _`d_hash_and_lookup`:

d_hash_and_lookup
=================

.. c:function:: struct dentry *d_hash_and_lookup(struct dentry *dir, struct qstr *name)

    hash the qstr then search for a dentry

    :param struct dentry \*dir:
        Directory to search in

    :param struct qstr \*name:
        qstr of name we wish to find

.. _`d_hash_and_lookup.description`:

Description
-----------

On lookup failure NULL is returned; on bad name - ERR_PTR(-error)

.. _`d_delete`:

d_delete
========

.. c:function:: void d_delete(struct dentry *dentry)

    delete a dentry

    :param struct dentry \*dentry:
        The dentry to delete

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

    :param struct dentry \*entry:
        dentry to add to the hash

.. _`d_rehash.description`:

Description
-----------

Adds a dentry to the hash according to its name.

.. _`d_add`:

d_add
=====

.. c:function:: void d_add(struct dentry *entry, struct inode *inode)

    add dentry to hash queues

    :param struct dentry \*entry:
        dentry to add

    :param struct inode \*inode:
        The inode to attach to this dentry

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

    :param struct dentry \*entry:
        dentry to add

    :param struct inode \*inode:
        The inode to go with this dentry

.. _`d_exact_alias.description`:

Description
-----------

If an unhashed dentry with the same name/parent and desired
inode already exists, hash and return it.  Otherwise, return
NULL.

Parent directory should be locked.

.. _`dentry_update_name_case`:

dentry_update_name_case
=======================

.. c:function:: void dentry_update_name_case(struct dentry *dentry, struct qstr *name)

    update case insensitive dentry with a new name

    :param struct dentry \*dentry:
        dentry to be updated

    :param struct qstr \*name:
        new name

.. _`dentry_update_name_case.description`:

Description
-----------

Update a case insensitive dentry with new case of name.

dentry must have been returned by d_lookup with name \ ``name``\ . Old and new
name lengths must match (ie. no d_compare which allows mismatched name
lengths).

Parent inode i_mutex must be held over d_lookup and into this call (to
keep renames and concurrent inserts, and readdir(2) away).

.. _`d_ancestor`:

d_ancestor
==========

.. c:function:: struct dentry *d_ancestor(struct dentry *p1, struct dentry *p2)

    search for an ancestor

    :param struct dentry \*p1:
        ancestor dentry

    :param struct dentry \*p2:
        child dentry

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

    :param struct inode \*inode:
        the inode which may have a disconnected dentry

    :param struct dentry \*dentry:
        a negative dentry which we want to point to the inode.

.. _`d_splice_alias.description`:

Description
-----------

If inode is a directory and has an IS_ROOT alias, then d_move that in
place of the given dentry and return it, else simply d_add the inode
to the dentry and return NULL.

If a non-IS_ROOT directory is found, the filesystem is corrupt, and

.. _`d_splice_alias.we-should-error-out`:

we should error out
-------------------

directories can't have multiple aliases.

This is needed in the lookup routine of any filesystem that is exportable
(via knfsd) so that we can build dcache paths to directories effectively.

If a dentry was found and moved, then it is returned.  Otherwise NULL
is returned.  This matches the expected return value of ->lookup.

Cluster filesystems may call this function with a negative, hashed dentry.
In that case, we know that the inode will be a regular file, and also this
will only occur during atomic_open. So we need to check for the dentry
being already hashed only in the final case.

.. _`prepend_name`:

prepend_name
============

.. c:function:: int prepend_name(char **buffer, int *buflen, struct qstr *name)

    prepend a pathname in front of current buffer pointer

    :param char \*\*buffer:
        buffer pointer

    :param int \*buflen:
        allocated length of the buffer

    :param struct qstr \*name:
        name string and length qstr structure

.. _`prepend_name.description`:

Description
-----------

With RCU path tracing, it may race with \ :c:func:`d_move`\ . Use \ :c:func:`ACCESS_ONCE`\  to
make sure that either the old or the new name pointer and length are
fetched. However, there may be mismatch between length and pointer.
The length cannot be trusted, we need to copy it byte-by-byte until
the length is reached or a null byte is found. It also prepends "/" at
the beginning of the name. The sequence number check at the caller will
retry it again when a \ :c:func:`d_move`\  does happen. So any garbage in the buffer
due to mismatched pointer and length will be discarded.

Data dependency barrier is needed to make sure that we see that terminating
NUL.  Alpha strikes again, film at 11...

.. _`prepend_path`:

prepend_path
============

.. c:function:: int prepend_path(const struct path *path, const struct path *root, char **buffer, int *buflen)

    Prepend path string to a buffer

    :param const struct path \*path:
        the dentry/vfsmount to report

    :param const struct path \*root:
        root vfsmnt/dentry

    :param char \*\*buffer:
        pointer to the end of the buffer

    :param int \*buflen:
        pointer to buffer length

.. _`prepend_path.description`:

Description
-----------

The function will first try to write out the pathname without taking any
lock other than the RCU read lock to make sure that dentries won't go away.
It only checks the sequence number of the global rename_lock as any change
in the dentry's d_seq will be preceded by changes in the rename_lock
sequence number. If the sequence number had been changed, it will restart
the whole pathname back-tracing sequence again by taking the rename_lock.
In this case, there is no need to take the RCU read lock as the recursive
parent pointer references will keep the dentry chain alive as long as no
rename operation is performed.

.. _`__d_path`:

__d_path
========

.. c:function:: char *__d_path(const struct path *path, const struct path *root, char *buf, int buflen)

    return the path of a dentry

    :param const struct path \*path:
        the dentry/vfsmount to report

    :param const struct path \*root:
        root vfsmnt/dentry

    :param char \*buf:
        buffer to return value in

    :param int buflen:
        buffer length

.. _`__d_path.description`:

Description
-----------

Convert a dentry into an ASCII path name.

Returns a pointer into the buffer or an error code if the
path was too long.

"buflen" should be positive.

If the path is not reachable from the supplied root, return \ ``NULL``\ .

.. _`d_path`:

d_path
======

.. c:function:: char *d_path(const struct path *path, char *buf, int buflen)

    return the path of a dentry

    :param const struct path \*path:
        path to report

    :param char \*buf:
        buffer to return value in

    :param int buflen:
        buffer length

.. _`d_path.description`:

Description
-----------

Convert a dentry into an ASCII path name. If the entry has been deleted
the string " (deleted)" is appended. Note that this is ambiguous.

Returns a pointer into the buffer or an error code if the path was
too long. Note: Callers should use the returned pointer, not the passed
in buffer, to use the name! The implementation often starts at an offset
into the buffer, and may leave 0 bytes at the start.

"buflen" should be positive.

.. _`is_subdir`:

is_subdir
=========

.. c:function:: bool is_subdir(struct dentry *new_dentry, struct dentry *old_dentry)

    is new dentry a subdirectory of old_dentry

    :param struct dentry \*new_dentry:
        new dentry

    :param struct dentry \*old_dentry:
        old dentry

.. _`is_subdir.description`:

Description
-----------

Returns true if new_dentry is a subdirectory of the parent (at any depth).
Returns false otherwise.
Caller must ensure that "new_dentry" is pinned before calling \ :c:func:`is_subdir`\ 

.. This file was automatic generated / don't edit.

