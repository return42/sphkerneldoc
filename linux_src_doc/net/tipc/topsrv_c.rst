.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/topsrv.c

.. _`tipc_topsrv`:

struct tipc_topsrv
==================

.. c:type:: struct tipc_topsrv

    TIPC server structure

.. _`tipc_topsrv.definition`:

Definition
----------

.. code-block:: c

    struct tipc_topsrv {
        struct idr conn_idr;
        spinlock_t idr_lock;
        int idr_in_use;
        struct net *net;
        struct work_struct awork;
        struct workqueue_struct *rcv_wq;
        struct workqueue_struct *send_wq;
        int max_rcvbuf_size;
        struct socket *listener;
        char name[TIPC_SERVER_NAME_LEN];
    }

.. _`tipc_topsrv.members`:

Members
-------

conn_idr
    identifier set of connection

idr_lock
    protect the connection identifier set

idr_in_use
    amount of allocated identifier entry

net
    network namspace instance

awork
    *undescribed*

rcv_wq
    receive workqueue

send_wq
    send workqueue

max_rcvbuf_size
    maximum permitted receive message length

listener
    *undescribed*

name
    server name

.. _`tipc_conn`:

struct tipc_conn
================

.. c:type:: struct tipc_conn

    TIPC connection structure

.. _`tipc_conn.definition`:

Definition
----------

.. code-block:: c

    struct tipc_conn {
        struct kref kref;
        int conid;
        struct socket *sock;
        unsigned long flags;
        struct tipc_topsrv *server;
        struct list_head sub_list;
        spinlock_t sub_lock;
        struct work_struct rwork;
        struct list_head outqueue;
        spinlock_t outqueue_lock;
        struct work_struct swork;
    }

.. _`tipc_conn.members`:

Members
-------

kref
    reference counter to connection object

conid
    connection identifier

sock
    socket handler associated with connection

flags
    indicates connection state

server
    pointer to connected server

sub_list
    lsit to all pertaing subscriptions

sub_lock
    lock protecting the subscription list

rwork
    receive work item

outqueue
    pointer to first outbound message in queue

outqueue_lock
    control access to the outqueue

swork
    send work item

.. This file was automatic generated / don't edit.

