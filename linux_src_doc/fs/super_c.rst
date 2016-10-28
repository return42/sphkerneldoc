.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/super.c

.. _`destroy_super`:

destroy_super
=============

.. c:function:: void destroy_super(struct super_block *s)

    frees a superblock

    :param struct super_block \*s:
        superblock to free

.. _`destroy_super.description`:

Description
-----------

Frees a superblock.

.. _`alloc_super`:

alloc_super
===========

.. c:function:: struct super_block *alloc_super(struct file_system_type *type, int flags)

    create new superblock

    :param struct file_system_type \*type:
        filesystem type superblock should belong to

    :param int flags:
        the mount flags

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

    :param struct super_block \*sb:
        superblock in question

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

    :param struct super_block \*s:
        superblock to deactivate

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

    :param struct super_block \*s:
        superblock to deactivate

.. _`deactivate_super.description`:

Description
-----------

Variant of \ :c:func:`deactivate_locked_super`\ , except that superblock is \*not\*
locked by caller.  If we are going to drop the final active reference,
lock will be acquired prior to that.

.. _`grab_super`:

grab_super
==========

.. c:function:: int grab_super(struct super_block *s)

    acquire an active reference

    :param struct super_block \*s:
        reference we are trying to make active

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

    common helper for ->\ :c:func:`kill_sb`\ 

    :param struct super_block \*sb:
        superblock to kill

.. _`generic_shutdown_super.description`:

Description
-----------

\ :c:func:`generic_shutdown_super`\  does all fs-independent work on superblock
shutdown.  Typical ->\ :c:func:`kill_sb`\  should pick all fs-specific objects
that need destruction out of superblock, call \ :c:func:`generic_shutdown_super`\ 
and release aforementioned objects.  Note: dentries and inodes \_are\_
taken care of and do not need specific handling.

Upon calling this function, the filesystem may no longer alter or
rearrange the set of dentries belonging to this super_block, nor may it
change the attachments of dentries to inodes.

.. _`sget`:

sget
====

.. c:function:: struct super_block *sget(struct file_system_type *type, int (*test)(struct super_block *,void *), int (*set)(struct super_block *,void *), int flags, void *data)

    find or create a superblock

    :param struct file_system_type \*type:
        filesystem type superblock should belong to

    :param int (\*test)(struct super_block \*,void \*):
        comparison callback

    :param int (\*set)(struct super_block \*,void \*):
        setup callback

    :param int flags:
        mount flags

    :param void \*data:
        argument to each of them

.. _`iterate_supers`:

iterate_supers
==============

.. c:function:: void iterate_supers(void (*f)(struct super_block *, void *), void *arg)

    call function for all active superblocks

    :param void (\*f)(struct super_block \*, void \*):
        function to call

    :param void \*arg:
        argument to pass to it

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

    :param struct file_system_type \*type:
        fs type

    :param void (\*f)(struct super_block \*, void \*):
        function to call

    :param void \*arg:
        argument to pass to it

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

    :param struct block_device \*bdev:
        device to get the superblock for

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

    :param struct block_device \*bdev:
        device to get the superblock for

.. _`get_super_thawed.description`:

Description
-----------

Scans the superblock list and finds the superblock of the file system
mounted on the device. The superblock is returned once it is thawed
(or immediately if it was not frozen). \ ``NULL``\  is returned if no match
is found.

.. _`get_active_super`:

get_active_super
================

.. c:function:: struct super_block *get_active_super(struct block_device *bdev)

    get an active reference to the superblock of a device

    :param struct block_device \*bdev:
        device to get the superblock for

.. _`get_active_super.description`:

Description
-----------

Scans the superblock list and finds the superblock of the file system
mounted on the device given.  Returns the superblock with an active
reference or \ ``NULL``\  if none was found.

.. _`do_remount_sb`:

do_remount_sb
=============

.. c:function:: int do_remount_sb(struct super_block *sb, int flags, void *data, int force)

    asks filesystem to change mount options.

    :param struct super_block \*sb:
        superblock in question

    :param int flags:
        numeric part of options

    :param void \*data:
        the rest of options

    :param int force:
        whether or not to force the change

.. _`do_remount_sb.description`:

Description
-----------

Alters the mount options of a mounted file system.

.. _`sb_wait_write`:

sb_wait_write
=============

.. c:function:: void sb_wait_write(struct super_block *sb, int level)

    wait until all writers to given file system finish

    :param struct super_block \*sb:
        the super for which we wait

    :param int level:
        type of writers we wait for (normal vs page fault)

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

    :param struct super_block \*sb:
        the super to lock

.. _`freeze_super.description`:

Description
-----------

Syncs the super to make sure the filesystem is consistent and calls the fs's
freeze_fs.  Subsequent calls to this without first thawing the fs will return
-EBUSY.

During this function, sb->s_writers.frozen goes through these values:

.. _`freeze_super.sb_unfrozen`:

SB_UNFROZEN
-----------

File system is normal, all writes progress as usual.

.. _`freeze_super.sb_freeze_write`:

SB_FREEZE_WRITE
---------------

The file system is in the process of being frozen.  New
writes should be blocked, though page faults are still allowed. We wait for
all writes to complete and then proceed to the next stage.

.. _`freeze_super.sb_freeze_pagefault`:

SB_FREEZE_PAGEFAULT
-------------------

Freezing continues. Now also page faults are blocked
but internal fs threads can still modify the filesystem (although they
should not dirty new pages or inodes), writeback can run etc. After waiting
for all running page faults we sync the filesystem which will clean all
dirty pages and inodes (no new dirty pages or inodes can be created when
sync is running).

.. _`freeze_super.sb_freeze_fs`:

SB_FREEZE_FS
------------

The file system is frozen. Now all internal sources of fs
modification are blocked (e.g. XFS preallocation truncation on inode
reclaim). This is usually implemented by blocking new transactions for
filesystems that have them and need this additional guard. After all
internal writers are finished we call ->\ :c:func:`freeze_fs`\  to finish filesystem
freezing. Then we transition to SB_FREEZE_COMPLETE state. This state is
mostly auxiliary for filesystems to verify they do not modify frozen fs.

sb->s_writers.frozen is protected by sb->s_umount.

.. _`thaw_super`:

thaw_super
==========

.. c:function:: int thaw_super(struct super_block *sb)

    - unlock filesystem

    :param struct super_block \*sb:
        the super to thaw

.. _`thaw_super.description`:

Description
-----------

Unlocks the filesystem and marks it writeable again after \ :c:func:`freeze_super`\ .

.. This file was automatic generated / don't edit.

