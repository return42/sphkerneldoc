.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/auditsc.c

.. _`audit_alloc`:

audit_alloc
===========

.. c:function:: int audit_alloc(struct task_struct *tsk)

    allocate an audit context block for a task

    :param tsk:
        task
    :type tsk: struct task_struct \*

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

    :param tsk:
        task whose audit context block to free
    :type tsk: struct task_struct \*

.. _`__audit_free.description`:

Description
-----------

Called from copy_process and do_exit

.. _`__audit_syscall_entry`:

__audit_syscall_entry
=====================

.. c:function:: void __audit_syscall_entry(int major, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4)

    fill in an audit record at syscall entry

    :param major:
        major syscall type (function)
    :type major: int

    :param a1:
        additional syscall register 1
    :type a1: unsigned long

    :param a2:
        additional syscall register 2
    :type a2: unsigned long

    :param a3:
        additional syscall register 3
    :type a3: unsigned long

    :param a4:
        additional syscall register 4
    :type a4: unsigned long

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

    :param success:
        success value of the syscall
    :type success: int

    :param return_code:
        return value of the syscall
    :type return_code: long

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

    :param uptr:
        userland ptr to pathname
    :type uptr: const __user char \*

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

    :param name:
        name to add
    :type name: struct filename \*

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

    :param name:
        name being audited
    :type name: struct filename \*

    :param dentry:
        dentry being audited
    :type dentry: const struct dentry \*

    :param flags:
        attributes for this particular entry
    :type flags: unsigned int

.. _`__audit_inode_child`:

__audit_inode_child
===================

.. c:function:: void __audit_inode_child(struct inode *parent, const struct dentry *dentry, const unsigned char type)

    collect inode info for created/removed objects

    :param parent:
        inode of dentry parent
    :type parent: struct inode \*

    :param dentry:
        dentry being audited
    :type dentry: const struct dentry \*

    :param type:
        AUDIT_TYPE_* value that we're looking for
    :type type: const unsigned char

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

.. c:function:: int auditsc_get_stamp(struct audit_context *ctx, struct timespec64 *t, unsigned int *serial)

    get local copies of audit_context values

    :param ctx:
        audit_context for the task
    :type ctx: struct audit_context \*

    :param t:
        timespec64 to store time recorded in the audit_context
    :type t: struct timespec64 \*

    :param serial:
        serial value that is recorded in the audit_context
    :type serial: unsigned int \*

.. _`auditsc_get_stamp.description`:

Description
-----------

Also sets the context as auditable.

.. _`audit_set_loginuid`:

audit_set_loginuid
==================

.. c:function:: int audit_set_loginuid(kuid_t loginuid)

    set current task's audit_context loginuid

    :param loginuid:
        loginuid value
    :type loginuid: kuid_t

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

    :param oflag:
        open flag
    :type oflag: int

    :param mode:
        mode bits
    :type mode: umode_t

    :param attr:
        queue attributes
    :type attr: struct mq_attr \*

.. _`__audit_mq_sendrecv`:

__audit_mq_sendrecv
===================

.. c:function:: void __audit_mq_sendrecv(mqd_t mqdes, size_t msg_len, unsigned int msg_prio, const struct timespec64 *abs_timeout)

    record audit data for a POSIX MQ timed send/receive

    :param mqdes:
        MQ descriptor
    :type mqdes: mqd_t

    :param msg_len:
        Message length
    :type msg_len: size_t

    :param msg_prio:
        Message priority
    :type msg_prio: unsigned int

    :param abs_timeout:
        Message timeout in absolute time
    :type abs_timeout: const struct timespec64 \*

.. _`__audit_mq_notify`:

__audit_mq_notify
=================

.. c:function:: void __audit_mq_notify(mqd_t mqdes, const struct sigevent *notification)

    record audit data for a POSIX MQ notify

    :param mqdes:
        MQ descriptor
    :type mqdes: mqd_t

    :param notification:
        Notification event
    :type notification: const struct sigevent \*

.. _`__audit_mq_getsetattr`:

__audit_mq_getsetattr
=====================

