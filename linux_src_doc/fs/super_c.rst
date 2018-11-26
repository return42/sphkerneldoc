.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/super.c

.. _`alloc_super`:

alloc_super
===========

.. c:function:: struct super_block *alloc_super(struct file_system_type *type, int flags, struct user_namespace *user_ns)

    create new superblock

    :param type:
        filesystem type superblock should belong to
    :type type: struct file_system_type \*

    :param flags:
        the mount flags
    :type flags: int

    :param user_ns:
        User namespace for the super_block
    :type user_ns: struct user_namespace \*

.. _`alloc_super.description`:

Description
-----------

     Allocates and initializes a new \ :c:type:`struct super_block <super_block>`\ .  \ :c:func:`alloc_super`\ 
     returns a pointer new superblock or \ ``NULL``\  if allocation had failed.

.. _`put_super`:

put_super
=========

.. c:function:: void put_super(struct super_block *sb)

    drop a temporary reference to superblock

    :param sb:
        superblock in question
    :type sb: struct super_block \*

.. _`put_super.description`:

Description
-----------

     Drops a temporary reference, frees superblock if there's no
     references left.

.. _`deactivate_locked_super`:

deactivate_locked_super
=======================

.. c:function:: void deactivate_locked_super(struct super_block *s)

    drop an active reference to superblock

    :param s:
        superblock to deactivate
    :type s: struct super_block \*

.. _`deactivate_locked_super.description`:

Description
-----------

     Drops an active reference to superblock, converting it into a temporary
     one if there is no other active references left.  In that case we
     tell fs driver to shut it down and drop the temporary reference we
     had just acquired.

     Caller holds exclusive lock on superblock; that lock is released.

.. _`deactivate_super`:

deactivate_super
================

.. c:function:: void deactivate_super(struct super_block *s)

    drop an active reference to superblock

    :param s:
        superblock to deactivate
    :type s: struct super_block \*

.. _`deactivate_super.description`:

Description
-----------

     Variant of \ :c:func:`deactivate_locked_super`\ , except that superblock is *not*
     locked by caller.  If we are going to drop the final active reference,
     lock will be acquired prior to that.

.. _`grab_super`:

grab_super
==========

.. c:function:: int grab_super(struct super_block *s)

    acquire an active reference

    :param s:
        reference we are trying to make active
    :type s: struct super_block \*

.. _`grab_super.description`:

Description
-----------

     Tries to acquire an active reference.  \ :c:func:`grab_super`\  is used when we
     had just found a superblock in super_blocks or fs_type->fs_supers
     and want to turn it into a full-blown active reference.  \ :c:func:`grab_super`\ 
     is called with sb_lock held and drops it.  Returns 1 in case of
     success, 0 if we had failed (superblock contents was already dead or
     dying when \ :c:func:`grab_super`\  had been called).  Note that this is only
     called for superblocks not in rundown mode (== ones still on ->fs_supers
     of their type), so increment of ->s_count is OK here.

.. _`generic_shutdown_super`:

generic_shutdown_super
======================

.. c:function:: void generic_shutdown_super(struct super_block *sb)

    common helper for ->kill_sb()

    :param sb:
        superblock to kill
    :type sb: struct super_block \*

.. _`generic_shutdown_super.description`:

Description
-----------

     \ :c:func:`generic_shutdown_super`\  does all fs-independent work on superblock
     shutdown.  Typical ->kill_sb() should pick all fs-specific objects
     that need destruction out of superblock, call \ :c:func:`generic_shutdown_super`\ 
     and release aforementioned objects.  Note: dentries and inodes _are_
     taken care of and do not need specific handling.

     Upon calling this function, the filesystem may no longer alter or
     rearrange the set of dentries belonging to this super_block, nor may it
     change the attachments of dentries to inodes.

.. _`sget_userns`:

sget_userns
===========

