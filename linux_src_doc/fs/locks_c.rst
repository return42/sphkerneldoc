.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/locks.c

.. _`posix_lock_file`:

posix_lock_file
===============

.. c:function:: int posix_lock_file(struct file *filp, struct file_lock *fl, struct file_lock *conflock)

    Apply a POSIX-style lock to a file

    :param filp:
        The file to apply the lock to
    :type filp: struct file \*

    :param fl:
        The lock to be applied
    :type fl: struct file_lock \*

    :param conflock:
        Place to return a copy of the conflicting lock, if found.
    :type conflock: struct file_lock \*

.. _`posix_lock_file.description`:

Description
-----------

Add a POSIX style lock to a file.
We merge adjacent & overlapping locks whenever possible.
POSIX locks are sorted by owner task, then by starting address

Note that if called with an FL_EXISTS argument, the caller may determine
whether or not a lock was successfully freed by testing the return
value for -ENOENT.

.. _`posix_lock_inode_wait`:

posix_lock_inode_wait
=====================

.. c:function:: int posix_lock_inode_wait(struct inode *inode, struct file_lock *fl)

    Apply a POSIX-style lock to a file

    :param inode:
        inode of file to which lock request should be applied
    :type inode: struct inode \*

    :param fl:
        The lock to be applied
    :type fl: struct file_lock \*

.. _`posix_lock_inode_wait.description`:

Description
-----------

Apply a POSIX style lock request to an inode.

.. _`locks_mandatory_locked`:

locks_mandatory_locked
======================

.. c:function:: int locks_mandatory_locked(struct file *file)

    Check for an active lock

    :param file:
        the file to check
    :type file: struct file \*

.. _`locks_mandatory_locked.description`:

Description
-----------

Searches the inode's list of locks to find any POSIX locks which conflict.
This function is called from \ :c:func:`locks_verify_locked`\  only.

.. _`locks_mandatory_area`:

locks_mandatory_area
====================

.. c:function:: int locks_mandatory_area(struct inode *inode, struct file *filp, loff_t start, loff_t end, unsigned char type)

    Check for a conflicting lock

    :param inode:
        the file to check
    :type inode: struct inode \*

    :param filp:
        how the file was opened (if it was)
    :type filp: struct file \*

    :param start:
        first byte in the file to check
    :type start: loff_t

    :param end:
        lastbyte in the file to check
    :type end: loff_t

    :param type:
        \ ``F_WRLCK``\  for a write lock, else \ ``F_RDLCK``\ 
    :type type: unsigned char

.. _`locks_mandatory_area.description`:

Description
-----------

Searches the inode's list of locks to find any POSIX locks which conflict.

.. _`__break_lease`:

__break_lease
=============

.. c:function:: int __break_lease(struct inode *inode, unsigned int mode, unsigned int type)

    revoke all outstanding leases on file

    :param inode:
        the inode of the file to return
    :type inode: struct inode \*

    :param mode:
        O_RDONLY: break only write leases; O_WRONLY or O_RDWR:
        break all leases
    :type mode: unsigned int

    :param type:
        FL_LEASE: break leases and delegations; FL_DELEG: break
        only delegations
    :type type: unsigned int

.. _`__break_lease.description`:

Description
-----------

     break_lease (inlined for speed) has checked there already is at least
     some kind of lock (maybe a lease) on this file.  Leases are broken on
     a call to \ :c:func:`open`\  or \ :c:func:`truncate`\ .  This function can sleep unless you
     specified \ ``O_NONBLOCK``\  to your \ :c:func:`open`\ .

.. _`lease_get_mtime`:

lease_get_mtime
===============

.. c:function:: void lease_get_mtime(struct inode *inode, struct timespec64 *time)

    update modified time of an inode with exclusive lease

    :param inode:
        the inode
    :type inode: struct inode \*

    :param time:
        pointer to a timespec which contains the last modified time
    :type time: struct timespec64 \*

.. _`lease_get_mtime.description`:

Description
-----------

This is to force NFS clients to flush their caches for files with
exclusive leases.  The justification is that if someone has an
exclusive lease, then they could be modifying it.

.. _`fcntl_getlease`:

fcntl_getlease
==============

.. c:function:: int fcntl_getlease(struct file *filp)

    Enquire what lease is currently active

    :param filp:
        the file
    :type filp: struct file \*

.. _`fcntl_getlease.description`:

