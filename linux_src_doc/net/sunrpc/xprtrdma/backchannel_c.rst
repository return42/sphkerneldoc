.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtrdma/backchannel.c

.. _`xprt_rdma_bc_setup`:

xprt_rdma_bc_setup
==================

.. c:function:: int xprt_rdma_bc_setup(struct rpc_xprt *xprt, unsigned int reqs)

    Pre-allocate resources for handling backchannel requests

    :param struct rpc_xprt \*xprt:
        transport associated with these backchannel resources

    :param unsigned int reqs:
        number of concurrent incoming requests to expect

.. _`xprt_rdma_bc_setup.description`:

Description
-----------

Returns 0 on success; otherwise a negative errno

.. _`xprt_rdma_bc_up`:

xprt_rdma_bc_up
===============

.. c:function:: int xprt_rdma_bc_up(struct svc_serv *serv, struct net *net)

    Create transport endpoint for backchannel service

    :param struct svc_serv \*serv:
        server endpoint

    :param struct net \*net:
        network namespace

.. _`xprt_rdma_bc_up.description`:

Description
-----------

The "xprt" is an implied argument: it supplies the name of the
backchannel transport class.

Returns zero on success, negative errno on failure

.. _`xprt_rdma_bc_maxpayload`:

xprt_rdma_bc_maxpayload
=======================

.. c:function:: size_t xprt_rdma_bc_maxpayload(struct rpc_xprt *xprt)

    Return maximum backchannel message size

    :param struct rpc_xprt \*xprt:
        transport

.. _`xprt_rdma_bc_maxpayload.description`:

Description
-----------

Returns maximum size, in bytes, of a backchannel message

.. _`xprt_rdma_bc_send_reply`:

xprt_rdma_bc_send_reply
=======================

.. c:function:: int xprt_rdma_bc_send_reply(struct rpc_rqst *rqst)

    marshal and send a backchannel reply

    :param struct rpc_rqst \*rqst:
        RPC rqst with a backchannel RPC reply in rq_snd_buf

.. _`xprt_rdma_bc_send_reply.description`:

Description
-----------

Caller holds the transport's write lock.

.. _`xprt_rdma_bc_send_reply.return`:

Return
------

%0 if the RPC message has been sent
\ ``-ENOTCONN``\  if the caller should reconnect and call again
\ ``-EIO``\  if a permanent error occurred and the request was not
sent. Do not try to send this message again.

.. _`xprt_rdma_bc_destroy`:

xprt_rdma_bc_destroy
====================

.. c:function:: void xprt_rdma_bc_destroy(struct rpc_xprt *xprt, unsigned int reqs)

    Release resources for handling backchannel requests

    :param struct rpc_xprt \*xprt:
        transport associated with these backchannel resources

    :param unsigned int reqs:
        number of incoming requests to destroy; ignored

.. _`xprt_rdma_bc_free_rqst`:

xprt_rdma_bc_free_rqst
======================

.. c:function:: void xprt_rdma_bc_free_rqst(struct rpc_rqst *rqst)

    Release a backchannel rqst

    :param struct rpc_rqst \*rqst:
        request to release

.. _`rpcrdma_bc_receive_call`:

rpcrdma_bc_receive_call
=======================

.. c:function:: void rpcrdma_bc_receive_call(struct rpcrdma_xprt *r_xprt, struct rpcrdma_rep *rep)

    Handle a backward direction call

    :param struct rpcrdma_xprt \*r_xprt:
        transport receiving the call

    :param struct rpcrdma_rep \*rep:
        receive buffer containing the call

.. _`rpcrdma_bc_receive_call.operational-assumptions`:

Operational assumptions
-----------------------

o Backchannel credits are ignored, just as the NFS server
forechannel currently does
o The ULP manages a replay cache (eg, NFSv4.1 sessions).
No replay detection is done at the transport level

.. This file was automatic generated / don't edit.

