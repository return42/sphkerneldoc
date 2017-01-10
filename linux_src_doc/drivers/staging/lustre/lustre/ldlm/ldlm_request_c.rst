.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ldlm/ldlm_request.c

.. _`debug_subsystem`:

DEBUG_SUBSYSTEM
===============

.. c:function::  DEBUG_SUBSYSTEM()

    LDLM request-processing routines.

.. _`debug_subsystem.description`:

Description
-----------

An AST is a callback issued on a lock when its state is changed. There are
several different types of ASTs (callbacks) registered for each lock:

- completion AST: when a lock is enqueued by some process, but cannot be
granted immediately due to other conflicting locks on the same resource,
the completion AST is sent to notify the caller when the lock is
eventually granted

- blocking AST: when a lock is granted to some process, if another process
enqueues a conflicting (blocking) lock on a resource, a blocking AST is
sent to notify the holder(s) of the lock(s) of the conflicting lock
request. The lock holder(s) must release their lock(s) on that resource in
a timely manner or be evicted by the server.

- glimpse AST: this is used when a process wants information about a lock
(i.e. the lock value block (LVB)) but does not necessarily require holding
the lock. If the resource is locked, the lock holder(s) are sent glimpse
ASTs and the LVB is returned to the caller, and lock holder(s) may CANCEL
their lock(s) if they are idle. If the resource is not locked, the server
may grant the lock.

.. _`ldlm_cp_timeout`:

ldlm_cp_timeout
===============

.. c:function:: unsigned int ldlm_cp_timeout(struct ldlm_lock *lock)

    lock cancel, and their replies). Used for lock completion timeout on the client side.

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_cp_timeout.description`:

Description
-----------

\param[in] lock      lock which is waiting the completion callback

\retval              timeout in seconds to wait for the server reply

.. _`ldlm_completion_tail`:

ldlm_completion_tail
====================

.. c:function:: int ldlm_completion_tail(struct ldlm_lock *lock, void *data)

    actually granted.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`ldlm_completion_ast_async`:

ldlm_completion_ast_async
=========================

.. c:function:: int ldlm_completion_ast_async(struct ldlm_lock *lock, __u64 flags, void *data)

    >l_completion_ast() for a client, that doesn't wait until lock is granted. Suitable for locks enqueued through ptlrpcd, of other threads that cannot block for long.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param __u64 flags:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`ldlm_completion_ast`:

ldlm_completion_ast
===================

.. c:function:: int ldlm_completion_ast(struct ldlm_lock *lock, __u64 flags, void *data)

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param __u64 flags:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`ldlm_completion_ast.description`:

Description
-----------

- when a reply to an ENQUEUE RPC is received from the server
(ldlm_cli_enqueue_fini()). Lock might be granted or not granted at
this point (determined by flags);

- when LDLM_CP_CALLBACK RPC comes to client to notify it that lock has
been granted;

- when ldlm_lock_match(LDLM_FL_LVB_READY) is about to wait until lock
gets correct lvb;

- to force all locks when resource is destroyed (cleanup_resource());

- during lock conversion (not used currently).

If lock is not granted in the first case, this function waits until second
or penultimate cases happen in some other thread.

.. _`ldlm_cli_enqueue_fini`:

ldlm_cli_enqueue_fini
=====================

.. c:function:: int ldlm_cli_enqueue_fini(struct obd_export *exp, struct ptlrpc_request *req, enum ldlm_type type, __u8 with_policy, enum ldlm_mode mode, __u64 *flags, void *lvb, __u32 lvb_len, const struct lustre_handle *lockh, int rc)

    :param struct obd_export \*exp:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param enum ldlm_type type:
        *undescribed*

    :param __u8 with_policy:
        *undescribed*

    :param enum ldlm_mode mode:
        *undescribed*

    :param __u64 \*flags:
        *undescribed*

    :param void \*lvb:
        *undescribed*

    :param __u32 lvb_len:
        *undescribed*

    :param const struct lustre_handle \*lockh:
        *undescribed*

    :param int rc:
        *undescribed*

.. _`ldlm_cli_enqueue_fini.description`:

Description
-----------

Called after receiving reply from server.

.. _`ldlm_req_handles_avail`:

ldlm_req_handles_avail
======================

.. c:function:: int ldlm_req_handles_avail(int req_size, int off)

    size.  PAGE_SIZE-512 is to allow TCP/IP and LNET headers to fit into a single page on the send/receive side. XXX: 512 should be changed to more adequate value.

    :param int req_size:
        *undescribed*

    :param int off:
        *undescribed*

.. _`ldlm_prep_elc_req`:

ldlm_prep_elc_req
=================

.. c:function:: int ldlm_prep_elc_req(struct obd_export *exp, struct ptlrpc_request *req, int version, int opc, int canceloff, struct list_head *cancels, int count)

    \a count locks in \a cancels.

    :param struct obd_export \*exp:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param int version:
        *undescribed*

    :param int opc:
        *undescribed*

    :param int canceloff:
        *undescribed*

    :param struct list_head \*cancels:
        *undescribed*

    :param int count:
        *undescribed*

.. _`ldlm_prep_elc_req.description`:

Description
-----------

This is to be called by functions preparing their own requests that
might contain lists of locks to cancel in addition to actual operation
that needs to be performed.

.. _`ldlm_cli_enqueue`:

ldlm_cli_enqueue
================

.. c:function:: int ldlm_cli_enqueue(struct obd_export *exp, struct ptlrpc_request **reqp, struct ldlm_enqueue_info *einfo, const struct ldlm_res_id *res_id, union ldlm_policy_data const *policy, __u64 *flags, void *lvb, __u32 lvb_len, enum lvb_type lvb_type, struct lustre_handle *lockh, int async)

    side lock enqueue.

    :param struct obd_export \*exp:
        *undescribed*

    :param struct ptlrpc_request \*\*reqp:
        *undescribed*

    :param struct ldlm_enqueue_info \*einfo:
        *undescribed*

    :param const struct ldlm_res_id \*res_id:
        *undescribed*

    :param union ldlm_policy_data const \*policy:
        *undescribed*

    :param __u64 \*flags:
        *undescribed*

    :param void \*lvb:
        *undescribed*

    :param __u32 lvb_len:
        *undescribed*

    :param enum lvb_type lvb_type:
        *undescribed*

    :param struct lustre_handle \*lockh:
        *undescribed*

    :param int async:
        *undescribed*

.. _`ldlm_cli_enqueue.description`:

Description
-----------

If a request has some specific initialisation it is passed in \a reqp,
otherwise it is created in ldlm_cli_enqueue.

Supports sync and async requests, pass \a async flag accordingly. If a
request was created in ldlm_cli_enqueue and it is the async request,
pass it to the caller in \a reqp.

.. _`ldlm_cli_cancel_local`:

ldlm_cli_cancel_local
=====================

.. c:function:: __u64 ldlm_cli_cancel_local(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_cli_cancel_local.return`:

