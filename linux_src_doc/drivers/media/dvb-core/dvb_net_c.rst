.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-core/dvb_net.c

.. _`dvb_net_eth_type_trans`:

dvb_net_eth_type_trans
======================

.. c:function:: __be16 dvb_net_eth_type_trans(struct sk_buff *skb, struct net_device *dev)

    assume 802.3 if the type field is short enough to be a length. This is normal practice and works for any 'now in use' protocol.

    :param struct sk_buff \*skb:
        *undescribed*

    :param struct net_device \*dev:
        *undescribed*

.. _`dvb_net_eth_type_trans.description`:

Description
-----------

stolen from eth.c out of the linux kernel, hacked for dvb-device
by Michael Holzt <kju@debian.org>

.. _`dvb_net_ule`:

dvb_net_ule
===========

.. c:function:: void dvb_net_ule(struct net_device *dev, const u8 *buf, size_t buf_len)

    ietf-ipdvb-ule-03.txt from a sequence of TS cells of a single PID.

    :param struct net_device \*dev:
        *undescribed*

    :param const u8 \*buf:
        *undescribed*

    :param size_t buf_len:
        *undescribed*

.. This file was automatic generated / don't edit.

