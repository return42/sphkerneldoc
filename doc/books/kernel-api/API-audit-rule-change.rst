.. -*- coding: utf-8; mode: rst -*-

.. _API-audit-rule-change:

=================
audit_rule_change
=================

*man audit_rule_change(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
