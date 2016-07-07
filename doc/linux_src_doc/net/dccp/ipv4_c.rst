.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ipv4.c

.. _`dccp_invalid_packet`:

dccp_invalid_packet
===================

.. c:function:: int dccp_invalid_packet(struct sk_buff *skb)

    check for malformed packets Implements RFC 4340, 8.5:  Step 1: Check header basics Packets that fail these checks are ignored and do not receive Resets.

    :param struct sk_buff \*skb:
        *undescribed*

.. This file was automatic generated / don't edit.

