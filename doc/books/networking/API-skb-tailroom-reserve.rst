
.. _API-skb-tailroom-reserve:

====================
skb_tailroom_reserve
====================

*man skb_tailroom_reserve(9)*

*4.6.0-rc1*

adjust reserved_tailroom


Synopsis
========

.. c:function:: void skb_tailroom_reserve( struct sk_buff * skb, unsigned int mtu, unsigned int needed_tailroom )

Arguments
=========

``skb``
    buffer to alter

``mtu``
    maximum amount of headlen permitted

``needed_tailroom``
    minimum amount of reserved_tailroom


Description
===========

Set reserved_tailroom so that headlen can be as large as possible but not larger than mtu and tailroom cannot be smaller than needed_tailroom. The required headroom should
already have been reserved before using this function.
