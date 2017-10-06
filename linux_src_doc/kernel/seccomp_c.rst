.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/seccomp.c

.. _`seccomp_filter`:

struct seccomp_filter
=====================

.. c:type:: struct seccomp_filter

    container for seccomp BPF programs

.. _`seccomp_filter.definition`:

Definition
----------

.. code-block:: c

    struct seccomp_filter {
        refcount_t usage;
        bool log;
        struct seccomp_filter *prev;
        struct bpf_prog *prog;
    }

.. _`seccomp_filter.members`:

Members
-------

usage
    reference count to manage the object lifetime.
    get/put helpers should be used when accessing an instance
    outside of a lifetime-guarded section.  In general, this
    is only needed for handling filters shared across tasks.

log
    true if all actions except for SECCOMP_RET_ALLOW should be logged

prev
    points to a previously installed, or inherited, filter

prog
    the BPF program to evaluate

.. _`seccomp_filter.description`:

Description
-----------

seccomp_filter objects are organized in a tree linked via the \ ``prev``\ 
pointer.  For any task, it appears to be a singly-linked list starting
with current->seccomp.filter, the most recently attached or inherited filter.
However, multiple filters may share a \ ``prev``\  node, by way of \ :c:func:`fork`\ , which
results in a unidirectional tree existing in memory.  This is similar to
how namespaces work.

seccomp_filter objects should never be modified after being attached
to a task_struct (other than \ ``usage``\ ).

.. _`seccomp_check_filter`:

seccomp_check_filter
====================

.. c:function:: int seccomp_check_filter(struct sock_filter *filter, unsigned int flen)

    verify seccomp filter code

    :param struct sock_filter \*filter:
        filter to verify

    :param unsigned int flen:
        length of filter

.. _`seccomp_check_filter.description`:

Description
-----------

Takes a previously checked filter (by bpf_check_classic) and
redirects all filter code that loads struct sk_buff data
and related data through seccomp_bpf_load.  It also
enforces length and alignment checking of those loads.

Returns 0 if the rule set is legal or -EINVAL if not.

.. _`action_only`:

ACTION_ONLY
===========

.. c:function::  ACTION_ONLY( ret)

    evaluates all seccomp filters against \ ``sd``\ 

    :param  ret:
        *undescribed*

.. _`action_only.description`:

Description
-----------

Returns valid seccomp BPF response codes.

.. _`seccomp_can_sync_threads`:

seccomp_can_sync_threads
========================

.. c:function:: pid_t seccomp_can_sync_threads( void)

    checks if all threads can be synchronized

    :param  void:
        no arguments

.. _`seccomp_can_sync_threads.description`:

Description
-----------

Expects sighand and cred_guard_mutex locks to be held.

Returns 0 on success, -ve on error, or the pid of a thread which was
either not in the correct seccomp mode or it did not have an ancestral
seccomp filter.

.. _`seccomp_sync_threads`:

seccomp_sync_threads
====================

.. c:function:: void seccomp_sync_threads( void)

    sets all threads to use current's filter

    :param  void:
        no arguments

.. _`seccomp_sync_threads.description`:

Description
-----------

Expects sighand and cred_guard_mutex locks to be held, and for
\ :c:func:`seccomp_can_sync_threads`\  to have returned success already
without dropping the locks.

.. _`seccomp_prepare_filter`:

seccomp_prepare_filter
======================

.. c:function:: struct seccomp_filter *seccomp_prepare_filter(struct sock_fprog *fprog)

    Prepares a seccomp filter for use.

    :param struct sock_fprog \*fprog:
        BPF program to install

.. _`seccomp_prepare_filter.description`:

Description
-----------

Returns filter on success or an ERR_PTR on failure.

.. _`seccomp_prepare_user_filter`:

seccomp_prepare_user_filter
===========================

.. c:function:: struct seccomp_filter *seccomp_prepare_user_filter(const char __user *user_filter)

    prepares a user-supplied sock_fprog

    :param const char __user \*user_filter:
        pointer to the user data containing a sock_fprog.

.. _`seccomp_prepare_user_filter.description`:

Description
-----------

Returns 0 on success and non-zero otherwise.

.. _`seccomp_attach_filter`:

seccomp_attach_filter
=====================

.. c:function:: long seccomp_attach_filter(unsigned int flags, struct seccomp_filter *filter)

    validate and attach filter

    :param unsigned int flags:
        flags to change filter behavior

    :param struct seccomp_filter \*filter:
        seccomp filter to add to the current process

.. _`seccomp_attach_filter.description`:

Description
-----------

Caller must be holding current->sighand->siglock lock.

Returns 0 on success, -ve on error.

.. _`seccomp_send_sigsys`:

seccomp_send_sigsys
===================

.. c:function:: void seccomp_send_sigsys(int syscall, int reason)

    signals the task to allow in-process syscall emulation

    :param int syscall:
        syscall number to send to userland

    :param int reason:
        filter-supplied reason code to send to userland (via si_errno)

.. _`seccomp_send_sigsys.description`:

Description
-----------

Forces a SIGSYS with a code of SYS_SECCOMP and related sigsys info.

.. _`seccomp_set_mode_strict`:

seccomp_set_mode_strict
=======================

.. c:function:: long seccomp_set_mode_strict( void)

    internal function for setting strict seccomp

    :param  void:
        no arguments

.. _`seccomp_set_mode_strict.description`:

Description
-----------

Once current->seccomp.mode is non-zero, it may not be changed.

Returns 0 on success or -EINVAL on failure.

.. _`seccomp_set_mode_filter`:

seccomp_set_mode_filter
=======================

.. c:function:: long seccomp_set_mode_filter(unsigned int flags, const char __user *filter)

    internal function for setting seccomp filter

    :param unsigned int flags:
        flags to change filter behavior

    :param const char __user \*filter:
        struct sock_fprog containing filter

.. _`seccomp_set_mode_filter.description`:

Description
-----------

This function may be called repeatedly to install additional filters.
Every filter successfully installed will be evaluated (in reverse order)
for each system call the task makes.

Once current->seccomp.mode is non-zero, it may not be changed.

Returns 0 on success or -EINVAL on failure.

.. _`prctl_set_seccomp`:

prctl_set_seccomp
=================

.. c:function:: long prctl_set_seccomp(unsigned long seccomp_mode, char __user *filter)

    configures current->seccomp.mode

    :param unsigned long seccomp_mode:
        requested mode to use

    :param char __user \*filter:
        optional struct sock_fprog for use with SECCOMP_MODE_FILTER

.. _`prctl_set_seccomp.description`:

Description
-----------

Returns 0 on success or -EINVAL on failure.

.. This file was automatic generated / don't edit.

