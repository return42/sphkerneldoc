.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/commoncap.c

.. _`cap_capable`:

cap_capable
===========

.. c:function:: int cap_capable(const struct cred *cred, struct user_namespace *targ_ns, int cap, int audit)

    Determine whether a task has a particular effective capability

    :param cred:
        The credentials to use
    :type cred: const struct cred \*

    :param targ_ns:
        *undescribed*
    :type targ_ns: struct user_namespace \*

    :param cap:
        The capability to check for
    :type cap: int

    :param audit:
        Whether to write an audit message or not
    :type audit: int

.. _`cap_capable.description`:

Description
-----------

Determine whether the nominated task has the specified capability amongst
its effective set, returning 0 if it does, -ve if it does not.

.. _`cap_capable.note-well`:

NOTE WELL
---------

\ :c:func:`cap_has_capability`\  cannot be used like the kernel's \ :c:func:`capable`\ 
and \ :c:func:`has_capability`\  functions.  That is, it has the reverse semantics:
\ :c:func:`cap_has_capability`\  returns 0 when a task has a capability, but the
kernel's \ :c:func:`capable`\  and \ :c:func:`has_capability`\  returns 1 for this case.

.. _`cap_settime`:

cap_settime
===========

.. c:function:: int cap_settime(const struct timespec64 *ts, const struct timezone *tz)

    Determine whether the current process may set the system clock

    :param ts:
        The time to set
    :type ts: const struct timespec64 \*

    :param tz:
        The timezone to set
    :type tz: const struct timezone \*

.. _`cap_settime.description`:

Description
-----------

Determine whether the current process may set the system clock and timezone
information, returning 0 if permission granted, -ve if denied.

.. _`cap_ptrace_access_check`:

cap_ptrace_access_check
=======================

.. c:function:: int cap_ptrace_access_check(struct task_struct *child, unsigned int mode)

    Determine whether the current process may access another

    :param child:
        The process to be accessed
    :type child: struct task_struct \*

    :param mode:
        The mode of attachment.
    :type mode: unsigned int

.. _`cap_ptrace_access_check.description`:

Description
-----------

If we are in the same or an ancestor user_ns and have all the target
task's capabilities, then ptrace access is allowed.
If we have the ptrace capability to the target user_ns, then ptrace
access is allowed.
Else denied.

Determine whether a process may access another, returning 0 if permission
granted, -ve if denied.

.. _`cap_ptrace_traceme`:

cap_ptrace_traceme
==================

.. c:function:: int cap_ptrace_traceme(struct task_struct *parent)

    Determine whether another process may trace the current

    :param parent:
        The task proposed to be the tracer
    :type parent: struct task_struct \*

.. _`cap_ptrace_traceme.description`:

Description
-----------

If parent is in the same or an ancestor user_ns and has all current's
capabilities, then ptrace access is allowed.
If parent has the ptrace capability to current's user_ns, then ptrace
access is allowed.
Else denied.

Determine whether the nominated task is permitted to trace the current
process, returning 0 if permission is granted, -ve if denied.

.. _`cap_capget`:

cap_capget
==========

.. c:function:: int cap_capget(struct task_struct *target, kernel_cap_t *effective, kernel_cap_t *inheritable, kernel_cap_t *permitted)

    Retrieve a task's capability sets

    :param target:
        The task from which to retrieve the capability sets
    :type target: struct task_struct \*

    :param effective:
        The place to record the effective set
    :type effective: kernel_cap_t \*

    :param inheritable:
        The place to record the inheritable set
    :type inheritable: kernel_cap_t \*

    :param permitted:
        The place to record the permitted set
    :type permitted: kernel_cap_t \*

.. _`cap_capget.description`:

Description
-----------

This function retrieves the capabilities of the nominated task and returns
them to the caller.

.. _`cap_capset`:

cap_capset
==========

