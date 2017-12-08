.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ldlm/ldlm_flock.c

.. _`debug_subsystem`:

DEBUG_SUBSYSTEM
===============

.. c:function::  DEBUG_SUBSYSTEM()

    Its policy properties are start and end of extent and PID.

.. _`debug_subsystem.description`:

Description
-----------

These locks are only done through MDS due to POSIX semantics requiring
e.g. that locks could be only partially released and as such split into
two parts, and also that two adjacent locks from the same process may be
merged into a single wider lock.

.. _`debug_subsystem.lock-modes-are-mapped-like-this`:

Lock modes are mapped like this
-------------------------------

PR and PW for READ and WRITE locks
NL to request a releasing of a portion of the lock

These flock locks never timeout.

.. _`ldlm_process_flock_lock`:

ldlm_process_flock_lock
=======================

.. c:function:: int ldlm_process_flock_lock(struct ldlm_lock *req)

    Must be called under ns lock held.

    :param struct ldlm_lock \*req:
        *undescribed*

.. _`ldlm_process_flock_lock.description`:

Description
-----------

This function looks for any conflicts for \a lock in the granted or
waiting queues. The lock is granted if no conflicts are found in
either queue.

It is also responsible for splitting a lock if a portion of the lock
is released.

.. _`ldlm_flock_completion_ast`:

ldlm_flock_completion_ast
=========================

.. c:function:: int ldlm_flock_completion_ast(struct ldlm_lock *lock, __u64 flags, void *data)

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param __u64 flags:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`ldlm_flock_completion_ast.description`:

Description
-----------

\param lock [in,out]: A lock to be handled
\param flags    [in]: flags
\param \*data    [in]: \ :c:func:`ldlm_work_cp_ast_lock`\  will use ldlm_cb_set_arg

\retval 0    : success
\retval <0   : failure

.. This file was automatic generated / don't edit.

