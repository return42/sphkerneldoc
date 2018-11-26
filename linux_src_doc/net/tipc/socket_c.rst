.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/socket.c

.. _`tipc_sock`:

struct tipc_sock
================

.. c:type:: struct tipc_sock

    TIPC socket structure

.. _`tipc_sock.definition`:

Definition
----------

.. code-block:: c

    struct tipc_sock {
        struct sock sk;
        u32 conn_type;
        u32 conn_instance;
        int published;
        u32 max_pkt;
        u32 portid;
        struct tipc_msg phdr;
        struct list_head cong_links;
        struct list_head publications;
        u32 pub_count;
        atomic_t dupl_rcvcnt;
        u16 conn_timeout;
        bool probe_unacked;
        u16 cong_link_cnt;
        u16 snt_unacked;
        u16 snd_win;
        u16 peer_caps;
        u16 rcv_unacked;
        u16 rcv_win;
        struct sockaddr_tipc peer;
        struct rhash_head node;
        struct tipc_mc_method mc_method;
        struct rcu_head rcu;
        struct tipc_group *group;
        bool group_is_open;
    }

.. _`tipc_sock.members`:

Members
-------

sk
    socket - interacts with 'port' and with user via the socket API

conn_type
    TIPC type used when connection was established

conn_instance
    TIPC instance used when connection was established

published
    non-zero if port has one or more associated names

max_pkt
    maximum packet size "hint" used when building messages sent by port

portid
    unique port identity in TIPC socket hash table

phdr
    preformatted message header used when sending messages
    #cong_links: list of congested links

cong_links
    *undescribed*

publications
    list of publications for port

pub_count
    total # of publications port has made during its lifetime

dupl_rcvcnt
    number of bytes counted twice, in both backlog and rcv queue

conn_timeout
    the time we can wait for an unresponded setup request

probe_unacked
    *undescribed*

cong_link_cnt
    number of congested links

snt_unacked
    # messages sent by socket, and not yet acked by peer

snd_win
    *undescribed*

peer_caps
    *undescribed*

rcv_unacked
    # messages read by user, but not yet acked back to peer

rcv_win
    *undescribed*

peer
    'connected' peer for dgram/rdm

node
    hash table node

mc_method
    cookie for use between socket and broadcast layer

rcu
    rcu struct for tipc_sock

group
    *undescribed*

group_is_open
    *undescribed*

.. _`tsk_advance_rx_queue`:

tsk_advance_rx_queue
====================

.. c:function:: void tsk_advance_rx_queue(struct sock *sk)

    discard first buffer in socket receive queue

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`tsk_advance_rx_queue.description`:

Description
-----------

Caller must hold socket lock

.. _`tsk_rej_rx_queue`:

tsk_rej_rx_queue
================

.. c:function:: void tsk_rej_rx_queue(struct sock *sk)

    reject all buffers in socket receive queue

    :param sk:
        *undescribed*
    :type sk: struct sock \*

.. _`tsk_rej_rx_queue.description`:

Description
-----------

Caller must hold socket lock

.. _`tipc_sk_create`:

tipc_sk_create
==============

.. c:function:: int tipc_sk_create(struct net *net, struct socket *sock, int protocol, int kern)

    create a TIPC socket

    :param net:
        network namespace (must be default network)
    :type net: struct net \*

    :param sock:
        pre-allocated socket structure
    :type sock: struct socket \*

    :param protocol:
        protocol indicator (must be 0)
    :type protocol: int

    :param kern:
        caused by kernel or by userspace?
    :type kern: int

.. _`tipc_sk_create.description`:

Description
-----------

This routine creates additional data structures used by the TIPC socket,
initializes them, and links them together.

Returns 0 on success, errno otherwise

.. _`tipc_release`:

tipc_release
============

.. c:function:: int tipc_release(struct socket *sock)

    destroy a TIPC socket

    :param sock:
        socket to destroy
    :type sock: struct socket \*

.. _`tipc_release.description`:

Description
-----------

