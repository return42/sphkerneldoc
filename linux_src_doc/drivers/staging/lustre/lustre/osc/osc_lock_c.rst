.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/osc/osc_lock.c

.. _`osc_handle_ptr`:

osc_handle_ptr
==============

.. c:function:: struct ldlm_lock *osc_handle_ptr(struct lustre_handle *handle)

    pointer cannot be dereferenced, as lock is not protected from concurrent reclaim. This function is a helper for \ :c:func:`osc_lock_invariant`\ .

    :param struct lustre_handle \*handle:
        *undescribed*

.. _`osc_lock_invariant`:

osc_lock_invariant
==================

.. c:function:: int osc_lock_invariant(struct osc_lock *ols)

    :param struct osc_lock \*ols:
        *undescribed*

.. _`osc_lock_lvb_update`:

osc_lock_lvb_update
===================

.. c:function:: void osc_lock_lvb_update(const struct lu_env *env, struct osc_object *osc, struct ldlm_lock *dlmlock, struct ost_lvb *lvb)

    with the DLM lock reply from the server. Copy of \ :c:func:`osc_update_enqueue`\  logic.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_object \*osc:
        *undescribed*

    :param struct ldlm_lock \*dlmlock:
        *undescribed*

    :param struct ost_lvb \*lvb:
        *undescribed*

.. _`osc_lock_lvb_update.description`:

Description
-----------

This can be optimized to not update attributes when lock is a result of a
local match.

Called under lock and resource spin-locks.

.. _`osc_lock_upcall`:

osc_lock_upcall
===============

.. c:function:: int osc_lock_upcall(void *cookie, struct lustre_handle *lockh, int errcode)

    received from a server, or after \ :c:func:`osc_enqueue_base`\  matched a local DLM lock.

    :param void \*cookie:
        *undescribed*

    :param struct lustre_handle \*lockh:
        *undescribed*

    :param int errcode:
        *undescribed*

.. _`osc_dlm_blocking_ast0`:

osc_dlm_blocking_ast0
=====================

.. c:function:: int osc_dlm_blocking_ast0(const struct lu_env *env, struct ldlm_lock *dlmlock, void *data, int flag)

    and ldlm_lock caches.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct ldlm_lock \*dlmlock:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param int flag:
        *undescribed*

.. _`osc_ldlm_blocking_ast`:

osc_ldlm_blocking_ast
=====================

.. c:function:: int osc_ldlm_blocking_ast(struct ldlm_lock *dlmlock, struct ldlm_lock_desc *new, void *data, int flag)

    some other lock, or is canceled. This function is installed as a ldlm_lock::l_blocking_ast() for client extent locks.

    :param struct ldlm_lock \*dlmlock:
        *undescribed*

    :param struct ldlm_lock_desc \*new:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param int flag:
        *undescribed*

.. _`osc_ldlm_blocking_ast.description`:

Description
-----------

Control flow is tricky, because ldlm uses the same call-back
(ldlm_lock::l_blocking_ast()) for both blocking and cancellation ast's.

\param dlmlock lock for which ast occurred.

\param new description of a conflicting lock in case of blocking ast.

\param data value of dlmlock->l_ast_data

\param flag LDLM_CB_BLOCKING or LDLM_CB_CANCELING. Used to distinguish
cancellation and blocking ast's.

.. _`osc_ldlm_blocking_ast.possible-use-cases`:

Possible use cases
------------------


- ldlm calls dlmlock->l_blocking_ast(..., LDLM_CB_CANCELING) to cancel
lock due to lock lru pressure, or explicit user request to purge
locks.

- ldlm calls dlmlock->l_blocking_ast(..., LDLM_CB_BLOCKING) to notify
us that dlmlock conflicts with another lock that some client is
enqueing. Lock is canceled.

- \ :c:func:`cl_lock_cancel`\  is called. \ :c:func:`osc_lock_cancel`\  calls
\ :c:func:`ldlm_cli_cancel`\  that calls

