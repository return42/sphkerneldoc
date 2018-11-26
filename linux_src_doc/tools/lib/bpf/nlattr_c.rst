.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/bpf/nlattr.c

.. _`libbpf_nla_parse`:

libbpf_nla_parse
================

.. c:function:: int libbpf_nla_parse(struct nlattr  *tb, int maxtype, struct nlattr *head, int len, struct libbpf_nla_policy *policy)

    \ ``arg``\  tb              Index array to be filled (maxtype+1 elements). \ ``arg``\  maxtype         Maximum attribute type expected and accepted. \ ``arg``\  head            Head of attribute stream. \ ``arg``\  len             Length of attribute stream. \ ``arg``\  policy          Attribute validation policy.

    :param tb:
        *undescribed*
    :type tb: struct nlattr  \*

    :param maxtype:
        *undescribed*
    :type maxtype: int

    :param head:
        *undescribed*
    :type head: struct nlattr \*

    :param len:
        *undescribed*
    :type len: int

    :param policy:
        *undescribed*
    :type policy: struct libbpf_nla_policy \*

.. _`libbpf_nla_parse.description`:

Description
-----------

Iterates over the stream of attributes and stores a pointer to each
attribute in the index array using the attribute type as index to
the array. Attribute with a type greater than the maximum type
specified will be silently ignored in order to maintain backwards
compatibility. If \a policy is not NULL, the attribute will be
validated using the specified policy.

\ ``see``\  nla_validate
\ ``return``\  0 on success or a negative error code.

.. _`libbpf_nla_parse_nested`:

libbpf_nla_parse_nested
=======================

.. c:function:: int libbpf_nla_parse_nested(struct nlattr  *tb, int maxtype, struct nlattr *nla, struct libbpf_nla_policy *policy)

    \ ``arg``\  tb              Index array to be filled (maxtype+1 elements). \ ``arg``\  maxtype         Maximum attribute type expected and accepted. \ ``arg``\  nla             Nested Attribute. \ ``arg``\  policy          Attribute validation policy.

    :param tb:
        *undescribed*
    :type tb: struct nlattr  \*

    :param maxtype:
        *undescribed*
    :type maxtype: int

    :param nla:
        *undescribed*
    :type nla: struct nlattr \*

    :param policy:
        *undescribed*
    :type policy: struct libbpf_nla_policy \*

.. _`libbpf_nla_parse_nested.description`:

Description
-----------

Feeds the stream of attributes nested into the specified attribute
to \ :c:func:`libbpf_nla_parse`\ .

\ ``see``\  libbpf_nla_parse
\ ``return``\  0 on success or a negative error code.

.. This file was automatic generated / don't edit.