This routine cleans up any messages that are still queued on the socket.
For DGRAM and RDM socket types, all queued messages are rejected.
For SEQPACKET and STREAM socket types, the first message is rejected
and any others are discarded.  (If the first message on a STREAM socket
is partially-read, it is discarded and the next one is rejected instead.)

.. _`tipc_release.note`:

NOTE
----

Rejected messages are not necessarily returned to the sender!  They
are returned or discarded according to the "destination droppable" setting
specified for the message by the sender.

Returns 0 on success, errno otherwise

.. _`tipc_bind`:

tipc_bind
=========

.. c:function:: int tipc_bind(struct socket *sock, struct sockaddr *uaddr, int uaddr_len)

    associate or disassocate TIPC name(s) with a socket

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param uaddr:
        socket address describing name(s) and desired operation
    :type uaddr: struct sockaddr \*

    :param uaddr_len:
        size of socket address data structure
    :type uaddr_len: int

.. _`tipc_bind.description`:

Description
-----------

Name and name sequence binding is indicated using a positive scope value;
a negative scope value unbinds the specified name.  Specifying no name
(i.e. a socket address length of 0) unbinds all names from the socket.

Returns 0 on success, errno otherwise

.. _`tipc_bind.note`:

NOTE
----

This routine doesn't need to take the socket lock since it doesn't
access any non-constant socket information.

.. _`tipc_getname`:

tipc_getname
============

.. c:function:: int tipc_getname(struct socket *sock, struct sockaddr *uaddr, int peer)

    get port ID of socket or peer socket

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param uaddr:
        area for returned socket address
    :type uaddr: struct sockaddr \*

    :param peer:
        0 = own ID, 1 = current peer ID, 2 = current/former peer ID
    :type peer: int

.. _`tipc_getname.description`:

Description
-----------

Returns 0 on success, errno otherwise

.. _`tipc_getname.note`:

NOTE
----

This routine doesn't need to take the socket lock since it only
accesses socket information that is unchanging (or which changes in
a completely predictable manner).

.. _`tipc_poll`:

tipc_poll
=========

.. c:function:: __poll_t tipc_poll(struct file *file, struct socket *sock, poll_table *wait)

    read and possibly block on pollmask

    :param file:
        file structure associated with the socket
    :type file: struct file \*

    :param sock:
        socket for which to calculate the poll bits
    :type sock: struct socket \*

    :param wait:
        ???
    :type wait: poll_table \*

.. _`tipc_poll.description`:

Description
-----------

Returns pollmask value

.. _`tipc_poll.commentary`:

COMMENTARY
----------

It appears that the usual socket locking mechanisms are not useful here
since the pollmask info is potentially out-of-date the moment this routine
exits.  TCP and other protocols seem to rely on higher level poll routines
to handle any preventable race conditions, so TIPC will do the same ...

.. _`tipc_poll.important`:

IMPORTANT
---------

The fact that a read or write operation is indicated does NOT
imply that the operation will succeed, merely that it should be performed
and will not block.

.. _`tipc_sendmcast`:

tipc_sendmcast
==============

.. c:function:: int tipc_sendmcast(struct socket *sock, struct tipc_name_seq *seq, struct msghdr *msg, size_t dlen, long timeout)

    send multicast message

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param seq:
        destination address
    :type seq: struct tipc_name_seq \*

    :param msg:
        message to send
    :type msg: struct msghdr \*

    :param dlen:
        length of data to send
    :type dlen: size_t

    :param timeout:
        timeout to wait for wakeup
    :type timeout: long

.. _`tipc_sendmcast.description`:

Description
-----------

Called from function \ :c:func:`tipc_sendmsg`\ , which has done all sanity checks
Returns the number of bytes sent on success, or errno

.. _`tipc_send_group_msg`:

tipc_send_group_msg
===================

.. c:function:: int tipc_send_group_msg(struct net *net, struct tipc_sock *tsk, struct msghdr *m, struct tipc_member *mb, u32 dnode, u32 dport, int dlen)

    send a message to a member in the group

    :param net:
        network namespace
    :type net: struct net \*

    :param tsk:
        *undescribed*
    :type tsk: struct tipc_sock \*

    :param m:
        message to send
    :type m: struct msghdr \*

    :param mb:
        group member
    :type mb: struct tipc_member \*

    :param dnode:
        destination node
    :type dnode: u32

    :param dport:
        destination port
    :type dport: u32

    :param dlen:
        total length of message data
    :type dlen: int

