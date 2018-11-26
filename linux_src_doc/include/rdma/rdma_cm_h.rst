.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/rdma_cm.h

.. _`rdma_cm_event_handler`:

rdma_cm_event_handler
=====================

.. c:function:: int rdma_cm_event_handler(struct rdma_cm_id *id, struct rdma_cm_event *event)

    Callback used to report user events.

    :param id:
        *undescribed*
    :type id: struct rdma_cm_id \*

    :param event:
        *undescribed*
    :type event: struct rdma_cm_event \*

.. _`rdma_cm_event_handler.notes`:

Notes
-----

Users may not call rdma_destroy_id from this callback to destroy
the passed in id, or a corresponding listen id.  Returning a
non-zero value from the callback will destroy the passed in id.

.. _`rdma_create_id`:

rdma_create_id
==============

.. c:function::  rdma_create_id( net,  event_handler,  context,  ps,  qp_type)

    Create an RDMA identifier.

    :param net:
        The network namespace in which to create the new id.
    :type net: 

    :param event_handler:
        User callback invoked to report events associated with the
        returned rdma_id.
    :type event_handler: 

    :param context:
        User specified context associated with the id.
    :type context: 

    :param ps:
        RDMA port space.
    :type ps: 

    :param qp_type:
        type of queue pair associated with the id.
    :type qp_type: 

.. _`rdma_create_id.description`:

Description
-----------

Returns a new rdma_cm_id. The id holds a reference on the network
namespace until it is destroyed.

The event handler callback serializes on the id's mutex and is
allowed to sleep.

.. _`rdma_destroy_id`:

rdma_destroy_id
===============

.. c:function:: void rdma_destroy_id(struct rdma_cm_id *id)

    Destroys an RDMA identifier.

    :param id:
        RDMA identifier.
    :type id: struct rdma_cm_id \*

.. _`rdma_destroy_id.note`:

Note
----

calling this function has the effect of canceling in-flight
asynchronous operations associated with the id.

.. _`rdma_bind_addr`:

rdma_bind_addr
==============

.. c:function:: int rdma_bind_addr(struct rdma_cm_id *id, struct sockaddr *addr)

    Bind an RDMA identifier to a source address and associated RDMA device, if needed.

    :param id:
        RDMA identifier.
    :type id: struct rdma_cm_id \*

    :param addr:
        Local address information.  Wildcard values are permitted.
    :type addr: struct sockaddr \*

.. _`rdma_bind_addr.description`:

Description
-----------

This associates a source address with the RDMA identifier before calling
rdma_listen.  If a specific local address is given, the RDMA identifier will
be bound to a local RDMA device.

.. _`rdma_resolve_addr`:

rdma_resolve_addr
=================

.. c:function:: int rdma_resolve_addr(struct rdma_cm_id *id, struct sockaddr *src_addr, const struct sockaddr *dst_addr, unsigned long timeout_ms)

    Resolve destination and optional source addresses from IP addresses to an RDMA address.  If successful, the specified rdma_cm_id will be bound to a local device.

    :param id:
        RDMA identifier.
    :type id: struct rdma_cm_id \*

    :param src_addr:
        Source address information.  This parameter may be NULL.
    :type src_addr: struct sockaddr \*

    :param dst_addr:
        Destination address information.
    :type dst_addr: const struct sockaddr \*

    :param timeout_ms:
        Time to wait for resolution to complete.
    :type timeout_ms: unsigned long

.. _`rdma_resolve_route`:

rdma_resolve_route
==================

.. c:function:: int rdma_resolve_route(struct rdma_cm_id *id, unsigned long timeout_ms)

    Resolve the RDMA address bound to the RDMA identifier into route information needed to establish a connection.

    :param id:
        *undescribed*
    :type id: struct rdma_cm_id \*

    :param timeout_ms:
        *undescribed*
    :type timeout_ms: unsigned long

.. _`rdma_resolve_route.description`:

Description
-----------

This is called on the client side of a connection.
Users must have first called rdma_resolve_addr to resolve a dst_addr
into an RDMA address before calling this routine.

.. _`rdma_create_qp`:

rdma_create_qp
==============

.. c:function:: int rdma_create_qp(struct rdma_cm_id *id, struct ib_pd *pd, struct ib_qp_init_attr *qp_init_attr)

    Allocate a QP and associate it with the specified RDMA identifier.

    :param id:
        *undescribed*
    :type id: struct rdma_cm_id \*

    :param pd:
        *undescribed*
    :type pd: struct ib_pd \*

    :param qp_init_attr:
        *undescribed*
    :type qp_init_attr: struct ib_qp_init_attr \*

.. _`rdma_create_qp.description`:

Description
-----------

QPs allocated to an rdma_cm_id will automatically be transitioned by the CMA
through their states.

.. _`rdma_destroy_qp`:

rdma_destroy_qp
===============

