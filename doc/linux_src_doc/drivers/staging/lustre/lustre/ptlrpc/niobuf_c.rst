.. -*- coding: utf-8; mode: rst -*-

========
niobuf.c
========


.. _`ptl_send_buf`:

ptl_send_buf
============

.. c:function:: int ptl_send_buf (lnet_handle_md_t *mdh, void *base, int len, lnet_ack_req_t ack, struct ptlrpc_cb_id *cbid, struct ptlrpc_connection *conn, int portal, __u64 xid, unsigned int offset)

    :param lnet_handle_md_t \*mdh:

        *undescribed*

    :param void \*base:

        *undescribed*

    :param int len:

        *undescribed*

    :param lnet_ack_req_t ack:

        *undescribed*

    :param struct ptlrpc_cb_id \*cbid:

        *undescribed*

    :param struct ptlrpc_connection \*conn:

        *undescribed*

    :param int portal:

        *undescribed*

    :param __u64 xid:

        *undescribed*

    :param unsigned int offset:

        *undescribed*



.. _`ptl_send_buf.description`:

Description
-----------

over \a conn connection to portal \a portal.
Returns 0 on success or error code.



.. _`ptlrpc_register_bulk`:

ptlrpc_register_bulk
====================

.. c:function:: int ptlrpc_register_bulk (struct ptlrpc_request *req)

    :param struct ptlrpc_request \*req:

        *undescribed*



.. _`ptlrpc_register_bulk.description`:

Description
-----------

Returns 0 on success or error code.



.. _`ptlrpc_unregister_bulk`:

ptlrpc_unregister_bulk
======================

.. c:function:: int ptlrpc_unregister_bulk (struct ptlrpc_request *req, int async)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param int async:

        *undescribed*



.. _`ptlrpc_unregister_bulk.description`:

Description
-----------

thread-safe (i.e. only interlocks with completion callback).
Returns 1 on success or 0 if network unregistration failed for whatever
reason.



.. _`ptlrpc_send_reply`:

ptlrpc_send_reply
=================

.. c:function:: int ptlrpc_send_reply (struct ptlrpc_request *req, int flags)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param int flags:

        *undescribed*



.. _`ptlrpc_send_reply.description`:

Description
-----------

\a flags defines reply types
Returns 0 on success or error code



.. _`ptlrpc_send_error`:

ptlrpc_send_error
=================

.. c:function:: int ptlrpc_send_error (struct ptlrpc_request *req, int may_be_difficult)

    :param struct ptlrpc_request \*req:

        *undescribed*

    :param int may_be_difficult:

        *undescribed*



.. _`ptlrpc_send_error.description`:

Description
-----------

reply buffers if necessary.



.. _`ptl_send_rpc`:

ptl_send_rpc
============

.. c:function:: int ptl_send_rpc (struct ptlrpc_request *request, int noreply)

    :param struct ptlrpc_request \*request:

        *undescribed*

    :param int noreply:

        *undescribed*



.. _`ptl_send_rpc.description`:

Description
-----------

if \a noreply is set, don't expect any reply back and don't set up
reply buffers.
Returns 0 on success or error code.



.. _`ptlrpc_register_rqbd`:

ptlrpc_register_rqbd
====================

.. c:function:: int ptlrpc_register_rqbd (struct ptlrpc_request_buffer_desc *rqbd)

    :param struct ptlrpc_request_buffer_desc \*rqbd:

        *undescribed*