.. _`tipc_send_group_unicast`:

tipc_send_group_unicast
=======================

.. c:function:: int tipc_send_group_unicast(struct socket *sock, struct msghdr *m, int dlen, long timeout)

    send message to a member in the group

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param m:
        message to send
    :type m: struct msghdr \*

    :param dlen:
        total length of message data
    :type dlen: int

    :param timeout:
        timeout to wait for wakeup
    :type timeout: long

.. _`tipc_send_group_unicast.description`:

Description
-----------

Called from function \ :c:func:`tipc_sendmsg`\ , which has done all sanity checks
Returns the number of bytes sent on success, or errno

.. _`tipc_send_group_anycast`:

tipc_send_group_anycast
=======================

.. c:function:: int tipc_send_group_anycast(struct socket *sock, struct msghdr *m, int dlen, long timeout)

    send message to any member with given identity

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param m:
        message to send
    :type m: struct msghdr \*

    :param dlen:
        total length of message data
    :type dlen: int

    :param timeout:
        timeout to wait for wakeup
    :type timeout: long

.. _`tipc_send_group_anycast.description`:

Description
-----------

Called from function \ :c:func:`tipc_sendmsg`\ , which has done all sanity checks
Returns the number of bytes sent on success, or errno

.. _`tipc_send_group_bcast`:

tipc_send_group_bcast
=====================

.. c:function:: int tipc_send_group_bcast(struct socket *sock, struct msghdr *m, int dlen, long timeout)

    send message to all members in communication group

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param m:
        message to send
    :type m: struct msghdr \*

    :param dlen:
        total length of message data
    :type dlen: int

    :param timeout:
        timeout to wait for wakeup
    :type timeout: long

.. _`tipc_send_group_bcast.description`:

Description
-----------

Called from function \ :c:func:`tipc_sendmsg`\ , which has done all sanity checks
Returns the number of bytes sent on success, or errno

.. _`tipc_send_group_mcast`:

tipc_send_group_mcast
=====================

.. c:function:: int tipc_send_group_mcast(struct socket *sock, struct msghdr *m, int dlen, long timeout)

    send message to all members with given identity

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param m:
        message to send
    :type m: struct msghdr \*

    :param dlen:
        total length of message data
    :type dlen: int

    :param timeout:
        timeout to wait for wakeup
    :type timeout: long

.. _`tipc_send_group_mcast.description`:

Description
-----------

Called from function \ :c:func:`tipc_sendmsg`\ , which has done all sanity checks
Returns the number of bytes sent on success, or errno

.. _`tipc_sk_mcast_rcv`:

tipc_sk_mcast_rcv
=================

.. c:function:: void tipc_sk_mcast_rcv(struct net *net, struct sk_buff_head *arrvq, struct sk_buff_head *inputq)

    Deliver multicast messages to all destination sockets

    :param net:
        *undescribed*
    :type net: struct net \*

    :param arrvq:
        queue with arriving messages, to be cloned after destination lookup
    :type arrvq: struct sk_buff_head \*

    :param inputq:
        queue with cloned messages, delivered to socket after dest lookup
    :type inputq: struct sk_buff_head \*

.. _`tipc_sk_mcast_rcv.description`:

Description
-----------

Multi-threaded: parallel calls with reference to same queues may occur

.. _`tipc_sk_conn_proto_rcv`:

tipc_sk_conn_proto_rcv
======================

.. c:function:: void tipc_sk_conn_proto_rcv(struct tipc_sock *tsk, struct sk_buff *skb, struct sk_buff_head *inputq, struct sk_buff_head *xmitq)

    receive a connection mng protocol message

    :param tsk:
        receiving socket
    :type tsk: struct tipc_sock \*

    :param skb:
        pointer to message buffer.
    :type skb: struct sk_buff \*

    :param inputq:
        *undescribed*
    :type inputq: struct sk_buff_head \*

    :param xmitq:
        *undescribed*
    :type xmitq: struct sk_buff_head \*

