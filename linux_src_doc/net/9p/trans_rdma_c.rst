.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/9p/trans_rdma.c

.. _`p9_trans_rdma`:

struct p9_trans_rdma
====================

.. c:type:: struct p9_trans_rdma

    RDMA transport instance

.. _`p9_trans_rdma.definition`:

Definition
----------

.. code-block:: c

    struct p9_trans_rdma {
        enum {
            P9_RDMA_INIT,
            P9_RDMA_ADDR_RESOLVED,
            P9_RDMA_ROUTE_RESOLVED,
            P9_RDMA_CONNECTED,
            P9_RDMA_FLUSHING,
            P9_RDMA_CLOSING,
            P9_RDMA_CLOSED,
        } state;
        struct rdma_cm_id *cm_id;,
        struct ib_pd *pd;,
        struct ib_qp *qp;,
        struct ib_cq *cq;,
        long timeout;,
        bool privport;,
        u16 port;,
        int sq_depth;,
        struct semaphore sq_sem;,
        int rq_depth;,
        struct semaphore rq_sem;,
        atomic_t excess_rc;,
        struct sockaddr_in addr;,
        spinlock_t req_lock;,
        struct completion cm_done;,
    }

.. _`p9_trans_rdma.members`:

Members
-------

state
    tracks the transport state machine for connection setup and tear down

cm_id
    The RDMA CM ID

pd
    Protection Domain pointer

qp
    Queue Pair pointer

cq
    Completion Queue pointer

timeout
    Number of uSecs to wait for connection management events

privport
    Whether a privileged port may be used

port
    The port to use

sq_depth
    The depth of the Send Queue

sq_sem
    Semaphore for the SQ

rq_depth
    The depth of the Receive Queue.

rq_sem
    Semaphore for the RQ

excess_rc
    Amount of posted Receive Contexts without a pending request.
    See \ :c:func:`rdma_request`\ 

addr
    The remote peer's address

req_lock
    Protects the active request list

cm_done
    Completion event for connection management tracking

.. _`parse_opts`:

parse_opts
==========

.. c:function:: int parse_opts(char *params, struct p9_rdma_opts *opts)

    parse mount options into rdma options structure

    :param params:
        options string passed from mount
    :type params: char \*

    :param opts:
        rdma transport-specific structure to parse options into
    :type opts: struct p9_rdma_opts \*

.. _`parse_opts.description`:

Description
-----------

Returns 0 upon success, -ERRNO upon failure

.. _`alloc_rdma`:

alloc_rdma
==========

.. c:function:: struct p9_trans_rdma *alloc_rdma(struct p9_rdma_opts *opts)

    Allocate and initialize the rdma transport structure

    :param opts:
        Mount options structure
    :type opts: struct p9_rdma_opts \*

.. _`rdma_create_trans`:

rdma_create_trans
=================

.. c:function:: int rdma_create_trans(struct p9_client *client, const char *addr, char *args)

    Transport method for creating a transport instance

    :param client:
        client instance
    :type client: struct p9_client \*

    :param addr:
        IP address string
    :type addr: const char \*

    :param args:
        Mount options string
    :type args: char \*

.. _`p9_trans_rdma_init`:

p9_trans_rdma_init
==================

.. c:function:: int p9_trans_rdma_init( void)

    Register the 9P RDMA transport driver

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

