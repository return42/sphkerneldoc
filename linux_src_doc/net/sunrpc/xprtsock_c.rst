.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtsock.c

.. _`xs_sendpages`:

xs_sendpages
============

.. c:function:: int xs_sendpages(struct socket *sock, struct sockaddr *addr, int addrlen, struct xdr_buf *xdr, unsigned int base, bool zerocopy, int *sent_p)

    write pages directly to a socket

    :param sock:
        socket to send on
    :type sock: struct socket \*

    :param addr:
        UDP only -- address of destination
    :type addr: struct sockaddr \*

    :param addrlen:
        UDP only -- length of destination address
    :type addrlen: int

    :param xdr:
        buffer containing this request
    :type xdr: struct xdr_buf \*

    :param base:
        starting position in the buffer
    :type base: unsigned int

    :param zerocopy:
        true if it is safe to use \ :c:func:`sendpage`\ 
    :type zerocopy: bool

    :param sent_p:
        return the total number of bytes successfully queued for sending
    :type sent_p: int \*

.. _`xs_nospace`:

xs_nospace
==========

.. c:function:: int xs_nospace(struct rpc_rqst *req)

    handle transmit was incomplete

    :param req:
        pointer to RPC request
    :type req: struct rpc_rqst \*

.. _`xs_local_send_request`:

xs_local_send_request
=====================

.. c:function:: int xs_local_send_request(struct rpc_rqst *req)

    write an RPC request to an AF_LOCAL socket

    :param req:
        pointer to RPC request
    :type req: struct rpc_rqst \*

.. _`xs_local_send_request.return-values`:

Return values
-------------

0:    The request has been sent

.. _`xs_local_send_request.eagain`:

EAGAIN
------

The socket was blocked, please call again later to
complete the request

.. _`xs_local_send_request.enotconn`:

ENOTCONN
--------

Caller needs to invoke connect logic then call again

.. _`xs_local_send_request.other`:

other
-----

Some other error occured, the request was not sent

.. _`xs_udp_send_request`:

xs_udp_send_request
===================

.. c:function:: int xs_udp_send_request(struct rpc_rqst *req)

    write an RPC request to a UDP socket

    :param req:
        pointer to RPC request
    :type req: struct rpc_rqst \*

.. _`xs_udp_send_request.return-values`:

Return values
-------------

0:    The request has been sent

.. _`xs_udp_send_request.eagain`:

EAGAIN
------

The socket was blocked, please call again later to
complete the request

.. _`xs_udp_send_request.enotconn`:

ENOTCONN
--------

Caller needs to invoke connect logic then call again

.. _`xs_udp_send_request.other`:

other
-----

Some other error occurred, the request was not sent

.. _`xs_tcp_send_request`:

xs_tcp_send_request
===================

.. c:function:: int xs_tcp_send_request(struct rpc_rqst *req)

    write an RPC request to a TCP socket

    :param req:
        pointer to RPC request
    :type req: struct rpc_rqst \*

.. _`xs_tcp_send_request.return-values`:

Return values
-------------

0:    The request has been sent

.. _`xs_tcp_send_request.eagain`:

EAGAIN
------

The socket was blocked, please call again later to
complete the request

.. _`xs_tcp_send_request.enotconn`:

ENOTCONN
--------

Caller needs to invoke connect logic then call again

.. _`xs_tcp_send_request.other`:

other
-----

Some other error occurred, the request was not sent

.. _`xs_tcp_send_request.xxx`:

XXX
---

In the case of soft timeouts, should we eventually give up
if sendmsg is not able to make progress?

.. _`xs_error_report`:

xs_error_report
===============

.. c:function:: void xs_error_report(struct sock *sk)

    callback to handle TCP socket state errors

    :param sk:
        socket
    :type sk: struct sock \*

.. _`xs_error_report.note`:

Note
----

we don't call \ :c:func:`sock_error`\  since there may be a rpc_task
using the socket, and so we don't want to clear sk->sk_err.

.. _`xs_close`:

xs_close
========

.. c:function:: void xs_close(struct rpc_xprt *xprt)

    close a socket

    :param xprt:
        transport
    :type xprt: struct rpc_xprt \*

.. _`xs_close.description`:

Description
-----------

This is used when all requests are complete; ie, no DRC state remains
on the server we want to save.

The caller \_must\_ be holding XPRT_LOCKED in order to avoid issues with
\ :c:func:`xs_reset_transport`\  zeroing the socket from underneath a writer.

.. _`xs_destroy`:

xs_destroy
==========

.. c:function:: void xs_destroy(struct rpc_xprt *xprt)

    prepare to shutdown a transport

    :param xprt:
        doomed transport
    :type xprt: struct rpc_xprt \*

.. _`xs_udp_data_read_skb`:

xs_udp_data_read_skb
====================

.. c:function:: void xs_udp_data_read_skb(struct rpc_xprt *xprt, struct sock *sk, struct sk_buff *skb)

    receive callback for UDP sockets

    :param xprt:
        transport
    :type xprt: struct rpc_xprt \*

    :param sk:
        socket
    :type sk: struct sock \*

    :param skb:
        skbuff
    :type skb: struct sk_buff \*

.. _`xs_data_ready`:

xs_data_ready
=============

.. c:function:: void xs_data_ready(struct sock *sk)

    "data ready" callback for UDP sockets

    :param sk:
        socket with data to read
    :type sk: struct sock \*

.. _`xs_tcp_state_change`:

xs_tcp_state_change
===================

.. c:function:: void xs_tcp_state_change(struct sock *sk)

    callback to handle TCP socket state changes

    :param sk:
        socket whose state has changed
    :type sk: struct sock \*

.. _`xs_udp_write_space`:

xs_udp_write_space
==================

.. c:function:: void xs_udp_write_space(struct sock *sk)

    callback invoked when socket buffer space becomes available

    :param sk:
        socket whose state has changed
    :type sk: struct sock \*

.. _`xs_udp_write_space.description`:

Description
-----------

Called when more output buffer space is available for this socket.
We try not to wake our writers until they can make "significant"
progress, otherwise we'll waste resources thrashing kernel_sendmsg
with a bunch of small requests.

.. _`xs_tcp_write_space`:

xs_tcp_write_space
==================

.. c:function:: void xs_tcp_write_space(struct sock *sk)

    callback invoked when socket buffer space becomes available

    :param sk:
        socket whose state has changed
    :type sk: struct sock \*

.. _`xs_tcp_write_space.description`:

Description
-----------

Called when more output buffer space is available for this socket.
We try not to wake our writers until they can make "significant"
progress, otherwise we'll waste resources thrashing kernel_sendmsg
with a bunch of small requests.

.. _`xs_udp_set_buffer_size`:

xs_udp_set_buffer_size
======================

.. c:function:: void xs_udp_set_buffer_size(struct rpc_xprt *xprt, size_t sndsize, size_t rcvsize)

    set send and receive limits

    :param xprt:
        generic transport
    :type xprt: struct rpc_xprt \*

    :param sndsize:
        requested size of send buffer, in bytes
    :type sndsize: size_t

    :param rcvsize:
        requested size of receive buffer, in bytes
    :type rcvsize: size_t

.. _`xs_udp_set_buffer_size.description`:

Description
-----------

Set socket send and receive buffer size limits.

.. _`xs_udp_timer`:

xs_udp_timer
============

.. c:function:: void xs_udp_timer(struct rpc_xprt *xprt, struct rpc_task *task)

    called when a retransmit timeout occurs on a UDP transport

    :param xprt:
        *undescribed*
    :type xprt: struct rpc_xprt \*

    :param task:
        task that timed out
    :type task: struct rpc_task \*

.. _`xs_udp_timer.description`:

Description
-----------

Adjust the congestion window after a retransmit timeout has occurred.

.. _`xs_sock_set_reuseport`:

xs_sock_set_reuseport
=====================

.. c:function:: void xs_sock_set_reuseport(struct socket *sock)

    set the socket's port and address reuse options

    :param sock:
        socket
    :type sock: struct socket \*

.. _`xs_sock_set_reuseport.description`:

Description
-----------

Note that this function has to be called on all sockets that share the
same port, and it must be called before binding.

.. _`xs_set_port`:

xs_set_port
===========

.. c:function:: void xs_set_port(struct rpc_xprt *xprt, unsigned short port)

    reset the port number in the remote endpoint address

    :param xprt:
        generic transport
    :type xprt: struct rpc_xprt \*

    :param port:
        new port number
    :type port: unsigned short

.. _`xs_local_setup_socket`:

xs_local_setup_socket
=====================

.. c:function:: int xs_local_setup_socket(struct sock_xprt *transport)

    create AF_LOCAL socket, connect to a local endpoint

    :param transport:
        socket transport to connect
    :type transport: struct sock_xprt \*

.. _`xs_enable_swap`:

xs_enable_swap
==============

.. c:function:: int xs_enable_swap(struct rpc_xprt *xprt)

    Tag this transport as being used for swap.

    :param xprt:
        transport to tag
    :type xprt: struct rpc_xprt \*

.. _`xs_enable_swap.description`:

Description
-----------

Take a reference to this transport on behalf of the rpc_clnt, and
optionally mark it for swapping if it wasn't already.

.. _`xs_disable_swap`:

xs_disable_swap
===============