.. c:function:: void rdma_destroy_qp(struct rdma_cm_id *id)

    Deallocate the QP associated with the specified RDMA identifier.

    :param id:
        *undescribed*
    :type id: struct rdma_cm_id \*

.. _`rdma_destroy_qp.description`:

Description
-----------

Users must destroy any QP associated with an RDMA identifier before
destroying the RDMA ID.

.. _`rdma_init_qp_attr`:

rdma_init_qp_attr
=================

.. c:function:: int rdma_init_qp_attr(struct rdma_cm_id *id, struct ib_qp_attr *qp_attr, int *qp_attr_mask)

    Initializes the QP attributes for use in transitioning to a specified QP state.

    :param id:
        Communication identifier associated with the QP attributes to
        initialize.
    :type id: struct rdma_cm_id \*

    :param qp_attr:
        On input, specifies the desired QP state.  On output, the
        mandatory and desired optional attributes will be set in order to
        modify the QP to the specified state.
    :type qp_attr: struct ib_qp_attr \*

    :param qp_attr_mask:
        The QP attribute mask that may be used to transition the
        QP to the specified state.
    :type qp_attr_mask: int \*

.. _`rdma_init_qp_attr.description`:

Description
-----------

Users must set the \ ``qp_attr->qp_state``\  to the desired QP state.  This call
will set all required attributes for the given transition, along with
known optional attributes.  Users may override the attributes returned from
this call before calling ib_modify_qp.

Users that wish to have their QP automatically transitioned through its
states can associate a QP with the rdma_cm_id by calling \ :c:func:`rdma_create_qp`\ .

.. _`rdma_connect`:

rdma_connect
============

.. c:function:: int rdma_connect(struct rdma_cm_id *id, struct rdma_conn_param *conn_param)

    Initiate an active connection request.

    :param id:
        Connection identifier to connect.
    :type id: struct rdma_cm_id \*

    :param conn_param:
        Connection information used for connected QPs.
    :type conn_param: struct rdma_conn_param \*

.. _`rdma_connect.description`:

Description
-----------

Users must have resolved a route for the rdma_cm_id to connect with
by having called rdma_resolve_route before calling this routine.

This call will either connect to a remote QP or obtain remote QP
information for unconnected rdma_cm_id's.  The actual operation is
based on the rdma_cm_id's port space.

.. _`rdma_listen`:

rdma_listen
===========

.. c:function:: int rdma_listen(struct rdma_cm_id *id, int backlog)

    This function is called by the passive side to listen for incoming connection requests.

    :param id:
        *undescribed*
    :type id: struct rdma_cm_id \*

    :param backlog:
        *undescribed*
    :type backlog: int

.. _`rdma_listen.description`:

Description
-----------

Users must have bound the rdma_cm_id to a local address by calling
rdma_bind_addr before calling this routine.

.. _`rdma_accept`:

rdma_accept
===========

.. c:function::  rdma_accept( id,  conn_param)

    Called to accept a connection request or response.

    :param id:
        Connection identifier associated with the request.
    :type id: 

    :param conn_param:
        Information needed to establish the connection.  This must be
        provided if accepting a connection request.  If accepting a connection
        response, this parameter must be NULL.
    :type conn_param: 

.. _`rdma_accept.description`:

Description
-----------

Typically, this routine is only called by the listener to accept a connection
request.  It must also be called on the active side of a connection if the
user is performing their own QP transitions.

In the case of error, a reject message is sent to the remote side and the
state of the qp associated with the id is modified to error, such that any
previously posted receive buffers would be flushed.

.. _`rdma_notify`:

rdma_notify
===========

.. c:function:: int rdma_notify(struct rdma_cm_id *id, enum ib_event_type event)

    Notifies the RDMA CM of an asynchronous event that has occurred on the connection.

    :param id:
        Connection identifier to transition to established.
    :type id: struct rdma_cm_id \*

    :param event:
        Asynchronous event.
    :type event: enum ib_event_type

.. _`rdma_notify.description`:

Description
-----------

This routine should be invoked by users to notify the CM of relevant
communication events.  Events that should be reported to the CM and

.. _`rdma_notify.when-to-report-them-are`:

when to report them are
-----------------------


IB_EVENT_COMM_EST - Used when a message is received on a connected
QP before an RTU has been received.

.. _`rdma_reject`:

rdma_reject
===========

.. c:function:: int rdma_reject(struct rdma_cm_id *id, const void *private_data, u8 private_data_len)

    Called to reject a connection request or response.

    :param id:
        *undescribed*
    :type id: struct rdma_cm_id \*

    :param private_data:
        *undescribed*
    :type private_data: const void \*

    :param private_data_len:
        *undescribed*
    :type private_data_len: u8

.. _`rdma_disconnect`:

rdma_disconnect
===============

.. c:function:: int rdma_disconnect(struct rdma_cm_id *id)

    This function disconnects the associated QP and transitions it into the error state.

    :param id:
        *undescribed*
    :type id: struct rdma_cm_id \*

.. _`rdma_join_multicast`:

