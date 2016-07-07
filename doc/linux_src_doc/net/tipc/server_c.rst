.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/server.c

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
        struct tipc_server *server;
        struct work_struct rwork;
        int (* rx_action) (struct tipc_conn *con);
        void *usr_data;
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

rwork
    receive work item

rx_action
    what to do when connection socket is active

usr_data
    user-specified field

outqueue
    list of connection objects for its server

outqueue_lock
    control access to the outqueue

swork
    send work item

.. This file was automatic generated / don't edit.

