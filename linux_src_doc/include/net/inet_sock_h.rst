.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/inet_sock.h

.. _`sk_to_full_sk`:

sk_to_full_sk
=============

.. c:function:: struct sock *sk_to_full_sk(struct sock *sk)

    Access to a full socket

    :param struct sock \*sk:
        pointer to a socket

.. _`sk_to_full_sk.description`:

Description
-----------

SYNACK messages might be attached to request sockets.
Some places want to reach the listener in this case.

.. _`inet_sk_state_load`:

inet_sk_state_load
==================

.. c:function:: int inet_sk_state_load(const struct sock *sk)

    read sk->sk_state for lockless contexts

    :param const struct sock \*sk:
        socket pointer

.. _`inet_sk_state_load.description`:

Description
-----------

Paired with \ :c:func:`inet_sk_state_store`\ . Used in places we don't hold socket lock:
\ :c:func:`tcp_diag_get_info`\ , \ :c:func:`tcp_get_info`\ , \ :c:func:`tcp_poll`\ , \ :c:func:`get_tcp4_sock`\  ...

.. _`inet_sk_state_store`:

inet_sk_state_store
===================

.. c:function:: void inet_sk_state_store(struct sock *sk, int newstate)

    update sk->sk_state

    :param struct sock \*sk:
        socket pointer

    :param int newstate:
        new state

.. _`inet_sk_state_store.description`:

Description
-----------

Paired with \ :c:func:`inet_sk_state_load`\ . Should be used in contexts where
state change might impact lockless readers.

.. This file was automatic generated / don't edit.

