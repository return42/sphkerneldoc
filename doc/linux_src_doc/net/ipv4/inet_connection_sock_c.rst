.. -*- coding: utf-8; mode: rst -*-

======================
inet_connection_sock.c
======================


.. _`inet_csk_clone_lock`:

inet_csk_clone_lock
===================

.. c:function:: struct sock *inet_csk_clone_lock (const struct sock *sk, const struct request_sock *req, const gfp_t priority)

    clone an inet socket, and lock its clone

    :param const struct sock \*sk:
        the socket to clone

    :param const struct request_sock \*req:
        request_sock

    :param const gfp_t priority:
        for allocation (\ ``GFP_KERNEL``\ , ``GFP_ATOMIC``\ , etc)



.. _`inet_csk_clone_lock.description`:

Description
-----------

Caller must unlock socket even in error path (bh_unlock_sock(newsk))

