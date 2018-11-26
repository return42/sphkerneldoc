.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/backchannel_rqst.c

.. _`xprt_destroy_backchannel`:

xprt_destroy_backchannel
========================

.. c:function:: void xprt_destroy_backchannel(struct rpc_xprt *xprt, unsigned int max_reqs)

    Destroys the backchannel preallocated structures.

    :param xprt:
        the transport holding the preallocated strucures
        \ ``max_reqs``\     the maximum number of preallocated structures to destroy
    :type xprt: struct rpc_xprt \*

    :param max_reqs:
        *undescribed*
    :type max_reqs: unsigned int

.. _`xprt_destroy_backchannel.description`:

Description
-----------

Since these structures may have been allocated by multiple calls
to xprt_setup_backchannel, we only destroy up to the maximum number
of reqs specified by the caller.

.. This file was automatic generated / don't edit.

