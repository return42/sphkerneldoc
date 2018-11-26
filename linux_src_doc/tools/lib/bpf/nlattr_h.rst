.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/bpf/nlattr.h

.. _`libbpf_nla_data`:

libbpf_nla_data
===============

.. c:function:: void *libbpf_nla_data(const struct nlattr *nla)

    head of payload

    :param nla:
        netlink attribute
    :type nla: const struct nlattr \*

.. _`libbpf_nla_len`:

libbpf_nla_len
==============

.. c:function:: int libbpf_nla_len(const struct nlattr *nla)

    length of payload

    :param nla:
        netlink attribute
    :type nla: const struct nlattr \*

.. This file was automatic generated / don't edit.

