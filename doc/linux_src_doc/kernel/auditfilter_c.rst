.. -*- coding: utf-8; mode: rst -*-

=============
auditfilter.c
=============

.. _`audit_rule_change`:

audit_rule_change
=================

.. c:function:: int audit_rule_change (int type, __u32 portid, int seq, void *data, size_t datasz)

    apply all rules to the specified message type

    :param int type:
        audit message type

    :param __u32 portid:
        target port id for netlink audit messages

    :param int seq:
        netlink audit message sequence (serial) number

    :param void \*data:
        payload data

    :param size_t datasz:
        size of payload data


.. _`audit_list_rules_send`:

audit_list_rules_send
=====================

.. c:function:: int audit_list_rules_send (struct sk_buff *request_skb, int seq)

    list the audit rules

    :param struct sk_buff \*request_skb:
        skb of request we are replying to (used to target the reply)

    :param int seq:
        netlink audit message sequence (serial) number


.. _`parent_len`:

parent_len
==========

.. c:function:: int parent_len (const char *path)

    find the length of the parent portion of a pathname

    :param const char \*path:
        pathname of which to determine length


.. _`audit_compare_dname_path`:

audit_compare_dname_path
========================

.. c:function:: int audit_compare_dname_path (const char *dname, const char *path, int parentlen)

    compare given dentry name with last component in given path. Return of 0 indicates a match.

    :param const char \*dname:
        dentry name that we're comparing

    :param const char \*path:
        full pathname that we're comparing

    :param int parentlen:
        length of the parent if known. Passing in AUDIT_NAME_FULL
        here indicates that we must compute this value.