.. c:function:: struct super_block *sget_userns(struct file_system_type *type, int (*test)(struct super_block *,void *), int (*set)(struct super_block *,void *), int flags, struct user_namespace *user_ns, void *data)

    find or create a superblock

    :param type:
        filesystem type superblock should belong to
    :type type: struct file_system_type \*

    :param int (\*test)(struct super_block \*,void \*):
        comparison callback

    :param int (\*set)(struct super_block \*,void \*):
        setup callback

    :param flags:
        mount flags
    :type flags: int

    :param user_ns:
        User namespace for the super_block
    :type user_ns: struct user_namespace \*

    :param data:
        argument to each of them
    :type data: void \*

.. _`sget`:

sget
====

.. c:function:: struct super_block *sget(struct file_system_type *type, int (*test)(struct super_block *,void *), int (*set)(struct super_block *,void *), int flags, void *data)

    find or create a superblock

    :param type:
        filesystem type superblock should belong to
    :type type: struct file_system_type \*

    :param int (\*test)(struct super_block \*,void \*):
        comparison callback

    :param int (\*set)(struct super_block \*,void \*):
        setup callback

    :param flags:
        mount flags
    :type flags: int

    :param data:
        argument to each of them
    :type data: void \*

.. _`iterate_supers`:

iterate_supers
==============

.. c:function:: void iterate_supers(void (*f)(struct super_block *, void *), void *arg)

    call function for all active superblocks

    :param void (\*f)(struct super_block \*, void \*):
        function to call

    :param arg:
        argument to pass to it
    :type arg: void \*

.. _`iterate_supers.description`:

Description
-----------

     Scans the superblock list and calls given function, passing it
     locked superblock and given argument.

.. _`iterate_supers_type`:

iterate_supers_type
===================

.. c:function:: void iterate_supers_type(struct file_system_type *type, void (*f)(struct super_block *, void *), void *arg)

    call function for superblocks of given type

    :param type:
        fs type
    :type type: struct file_system_type \*

    :param void (\*f)(struct super_block \*, void \*):
        function to call

    :param arg:
        argument to pass to it
    :type arg: void \*

.. _`iterate_supers_type.description`:

Description
-----------

     Scans the superblock list and calls given function, passing it
     locked superblock and given argument.

.. _`get_super`:

get_super
=========

.. c:function:: struct super_block *get_super(struct block_device *bdev)

    get the superblock of a device

    :param bdev:
        device to get the superblock for
    :type bdev: struct block_device \*

.. _`get_super.description`:

Description
-----------

     Scans the superblock list and finds the superblock of the file system
     mounted on the device given. \ ``NULL``\  is returned if no match is found.

.. _`get_super_thawed`:

get_super_thawed
================

.. c:function:: struct super_block *get_super_thawed(struct block_device *bdev)

    get thawed superblock of a device

    :param bdev:
        device to get the superblock for
    :type bdev: struct block_device \*

.. _`get_super_thawed.description`:

Description
-----------

     Scans the superblock list and finds the superblock of the file system
     mounted on the device. The superblock is returned once it is thawed
     (or immediately if it was not frozen). \ ``NULL``\  is returned if no match
     is found.

.. _`get_super_exclusive_thawed`:

get_super_exclusive_thawed
==========================

.. c:function:: struct super_block *get_super_exclusive_thawed(struct block_device *bdev)

    get thawed superblock of a device

    :param bdev:
        device to get the superblock for
    :type bdev: struct block_device \*

.. _`get_super_exclusive_thawed.description`:

Description
-----------

     Scans the superblock list and finds the superblock of the file system
     mounted on the device. The superblock is returned once it is thawed
     (or immediately if it was not frozen) and s_umount semaphore is held
     in exclusive mode. \ ``NULL``\  is returned if no match is found.

.. _`get_active_super`:

get_active_super
================

.. c:function:: struct super_block *get_active_super(struct block_device *bdev)

    get an active reference to the superblock of a device

    :param bdev:
        device to get the superblock for
    :type bdev: struct block_device \*

.. _`get_active_super.description`:

Description
-----------

Scans the superblock list and finds the superblock of the file system
mounted on the device given.  Returns the superblock with an active
reference or \ ``NULL``\  if none was found.