Description
-----------

     The value returned by this function will be one of
     (if no lease break is pending):

     \ ``F_RDLCK``\  to indicate a shared lease is held.

     \ ``F_WRLCK``\  to indicate an exclusive lease is held.

     \ ``F_UNLCK``\  to indicate no lease is held.

     (if a lease break is pending):

     \ ``F_RDLCK``\  to indicate an exclusive lease needs to be
             changed to a shared lease (or removed).

     \ ``F_UNLCK``\  to indicate the lease needs to be removed.

     XXX: sfr & willy disagree over whether F_INPROGRESS
     should be returned to userspace.

.. _`check_conflicting_open`:

check_conflicting_open
======================

.. c:function:: int check_conflicting_open(const struct dentry *dentry, const long arg, int flags)

    see if the given dentry points to a file that has an existing open that would conflict with the desired lease.

    :param dentry:
        dentry to check
    :type dentry: const struct dentry \*

    :param arg:
        type of lease that we're trying to acquire
    :type arg: const long

    :param flags:
        current lock flags
    :type flags: int

.. _`check_conflicting_open.description`:

Description
-----------

Check to see if there's an existing open fd on this file that would
conflict with the lease we're trying to set.

.. _`generic_setlease`:

generic_setlease
================

.. c:function:: int generic_setlease(struct file *filp, long arg, struct file_lock **flp, void **priv)

    sets a lease on an open file

    :param filp:
        file pointer
    :type filp: struct file \*

    :param arg:
        type of lease to obtain
    :type arg: long

    :param flp:
        input - file_lock to use, output - file_lock inserted
    :type flp: struct file_lock \*\*

    :param priv:
        private data for lm_setup (may be NULL if lm_setup
        doesn't require it)
    :type priv: void \*\*

.. _`generic_setlease.description`:

Description
-----------

     The (input) flp->fl_lmops->lm_break function is required
     by \ :c:func:`break_lease`\ .

.. _`vfs_setlease`:

vfs_setlease
============

.. c:function:: int vfs_setlease(struct file *filp, long arg, struct file_lock **lease, void **priv)

    sets a lease on an open file

    :param filp:
        file pointer
    :type filp: struct file \*

    :param arg:
        type of lease to obtain
    :type arg: long

    :param lease:
        file_lock to use when adding a lease
    :type lease: struct file_lock \*\*

    :param priv:
        private info for lm_setup when adding a lease (may be
        NULL if lm_setup doesn't require it)
    :type priv: void \*\*

.. _`vfs_setlease.description`:

Description
-----------

Call this to establish a lease on the file. The "lease" argument is not
used for F_UNLCK requests and may be NULL. For commands that set or alter
an existing lease, the ``(*lease)->fl_lmops->lm_break`` operation must be
set; if not, this function will return -ENOLCK (and generate a scary-looking
stack trace).

The "priv" pointer is passed directly to the lm_setup function as-is. It
may be NULL if the lm_setup operation doesn't require it.

.. _`fcntl_setlease`:

fcntl_setlease
==============

.. c:function:: int fcntl_setlease(unsigned int fd, struct file *filp, long arg)

    sets a lease on an open file

    :param fd:
        open file descriptor
    :type fd: unsigned int

    :param filp:
        file pointer
    :type filp: struct file \*

    :param arg:
        type of lease to obtain
    :type arg: long

.. _`fcntl_setlease.description`:

Description
-----------

     Call this fcntl to establish a lease on the file.
     Note that you also need to call \ ``F_SETSIG``\  to
     receive a signal when the lease is broken.

.. _`flock_lock_inode_wait`:

flock_lock_inode_wait
=====================

.. c:function:: int flock_lock_inode_wait(struct inode *inode, struct file_lock *fl)

    Apply a FLOCK-style lock to a file

    :param inode:
        inode of the file to apply to
    :type inode: struct inode \*

    :param fl:
        The lock to be applied
    :type fl: struct file_lock \*

.. _`flock_lock_inode_wait.description`:

Description
-----------

Apply a FLOCK style lock request to an inode.

.. _`locks_lock_inode_wait`:

locks_lock_inode_wait
=====================

.. c:function:: int locks_lock_inode_wait(struct inode *inode, struct file_lock *fl)

    Apply a lock to an inode

    :param inode:
        inode of the file to apply to
    :type inode: struct inode \*

    :param fl:
        The lock to be applied
    :type fl: struct file_lock \*

.. _`locks_lock_inode_wait.description`:

Description
-----------

Apply a POSIX or FLOCK style lock request to an inode.

.. _`sys_flock`:

sys_flock
=========

.. c:function:: long sys_flock(unsigned int fd, unsigned int cmd)

    - \ :c:func:`flock`\  system call.

    :param fd:
        the file descriptor to lock.
    :type fd: unsigned int

    :param cmd:
        the type of lock to apply.
    :type cmd: unsigned int

.. _`sys_flock.description`:

Description
-----------

     Apply a \ ``FL_FLOCK``\  style lock to an open file descriptor.
     The \ ``cmd``\  can be one of:

     - \ ``LOCK_SH``\  -- a shared lock.
     - \ ``LOCK_EX``\  -- an exclusive lock.
     - \ ``LOCK_UN``\  -- remove an existing lock.
     - \ ``LOCK_MAND``\  -- a 'mandatory' flock.
       This exists to emulate Windows Share Modes.

     \ ``LOCK_MAND``\  can be combined with \ ``LOCK_READ``\  or \ ``LOCK_WRITE``\  to allow other
     processes read and write access respectively.

.. _`vfs_test_lock`:

vfs_test_lock
=============

.. c:function:: int vfs_test_lock(struct file *filp, struct file_lock *fl)

    test file byte range lock

    :param filp:
        The file to test lock for
    :type filp: struct file \*

    :param fl:
        The lock to test; also used to hold result
    :type fl: struct file_lock \*

.. _`vfs_test_lock.description`:

Description
-----------

Returns -ERRNO on failure.  Indicates presence of conflicting lock by
setting conf->fl_type to something other than F_UNLCK.

.. _`locks_translate_pid`:

locks_translate_pid
===================

.. c:function:: pid_t locks_translate_pid(struct file_lock *fl, struct pid_namespace *ns)

    translate a file_lock's fl_pid number into a namespace

    :param fl:
        The file_lock who's fl_pid should be translated
    :type fl: struct file_lock \*

    :param ns:
        The namespace into which the pid should be translated
    :type ns: struct pid_namespace \*

.. _`locks_translate_pid.description`:

Description
-----------

Used to tranlate a fl_pid into a namespace virtual pid number

.. _`vfs_lock_file`:

vfs_lock_file
=============

.. c:function:: int vfs_lock_file(struct file *filp, unsigned int cmd, struct file_lock *fl, struct file_lock *conf)

    file byte range lock

    :param filp:
        The file to apply the lock to
    :type filp: struct file \*

    :param cmd:
        type of locking operation (F_SETLK, F_GETLK, etc.)
    :type cmd: unsigned int

    :param fl:
        The lock to be applied
    :type fl: struct file_lock \*

    :param conf:
        Place to return a copy of the conflicting lock, if found.
    :type conf: struct file_lock \*

.. _`vfs_lock_file.description`:

Description
-----------

A caller that doesn't care about the conflicting lock may pass NULL
as the final argument.

If the filesystem defines a private ->lock() method, then \ ``conf``\  will
be left unchanged; so a caller that cares should initialize it to
some acceptable default.

To avoid blocking kernel daemons, such as lockd, that need to acquire POSIX
locks, the ->lock() interface may return asynchronously, before the lock has
been granted or denied by the underlying filesystem, if (and only if)
lm_grant is set. Callers expecting ->lock() to return asynchronously
will only use F_SETLK, not F_SETLKW; they will set FL_SLEEP if (and only if)
the request is for a blocking lock. When ->lock() does return asynchronously,
it must return FILE_LOCK_DEFERRED, and call ->lm_grant() when the lock
request completes.
If the request is for non-blocking lock the file system should return
FILE_LOCK_DEFERRED then try to get the lock and call the callback routine
with the result. If the request timed out the callback routine will return a
nonzero return code and the file system should release the lock. The file
system is also responsible to keep a corresponding posix lock when it
grants a lock so the VFS can find out which locks are locally held and do
the correct lock cleanup when required.
The underlying filesystem must not drop the kernel lock or call
->lm_grant() before returning to the caller with a FILE_LOCK_DEFERRED
return code.

.. _`posix_unblock_lock`:

posix_unblock_lock
==================

.. c:function:: int posix_unblock_lock(struct file_lock *waiter)

    stop waiting for a file lock

    :param waiter:
        the lock which was waiting
    :type waiter: struct file_lock \*

.. _`posix_unblock_lock.description`:

Description
-----------

     lockd needs to block waiting for locks.

.. _`vfs_cancel_lock`:

vfs_cancel_lock
===============

.. c:function:: int vfs_cancel_lock(struct file *filp, struct file_lock *fl)

    file byte range unblock lock

    :param filp:
        The file to apply the unblock to
    :type filp: struct file \*

    :param fl:
        The lock to be unblocked
    :type fl: struct file_lock \*

.. _`vfs_cancel_lock.description`:

Description
-----------

Used by lock managers to cancel blocked requests

.. This file was automatic generated / don't edit.

