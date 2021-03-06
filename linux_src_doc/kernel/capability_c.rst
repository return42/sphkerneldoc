.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/capability.c

.. _`sys_capget`:

sys_capget
==========

.. c:function:: long sys_capget(cap_user_header_t header, cap_user_data_t dataptr)

    get the capabilities of a given process.

    :param header:
        pointer to struct that contains capability version and
        target pid data
    :type header: cap_user_header_t

    :param dataptr:
        pointer to struct that contains the effective, permitted,
        and inheritable capabilities that are returned
    :type dataptr: cap_user_data_t

.. _`sys_capget.description`:

Description
-----------

Returns 0 on success and < 0 on error.

.. _`sys_capset`:

sys_capset
==========

.. c:function:: long sys_capset(cap_user_header_t header, const cap_user_data_t data)

    set capabilities for a process or (\*) a group of processes

    :param header:
        pointer to struct that contains capability version and
        target pid data
    :type header: cap_user_header_t

    :param data:
        pointer to struct that contains the effective, permitted,
        and inheritable capabilities
    :type data: const cap_user_data_t

.. _`sys_capset.description`:

Description
-----------

Set capabilities for the current process only.  The ability to any other
process(es) has been deprecated and removed.

.. _`sys_capset.the-restrictions-on-setting-capabilities-are-specified-as`:

The restrictions on setting capabilities are specified as
---------------------------------------------------------


I: any raised capabilities must be a subset of the old permitted
P: any raised capabilities must be a subset of the old permitted
E: must be set to a subset of new permitted

Returns 0 on success and < 0 on error.

.. _`has_ns_capability`:

has_ns_capability
=================

.. c:function:: bool has_ns_capability(struct task_struct *t, struct user_namespace *ns, int cap)

    Does a task have a capability in a specific user ns

    :param t:
        The task in question
    :type t: struct task_struct \*

    :param ns:
        target user namespace
    :type ns: struct user_namespace \*

    :param cap:
        The capability to be tested for
    :type cap: int

.. _`has_ns_capability.description`:

Description
-----------

Return true if the specified task has the given superior capability
currently in effect to the specified user namespace, false if not.

Note that this does not set PF_SUPERPRIV on the task.

.. _`has_capability`:

has_capability
==============

.. c:function:: bool has_capability(struct task_struct *t, int cap)

    Does a task have a capability in init_user_ns

    :param t:
        The task in question
    :type t: struct task_struct \*

    :param cap:
        The capability to be tested for
    :type cap: int

.. _`has_capability.description`:

Description
-----------

Return true if the specified task has the given superior capability
currently in effect to the initial user namespace, false if not.

Note that this does not set PF_SUPERPRIV on the task.

.. _`has_ns_capability_noaudit`:

has_ns_capability_noaudit
=========================

.. c:function:: bool has_ns_capability_noaudit(struct task_struct *t, struct user_namespace *ns, int cap)

    Does a task have a capability (unaudited) in a specific user ns.

    :param t:
        The task in question
    :type t: struct task_struct \*

    :param ns:
        target user namespace
    :type ns: struct user_namespace \*

    :param cap:
        The capability to be tested for
    :type cap: int

.. _`has_ns_capability_noaudit.description`:

Description
-----------

Return true if the specified task has the given superior capability
currently in effect to the specified user namespace, false if not.
Do not write an audit message for the check.

Note that this does not set PF_SUPERPRIV on the task.

.. _`has_capability_noaudit`:

has_capability_noaudit
======================

.. c:function:: bool has_capability_noaudit(struct task_struct *t, int cap)

    Does a task have a capability (unaudited) in the initial user ns

    :param t:
        The task in question
    :type t: struct task_struct \*

    :param cap:
        The capability to be tested for
    :type cap: int

.. _`has_capability_noaudit.description`:

Description
-----------

Return true if the specified task has the given superior capability
currently in effect to init_user_ns, false if not.  Don't write an
audit message for the check.

Note that this does not set PF_SUPERPRIV on the task.

