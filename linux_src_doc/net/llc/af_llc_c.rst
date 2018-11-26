.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/af_llc.c

.. _`llc_ui_next_link_no`:

llc_ui_next_link_no
===================

.. c:function:: u16 llc_ui_next_link_no(int sap)

    return the next unused link number for a sap

    :param sap:
        Address of sap to get link number from.
    :type sap: int

.. _`llc_ui_next_link_no.description`:

Description
-----------

Return the next unused link number for a given sap.

.. _`llc_proto_type`:

llc_proto_type
==============

.. c:function:: __be16 llc_proto_type(u16 arphrd)

    return eth protocol for ARP header type

    :param arphrd:
        ARP header type.
    :type arphrd: u16

.. _`llc_proto_type.description`:

Description
-----------

Given an ARP header type return the corresponding ethernet protocol.

.. _`llc_ui_addr_null`:

llc_ui_addr_null
================

.. c:function:: u8 llc_ui_addr_null(struct sockaddr_llc *addr)

    determines if a address structure is null

    :param addr:
        Address to test if null.
    :type addr: struct sockaddr_llc \*

.. _`llc_ui_header_len`:

llc_ui_header_len
=================

.. c:function:: u8 llc_ui_header_len(struct sock *sk, struct sockaddr_llc *addr)

    return length of llc header based on operation

    :param sk:
        Socket which contains a valid llc socket type.
    :type sk: struct sock \*

    :param addr:
        Complete sockaddr_llc structure received from the user.
    :type addr: struct sockaddr_llc \*

.. _`llc_ui_header_len.description`:

Description
-----------

Provide the length of the llc header depending on what kind of
operation the user would like to perform and the type of socket.
Returns the correct llc header length.

.. _`llc_ui_send_data`:

llc_ui_send_data
================

.. c:function:: int llc_ui_send_data(struct sock* sk, struct sk_buff *skb, int noblock)

    send data via reliable llc2 connection

    :param sk:
        Connection the socket is using.
    :type sk: struct sock\*

    :param skb:
        Data the user wishes to send.
    :type skb: struct sk_buff \*

    :param noblock:
        can we block waiting for data?
    :type noblock: int

.. _`llc_ui_send_data.description`:

Description
-----------

Send data via reliable llc2 connection.
Returns 0 upon success, non-zero if action did not succeed.

.. _`llc_ui_create`:

llc_ui_create
=============

.. c:function:: int llc_ui_create(struct net *net, struct socket *sock, int protocol, int kern)

    alloc and init a new llc_ui socket

    :param net:
        network namespace (must be default network)
    :type net: struct net \*

    :param sock:
        Socket to initialize and attach allocated sk to.
    :type sock: struct socket \*

    :param protocol:
        Unused.
    :type protocol: int

    :param kern:
        on behalf of kernel or userspace
    :type kern: int

.. _`llc_ui_create.description`:

Description
-----------

Allocate and initialize a new llc_ui socket, validate the user wants a
socket type we have available.
Returns 0 upon success, negative upon failure.

.. _`llc_ui_release`:

llc_ui_release
==============

.. c:function:: int llc_ui_release(struct socket *sock)

    shutdown socket

    :param sock:
        Socket to release.
    :type sock: struct socket \*

.. _`llc_ui_release.description`:

Description
-----------

Shutdown and deallocate an existing socket.

.. _`llc_ui_autoport`:

llc_ui_autoport
===============

.. c:function:: int llc_ui_autoport( void)

    provide dynamically allocate SAP number

    :param void:
        no arguments
    :type void: 

.. _`llc_ui_autoport.description`:

Description
-----------

Provide the caller with a dynamically allocated SAP number according
to the rules that are set in this function. Returns: 0, upon failure,
SAP number otherwise.

.. _`llc_ui_autobind`:

llc_ui_autobind
===============

