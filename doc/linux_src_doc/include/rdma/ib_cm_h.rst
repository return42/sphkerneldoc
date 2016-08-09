.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/ib_cm.h

.. _`ib_cm_handler`:

ib_cm_handler
=============

.. c:function:: int ib_cm_handler(struct ib_cm_id *cm_id, struct ib_cm_event *event)

    User-defined callback to process communication events.

    :param struct ib_cm_id \*cm_id:
        Communication identifier associated with the reported event.

    :param struct ib_cm_event \*event:
        Information about the communication event.

.. _`ib_cm_handler.description`:

Description
-----------

IB_CM_REQ_RECEIVED and IB_CM_SIDR_REQ_RECEIVED communication events
generated as a result of listen requests result in the allocation of a
new \ ``cm_id``\ .  The new \ ``cm_id``\  is returned to the user through this callback.
Clients are responsible for destroying the new \ ``cm_id``\ .  For peer-to-peer
IB_CM_REQ_RECEIVED and all other events, the returned \ ``cm_id``\  corresponds
to a user's existing communication identifier.

Users may not call ib_destroy_cm_id while in the context of this callback;
however, returning a non-zero value instructs the communication manager to
destroy the \ ``cm_id``\  after the callback completes.

.. _`ib_create_cm_id`:

ib_create_cm_id
===============

.. c:function:: struct ib_cm_id *ib_create_cm_id(struct ib_device *device, ib_cm_handler cm_handler, void *context)

    Allocate a communication identifier.

    :param struct ib_device \*device:
        Device associated with the cm_id.  All related communication will
        be associated with the specified device.

    :param ib_cm_handler cm_handler:
        Callback invoked to notify the user of CM events.

    :param void \*context:
        User specified context associated with the communication
        identifier.

.. _`ib_create_cm_id.description`:

Description
-----------

Communication identifiers are used to track connection states, service
ID resolution requests, and listen requests.

.. _`ib_destroy_cm_id`:

ib_destroy_cm_id
================

.. c:function:: void ib_destroy_cm_id(struct ib_cm_id *cm_id)

    Destroy a connection identifier.

    :param struct ib_cm_id \*cm_id:
        Connection identifier to destroy.

.. _`ib_destroy_cm_id.description`:

Description
-----------

This call blocks until the connection identifier is destroyed.

.. _`ib_cm_listen`:

ib_cm_listen
============

.. c:function:: int ib_cm_listen(struct ib_cm_id *cm_id, __be64 service_id, __be64 service_mask)

    Initiates listening on the specified service ID for connection and service ID resolution requests.

    :param struct ib_cm_id \*cm_id:
        Connection identifier associated with the listen request.

    :param __be64 service_id:
        Service identifier matched against incoming connection
        and service ID resolution requests.  The service ID should be specified
        network-byte order.  If set to IB_CM_ASSIGN_SERVICE_ID, the CM will
        assign a service ID to the caller.

    :param __be64 service_mask:
        Mask applied to service ID used to listen across a
        range of service IDs.  If set to 0, the service ID is matched
        exactly.  This parameter is ignored if \ ``service_id``\  is set to
        IB_CM_ASSIGN_SERVICE_ID.

.. _`ib_send_cm_req`:

ib_send_cm_req
==============

.. c:function:: int ib_send_cm_req(struct ib_cm_id *cm_id, struct ib_cm_req_param *param)

    Sends a connection request to the remote node.

    :param struct ib_cm_id \*cm_id:
        Connection identifier that will be associated with the
        connection request.

    :param struct ib_cm_req_param \*param:
        Connection request information needed to establish the
        connection.

.. _`ib_send_cm_rep`:

ib_send_cm_rep
==============

.. c:function:: int ib_send_cm_rep(struct ib_cm_id *cm_id, struct ib_cm_rep_param *param)

    Sends a connection reply in response to a connection request.

    :param struct ib_cm_id \*cm_id:
        Connection identifier that will be associated with the
        connection request.

    :param struct ib_cm_rep_param \*param:
        Connection reply information needed to establish the
        connection.

