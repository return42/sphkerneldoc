.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_user.h

.. _`netlbl_netlink_auditinfo`:

netlbl_netlink_auditinfo
========================

.. c:function:: void netlbl_netlink_auditinfo(struct sk_buff *skb, struct netlbl_audit *audit_info)

    Fetch the audit information from a NETLINK msg

    :param skb:
        the packet
    :type skb: struct sk_buff \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. This file was automatic generated / don't edit.

