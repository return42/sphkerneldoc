.. -*- coding: utf-8; mode: rst -*-

==================
backchannel_rqst.c
==================


.. _`xprt_destroy_backchannel`:

xprt_destroy_backchannel
========================

.. c:function:: void xprt_destroy_backchannel (struct rpc_xprt *xprt, unsigned int max_reqs)

    Destroys the backchannel preallocated structures.

    :param struct rpc_xprt \*xprt:
        the transport holding the preallocated strucures
        ``max_reqs``        the maximum number of preallocated structures to destroy

    :param unsigned int max_reqs:

        *undescribed*



.. _`xprt_destroy_backchannel.description`:

Description
-----------

Since these structures may have been allocated by multiple calls
to xprt_setup_backchannel, we only destroy up to the maximum number
of reqs specified by the caller.

