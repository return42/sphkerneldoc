
.. _API-skb-fclone-busy:

===============
skb_fclone_busy
===============

*man skb_fclone_busy(9)*

*4.6.0-rc1*

check if fclone is busy


Synopsis
========

.. c:function:: bool skb_fclone_busy( const struct sock * sk, const struct sk_buff * skb )

Arguments
=========

``sk``
    -- undescribed --

``skb``
    buffer


Description
===========

Returns true if skb is a fast clone, and its clone is not freed. Some drivers call ``skb_orphan`` in their ``ndo_start_xmit``, so we also check that this didnt happen.
