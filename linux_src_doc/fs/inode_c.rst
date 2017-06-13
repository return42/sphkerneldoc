.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/inode.c

.. _`inode_init_always`:

inode_init_always
=================

.. c:function:: int inode_init_always(struct super_block *sb, struct inode *inode)

    perform inode structure initialisation

    :param struct super_block \*sb:
        superblock inode belongs to

    :param struct inode \*inode:
        inode to initialise

.. _`inode_init_always.description`:

Description
-----------

These are initializations that need to be done on every inode
allocation as the fields are not initialised by slab allocation.

.. _`drop_nlink`:

drop_nlink
==========

.. c:function:: void drop_nlink(struct inode *inode)

    directly drop an inode's link count

    :param struct inode \*inode:
        inode

.. _`drop_nlink.description`:

Description
-----------

This is a low-level filesystem helper to replace any
direct filesystem manipulation of i_nlink.  In cases
where we are attempting to track writes to the
filesystem, a decrement to zero means an imminent
write when the file is truncated and actually unlinked
on the filesystem.

.. _`clear_nlink`:

clear_nlink
===========

.. c:function:: void clear_nlink(struct inode *inode)

    directly zero an inode's link count

    :param struct inode \*inode:
        inode

.. _`clear_nlink.description`:

Description
-----------

This is a low-level filesystem helper to replace any
direct filesystem manipulation of i_nlink.  See
\ :c:func:`drop_nlink`\  for why we care about i_nlink hitting zero.

.. _`set_nlink`:

set_nlink
=========

.. c:function:: void set_nlink(struct inode *inode, unsigned int nlink)

    directly set an inode's link count

    :param struct inode \*inode:
        inode

    :param unsigned int nlink:
        new nlink (should be non-zero)

.. _`set_nlink.description`:

Description
-----------

This is a low-level filesystem helper to replace any
direct filesystem manipulation of i_nlink.

.. _`inc_nlink`:

inc_nlink
=========

.. c:function:: void inc_nlink(struct inode *inode)

    directly increment an inode's link count

    :param struct inode \*inode:
        inode

.. _`inc_nlink.description`:

Description
-----------

This is a low-level filesystem helper to replace any
direct filesystem manipulation of i_nlink.  Currently,
it is only here for parity with \ :c:func:`dec_nlink`\ .

.. _`inode_sb_list_add`:

inode_sb_list_add
=================

.. c:function:: void inode_sb_list_add(struct inode *inode)

    add inode to the superblock list of inodes

    :param struct inode \*inode:
        inode to add

.. _`__insert_inode_hash`:

__insert_inode_hash
===================

.. c:function:: void __insert_inode_hash(struct inode *inode, unsigned long hashval)

    hash an inode

    :param struct inode \*inode:
        unhashed inode

    :param unsigned long hashval:
        unsigned long value used to locate this object in the
        inode_hashtable.

.. _`__insert_inode_hash.description`:

Description
-----------

     Add an inode to the inode hash for this superblock.

.. _`__remove_inode_hash`:

__remove_inode_hash
===================

.. c:function:: void __remove_inode_hash(struct inode *inode)

    remove an inode from the hash

    :param struct inode \*inode:
        inode to unhash

.. _`__remove_inode_hash.description`:

Description
-----------

     Remove an inode from the superblock.

.. _`evict_inodes`:

evict_inodes
============

.. c:function:: void evict_inodes(struct super_block *sb)

    evict all evictable inodes for a superblock

    :param struct super_block \*sb:
        superblock to operate on

.. _`evict_inodes.description`:

Description
-----------

Make sure that no inodes with zero refcount are retained.  This is
called by superblock shutdown after having MS_ACTIVE flag removed,
so any inode reaching zero refcount during or after that call will
be immediately evicted.

.. _`invalidate_inodes`:

invalidate_inodes
=================

.. c:function:: int invalidate_inodes(struct super_block *sb, bool kill_dirty)

    attempt to free all inodes on a superblock

    :param struct super_block \*sb:
        superblock to operate on

    :param bool kill_dirty:
        flag to guide handling of dirty inodes

.. _`invalidate_inodes.description`:

Description
-----------

Attempts to free all inodes for a given superblock.  If there were any
busy inodes return a non-zero value, else zero.
If \ ``kill_dirty``\  is set, discard dirty inodes too, otherwise treat
them as busy.

