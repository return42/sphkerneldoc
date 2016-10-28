.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/clnt.c

.. _`rpc_create`:

rpc_create
==========

.. c:function:: struct rpc_clnt *rpc_create(struct rpc_create_args *args)

    create an RPC client and transport with one call

    :param struct rpc_create_args \*args:
        rpc_clnt create argument structure

.. _`rpc_create.description`:

Description
-----------

Creates and initializes an RPC transport and an RPC client.

It can ping the server in order to determine if it is up, and to see if
it supports this program and version.  RPC_CLNT_CREATE_NOPING disables
this behavior so asynchronous tasks can also use rpc_create.

.. _`rpc_clone_client`:

rpc_clone_client
================

.. c:function:: struct rpc_clnt *rpc_clone_client(struct rpc_clnt *clnt)

    Clone an RPC client structure

    :param struct rpc_clnt \*clnt:
        RPC client whose parameters are copied

.. _`rpc_clone_client.description`:

Description
-----------

Returns a fresh RPC client or an ERR_PTR.

.. _`rpc_clone_client_set_auth`:

rpc_clone_client_set_auth
=========================

.. c:function:: struct rpc_clnt *rpc_clone_client_set_auth(struct rpc_clnt *clnt, rpc_authflavor_t flavor)

    Clone an RPC client structure and set its auth

    :param struct rpc_clnt \*clnt:
        RPC client whose parameters are copied

    :param rpc_authflavor_t flavor:
        security flavor for new client

.. _`rpc_clone_client_set_auth.description`:

Description
-----------

Returns a fresh RPC client or an ERR_PTR.

.. _`rpc_switch_client_transport`:

rpc_switch_client_transport
===========================

.. c:function:: int rpc_switch_client_transport(struct rpc_clnt *clnt, struct xprt_create *args, const struct rpc_timeout *timeout)

    switch the RPC transport on the fly

    :param struct rpc_clnt \*clnt:
        pointer to a struct rpc_clnt

    :param struct xprt_create \*args:
        pointer to the new transport arguments

    :param const struct rpc_timeout \*timeout:
        pointer to the new timeout parameters

.. _`rpc_switch_client_transport.description`:

Description
-----------

This function allows the caller to switch the RPC transport for the
rpc_clnt structure 'clnt' to allow it to connect to a mirrored NFS
server, for instance.  It assumes that the caller has ensured that
there are no active RPC tasks by using some form of locking.

Returns zero if "clnt" is now using the new xprt.  Otherwise a
negative errno is returned, and "clnt" continues to use the old
xprt.

.. _`rpc_clnt_iterate_for_each_xprt`:

rpc_clnt_iterate_for_each_xprt
==============================

.. c:function:: int rpc_clnt_iterate_for_each_xprt(struct rpc_clnt *clnt, int (*fn)(struct rpc_clnt *, struct rpc_xprt *, void *), void *data)

    Apply a function to all transports

    :param struct rpc_clnt \*clnt:
        pointer to client

    :param int (\*fn)(struct rpc_clnt \*, struct rpc_xprt \*, void \*):
        function to apply

    :param void \*data:
        void pointer to function data

.. _`rpc_clnt_iterate_for_each_xprt.description`:

Description
-----------

Iterates through the list of RPC transports currently attached to the
client and applies the function fn(clnt, xprt, data).

On error, the iteration stops, and the function returns the error value.

.. _`rpc_bind_new_program`:

rpc_bind_new_program
====================

.. c:function:: struct rpc_clnt *rpc_bind_new_program(struct rpc_clnt *old, const struct rpc_program *program, u32 vers)

    bind a new RPC program to an existing client

    :param struct rpc_clnt \*old:
        old rpc_client

    :param const struct rpc_program \*program:
        rpc program to set

    :param u32 vers:
        rpc program version

.. _`rpc_bind_new_program.description`:

Description
-----------

Clones the rpc client and sets up a new RPC program. This is mainly
of use for enabling different RPC programs to share the same transport.
The Sun NFSv2/v3 ACL protocol can do this.

.. _`rpc_run_task`:

rpc_run_task
============

.. c:function:: struct rpc_task *rpc_run_task(const struct rpc_task_setup *task_setup_data)

    Allocate a new RPC task, then run rpc_execute against it

    :param const struct rpc_task_setup \*task_setup_data:
        pointer to task initialisation data

.. _`rpc_call_sync`:

rpc_call_sync
=============

.. c:function:: int rpc_call_sync(struct rpc_clnt *clnt, const struct rpc_message *msg, int flags)

    Perform a synchronous RPC call

    :param struct rpc_clnt \*clnt:
        pointer to RPC client

    :param const struct rpc_message \*msg:
        RPC call parameters

    :param int flags:
        RPC call flags

.. _`rpc_call_async`:

rpc_call_async
==============

.. c:function:: int rpc_call_async(struct rpc_clnt *clnt, const struct rpc_message *msg, int flags, const struct rpc_call_ops *tk_ops, void *data)

    Perform an asynchronous RPC call

    :param struct rpc_clnt \*clnt:
        pointer to RPC client

    :param const struct rpc_message \*msg:
        RPC call parameters

    :param int flags:
        RPC call flags

    :param const struct rpc_call_ops \*tk_ops:
        RPC call ops

    :param void \*data:
        user call data

.. _`rpc_run_bc_task`:

rpc_run_bc_task
===============

.. c:function:: struct rpc_task *rpc_run_bc_task(struct rpc_rqst *req)

    Allocate a new RPC task for backchannel use, then run rpc_execute against it

    :param struct rpc_rqst \*req:
        RPC request