.. c:function:: int cap_capset(struct cred *new, const struct cred *old, const kernel_cap_t *effective, const kernel_cap_t *inheritable, const kernel_cap_t *permitted)

    Validate and apply proposed changes to current's capabilities

    :param new:
        The proposed new credentials; alterations should be made here
    :type new: struct cred \*

    :param old:
        The current task's current credentials
    :type old: const struct cred \*

    :param effective:
        A pointer to the proposed new effective capabilities set
    :type effective: const kernel_cap_t \*

    :param inheritable:
        A pointer to the proposed new inheritable capabilities set
    :type inheritable: const kernel_cap_t \*

    :param permitted:
        A pointer to the proposed new permitted capabilities set
    :type permitted: const kernel_cap_t \*

.. _`cap_capset.description`:

Description
-----------

This function validates and applies a proposed mass change to the current
process's capability sets.  The changes are made to the proposed new
credentials, and assuming no error, will be committed by the caller of LSM.

.. _`cap_inode_need_killpriv`:

cap_inode_need_killpriv
=======================

.. c:function:: int cap_inode_need_killpriv(struct dentry *dentry)

    Determine if inode change affects privileges

    :param dentry:
        The inode/dentry in being changed with change marked ATTR_KILL_PRIV
    :type dentry: struct dentry \*

.. _`cap_inode_need_killpriv.description`:

Description
-----------

Determine if an inode having a change applied that's marked ATTR_KILL_PRIV
affects the security markings on that inode, and if it is, should
\ :c:func:`inode_killpriv`\  be invoked or the change rejected.

Returns 1 if security.capability has a value, meaning \ :c:func:`inode_killpriv`\ 
is required, 0 otherwise, meaning \ :c:func:`inode_killpriv`\  is not required.

.. _`cap_inode_killpriv`:

cap_inode_killpriv
==================

.. c:function:: int cap_inode_killpriv(struct dentry *dentry)

    Erase the security markings on an inode

    :param dentry:
        The inode/dentry to alter
    :type dentry: struct dentry \*

.. _`cap_inode_killpriv.description`:

Description
-----------

Erase the privilege-enhancing security markings on an inode.

Returns 0 if successful, -ve on error.

.. _`cap_bprm_set_creds`:

cap_bprm_set_creds
==================

.. c:function:: int cap_bprm_set_creds(struct linux_binprm *bprm)

    Set up the proposed credentials for \ :c:func:`execve`\ .

    :param bprm:
        The execution parameters, including the proposed creds
    :type bprm: struct linux_binprm \*

.. _`cap_bprm_set_creds.description`:

Description
-----------

Set up the proposed credentials for a new execution context being
constructed by \ :c:func:`execve`\ .  The proposed creds in \ ``bprm->cred``\  is altered,
which won't take effect immediately.  Returns 0 if successful, -ve on error.

.. _`cap_inode_setxattr`:

cap_inode_setxattr
==================

.. c:function:: int cap_inode_setxattr(struct dentry *dentry, const char *name, const void *value, size_t size, int flags)

    Determine whether an xattr may be altered

    :param dentry:
        The inode/dentry being altered
    :type dentry: struct dentry \*

    :param name:
        The name of the xattr to be changed
    :type name: const char \*

    :param value:
        The value that the xattr will be changed to
    :type value: const void \*

    :param size:
        The size of value
    :type size: size_t

    :param flags:
        The replacement flag
    :type flags: int

.. _`cap_inode_setxattr.description`:

Description
-----------

Determine whether an xattr may be altered or set on an inode, returning 0 if
permission is granted, -ve if denied.

This is used to make sure security xattrs don't get updated or set by those
who aren't privileged to do so.

.. _`cap_inode_removexattr`:

cap_inode_removexattr
=====================

.. c:function:: int cap_inode_removexattr(struct dentry *dentry, const char *name)

    Determine whether an xattr may be removed

    :param dentry:
        The inode/dentry being altered
    :type dentry: struct dentry \*

    :param name:
        The name of the xattr to be changed
    :type name: const char \*

