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

.. This file was automatic generated / don't edit.