Return
------

\retval LDLM_FL_LOCAL_ONLY if there is no need for a CANCEL RPC to the server
\retval LDLM_FL_CANCELING otherwise;
\retval LDLM_FL_BL_AST if there is a need for a separate CANCEL RPC.

.. _`ldlm_cancel_pack`:

ldlm_cancel_pack
================

.. c:function:: void ldlm_cancel_pack(struct ptlrpc_request *req, struct list_head *head, int count)

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param struct list_head \*head:
        *undescribed*

    :param int count:
        *undescribed*

.. _`ldlm_cli_cancel_req`:

ldlm_cli_cancel_req
===================

.. c:function:: int ldlm_cli_cancel_req(struct obd_export *exp, struct list_head *cancels, int count, enum ldlm_cancel_flags flags)

    handles of locks given in \a cancels list.

    :param struct obd_export \*exp:
        *undescribed*

    :param struct list_head \*cancels:
        *undescribed*

    :param int count:
        *undescribed*

    :param enum ldlm_cancel_flags flags:
        *undescribed*

.. _`ldlm_cli_update_pool`:

ldlm_cli_update_pool
====================

.. c:function:: int ldlm_cli_update_pool(struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ldlm_cli_cancel`:

ldlm_cli_cancel
===============

.. c:function:: int ldlm_cli_cancel(const struct lustre_handle *lockh, enum ldlm_cancel_flags cancel_flags)

    :param const struct lustre_handle \*lockh:
        *undescribed*

    :param enum ldlm_cancel_flags cancel_flags:
        *undescribed*

.. _`ldlm_cli_cancel.description`:

Description
-----------

Lock must not have any readers or writers by this time.

.. _`ldlm_cli_cancel_list_local`:

ldlm_cli_cancel_list_local
==========================

.. c:function:: int ldlm_cli_cancel_list_local(struct list_head *cancels, int count, enum ldlm_cancel_flags flags)

    Return the number of cancelled locks.

    :param struct list_head \*cancels:
        *undescribed*

    :param int count:
        *undescribed*

    :param enum ldlm_cancel_flags flags:
        *undescribed*

.. _`ldlm_cancel_no_wait_policy`:

ldlm_cancel_no_wait_policy
==========================

.. c:function:: enum ldlm_policy_res ldlm_cancel_no_wait_policy(struct ldlm_namespace *ns, struct ldlm_lock *lock, int unused, int added, int count)

    dirty data, to close a file, ...) or waiting for any RPCs in-flight (e.g. readahead requests, ...)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param int unused:
        *undescribed*

    :param int added:
        *undescribed*

    :param int count:
        *undescribed*

.. _`ldlm_cancel_lrur_policy`:

ldlm_cancel_lrur_policy
=======================

.. c:function:: enum ldlm_policy_res ldlm_cancel_lrur_policy(struct ldlm_namespace *ns, struct ldlm_lock *lock, int unused, int added, int count)

    resize policy. Decides whether to keep \a lock in LRU for current \a LRU size \a unused, added in current scan \a added and number of locks to be preferably canceled \a count.

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param int unused:
        *undescribed*

    :param int added:
        *undescribed*

    :param int count:
        *undescribed*

.. _`ldlm_cancel_lrur_policy.description`:

Description
-----------

\retval LDLM_POLICY_KEEP_LOCK keep lock in LRU in stop scanning

\retval LDLM_POLICY_CANCEL_LOCK cancel lock from LRU

.. _`ldlm_cancel_passed_policy`:

ldlm_cancel_passed_policy
=========================

.. c:function:: enum ldlm_policy_res ldlm_cancel_passed_policy(struct ldlm_namespace *ns, struct ldlm_lock *lock, int unused, int added, int count)

    \a lock in LRU for current \a LRU size \a unused, added in current scan \a added and number of locks to be preferably canceled \a count.

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param int unused:
        *undescribed*

    :param int added:
        *undescribed*

    :param int count:
        *undescribed*

.. _`ldlm_cancel_passed_policy.description`:

Description
-----------

\retval LDLM_POLICY_KEEP_LOCK keep lock in LRU in stop scanning

\retval LDLM_POLICY_CANCEL_LOCK cancel lock from LRU

.. _`ldlm_cancel_aged_policy`:

ldlm_cancel_aged_policy
=======================

.. c:function:: enum ldlm_policy_res ldlm_cancel_aged_policy(struct ldlm_namespace *ns, struct ldlm_lock *lock, int unused, int added, int count)

    LRU for current LRU size \a unused, added in current scan \a added and number of locks to be preferably canceled \a count.

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param int unused:
        *undescribed*

    :param int added:
        *undescribed*

    :param int count:
        *undescribed*

.. _`ldlm_cancel_aged_policy.description`:

Description
-----------

\retval LDLM_POLICY_KEEP_LOCK keep lock in LRU in stop scanning

\retval LDLM_POLICY_CANCEL_LOCK cancel lock from LRU

.. _`ldlm_cancel_default_policy`:

ldlm_cancel_default_policy
==========================

.. c:function:: enum ldlm_policy_res ldlm_cancel_default_policy(struct ldlm_namespace *ns, struct ldlm_lock *lock, int unused, int added, int count)

    in LRU for current LRU size \a unused, added in current scan \a added and number of locks to be preferably canceled \a count.

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param int unused:
        *undescribed*

    :param int added:
        *undescribed*

    :param int count:
        *undescribed*

.. _`ldlm_cancel_default_policy.description`:

Description
-----------

\retval LDLM_POLICY_KEEP_LOCK keep lock in LRU in stop scanning

\retval LDLM_POLICY_CANCEL_LOCK cancel lock from LRU

.. _`ldlm_cancel_lru`:

ldlm_cancel_lru
===============

.. c:function:: int ldlm_cancel_lru(struct ldlm_namespace *ns, int nr, enum ldlm_cancel_flags cancel_flags, int flags)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param int nr:
        *undescribed*

    :param enum ldlm_cancel_flags cancel_flags:
        *undescribed*

    :param int flags:
        *undescribed*

.. _`ldlm_cancel_lru.description`:

Description
-----------

When called with LCF_ASYNC the blocking callback will be handled
in a thread and this function will return after the thread has been
asked to call the callback.  When called with LCF_ASYNC the blocking
callback will be performed in this function.

.. _`ldlm_cancel_resource_local`:

ldlm_cancel_resource_local
==========================

.. c:function:: int ldlm_cancel_resource_local(struct ldlm_resource *res, struct list_head *cancels, union ldlm_policy_data *policy, enum ldlm_mode mode, __u64 lock_flags, enum ldlm_cancel_flags cancel_flags, void *opaque)

    given policy, mode. GET the found locks and add them into the \a cancels list.

    :param struct ldlm_resource \*res:
        *undescribed*

    :param struct list_head \*cancels:
        *undescribed*

    :param union ldlm_policy_data \*policy:
        *undescribed*

    :param enum ldlm_mode mode:
        *undescribed*

    :param __u64 lock_flags:
        *undescribed*

    :param enum ldlm_cancel_flags cancel_flags:
        *undescribed*

    :param void \*opaque:
        *undescribed*

.. _`ldlm_cli_cancel_list`:

ldlm_cli_cancel_list
====================

.. c:function:: int ldlm_cli_cancel_list(struct list_head *cancels, int count, struct ptlrpc_request *req, enum ldlm_cancel_flags flags)

    side locks from a list and send/prepare cancel RPCs to the server. If \a req is NULL, send CANCEL request to server with handles of locks in the \a cancels. If EARLY_CANCEL is not supported, send CANCEL requests separately per lock. If \a req is not NULL, put handles of locks in \a cancels into the request buffer at the offset \a off. Destroy \a cancels at the end.

    :param struct list_head \*cancels:
        *undescribed*

    :param int count:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param enum ldlm_cancel_flags flags:
        *undescribed*

.. _`ldlm_cli_cancel_unused_resource`:

ldlm_cli_cancel_unused_resource
===============================

.. c:function:: int ldlm_cli_cancel_unused_resource(struct ldlm_namespace *ns, const struct ldlm_res_id *res_id, union ldlm_policy_data *policy, enum ldlm_mode mode, enum ldlm_cancel_flags flags, void *opaque)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param const struct ldlm_res_id \*res_id:
        *undescribed*

    :param union ldlm_policy_data \*policy:
        *undescribed*

    :param enum ldlm_mode mode:
        *undescribed*

    :param enum ldlm_cancel_flags flags:
        *undescribed*

    :param void \*opaque:
        *undescribed*

.. _`ldlm_cli_cancel_unused_resource.description`:

Description
-----------

If flags & LDLM_FL_LOCAL_ONLY, throw the locks away without trying
to notify the server.

.. _`ldlm_cli_cancel_unused`:

ldlm_cli_cancel_unused
======================

.. c:function:: int ldlm_cli_cancel_unused(struct ldlm_namespace *ns, const struct ldlm_res_id *res_id, enum ldlm_cancel_flags flags, void *opaque)

    that have 0 readers/writers.

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param const struct ldlm_res_id \*res_id:
        *undescribed*

    :param enum ldlm_cancel_flags flags:
        *undescribed*

    :param void \*opaque:
        *undescribed*

.. _`ldlm_cli_cancel_unused.description`:

Description
-----------

If flags & LCF_LOCAL, throw the locks away without trying
to notify the server.

.. _`ldlm_cancel_unused_locks_for_replay`:

ldlm_cancel_unused_locks_for_replay
===================================

.. c:function:: void ldlm_cancel_unused_locks_for_replay(struct ldlm_namespace *ns)

    in recovery, we can't wait for any outstanding RPCs to send any RPC to the server.

    :param struct ldlm_namespace \*ns:
        *undescribed*

.. _`ldlm_cancel_unused_locks_for_replay.description`:

Description
-----------

Called only in recovery before replaying locks. there is no need to
replay locks that are unused. since the clients may hold thousands of
cached unused locks, dropping the unused locks can greatly reduce the
load on the servers at recovery time.

.. This file was automatic generated / don't edit.

