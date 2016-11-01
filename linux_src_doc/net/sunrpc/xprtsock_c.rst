.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sunrpc/xprtsock.c

.. _`xs_sendpages`:

xs_sendpages
============

.. c:function:: int xs_sendpages(struct socket *sock, struct sockaddr *addr, int addrlen, struct xdr_buf *xdr, unsigned int base, bool zerocopy, int *sent_p)

    write pages directly to a socket

    :param struct socket \*sock:
        socket to send on

    :param struct sockaddr \*addr:
        UDP only -- address of destination

    :param int addrlen:
        UDP only -- length of destination address

    :param struct xdr_buf \*xdr:
        buffer containing this request

    :param unsigned int base:
        starting position in the buffer

    :param bool zerocopy:
        true if it is safe to use \ :c:func:`sendpage`\ 

    :param int \*sent_p:
        return the total number of bytes successfully queued for sending

.. _`xs_nospace`:

xs_nospace
==========

.. c:function:: int xs_nospace(struct rpc_task *task)

    place task on wait queue if transmit was incomplete

    :param struct rpc_task \*task:
        task to put to sleep

.. _`xs_local_send_request`:

xs_local_send_request
=====================

.. c:function:: int xs_local_send_request(struct rpc_task *task)

    write an RPC request to an AF_LOCAL socket

    :param struct rpc_task \*task:
        RPC task that manages the state of an RPC request

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

.. c:function:: int xs_udp_send_request(struct rpc_task *task)

    write an RPC request to a UDP socket

    :param struct rpc_task \*task:
        address of RPC task that manages the state of an RPC request

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

.. c:function:: int xs_tcp_send_request(struct rpc_task *task)

    write an RPC request to a TCP socket

    :param struct rpc_task \*task:
        address of RPC task that manages the state of an RPC request

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

.. _`xs_tcp_release_xprt`:

xs_tcp_release_xprt
===================

.. c:function:: void xs_tcp_release_xprt(struct rpc_xprt *xprt, struct rpc_task *task)

    clean up after a tcp transmission

    :param struct rpc_xprt \*xprt:
        transport

    :param struct rpc_task \*task:
        rpc task

.. _`xs_tcp_release_xprt.description`:

Description
-----------

This cleans up if an error causes us to abort the transmission of a request.
In this case, the socket may need to be reset in order to avoid confusing
the server.

.. _`xs_error_report`:

xs_error_report
===============

.. c:function:: void xs_error_report(struct sock *sk)

    callback to handle TCP socket state errors

    :param struct sock \*sk:
        socket

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

    :param struct rpc_xprt \*xprt:
        transport

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

    :param struct rpc_xprt \*xprt:
        doomed transport

.. _`xs_local_data_read_skb`:

xs_local_data_read_skb
======================

.. c:function:: void xs_local_data_read_skb(struct rpc_xprt *xprt, struct sock *sk, struct sk_buff *skb)

    :param struct rpc_xprt \*xprt:
        transport

    :param struct sock \*sk:
        socket

    :param struct sk_buff \*skb:
        skbuff

.. _`xs_local_data_read_skb.description`:

Description
-----------

Currently this assumes we can read the whole reply in a single gulp.

.. _`xs_udp_data_read_skb`:

xs_udp_data_read_skb
====================

.. c:function:: void xs_udp_data_read_skb(struct rpc_xprt *xprt, struct sock *sk, struct sk_buff *skb)

    receive callback for UDP sockets

    :param struct rpc_xprt \*xprt:
        transport

    :param struct sock \*sk:
        socket

    :param struct sk_buff \*skb:
        skbuff

.. _`xs_data_ready`:

xs_data_ready
=============

.. c:function:: void xs_data_ready(struct sock *sk)

    "data ready" callback for UDP sockets

    :param struct sock \*sk:
        socket with data to read

.. _`xs_tcp_state_change`:

xs_tcp_state_change
===================

.. c:function:: void xs_tcp_state_change(struct sock *sk)

    callback to handle TCP socket state changes

    :param struct sock \*sk:
        socket whose state has changed

.. _`xs_udp_write_space`:

xs_udp_write_space
==================

.. c:function:: void xs_udp_write_space(struct sock *sk)

    callback invoked when socket buffer space becomes available

    :param struct sock \*sk:
        socket whose state has changed

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

    :param struct sock \*sk:
        socket whose state has changed

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

    :param struct rpc_xprt \*xprt:
        generic transport

    :param size_t sndsize:
        requested size of send buffer, in bytes

    :param size_t rcvsize:
        requested size of receive buffer, in bytes

