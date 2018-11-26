.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprt.c

.. _`xprt_register_transport`:

xprt_register_transport
=======================

.. c:function:: int xprt_register_transport(struct xprt_class *transport)

    register a transport implementation

    :param transport:
        transport to register
    :type transport: struct xprt_class \*

.. _`xprt_register_transport.description`:

Description
-----------

If a transport implementation is loaded as a kernel module, it can
call this interface to make itself known to the RPC client.

.. _`xprt_register_transport.return`:

Return
------

0:           transport successfully registered
-EEXIST:     transport already registered
-EINVAL:     transport module being unloaded

.. _`xprt_unregister_transport`:

xprt_unregister_transport
=========================

.. c:function:: int xprt_unregister_transport(struct xprt_class *transport)

    unregister a transport implementation

    :param transport:
        transport to unregister
    :type transport: struct xprt_class \*

.. _`xprt_unregister_transport.return`:

Return
------

0:           transport successfully unregistered
-ENOENT:     transport never registered

.. _`xprt_load_transport`:

xprt_load_transport
===================

.. c:function:: int xprt_load_transport(const char *transport_name)

    load a transport implementation

    :param transport_name:
        transport to load
    :type transport_name: const char \*

.. _`xprt_load_transport.return`:

Return
------

0:           transport successfully loaded
-ENOENT:     transport module not available

.. _`xprt_reserve_xprt`:

xprt_reserve_xprt
=================

.. c:function:: int xprt_reserve_xprt(struct rpc_xprt *xprt, struct rpc_task *task)

    serialize write access to transports

    :param xprt:
        pointer to the target transport
    :type xprt: struct rpc_xprt \*

    :param task:
        task that is requesting access to the transport
    :type task: struct rpc_task \*

.. _`xprt_reserve_xprt.description`:

Description
-----------

This prevents mixing the payload of separate requests, and prevents
transport connects from colliding with writes.  No congestion control
is provided.

.. _`xprt_release_xprt`:

xprt_release_xprt
=================

.. c:function:: void xprt_release_xprt(struct rpc_xprt *xprt, struct rpc_task *task)

    allow other requests to use a transport

    :param xprt:
        transport with other tasks potentially waiting
    :type xprt: struct rpc_xprt \*

    :param task:
        task that is releasing access to the transport
    :type task: struct rpc_task \*

.. _`xprt_release_xprt.description`:

Description
-----------

Note that "task" can be NULL.  No congestion control is provided.

.. _`xprt_release_xprt_cong`:

xprt_release_xprt_cong
======================

.. c:function:: void xprt_release_xprt_cong(struct rpc_xprt *xprt, struct rpc_task *task)

    allow other requests to use a transport

    :param xprt:
        transport with other tasks potentially waiting
    :type xprt: struct rpc_xprt \*

    :param task:
        task that is releasing access to the transport
    :type task: struct rpc_task \*

.. _`xprt_release_xprt_cong.description`:

Description
-----------

Note that "task" can be NULL.  Another task is awoken to use the
transport if the transport's congestion window allows it.

.. _`xprt_request_get_cong`:

xprt_request_get_cong
=====================

.. c:function:: bool xprt_request_get_cong(struct rpc_xprt *xprt, struct rpc_rqst *req)

    Request congestion control credits

    :param xprt:
        pointer to transport
    :type xprt: struct rpc_xprt \*

    :param req:
        pointer to RPC request
    :type req: struct rpc_rqst \*

.. _`xprt_request_get_cong.description`:

Description
-----------

Useful for transports that require congestion control.

.. _`xprt_release_rqst_cong`:

xprt_release_rqst_cong
======================

.. c:function:: void xprt_release_rqst_cong(struct rpc_task *task)

    housekeeping when request is complete

    :param task:
        RPC request that recently completed
    :type task: struct rpc_task \*

.. _`xprt_release_rqst_cong.description`:

Description
-----------

Useful for transports that require congestion control.

.. _`xprt_adjust_cwnd`:

xprt_adjust_cwnd
================

.. c:function:: void xprt_adjust_cwnd(struct rpc_xprt *xprt, struct rpc_task *task, int result)

    adjust transport congestion window

    :param xprt:
        pointer to xprt
    :type xprt: struct rpc_xprt \*

    :param task:
        recently completed RPC request used to adjust window
    :type task: struct rpc_task \*

    :param result:
        result code of completed RPC request
    :type result: int

.. _`xprt_adjust_cwnd.description`:

Description
-----------