.. _`rpc_peeraddr`:

rpc_peeraddr
============

.. c:function:: size_t rpc_peeraddr(struct rpc_clnt *clnt, struct sockaddr *buf, size_t bufsize)

    extract remote peer address from clnt's xprt

    :param struct rpc_clnt \*clnt:
        RPC client structure

    :param struct sockaddr \*buf:
        target buffer

    :param size_t bufsize:
        length of target buffer

.. _`rpc_peeraddr.description`:

Description
-----------

Returns the number of bytes that are actually in the stored address.

.. _`rpc_peeraddr2str`:

rpc_peeraddr2str
================

.. c:function:: const char *rpc_peeraddr2str(struct rpc_clnt *clnt, enum rpc_display_format_t format)

    return remote peer address in printable format

    :param struct rpc_clnt \*clnt:
        RPC client structure

    :param enum rpc_display_format_t format:
        address format

.. _`rpc_peeraddr2str.description`:

Description
-----------

NB: the lifetime of the memory referenced by the returned pointer is
the same as the rpc_xprt itself.  As long as the caller uses this
pointer, it must hold the RCU read lock.

.. _`rpc_localaddr`:

rpc_localaddr
=============

.. c:function:: int rpc_localaddr(struct rpc_clnt *clnt, struct sockaddr *buf, size_t buflen)

    discover local endpoint address for an RPC client

    :param struct rpc_clnt \*clnt:
        RPC client structure

    :param struct sockaddr \*buf:
        target buffer

    :param size_t buflen:
        size of target buffer, in bytes

.. _`rpc_localaddr.description`:

Description
-----------

Returns zero and fills in "buf" and "buflen" if successful;
otherwise, a negative errno is returned.

This works even if the underlying transport is not currently connected,
or if the upper layer never previously provided a source address.

.. _`rpc_localaddr.the-result-of-this-function-call-is-transient`:

The result of this function call is transient
---------------------------------------------

multiple calls in
succession may give different results, depending on how local
networking configuration changes over time.

.. _`rpc_protocol`:

rpc_protocol
============

.. c:function:: int rpc_protocol(struct rpc_clnt *clnt)

    Get transport protocol number for an RPC client

    :param struct rpc_clnt \*clnt:
        RPC client to query

.. _`rpc_net_ns`:

rpc_net_ns
==========

.. c:function:: struct net *rpc_net_ns(struct rpc_clnt *clnt)

    Get the network namespace for this RPC client

    :param struct rpc_clnt \*clnt:
        RPC client to query

.. _`rpc_max_payload`:

rpc_max_payload
===============

.. c:function:: size_t rpc_max_payload(struct rpc_clnt *clnt)

    Get maximum payload size for a transport, in bytes

    :param struct rpc_clnt \*clnt:
        RPC client to query

.. _`rpc_max_payload.description`:

Description
-----------

For stream transports, this is one RPC record fragment (see RFC
1831), as we don't support multi-record requests yet.  For datagram
transports, this is the size of an IP packet minus the IP, UDP, and
RPC header sizes.

.. _`rpc_max_bc_payload`:

rpc_max_bc_payload
==================

.. c:function:: size_t rpc_max_bc_payload(struct rpc_clnt *clnt)

    Get maximum backchannel payload size, in bytes

    :param struct rpc_clnt \*clnt:
        RPC client to query

.. _`rpc_get_timeout`:

rpc_get_timeout
===============

.. c:function:: unsigned long rpc_get_timeout(struct rpc_clnt *clnt)

    Get timeout for transport in units of HZ

    :param struct rpc_clnt \*clnt:
        RPC client to query

.. _`rpc_force_rebind`:

rpc_force_rebind
================

.. c:function:: void rpc_force_rebind(struct rpc_clnt *clnt)

    force transport to check that remote port is unchanged

    :param struct rpc_clnt \*clnt:
        client to rebind

.. _`rpc_clnt_test_and_add_xprt`:

rpc_clnt_test_and_add_xprt
==========================

.. c:function:: int rpc_clnt_test_and_add_xprt(struct rpc_clnt *clnt, struct rpc_xprt_switch *xps, struct rpc_xprt *xprt, void *dummy)

    Test and add a new transport to a rpc_clnt

    :param struct rpc_clnt \*clnt:
        pointer to struct rpc_clnt

    :param struct rpc_xprt_switch \*xps:
        pointer to struct rpc_xprt_switch,

    :param struct rpc_xprt \*xprt:
        pointer struct rpc_xprt

    :param void \*dummy:
        unused

.. _`rpc_clnt_add_xprt`:

rpc_clnt_add_xprt
=================

.. c:function:: int rpc_clnt_add_xprt(struct rpc_clnt *clnt, struct xprt_create *xprtargs, int (*setup)(struct rpc_clnt *, struct rpc_xprt_switch *, struct rpc_xprt *, void *), void *data)

    Add a new transport to a rpc_clnt

    :param struct rpc_clnt \*clnt:
        pointer to struct rpc_clnt

    :param struct xprt_create \*xprtargs:
        pointer to struct xprt_create

    :param int (\*setup)(struct rpc_clnt \*, struct rpc_xprt_switch \*, struct rpc_xprt \*, void \*):
        callback to test and/or set up the connection

    :param void \*data:
        pointer to setup function data

.. _`rpc_clnt_add_xprt.description`:

Description
-----------

Creates a new transport using the parameters set in args and
adds it to clnt.
If ping is set, then test that connectivity succeeds before
adding the new transport.

.. This file was automatic generated / don't edit.