.. _`cap_inode_removexattr.description`:

Description
-----------

Determine whether an xattr may be removed from an inode, returning 0 if
permission is granted, -ve if denied.

This is used to make sure security xattrs don't get removed by those who
aren't privileged to remove them.

.. _`cap_task_fix_setuid`:

cap_task_fix_setuid
===================

.. c:function:: int cap_task_fix_setuid(struct cred *new, const struct cred *old, int flags)

    Fix up the results of \ :c:func:`setuid`\  call

    :param new:
        The proposed credentials
    :type new: struct cred \*

    :param old:
        The current task's current credentials
    :type old: const struct cred \*

    :param flags:
        Indications of what has changed
    :type flags: int

.. _`cap_task_fix_setuid.description`:

Description
-----------

Fix up the results of \ :c:func:`setuid`\  call before the credential changes are
actually applied, returning 0 to grant the changes, -ve to deny them.

.. _`cap_task_setscheduler`:

cap_task_setscheduler
=====================

.. c:function:: int cap_task_setscheduler(struct task_struct *p)

    Detemine if scheduler policy change is permitted

    :param p:
        The task to affect
    :type p: struct task_struct \*

.. _`cap_task_setscheduler.description`:

Description
-----------

Detemine if the requested scheduler policy change is permitted for the
specified task, returning 0 if permission is granted, -ve if denied.

.. _`cap_task_setioprio`:

cap_task_setioprio
==================

.. c:function:: int cap_task_setioprio(struct task_struct *p, int ioprio)

    Detemine if I/O priority change is permitted

    :param p:
        The task to affect
    :type p: struct task_struct \*

    :param ioprio:
        The I/O priority to set
    :type ioprio: int

.. _`cap_task_setioprio.description`:

Description
-----------

Detemine if the requested I/O priority change is permitted for the specified
task, returning 0 if permission is granted, -ve if denied.

.. _`cap_task_setnice`:

cap_task_setnice
================

.. c:function:: int cap_task_setnice(struct task_struct *p, int nice)

    Detemine if task priority change is permitted

    :param p:
        The task to affect
    :type p: struct task_struct \*

    :param nice:
        The nice value to set
    :type nice: int

.. _`cap_task_setnice.description`:

Description
-----------

Detemine if the requested task priority change is permitted for the
specified task, returning 0 if permission is granted, -ve if denied.

.. _`cap_task_prctl`:

cap_task_prctl
==============

.. c:function:: int cap_task_prctl(int option, unsigned long arg2, unsigned long arg3, unsigned long arg4, unsigned long arg5)

    Implement process control functions for this security module

    :param option:
        The process control function requested
    :type option: int

    :param arg2:
        The argument data for this function
    :type arg2: unsigned long

    :param arg3:
        *undescribed*
    :type arg3: unsigned long

    :param arg4:
        *undescribed*
    :type arg4: unsigned long

    :param arg5:
        *undescribed*
    :type arg5: unsigned long

.. _`cap_task_prctl.description`:

Description
-----------

Allow process control functions (sys_prctl()) to alter capabilities; may
also deny access to other functions not otherwise implemented here.

Returns 0 or +ve on success, -ENOSYS if this function is not implemented
here, other -ve on error.  If -ENOSYS is returned, \ :c:func:`sys_prctl`\  and other LSM
modules will consider performing the function.

.. _`cap_vm_enough_memory`:

cap_vm_enough_memory
====================

.. c:function:: int cap_vm_enough_memory(struct mm_struct *mm, long pages)

    Determine whether a new virtual mapping is permitted

    :param mm:
        The VM space in which the new mapping is to be made
    :type mm: struct mm_struct \*

    :param pages:
        The size of the mapping
    :type pages: long

.. _`cap_vm_enough_memory.description`:

Description
-----------

Determine whether the allocation of a new virtual mapping by the current
task is permitted, returning 1 if permission is granted, 0 if not.

.. This file was automatic generated / don't edit.