The transport code maintains an estimate on the maximum number of out-
standing RPC requests, using a smoothed version of the congestion
avoidance implemented in 44BSD. This is basically the Van Jacobson
congestion algorithm: If a retransmit occurs, the congestion window is
halved; otherwise, it is incremented by 1/cwnd when

     -       a reply is received and
     -       a full number of requests are outstanding and
     -       the congestion window hasn't been updated recently.

.. _`xprt_wake_pending_tasks`:

xprt_wake_pending_tasks
=======================

.. c:function:: void xprt_wake_pending_tasks(struct rpc_xprt *xprt, int status)

    wake all tasks on a transport's pending queue

    :param xprt:
        transport with waiting tasks
    :type xprt: struct rpc_xprt \*

    :param status:
        result code to plant in each task before waking it
    :type status: int

.. _`xprt_wait_for_buffer_space`:

xprt_wait_for_buffer_space
==========================

.. c:function:: void xprt_wait_for_buffer_space(struct rpc_xprt *xprt)

    wait for transport output buffer to clear

    :param xprt:
        transport
    :type xprt: struct rpc_xprt \*

.. _`xprt_wait_for_buffer_space.description`:

Description
-----------

Note that we only set the timer for the case of \ :c:func:`RPC_IS_SOFT`\ , since
we don't in general want to force a socket disconnection due to
an incomplete RPC call transmission.

.. _`xprt_write_space`:

xprt_write_space
================

.. c:function:: bool xprt_write_space(struct rpc_xprt *xprt)

    wake the task waiting for transport output buffer space

    :param xprt:
        transport with waiting tasks
    :type xprt: struct rpc_xprt \*

.. _`xprt_write_space.description`:

Description
-----------

Can be called in a soft IRQ context, so xprt_write_space never sleeps.

.. _`xprt_set_retrans_timeout_def`:

xprt_set_retrans_timeout_def
============================

.. c:function:: void xprt_set_retrans_timeout_def(struct rpc_task *task)

    set a request's retransmit timeout

    :param task:
        task whose timeout is to be set
    :type task: struct rpc_task \*

.. _`xprt_set_retrans_timeout_def.description`:

Description
-----------

Set a request's retransmit timeout based on the transport's
default timeout parameters.  Used by transports that don't adjust
the retransmit timeout based on round-trip time estimation.

.. _`xprt_set_retrans_timeout_rtt`:

xprt_set_retrans_timeout_rtt
============================

.. c:function:: void xprt_set_retrans_timeout_rtt(struct rpc_task *task)

    set a request's retransmit timeout

    :param task:
        task whose timeout is to be set
    :type task: struct rpc_task \*

.. _`xprt_set_retrans_timeout_rtt.description`:

Description
-----------

Set a request's retransmit timeout using the RTT estimator.

.. _`xprt_adjust_timeout`:

xprt_adjust_timeout
===================

.. c:function:: int xprt_adjust_timeout(struct rpc_rqst *req)

    adjust timeout values for next retransmit

    :param req:
        RPC request containing parameters to use for the adjustment
    :type req: struct rpc_rqst \*

.. _`xprt_disconnect_done`:

xprt_disconnect_done
====================

.. c:function:: void xprt_disconnect_done(struct rpc_xprt *xprt)

    mark a transport as disconnected

    :param xprt:
        transport to flag for disconnect
    :type xprt: struct rpc_xprt \*

.. _`xprt_force_disconnect`:

xprt_force_disconnect
=====================

.. c:function:: void xprt_force_disconnect(struct rpc_xprt *xprt)

    force a transport to disconnect

    :param xprt:
        transport to disconnect
    :type xprt: struct rpc_xprt \*

.. _`xprt_conditional_disconnect`:

xprt_conditional_disconnect
===========================

.. c:function:: void xprt_conditional_disconnect(struct rpc_xprt *xprt, unsigned int cookie)

    force a transport to disconnect

    :param xprt:
        transport to disconnect
    :type xprt: struct rpc_xprt \*

    :param cookie:
        'connection cookie'
    :type cookie: unsigned int

.. _`xprt_conditional_disconnect.description`:

Description
-----------

This attempts to break the connection if and only if 'cookie' matches
the current transport 'connection cookie'. It ensures that we don't
try to break the connection more than once when we need to retransmit
a batch of RPC requests.

.. _`xprt_connect`:

xprt_connect
============

.. c:function:: void xprt_connect(struct rpc_task *task)

    schedule a transport connect operation

    :param task:
        RPC task that is requesting the connect
    :type task: struct rpc_task \*

