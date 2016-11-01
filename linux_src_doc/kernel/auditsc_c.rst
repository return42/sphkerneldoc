.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/auditsc.c

.. _`audit_alloc`:

audit_alloc
===========

.. c:function:: int audit_alloc(struct task_struct *tsk)

    allocate an audit context block for a task

    :param struct task_struct \*tsk:
        task

.. _`audit_alloc.description`:

Description
-----------

Filter on the task information and allocate a per-task audit context
if necessary.  Doing so turns on system call auditing for the
specified task.  This is called from copy_process, so no lock is
needed.

.. _`__audit_free`:

__audit_free
============

.. c:function:: void __audit_free(struct task_struct *tsk)

    free a per-task audit context

    :param struct task_struct \*tsk:
        task whose audit context block to free

.. _`__audit_free.description`:

Description
-----------

Called from copy_process and do_exit

.. _`__audit_syscall_entry`:

__audit_syscall_entry
=====================

.. c:function:: void __audit_syscall_entry(int major, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4)

    fill in an audit record at syscall entry

    :param int major:
        major syscall type (function)

    :param unsigned long a1:
        additional syscall register 1

    :param unsigned long a2:
        additional syscall register 2

    :param unsigned long a3:
        additional syscall register 3

    :param unsigned long a4:
        additional syscall register 4

.. _`__audit_syscall_entry.description`:

Description
-----------

Fill in audit context at syscall entry.  This only happens if the
audit context was created when the task was created and the state or
filters demand the audit context be built.  If the state from the
per-task filter or from the per-syscall filter is AUDIT_RECORD_CONTEXT,
then the record will be written at syscall exit time (otherwise, it
will only be written if another part of the kernel requests that it
be written).

.. _`__audit_syscall_exit`:

__audit_syscall_exit
====================

.. c:function:: void __audit_syscall_exit(int success, long return_code)

    deallocate audit context after a system call

    :param int success:
        success value of the syscall

    :param long return_code:
        return value of the syscall

.. _`__audit_syscall_exit.description`:

Description
-----------

Tear down after system call.  If the audit context has been marked as
auditable (either because of the AUDIT_RECORD_CONTEXT state from
filtering, or because some other part of the kernel wrote an audit
message), then write out the syscall information.  In call cases,
free the names stored from \ :c:func:`getname`\ .

.. _`__audit_reusename`:

__audit_reusename
=================

.. c:function:: struct filename *__audit_reusename(const __user char *uptr)

    fill out filename with info from existing entry

    :param const __user char \*uptr:
        userland ptr to pathname

.. _`__audit_reusename.description`:

Description
-----------

Search the audit_names list for the current audit context. If there is an
existing entry with a matching "uptr" then return the filename
associated with that audit_name. If not, return NULL.

.. _`__audit_getname`:

__audit_getname
===============

.. c:function:: void __audit_getname(struct filename *name)

    add a name to the list

    :param struct filename \*name:
        name to add

.. _`__audit_getname.description`:

Description
-----------

Add a name to the list of audit names for this context.
Called from fs/namei.c:getname().

.. _`__audit_inode`:

__audit_inode
=============

.. c:function:: void __audit_inode(struct filename *name, const struct dentry *dentry, unsigned int flags)

    store the inode and device from a lookup

    :param struct filename \*name:
        name being audited

    :param const struct dentry \*dentry:
        dentry being audited

    :param unsigned int flags:
        attributes for this particular entry

.. _`__audit_inode_child`:

__audit_inode_child
===================

.. c:function:: void __audit_inode_child(struct inode *parent, const struct dentry *dentry, const unsigned char type)

    collect inode info for created/removed objects

    :param struct inode \*parent:
        inode of dentry parent

    :param const struct dentry \*dentry:
        dentry being audited

    :param const unsigned char type:
        AUDIT_TYPE\_\* value that we're looking for

.. _`__audit_inode_child.description`:

Description
-----------

For syscalls that create or remove filesystem objects, audit_inode
can only collect information for the filesystem object's parent.
This call updates the audit context with the child's information.
Syscalls that create a new filesystem object must be hooked after
the object is created.  Syscalls that remove a filesystem object
must be hooked prior, in order to capture the target inode during
unsuccessful attempts.

.. _`auditsc_get_stamp`:

auditsc_get_stamp
=================

.. c:function:: int auditsc_get_stamp(struct audit_context *ctx, struct timespec *t, unsigned int *serial)

    get local copies of audit_context values

    :param struct audit_context \*ctx:
        audit_context for the task

    :param struct timespec \*t:
        timespec to store time recorded in the audit_context

    :param unsigned int \*serial:
        serial value that is recorded in the audit_context

.. _`auditsc_get_stamp.description`:

Description
-----------

Also sets the context as auditable.

.. _`audit_set_loginuid`:

audit_set_loginuid
==================

.. c:function:: int audit_set_loginuid(kuid_t loginuid)

    set current task's audit_context loginuid

    :param kuid_t loginuid:
        loginuid value

.. _`audit_set_loginuid.description`:

Description
-----------

Returns 0.

Called (set) from fs/proc/base.c::proc_loginuid_write().

.. _`__audit_mq_open`:

__audit_mq_open
===============