.. _`new_inode_pseudo`:

new_inode_pseudo
================

.. c:function:: struct inode *new_inode_pseudo(struct super_block *sb)

    obtain an inode

    :param struct super_block \*sb:
        superblock

.. _`new_inode_pseudo.description`:

Description
-----------

     Allocates a new inode for given superblock.
     Inode wont be chained in superblock s_inodes list
     This means :
     - fs can't be unmount
     - quotas, fsnotify, writeback can't work

.. _`new_inode`:

new_inode
=========

.. c:function:: struct inode *new_inode(struct super_block *sb)

    obtain an inode

    :param struct super_block \*sb:
        superblock

.. _`new_inode.description`:

Description
-----------

     Allocates a new inode for given superblock. The default gfp_mask
     for allocations related to inode->i_mapping is GFP_HIGHUSER_MOVABLE.
     If HIGHMEM pages are unsuitable or it is known that pages allocated
     for the page cache are not reclaimable or migratable,
     \ :c:func:`mapping_set_gfp_mask`\  must be called with suitable flags on the
     newly created inode's mapping

.. _`unlock_new_inode`:

unlock_new_inode
================

.. c:function:: void unlock_new_inode(struct inode *inode)

    clear the I_NEW state and wake up any waiters

    :param struct inode \*inode:
        new inode to unlock

.. _`unlock_new_inode.description`:

Description
-----------

Called when the inode is fully initialised to clear the new state of the
inode and wake up anyone waiting for the inode to finish initialisation.

.. _`lock_two_nondirectories`:

lock_two_nondirectories
=======================

.. c:function:: void lock_two_nondirectories(struct inode *inode1, struct inode *inode2)

    take two i_mutexes on non-directory objects

    :param struct inode \*inode1:
        first inode to lock

    :param struct inode \*inode2:
        second inode to lock

.. _`lock_two_nondirectories.description`:

Description
-----------

Lock any non-NULL argument that is not a directory.
Zero, one or two objects may be locked by this function.

.. _`unlock_two_nondirectories`:

unlock_two_nondirectories
=========================

.. c:function:: void unlock_two_nondirectories(struct inode *inode1, struct inode *inode2)

    release locks from \ :c:func:`lock_two_nondirectories`\ 

    :param struct inode \*inode1:
        first inode to unlock

    :param struct inode \*inode2:
        second inode to unlock

.. _`iget5_locked`:

iget5_locked
============

.. c:function:: struct inode *iget5_locked(struct super_block *sb, unsigned long hashval, int (*test)(struct inode *, void *), int (*set)(struct inode *, void *), void *data)

    obtain an inode from a mounted file system

    :param struct super_block \*sb:
        super block of file system

    :param unsigned long hashval:
        hash value (usually inode number) to get

    :param int (\*test)(struct inode \*, void \*):
        callback used for comparisons between inodes

    :param int (\*set)(struct inode \*, void \*):
        callback used to initialize a new struct inode

    :param void \*data:
        opaque data pointer to pass to \ ``test``\  and \ ``set``\ 

.. _`iget5_locked.description`:

Description
-----------

Search for the inode specified by \ ``hashval``\  and \ ``data``\  in the inode cache,
and if present it is return it with an increased reference count. This is
a generalized version of \ :c:func:`iget_locked`\  for file systems where the inode
number is not sufficient for unique identification of an inode.

If the inode is not in cache, allocate a new inode and return it locked,
hashed, and with the I_NEW flag set. The file system gets to fill it in
before unlocking it via \ :c:func:`unlock_new_inode`\ .

Note both \ ``test``\  and \ ``set``\  are called with the inode_hash_lock held, so can't
sleep.

.. _`iget_locked`:

iget_locked
===========

.. c:function:: struct inode *iget_locked(struct super_block *sb, unsigned long ino)

    obtain an inode from a mounted file system

    :param struct super_block \*sb:
        super block of file system

    :param unsigned long ino:
        inode number to get

.. _`iget_locked.description`:

Description
-----------

Search for the inode specified by \ ``ino``\  in the inode cache and if present
return it with an increased reference count. This is for file systems
where the inode number is sufficient for unique identification of an inode.