.. c:function:: int llc_ui_autobind(struct socket *sock, struct sockaddr_llc *addr)

    automatically bind a socket to a sap

    :param sock:
        socket to bind
    :type sock: struct socket \*

    :param addr:
        address to connect to
    :type addr: struct sockaddr_llc \*

.. _`llc_ui_autobind.description`:

Description
-----------

Used by llc_ui_connect and llc_ui_sendmsg when the user hasn't
specifically used llc_ui_bind to bind to an specific address/sap

.. _`llc_ui_autobind.return`:

Return
------

0 upon success, negative otherwise.

.. _`llc_ui_bind`:

llc_ui_bind
===========

.. c:function:: int llc_ui_bind(struct socket *sock, struct sockaddr *uaddr, int addrlen)

    bind a socket to a specific address.

    :param sock:
        Socket to bind an address to.
    :type sock: struct socket \*

    :param uaddr:
        Address the user wants the socket bound to.
    :type uaddr: struct sockaddr \*

    :param addrlen:
        Length of the uaddr structure.
    :type addrlen: int

.. _`llc_ui_bind.description`:

Description
-----------

Bind a socket to a specific address. For llc a user is able to bind to
a specific sap only or mac + sap.
If the user desires to bind to a specific mac + sap, it is possible to
have multiple sap connections via multiple macs.
Bind and autobind for that matter must enforce the correct sap usage
otherwise all hell will break loose.

.. _`llc_ui_bind.return`:

Return
------

0 upon success, negative otherwise.

.. _`llc_ui_shutdown`:

llc_ui_shutdown
===============

.. c:function:: int llc_ui_shutdown(struct socket *sock, int how)

    shutdown a connect llc2 socket.

    :param sock:
        Socket to shutdown.
    :type sock: struct socket \*

    :param how:
        What part of the socket to shutdown.
    :type how: int

.. _`llc_ui_shutdown.description`:

Description
-----------

Shutdown a connected llc2 socket. Currently this function only supports
shutting down both sends and receives (2), we could probably make this
function such that a user can shutdown only half the connection but not
right now.

.. _`llc_ui_shutdown.return`:

Return
------

0 upon success, negative otherwise.

.. _`llc_ui_connect`:

llc_ui_connect
==============

.. c:function:: int llc_ui_connect(struct socket *sock, struct sockaddr *uaddr, int addrlen, int flags)

    Connect to a remote llc2 mac + sap.

    :param sock:
        Socket which will be connected to the remote destination.
    :type sock: struct socket \*

    :param uaddr:
        Remote and possibly the local address of the new connection.
    :type uaddr: struct sockaddr \*

    :param addrlen:
        Size of uaddr structure.
    :type addrlen: int

    :param flags:
        Operational flags specified by the user.
    :type flags: int

.. _`llc_ui_connect.description`:

Description
-----------

Connect to a remote llc2 mac + sap. The caller must specify the
destination mac and address to connect to. If the user hasn't previously
called bind(2) with a smac the address of the first interface of the
specified arp type will be used.
This function will autobind if user did not previously call bind.

.. _`llc_ui_connect.return`:

Return
------

0 upon success, negative otherwise.

.. _`llc_ui_listen`:

llc_ui_listen
=============

.. c:function:: int llc_ui_listen(struct socket *sock, int backlog)

    allow a normal socket to accept incoming connections

    :param sock:
        Socket to allow incoming connections on.
    :type sock: struct socket \*

    :param backlog:
        Number of connections to queue.
    :type backlog: int

.. _`llc_ui_listen.description`:

Description
-----------

Allow a normal socket to accept incoming connections.
Returns 0 upon success, negative otherwise.

.. _`llc_ui_accept`:

llc_ui_accept
=============

.. c:function:: int llc_ui_accept(struct socket *sock, struct socket *newsock, int flags, bool kern)

    accept a new incoming connection.

    :param sock:
        Socket which connections arrive on.
    :type sock: struct socket \*

    :param newsock:
        Socket to move incoming connection to.
    :type newsock: struct socket \*

    :param flags:
        User specified operational flags.
    :type flags: int

    :param kern:
        If the socket is kernel internal
    :type kern: bool

