.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/qmi_interface.c

.. _`qmi_recv_new_server`:

qmi_recv_new_server
===================

.. c:function:: void qmi_recv_new_server(struct qmi_handle *qmi, unsigned int service, unsigned int instance, unsigned int node, unsigned int port)

    handler of NEW_SERVER control message

    :param struct qmi_handle \*qmi:
        qmi handle

    :param unsigned int service:
        service id of the new server

    :param unsigned int instance:
        instance id of the new server

    :param unsigned int node:
        node of the new server

    :param unsigned int port:
        port of the new server

.. _`qmi_recv_new_server.description`:

Description
-----------

Calls the new_server callback to inform the client about a newly registered
server matching the currently registered service lookup.

.. _`qmi_recv_del_server`:

qmi_recv_del_server
===================

.. c:function:: void qmi_recv_del_server(struct qmi_handle *qmi, unsigned int node, unsigned int port)

    handler of DEL_SERVER control message

    :param struct qmi_handle \*qmi:
        qmi handle

    :param unsigned int node:
        node of the dying server, a value of -1 matches all nodes

    :param unsigned int port:
        port of the dying server, a value of -1 matches all ports

.. _`qmi_recv_del_server.description`:

Description
-----------

Calls the del_server callback for each previously seen server, allowing the
client to react to the disappearing server.

.. _`qmi_recv_bye`:

qmi_recv_bye
============

.. c:function:: void qmi_recv_bye(struct qmi_handle *qmi, unsigned int node)

    handler of BYE control message

    :param struct qmi_handle \*qmi:
        qmi handle

    :param unsigned int node:
        id of the dying node

.. _`qmi_recv_bye.description`:

Description
-----------

Signals the client that all previously registered services on this node are
now gone and then calls the bye callback to allow the client client further
cleaning up resources associated with this remote.

.. _`qmi_recv_del_client`:

qmi_recv_del_client
===================

.. c:function:: void qmi_recv_del_client(struct qmi_handle *qmi, unsigned int node, unsigned int port)

    handler of DEL_CLIENT control message

    :param struct qmi_handle \*qmi:
        qmi handle

    :param unsigned int node:
        node of the dying client

    :param unsigned int port:
        port of the dying client

.. _`qmi_recv_del_client.description`:

Description
-----------

Signals the client about a dying client, by calling the del_client callback.

.. _`qmi_add_lookup`:

qmi_add_lookup
==============

.. c:function:: int qmi_add_lookup(struct qmi_handle *qmi, unsigned int service, unsigned int version, unsigned int instance)

    register a new lookup with the name service

    :param struct qmi_handle \*qmi:
        qmi handle

    :param unsigned int service:
        service id of the request

    :param unsigned int version:
        version number of the request

    :param unsigned int instance:
        instance id of the request

.. _`qmi_add_lookup.description`:

Description
-----------

Registering a lookup query with the name server will cause the name server
to send NEW_SERVER and DEL_SERVER control messages to this socket as
matching services are registered.

.. _`qmi_add_lookup.return`:

Return
------

0 on success, negative errno on failure.

.. _`qmi_add_server`:

qmi_add_server
==============

.. c:function:: int qmi_add_server(struct qmi_handle *qmi, unsigned int service, unsigned int version, unsigned int instance)

    register a service with the name service

    :param struct qmi_handle \*qmi:
        qmi handle

    :param unsigned int service:
        type of the service

    :param unsigned int version:
        version of the service

    :param unsigned int instance:
        instance of the service

.. _`qmi_add_server.description`:

Description
-----------

Register a new service with the name service. This allows clients to find
and start sending messages to the client associated with \ ``qmi``\ .

.. _`qmi_add_server.return`:

Return
------

0 on success, negative errno on failure.

.. _`qmi_txn_init`:

qmi_txn_init
============

.. c:function:: int qmi_txn_init(struct qmi_handle *qmi, struct qmi_txn *txn, struct qmi_elem_info *ei, void *c_struct)

    allocate transaction id within the given QMI handle

    :param struct qmi_handle \*qmi:
        QMI handle

    :param struct qmi_txn \*txn:
        transaction context

    :param struct qmi_elem_info \*ei:
        description of how to decode a matching response (optional)

    :param void \*c_struct:
        pointer to the object to decode the response into (optional)

