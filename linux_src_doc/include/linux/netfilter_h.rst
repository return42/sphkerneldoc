.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/netfilter.h

.. _`nf_hook`:

nf_hook
=======

.. c:function:: int nf_hook(u_int8_t pf, unsigned int hook, struct net *net, struct sock *sk, struct sk_buff *skb, struct net_device *indev, struct net_device *outdev, int (*okfn)(struct net *, struct sock *, struct sk_buff *))

    call a netfilter hook

    :param pf:
        *undescribed*
    :type pf: u_int8_t

    :param hook:
        *undescribed*
    :type hook: unsigned int

    :param net:
        *undescribed*
    :type net: struct net \*

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param indev:
        *undescribed*
    :type indev: struct net_device \*

    :param outdev:
        *undescribed*
    :type outdev: struct net_device \*

    :param int (\*okfn)(struct net \*, struct sock \*, struct sk_buff \*):
        *undescribed*

.. _`nf_hook.description`:

Description
-----------

Returns 1 if the hook has allowed the packet to pass.  The function
okfn must be invoked by the caller in this case.  Any other return
value indicates the packet has been consumed by the hook.

.. _`declare_per_cpu`:

DECLARE_PER_CPU
===============

.. c:function::  DECLARE_PER_CPU( bool,  nf_skb_duplicated)

    TEE target has sent a packet

    :param bool:
        *undescribed*
    :type bool: 

    :param nf_skb_duplicated:
        *undescribed*
    :type nf_skb_duplicated: 

.. _`declare_per_cpu.description`:

Description
-----------

When a xtables target sends a packet, the OUTPUT and POSTROUTING
hooks are traversed again, i.e. nft and xtables are invoked recursively.

This is used by xtables TEE target to prevent the duplicated skb from
being duplicated again.

.. This file was automatic generated / don't edit.

