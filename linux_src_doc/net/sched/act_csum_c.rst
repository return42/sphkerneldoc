.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sched/act_csum.c

.. _`tcf_csum_skb_nextlayer`:

tcf_csum_skb_nextlayer
======================

.. c:function:: void *tcf_csum_skb_nextlayer(struct sk_buff *skb, unsigned int ihl, unsigned int ipl, unsigned int jhl)

    Get next layer pointer

    :param skb:
        sk_buff to use
    :type skb: struct sk_buff \*

    :param ihl:
        previous summed headers length
    :type ihl: unsigned int

    :param ipl:
        complete packet length
    :type ipl: unsigned int

    :param jhl:
        next header length
    :type jhl: unsigned int

.. _`tcf_csum_skb_nextlayer.description`:

Description
-----------

Check the expected next layer availability in the specified sk_buff.
Return the next layer pointer if pass, NULL otherwise.

.. This file was automatic generated / don't edit.

