.. -*- coding: utf-8; mode: rst -*-

.. _API-audit-list-rules-send:

=====================
audit_list_rules_send
=====================

*man audit_list_rules_send(9)*

*4.6.0-rc5*

list the audit rules


Synopsis
========

.. c:function:: int audit_list_rules_send( struct sk_buff * request_skb, int seq )

Arguments
=========

``request_skb``
    skb of request we are replying to (used to target the reply)

``seq``
    netlink audit message sequence (serial) number


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