.. _`ib_send_cm_rtu`:

ib_send_cm_rtu
==============

.. c:function:: int ib_send_cm_rtu(struct ib_cm_id *cm_id, const void *private_data, u8 private_data_len)

    Sends a connection ready to use message in response to a connection reply message.

    :param struct ib_cm_id \*cm_id:
        Connection identifier associated with the connection request.

    :param const void \*private_data:
        Optional user-defined private data sent with the
        ready to use message.

    :param u8 private_data_len:
        Size of the private data buffer, in bytes.

.. _`ib_send_cm_dreq`:

ib_send_cm_dreq
===============

.. c:function:: int ib_send_cm_dreq(struct ib_cm_id *cm_id, const void *private_data, u8 private_data_len)

    Sends a disconnection request for an existing connection.

    :param struct ib_cm_id \*cm_id:
        Connection identifier associated with the connection being
        released.

    :param const void \*private_data:
        Optional user-defined private data sent with the
        disconnection request message.

    :param u8 private_data_len:
        Size of the private data buffer, in bytes.

.. _`ib_send_cm_drep`:

ib_send_cm_drep
===============

.. c:function:: int ib_send_cm_drep(struct ib_cm_id *cm_id, const void *private_data, u8 private_data_len)

    Sends a disconnection reply to a disconnection request.

    :param struct ib_cm_id \*cm_id:
        Connection identifier associated with the connection being
        released.

    :param const void \*private_data:
        Optional user-defined private data sent with the
        disconnection reply message.

    :param u8 private_data_len:
        Size of the private data buffer, in bytes.

.. _`ib_send_cm_drep.description`:

Description
-----------

If the cm_id is in the correct state, the CM will transition the connection
to the timewait state, even if an error occurs sending the DREP message.

.. _`ib_cm_notify`:

ib_cm_notify
============

.. c:function:: int ib_cm_notify(struct ib_cm_id *cm_id, enum ib_event_type event)

    Notifies the CM of an event reported to the consumer.

    :param struct ib_cm_id \*cm_id:
        Connection identifier to transition to established.

    :param enum ib_event_type event:
        Type of event.

.. _`ib_cm_notify.description`:

Description
-----------

This routine should be invoked by users to notify the CM of relevant
communication events.  Events that should be reported to the CM and

.. _`ib_cm_notify.when-to-report-them-are`:

when to report them are
-----------------------


IB_EVENT_COMM_EST - Used when a message is received on a connected
QP before an RTU has been received.
IB_EVENT_PATH_MIG - Notifies the CM that the connection has failed over
to the alternate path.

.. _`ib_send_cm_rej`:

ib_send_cm_rej
==============

.. c:function:: int ib_send_cm_rej(struct ib_cm_id *cm_id, enum ib_cm_rej_reason reason, void *ari, u8 ari_length, const void *private_data, u8 private_data_len)

    Sends a connection rejection message to the remote node.

    :param struct ib_cm_id \*cm_id:
        Connection identifier associated with the connection being
        rejected.

    :param enum ib_cm_rej_reason reason:
        Reason for the connection request rejection.

    :param void \*ari:
        Optional additional rejection information.

    :param u8 ari_length:
        Size of the additional rejection information, in bytes.

    :param const void \*private_data:
        Optional user-defined private data sent with the
        rejection message.

    :param u8 private_data_len:
        Size of the private data buffer, in bytes.

.. _`ib_send_cm_mra`:

ib_send_cm_mra
==============

