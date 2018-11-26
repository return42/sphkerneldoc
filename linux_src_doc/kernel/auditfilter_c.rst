.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/auditfilter.c

.. _`audit_rule_change`:

audit_rule_change
=================

.. c:function:: int audit_rule_change(int type, int seq, void *data, size_t datasz)

    apply all rules to the specified message type

    :param type:
        audit message type
    :type type: int

    :param seq:
        netlink audit message sequence (serial) number
    :type seq: int

    :param data:
        payload data
    :type data: void \*

    :param datasz:
        size of payload data
    :type datasz: size_t

.. _`audit_list_rules_send`:

audit_list_rules_send
=====================

.. c:function:: int audit_list_rules_send(struct sk_buff *request_skb, int seq)

    list the audit rules

    :param request_skb:
        skb of request we are replying to (used to target the reply)
    :type request_skb: struct sk_buff \*

    :param seq:
        netlink audit message sequence (serial) number
    :type seq: int

.. _`parent_len`:

parent_len
==========

.. c:function:: int parent_len(const char *path)

    find the length of the parent portion of a pathname

    :param path:
        pathname of which to determine length
    :type path: const char \*

.. _`audit_compare_dname_path`:

audit_compare_dname_path
========================

.. c:function:: int audit_compare_dname_path(const char *dname, const char *path, int parentlen)

    compare given dentry name with last component in given path. Return of 0 indicates a match.

    :param dname:
        dentry name that we're comparing
    :type dname: const char \*

    :param path:
        full pathname that we're comparing
    :type path: const char \*

    :param parentlen:
        length of the parent if known. Passing in AUDIT_NAME_FULL
        here indicates that we must compute this value.
    :type parentlen: int

.. This file was automatic generated / don't edit.

