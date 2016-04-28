.. -*- coding: utf-8; mode: rst -*-

.. _API-skwq-has-sleeper:

================
skwq_has_sleeper
================

*man skwq_has_sleeper(9)*

*4.6.0-rc5*

check if there are any waiting processes


Synopsis
========

.. c:function:: bool skwq_has_sleeper( struct socket_wq * wq )

Arguments
=========

``wq``
    struct socket_wq


Description
===========

Returns true if socket_wq has waiting processes

The purpose of the skwq_has_sleeper and sock_poll_wait is to wrap
the memory barrier call. They were added due to the race found within
the tcp code.


Consider following tcp code paths
=================================

CPU1 CPU2

sys_select receive packet ... ... __add_wait_queue update
tp->rcv_nxt ... ... tp->rcv_nxt check sock_def_readable ... {
schedule ``rcu_read_lock``; wq = rcu_dereference(sk->sk_wq); if (wq &&
waitqueue_active( ``wq``->wait))
wake_up_interruptible( ``wq``->wait) ... }

The race for tcp fires when the __add_wait_queue changes done by
CPU1 stay in its cache, and so does the tp->rcv_nxt update on CPU2
side. The CPU1 could then endup calling schedule and sleep forever if
there are no more data on the socket.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
