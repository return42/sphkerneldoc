.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/datagram.c

.. _`__skb_try_recv_datagram`:

__skb_try_recv_datagram
=======================

.. c:function:: struct sk_buff *__skb_try_recv_datagram(struct sock *sk, unsigned int flags, void (*destructor)(struct sock *sk, struct sk_buff *skb), int *peeked, int *off, int *err, struct sk_buff **last)

    Receive a datagram skbuff

    :param sk:
        socket
    :type sk: struct sock \*

    :param flags:
        MSG\_ flags
    :type flags: unsigned int

    :param void (\*destructor)(struct sock \*sk, struct sk_buff \*skb):
        invoked under the receive lock on successful dequeue

    :param peeked:
        returns non-zero if this packet has been seen before
    :type peeked: int \*

    :param off:
        an offset in bytes to peek skb from. Returns an offset
        within an skb where data actually starts
    :type off: int \*

    :param err:
        error code returned
    :type err: int \*

    :param last:
        set to last peeked message to inform the wait function
        what to look for when peeking
    :type last: struct sk_buff \*\*

.. _`__skb_try_recv_datagram.description`:

Description
-----------

     Get a datagram skbuff, understands the peeking, nonblocking wakeups
     and possible races. This replaces identical code in packet, raw and
     udp, as well as the IPX AX.25 and Appletalk. It also finally fixes
     the long standing peek and read race for datagram sockets. If you
     alter this routine remember it must be re-entrant.

     This function will lock the socket if a skb is returned, so
     the caller needs to unlock the socket in that case (usually by
     calling skb_free_datagram). Returns NULL with \ ``err``\  set to
     -EAGAIN if no data was available or to some other value if an
     error was detected.

     * It does not lock socket since today. This function is
     * free of race conditions. This measure should/can improve
     * significantly datagram socket latencies at high loads,
     * when data copying to user space takes lots of time.
     * (BTW I've just killed the last \ :c:func:`cli`\  in IP/IPv6/core/netlink/packet
     *  8) Great win.)
     *                                           --ANK (980729)

     The order of the tests when we find no data waiting are specified
     quite explicitly by POSIX 1003.1g, don't change them without having
     the standard around please.

.. _`skb_kill_datagram`:

skb_kill_datagram
=================

.. c:function:: int skb_kill_datagram(struct sock *sk, struct sk_buff *skb, unsigned int flags)

    Free a datagram skbuff forcibly

    :param sk:
        socket
    :type sk: struct sock \*

    :param skb:
        datagram skbuff
    :type skb: struct sk_buff \*

    :param flags:
        MSG\_ flags
    :type flags: unsigned int

.. _`skb_kill_datagram.description`:

Description
-----------

     This function frees a datagram skbuff that was received by
     skb_recv_datagram.  The flags argument must match the one
     used for skb_recv_datagram.

     If the MSG_PEEK flag is set, and the packet is still on the
     receive queue of the socket, it will be taken off the queue
     before it is freed.

     This function currently only disables BH when acquiring the
     sk_receive_queue lock.  Therefore it must not be used in a
     context where that lock is acquired in an IRQ context.

     It returns 0 if the packet was removed by us.

.. _`skb_copy_datagram_iter`:

skb_copy_datagram_iter
======================

.. c:function:: int skb_copy_datagram_iter(const struct sk_buff *skb, int offset, struct iov_iter *to, int len)

    Copy a datagram to an iovec iterator.

    :param skb:
        buffer to copy
    :type skb: const struct sk_buff \*

    :param offset:
        offset in the buffer to start copying from
    :type offset: int

    :param to:
        iovec iterator to copy to
    :type to: struct iov_iter \*

    :param len:
        amount of data to copy from buffer to iovec
    :type len: int

.. _`skb_copy_datagram_from_iter`:

skb_copy_datagram_from_iter
===========================

.. c:function:: int skb_copy_datagram_from_iter(struct sk_buff *skb, int offset, struct iov_iter *from, int len)

    Copy a datagram from an iov_iter.

    :param skb:
        buffer to copy
    :type skb: struct sk_buff \*

    :param offset:
        offset in the buffer to start copying to
    :type offset: int

    :param from:
        the copy source
    :type from: struct iov_iter \*

    :param len:
        amount of data to copy to buffer from iovec
    :type len: int

.. _`skb_copy_datagram_from_iter.description`:

Description
-----------

     Returns 0 or -EFAULT.

.. _`zerocopy_sg_from_iter`:

zerocopy_sg_from_iter
=====================

.. c:function:: int zerocopy_sg_from_iter(struct sk_buff *skb, struct iov_iter *from)

    Build a zerocopy datagram from an iov_iter

    :param skb:
        buffer to copy
    :type skb: struct sk_buff \*

    :param from:
        the source to copy from
    :type from: struct iov_iter \*

.. _`zerocopy_sg_from_iter.description`:

Description
-----------

     The function will first copy up to headlen, and then pin the userspace
     pages and build frags through them.

     Returns 0, -EFAULT or -EMSGSIZE.

.. _`skb_copy_and_csum_datagram_msg`:

skb_copy_and_csum_datagram_msg
==============================

.. c:function:: int skb_copy_and_csum_datagram_msg(struct sk_buff *skb, int hlen, struct msghdr *msg)

    Copy and checksum skb to user iovec.

    :param skb:
        skbuff
    :type skb: struct sk_buff \*

    :param hlen:
        hardware length
    :type hlen: int

    :param msg:
        destination
    :type msg: struct msghdr \*

.. _`skb_copy_and_csum_datagram_msg.description`:

Description
-----------

     Caller _must_ check that skb will fit to this iovec.

.. _`skb_copy_and_csum_datagram_msg.return`:

Return
------

0       - success.
              -EINVAL - checksum failure.
              -EFAULT - fault during copy.

.. _`datagram_poll`:

datagram_poll
=============

.. c:function:: __poll_t datagram_poll(struct file *file, struct socket *sock, poll_table *wait)

    generic datagram poll

    :param file:
        file struct
    :type file: struct file \*

    :param sock:
        socket
    :type sock: struct socket \*

    :param wait:
        poll table
    :type wait: poll_table \*

.. _`datagram_poll.description`:

Description
-----------

     Datagram poll: Again totally generic. This also handles
     sequenced packet sockets providing the socket receive queue
     is only ever holding data ready to receive.

.. _`datagram_poll.note`:

Note
----

when you *don't* use this routine for this protocol,
     and you use a different write policy from \ :c:func:`sock_writeable`\ 
     then please supply your own write_space callback.

.. This file was automatic generated / don't edit.

