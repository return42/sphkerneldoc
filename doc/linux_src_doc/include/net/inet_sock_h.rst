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

.. This file was automatic generated / don't edit.