.. _`ns_capable`:

ns_capable
==========

.. c:function:: bool ns_capable(struct user_namespace *ns, int cap)

    Determine if the current task has a superior capability in effect

    :param ns:
        The usernamespace we want the capability in
    :type ns: struct user_namespace \*

    :param cap:
        The capability to be tested for
    :type cap: int

.. _`ns_capable.description`:

Description
-----------

Return true if the current task has the given superior capability currently
available for use, false if not.

This sets PF_SUPERPRIV on the task if the capability is available on the
assumption that it's about to be used.

.. _`ns_capable_noaudit`:

ns_capable_noaudit
==================

.. c:function:: bool ns_capable_noaudit(struct user_namespace *ns, int cap)

    Determine if the current task has a superior capability (unaudited) in effect

    :param ns:
        The usernamespace we want the capability in
    :type ns: struct user_namespace \*

    :param cap:
        The capability to be tested for
    :type cap: int

.. _`ns_capable_noaudit.description`:

Description
-----------

Return true if the current task has the given superior capability currently
available for use, false if not.

This sets PF_SUPERPRIV on the task if the capability is available on the
assumption that it's about to be used.

.. _`capable`:

capable
=======

.. c:function:: bool capable(int cap)

    Determine if the current task has a superior capability in effect

    :param cap:
        The capability to be tested for
    :type cap: int

.. _`capable.description`:

Description
-----------

Return true if the current task has the given superior capability currently
available for use, false if not.

This sets PF_SUPERPRIV on the task if the capability is available on the
assumption that it's about to be used.

.. _`file_ns_capable`:

file_ns_capable
===============

.. c:function:: bool file_ns_capable(const struct file *file, struct user_namespace *ns, int cap)

    Determine if the file's opener had a capability in effect

    :param file:
        The file we want to check
    :type file: const struct file \*

    :param ns:
        The usernamespace we want the capability in
    :type ns: struct user_namespace \*

    :param cap:
        The capability to be tested for
    :type cap: int

.. _`file_ns_capable.description`:

Description
-----------

Return true if task that opened the file had a capability in effect
when the file was opened.

This does not set PF_SUPERPRIV because the caller may not
actually be privileged.

.. _`privileged_wrt_inode_uidgid`:

privileged_wrt_inode_uidgid
===========================

.. c:function:: bool privileged_wrt_inode_uidgid(struct user_namespace *ns, const struct inode *inode)

    Do capabilities in the namespace work over the inode?

    :param ns:
        The user namespace in question
    :type ns: struct user_namespace \*

    :param inode:
        The inode in question
    :type inode: const struct inode \*

.. _`privileged_wrt_inode_uidgid.description`:

Description
-----------

Return true if the inode uid and gid are within the namespace.

.. _`capable_wrt_inode_uidgid`:

capable_wrt_inode_uidgid
========================

.. c:function:: bool capable_wrt_inode_uidgid(const struct inode *inode, int cap)

    Check nsown_capable and uid and gid mapped

    :param inode:
        The inode in question
    :type inode: const struct inode \*

    :param cap:
        The capability in question
    :type cap: int

.. _`capable_wrt_inode_uidgid.description`:

Description
-----------

Return true if the current task has the given capability targeted at
its own user namespace and that the given inode's uid and gid are
mapped into the current user namespace.

.. _`ptracer_capable`:

ptracer_capable
===============

.. c:function:: bool ptracer_capable(struct task_struct *tsk, struct user_namespace *ns)

    Determine if the ptracer holds CAP_SYS_PTRACE in the namespace

    :param tsk:
        The task that may be ptraced
    :type tsk: struct task_struct \*

    :param ns:
        The user namespace to search for CAP_SYS_PTRACE in
    :type ns: struct user_namespace \*

.. _`ptracer_capable.description`:

Description
-----------

Return true if the task that is ptracing the current task had CAP_SYS_PTRACE
in the specified user namespace.

.. This file was automatic generated / don't edit.

