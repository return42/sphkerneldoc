.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/sa_query.c

.. _`ib_sa_cancel_query`:

ib_sa_cancel_query
==================

.. c:function:: void ib_sa_cancel_query(int id, struct ib_sa_query *query)

    try to cancel an SA query

    :param int id:
        ID of query to cancel

    :param struct ib_sa_query \*query:
        query pointer to cancel

.. _`ib_sa_cancel_query.description`:

Description
-----------

Try to cancel an SA query.  If the id and query don't match up or
the query has already completed, nothing is done.  Otherwise the
query is canceled and will complete with a status of -EINTR.

.. _`opa_pr_query_possible`:

opa_pr_query_possible
=====================

.. c:function:: int opa_pr_query_possible(struct ib_sa_client *client, struct ib_device *device, u8 port_num, struct sa_path_rec *rec)

    Retuns PR_NOT_SUPPORTED if a path record query is not possible, PR_OPA_SUPPORTED if an OPA path record query is possible and PR_IB_SUPPORTED if an IB path record query is possible.

    :param struct ib_sa_client \*client:
        *undescribed*

    :param struct ib_device \*device:
        *undescribed*

    :param u8 port_num:
        *undescribed*

    :param struct sa_path_rec \*rec:
        *undescribed*

.. _`ib_sa_path_rec_get`:

ib_sa_path_rec_get
==================

.. c:function:: int ib_sa_path_rec_get(struct ib_sa_client *client, struct ib_device *device, u8 port_num, struct sa_path_rec *rec, ib_sa_comp_mask comp_mask, int timeout_ms, gfp_t gfp_mask, void (*callback)(int status, struct sa_path_rec *resp, void *context), void *context, struct ib_sa_query **sa_query)

    Start a Path get query

    :param struct ib_sa_client \*client:
        SA client

    :param struct ib_device \*device:
        device to send query on

    :param u8 port_num:
        port number to send query on

    :param struct sa_path_rec \*rec:
        Path Record to send in query

    :param ib_sa_comp_mask comp_mask:
        component mask to send in query

    :param int timeout_ms:
        time to wait for response

    :param gfp_t gfp_mask:
        GFP mask to use for internal allocations

    :param void (\*callback)(int status, struct sa_path_rec \*resp, void \*context):
        function called when query completes, times out or is
        canceled

    :param void \*context:
        opaque user context passed to callback

    :param struct ib_sa_query \*\*sa_query:
        query context, used to cancel query

.. _`ib_sa_path_rec_get.description`:

Description
-----------

Send a Path Record Get query to the SA to look up a path.  The
callback function will be called when the query completes (or
fails); status is 0 for a successful response, -EINTR if the query
is canceled, -ETIMEDOUT is the query timed out, or -EIO if an error
occurred sending the query.  The resp parameter of the callback is
only valid if status is 0.

If the return value of \ :c:func:`ib_sa_path_rec_get`\  is negative, it is an
error code.  Otherwise it is a query ID that can be used to cancel
the query.

.. _`ib_sa_service_rec_query`:

ib_sa_service_rec_query
=======================

.. c:function:: int ib_sa_service_rec_query(struct ib_sa_client *client, struct ib_device *device, u8 port_num, u8 method, struct ib_sa_service_rec *rec, ib_sa_comp_mask comp_mask, int timeout_ms, gfp_t gfp_mask, void (*callback)(int status, struct ib_sa_service_rec *resp, void *context), void *context, struct ib_sa_query **sa_query)

    Start Service Record operation

    :param struct ib_sa_client \*client:
        SA client

    :param struct ib_device \*device:
        device to send request on

    :param u8 port_num:
        port number to send request on

    :param u8 method:
        SA method - should be get, set, or delete

    :param struct ib_sa_service_rec \*rec:
        Service Record to send in request

    :param ib_sa_comp_mask comp_mask:
        component mask to send in request

    :param int timeout_ms:
        time to wait for response

    :param gfp_t gfp_mask:
        GFP mask to use for internal allocations

    :param void (\*callback)(int status, struct ib_sa_service_rec \*resp, void \*context):
        function called when request completes, times out or is
        canceled

    :param void \*context:
        opaque user context passed to callback

    :param struct ib_sa_query \*\*sa_query:
        request context, used to cancel request

.. _`ib_sa_service_rec_query.description`:

Description
-----------

Send a Service Record set/get/delete to the SA to register,
unregister or query a service record.
The callback function will be called when the request completes (or
fails); status is 0 for a successful response, -EINTR if the query
is canceled, -ETIMEDOUT is the query timed out, or -EIO if an error
occurred sending the query.  The resp parameter of the callback is
only valid if status is 0.

If the return value of \ :c:func:`ib_sa_service_rec_query`\  is negative, it is an
error code.  Otherwise it is a request ID that can be used to cancel
the query.

.. This file was automatic generated / don't edit.

