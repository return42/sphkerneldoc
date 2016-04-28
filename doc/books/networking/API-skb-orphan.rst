.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-orphan:

==========
skb_orphan
==========

*man skb_orphan(9)*

*4.6.0-rc5*

orphan a buffer


Synopsis
========

.. c:function:: void skb_orphan( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to orphan


Description
===========

If a buffer currently has an owner then we call the owner's destructor
function and make the ``skb`` unowned. The buffer continues to exist but
is no longer charged to its former owner.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
