
.. _API-sk-state-load:

=============
sk_state_load
=============

*man sk_state_load(9)*

*4.6.0-rc1*

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

Paired with ``sk_state_store``. Used in places we do not hold socket lock : ``tcp_diag_get_info``, ``tcp_get_info``, ``tcp_poll``, ``get_tcp4_sock`` ...