If the inode is not in cache, allocate a new inode and return it locked,
hashed, and with the I_NEW flag set.  The file system gets to fill it in
before unlocking it via \ :c:func:`unlock_new_inode`\ .

.. _`iunique`:

iunique
=======

.. c:function:: ino_t iunique(struct super_block *sb, ino_t max_reserved)

    get a unique inode number

    :param struct super_block \*sb:
        superblock

    :param ino_t max_reserved:
        highest reserved inode number

.. _`iunique.description`:

Description
-----------

     Obtain an inode number that is unique on the system for a given
     superblock. This is used by file systems that have no natural
     permanent inode numbering system. An inode number is returned that
     is higher than the reserved limit but unique.

.. _`iunique.bugs`:

BUGS
----

     With a large number of inodes live on the file system this function
     currently becomes quite slow.

.. _`ilookup5_nowait`:

ilookup5_nowait
===============

.. c:function:: struct inode *ilookup5_nowait(struct super_block *sb, unsigned long hashval, int (*test)(struct inode *, void *), void *data)

    search for an inode in the inode cache

    :param struct super_block \*sb:
        super block of file system to search

    :param unsigned long hashval:
        hash value (usually inode number) to search for

    :param int (\*test)(struct inode \*, void \*):
        callback used for comparisons between inodes

    :param void \*data:
        opaque data pointer to pass to \ ``test``\ 

.. _`ilookup5_nowait.description`:

Description
-----------

Search for the inode specified by \ ``hashval``\  and \ ``data``\  in the inode cache.
If the inode is in the cache, the inode is returned with an incremented
reference count.

.. _`ilookup5_nowait.note`:

Note
----

I_NEW is not waited upon so you have to be very careful what you do
with the returned inode.  You probably should be using \ :c:func:`ilookup5`\  instead.

Note2: \ ``test``\  is called with the inode_hash_lock held, so can't sleep.

.. _`ilookup5`:

ilookup5
========

.. c:function:: struct inode *ilookup5(struct super_block *sb, unsigned long hashval, int (*test)(struct inode *, void *), void *data)

    search for an inode in the inode cache

    :param struct super_block \*sb:
        super block of file system to search

    :param unsigned long hashval:
        hash value (usually inode number) to search for

    :param int (\*test)(struct inode \*, void \*):
        callback used for comparisons between inodes

    :param void \*data:
        opaque data pointer to pass to \ ``test``\ 

.. _`ilookup5.description`:

Description
-----------

Search for the inode specified by \ ``hashval``\  and \ ``data``\  in the inode cache,
and if the inode is in the cache, return the inode with an incremented
reference count.  Waits on I_NEW before returning the inode.
returned with an incremented reference count.

This is a generalized version of \ :c:func:`ilookup`\  for file systems where the
inode number is not sufficient for unique identification of an inode.

.. _`ilookup5.note`:

Note
----

@test is called with the inode_hash_lock held, so can't sleep.

.. _`ilookup`:

ilookup
=======

.. c:function:: struct inode *ilookup(struct super_block *sb, unsigned long ino)

    search for an inode in the inode cache

    :param struct super_block \*sb:
        super block of file system to search

    :param unsigned long ino:
        inode number to search for

.. _`ilookup.description`:

Description
-----------

Search for the inode \ ``ino``\  in the inode cache, and if the inode is in the
cache, the inode is returned with an incremented reference count.

.. _`find_inode_nowait`:

find_inode_nowait
=================

.. c:function:: struct inode *find_inode_nowait(struct super_block *sb, unsigned long hashval, int (*match)(struct inode *, unsigned long, void *), void *data)

    find an inode in the inode cache

    :param struct super_block \*sb:
        super block of file system to search

    :param unsigned long hashval:
        hash value (usually inode number) to search for

    :param int (\*match)(struct inode \*, unsigned long, void \*):
        callback used for comparisons between inodes

    :param void \*data:
        opaque data pointer to pass to \ ``match``\ 

.. _`find_inode_nowait.description`:

Description
-----------

Search for the inode specified by \ ``hashval``\  and \ ``data``\  in the inode
cache, where the helper function \ ``match``\  will return 0 if the inode
does not match, 1 if the inode does match, and -1 if the search
should be stopped.  The \ ``match``\  function must be responsible for
taking the i_lock spin_lock and checking i_state for an inode being
freed or being initialized, and incrementing the reference count
before returning 1.  It also must not sleep, since it is called with
the inode_hash_lock spinlock held.

