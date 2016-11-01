.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/tcp_timer.c

.. _`tcp_write_err`:

tcp_write_err
=============

.. c:function:: void tcp_write_err(struct sock *sk)

    close socket and save error info

    :param struct sock \*sk:
        The socket the error has appeared on.

.. _`tcp_write_err.return`:

Return
------

Nothing (void)

.. _`tcp_out_of_resources`:

tcp_out_of_resources
====================

.. c:function:: int tcp_out_of_resources(struct sock *sk, bool do_reset)

    Close socket if out of resources

    :param struct sock \*sk:
        pointer to current socket

    :param bool do_reset:
        send a last packet with reset flag

.. _`tcp_out_of_resources.description`:

Description
-----------

Do not allow orphaned sockets to eat all our resources.
This is direct violation of TCP specs, but it is required
to prevent DoS attacks. It is called when a retransmission timeout
or zero probe timeout occurs on orphaned socket.

Criteria is still not confirmed experimentally and may change.
We kill the socket, if:
1. If number of orphaned sockets exceeds an administratively configured
limit.
2. If we have strong memory pressure.

.. _`tcp_orphan_retries`:

tcp_orphan_retries
==================

.. c:function:: int tcp_orphan_retries(struct sock *sk, bool alive)

    Returns maximal number of retries on an orphaned socket

    :param struct sock \*sk:
        Pointer to the current socket.

    :param bool alive:
        bool, socket alive state

.. _`retransmits_timed_out`:

retransmits_timed_out
=====================

.. c:function:: bool retransmits_timed_out(struct sock *sk, unsigned int boundary, unsigned int timeout, bool syn_set)

    returns true if this connection has timed out

    :param struct sock \*sk:
        The current socket

    :param unsigned int boundary:
        max number of retransmissions

    :param unsigned int timeout:
        A custom timeout value.
        If set to 0 the default timeout is calculated and used.
        Using TCP_RTO_MIN and the number of unsuccessful retransmits.

    :param bool syn_set:
        true if the SYN Bit was set.

.. _`retransmits_timed_out.description`:

Description
-----------

The default "timeout" value this function can calculate and use
is equivalent to the timeout of a TCP Connection
after "boundary" unsuccessful, exponentially backed-off
retransmissions with an initial RTO of TCP_RTO_MIN or TCP_TIMEOUT_INIT if
syn_set flag is set.

.. _`tcp_delack_timer`:

tcp_delack_timer
================

.. c:function:: void tcp_delack_timer(unsigned long data)

    The TCP delayed ACK timeout handler

    :param unsigned long data:
        Pointer to the current socket. (gets casted to struct sock \*)

.. _`tcp_delack_timer.description`:

Description
-----------

This function gets (indirectly) called when the kernel timer for a TCP packet
of this socket expires. Calls \ :c:func:`tcp_delack_timer_handler`\  to do the actual work.

.. _`tcp_delack_timer.return`:

Return
------

Nothing (void)

.. _`tcp_retransmit_timer`:

tcp_retransmit_timer
====================

.. c:function:: void tcp_retransmit_timer(struct sock *sk)

    The TCP retransmit timeout handler

    :param struct sock \*sk:
        Pointer to the current socket.

.. _`tcp_retransmit_timer.description`:

Description
-----------

This function gets called when the kernel timer for a TCP packet
of this socket expires.

It handles retransmission, timer adjustment and other necesarry measures.

.. _`tcp_retransmit_timer.return`:

Return
------

Nothing (void)

.. This file was automatic generated / don't edit.