.. c:function:: void xs_disable_swap(struct rpc_xprt *xprt)

    Untag this transport as being used for swap.

    :param xprt:
        transport to tag
    :type xprt: struct rpc_xprt \*

.. _`xs_disable_swap.description`:

Description
-----------

Drop a "swapper" reference to this xprt on behalf of the rpc_clnt. If the
swapper refcount goes to 0, untag the socket as a memalloc socket.

.. _`xs_tcp_shutdown`:

xs_tcp_shutdown
===============

.. c:function:: void xs_tcp_shutdown(struct rpc_xprt *xprt)

    gracefully shut down a TCP socket

    :param xprt:
        transport
    :type xprt: struct rpc_xprt \*

.. _`xs_tcp_shutdown.description`:

Description
-----------

Initiates a graceful shutdown of the TCP socket by calling the
equivalent of shutdown(SHUT_RDWR);

.. _`xs_tcp_setup_socket`:

xs_tcp_setup_socket
===================

.. c:function:: void xs_tcp_setup_socket(struct work_struct *work)

    create a TCP socket and connect to a remote endpoint

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`xs_tcp_setup_socket.description`:

Description
-----------

Invoked by a work queue tasklet.

.. _`xs_connect`:

xs_connect
==========

.. c:function:: void xs_connect(struct rpc_xprt *xprt, struct rpc_task *task)

    connect a socket to a remote endpoint

    :param xprt:
        pointer to transport structure
    :type xprt: struct rpc_xprt \*

    :param task:
        address of RPC task that manages state of connect request
    :type task: struct rpc_task \*

.. _`xs_connect.tcp`:

TCP
---

If the remote end dropped the connection, delay reconnecting.

UDP socket connects are synchronous, but we use a work queue anyway
to guarantee that even unprivileged user processes can set up a
socket on a privileged port.

If a UDP socket connect fails, the delay behavior here prevents
retry floods (hard mounts).

.. _`xs_local_print_stats`:

xs_local_print_stats
====================

.. c:function:: void xs_local_print_stats(struct rpc_xprt *xprt, struct seq_file *seq)

    display AF_LOCAL socket-specifc stats

    :param xprt:
        rpc_xprt struct containing statistics
    :type xprt: struct rpc_xprt \*

    :param seq:
        output file
    :type seq: struct seq_file \*

.. _`xs_udp_print_stats`:

xs_udp_print_stats
==================

.. c:function:: void xs_udp_print_stats(struct rpc_xprt *xprt, struct seq_file *seq)

    display UDP socket-specifc stats

    :param xprt:
        rpc_xprt struct containing statistics
    :type xprt: struct rpc_xprt \*

    :param seq:
        output file
    :type seq: struct seq_file \*

.. _`xs_tcp_print_stats`:

xs_tcp_print_stats
==================

.. c:function:: void xs_tcp_print_stats(struct rpc_xprt *xprt, struct seq_file *seq)

    display TCP socket-specifc stats

    :param xprt:
        rpc_xprt struct containing statistics
    :type xprt: struct rpc_xprt \*

    :param seq:
        output file
    :type seq: struct seq_file \*

.. _`xs_setup_local`:

xs_setup_local
==============

.. c:function:: struct rpc_xprt *xs_setup_local(struct xprt_create *args)

    Set up transport to use an AF_LOCAL socket

    :param args:
        rpc transport creation arguments
    :type args: struct xprt_create \*

.. _`xs_setup_local.description`:

Description
-----------

AF_LOCAL is a "tpi_cots_ord" transport, just like TCP

.. _`xs_setup_udp`:

xs_setup_udp
============

.. c:function:: struct rpc_xprt *xs_setup_udp(struct xprt_create *args)

    Set up transport to use a UDP socket

    :param args:
        rpc transport creation arguments
    :type args: struct xprt_create \*

.. _`xs_setup_tcp`:

xs_setup_tcp
============

.. c:function:: struct rpc_xprt *xs_setup_tcp(struct xprt_create *args)

    Set up transport to use a TCP socket

    :param args:
        rpc transport creation arguments
    :type args: struct xprt_create \*

.. _`xs_setup_bc_tcp`:

xs_setup_bc_tcp
===============

.. c:function:: struct rpc_xprt *xs_setup_bc_tcp(struct xprt_create *args)

    Set up transport to use a TCP backchannel socket

    :param args:
        rpc transport creation arguments
    :type args: struct xprt_create \*

.. _`init_socket_xprt`:

init_socket_xprt
================

.. c:function:: int init_socket_xprt( void)

    set up xprtsock's sysctls, register with RPC client

    :param void:
        no arguments
    :type void: 

.. _`cleanup_socket_xprt`:

cleanup_socket_xprt
===================

.. c:function:: void cleanup_socket_xprt( void)

    remove xprtsock's sysctls, unregister

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