This is a even more generalized version of \ :c:func:`ilookup5`\  when the
function must never block --- \ :c:func:`find_inode`\  can block in
\ :c:func:`__wait_on_freeing_inode`\  --- or when the caller can not increment
the reference count because the resulting \ :c:func:`iput`\  might cause an
inode eviction.  The tradeoff is that the \ ``match``\  funtion must be
very carefully implemented.

.. _`iput`:

iput
====

.. c:function:: void iput(struct inode *inode)

    put an inode

    :param struct inode \*inode:
        inode to put

.. _`iput.description`:

Description
-----------

     Puts an inode, dropping its usage count. If the inode use count hits
     zero, the inode is then freed and may also be destroyed.

     Consequently, \ :c:func:`iput`\  can sleep.

.. _`bmap`:

bmap
====

.. c:function:: sector_t bmap(struct inode *inode, sector_t block)

    find a block number in a file

    :param struct inode \*inode:
        inode of file

    :param sector_t block:
        block to find

.. _`bmap.description`:

Description
-----------

     Returns the block number on the device holding the inode that
     is the disk block number for the block of the file requested.
     That is, asked for block 4 of inode 1 the function will return the
     disk block relative to the disk start that holds that block of the
     file.

.. _`__atime_needs_update`:

__atime_needs_update
====================

.. c:function:: bool __atime_needs_update(const struct path *path, struct inode *inode, bool rcu)

    update the access time

    :param const struct path \*path:
        the \ :c:type:`struct path <path>`\  to update

    :param struct inode \*inode:
        inode to update

    :param bool rcu:
        *undescribed*

.. _`__atime_needs_update.description`:

Description
-----------

     Update the accessed time on an inode and mark it for writeback.
     This function automatically handles read only file systems and media,
     as well as the "noatime" flag and inode specific "noatime" markers.

.. _`file_update_time`:

file_update_time
================

.. c:function:: int file_update_time(struct file *file)

    update mtime and ctime time

    :param struct file \*file:
        file accessed

.. _`file_update_time.description`:

Description
-----------

     Update the mtime and ctime members of an inode and mark the inode
     for writeback.  Note that this function is meant exclusively for
     usage in the file write path of filesystems, and filesystems may
     choose to explicitly ignore update via this function with the
     S_NOCMTIME inode flag, e.g. for network filesystem where these
     timestamps are handled by the server.  This can return an error for
     file systems who need to allocate space in order to update an inode.

.. _`inode_init_owner`:

inode_init_owner
================

.. c:function:: void inode_init_owner(struct inode *inode, const struct inode *dir, umode_t mode)

    Init uid,gid,mode for new inode according to posix standards

    :param struct inode \*inode:
        New inode

    :param const struct inode \*dir:
        Directory inode

    :param umode_t mode:
        mode of the new inode

.. _`inode_owner_or_capable`:

inode_owner_or_capable
======================

.. c:function:: bool inode_owner_or_capable(const struct inode *inode)

    check current task permissions to inode

    :param const struct inode \*inode:
        inode being checked

.. _`inode_owner_or_capable.description`:

Description
-----------

Return true if current either has CAP_FOWNER in a namespace with the
inode owner uid mapped, or owns the file.

.. _`inode_dio_wait`:

inode_dio_wait
==============

.. c:function:: void inode_dio_wait(struct inode *inode)

    wait for outstanding DIO requests to finish

    :param struct inode \*inode:
        inode to wait for

.. _`inode_dio_wait.description`:

Description
-----------

Waits for all pending direct I/O requests to finish so that we can
proceed with a truncate or equivalent operation.

Must be called under a lock that serializes taking new references
to i_dio_count, usually by inode->i_mutex.

.. _`current_time`:

current_time
============

.. c:function:: struct timespec current_time(struct inode *inode)

    Return FS time

    :param struct inode \*inode:
        inode.

.. _`current_time.description`:

Description
-----------

Return the current time truncated to the time granularity supported by
the fs.

Note that inode and inode->sb cannot be NULL.
Otherwise, the function warns and returns time without truncation.

.. This file was automatic generated / don't edit.