dlmlock->l_blocking_ast(..., LDLM_CB_CANCELING)

recursively entering \ :c:func:`osc_ldlm_blocking_ast`\ .

- client cancels lock voluntary (e.g., as a part of early cancellation):

\ :c:func:`cl_lock_cancel`\ ->
\ :c:func:`osc_lock_cancel`\ ->
\ :c:func:`ldlm_cli_cancel`\ ->
dlmlock->l_blocking_ast(..., LDLM_CB_CANCELING)

.. _`osc_ldlm_weigh_ast`:

osc_ldlm_weigh_ast
==================

.. c:function:: unsigned long osc_ldlm_weigh_ast(struct ldlm_lock *dlmlock)

    :param struct ldlm_lock \*dlmlock:
        *undescribed*

.. _`osc_lock_to_lockless`:

osc_lock_to_lockless
====================

.. c:function:: void osc_lock_to_lockless(const struct lu_env *env, struct osc_lock *ols, int force)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_lock \*ols:
        *undescribed*

    :param int force:
        *undescribed*

.. _`osc_lock_to_lockless.steps-to-check`:

Steps to check
--------------

- if the lock has an explicit requirement for a non-lockless lock;
- if the io lock request type ci_lockreq;
- send the enqueue rpc to ost to make the further decision;
- special treat to truncate lockless lock

Additional policy can be implemented here, e.g., never do lockless-io
for large extents.

.. _`osc_lock_enqueue`:

osc_lock_enqueue
================

.. c:function:: int osc_lock_enqueue(const struct lu_env *env, const struct cl_lock_slice *slice, struct cl_io *unused, struct cl_sync_io *anchor)

    :clo_enqueue() method for osc layer. This initiates ldlm enqueue:

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_lock_slice \*slice:
        *undescribed*

    :param struct cl_io \*unused:
        *undescribed*

    :param struct cl_sync_io \*anchor:
        *undescribed*

.. _`osc_lock_enqueue.description`:

Description
-----------

- cancels conflicting locks early (osc_lock_enqueue_wait());

- calls \ :c:func:`osc_enqueue_base`\  to do actual enqueue.

\ :c:func:`osc_enqueue_base`\  is supplied with an upcall function that is executed
when lock is received either after a local cached ldlm lock is matched, or
when a reply from the server is received.

This function does not wait for the network communication to complete.

.. _`osc_lock_detach`:

osc_lock_detach
===============

.. c:function:: void osc_lock_detach(const struct lu_env *env, struct osc_lock *olck)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_lock \*olck:
        *undescribed*

.. _`osc_lock_cancel`:

osc_lock_cancel
===============

.. c:function:: void osc_lock_cancel(const struct lu_env *env, const struct cl_lock_slice *slice)

    :clo_cancel() method for osc layer. This is called (as part of \ :c:func:`cl_lock_cancel`\ ) when lock is canceled either voluntary (LRU pressure, early cancellation, umount, etc.) or due to the conflict with some other lock some where in the cluster. This function does the

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_lock_slice \*slice:
        *undescribed*

.. _`osc_lock_cancel.following`:

following
---------


- invalidates all pages protected by this lock (after sending dirty
ones to the server, as necessary);

- decref's underlying ldlm lock;

- cancels ldlm lock (ldlm_cli_cancel()).

.. _`osc_dlmlock_at_pgoff`:

osc_dlmlock_at_pgoff
====================

.. c:function:: struct ldlm_lock *osc_dlmlock_at_pgoff(const struct lu_env *env, struct osc_object *obj, pgoff_t index, int pending, int canceling)

    given \a except lock.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_object \*obj:
        *undescribed*

    :param pgoff_t index:
        *undescribed*

    :param int pending:
        *undescribed*

    :param int canceling:
        *undescribed*

.. This file was automatic generated / don't edit.

