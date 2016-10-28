.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/inet_timewait_sock.c

.. _`inet_twsk_bind_unhash`:

inet_twsk_bind_unhash
=====================

.. c:function:: void inet_twsk_bind_unhash(struct inet_timewait_sock *tw, struct inet_hashinfo *hashinfo)

    unhash a timewait socket from bind hash

    :param struct inet_timewait_sock \*tw:
        timewait socket

    :param struct inet_hashinfo \*hashinfo:
        hashinfo pointer

.. _`inet_twsk_bind_unhash.description`:

Description
-----------

unhash a timewait socket from bind hash, if hashed.
bind hash lock must be held by caller.
Returns 1 if caller should call \ :c:func:`inet_twsk_put`\  after lock release.

.. This file was automatic generated / don't edit.

