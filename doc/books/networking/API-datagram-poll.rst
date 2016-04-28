.. -*- coding: utf-8; mode: rst -*-

.. _API-datagram-poll:

=============
datagram_poll
=============

*man datagram_poll(9)*

*4.6.0-rc5*

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

Again totally generic. This also handles sequenced packet sockets
providing the socket receive queue is only ever holding data ready to
receive.


Note
====

when you _don't_ use this routine for this protocol, and you use a
different write policy from ``sock_writeable`` then please supply your
own write_space callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