rdma_join_multicast
===================

.. c:function:: int rdma_join_multicast(struct rdma_cm_id *id, struct sockaddr *addr, u8 join_state, void *context)

    Join the multicast group specified by the given address.

    :param id:
        Communication identifier associated with the request.
    :type id: struct rdma_cm_id \*

    :param addr:
        Multicast address identifying the group to join.
    :type addr: struct sockaddr \*

    :param join_state:
        Multicast JoinState bitmap requested by port.
        Bitmap is based on IB_SA_MCMEMBER_REC_JOIN_STATE bits.
    :type join_state: u8

    :param context:
        User-defined context associated with the join request, returned
        to the user through the private_data pointer in multicast events.
    :type context: void \*

.. _`rdma_leave_multicast`:

rdma_leave_multicast
====================

.. c:function:: void rdma_leave_multicast(struct rdma_cm_id *id, struct sockaddr *addr)

    Leave the multicast group specified by the given address.

    :param id:
        *undescribed*
    :type id: struct rdma_cm_id \*

    :param addr:
        *undescribed*
    :type addr: struct sockaddr \*

.. _`rdma_set_service_type`:

rdma_set_service_type
=====================

.. c:function:: void rdma_set_service_type(struct rdma_cm_id *id, int tos)

    Set the type of service associated with a connection identifier.

    :param id:
        Communication identifier to associated with service type.
    :type id: struct rdma_cm_id \*

    :param tos:
        Type of service.
    :type tos: int

.. _`rdma_set_service_type.description`:

Description
-----------

The type of service is interpretted as a differentiated service
field (RFC 2474).  The service type should be specified before
performing route resolution, as existing communication on the
connection identifier may be unaffected.  The type of service
requested may not be supported by the network to all destinations.

.. _`rdma_set_reuseaddr`:

rdma_set_reuseaddr
==================

.. c:function:: int rdma_set_reuseaddr(struct rdma_cm_id *id, int reuse)

    Allow the reuse of local addresses when binding the rdma_cm_id.

    :param id:
        Communication identifier to configure.
    :type id: struct rdma_cm_id \*

    :param reuse:
        Value indicating if the bound address is reusable.
    :type reuse: int

.. _`rdma_set_reuseaddr.description`:

Description
-----------

Reuse must be set before an address is bound to the id.

.. _`rdma_set_afonly`:

rdma_set_afonly
===============

.. c:function:: int rdma_set_afonly(struct rdma_cm_id *id, int afonly)

    Specify that listens are restricted to the bound address family only.

    :param id:
        Communication identifer to configure.
    :type id: struct rdma_cm_id \*

    :param afonly:
        Value indicating if listens are restricted.
    :type afonly: int

.. _`rdma_set_afonly.description`:

Description
-----------

Must be set before identifier is in the listening state.

.. _`rdma_is_consumer_reject`:

rdma_is_consumer_reject
=======================

.. c:function:: bool rdma_is_consumer_reject(struct rdma_cm_id *id, int reason)

    return true if the consumer rejected the connect request.

    :param id:
        Communication identifier that received the REJECT event.
    :type id: struct rdma_cm_id \*

    :param reason:
        Value returned in the REJECT event status field.
    :type reason: int

.. _`rdma_consumer_reject_data`:

rdma_consumer_reject_data
=========================

.. c:function:: const void *rdma_consumer_reject_data(struct rdma_cm_id *id, struct rdma_cm_event *ev, u8 *data_len)

    return the consumer reject private data and length, if any.

    :param id:
        Communication identifier that received the REJECT event.
    :type id: struct rdma_cm_id \*

    :param ev:
        RDMA CM reject event.
    :type ev: struct rdma_cm_event \*

    :param data_len:
        Pointer to the resulting length of the consumer data.
    :type data_len: u8 \*

.. _`rdma_read_gids`:

rdma_read_gids
==============

.. c:function:: void rdma_read_gids(struct rdma_cm_id *cm_id, union ib_gid *sgid, union ib_gid *dgid)

    Return the SGID and DGID used for establishing connection. This can be used after \ :c:func:`rdma_resolve_addr`\  on client side. This can be use on new connection on server side. This is applicable to IB, RoCE, iWarp. If cm_id is not bound yet to the RDMA device, it doesn't copy and SGID or DGID to the given pointers.

    :param cm_id:
        *undescribed*
    :type cm_id: struct rdma_cm_id \*

    :param sgid:
        Pointer to SGID where SGID will be returned. It is optional.
    :type sgid: union ib_gid \*

    :param dgid:
        Pointer to DGID where DGID will be returned. It is optional.
    :type dgid: union ib_gid \*

.. _`rdma_read_gids.note`:

Note
----

This API should not be used by any new ULPs or new code.
Instead, users interested in querying GIDs should refer to path record
of the rdma_cm_id to query the GIDs.
This API is provided for compatibility for existing users.

.. This file was automatic generated / don't edit.

