
.. _API-audit-rule-change:

=================
audit_rule_change
=================

*man audit_rule_change(9)*

*4.6.0-rc1*

apply all rules to the specified message type


Synopsis
========

.. c:function:: int audit_rule_change( int type, __u32 portid, int seq, void * data, size_t datasz )

Arguments
=========

``type``
    audit message type

``portid``
    target port id for netlink audit messages

``seq``
    netlink audit message sequence (serial) number

``data``
    payload data

``datasz``
    size of payload data