.. _`do_remount_sb`:

do_remount_sb
=============

.. c:function:: int do_remount_sb(struct super_block *sb, int sb_flags, void *data, int force)

    asks filesystem to change mount options.

    :param sb:
        superblock in question
    :type sb: struct super_block \*

    :param sb_flags:
        revised superblock flags
    :type sb_flags: int

    :param data:
        the rest of options
    :type data: void \*

    :param force:
        whether or not to force the change
    :type force: int

.. _`do_remount_sb.description`:

Description
-----------

     Alters the mount options of a mounted file system.

.. _`emergency_thaw_all`:

emergency_thaw_all
==================

.. c:function:: void emergency_thaw_all( void)

    - forcibly thaw every frozen filesystem

    :param void:
        no arguments
    :type void: 

.. _`emergency_thaw_all.description`:

Description
-----------

Used for emergency unfreeze of all filesystems via SysRq

.. _`get_anon_bdev`:

get_anon_bdev
=============

.. c:function:: int get_anon_bdev(dev_t *p)

    Allocate a block device for filesystems which don't have one.

    :param p:
        Pointer to a dev_t.
    :type p: dev_t \*

.. _`get_anon_bdev.description`:

Description
-----------

Filesystems which don't use real block devices can call this function
to allocate a virtual block device.

.. _`get_anon_bdev.context`:

Context
-------

Any context.  Frequently called while holding sb_lock.

.. _`get_anon_bdev.return`:

Return
------

0 on success, -EMFILE if there are no anonymous bdevs left
or -ENOMEM if memory allocation failed.

.. _`sb_wait_write`:

sb_wait_write
=============

.. c:function:: void sb_wait_write(struct super_block *sb, int level)

    wait until all writers to given file system finish

    :param sb:
        the super for which we wait
    :type sb: struct super_block \*

    :param level:
        type of writers we wait for (normal vs page fault)
    :type level: int

.. _`sb_wait_write.description`:

Description
-----------

This function waits until there are no writers of given type to given file
system.

.. _`freeze_super`:

freeze_super
============

.. c:function:: int freeze_super(struct super_block *sb)

    lock the filesystem and force it into a consistent state

    :param sb:
        the super to lock
    :type sb: struct super_block \*

.. _`freeze_super.description`:

Description
-----------

Syncs the super to make sure the filesystem is consistent and calls the fs's
freeze_fs.  Subsequent calls to this without first thawing the fs will return
-EBUSY.

During this function, sb->s_writers.frozen goes through these values:

SB_UNFROZEN: File system is normal, all writes progress as usual.

SB_FREEZE_WRITE: The file system is in the process of being frozen.  New
writes should be blocked, though page faults are still allowed. We wait for
all writes to complete and then proceed to the next stage.

SB_FREEZE_PAGEFAULT: Freezing continues. Now also page faults are blocked
but internal fs threads can still modify the filesystem (although they
should not dirty new pages or inodes), writeback can run etc. After waiting
for all running page faults we sync the filesystem which will clean all
dirty pages and inodes (no new dirty pages or inodes can be created when
sync is running).

SB_FREEZE_FS: The file system is frozen. Now all internal sources of fs
modification are blocked (e.g. XFS preallocation truncation on inode
reclaim). This is usually implemented by blocking new transactions for
filesystems that have them and need this additional guard. After all
internal writers are finished we call ->freeze_fs() to finish filesystem
freezing. Then we transition to SB_FREEZE_COMPLETE state. This state is
mostly auxiliary for filesystems to verify they do not modify frozen fs.

sb->s_writers.frozen is protected by sb->s_umount.

.. _`thaw_super_locked`:

thaw_super_locked
=================

.. c:function:: int thaw_super_locked(struct super_block *sb)

    - unlock filesystem

    :param sb:
        the super to thaw
    :type sb: struct super_block \*

.. _`thaw_super_locked.description`:

Description
-----------

Unlocks the filesystem and marks it writeable again after \ :c:func:`freeze_super`\ .

.. This file was automatic generated / don't edit.

