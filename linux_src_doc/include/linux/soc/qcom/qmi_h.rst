.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/soc/qcom/qmi.h

.. _`qmi_elem_info`:

struct qmi_elem_info
====================

.. c:type:: struct qmi_elem_info

    describes how to encode a single QMI element

.. _`qmi_elem_info.definition`:

Definition
----------

.. code-block:: c

    struct qmi_elem_info {
        enum qmi_elem_type data_type;
        u32 elem_len;
        u32 elem_size;
        enum qmi_array_type array_type;
        u8 tlv_type;
        u32 offset;
        struct qmi_elem_info *ei_array;
    }

.. _`qmi_elem_info.members`:

Members
-------

data_type
    Data type of this element.

elem_len
    Array length of this element, if an array.

elem_size
    Size of a single instance of this data type.

array_type
    Array type of this element.

tlv_type
    QMI message specific type to identify which element
    is present in an incoming message.

offset
    Specifies the offset of the first instance of this
    element in the data structure.

ei_array
    Null-terminated array of \ ``qmi_elem_info``\  to describe nested
    structures.

.. _`qmi_service`:

struct qmi_service
==================

.. c:type:: struct qmi_service

    context to track lookup-results

.. _`qmi_service.definition`:

Definition
----------

.. code-block:: c

    struct qmi_service {
        unsigned int service;
        unsigned int version;
        unsigned int instance;
        unsigned int node;
        unsigned int port;
        void *priv;
        struct list_head list_node;
    }

.. _`qmi_service.members`:

Members
-------

service
    service type

version
    version of the \ ``service``\ 

instance
    instance id of the \ ``service``\ 

node
    node of the service

port
    port of the service

priv
    handle for client's use

list_node
    list_head for house keeping

.. _`qmi_ops`:

struct qmi_ops
==============

.. c:type:: struct qmi_ops

    callbacks for qmi_handle

.. _`qmi_ops.definition`:

Definition
----------

.. code-block:: c

    struct qmi_ops {
        int (*new_server)(struct qmi_handle *qmi, struct qmi_service *svc);
        void (*del_server)(struct qmi_handle *qmi, struct qmi_service *svc);
        void (*net_reset)(struct qmi_handle *qmi);
        void (*msg_handler)(struct qmi_handle *qmi, struct sockaddr_qrtr *sq, const void *data, size_t count);
        void (*bye)(struct qmi_handle *qmi, unsigned int node);
        void (*del_client)(struct qmi_handle *qmi, unsigned int node, unsigned int port);
    }

.. _`qmi_ops.members`:

Members
-------

new_server
    inform client of a new_server lookup-result, returning
    successfully from this call causes the library to call
    \ ``del_server``\  as the service is removed from the
    lookup-result. \ ``priv``\  of the qmi_service can be used by
    the client

del_server
    inform client of a del_server lookup-result

net_reset
    inform client that the name service was restarted and
    that and any state needs to be released

msg_handler
    invoked for incoming messages, allows a client to
    override the usual QMI message handler

bye
    inform a client that all clients from a node are gone

del_client
    inform a client that a particular client is gone

.. _`qmi_txn`:

struct qmi_txn
==============

.. c:type:: struct qmi_txn

    transaction context

.. _`qmi_txn.definition`:

Definition
----------

.. code-block:: c

    struct qmi_txn {
        struct qmi_handle *qmi;
        int id;
        struct mutex lock;
        struct completion completion;
        int result;
        struct qmi_elem_info *ei;
        void *dest;
    }

.. _`qmi_txn.members`:

Members
-------

qmi
    QMI handle this transaction is associated with

id
    transaction id

lock
    for synchronization between handler and waiter of messages

completion
    completion object as the transaction receives a response

result
    result code for the completed transaction

ei
    description of the QMI encoded response (optional)

dest
    destination buffer to decode message into (optional)

.. _`qmi_msg_handler`:

struct qmi_msg_handler
======================

.. c:type:: struct qmi_msg_handler

    description of QMI message handler

.. _`qmi_msg_handler.definition`:

Definition
----------

.. code-block:: c

    struct qmi_msg_handler {
        unsigned int type;
        unsigned int msg_id;
        struct qmi_elem_info *ei;
        size_t decoded_size;
        void (*fn)(struct qmi_handle *qmi, struct sockaddr_qrtr *sq, struct qmi_txn *txn, const void *decoded);
    }

.. _`qmi_msg_handler.members`:

Members
-------

type
    type of message

msg_id
    message id

ei
    description of the QMI encoded message

decoded_size
    size of the decoded object

fn
    function to invoke as the message is decoded

.. _`qmi_handle`:

struct qmi_handle
=================

.. c:type:: struct qmi_handle

    QMI context

.. _`qmi_handle.definition`:

Definition
----------

.. code-block:: c

    struct qmi_handle {
        struct socket *sock;
        struct mutex sock_lock;
        struct sockaddr_qrtr sq;
        struct work_struct work;
        struct workqueue_struct *wq;
        void *recv_buf;
        size_t recv_buf_size;
        struct list_head lookups;
        struct list_head lookup_results;
        struct list_head services;
        struct qmi_ops ops;
        struct idr txns;
        struct mutex txn_lock;
        const struct qmi_msg_handler *handlers;
    }

.. _`qmi_handle.members`:

Members
-------

sock
    socket handle

sock_lock
    synchronization of \ ``sock``\  modifications

sq
    sockaddr of \ ``sock``\ 

work
    work for handling incoming messages

wq
    workqueue to post \ ``work``\  on

recv_buf
    scratch buffer for handling incoming messages

recv_buf_size
    size of \ ``recv_buf``\ 

lookups
    list of registered lookup requests

lookup_results
    list of lookup-results advertised to the client

services
    list of registered services (by this client)

ops
    reference to callbacks

txns
    outstanding transactions

txn_lock
    lock for modifications of \ ``txns``\ 

handlers
    list of handlers for incoming messages

.. This file was automatic generated / don't edit.

