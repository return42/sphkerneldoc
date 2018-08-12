.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprt.c

.. _`xprt_register_transport`:

xprt_register_transport
=======================

.. c:function:: int xprt_register_transport(struct xprt_class *transport)

    register a transport implementation

    :param struct xprt_class \*transport:
        transport to register

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

    :param struct xprt_class \*transport:
        transport to unregister

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

    :param const char \*transport_name:
        transport to load

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

    :param struct rpc_xprt \*xprt:
        pointer to the target transport

    :param struct rpc_task \*task:
        task that is requesting access to the transport

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

    :param struct rpc_xprt \*xprt:
        transport with other tasks potentially waiting

    :param struct rpc_task \*task:
        task that is releasing access to the transport

.. _`xprt_release_xprt.description`:

Description
-----------

Note that "task" can be NULL.  No congestion control is provided.

.. _`xprt_release_xprt_cong`:

xprt_release_xprt_cong
======================

.. c:function:: void xprt_release_xprt_cong(struct rpc_xprt *xprt, struct rpc_task *task)

    allow other requests to use a transport

    :param struct rpc_xprt \*xprt:
        transport with other tasks potentially waiting

    :param struct rpc_task \*task:
        task that is releasing access to the transport

.. _`xprt_release_xprt_cong.description`:

Description
-----------

Note that "task" can be NULL.  Another task is awoken to use the
transport if the transport's congestion window allows it.

.. _`xprt_release_rqst_cong`:

xprt_release_rqst_cong
======================

.. c:function:: void xprt_release_rqst_cong(struct rpc_task *task)

    housekeeping when request is complete

    :param struct rpc_task \*task:
        RPC request that recently completed

.. _`xprt_release_rqst_cong.description`:

Description
-----------

Useful for transports that require congestion control.

.. _`xprt_adjust_cwnd`:

xprt_adjust_cwnd
================

.. c:function:: void xprt_adjust_cwnd(struct rpc_xprt *xprt, struct rpc_task *task, int result)

    adjust transport congestion window

    :param struct rpc_xprt \*xprt:
        pointer to xprt

    :param struct rpc_task \*task:
        recently completed RPC request used to adjust window

    :param int result:
        result code of completed RPC request

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

    :param struct rpc_xprt \*xprt:
        transport with waiting tasks

    :param int status:
        result code to plant in each task before waking it

.. _`xprt_wait_for_buffer_space`:

xprt_wait_for_buffer_space
==========================

.. c:function:: void xprt_wait_for_buffer_space(struct rpc_task *task, rpc_action action)

    wait for transport output buffer to clear

    :param struct rpc_task \*task:
        task to be put to sleep

    :param rpc_action action:
        function pointer to be executed after wait

.. _`xprt_wait_for_buffer_space.description`:

Description
-----------

Note that we only set the timer for the case of \ :c:func:`RPC_IS_SOFT`\ , since
we don't in general want to force a socket disconnection due to
an incomplete RPC call transmission.

.. _`xprt_write_space`:

xprt_write_space
================

.. c:function:: void xprt_write_space(struct rpc_xprt *xprt)

    wake the task waiting for transport output buffer space

    :param struct rpc_xprt \*xprt:
        transport with waiting tasks

.. _`xprt_write_space.description`:

Description
-----------

Can be called in a soft IRQ context, so xprt_write_space never sleeps.

.. _`xprt_set_retrans_timeout_def`:

xprt_set_retrans_timeout_def
============================

.. c:function:: void xprt_set_retrans_timeout_def(struct rpc_task *task)

    set a request's retransmit timeout

    :param struct rpc_task \*task:
        task whose timeout is to be set

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

    :param struct rpc_task \*task:
        task whose timeout is to be set

.. _`xprt_set_retrans_timeout_rtt.description`:

Description
-----------

Set a request's retransmit timeout using the RTT estimator.

.. _`xprt_adjust_timeout`:

xprt_adjust_timeout
===================

.. c:function:: int xprt_adjust_timeout(struct rpc_rqst *req)

    adjust timeout values for next retransmit

    :param struct rpc_rqst \*req:
        RPC request containing parameters to use for the adjustment

.. _`xprt_disconnect_done`:

xprt_disconnect_done
====================

.. c:function:: void xprt_disconnect_done(struct rpc_xprt *xprt)

    mark a transport as disconnected

    :param struct rpc_xprt \*xprt:
        transport to flag for disconnect

.. _`xprt_force_disconnect`:

xprt_force_disconnect
=====================

.. c:function:: void xprt_force_disconnect(struct rpc_xprt *xprt)

    force a transport to disconnect

    :param struct rpc_xprt \*xprt:
        transport to disconnect