.. _`llc_ui_accept.description`:

Description
-----------

Accept a new incoming connection.
Returns 0 upon success, negative otherwise.

.. _`llc_ui_recvmsg`:

llc_ui_recvmsg
==============

.. c:function:: int llc_ui_recvmsg(struct socket *sock, struct msghdr *msg, size_t len, int flags)

    copy received data to the socket user.

    :param sock:
        Socket to copy data from.
    :type sock: struct socket \*

    :param msg:
        Various user space related information.
    :type msg: struct msghdr \*

    :param len:
        Size of user buffer.
    :type len: size_t

    :param flags:
        User specified flags.
    :type flags: int

.. _`llc_ui_recvmsg.description`:

Description
-----------

Copy received data to the socket user.
Returns non-negative upon success, negative otherwise.

.. _`llc_ui_sendmsg`:

llc_ui_sendmsg
==============

.. c:function:: int llc_ui_sendmsg(struct socket *sock, struct msghdr *msg, size_t len)

    Transmit data provided by the socket user.

    :param sock:
        Socket to transmit data from.
    :type sock: struct socket \*

    :param msg:
        Various user related information.
    :type msg: struct msghdr \*

    :param len:
        Length of data to transmit.
    :type len: size_t

.. _`llc_ui_sendmsg.description`:

Description
-----------

Transmit data provided by the socket user.
Returns non-negative upon success, negative otherwise.

.. _`llc_ui_getname`:

llc_ui_getname
==============

.. c:function:: int llc_ui_getname(struct socket *sock, struct sockaddr *uaddr, int peer)

    return the address info of a socket

    :param sock:
        Socket to get address of.
    :type sock: struct socket \*

    :param uaddr:
        Address structure to return information.
    :type uaddr: struct sockaddr \*

    :param peer:
        Does user want local or remote address information.
    :type peer: int

.. _`llc_ui_getname.description`:

Description
-----------

Return the address information of a socket.

.. _`llc_ui_ioctl`:

llc_ui_ioctl
============

.. c:function:: int llc_ui_ioctl(struct socket *sock, unsigned int cmd, unsigned long arg)

    io controls for PF_LLC

    :param sock:
        Socket to get/set info
    :type sock: struct socket \*

    :param cmd:
        command
    :type cmd: unsigned int

    :param arg:
        optional argument for cmd
    :type arg: unsigned long

.. _`llc_ui_ioctl.description`:

Description
-----------

get/set info on llc sockets

.. _`llc_ui_setsockopt`:

llc_ui_setsockopt
=================

.. c:function:: int llc_ui_setsockopt(struct socket *sock, int level, int optname, char __user *optval, unsigned int optlen)

    set various connection specific parameters.

    :param sock:
        Socket to set options on.
    :type sock: struct socket \*

    :param level:
        Socket level user is requesting operations on.
    :type level: int

    :param optname:
        Operation name.
    :type optname: int

    :param optval:
        User provided operation data.
    :type optval: char __user \*

    :param optlen:
        Length of optval.
    :type optlen: unsigned int

.. _`llc_ui_setsockopt.description`:

Description
-----------

Set various connection specific parameters.

.. _`llc_ui_getsockopt`:

llc_ui_getsockopt
=================

.. c:function:: int llc_ui_getsockopt(struct socket *sock, int level, int optname, char __user *optval, int __user *optlen)

    get connection specific socket info

    :param sock:
        Socket to get information from.
    :type sock: struct socket \*

    :param level:
        Socket level user is requesting operations on.
    :type level: int

    :param optname:
        Operation name.
    :type optname: int

    :param optval:
        Variable to return operation data in.
    :type optval: char __user \*

    :param optlen:
        Length of optval.
    :type optlen: int __user \*

.. _`llc_ui_getsockopt.description`:

Description
-----------

Get connection specific socket information.

.. This file was automatic generated / don't edit.