.. _`xprt_lookup_rqst`:

xprt_lookup_rqst
================

.. c:function:: struct rpc_rqst *xprt_lookup_rqst(struct rpc_xprt *xprt, __be32 xid)

    find an RPC request corresponding to an XID

    :param xprt:
        transport on which the original request was transmitted
    :type xprt: struct rpc_xprt \*

    :param xid:
        RPC XID of incoming reply
    :type xid: __be32

.. _`xprt_lookup_rqst.description`:

Description
-----------

Caller holds xprt->queue_lock.

.. _`xprt_pin_rqst`:

xprt_pin_rqst
=============

.. c:function:: void xprt_pin_rqst(struct rpc_rqst *req)

    Pin a request on the transport receive list

    :param req:
        Request to pin
    :type req: struct rpc_rqst \*

.. _`xprt_pin_rqst.description`:

Description
-----------

Caller must ensure this is atomic with the call to \ :c:func:`xprt_lookup_rqst`\ 
so should be holding the xprt receive lock.

.. _`xprt_unpin_rqst`:

xprt_unpin_rqst
===============

.. c:function:: void xprt_unpin_rqst(struct rpc_rqst *req)

    Unpin a request on the transport receive list

    :param req:
        Request to pin
    :type req: struct rpc_rqst \*

.. _`xprt_unpin_rqst.description`:

Description
-----------

Caller should be holding the xprt receive lock.

.. _`xprt_request_enqueue_receive`:

xprt_request_enqueue_receive
============================

.. c:function:: void xprt_request_enqueue_receive(struct rpc_task *task)

    Add an request to the receive queue

    :param task:
        RPC task
    :type task: struct rpc_task \*

.. _`xprt_request_dequeue_receive_locked`:

xprt_request_dequeue_receive_locked
===================================

.. c:function:: void xprt_request_dequeue_receive_locked(struct rpc_task *task)

    Remove a request from the receive queue

    :param task:
        RPC task
    :type task: struct rpc_task \*

.. _`xprt_request_dequeue_receive_locked.description`:

Description
-----------

Caller must hold xprt->queue_lock.

.. _`xprt_update_rtt`:

xprt_update_rtt
===============

.. c:function:: void xprt_update_rtt(struct rpc_task *task)

    Update RPC RTT statistics

    :param task:
        RPC request that recently completed
    :type task: struct rpc_task \*

.. _`xprt_update_rtt.description`:

Description
-----------

Caller holds xprt->queue_lock.

.. _`xprt_complete_rqst`:

xprt_complete_rqst
==================

.. c:function:: void xprt_complete_rqst(struct rpc_task *task, int copied)

    called when reply processing is complete

    :param task:
        RPC request that recently completed
    :type task: struct rpc_task \*

    :param copied:
        actual number of bytes received from the transport
    :type copied: int

.. _`xprt_complete_rqst.description`:

Description
-----------

Caller holds xprt->queue_lock.

.. _`xprt_request_wait_receive`:

xprt_request_wait_receive
=========================

.. c:function:: void xprt_request_wait_receive(struct rpc_task *task)

    wait for the reply to an RPC request

    :param task:
        RPC task about to send a request
    :type task: struct rpc_task \*

.. _`xprt_request_enqueue_transmit`:

xprt_request_enqueue_transmit
=============================

.. c:function:: void xprt_request_enqueue_transmit(struct rpc_task *task)

    queue a task for transmission

    :param task:
        pointer to rpc_task
    :type task: struct rpc_task \*

.. _`xprt_request_enqueue_transmit.description`:

Description
-----------

Add a task to the transmission queue.

.. _`xprt_request_dequeue_transmit_locked`:

xprt_request_dequeue_transmit_locked
====================================

.. c:function:: void xprt_request_dequeue_transmit_locked(struct rpc_task *task)

    remove a task from the transmission queue

    :param task:
        pointer to rpc_task
    :type task: struct rpc_task \*

.. _`xprt_request_dequeue_transmit_locked.description`:

Description
-----------

Remove a task from the transmission queue
Caller must hold xprt->queue_lock

.. _`xprt_request_dequeue_transmit`:

xprt_request_dequeue_transmit
=============================

.. c:function:: void xprt_request_dequeue_transmit(struct rpc_task *task)

    remove a task from the transmission queue

    :param task:
        pointer to rpc_task
    :type task: struct rpc_task \*

.. _`xprt_request_dequeue_transmit.description`:

