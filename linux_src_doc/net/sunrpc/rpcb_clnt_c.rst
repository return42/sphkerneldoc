.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/rpcb_clnt.c

.. _`rpcb_register`:

rpcb_register
=============

.. c:function:: int rpcb_register(struct net *net, u32 prog, u32 vers, int prot, unsigned short port)

    set or unset a port registration with the local rpcbind svc

    :param net:
        target network namespace
    :type net: struct net \*

    :param prog:
        RPC program number to bind
    :type prog: u32

    :param vers:
        RPC version number to bind
    :type vers: u32

    :param prot:
        transport protocol to register
    :type prot: int

    :param port:
        port value to register
    :type port: unsigned short

.. _`rpcb_register.description`:

Description
-----------

Returns zero if the registration request was dispatched successfully
and the rpcbind daemon returned success.  Otherwise, returns an errno
value that reflects the nature of the error (request could not be
dispatched, timed out, or rpcbind returned an error).

RPC services invoke this function to advertise their contact
information via the system's rpcbind daemon.  RPC services
invoke this function once for each [program, version, transport]
tuple they wish to advertise.

Callers may also unregister RPC services that are no longer
available by setting the passed-in port to zero.  This removes
all registered transports for [program, version] from the local
rpcbind database.

This function uses rpcbind protocol version 2 to contact the
local rpcbind daemon.

Registration works over both AF_INET and AF_INET6, and services
registered via this function are advertised as available for any
address.  If the local rpcbind daemon is listening on AF_INET6,
services registered via this function will be advertised on
IN6ADDR_ANY (ie available for all AF_INET and AF_INET6
addresses).

.. _`rpcb_v4_register`:

rpcb_v4_register
================

.. c:function:: int rpcb_v4_register(struct net *net, const u32 program, const u32 version, const struct sockaddr *address, const char *netid)

    set or unset a port registration with the local rpcbind

    :param net:
        target network namespace
    :type net: struct net \*

    :param program:
        RPC program number of service to (un)register
    :type program: const u32

    :param version:
        RPC version number of service to (un)register
    :type version: const u32

    :param address:
        address family, IP address, and port to (un)register
    :type address: const struct sockaddr \*

    :param netid:
        netid of transport protocol to (un)register
    :type netid: const char \*

.. _`rpcb_v4_register.description`:

Description
-----------

Returns zero if the registration request was dispatched successfully
and the rpcbind daemon returned success.  Otherwise, returns an errno
value that reflects the nature of the error (request could not be
dispatched, timed out, or rpcbind returned an error).

RPC services invoke this function to advertise their contact
information via the system's rpcbind daemon.  RPC services
invoke this function once for each [program, version, address,
netid] tuple they wish to advertise.

Callers may also unregister RPC services that are registered at a
specific address by setting the port number in \ ``address``\  to zero.
They may unregister all registered protocol families at once for
a service by passing a NULL \ ``address``\  argument.  If \ ``netid``\  is ""
then all netids for [program, version, address] are unregistered.

This function uses rpcbind protocol version 4 to contact the
local rpcbind daemon.  The local rpcbind daemon must support
version 4 of the rpcbind protocol in order for these functions
to register a service successfully.

Supported netids include "udp" and "tcp" for UDP and TCP over
IPv4, and "udp6" and "tcp6" for UDP and TCP over IPv6,
respectively.

The contents of \ ``address``\  determine the address family and the
port to be registered.  The usual practice is to pass INADDR_ANY
as the raw address, but specifying a non-zero address is also
supported by this API if the caller wishes to advertise an RPC
service on a specific network interface.

Note that passing in INADDR_ANY does not create the same service
registration as IN6ADDR_ANY.  The former advertises an RPC
service on any IPv4 address, but not on IPv6.  The latter
advertises the service on all IPv4 and IPv6 addresses.

.. _`rpcb_getport_async`:

rpcb_getport_async
==================

.. c:function:: void rpcb_getport_async(struct rpc_task *task)

    obtain the port for a given RPC service on a given host

    :param task:
        task that is waiting for portmapper request
    :type task: struct rpc_task \*

.. _`rpcb_getport_async.description`:

Description
-----------

This one can be called for an ongoing RPC request, and can be used in
an async (rpciod) context.

.. This file was automatic generated / don't edit.

