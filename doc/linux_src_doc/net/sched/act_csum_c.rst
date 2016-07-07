.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sched/act_csum.c

.. _`tcf_csum_skb_nextlayer`:

tcf_csum_skb_nextlayer
======================

.. c:function:: void *tcf_csum_skb_nextlayer(struct sk_buff *skb, unsigned int ihl, unsigned int ipl, unsigned int jhl)

    Get next layer pointer

    :param struct sk_buff \*skb:
        sk_buff to use

    :param unsigned int ihl:
        previous summed headers length

    :param unsigned int ipl:
        complete packet length

    :param unsigned int jhl:
        next header length

.. _`tcf_csum_skb_nextlayer.description`:

Description
-----------

Check the expected next layer availability in the specified sk_buff.
Return the next layer pointer if pass, NULL otherwise.

.. This file was automatic generated / don't edit.

