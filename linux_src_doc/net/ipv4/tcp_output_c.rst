.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/tcp_output.c

.. _`tcp_release_cb`:

tcp_release_cb
==============

.. c:function:: void tcp_release_cb(struct sock *sk)

    tcp \ :c:func:`release_sock`\  callback

    :param sk:
        socket
    :type sk: struct sock \*

.. _`tcp_release_cb.description`:

Description
-----------

called from \ :c:func:`release_sock`\  to perform protocol dependent
actions before socket release.

.. _`tcp_make_synack`:

tcp_make_synack
===============

.. c:function:: struct sk_buff *tcp_make_synack(const struct sock *sk, struct dst_entry *dst, struct request_sock *req, struct tcp_fastopen_cookie *foc, enum tcp_synack_type synack_type)

    Prepare a SYN-ACK. sk: listener socket

    :param sk:
        *undescribed*
    :type sk: const struct sock \*

    :param dst:
        Caller should not use it again.
    :type dst: struct dst_entry \*

    :param req:
        *undescribed*
    :type req: struct request_sock \*

    :param foc:
        *undescribed*
    :type foc: struct tcp_fastopen_cookie \*

    :param synack_type:
        *undescribed*
    :type synack_type: enum tcp_synack_type

.. _`tcp_make_synack.dst`:

dst
---

dst entry attached to the SYNACK

.. _`tcp_make_synack.req`:

req
---

request_sock pointer

Allocate one skb and build a SYNACK packet.

.. This file was automatic generated / don't edit.