Description
-----------

Remove a task from the transmission queue

.. _`xprt_request_prepare`:

xprt_request_prepare
====================

.. c:function:: void xprt_request_prepare(struct rpc_rqst *req)

    prepare an encoded request for transport

    :param req:
        pointer to rpc_rqst
    :type req: struct rpc_rqst \*

.. _`xprt_request_prepare.description`:

Description
-----------

Calls into the transport layer to do whatever is needed to prepare
the request for transmission or receive.

.. _`xprt_request_need_retransmit`:

xprt_request_need_retransmit
============================

.. c:function:: bool xprt_request_need_retransmit(struct rpc_task *task)

    Test if a task needs retransmission

    :param task:
        pointer to rpc_task
    :type task: struct rpc_task \*

.. _`xprt_request_need_retransmit.description`:

Description
-----------

Test for whether a connection breakage requires the task to retransmit

.. _`xprt_prepare_transmit`:

xprt_prepare_transmit
=====================

.. c:function:: bool xprt_prepare_transmit(struct rpc_task *task)

    reserve the transport before sending a request

    :param task:
        RPC task about to send a request
    :type task: struct rpc_task \*

.. _`xprt_request_transmit`:

xprt_request_transmit
=====================

.. c:function:: int xprt_request_transmit(struct rpc_rqst *req, struct rpc_task *snd_task)

    send an RPC request on a transport

    :param req:
        pointer to request to transmit
    :type req: struct rpc_rqst \*

    :param snd_task:
        RPC task that owns the transport lock
    :type snd_task: struct rpc_task \*

.. _`xprt_request_transmit.description`:

Description
-----------

This performs the transmission of a single request.
Note that if the request is not the same as snd_task, then it
does need to be pinned.
Returns '0' on success.

.. _`xprt_transmit`:

xprt_transmit
=============

.. c:function:: void xprt_transmit(struct rpc_task *task)

    send an RPC request on a transport

    :param task:
        controlling RPC task
    :type task: struct rpc_task \*

.. _`xprt_transmit.description`:

Description
-----------

Attempts to drain the transmit queue. On exit, either the transport
signalled an error that needs to be handled before transmission can
resume, or \ ``task``\  finished transmitting, and detected that it already
received a reply.

.. _`xprt_reserve`:

xprt_reserve
============

.. c:function:: void xprt_reserve(struct rpc_task *task)

    allocate an RPC request slot

    :param task:
        RPC task requesting a slot allocation
    :type task: struct rpc_task \*

.. _`xprt_reserve.description`:

Description
-----------

If the transport is marked as being congested, or if no more
slots are available, place the task on the transport's
backlog queue.

.. _`xprt_retry_reserve`:

xprt_retry_reserve
==================

.. c:function:: void xprt_retry_reserve(struct rpc_task *task)

    allocate an RPC request slot

    :param task:
        RPC task requesting a slot allocation
    :type task: struct rpc_task \*

.. _`xprt_retry_reserve.description`:

Description
-----------

If no more slots are available, place the task on the transport's
backlog queue.
Note that the only difference with xprt_reserve is that we now
ignore the value of the XPRT_CONGESTED flag.

.. _`xprt_release`:

xprt_release
============

.. c:function:: void xprt_release(struct rpc_task *task)

    release an RPC request slot

    :param task:
        task which is finished with the slot
    :type task: struct rpc_task \*

.. _`xprt_create_transport`:

xprt_create_transport
=====================

.. c:function:: struct rpc_xprt *xprt_create_transport(struct xprt_create *args)

    create an RPC transport

    :param args:
        rpc transport creation arguments
    :type args: struct xprt_create \*

.. _`xprt_destroy`:

xprt_destroy
============

.. c:function:: void xprt_destroy(struct rpc_xprt *xprt)

    destroy an RPC transport, killing off all requests.

    :param xprt:
        transport to destroy
    :type xprt: struct rpc_xprt \*

.. _`xprt_get`:

xprt_get
========

.. c:function:: struct rpc_xprt *xprt_get(struct rpc_xprt *xprt)

    return a reference to an RPC transport.

    :param xprt:
        pointer to the transport
    :type xprt: struct rpc_xprt \*

.. _`xprt_put`:

xprt_put
========

.. c:function:: void xprt_put(struct rpc_xprt *xprt)

    release a reference to an RPC transport.

    :param xprt:
        pointer to the transport
    :type xprt: struct rpc_xprt \*

.. This file was automatic generated / don't edit.

