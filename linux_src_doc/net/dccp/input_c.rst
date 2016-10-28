.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/input.c

.. _`dccp_sample_rtt`:

dccp_sample_rtt
===============

.. c:function:: u32 dccp_sample_rtt(struct sock *sk, long delta)

    Validate and finalise computation of RTT sample

    :param struct sock \*sk:
        *undescribed*

    :param long delta:
        number of microseconds between packet and acknowledgment

.. _`dccp_sample_rtt.description`:

Description
-----------

The routine is kept generic to work in different contexts. It should be
called immediately when the ACK used for the RTT sample arrives.

.. This file was automatic generated / don't edit.

