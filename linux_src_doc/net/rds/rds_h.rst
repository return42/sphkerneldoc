.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rds/rds.h

.. _`rds_transport`:

struct rds_transport
====================

.. c:type:: struct rds_transport

    transport specific behavioural hooks

.. _`rds_transport.definition`:

Definition
----------

.. code-block:: c

    struct rds_transport {
        char t_name[TRANSNAMSIZ];
        struct list_head t_item;
        struct module *t_owner;
        unsigned int t_prefer_loopback:1, t_mp_capable:1;
        unsigned int t_type;
        int (*laddr_check)(struct net *net, __be32 addr);
        int (*conn_alloc)(struct rds_connection *conn, gfp_t gfp);
        void (*conn_free)(void *data);
        int (*conn_path_connect)(struct rds_conn_path *cp);
        void (*conn_path_shutdown)(struct rds_conn_path *conn);
        void (*xmit_path_prepare)(struct rds_conn_path *cp);
        void (*xmit_path_complete)(struct rds_conn_path *cp);
        int (*xmit)(struct rds_connection *conn, struct rds_message *rm, unsigned int hdr_off, unsigned int sg, unsigned int off);
        int (*xmit_rdma)(struct rds_connection *conn, struct rm_rdma_op *op);
        int (*xmit_atomic)(struct rds_connection *conn, struct rm_atomic_op *op);
        int (*recv_path)(struct rds_conn_path *cp);
        int (*inc_copy_to_user)(struct rds_incoming *inc, struct iov_iter *to);
        void (*inc_free)(struct rds_incoming *inc);
        int (*cm_handle_connect)(struct rdma_cm_id *cm_id, struct rdma_cm_event *event);
        int (*cm_initiate_connect)(struct rdma_cm_id *cm_id);
        void (*cm_connect_complete)(struct rds_connection *conn, struct rdma_cm_event *event);
        unsigned int (*stats_info_copy)(struct rds_info_iterator *iter, unsigned int avail);
        void (*exit)(void);
        void *(*get_mr)(struct scatterlist *sg, unsigned long nr_sg, struct rds_sock *rs, u32 *key_ret);
        void (*sync_mr)(void *trans_private, int direction);
        void (*free_mr)(void *trans_private, int invalidate);
        void (*flush_mrs)(void);
        bool (*t_unloading)(struct rds_connection *conn);
    }

.. _`rds_transport.members`:

Members
-------

t_name
    *undescribed*

t_item
    *undescribed*

t_owner
    *undescribed*

t_prefer_loopback
    *undescribed*

t_mp_capable
    *undescribed*

t_type
    *undescribed*

laddr_check
    *undescribed*

conn_alloc
    *undescribed*

conn_free
    *undescribed*

conn_path_connect
    *undescribed*

conn_path_shutdown
    *undescribed*

xmit_path_prepare
    *undescribed*

xmit_path_complete
    *undescribed*

xmit
    .xmit is called by \ :c:func:`rds_send_xmit`\  to tell the transport to send
    part of a message.  The caller serializes on the send_sem so this
    doesn't need to be reentrant for a given conn.  The header must be
    sent before the data payload.  .xmit must be prepared to send a
    message with no data payload.  .xmit should return the number of
    bytes that were sent down the connection, including header bytes.
    Returning 0 tells the caller that it doesn't need to perform any
    additional work now.  This is usually the case when the transport has
    filled the sending queue for its connection and will handle
    triggering the rds thread to continue the send when space becomes
    available.  Returning -EAGAIN tells the caller to retry the send
    immediately.  Returning -ENOMEM tells the caller to retry the send at
    some point in the future.

xmit_rdma
    *undescribed*

xmit_atomic
    *undescribed*

recv_path
    *undescribed*

inc_copy_to_user
    *undescribed*

inc_free
    *undescribed*

cm_handle_connect
    *undescribed*

cm_initiate_connect
    *undescribed*

cm_connect_complete
    *undescribed*

stats_info_copy
    *undescribed*

exit
    *undescribed*

get_mr
    *undescribed*

sync_mr
    *undescribed*

free_mr
    *undescribed*

flush_mrs
    *undescribed*

t_unloading
    *undescribed*

.. This file was automatic generated / don't edit.