.. _`tipc_sendmsg`:

tipc_sendmsg
============

.. c:function:: int tipc_sendmsg(struct socket *sock, struct msghdr *m, size_t dsz)

    send message in connectionless manner

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param m:
        message to send
    :type m: struct msghdr \*

    :param dsz:
        amount of user data to be sent
    :type dsz: size_t

.. _`tipc_sendmsg.description`:

Description
-----------

Message must have an destination specified explicitly.
Used for SOCK_RDM and SOCK_DGRAM messages,
and for 'SYN' messages on SOCK_SEQPACKET and SOCK_STREAM connections.
(Note: 'SYN+' is prohibited on SOCK_STREAM.)

Returns the number of bytes sent on success, or errno otherwise

.. _`tipc_sendstream`:

tipc_sendstream
===============

.. c:function:: int tipc_sendstream(struct socket *sock, struct msghdr *m, size_t dsz)

    send stream-oriented data

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param m:
        data to send
    :type m: struct msghdr \*

    :param dsz:
        total length of data to be transmitted
    :type dsz: size_t

.. _`tipc_sendstream.description`:

Description
-----------

Used for SOCK_STREAM data.

Returns the number of bytes sent on success (or partial success),
or errno if no data sent

.. _`tipc_send_packet`:

tipc_send_packet
================

.. c:function:: int tipc_send_packet(struct socket *sock, struct msghdr *m, size_t dsz)

    send a connection-oriented message

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param m:
        message to send
    :type m: struct msghdr \*

    :param dsz:
        length of data to be transmitted
    :type dsz: size_t

.. _`tipc_send_packet.description`:

Description
-----------

Used for SOCK_SEQPACKET messages.

Returns the number of bytes sent on success, or errno otherwise

.. _`tipc_sk_set_orig_addr`:

tipc_sk_set_orig_addr
=====================

.. c:function:: void tipc_sk_set_orig_addr(struct msghdr *m, struct sk_buff *skb)

    capture sender's address for received message

    :param m:
        descriptor for message info
    :type m: struct msghdr \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`tipc_sk_set_orig_addr.note`:

Note
----

Address is not captured if not requested by receiver.

.. _`tipc_sk_anc_data_recv`:

tipc_sk_anc_data_recv
=====================

.. c:function:: int tipc_sk_anc_data_recv(struct msghdr *m, struct sk_buff *skb, struct tipc_sock *tsk)

    optionally capture ancillary data for received message

    :param m:
        descriptor for message info
    :type m: struct msghdr \*

    :param skb:
        received message buffer
    :type skb: struct sk_buff \*

    :param tsk:
        TIPC port associated with message
    :type tsk: struct tipc_sock \*

.. _`tipc_sk_anc_data_recv.note`:

Note
----

Ancillary data is not captured if not requested by receiver.

Returns 0 if successful, otherwise errno

.. _`tipc_recvmsg`:

tipc_recvmsg
============

.. c:function:: int tipc_recvmsg(struct socket *sock, struct msghdr *m, size_t buflen, int flags)

    receive packet-oriented message

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param m:
        descriptor for message info
    :type m: struct msghdr \*

    :param buflen:
        length of user buffer area
    :type buflen: size_t

    :param flags:
        receive flags
    :type flags: int

.. _`tipc_recvmsg.description`:

Description
-----------

Used for SOCK_DGRAM, SOCK_RDM, and SOCK_SEQPACKET messages.
If the complete message doesn't fit in user area, truncate it.

Returns size of returned message data, errno otherwise

.. _`tipc_recvstream`:

tipc_recvstream
===============

.. c:function:: int tipc_recvstream(struct socket *sock, struct msghdr *m, size_t buflen, int flags)

    receive stream-oriented data

    :param sock:
        *undescribed*
    :type sock: struct socket \*

    :param m:
        descriptor for message info
    :type m: struct msghdr \*

    :param buflen:
        total size of user buffer area
    :type buflen: size_t

    :param flags:
        receive flags
    :type flags: int

