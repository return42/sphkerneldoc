.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/ptlrpc/client.c

.. _`ptlrpc_init_client`:

ptlrpc_init_client
==================

.. c:function:: void ptlrpc_init_client(int req_portal, int rep_portal, char *name, struct ptlrpc_client *cl)

    :param int req_portal:
        *undescribed*

    :param int rep_portal:
        *undescribed*

    :param char \*name:
        *undescribed*

    :param struct ptlrpc_client \*cl:
        *undescribed*

.. _`ptlrpc_uuid_to_connection`:

ptlrpc_uuid_to_connection
=========================

.. c:function:: struct ptlrpc_connection *ptlrpc_uuid_to_connection(struct obd_uuid *uuid)

    :param struct obd_uuid \*uuid:
        *undescribed*

.. _`ptlrpc_new_bulk`:

ptlrpc_new_bulk
===============

.. c:function:: struct ptlrpc_bulk_desc *ptlrpc_new_bulk(unsigned npages, unsigned max_brw, unsigned type, unsigned portal)

    Returns pointer to the descriptor or NULL on error.

    :param unsigned npages:
        *undescribed*

    :param unsigned max_brw:
        *undescribed*

    :param unsigned type:
        *undescribed*

    :param unsigned portal:
        *undescribed*

.. _`ptlrpc_prep_bulk_imp`:

ptlrpc_prep_bulk_imp
====================

.. c:function:: struct ptlrpc_bulk_desc *ptlrpc_prep_bulk_imp(struct ptlrpc_request *req, unsigned npages, unsigned max_brw, unsigned type, unsigned portal)

    can fit \a npages \* pages. \a type is bulk type. \a portal is where the bulk to be sent. Used on client-side. Returns pointer to newly allocated initialized bulk descriptor or NULL on error.

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param unsigned npages:
        *undescribed*

    :param unsigned max_brw:
        *undescribed*

    :param unsigned type:
        *undescribed*

    :param unsigned portal:
        *undescribed*

.. _`__ptlrpc_prep_bulk_page`:

__ptlrpc_prep_bulk_page
=======================

.. c:function:: void __ptlrpc_prep_bulk_page(struct ptlrpc_bulk_desc *desc, struct page *page, int pageoffset, int len, int pin)

    Data to transfer in the page starts at offset \a pageoffset and amount of data to transfer from the page is \a len

    :param struct ptlrpc_bulk_desc \*desc:
        *undescribed*

    :param struct page \*page:
        *undescribed*

    :param int pageoffset:
        *undescribed*

    :param int len:
        *undescribed*

    :param int pin:
        *undescribed*

.. _`__ptlrpc_free_bulk`:

__ptlrpc_free_bulk
==================

.. c:function:: void __ptlrpc_free_bulk(struct ptlrpc_bulk_desc *desc, int unpin)

    Works on bulk descriptors both from server and client side.

    :param struct ptlrpc_bulk_desc \*desc:
        *undescribed*

    :param int unpin:
        *undescribed*

.. _`ptlrpc_at_set_req_timeout`:

ptlrpc_at_set_req_timeout
=========================

.. c:function:: void ptlrpc_at_set_req_timeout(struct ptlrpc_request *req)

    for reply before timing out this request.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_at_recv_early_reply`:

ptlrpc_at_recv_early_reply
==========================

.. c:function:: int ptlrpc_at_recv_early_reply(struct ptlrpc_request *req)

    If anything goes wrong just ignore it - same as if it never happened

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_free_rq_pool`:

ptlrpc_free_rq_pool
===================

.. c:function:: void ptlrpc_free_rq_pool(struct ptlrpc_request_pool *pool)

    Frees all requests from the pool too

    :param struct ptlrpc_request_pool \*pool:
        *undescribed*

.. _`ptlrpc_add_rqs_to_pool`:

ptlrpc_add_rqs_to_pool
======================

.. c:function:: int ptlrpc_add_rqs_to_pool(struct ptlrpc_request_pool *pool, int num_rq)

    :param struct ptlrpc_request_pool \*pool:
        *undescribed*

    :param int num_rq:
        *undescribed*

.. _`ptlrpc_init_rq_pool`:

ptlrpc_init_rq_pool
===================

