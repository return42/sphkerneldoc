.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/mac80211/wme.c

.. _`ieee80211_fix_reserved_tid`:

ieee80211_fix_reserved_tid
==========================

.. c:function:: u8 ieee80211_fix_reserved_tid(u8 tid)

    return the TID to use if this one is reserved

    :param u8 tid:
        the assumed-reserved TID

.. _`ieee80211_fix_reserved_tid.return`:

Return
------

the alternative TID to use, or 0 on error

.. _`ieee80211_set_qos_hdr`:

ieee80211_set_qos_hdr
=====================

.. c:function:: void ieee80211_set_qos_hdr(struct ieee80211_sub_if_data *sdata, struct sk_buff *skb)

    Fill in the QoS header if there is one.

    :param struct ieee80211_sub_if_data \*sdata:
        local subif

    :param struct sk_buff \*skb:
        packet to be updated

.. This file was automatic generated / don't edit.