.. _`xs_udp_set_buffer_size.description`:

Description
-----------

Set socket send and receive buffer size limits.

.. _`xs_udp_timer`:

xs_udp_timer
============

.. c:function:: void xs_udp_timer(struct rpc_xprt *xprt, struct rpc_task *task)

    called when a retransmit timeout occurs on a UDP transport

    :param struct rpc_xprt \*xprt:
        *undescribed*

    :param struct rpc_task \*task:
        task that timed out

.. _`xs_udp_timer.description`:

Description
-----------

Adjust the congestion window after a retransmit timeout has occurred.

.. _`xs_sock_set_reuseport`:

xs_sock_set_reuseport
=====================

.. c:function:: void xs_sock_set_reuseport(struct socket *sock)

    set the socket's port and address reuse options

    :param struct socket \*sock:
        socket

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

    :param struct rpc_xprt \*xprt:
        generic transport

    :param unsigned short port:
        new port number

.. _`xs_local_setup_socket`:

xs_local_setup_socket
=====================

.. c:function:: int xs_local_setup_socket(struct sock_xprt *transport)

    create AF_LOCAL socket, connect to a local endpoint

    :param struct sock_xprt \*transport:
        socket transport to connect

.. _`xs_enable_swap`:

xs_enable_swap
==============

.. c:function:: int xs_enable_swap(struct rpc_xprt *xprt)

    Tag this transport as being used for swap.

    :param struct rpc_xprt \*xprt:
        transport to tag

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

    :param struct rpc_xprt \*xprt:
        transport to tag

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

    :param struct rpc_xprt \*xprt:
        transport

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

    :param struct work_struct \*work:
        *undescribed*

.. _`xs_tcp_setup_socket.description`:

Description
-----------

Invoked by a work queue tasklet.

.. _`xs_connect`:

xs_connect
==========

.. c:function:: void xs_connect(struct rpc_xprt *xprt, struct rpc_task *task)

    connect a socket to a remote endpoint

    :param struct rpc_xprt \*xprt:
        pointer to transport structure

    :param struct rpc_task \*task:
        address of RPC task that manages state of connect request

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

    :param struct rpc_xprt \*xprt:
        rpc_xprt struct containing statistics

    :param struct seq_file \*seq:
        output file

.. _`xs_udp_print_stats`:

xs_udp_print_stats
==================

.. c:function:: void xs_udp_print_stats(struct rpc_xprt *xprt, struct seq_file *seq)

    display UDP socket-specifc stats

    :param struct rpc_xprt \*xprt:
        rpc_xprt struct containing statistics

    :param struct seq_file \*seq:
        output file

.. _`xs_tcp_print_stats`:

xs_tcp_print_stats
==================

.. c:function:: void xs_tcp_print_stats(struct rpc_xprt *xprt, struct seq_file *seq)

    display TCP socket-specifc stats

    :param struct rpc_xprt \*xprt:
        rpc_xprt struct containing statistics

    :param struct seq_file \*seq:
        output file

.. _`xs_setup_local`:

xs_setup_local
==============

.. c:function:: struct rpc_xprt *xs_setup_local(struct xprt_create *args)

    Set up transport to use an AF_LOCAL socket

    :param struct xprt_create \*args:
        rpc transport creation arguments

.. _`xs_setup_local.description`:

Description
-----------

AF_LOCAL is a "tpi_cots_ord" transport, just like TCP

.. _`xs_setup_udp`:

xs_setup_udp
============

.. c:function:: struct rpc_xprt *xs_setup_udp(struct xprt_create *args)

    Set up transport to use a UDP socket

    :param struct xprt_create \*args:
        rpc transport creation arguments

.. _`xs_setup_tcp`:

xs_setup_tcp
============

.. c:function:: struct rpc_xprt *xs_setup_tcp(struct xprt_create *args)

    Set up transport to use a TCP socket

    :param struct xprt_create \*args:
        rpc transport creation arguments

.. _`xs_setup_bc_tcp`:

xs_setup_bc_tcp
===============

.. c:function:: struct rpc_xprt *xs_setup_bc_tcp(struct xprt_create *args)

    Set up transport to use a TCP backchannel socket

    :param struct xprt_create \*args:
        rpc transport creation arguments

.. _`init_socket_xprt`:

init_socket_xprt
================

.. c:function:: int init_socket_xprt( void)

    set up xprtsock's sysctls, register with RPC client

    :param  void:
        no arguments

.. _`cleanup_socket_xprt`:

cleanup_socket_xprt
===================

.. c:function:: void cleanup_socket_xprt( void)

    remove xprtsock's sysctls, unregister

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

