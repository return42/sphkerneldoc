.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-has-shared-frag:

===================
skb_has_shared_frag
===================

*man skb_has_shared_frag(9)*

*4.6.0-rc5*

can any frag be overwritten


Synopsis
========

.. c:function:: bool skb_has_shared_frag( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to test


Description
===========

Return true if the skb has at least one frag that might be modified by
an external entity (as in ``vmsplice``/``sendfile``)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
