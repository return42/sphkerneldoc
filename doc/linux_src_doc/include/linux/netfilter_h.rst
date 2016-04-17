.. -*- coding: utf-8; mode: rst -*-

===========
netfilter.h
===========


.. _`nf_hook_thresh`:

nf_hook_thresh
==============

.. c:function:: int nf_hook_thresh (u_int8_t pf, unsigned int hook, struct net *net, struct sock *sk, struct sk_buff *skb, struct net_device *indev, struct net_device *outdev, int (*okfn) (struct net *, struct sock *, struct sk_buff *, int thresh)

    call a netfilter hook

    :param u_int8_t pf:

        *undescribed*

    :param unsigned int hook:

        *undescribed*

    :param struct net \*net:

        *undescribed*

    :param struct sock \*sk:

        *undescribed*

    :param struct sk_buff \*skb:

        *undescribed*

    :param struct net_device \*indev:

        *undescribed*

    :param struct net_device \*outdev:

        *undescribed*

    :param int (\*okfn) (struct net \*, struct sock \*, struct sk_buff \*):

        *undescribed*

    :param int thresh:

        *undescribed*



.. _`nf_hook_thresh.description`:

Description
-----------


Returns 1 if the hook has allowed the packet to pass.  The function
okfn must be invoked by the caller in this case.  Any other return
value indicates the packet has been consumed by the hook.



.. _`declare_per_cpu`:

DECLARE_PER_CPU
===============

.. c:function:: DECLARE_PER_CPU ( bool,  nf_skb_duplicated)

    TEE target has sent a packet

    :param bool:

        *undescribed*

    :param nf_skb_duplicated:

        *undescribed*



.. _`declare_per_cpu.description`:

Description
-----------


When a xtables target sends a packet, the OUTPUT and POSTROUTING
hooks are traversed again, i.e. nft and xtables are invoked recursively.

This is used by xtables TEE target to prevent the duplicated skb from
being duplicated again.