.. _`qmi_txn_init.description`:

Description
-----------

This allocates a transaction id within the QMI handle. If \ ``ei``\  and \ ``c_struct``\ 
are specified any responses to this transaction will be decoded as described
by \ ``ei``\  into \ ``c_struct``\ .

A client calling \ :c:func:`qmi_txn_init`\  must call either \ :c:func:`qmi_txn_wait`\  or
\ :c:func:`qmi_txn_cancel`\  to free up the allocated resources.

.. _`qmi_txn_init.return`:

Return
------

Transaction id on success, negative errno on failure.

.. _`qmi_txn_wait`:

qmi_txn_wait
============

.. c:function:: int qmi_txn_wait(struct qmi_txn *txn, unsigned long timeout)

    wait for a response on a transaction

    :param struct qmi_txn \*txn:
        transaction handle

    :param unsigned long timeout:
        timeout, in jiffies

.. _`qmi_txn_wait.description`:

Description
-----------

If the transaction is decoded by the means of \ ``ei``\  and \ ``c_struct``\  the return
value will be the returned value of \ :c:func:`qmi_decode_message`\ , otherwise it's up
to the specified message handler to fill out the result.

.. _`qmi_txn_wait.return`:

Return
------

the transaction response on success, negative errno on failure.

.. _`qmi_txn_cancel`:

qmi_txn_cancel
==============

.. c:function:: void qmi_txn_cancel(struct qmi_txn *txn)

    cancel an ongoing transaction

    :param struct qmi_txn \*txn:
        transaction id

.. _`qmi_invoke_handler`:

qmi_invoke_handler
==================

.. c:function:: void qmi_invoke_handler(struct qmi_handle *qmi, struct sockaddr_qrtr *sq, struct qmi_txn *txn, const void *buf, size_t len)

    find and invoke a handler for a message

    :param struct qmi_handle \*qmi:
        qmi handle

    :param struct sockaddr_qrtr \*sq:
        sockaddr of the sender

    :param struct qmi_txn \*txn:
        transaction object for the message

    :param const void \*buf:
        buffer containing the message

    :param size_t len:
        length of \ ``buf``\ 

.. _`qmi_invoke_handler.description`:

Description
-----------

Find handler and invoke handler for the incoming message.

.. _`qmi_handle_net_reset`:

qmi_handle_net_reset
====================

.. c:function:: void qmi_handle_net_reset(struct qmi_handle *qmi)

    invoked to handle ENETRESET on a QMI handle

    :param struct qmi_handle \*qmi:
        the QMI context

.. _`qmi_handle_net_reset.description`:

Description
-----------

As a result of registering a name service with the QRTR all open sockets are
flagged with ENETRESET and this function will be called. The typical case is
the initial boot, where this signals that the local node id has been
configured and as such any bound sockets needs to be rebound. So close the
socket, inform the client and re-initialize the socket.

For clients it's generally sufficient to react to the del_server callbacks,
but server code is expected to treat the net_reset callback as a "bye" from
all nodes.

Finally the QMI handle will send out registration requests for any lookups
and services.

.. _`qmi_handle_init`:

qmi_handle_init
===============

.. c:function:: int qmi_handle_init(struct qmi_handle *qmi, size_t recv_buf_size, const struct qmi_ops *ops, const struct qmi_msg_handler *handlers)

    initialize a QMI client handle

    :param struct qmi_handle \*qmi:
        QMI handle to initialize

    :param size_t recv_buf_size:
        maximum size of incoming message

    :param const struct qmi_ops \*ops:
        reference to callbacks for QRTR notifications

    :param const struct qmi_msg_handler \*handlers:
        NULL-terminated list of QMI message handlers

.. _`qmi_handle_init.description`:

Description
-----------

This initializes the QMI client handle to allow sending and receiving QMI
messages. As messages are received the appropriate handler will be invoked.

