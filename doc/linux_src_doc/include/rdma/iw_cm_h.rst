.. -*- coding: utf-8; mode: rst -*-

=======
iw_cm.h
=======


.. _`int`:

int
===

.. c:function:: typedef int ( *iw_cm_handler)

    Function to be called by the IW CM when delivering events to the client.

    :param  \*iw_cm_handler:

        *undescribed*



.. _`int`:

int
===

.. c:function:: typedef int ( *iw_event_handler)

    Function called by the provider when delivering provider events to the IW CM. Returns either 0 indicating the event was processed or -errno if the event could not be processed.

    :param  \*iw_event_handler:

        *undescribed*



.. _`iw_create_cm_id`:

iw_create_cm_id
===============

.. c:function:: struct iw_cm_id *iw_create_cm_id (struct ib_device *device, iw_cm_handler cm_handler, void *context)

    Create an IW CM identifier.

    :param struct ib_device \*device:
        The IB device on which to create the IW CM identier.

    :param iw_cm_handler cm_handler:

        *undescribed*

    :param void \*context:
        User specified context associated with the id.



.. _`iw_destroy_cm_id`:

iw_destroy_cm_id
================

.. c:function:: void iw_destroy_cm_id (struct iw_cm_id *cm_id)

    Destroy an IW CM identifier.

    :param struct iw_cm_id \*cm_id:
        The previously created IW CM identifier to destroy.



.. _`iw_destroy_cm_id.description`:

Description
-----------

The client can assume that no events will be delivered for the CM ID after
this function returns.



.. _`iw_cm_unbind_qp`:

iw_cm_unbind_qp
===============

.. c:function:: void iw_cm_unbind_qp (struct iw_cm_id *cm_id, struct ib_qp *qp)

    Unbind the specified IW CM identifier and QP

    :param struct iw_cm_id \*cm_id:
        The IW CM idenfier to unbind from the QP.

    :param struct ib_qp \*qp:
        The QP



.. _`iw_cm_unbind_qp.description`:

Description
-----------

This is called by the provider when destroying the QP to ensure
that any references held by the IWCM are released. It may also
be called by the IWCM when destroying a CM_ID to that any
references held by the provider are released.



.. _`iw_cm_get_qp`:

iw_cm_get_qp
============

.. c:function:: struct ib_qp *iw_cm_get_qp (struct ib_device *device, int qpn)

    Return the ib_qp associated with a QPN

    :param struct ib_device \*device:

        *undescribed*

    :param int qpn:
        The queue pair number



.. _`iw_cm_listen`:

iw_cm_listen
============

.. c:function:: int iw_cm_listen (struct iw_cm_id *cm_id, int backlog)

    Listen for incoming connection requests on the specified IW CM id.

    :param struct iw_cm_id \*cm_id:
        The IW CM identifier.

    :param int backlog:
        The maximum number of outstanding un-accepted inbound listen
        requests to queue.



.. _`iw_cm_listen.description`:

Description
-----------

The source address and port number are specified in the IW CM identifier
structure.



.. _`iw_cm_accept`:

iw_cm_accept
============

.. c:function:: int iw_cm_accept (struct iw_cm_id *cm_id, struct iw_cm_conn_param *iw_param)

    Called to accept an incoming connect request.

    :param struct iw_cm_id \*cm_id:
        The IW CM identifier associated with the connection request.

    :param struct iw_cm_conn_param \*iw_param:
        Pointer to a structure containing connection establishment
        parameters.



.. _`iw_cm_accept.description`:

Description
-----------

The specified cm_id will have been provided in the event data for a
CONNECT_REQUEST event. Subsequent events related to this connection will be
delivered to the specified IW CM identifier prior and may occur prior to
the return of this function. If this function returns a non-zero value, the
client can assume that no events will be delivered to the specified IW CM
identifier.



.. _`iw_cm_reject`:

iw_cm_reject
============

.. c:function:: int iw_cm_reject (struct iw_cm_id *cm_id, const void *private_data, u8 private_data_len)

    Reject an incoming connection request.

    :param struct iw_cm_id \*cm_id:
        Connection identifier associated with the request.

    :param const void \*private_data:

        *undescribed*

    :param u8 private_data_len:
        The number of bytes in the private_data parameter.



.. _`iw_cm_reject.description`:

Description
-----------

The client can assume that no events will be delivered to the specified IW
CM identifier following the return of this function. The private_data
buffer is available for reuse when this function returns.



.. _`iw_cm_connect`:

iw_cm_connect
=============

.. c:function:: int iw_cm_connect (struct iw_cm_id *cm_id, struct iw_cm_conn_param *iw_param)

    Called to request a connection to a remote peer.

    :param struct iw_cm_id \*cm_id:
        The IW CM identifier for the connection.

    :param struct iw_cm_conn_param \*iw_param:
        Pointer to a structure containing connection  establishment
        parameters.



.. _`iw_cm_connect.description`:

Description
-----------

Events may be delivered to the specified IW CM identifier prior to the
return of this function. If this function returns a non-zero value, the
client can assume that no events will be delivered to the specified IW CM
identifier.



.. _`iw_cm_disconnect`:

iw_cm_disconnect
================

.. c:function:: int iw_cm_disconnect (struct iw_cm_id *cm_id, int abrupt)

    Close the specified connection.

    :param struct iw_cm_id \*cm_id:
        The IW CM identifier to close.

    :param int abrupt:
        If 0, the connection will be closed gracefully, otherwise, the
        connection will be reset.



.. _`iw_cm_disconnect.description`:

Description
-----------

The IW CM identifier is still active until the IW_CM_EVENT_CLOSE event is
delivered.



.. _`iw_cm_init_qp_attr`:

iw_cm_init_qp_attr
==================

.. c:function:: int iw_cm_init_qp_attr (struct iw_cm_id *cm_id, struct ib_qp_attr *qp_attr, int *qp_attr_mask)

    Called to initialize the attributes of the QP associated with a IW CM identifier.

    :param struct iw_cm_id \*cm_id:
        The IW CM identifier associated with the QP

    :param struct ib_qp_attr \*qp_attr:
        Pointer to the QP attributes structure.

    :param int \*qp_attr_mask:
        Pointer to a bit vector specifying which QP attributes are
        valid.

