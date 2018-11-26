.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/inet_connection_sock.c

.. _`inet_csk_clone_lock`:

inet_csk_clone_lock
===================

.. c:function:: struct sock *inet_csk_clone_lock(const struct sock *sk, const struct request_sock *req, const gfp_t priority)

    clone an inet socket, and lock its clone

    :param sk:
        the socket to clone
    :type sk: const struct sock \*

    :param req:
        request_sock
    :type req: const struct request_sock \*

    :param priority:
        for allocation (%GFP_KERNEL, \ ``GFP_ATOMIC``\ , etc)
    :type priority: const gfp_t

.. _`inet_csk_clone_lock.description`:

Description
-----------

Caller must unlock socket even in error path (bh_unlock_sock(newsk))

.. This file was automatic generated / don't edit.