.. c:function:: void __audit_mq_getsetattr(mqd_t mqdes, struct mq_attr *mqstat)

    record audit data for a POSIX MQ get/set attribute

    :param mqdes:
        MQ descriptor
    :type mqdes: mqd_t

    :param mqstat:
        MQ flags
    :type mqstat: struct mq_attr \*

.. _`__audit_ipc_obj`:

__audit_ipc_obj
===============

.. c:function:: void __audit_ipc_obj(struct kern_ipc_perm *ipcp)

    record audit data for ipc object

    :param ipcp:
        ipc permissions
    :type ipcp: struct kern_ipc_perm \*

.. _`__audit_ipc_set_perm`:

__audit_ipc_set_perm
====================

.. c:function:: void __audit_ipc_set_perm(unsigned long qbytes, uid_t uid, gid_t gid, umode_t mode)

    record audit data for new ipc permissions

    :param qbytes:
        msgq bytes
    :type qbytes: unsigned long

    :param uid:
        msgq user id
    :type uid: uid_t

    :param gid:
        msgq group id
    :type gid: gid_t

    :param mode:
        msgq mode (permissions)
    :type mode: umode_t

.. _`__audit_ipc_set_perm.description`:

Description
-----------

Called only after \ :c:func:`audit_ipc_obj`\ .

.. _`__audit_socketcall`:

__audit_socketcall
==================

.. c:function:: int __audit_socketcall(int nargs, unsigned long *args)

    record audit data for sys_socketcall

    :param nargs:
        number of args, which should not be more than AUDITSC_ARGS.
    :type nargs: int

    :param args:
        args array
    :type args: unsigned long \*

.. _`__audit_fd_pair`:

__audit_fd_pair
===============

.. c:function:: void __audit_fd_pair(int fd1, int fd2)

    record audit data for pipe and socketpair

    :param fd1:
        the first file descriptor
    :type fd1: int

    :param fd2:
        the second file descriptor
    :type fd2: int

.. _`__audit_sockaddr`:

__audit_sockaddr
================

.. c:function:: int __audit_sockaddr(int len, void *a)

    record audit data for sys_bind, sys_connect, sys_sendto

    :param len:
        data length in user space
    :type len: int

    :param a:
        data address in kernel space
    :type a: void \*

.. _`__audit_sockaddr.description`:

Description
-----------

Returns 0 for success or NULL context or < 0 on error.

.. _`audit_signal_info`:

audit_signal_info
=================

.. c:function:: int audit_signal_info(int sig, struct task_struct *t)

    record signal info for shutting down audit subsystem

    :param sig:
        signal value
    :type sig: int

    :param t:
        task being signaled
    :type t: struct task_struct \*

.. _`audit_signal_info.description`:

Description
-----------

If the audit subsystem is being terminated, record the task (pid)
and uid that is doing that.

.. _`__audit_log_bprm_fcaps`:

__audit_log_bprm_fcaps
======================

.. c:function:: int __audit_log_bprm_fcaps(struct linux_binprm *bprm, const struct cred *new, const struct cred *old)

    store information about a loading bprm and relevant fcaps

    :param bprm:
        pointer to the bprm being processed
    :type bprm: struct linux_binprm \*

    :param new:
        the proposed new credentials
    :type new: const struct cred \*

    :param old:
        the old credentials
    :type old: const struct cred \*

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

    :param new:
        the new credentials
    :type new: const struct cred \*

    :param old:
        the old (current) credentials
    :type old: const struct cred \*

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

    :param signr:
        signal value
    :type signr: long

.. _`audit_core_dumps.description`:

Description
-----------

If a process ends with a core dump, something fishy is going on and we
should record the event for investigation.

.. _`audit_seccomp`:

audit_seccomp
=============

.. c:function:: void audit_seccomp(unsigned long syscall, long signr, int code)

    record information about a seccomp action

    :param syscall:
        syscall number
    :type syscall: unsigned long

    :param signr:
        signal value
    :type signr: long

    :param code:
        the seccomp action
    :type code: int

.. _`audit_seccomp.description`:

Description
-----------

Record the information associated with a seccomp action. Event filtering for
seccomp actions that are not to be logged is done in \ :c:func:`seccomp_log`\ .
Therefore, this function forces auditing independent of the audit_enabled
and dummy context state because seccomp actions should be logged even when
audit is not in use.

.. This file was automatic generated / don't edit.

