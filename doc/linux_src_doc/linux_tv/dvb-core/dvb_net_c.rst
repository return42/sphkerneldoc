.. -*- coding: utf-8; mode: rst -*-

=========
dvb_net.c
=========



.. _xref_dvb_net_eth_type_trans:

dvb_net_eth_type_trans
======================

.. c:function:: __be16 dvb_net_eth_type_trans (struct sk_buff * skb, struct net_device * dev)

    

    :param struct sk_buff * skb:

        _undescribed_

    :param struct net_device * dev:

        _undescribed_



Description
-----------

	assume 802.3 if the type field is short enough to be a length.
	This is normal practice and works for any 'now in use' protocol.


 stolen from eth.c out of the linux kernel, hacked for dvb-device
 by Michael Holzt <kju**debian**.org>




.. _xref_dvb_net_ule:

dvb_net_ule
===========

.. c:function:: void dvb_net_ule (struct net_device * dev, const u8 * buf, size_t buf_len)

    ietf-ipdvb-ule-03.txt from a sequence of TS cells of a single PID.

    :param struct net_device * dev:

        _undescribed_

    :param const u8 * buf:

        _undescribed_

    :param size_t buf_len:

        _undescribed_