.. c:function:: int ib_send_cm_mra(struct ib_cm_id *cm_id, u8 service_timeout, const void *private_data, u8 private_data_len)

    Sends a message receipt acknowledgement to a connection message.

    :param struct ib_cm_id \*cm_id:
        Connection identifier associated with the connection message.

    :param u8 service_timeout:
        The lower 5-bits specify the maximum time required for
        the sender to reply to the connection message.  The upper 3-bits
        specify additional control flags.

    :param const void \*private_data:
        Optional user-defined private data sent with the
        message receipt acknowledgement.

    :param u8 private_data_len:
        Size of the private data buffer, in bytes.

.. _`ib_send_cm_lap`:

ib_send_cm_lap
==============

.. c:function:: int ib_send_cm_lap(struct ib_cm_id *cm_id, struct ib_sa_path_rec *alternate_path, const void *private_data, u8 private_data_len)

    Sends a load alternate path request.

    :param struct ib_cm_id \*cm_id:
        Connection identifier associated with the load alternate path
        message.

    :param struct ib_sa_path_rec \*alternate_path:
        A path record that identifies the alternate path to
        load.

    :param const void \*private_data:
        Optional user-defined private data sent with the
        load alternate path message.

    :param u8 private_data_len:
        Size of the private data buffer, in bytes.

.. _`ib_cm_init_qp_attr`:

ib_cm_init_qp_attr
==================

.. c:function:: int ib_cm_init_qp_attr(struct ib_cm_id *cm_id, struct ib_qp_attr *qp_attr, int *qp_attr_mask)

    Initializes the QP attributes for use in transitioning to a specified QP state.

    :param struct ib_cm_id \*cm_id:
        Communication identifier associated with the QP attributes to
        initialize.

    :param struct ib_qp_attr \*qp_attr:
        On input, specifies the desired QP state.  On output, the
        mandatory and desired optional attributes will be set in order to
        modify the QP to the specified state.

    :param int \*qp_attr_mask:
        The QP attribute mask that may be used to transition the
        QP to the specified state.

.. _`ib_cm_init_qp_attr.description`:

Description
-----------

Users must set the \ ``qp_attr``\ ->qp_state to the desired QP state.  This call
will set all required attributes for the given transition, along with
known optional attributes.  Users may override the attributes returned from
this call before calling ib_modify_qp.

.. _`ib_send_cm_apr`:

ib_send_cm_apr
==============

.. c:function:: int ib_send_cm_apr(struct ib_cm_id *cm_id, enum ib_cm_apr_status status, void *info, u8 info_length, const void *private_data, u8 private_data_len)

    Sends an alternate path response message in response to a load alternate path request.

    :param struct ib_cm_id \*cm_id:
        Connection identifier associated with the alternate path response.

    :param enum ib_cm_apr_status status:
        Reply status sent with the alternate path response.

    :param void \*info:
        Optional additional information sent with the alternate path
        response.

    :param u8 info_length:
        Size of the additional information, in bytes.

    :param const void \*private_data:
        Optional user-defined private data sent with the
        alternate path response message.

    :param u8 private_data_len:
        Size of the private data buffer, in bytes.

.. _`ib_send_cm_sidr_req`:

ib_send_cm_sidr_req
===================

.. c:function:: int ib_send_cm_sidr_req(struct ib_cm_id *cm_id, struct ib_cm_sidr_req_param *param)

    Sends a service ID resolution request to the remote node.

    :param struct ib_cm_id \*cm_id:
        Communication identifier that will be associated with the
        service ID resolution request.

    :param struct ib_cm_sidr_req_param \*param:
        Service ID resolution request information.

.. _`ib_send_cm_sidr_rep`:

ib_send_cm_sidr_rep
===================

.. c:function:: int ib_send_cm_sidr_rep(struct ib_cm_id *cm_id, struct ib_cm_sidr_rep_param *param)

    Sends a service ID resolution reply to the remote node.

    :param struct ib_cm_id \*cm_id:
        Communication identifier associated with the received service ID
        resolution request.

    :param struct ib_cm_sidr_rep_param \*param:
        Service ID resolution reply information.

.. This file was automatic generated / don't edit.

