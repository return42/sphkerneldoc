.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/sa_query.c

.. _`ib_sa_cancel_query`:

ib_sa_cancel_query
==================

.. c:function:: void ib_sa_cancel_query(int id, struct ib_sa_query *query)

    try to cancel an SA query

    :param id:
        ID of query to cancel
    :type id: int

    :param query:
        query pointer to cancel
    :type query: struct ib_sa_query \*

.. _`ib_sa_cancel_query.description`:

Description
-----------

Try to cancel an SA query.  If the id and query don't match up or
the query has already completed, nothing is done.  Otherwise the
query is canceled and will complete with a status of -EINTR.

.. _`ib_init_ah_attr_from_path`:

ib_init_ah_attr_from_path
=========================

.. c:function:: int ib_init_ah_attr_from_path(struct ib_device *device, u8 port_num, struct sa_path_rec *rec, struct rdma_ah_attr *ah_attr, const struct ib_gid_attr *gid_attr)

    Initialize address handle attributes based on an SA path record.

    :param device:
        Device associated ah attributes initialization.
    :type device: struct ib_device \*

    :param port_num:
        Port on the specified device.
    :type port_num: u8

    :param rec:
        path record entry to use for ah attributes initialization.
    :type rec: struct sa_path_rec \*

    :param ah_attr:
        address handle attributes to initialization from path record.
    :type ah_attr: struct rdma_ah_attr \*

    :param gid_attr:
        *undescribed*
    :type gid_attr: const struct ib_gid_attr \*

.. _`ib_init_ah_attr_from_path.description`:

Description
-----------

When \ :c:func:`ib_init_ah_attr_from_path`\  returns success,
(a) for IB link layer it optionally contains a reference to SGID attribute
when GRH is present for IB link layer.
(b) for RoCE link layer it contains a reference to SGID attribute.
User must invoke \ :c:func:`rdma_destroy_ah_attr`\  to release reference to SGID
attributes which are initialized using \ :c:func:`ib_init_ah_attr_from_path`\ .

.. _`opa_pr_query_possible`:

opa_pr_query_possible
=====================

.. c:function:: int opa_pr_query_possible(struct ib_sa_client *client, struct ib_device *device, u8 port_num, struct sa_path_rec *rec)

    Retuns PR_NOT_SUPPORTED if a path record query is not possible, PR_OPA_SUPPORTED if an OPA path record query is possible and PR_IB_SUPPORTED if an IB path record query is possible.

    :param client:
        *undescribed*
    :type client: struct ib_sa_client \*

    :param device:
        *undescribed*
    :type device: struct ib_device \*

    :param port_num:
        *undescribed*
    :type port_num: u8

    :param rec:
        *undescribed*
    :type rec: struct sa_path_rec \*

.. _`ib_sa_path_rec_get`:

ib_sa_path_rec_get
==================

.. c:function:: int ib_sa_path_rec_get(struct ib_sa_client *client, struct ib_device *device, u8 port_num, struct sa_path_rec *rec, ib_sa_comp_mask comp_mask, unsigned long timeout_ms, gfp_t gfp_mask, void (*callback)(int status, struct sa_path_rec *resp, void *context), void *context, struct ib_sa_query **sa_query)

    Start a Path get query

    :param client:
        SA client
    :type client: struct ib_sa_client \*

    :param device:
        device to send query on
    :type device: struct ib_device \*

    :param port_num:
        port number to send query on
    :type port_num: u8

    :param rec:
        Path Record to send in query
    :type rec: struct sa_path_rec \*

    :param comp_mask:
        component mask to send in query
    :type comp_mask: ib_sa_comp_mask

    :param timeout_ms:
        time to wait for response
    :type timeout_ms: unsigned long

    :param gfp_mask:
        GFP mask to use for internal allocations
    :type gfp_mask: gfp_t

    :param void (\*callback)(int status, struct sa_path_rec \*resp, void \*context):
        function called when query completes, times out or is
        canceled

    :param context:
        opaque user context passed to callback
    :type context: void \*

    :param sa_query:
        query context, used to cancel query
    :type sa_query: struct ib_sa_query \*\*

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

.. c:function:: int ib_sa_service_rec_query(struct ib_sa_client *client, struct ib_device *device, u8 port_num, u8 method, struct ib_sa_service_rec *rec, ib_sa_comp_mask comp_mask, unsigned long timeout_ms, gfp_t gfp_mask, void (*callback)(int status, struct ib_sa_service_rec *resp, void *context), void *context, struct ib_sa_query **sa_query)

    Start Service Record operation

    :param client:
        SA client
    :type client: struct ib_sa_client \*

    :param device:
        device to send request on
    :type device: struct ib_device \*

    :param port_num:
        port number to send request on
    :type port_num: u8

    :param method:
        SA method - should be get, set, or delete
    :type method: u8

    :param rec:
        Service Record to send in request
    :type rec: struct ib_sa_service_rec \*

    :param comp_mask:
        component mask to send in request
    :type comp_mask: ib_sa_comp_mask

    :param timeout_ms:
        time to wait for response
    :type timeout_ms: unsigned long

    :param gfp_mask:
        GFP mask to use for internal allocations
    :type gfp_mask: gfp_t

    :param void (\*callback)(int status, struct ib_sa_service_rec \*resp, void \*context):
        function called when request completes, times out or is
        canceled

    :param context:
        opaque user context passed to callback
    :type context: void \*

    :param sa_query:
        request context, used to cancel request
    :type sa_query: struct ib_sa_query \*\*

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