.. c:function:: void __audit_mq_open(int oflag, umode_t mode, struct mq_attr *attr)

    record audit data for a POSIX MQ open

    :param int oflag:
        open flag

    :param umode_t mode:
        mode bits

    :param struct mq_attr \*attr:
        queue attributes

.. _`__audit_mq_sendrecv`:

__audit_mq_sendrecv
===================

.. c:function:: void __audit_mq_sendrecv(mqd_t mqdes, size_t msg_len, unsigned int msg_prio, const struct timespec *abs_timeout)

    record audit data for a POSIX MQ timed send/receive

    :param mqd_t mqdes:
        MQ descriptor

    :param size_t msg_len:
        Message length

    :param unsigned int msg_prio:
        Message priority

    :param const struct timespec \*abs_timeout:
        Message timeout in absolute time

.. _`__audit_mq_notify`:

__audit_mq_notify
=================

.. c:function:: void __audit_mq_notify(mqd_t mqdes, const struct sigevent *notification)

    record audit data for a POSIX MQ notify

    :param mqd_t mqdes:
        MQ descriptor

    :param const struct sigevent \*notification:
        Notification event

.. _`__audit_mq_getsetattr`:

__audit_mq_getsetattr
=====================

.. c:function:: void __audit_mq_getsetattr(mqd_t mqdes, struct mq_attr *mqstat)

    record audit data for a POSIX MQ get/set attribute

    :param mqd_t mqdes:
        MQ descriptor

    :param struct mq_attr \*mqstat:
        MQ flags

.. _`__audit_ipc_obj`:

__audit_ipc_obj
===============

.. c:function:: void __audit_ipc_obj(struct kern_ipc_perm *ipcp)

    record audit data for ipc object

    :param struct kern_ipc_perm \*ipcp:
        ipc permissions

.. _`__audit_ipc_set_perm`:

__audit_ipc_set_perm
====================

.. c:function:: void __audit_ipc_set_perm(unsigned long qbytes, uid_t uid, gid_t gid, umode_t mode)

    record audit data for new ipc permissions

    :param unsigned long qbytes:
        msgq bytes

    :param uid_t uid:
        msgq user id

    :param gid_t gid:
        msgq group id

    :param umode_t mode:
        msgq mode (permissions)

.. _`__audit_ipc_set_perm.description`:

Description
-----------

Called only after \ :c:func:`audit_ipc_obj`\ .

.. _`__audit_socketcall`:

__audit_socketcall
==================

.. c:function:: int __audit_socketcall(int nargs, unsigned long *args)

    record audit data for sys_socketcall

    :param int nargs:
        number of args, which should not be more than AUDITSC_ARGS.

    :param unsigned long \*args:
        args array

.. _`__audit_fd_pair`:

__audit_fd_pair
===============

.. c:function:: void __audit_fd_pair(int fd1, int fd2)

    record audit data for pipe and socketpair

    :param int fd1:
        the first file descriptor

    :param int fd2:
        the second file descriptor

.. _`__audit_sockaddr`:

__audit_sockaddr
================

.. c:function:: int __audit_sockaddr(int len, void *a)

    record audit data for sys_bind, sys_connect, sys_sendto

    :param int len:
        data length in user space

    :param void \*a:
        data address in kernel space

.. _`__audit_sockaddr.description`:

Description
-----------

Returns 0 for success or NULL context or < 0 on error.

.. _`__audit_signal_info`:

__audit_signal_info
===================

.. c:function:: int __audit_signal_info(int sig, struct task_struct *t)

    record signal info for shutting down audit subsystem

    :param int sig:
        signal value

    :param struct task_struct \*t:
        task being signaled

.. _`__audit_signal_info.description`:

Description
-----------

If the audit subsystem is being terminated, record the task (pid)
and uid that is doing that.

.. _`__audit_log_bprm_fcaps`:

__audit_log_bprm_fcaps
======================

.. c:function:: int __audit_log_bprm_fcaps(struct linux_binprm *bprm, const struct cred *new, const struct cred *old)

    store information about a loading bprm and relevant fcaps

    :param struct linux_binprm \*bprm:
        pointer to the bprm being processed

    :param const struct cred \*new:
        the proposed new credentials

    :param const struct cred \*old:
        the old credentials

.. _`__audit_log_bprm_fcaps.description`:

Description
-----------

Simply check if the proc already has the caps given by the file and if not
store the priv escalation info for later auditing at the end of the syscall

-Eric

.. _`__audit_log_capset`:

__audit_log_capset
==================

.. c:function:: void __audit_log_capset(const struct cred *new, const struct cred *old)

    store information about the arguments to the capset syscall

    :param const struct cred \*new:
        the new credentials

    :param const struct cred \*old:
        the old (current) credentials

.. _`__audit_log_capset.description`:

Description
-----------

Record the arguments userspace sent to sys_capset for later printing by the
audit system if applicable

.. _`audit_core_dumps`:

audit_core_dumps
================

.. c:function:: void audit_core_dumps(long signr)

    record information about processes that end abnormally

    :param long signr:
        signal value

.. _`audit_core_dumps.description`:

Description
-----------

If a process ends with a core dump, something fishy is going on and we
should record the event for investigation.

.. This file was automatic generated / don't edit.

