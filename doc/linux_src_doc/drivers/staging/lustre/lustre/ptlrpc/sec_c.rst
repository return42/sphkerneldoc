.. -*- coding: utf-8; mode: rst -*-

=====
sec.c
=====


.. _`sptlrpc_req_get_ctx`:

sptlrpc_req_get_ctx
===================

.. c:function:: int sptlrpc_req_get_ctx (struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`sptlrpc_req_get_ctx.description`:

Description
-----------

\pre req->rq_cli_ctx == NULL.

\retval 0 succeed, and req->rq_cli_ctx is set.
\retval -ev error number, and req->rq_cli_ctx == NULL.



.. _`sptlrpc_req_put_ctx`:

sptlrpc_req_put_ctx
===================

.. c:function:: void sptlrpc_req_put_ctx (struct ptlrpc_request *req, int sync)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param int sync:

        *undescribed*



.. _`sptlrpc_req_put_ctx.description`:

Description
-----------

\pre req->rq_cli_ctx != NULL.
\post req->rq_cli_ctx == NULL.

If \a sync == 0, this function should return quickly without sleep;
otherwise it might trigger and wait for the whole process of sending
an context-destroying rpc to server.



.. _`sptlrpc_req_replace_dead_ctx`:

sptlrpc_req_replace_dead_ctx
============================

.. c:function:: int sptlrpc_req_replace_dead_ctx (struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`sptlrpc_req_replace_dead_ctx.description`:

Description
-----------

thus marked original contexts dead, we'll find a new context for it. if
no switch is needed, \a req will end up with the same context.

\note a request must have a context, to keep other parts of code happy.
In any case of failure during the switching, we must restore the old one.



.. _`sptlrpc_req_refresh_ctx`:

sptlrpc_req_refresh_ctx
=======================

.. c:function:: int sptlrpc_req_refresh_ctx (struct ptlrpc_request *req, long timeout)

    to-date. \param timeout - < 0: don't wait - = 0: wait until success or fatal error occur - > 0: timeout value (in seconds)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param long timeout:

        *undescribed*



.. _`sptlrpc_req_refresh_ctx.description`:

Description
-----------


The status of the context could be subject to be changed by other threads
at any time. We allow this race, but once we return with 0, the caller will
suppose it's uptodated and keep using it until the owning rpc is done.

\retval 0 only if the context is uptodated.
\retval -ev error number.



.. _`sptlrpc_req_set_flavor`:

sptlrpc_req_set_flavor
======================

.. c:function:: void sptlrpc_req_set_flavor (struct ptlrpc_request *req, int opcode)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param int opcode:

        *undescribed*



.. _`sptlrpc_req_set_flavor.description`:

Description
-----------


\note this could be called in two situations:
- new request from :c:func:`ptlrpc_pre_req`, with proper ``opcode``
- old request which changed ctx in the middle, with ``opcode`` == 0



.. _`sptlrpc_import_check_ctx`:

sptlrpc_import_check_ctx
========================

.. c:function:: int sptlrpc_import_check_ctx (struct obd_import *imp)

    :param struct obd_import \*imp:

        *undescribed*



.. _`sptlrpc_import_check_ctx.description`:

Description
-----------

or not. We may create a new context and try to refresh it, and try
repeatedly try in case of non-fatal errors. Return 0 means success.



.. _`sptlrpc_cli_wrap_request`:

sptlrpc_cli_wrap_request
========================

.. c:function:: int sptlrpc_cli_wrap_request (struct ptlrpc_request *req)

    defined security transformation upon the request message of \a req. After this function called, req->rq_reqmsg is still accessible as clear text.

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`sptlrpc_cli_unwrap_reply`:

sptlrpc_cli_unwrap_reply
========================

.. c:function:: int sptlrpc_cli_unwrap_reply (struct ptlrpc_request *req)

     message of \a req. After return successfully, req->rq_repmsg points to the reply message in clear text.

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`sptlrpc_cli_unwrap_reply.description`:

Description
-----------


\pre the reply buffer should have been un-posted from LNet, so nothing is
going to change.



.. _`sptlrpc_cli_unwrap_early_reply`:

sptlrpc_cli_unwrap_early_reply
==============================

.. c:function:: int sptlrpc_cli_unwrap_early_reply (struct ptlrpc_request *req, struct ptlrpc_request **req_ret)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param struct ptlrpc_request \*\*req_ret:

        *undescribed*



.. _`sptlrpc_cli_unwrap_early_reply.description`:

Description
-----------

reply message of \a req. We expect the rq_reply_off is 0, and
rq_nob_received is the early reply size.

Because the receive buffer might be still posted, the reply data might be
changed at any time, no matter we're holding rq_lock or not. For this reason
we allocate a separate ptlrpc_request and reply buffer for early reply
processing.

\retval 0 success, \a req_ret is filled with a duplicated ptlrpc_request.
Later the caller must call :c:func:`sptlrpc_cli_finish_early_reply` on the returned
\a \*req_ret to release it.
\retval -ev error number, and \a req_ret will not be set.



.. _`sptlrpc_cli_finish_early_reply`:

sptlrpc_cli_finish_early_reply
==============================

.. c:function:: void sptlrpc_cli_finish_early_reply (struct ptlrpc_request *early_req)

    :param struct ptlrpc_request \*early_req:

        *undescribed*



.. _`sptlrpc_cli_finish_early_reply.description`:

Description
-----------


\pre \a early_req was obtained from calling :c:func:`sptlrpc_cli_unwrap_early_reply`.



.. _`sptlrpc_import_sec_adapt`:

sptlrpc_import_sec_adapt
========================

.. c:function:: int sptlrpc_import_sec_adapt (struct obd_import *imp, struct ptlrpc_svc_ctx *svc_ctx, struct sptlrpc_flavor *flvr)

    :param struct obd_import \*imp:

        *undescribed*

    :param struct ptlrpc_svc_ctx \*svc_ctx:

        *undescribed*

    :param struct sptlrpc_flavor \*flvr:

        *undescribed*



.. _`sptlrpc_import_sec_adapt.description`:

Description
-----------

configuration. Upon called, imp->imp_sec may or may not be NULL.

 - regular import: \a svc_ctx should be NULL and \a flvr is ignored;
 - reverse import: \a svc_ctx and \a flvr are obtained from incoming request.



.. _`sptlrpc_cli_alloc_reqbuf`:

sptlrpc_cli_alloc_reqbuf
========================

.. c:function:: int sptlrpc_cli_alloc_reqbuf (struct ptlrpc_request *req, int msgsize)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param int msgsize:

        *undescribed*



.. _`sptlrpc_cli_alloc_reqbuf.description`:

Description
-----------

successfully, req->rq_reqmsg points to a buffer with size \a msgsize.



.. _`sptlrpc_cli_free_reqbuf`:

sptlrpc_cli_free_reqbuf
=======================

.. c:function:: void sptlrpc_cli_free_reqbuf (struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`sptlrpc_cli_free_reqbuf.description`:

Description
-----------

req->rq_reqmsg is set to NULL and should not be accessed anymore.



.. _`sptlrpc_cli_enlarge_reqbuf`:

sptlrpc_cli_enlarge_reqbuf
==========================

.. c:function:: int sptlrpc_cli_enlarge_reqbuf (struct ptlrpc_request *req, int segment, int newsize)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param int segment:

        *undescribed*

    :param int newsize:

        *undescribed*



.. _`sptlrpc_cli_enlarge_reqbuf.description`:

Description
-----------

by req->rq_reqmsg to size \a newsize, all previously filled-in data will be
preserved after the enlargement. this must be called after original request
buffer being allocated.

\note after this be called, rq_reqmsg and rq_reqlen might have been changed,
so caller should refresh its local pointers if needed.



.. _`sptlrpc_cli_alloc_repbuf`:

sptlrpc_cli_alloc_repbuf
========================

.. c:function:: int sptlrpc_cli_alloc_repbuf (struct ptlrpc_request *req, int msgsize)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param int msgsize:

        *undescribed*



.. _`sptlrpc_cli_alloc_repbuf.description`:

Description
-----------


\note After this, req->rq_repmsg is still not accessible.



.. _`sptlrpc_cli_free_repbuf`:

sptlrpc_cli_free_repbuf
=======================

.. c:function:: void sptlrpc_cli_free_repbuf (struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`sptlrpc_cli_free_repbuf.description`:

Description
-----------

req->rq_repmsg is set to NULL and should not be accessed anymore.



.. _`sptlrpc_target_export_check`:

sptlrpc_target_export_check
===========================

.. c:function:: int sptlrpc_target_export_check (struct obd_export *exp, struct ptlrpc_request *req)

    :param struct obd_export \*exp:

        *undescribed*

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`sptlrpc_target_export_check.description`:

Description
-----------

is allowed by the export \a exp. Main logic is about taking care of
changing configurations. Return 0 means success.



.. _`sptlrpc_svc_unwrap_request`:

sptlrpc_svc_unwrap_request
==========================

.. c:function:: int sptlrpc_svc_unwrap_request (struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`sptlrpc_svc_unwrap_request.description`:

Description
-----------

incoming \a req. This must be the first thing to do with a incoming
request in ptlrpc layer.

\retval SECSVC_OK success, and req->rq_reqmsg point to request message in
clear text, size is req->rq_reqlen; also req->rq_svc_ctx is set.
\retval SECSVC_COMPLETE success, the request has been fully processed, and
reply message has been prepared.
\retval SECSVC_DROP failed, this request should be dropped.



.. _`sptlrpc_svc_alloc_rs`:

sptlrpc_svc_alloc_rs
====================

.. c:function:: int sptlrpc_svc_alloc_rs (struct ptlrpc_request *req, int msglen)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param int msglen:

        *undescribed*



.. _`sptlrpc_svc_alloc_rs.description`:

Description
-----------

req->rq_reply_state is set, and req->rq_reply_state->rs_msg point to
a buffer of \a msglen size.



.. _`sptlrpc_svc_wrap_reply`:

sptlrpc_svc_wrap_reply
======================

.. c:function:: int sptlrpc_svc_wrap_reply (struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`sptlrpc_svc_wrap_reply.description`:

Description
-----------


\post req->rq_reply_off is set to appropriate server-controlled reply offset.
\post req->rq_repmsg and req->rq_reply_state->rs_msg becomes inaccessible.



.. _`sptlrpc_svc_free_rs`:

sptlrpc_svc_free_rs
===================

.. c:function:: void sptlrpc_svc_free_rs (struct ptlrpc_reply_state *rs)

    :param struct ptlrpc_reply_state \*rs:

        *undescribed*



.. _`sptlrpc_cli_wrap_bulk`:

sptlrpc_cli_wrap_bulk
=====================

.. c:function:: int sptlrpc_cli_wrap_bulk (struct ptlrpc_request *req, struct ptlrpc_bulk_desc *desc)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param struct ptlrpc_bulk_desc \*desc:

        *undescribed*



.. _`sptlrpc_cli_wrap_bulk.description`:

Description
-----------

before transforming the request message.



.. _`sptlrpc_cli_unwrap_bulk_read`:

sptlrpc_cli_unwrap_bulk_read
============================

.. c:function:: int sptlrpc_cli_unwrap_bulk_read (struct ptlrpc_request *req, struct ptlrpc_bulk_desc *desc, int nob)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param struct ptlrpc_bulk_desc \*desc:

        *undescribed*

    :param int nob:

        *undescribed*



.. _`sptlrpc_cli_unwrap_bulk_read.description`:

Description
-----------

return nob of actual plain text size received, or error code.



.. _`sptlrpc_cli_unwrap_bulk_write`:

sptlrpc_cli_unwrap_bulk_write
=============================

.. c:function:: int sptlrpc_cli_unwrap_bulk_write (struct ptlrpc_request *req, struct ptlrpc_bulk_desc *desc)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param struct ptlrpc_bulk_desc \*desc:

        *undescribed*



.. _`sptlrpc_cli_unwrap_bulk_write.description`:

Description
-----------

return 0 for success or error code.