.. c:function:: struct ptlrpc_request_pool *ptlrpc_init_rq_pool(int num_rq, int msgsize, int (*) populate_pool (struct ptlrpc_request_pool *, int)

    \a num_rq - initial number of requests to create for the pool \a msgsize - maximum message size possible for requests in thid pool \a populate_pool - function to be called when more requests need to be added to the pool Returns pointer to newly created pool or NULL on error.

    :param int num_rq:
        *undescribed*

    :param int msgsize:
        *undescribed*

    :param (int (\*) populate_pool (struct ptlrpc_request_pool \*, int):
        *undescribed*

.. _`ptlrpc_prep_req_from_pool`:

ptlrpc_prep_req_from_pool
=========================

.. c:function:: struct ptlrpc_request *ptlrpc_prep_req_from_pool(struct ptlrpc_request_pool *pool)

    :param struct ptlrpc_request_pool \*pool:
        *undescribed*

.. _`__ptlrpc_free_req_to_pool`:

__ptlrpc_free_req_to_pool
=========================

.. c:function:: void __ptlrpc_free_req_to_pool(struct ptlrpc_request *request)

    :param struct ptlrpc_request \*request:
        *undescribed*

.. _`ptlrpc_request_pack`:

ptlrpc_request_pack
===================

.. c:function:: int ptlrpc_request_pack(struct ptlrpc_request *request, __u32 version, int opcode)

    steps if necessary.

    :param struct ptlrpc_request \*request:
        *undescribed*

    :param __u32 version:
        *undescribed*

    :param int opcode:
        *undescribed*

.. _`__ptlrpc_request_alloc`:

__ptlrpc_request_alloc
======================

.. c:function:: struct ptlrpc_request *__ptlrpc_request_alloc(struct obd_import *imp, struct ptlrpc_request_pool *pool)

    and possibly using existing request from pool \a pool if provided. Returns allocated request structure with import field filled or NULL on error.

    :param struct obd_import \*imp:
        *undescribed*

    :param struct ptlrpc_request_pool \*pool:
        *undescribed*

.. _`ptlrpc_request_alloc_internal`:

ptlrpc_request_alloc_internal
=============================

.. c:function:: struct ptlrpc_request *ptlrpc_request_alloc_internal(struct obd_import *imp, struct ptlrpc_request_pool *pool, const struct req_format *format)

    Calls \__ptlrpc_request_alloc to allocate new request structure and inits buffer structures according to capsule template \a format. Returns allocated request structure pointer or NULL on error.

    :param struct obd_import \*imp:
        *undescribed*

    :param struct ptlrpc_request_pool \*pool:
        *undescribed*

    :param const struct req_format \*format:
        *undescribed*

.. _`ptlrpc_request_alloc`:

ptlrpc_request_alloc
====================

.. c:function:: struct ptlrpc_request *ptlrpc_request_alloc(struct obd_import *imp, const struct req_format *format)

    buffer structure according to capsule template \a format.

    :param struct obd_import \*imp:
        *undescribed*

    :param const struct req_format \*format:
        *undescribed*

.. _`ptlrpc_request_alloc_pool`:

ptlrpc_request_alloc_pool
=========================

.. c:function:: struct ptlrpc_request *ptlrpc_request_alloc_pool(struct obd_import *imp, struct ptlrpc_request_pool *pool, const struct req_format *format)

    initialize its buffer structure according to capsule template \a format.

    :param struct obd_import \*imp:
        *undescribed*

    :param struct ptlrpc_request_pool \*pool:
        *undescribed*

    :param const struct req_format \*format:
        *undescribed*

.. _`ptlrpc_request_free`:

ptlrpc_request_free
===================

.. c:function:: void ptlrpc_request_free(struct ptlrpc_request *request)

    For requests obtained from a pool earlier, return request back to pool.

    :param struct ptlrpc_request \*request:
        *undescribed*

.. _`ptlrpc_request_alloc_pack`:

ptlrpc_request_alloc_pack
=========================

.. c:function:: struct ptlrpc_request *ptlrpc_request_alloc_pack(struct obd_import *imp, const struct req_format *format, __u32 version, int opcode)

    network transfer. Only used for simple requests like OBD_PING where the only important part of the request is operation itself. Returns allocated request or NULL on error.

    :param struct obd_import \*imp:
        *undescribed*

    :param const struct req_format \*format:
        *undescribed*

    :param __u32 version:
        *undescribed*

    :param int opcode:
        *undescribed*

.. _`ptlrpc_prep_set`:

ptlrpc_prep_set
===============

.. c:function:: struct ptlrpc_request_set *ptlrpc_prep_set( void)

    Returns a pointer to the newly allocated set structure or NULL on error.

    :param  void:
        no arguments

.. _`ptlrpc_prep_fcset`:

ptlrpc_prep_fcset
=================

.. c:function:: struct ptlrpc_request_set *ptlrpc_prep_fcset(int max, set_producer_func func, void *arg)

    extension. This extension allows to control the number of requests in-flight for the whole set. A callback function to generate requests must be provided and the request set will keep the number of requests sent over the wire to \ ``max_inflight``\ . Returns a pointer to the newly allocated set structure or NULL on error.

    :param int max:
        *undescribed*

    :param set_producer_func func:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`ptlrpc_set_destroy`:

ptlrpc_set_destroy
==================

.. c:function:: void ptlrpc_set_destroy(struct ptlrpc_request_set *set)

    ptlrpc_prep_set. Ensures that all requests on the set have completed and removes all requests from the request list in a set. If any unsent request happen to be on the list, pretends that they got an error in flight and calls their completion handler.

    :param struct ptlrpc_request_set \*set:
        *undescribed*

.. _`ptlrpc_set_add_req`:

ptlrpc_set_add_req
==================

.. c:function:: void ptlrpc_set_add_req(struct ptlrpc_request_set *set, struct ptlrpc_request *req)

    Assumes request reference from the caller.

    :param struct ptlrpc_request_set \*set:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_set_add_new_req`:

ptlrpc_set_add_new_req
======================

.. c:function:: void ptlrpc_set_add_new_req(struct ptlrpcd_ctl *pc, struct ptlrpc_request *req)

    and wake the thread to make any necessary processing. Currently only used for ptlrpcd.

    :param struct ptlrpcd_ctl \*pc:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_import_delay_req`:

ptlrpc_import_delay_req
=======================

.. c:function:: int ptlrpc_import_delay_req(struct obd_import *imp, struct ptlrpc_request *req, int *status)

    can be sent, is an error, or should be delayed.

    :param struct obd_import \*imp:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param int \*status:
        *undescribed*

.. _`ptlrpc_import_delay_req.description`:

Description
-----------

Returns true if this request should be delayed. If false, and
\*status is set, then the request can not be sent and \*status is the
error code.  If false and status is 0, then request can be sent.

The imp->imp_lock must be held.

.. _`ptlrpc_console_allow`:

ptlrpc_console_allow
====================

.. c:function:: int ptlrpc_console_allow(struct ptlrpc_request *req)

    should be printed to the console or not. Makes it's decision on request status and other properties. Returns 1 to print error on the system console or 0 if not.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_check_status`:

ptlrpc_check_status
===================

.. c:function:: int ptlrpc_check_status(struct ptlrpc_request *req)

    Returns the status.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_save_versions`:

ptlrpc_save_versions
====================

.. c:function:: void ptlrpc_save_versions(struct ptlrpc_request *req)

    versions of objects into request for replay. Versions are obtained from server reply. used for VBR.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`after_reply`:

after_reply
===========

.. c:function:: int after_reply(struct ptlrpc_request *req)

    Returns 0 on success or error code. The return value would be assigned to req->rq_status by the caller as request processing status. This function also decides if the request needs to be saved for later replay.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_send_new_req`:

ptlrpc_send_new_req
===================

.. c:function:: int ptlrpc_send_new_req(struct ptlrpc_request *req)

    Also adjusts request phase. Returns 0 on success or error code.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_check_set`:

ptlrpc_check_set
================

.. c:function:: int ptlrpc_check_set(const struct lu_env *env, struct ptlrpc_request_set *set)

    and no more replies are expected. (it is possible to get less replies than requests sent e.g. due to timed out requests or requests that we had trouble to send out)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct ptlrpc_request_set \*set:
        *undescribed*

.. _`ptlrpc_check_set.note`:

NOTE
----

This function contains a potential schedule point (\ :c:func:`cond_resched`\ ).

.. _`ptlrpc_expire_one_request`:

ptlrpc_expire_one_request
=========================

.. c:function:: int ptlrpc_expire_one_request(struct ptlrpc_request *req, int async_unlink)

    until LNet actually confirms network buffer unlinking. Return 1 if we should give up further retrying attempts or 0 otherwise.

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param int async_unlink:
        *undescribed*

.. _`ptlrpc_expired_set`:

ptlrpc_expired_set
==================

.. c:function:: int ptlrpc_expired_set(void *data)

    Callback used when waiting on sets with l_wait_event. Always returns 1.

    :param void \*data:
        *undescribed*

.. _`ptlrpc_mark_interrupted`:

ptlrpc_mark_interrupted
=======================

.. c:function:: void ptlrpc_mark_interrupted(struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_interrupted_set`:

ptlrpc_interrupted_set
======================

.. c:function:: void ptlrpc_interrupted_set(void *data)

    a set \a data. Callback for l_wait_event for interruptible waits.

    :param void \*data:
        *undescribed*

.. _`ptlrpc_set_next_timeout`:

ptlrpc_set_next_timeout
=======================

.. c:function:: int ptlrpc_set_next_timeout(struct ptlrpc_request_set *set)

    :param struct ptlrpc_request_set \*set:
        *undescribed*

.. _`ptlrpc_set_wait`:

ptlrpc_set_wait
===============

.. c:function:: int ptlrpc_set_wait(struct ptlrpc_request_set *set)

    requests in the set complete (either get a reply, timeout, get an error or otherwise be interrupted). Returns 0 on success or error code otherwise.

    :param struct ptlrpc_request_set \*set:
        *undescribed*

.. _`__ptlrpc_free_req`:

__ptlrpc_free_req
=================

.. c:function:: void __ptlrpc_free_req(struct ptlrpc_request *request, int locked)

    Called when request count reached zero and request needs to be freed. Removes request from all sorts of sending/replay lists it might be on, frees network buffers if any are present. If \a locked is set, that means caller is already holding import imp_lock and so we no longer need to reobtain it (for certain lists manipulations)

    :param struct ptlrpc_request \*request:
        *undescribed*

    :param int locked:
        *undescribed*

.. _`__ptlrpc_req_finished`:

__ptlrpc_req_finished
=====================

.. c:function:: int __ptlrpc_req_finished(struct ptlrpc_request *request, int locked)

    Drops one reference count for request \a request. \a locked set indicates that caller holds import imp_lock. Frees the request when reference count reaches zero.

    :param struct ptlrpc_request \*request:
        *undescribed*

    :param int locked:
        *undescribed*

.. _`ptlrpc_req_finished`:

ptlrpc_req_finished
===================

.. c:function:: void ptlrpc_req_finished(struct ptlrpc_request *request)

    :param struct ptlrpc_request \*request:
        *undescribed*

.. _`ptlrpc_req_xid`:

ptlrpc_req_xid
==============

.. c:function:: __u64 ptlrpc_req_xid(struct ptlrpc_request *request)

    :param struct ptlrpc_request \*request:
        *undescribed*

.. _`ptlrpc_unregister_reply`:

ptlrpc_unregister_reply
=======================

.. c:function:: int ptlrpc_unregister_reply(struct ptlrpc_request *request, int async)

    NB does \_NOT\_ unregister any client-side bulk. IDEMPOTENT, but \_not\_ safe against concurrent callers. The request owner (i.e. the thread doing the I/O) must call... Returns 0 on success or 1 if unregistering cannot be made.

    :param struct ptlrpc_request \*request:
        *undescribed*

    :param int async:
        *undescribed*

.. _`ptlrpc_request_committed`:

ptlrpc_request_committed
========================

.. c:function:: void ptlrpc_request_committed(struct ptlrpc_request *req, int force)

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param int force:
        *undescribed*

.. _`ptlrpc_free_committed`:

ptlrpc_free_committed
=====================

.. c:function:: void ptlrpc_free_committed(struct obd_import *imp)

    all requests have transno smaller than last_committed for the import and don't have rq_replay set. Since requests are sorted in transno order, stops when meeting first transno bigger than last_committed. caller must hold imp->imp_lock

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_resend_req`:

ptlrpc_resend_req
=================

.. c:function:: void ptlrpc_resend_req(struct ptlrpc_request *req)

    For bulk requests we assign new xid (to avoid problems with lost replies and therefore several transfers landing into same buffer from different sending attempts).

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_request_addref`:

ptlrpc_request_addref
=====================

.. c:function:: struct ptlrpc_request *ptlrpc_request_addref(struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_retain_replayable_request`:

ptlrpc_retain_replayable_request
================================

.. c:function:: void ptlrpc_retain_replayable_request(struct ptlrpc_request *req, struct obd_import *imp)

    Must be called under imp_lock

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_queue_wait`:

ptlrpc_queue_wait
=================

.. c:function:: int ptlrpc_queue_wait(struct ptlrpc_request *req)

    Returns request processing status.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_replay_interpret`:

ptlrpc_replay_interpret
=======================

.. c:function:: int ptlrpc_replay_interpret(const struct lu_env *env, struct ptlrpc_request *req, void *data, int rc)

    In case of successful reply calls registered request replay callback. In case of error restart replay process.

    :param const struct lu_env \*env:
        *undescribed*

    :param struct ptlrpc_request \*req:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param int rc:
        *undescribed*

.. _`ptlrpc_replay_req`:

ptlrpc_replay_req
=================

.. c:function:: int ptlrpc_replay_req(struct ptlrpc_request *req)

    Adds it to ptlrpcd queue for actual sending. Returns 0 on success.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`ptlrpc_abort_inflight`:

ptlrpc_abort_inflight
=====================

.. c:function:: void ptlrpc_abort_inflight(struct obd_import *imp)

    flight request on import \a imp sending and delayed lists

    :param struct obd_import \*imp:
        *undescribed*

.. _`ptlrpc_abort_set`:

ptlrpc_abort_set
================

.. c:function:: void ptlrpc_abort_set(struct ptlrpc_request_set *set)

    :param struct ptlrpc_request_set \*set:
        *undescribed*

.. _`year_2004`:

YEAR_2004
=========

.. c:function::  YEAR_2004()

    this node, and only requires the property that it is monotonically increasing.  It does not need to be sequential.  Since this is also used as the RDMA match bits, it is important that a single client NOT have the same match bits for two different in-flight requests, hence we do NOT want to have an XID per target or similar.

.. _`year_2004.description`:

Description
-----------

To avoid an unlikely collision between match bits after a client reboot
(which would deliver old data into the wrong RDMA buffer) initialize
the XID based on the current time, assuming a maximum RPC rate of 1M RPC/s.
If the time is clearly incorrect, we instead use a 62-bit random number.
In the worst case the random number will overflow 1M RPCs per second in
9133 years, or permutations thereof.

.. _`ptlrpc_next_xid`:

ptlrpc_next_xid
===============

.. c:function:: __u64 ptlrpc_next_xid( void)

    :param  void:
        no arguments

.. _`ptlrpc_next_xid.description`:

Description
-----------

Multi-bulk BRW RPCs consume multiple XIDs for each bulk transfer, starting
at the returned xid, up to xid + PTLRPC_BULK_OPS_COUNT - 1. The BRW RPC
itself uses the last bulk xid needed, so the server can determine the
the number of bulk transfers from the RPC XID and a bitmask.  The starting
xid must align to a power-of-two value.

This is assumed to be true due to the initial ptlrpc_last_xid
value also being initialized to a power-of-two value. LU-1431

.. _`ptlrpc_sample_next_xid`:

ptlrpc_sample_next_xid
======================

.. c:function:: __u64 ptlrpc_sample_next_xid( void)

    Returns possible next xid.

    :param  void:
        no arguments

.. _`ptlrpcd_alloc_work`:

ptlrpcd_alloc_work
==================

.. c:function:: void *ptlrpcd_alloc_work(struct obd_import *imp, int (*) cb (const struct lu_env *, void *, void *cbdata)

    :param struct obd_import \*imp:
        *undescribed*

    :param (int (\*) cb (const struct lu_env \*, void \*):
        *undescribed*

    :param void \*cbdata:
        *undescribed*

.. This file was automatic generated / don't edit.

