.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ldlm/ldlm_lock.c

.. _`ldlm_convert_policy_to_wire`:

ldlm_convert_policy_to_wire
===========================

.. c:function:: void ldlm_convert_policy_to_wire(enum ldlm_type type, const ldlm_policy_data_t *lpolicy, ldlm_wire_policy_data_t *wpolicy)

    :param enum ldlm_type type:
        *undescribed*

    :param const ldlm_policy_data_t \*lpolicy:
        *undescribed*

    :param ldlm_wire_policy_data_t \*wpolicy:
        *undescribed*

.. _`ldlm_convert_policy_to_local`:

ldlm_convert_policy_to_local
============================

.. c:function:: void ldlm_convert_policy_to_local(struct obd_export *exp, enum ldlm_type type, const ldlm_wire_policy_data_t *wpolicy, ldlm_policy_data_t *lpolicy)

    :param struct obd_export \*exp:
        *undescribed*

    :param enum ldlm_type type:
        *undescribed*

    :param const ldlm_wire_policy_data_t \*wpolicy:
        *undescribed*

    :param ldlm_policy_data_t \*lpolicy:
        *undescribed*

.. _`ldlm_lock_get`:

ldlm_lock_get
=============

.. c:function:: struct ldlm_lock *ldlm_lock_get(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_get.description`:

Description
-----------

Lock refcounts, during creation:
- one special one for allocation, dec'd only once in destroy
- one for being a lock that's in-use
- one for the addref associated with a new lock

.. _`ldlm_lock_put`:

ldlm_lock_put
=============

.. c:function:: void ldlm_lock_put(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_put.description`:

Description
-----------

Also frees the lock if it was last reference.

.. _`ldlm_lock_remove_from_lru_nolock`:

ldlm_lock_remove_from_lru_nolock
================================

.. c:function:: int ldlm_lock_remove_from_lru_nolock(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_remove_from_lru_check`:

ldlm_lock_remove_from_lru_check
===============================

.. c:function:: int ldlm_lock_remove_from_lru_check(struct ldlm_lock *lock, time_t last_use)

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param time_t last_use:
        *undescribed*

.. _`ldlm_lock_remove_from_lru_check.description`:

Description
-----------

If \a last_use is non-zero, it will remove the lock from LRU only if
it matches lock's l_last_used.

\retval 0 if \a last_use is set, the lock is not in LRU list or \a last_use
doesn't match lock's l_last_used;
otherwise, the lock hasn't been in the LRU list.
\retval 1 the lock was in LRU list and removed.

.. _`ldlm_lock_add_to_lru_nolock`:

ldlm_lock_add_to_lru_nolock
===========================

.. c:function:: void ldlm_lock_add_to_lru_nolock(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_add_to_lru`:

ldlm_lock_add_to_lru
====================

.. c:function:: void ldlm_lock_add_to_lru(struct ldlm_lock *lock)

    first.

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_touch_in_lru`:

ldlm_lock_touch_in_lru
======================

.. c:function:: void ldlm_lock_touch_in_lru(struct ldlm_lock *lock)

    the LRU. Performs necessary LRU locking

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_destroy_internal`:

ldlm_lock_destroy_internal
==========================

.. c:function:: int ldlm_lock_destroy_internal(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_destroy_internal.description`:

Description
-----------

Used by ldlm_lock_destroy and ldlm_lock_destroy_nolock
Must be called with l_lock and lr_lock held.

Does not actually free the lock data, but rather marks the lock as
destroyed by setting l_destroyed field in the lock to 1.  Destroys a
handle->lock association too, so that the lock can no longer be found
and removes the lock from LRU list.  Actual lock freeing occurs when
last lock reference goes away.

Original comment (of some historical value):
This used to have a 'strict' flag, which recovery would use to mark an
in-use lock as needing-to-die.  Lest I am ever tempted to put it back, I
shall explain why it's gone: with the new hash table scheme, once you call
ldlm_lock_destroy, you can never drop your final references on this lock.
Because it's not in the hash table anymore.  -phil

.. _`ldlm_lock_destroy`:

ldlm_lock_destroy
=================

.. c:function:: void ldlm_lock_destroy(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_destroy_nolock`:

ldlm_lock_destroy_nolock
========================

.. c:function:: void ldlm_lock_destroy_nolock(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_change_resource`:

ldlm_lock_change_resource
=========================

.. c:function:: int ldlm_lock_change_resource(struct ldlm_namespace *ns, struct ldlm_lock *lock, const struct ldlm_res_id *new_resid)

    This is used on client when server returns some other lock than requested (typically as a result of intent operation)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param const struct ldlm_res_id \*new_resid:
        *undescribed*

.. _`ldlm_lock2handle`:

ldlm_lock2handle
================

.. c:function:: void ldlm_lock2handle(const struct ldlm_lock *lock, struct lustre_handle *lockh)

    Does not take any references.

    :param const struct ldlm_lock \*lock:
        *undescribed*

    :param struct lustre_handle \*lockh:
        *undescribed*

.. _`__ldlm_handle2lock`:

__ldlm_handle2lock
==================

.. c:function:: struct ldlm_lock *__ldlm_handle2lock(const struct lustre_handle *handle, __u64 flags)

    :param const struct lustre_handle \*handle:
        *undescribed*

    :param __u64 flags:
        *undescribed*

.. _`__ldlm_handle2lock.description`:

Description
-----------

if \a flags: atomically get the lock and set the flags.
Return NULL if flag already set

.. _`ldlm_lock2desc`:

ldlm_lock2desc
==============

.. c:function:: void ldlm_lock2desc(struct ldlm_lock *lock, struct ldlm_lock_desc *desc)

    lock descriptor \a desc structure.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param struct ldlm_lock_desc \*desc:
        *undescribed*

.. _`ldlm_add_bl_work_item`:

ldlm_add_bl_work_item
=====================

.. c:function:: void ldlm_add_bl_work_item(struct ldlm_lock *lock, struct ldlm_lock *new, struct list_head *work_list)

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param struct ldlm_lock \*new:
        *undescribed*

    :param struct list_head \*work_list:
        *undescribed*

.. _`ldlm_add_bl_work_item.description`:

Description
-----------

Only add if we have not sent a blocking AST to the lock yet.

.. _`ldlm_add_cp_work_item`:

ldlm_add_cp_work_item
=====================

.. c:function:: void ldlm_add_cp_work_item(struct ldlm_lock *lock, struct list_head *work_list)

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param struct list_head \*work_list:
        *undescribed*

.. _`ldlm_add_ast_work_item`:

ldlm_add_ast_work_item
======================

.. c:function:: void ldlm_add_ast_work_item(struct ldlm_lock *lock, struct ldlm_lock *new, struct list_head *work_list)

    what sort of an AST work needs to be done and calls the proper adding function. Must be called with lr_lock held.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param struct ldlm_lock \*new:
        *undescribed*

    :param struct list_head \*work_list:
        *undescribed*

.. _`ldlm_lock_addref`:

ldlm_lock_addref
================

.. c:function:: void ldlm_lock_addref(const struct lustre_handle *lockh, __u32 mode)

    r/w reference type is determined by \a mode Calls ldlm_lock_addref_internal.

    :param const struct lustre_handle \*lockh:
        *undescribed*

    :param __u32 mode:
        *undescribed*

.. _`ldlm_lock_addref_internal_nolock`:

ldlm_lock_addref_internal_nolock
================================

.. c:function:: void ldlm_lock_addref_internal_nolock(struct ldlm_lock *lock, __u32 mode)

    Add specified reader/writer reference to LDLM lock \a lock. r/w reference type is determined by \a mode Removes lock from LRU if it is there. Assumes the LDLM lock is already locked.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param __u32 mode:
        *undescribed*

.. _`ldlm_lock_addref_try`:

ldlm_lock_addref_try
====================

.. c:function:: int ldlm_lock_addref_try(const struct lustre_handle *lockh, __u32 mode)

    fails if lock is already LDLM_FL_CBPENDING or destroyed.

    :param const struct lustre_handle \*lockh:
        *undescribed*

    :param __u32 mode:
        *undescribed*

.. _`ldlm_lock_addref_try.description`:

Description
-----------

\retval 0 success, lock was addref-ed

\retval -EAGAIN lock is being canceled.

.. _`ldlm_lock_addref_internal`:

ldlm_lock_addref_internal
=========================

.. c:function:: void ldlm_lock_addref_internal(struct ldlm_lock *lock, __u32 mode)

    Locks LDLM lock and calls ldlm_lock_addref_internal_nolock to do the work. Only called for local locks.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param __u32 mode:
        *undescribed*

.. _`ldlm_lock_decref_internal_nolock`:

ldlm_lock_decref_internal_nolock
================================

.. c:function:: void ldlm_lock_decref_internal_nolock(struct ldlm_lock *lock, __u32 mode)

    Assumes LDLM lock is already locked. only called in ldlm_flock_destroy and for local locks. Does NOT add lock to LRU if no r/w references left to accommodate flock locks that cannot be placed in LRU.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param __u32 mode:
        *undescribed*

.. _`ldlm_lock_decref_internal`:

ldlm_lock_decref_internal
=========================

.. c:function:: void ldlm_lock_decref_internal(struct ldlm_lock *lock, __u32 mode)

    Locks LDLM lock first. If the lock is determined to be client lock on a client and r/w refcount drops to zero and the lock is not blocked, the lock is added to LRU lock on the namespace. For blocked LDLM locks if r/w count drops to zero, blocking_ast is called.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param __u32 mode:
        *undescribed*

.. _`ldlm_lock_decref`:

ldlm_lock_decref
================

.. c:function:: void ldlm_lock_decref(const struct lustre_handle *lockh, __u32 mode)

    :param const struct lustre_handle \*lockh:
        *undescribed*

    :param __u32 mode:
        *undescribed*

.. _`ldlm_lock_decref_and_cancel`:

ldlm_lock_decref_and_cancel
===========================

.. c:function:: void ldlm_lock_decref_and_cancel(const struct lustre_handle *lockh, __u32 mode)

    \a lockh and mark it for subsequent cancellation once r/w refcount drops to zero instead of putting into LRU.

    :param const struct lustre_handle \*lockh:
        *undescribed*

    :param __u32 mode:
        *undescribed*

.. _`ldlm_lock_decref_and_cancel.description`:

Description
-----------

Typical usage is for GROUP locks which we cannot allow to be cached.

.. _`search_granted_lock`:

search_granted_lock
===================

.. c:function:: void search_granted_lock(struct list_head *queue, struct ldlm_lock *req, struct sl_insert_point *prev)

    :param struct list_head \*queue:
        *undescribed*

    :param struct ldlm_lock \*req:
        *undescribed*

    :param struct sl_insert_point \*prev:
        *undescribed*

.. _`search_granted_lock.description`:

Description
-----------

Used for locks eligible for skiplist optimization.

.. _`search_granted_lock.parameters`:

Parameters
----------

queue [input]:  the granted list where search acts on;
req [input]:    the lock whose position to be located;
prev [output]:  positions within 3 lists to insert \ ``req``\  to

.. _`search_granted_lock.return-value`:

Return Value
------------

filled \ ``prev``\ 

.. _`search_granted_lock.note`:

NOTE
----

called by
- ldlm_grant_lock_with_skiplist

.. _`ldlm_granted_list_add_lock`:

ldlm_granted_list_add_lock
==========================

.. c:function:: void ldlm_granted_list_add_lock(struct ldlm_lock *lock, struct sl_insert_point *prev)

    \a prev.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param struct sl_insert_point \*prev:
        *undescribed*

.. _`ldlm_grant_lock_with_skiplist`:

ldlm_grant_lock_with_skiplist
=============================

.. c:function:: void ldlm_grant_lock_with_skiplist(struct ldlm_lock *lock)

    correctness.

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_grant_lock`:

ldlm_grant_lock
===============

.. c:function:: void ldlm_grant_lock(struct ldlm_lock *lock, struct list_head *work_list)

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param struct list_head \*work_list:
        *undescribed*

.. _`ldlm_grant_lock.description`:

Description
-----------

Includes putting the lock into granted list and updating lock mode.

.. _`ldlm_grant_lock.note`:

NOTE
----

called by
- ldlm_lock_enqueue
- ldlm_reprocess_queue
- ldlm_lock_convert

must be called with lr_lock held

.. _`search_queue`:

search_queue
============

.. c:function:: struct ldlm_lock *search_queue(struct list_head *queue, enum ldlm_mode *mode, ldlm_policy_data_t *policy, struct ldlm_lock *old_lock, __u64 flags, int unref)

    :param struct list_head \*queue:
        *undescribed*

    :param enum ldlm_mode \*mode:
        *undescribed*

    :param ldlm_policy_data_t \*policy:
        *undescribed*

    :param struct ldlm_lock \*old_lock:
        *undescribed*

    :param __u64 flags:
        *undescribed*

    :param int unref:
        *undescribed*

.. _`search_queue.description`:

Description
-----------

\retval a referenced lock or NULL.  See the flag descriptions below, in the
comment above ldlm_lock_match

.. _`ldlm_lock_allow_match_locked`:

ldlm_lock_allow_match_locked
============================

.. c:function:: void ldlm_lock_allow_match_locked(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_allow_match_locked.description`:

Description
-----------

Used to prevent certain races in LOV/OSC where the lock is granted, but LVB
is not yet valid.
Assumes LDLM lock is already locked.

.. _`ldlm_lock_allow_match`:

ldlm_lock_allow_match
=====================

.. c:function:: void ldlm_lock_allow_match(struct ldlm_lock *lock)

    Locks the lock and then \see ldlm_lock_allow_match_locked

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_match`:

ldlm_lock_match
===============

.. c:function:: enum ldlm_mode ldlm_lock_match(struct ldlm_namespace *ns, __u64 flags, const struct ldlm_res_id *res_id, enum ldlm_type type, ldlm_policy_data_t *policy, enum ldlm_mode mode, struct lustre_handle *lockh, int unref)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param __u64 flags:
        *undescribed*

    :param const struct ldlm_res_id \*res_id:
        *undescribed*

    :param enum ldlm_type type:
        *undescribed*

    :param ldlm_policy_data_t \*policy:
        *undescribed*

    :param enum ldlm_mode mode:
        *undescribed*

    :param struct lustre_handle \*lockh:
        *undescribed*

    :param int unref:
        *undescribed*

.. _`ldlm_lock_match.description`:

Description
-----------

Typically returns a reference to matched lock unless LDLM_FL_TEST_LOCK is
set in \a flags

.. _`ldlm_lock_match.can-be-called-in-two-ways`:

Can be called in two ways
-------------------------


If 'ns' is NULL, then lockh describes an existing lock that we want to look
for a duplicate of.

Otherwise, all of the fields must be filled in, to match against.

If 'flags' contains LDLM_FL_LOCAL_ONLY, then only match local locks on the
server (ie, connh is NULL)
If 'flags' contains LDLM_FL_BLOCK_GRANTED, then only locks on the granted
list will be considered
If 'flags' contains LDLM_FL_CBPENDING, then locks that have been marked
to be canceled can still be matched as long as they still have reader
or writer referneces
If 'flags' contains LDLM_FL_TEST_LOCK, then don't actually reference a lock,
just tell us if we would have matched.

\retval 1 if it finds an already-existing lock that is compatible; in this
case, lockh is filled in with a \ :c:func:`addref`\ ed lock

We also check security context, and if that fails we simply return 0 (to
keep caller code unchanged), the context failure will be discovered by
caller sometime later.

.. _`ldlm_lock_create`:

ldlm_lock_create
================

.. c:function:: struct ldlm_lock *ldlm_lock_create(struct ldlm_namespace *ns, const struct ldlm_res_id *res_id, enum ldlm_type type, enum ldlm_mode mode, const struct ldlm_callback_suite *cbs, void *data, __u32 lvb_len, enum lvb_type lvb_type)

    Returns a referenced lock

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param const struct ldlm_res_id \*res_id:
        *undescribed*

    :param enum ldlm_type type:
        *undescribed*

    :param enum ldlm_mode mode:
        *undescribed*

    :param const struct ldlm_callback_suite \*cbs:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param __u32 lvb_len:
        *undescribed*

    :param enum lvb_type lvb_type:
        *undescribed*

.. _`ldlm_lock_enqueue`:

ldlm_lock_enqueue
=================

.. c:function:: enum ldlm_error ldlm_lock_enqueue(struct ldlm_namespace *ns, struct ldlm_lock **lockp, void *cookie, __u64 *flags)

    On the client this is called from ldlm_cli_enqueue_fini after we already got an initial reply from the server with some status.

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct ldlm_lock \*\*lockp:
        *undescribed*

    :param void \*cookie:
        *undescribed*

    :param __u64 \*flags:
        *undescribed*

.. _`ldlm_lock_enqueue.description`:

Description
-----------

Does not block. As a result of enqueue the lock would be put
into granted or waiting list.

.. _`ldlm_work_bl_ast_lock`:

ldlm_work_bl_ast_lock
=====================

.. c:function:: int ldlm_work_bl_ast_lock(struct ptlrpc_request_set *rqset, void *opaq)

    :param struct ptlrpc_request_set \*rqset:
        *undescribed*

    :param void \*opaq:
        *undescribed*

.. _`ldlm_work_cp_ast_lock`:

ldlm_work_cp_ast_lock
=====================

.. c:function:: int ldlm_work_cp_ast_lock(struct ptlrpc_request_set *rqset, void *opaq)

    :param struct ptlrpc_request_set \*rqset:
        *undescribed*

    :param void \*opaq:
        *undescribed*

.. _`ldlm_work_revoke_ast_lock`:

ldlm_work_revoke_ast_lock
=========================

.. c:function:: int ldlm_work_revoke_ast_lock(struct ptlrpc_request_set *rqset, void *opaq)

    :param struct ptlrpc_request_set \*rqset:
        *undescribed*

    :param void \*opaq:
        *undescribed*

.. _`ldlm_work_gl_ast_lock`:

ldlm_work_gl_ast_lock
=====================

.. c:function:: int ldlm_work_gl_ast_lock(struct ptlrpc_request_set *rqset, void *opaq)

    :param struct ptlrpc_request_set \*rqset:
        *undescribed*

    :param void \*opaq:
        *undescribed*

.. _`ldlm_run_ast_work`:

ldlm_run_ast_work
=================

.. c:function:: int ldlm_run_ast_work(struct ldlm_namespace *ns, struct list_head *rpc_list, enum ldlm_desc_ast_t ast_type)

    :param struct ldlm_namespace \*ns:
        *undescribed*

    :param struct list_head \*rpc_list:
        *undescribed*

    :param enum ldlm_desc_ast_t ast_type:
        *undescribed*

.. _`ldlm_run_ast_work.description`:

Description
-----------

Used on server to send multiple ASTs together instead of sending one by
one.

.. _`ldlm_cancel_callback`:

ldlm_cancel_callback
====================

.. c:function:: void ldlm_cancel_callback(struct ldlm_lock *lock)

    "cancelling" mode.

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_unlink_lock_skiplist`:

ldlm_unlink_lock_skiplist
=========================

.. c:function:: void ldlm_unlink_lock_skiplist(struct ldlm_lock *req)

    enabled LDLM lock \a req from granted list

    :param struct ldlm_lock \*req:
        *undescribed*

.. _`ldlm_lock_cancel`:

ldlm_lock_cancel
================

.. c:function:: void ldlm_lock_cancel(struct ldlm_lock *lock)

    :param struct ldlm_lock \*lock:
        *undescribed*

.. _`ldlm_lock_set_data`:

ldlm_lock_set_data
==================

.. c:function:: int ldlm_lock_set_data(const struct lustre_handle *lockh, void *data)

    :param const struct lustre_handle \*lockh:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`ldlm_lock_dump_handle`:

ldlm_lock_dump_handle
=====================

.. c:function:: void ldlm_lock_dump_handle(int level, const struct lustre_handle *lockh)

    :param int level:
        *undescribed*

    :param const struct lustre_handle \*lockh:
        *undescribed*

.. _`ldlm_lock_dump_handle.description`:

Description
-----------

Used when printing all locks on a resource for debug purposes.

.. _`_ldlm_lock_debug`:

_ldlm_lock_debug
================

.. c:function:: void _ldlm_lock_debug(struct ldlm_lock *lock, struct libcfs_debug_msg_data *msgdata, const char *fmt,  ...)

    Helper function.

    :param struct ldlm_lock \*lock:
        *undescribed*

    :param struct libcfs_debug_msg_data \*msgdata:
        *undescribed*

    :param const char \*fmt:
        *undescribed*

    :param ... :
        variable arguments

.. This file was automatic generated / don't edit.

