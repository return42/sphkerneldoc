
.. _API-datagram-poll:

=============
datagram_poll
=============

*man datagram_poll(9)*

*4.6.0-rc1*

generic datagram poll


Synopsis
========

.. c:function:: unsigned int datagram_poll( struct file * file, struct socket * sock, poll_table * wait )

Arguments
=========

``file``
    file struct

``sock``
    socket

``wait``
    poll table


Datagram poll
=============

Again totally generic. This also handles sequenced packet sockets providing the socket receive queue is only ever holding data ready to receive.


Note
====

when you _don't_ use this routine for this protocol, and you use a different write policy from ``sock_writeable`` then please supply your own write_space callback.
