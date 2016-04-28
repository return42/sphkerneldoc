.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-state-load:

=============
sk_state_load
=============

*man sk_state_load(9)*

*4.6.0-rc5*

read sk->sk_state for lockless contexts


Synopsis
========

.. c:function:: int sk_state_load( const struct sock * sk )

Arguments
=========

``sk``
    socket pointer


Description
===========

Paired with ``sk_state_store``. Used in places we do not hold socket
lock : ``tcp_diag_get_info``, ``tcp_get_info``, ``tcp_poll``,
``get_tcp4_sock`` ...


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