.. _`tipc_recvstream.description`:

Description
-----------

Used for SOCK_STREAM messages only.  If not enough data is available
will optionally wait for more; never truncates data.

Returns size of returned message data, errno otherwise

.. _`tipc_write_space`:

tipc_write_space
================

.. c:function:: void tipc_write_space(struct sock *sk)

    wake up thread if port congestion is released

    :param sk:
        socket
    :type sk: struct sock \*

.. _`tipc_data_ready`:

tipc_data_ready
===============

.. c:function:: void tipc_data_ready(struct sock *sk)

    wake up threads to indicate messages have been received

    :param sk:
        socket
    :type sk: struct sock \*

.. _`tipc_sk_filter_connect`:

tipc_sk_filter_connect
======================

.. c:function:: bool tipc_sk_filter_connect(struct tipc_sock *tsk, struct sk_buff *skb)

    check incoming message for a connection-based socket

    :param tsk:
        TIPC socket
    :type tsk: struct tipc_sock \*

    :param skb:
        pointer to message buffer.
        Returns true if message should be added to receive queue, false otherwise
    :type skb: struct sk_buff \*

.. _`rcvbuf_limit`:

rcvbuf_limit
============

.. c:function:: unsigned int rcvbuf_limit(struct sock *sk, struct sk_buff *skb)

    get proper overload limit of socket receive queue

    :param sk:
        socket
    :type sk: struct sock \*

    :param skb:
        message
    :type skb: struct sk_buff \*

.. _`rcvbuf_limit.description`:

Description
-----------

For connection oriented messages, irrespective of importance,
default queue limit is 2 MB.

For connectionless messages, queue limits are based on message

.. _`rcvbuf_limit.importance-as-follows`:

importance as follows
---------------------


TIPC_LOW_IMPORTANCE       (2 MB)
TIPC_MEDIUM_IMPORTANCE    (4 MB)
TIPC_HIGH_IMPORTANCE      (8 MB)
TIPC_CRITICAL_IMPORTANCE  (16 MB)

Returns overload limit according to corresponding message importance

.. _`tipc_sk_filter_rcv`:

tipc_sk_filter_rcv
==================

.. c:function:: void tipc_sk_filter_rcv(struct sock *sk, struct sk_buff *skb, struct sk_buff_head *xmitq)

    validate incoming message

    :param sk:
        socket
    :type sk: struct sock \*

    :param skb:
        pointer to message.
    :type skb: struct sk_buff \*

    :param xmitq:
        *undescribed*
    :type xmitq: struct sk_buff_head \*

.. _`tipc_sk_filter_rcv.description`:

Description
-----------

Enqueues message on receive queue if acceptable; optionally handles
disconnect indication for a connected socket.

Called with socket lock already taken

.. _`tipc_sk_backlog_rcv`:

tipc_sk_backlog_rcv
===================

.. c:function:: int tipc_sk_backlog_rcv(struct sock *sk, struct sk_buff *skb)

    handle incoming message from backlog queue

    :param sk:
        socket
    :type sk: struct sock \*

    :param skb:
        message
    :type skb: struct sk_buff \*

.. _`tipc_sk_backlog_rcv.description`:

Description
-----------

Caller must hold socket lock

.. _`tipc_sk_enqueue`:

tipc_sk_enqueue
===============

.. c:function:: void tipc_sk_enqueue(struct sk_buff_head *inputq, struct sock *sk, u32 dport, struct sk_buff_head *xmitq)

    extract all buffers with destination 'dport' from inputq and try adding them to socket or backlog queue

    :param inputq:
        list of incoming buffers with potentially different destinations
    :type inputq: struct sk_buff_head \*

    :param sk:
        socket where the buffers should be enqueued
    :type sk: struct sock \*

    :param dport:
        port number for the socket
    :type dport: u32

    :param xmitq:
        *undescribed*
    :type xmitq: struct sk_buff_head \*

.. _`tipc_sk_enqueue.description`:

Description
-----------

Caller must hold socket lock

.. _`tipc_sk_rcv`:

tipc_sk_rcv
===========

.. c:function:: void tipc_sk_rcv(struct net *net, struct sk_buff_head *inputq)

    handle a chain of incoming buffers

    :param net:
        *undescribed*
    :type net: struct net \*

    :param inputq:
        buffer list containing the buffers
        Consumes all buffers in list until inputq is empty
    :type inputq: struct sk_buff_head \*

.. _`tipc_sk_rcv.note`:

Note
----

may be called in multiple threads referring to the same queue

.. _`tipc_connect`:

tipc_connect
============

.. c:function:: int tipc_connect(struct socket *sock, struct sockaddr *dest, int destlen, int flags)

    establish a connection to another TIPC port

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param dest:
        socket address for destination port
    :type dest: struct sockaddr \*

    :param destlen:
        size of socket address data structure
    :type destlen: int

    :param flags:
        file-related flags associated with socket
    :type flags: int

.. _`tipc_connect.description`:

Description
-----------

Returns 0 on success, errno otherwise

.. _`tipc_listen`:

tipc_listen
===========

.. c:function:: int tipc_listen(struct socket *sock, int len)

    allow socket to listen for incoming connections

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param len:
        (unused)
    :type len: int

.. _`tipc_listen.description`:

Description
-----------

Returns 0 on success, errno otherwise

.. _`tipc_accept`:

tipc_accept
===========

.. c:function:: int tipc_accept(struct socket *sock, struct socket *new_sock, int flags, bool kern)

    wait for connection request

    :param sock:
        listening socket
    :type sock: struct socket \*

    :param new_sock:
        *undescribed*
    :type new_sock: struct socket \*

    :param flags:
        file-related flags associated with socket
    :type flags: int

    :param kern:
        *undescribed*
    :type kern: bool

.. _`tipc_accept.description`:

Description
-----------

Returns 0 on success, errno otherwise

.. _`tipc_shutdown`:

tipc_shutdown
=============

.. c:function:: int tipc_shutdown(struct socket *sock, int how)

    shutdown socket connection

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param how:
        direction to close (must be SHUT_RDWR)
    :type how: int

.. _`tipc_shutdown.description`:

Description
-----------

Terminates connection (if necessary), then purges socket's receive queue.

Returns 0 on success, errno otherwise

.. _`tipc_setsockopt`:

tipc_setsockopt
===============

.. c:function:: int tipc_setsockopt(struct socket *sock, int lvl, int opt, char __user *ov, unsigned int ol)

    set socket option

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param lvl:
        option level
    :type lvl: int

    :param opt:
        option identifier
    :type opt: int

    :param ov:
        pointer to new option value
    :type ov: char __user \*

    :param ol:
        length of option value
    :type ol: unsigned int

.. _`tipc_setsockopt.description`:

Description
-----------

For stream sockets only, accepts and ignores all IPPROTO_TCP options
(to ease compatibility).

Returns 0 on success, errno otherwise

.. _`tipc_getsockopt`:

tipc_getsockopt
===============

.. c:function:: int tipc_getsockopt(struct socket *sock, int lvl, int opt, char __user *ov, int __user *ol)

    get socket option

    :param sock:
        socket structure
    :type sock: struct socket \*

    :param lvl:
        option level
    :type lvl: int

    :param opt:
        option identifier
    :type opt: int

    :param ov:
        receptacle for option value
    :type ov: char __user \*

    :param ol:
        receptacle for length of option value
    :type ol: int __user \*

.. _`tipc_getsockopt.description`:

Description
-----------

For stream sockets only, returns 0 length result for all IPPROTO_TCP options
(to ease compatibility).

Returns 0 on success, errno otherwise

.. _`tipc_socket_init`:

tipc_socket_init
================

.. c:function:: int tipc_socket_init( void)

    initialize TIPC socket interface

    :param void:
        no arguments
    :type void: 

.. _`tipc_socket_init.description`:

Description
-----------

Returns 0 on success, errno otherwise

.. _`tipc_socket_stop`:

tipc_socket_stop
================

.. c:function:: void tipc_socket_stop( void)

    stop TIPC socket interface

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

