
.. _API-audit-list-rules-send:

=====================
audit_list_rules_send
=====================

*man audit_list_rules_send(9)*

*4.6.0-rc1*

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
