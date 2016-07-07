.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/send.h

.. _`batadv_send_skb_via_tt`:

batadv_send_skb_via_tt
======================

.. c:function:: int batadv_send_skb_via_tt(struct batadv_priv *bat_priv, struct sk_buff *skb, u8 *dst_hint, unsigned short vid)

    send an skb via TT lookup

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        the payload to send

    :param u8 \*dst_hint:
        can be used to override the destination contained in the skb

    :param unsigned short vid:
        the vid to be used to search the translation table

.. _`batadv_send_skb_via_tt.description`:

Description
-----------

Look up the recipient node for the destination address in the ethernet
header via the translation table. Wrap the given skb into a batman-adv
unicast header. Then send this frame to the according destination node.

.. _`batadv_send_skb_via_tt.return`:

Return
------

NET_XMIT_DROP in case of error or NET_XMIT_SUCCESS otherwise.

.. _`batadv_send_skb_via_tt_4addr`:

batadv_send_skb_via_tt_4addr
============================

.. c:function:: int batadv_send_skb_via_tt_4addr(struct batadv_priv *bat_priv, struct sk_buff *skb, int packet_subtype, u8 *dst_hint, unsigned short vid)

    send an skb via TT lookup

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct sk_buff \*skb:
        the payload to send

    :param int packet_subtype:
        the unicast 4addr packet subtype to use

    :param u8 \*dst_hint:
        can be used to override the destination contained in the skb

    :param unsigned short vid:
        the vid to be used to search the translation table

.. _`batadv_send_skb_via_tt_4addr.description`:

Description
-----------

Look up the recipient node for the destination address in the ethernet
header via the translation table. Wrap the given skb into a batman-adv
unicast-4addr header. Then send this frame to the according destination
node.

.. _`batadv_send_skb_via_tt_4addr.return`:

Return
------

NET_XMIT_DROP in case of error or NET_XMIT_SUCCESS otherwise.

.. This file was automatic generated / don't edit.