.. _`xprt_conditional_disconnect`:

xprt_conditional_disconnect
===========================

.. c:function:: void xprt_conditional_disconnect(struct rpc_xprt *xprt, unsigned int cookie)

    force a transport to disconnect

    :param struct rpc_xprt \*xprt:
        transport to disconnect

    :param unsigned int cookie:
        'connection cookie'

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

    :param struct rpc_task \*task:
        RPC task that is requesting the connect

.. _`xprt_lookup_rqst`:

xprt_lookup_rqst
================

.. c:function:: struct rpc_rqst *xprt_lookup_rqst(struct rpc_xprt *xprt, __be32 xid)

    find an RPC request corresponding to an XID

    :param struct rpc_xprt \*xprt:
        transport on which the original request was transmitted

    :param __be32 xid:
        RPC XID of incoming reply

.. _`xprt_lookup_rqst.description`:

Description
-----------

Caller holds xprt->recv_lock.

.. _`xprt_pin_rqst`:

xprt_pin_rqst
=============

.. c:function:: void xprt_pin_rqst(struct rpc_rqst *req)

    Pin a request on the transport receive list

    :param struct rpc_rqst \*req:
        Request to pin

.. _`xprt_pin_rqst.description`:

Description
-----------

Caller must ensure this is atomic with the call to \ :c:func:`xprt_lookup_rqst`\ 
so should be holding the xprt transport lock.

.. _`xprt_unpin_rqst`:

xprt_unpin_rqst
===============

.. c:function:: void xprt_unpin_rqst(struct rpc_rqst *req)

    Unpin a request on the transport receive list

    :param struct rpc_rqst \*req:
        Request to pin

.. _`xprt_unpin_rqst.description`:

Description
-----------

Caller should be holding the xprt transport lock.

.. _`xprt_update_rtt`:

xprt_update_rtt
===============

.. c:function:: void xprt_update_rtt(struct rpc_task *task)

    Update RPC RTT statistics

    :param struct rpc_task \*task:
        RPC request that recently completed

.. _`xprt_update_rtt.description`:

Description
-----------

Caller holds xprt->recv_lock.

.. _`xprt_complete_rqst`:

xprt_complete_rqst
==================

.. c:function:: void xprt_complete_rqst(struct rpc_task *task, int copied)

    called when reply processing is complete

    :param struct rpc_task \*task:
        RPC request that recently completed

    :param int copied:
        actual number of bytes received from the transport

.. _`xprt_complete_rqst.description`:

Description
-----------

Caller holds xprt->recv_lock.

.. _`xprt_prepare_transmit`:

xprt_prepare_transmit
=====================

.. c:function:: bool xprt_prepare_transmit(struct rpc_task *task)

    reserve the transport before sending a request

    :param struct rpc_task \*task:
        RPC task about to send a request

.. _`xprt_transmit`:

xprt_transmit
=============

.. c:function:: void xprt_transmit(struct rpc_task *task)

    send an RPC request on a transport

    :param struct rpc_task \*task:
        controlling RPC task

.. _`xprt_transmit.description`:

Description
-----------

We have to copy the iovec because sendmsg fiddles with its contents.

.. _`xprt_reserve`:

xprt_reserve
============

.. c:function:: void xprt_reserve(struct rpc_task *task)

    allocate an RPC request slot

    :param struct rpc_task \*task:
        RPC task requesting a slot allocation

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

    :param struct rpc_task \*task:
        RPC task requesting a slot allocation

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

    :param struct rpc_task \*task:
        task which is finished with the slot

.. _`xprt_create_transport`:

xprt_create_transport
=====================

.. c:function:: struct rpc_xprt *xprt_create_transport(struct xprt_create *args)

    create an RPC transport

    :param struct xprt_create \*args:
        rpc transport creation arguments

.. _`xprt_destroy`:

xprt_destroy
============

.. c:function:: void xprt_destroy(struct rpc_xprt *xprt)

    destroy an RPC transport, killing off all requests.

    :param struct rpc_xprt \*xprt:
        transport to destroy

.. _`xprt_get`:

xprt_get
========

.. c:function:: struct rpc_xprt *xprt_get(struct rpc_xprt *xprt)

    return a reference to an RPC transport.

    :param struct rpc_xprt \*xprt:
        pointer to the transport

.. _`xprt_put`:

xprt_put
========

.. c:function:: void xprt_put(struct rpc_xprt *xprt)

    release a reference to an RPC transport.

    :param struct rpc_xprt \*xprt:
        pointer to the transport

.. This file was automatic generated / don't edit.