.. _`qmi_handle_init.return`:

Return
------

0 on success, negative errno on failure.

.. _`qmi_handle_release`:

qmi_handle_release
==================

.. c:function:: void qmi_handle_release(struct qmi_handle *qmi)

    release the QMI client handle

    :param struct qmi_handle \*qmi:
        QMI client handle

.. _`qmi_handle_release.description`:

Description
-----------

This closes the underlying socket and stops any handling of QMI messages.

.. _`qmi_send_message`:

qmi_send_message
================

.. c:function:: ssize_t qmi_send_message(struct qmi_handle *qmi, struct sockaddr_qrtr *sq, struct qmi_txn *txn, int type, int msg_id, size_t len, struct qmi_elem_info *ei, const void *c_struct)

    send a QMI message

    :param struct qmi_handle \*qmi:
        QMI client handle

    :param struct sockaddr_qrtr \*sq:
        destination sockaddr

    :param struct qmi_txn \*txn:
        transaction object to use for the message

    :param int type:
        type of message to send

    :param int msg_id:
        message id

    :param size_t len:
        max length of the QMI message

    :param struct qmi_elem_info \*ei:
        QMI message description

    :param const void \*c_struct:
        object to be encoded

.. _`qmi_send_message.description`:

Description
-----------

This function encodes \ ``c_struct``\  using \ ``ei``\  into a message of type \ ``type``\ ,
with \ ``msg_id``\  and \ ``txn``\  into a buffer of maximum size \ ``len``\ , and sends this to
\ ``sq``\ .

.. _`qmi_send_message.return`:

Return
------

0 on success, negative errno on failure.

.. _`qmi_send_request`:

qmi_send_request
================

.. c:function:: ssize_t qmi_send_request(struct qmi_handle *qmi, struct sockaddr_qrtr *sq, struct qmi_txn *txn, int msg_id, size_t len, struct qmi_elem_info *ei, const void *c_struct)

    send a request QMI message

    :param struct qmi_handle \*qmi:
        QMI client handle

    :param struct sockaddr_qrtr \*sq:
        destination sockaddr

    :param struct qmi_txn \*txn:
        transaction object to use for the message

    :param int msg_id:
        message id

    :param size_t len:
        max length of the QMI message

    :param struct qmi_elem_info \*ei:
        QMI message description

    :param const void \*c_struct:
        object to be encoded

.. _`qmi_send_request.return`:

Return
------

0 on success, negative errno on failure.

.. _`qmi_send_response`:

qmi_send_response
=================

.. c:function:: ssize_t qmi_send_response(struct qmi_handle *qmi, struct sockaddr_qrtr *sq, struct qmi_txn *txn, int msg_id, size_t len, struct qmi_elem_info *ei, const void *c_struct)

    send a response QMI message

    :param struct qmi_handle \*qmi:
        QMI client handle

    :param struct sockaddr_qrtr \*sq:
        destination sockaddr

    :param struct qmi_txn \*txn:
        transaction object to use for the message

    :param int msg_id:
        message id

    :param size_t len:
        max length of the QMI message

    :param struct qmi_elem_info \*ei:
        QMI message description

    :param const void \*c_struct:
        object to be encoded

.. _`qmi_send_response.return`:

Return
------

0 on success, negative errno on failure.

.. _`qmi_send_indication`:

qmi_send_indication
===================

.. c:function:: ssize_t qmi_send_indication(struct qmi_handle *qmi, struct sockaddr_qrtr *sq, int msg_id, size_t len, struct qmi_elem_info *ei, const void *c_struct)

    send an indication QMI message

    :param struct qmi_handle \*qmi:
        QMI client handle

    :param struct sockaddr_qrtr \*sq:
        destination sockaddr

    :param int msg_id:
        message id

    :param size_t len:
        max length of the QMI message

    :param struct qmi_elem_info \*ei:
        QMI message description

    :param const void \*c_struct:
        object to be encoded

.. _`qmi_send_indication.return`:

Return
------

0 on success, negative errno on failure.

.. This file was automatic generated / don't edit.

