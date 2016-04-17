.. -*- coding: utf-8; mode: rst -*-

============
tcp_output.c
============


.. _`tcp_release_cb`:

tcp_release_cb
==============

.. c:function:: void tcp_release_cb (struct sock *sk)

    tcp release_sock() callback

    :param struct sock \*sk:
        socket



.. _`tcp_release_cb.description`:

Description
-----------

called from :c:func:`release_sock` to perform protocol dependent
actions before socket release.



.. _`tcp_make_synack`:

tcp_make_synack
===============

.. c:function:: struct sk_buff *tcp_make_synack (const struct sock *sk, struct dst_entry *dst, struct request_sock *req, struct tcp_fastopen_cookie *foc, bool attach_req)

    Prepare a SYN-ACK.

    :param const struct sock \*sk:

        *undescribed*

    :param struct dst_entry \*dst:
        Caller should not use it again.

    :param struct request_sock \*req:

        *undescribed*

    :param struct tcp_fastopen_cookie \*foc:

        *undescribed*

    :param bool attach_req:

        *undescribed*



.. _`tcp_make_synack.sk`:

sk
--

listener socket



.. _`tcp_make_synack.dst`:

dst
---

dst entry attached to the SYNACK



.. _`tcp_make_synack.req`:

req
---

request_sock pointer

Allocate one skb and build a SYNACK packet.

