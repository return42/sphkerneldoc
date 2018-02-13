.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/bpf/nlattr.c

.. _`nla_parse`:

nla_parse
=========

.. c:function:: int nla_parse(struct nlattr  *tb, int maxtype, struct nlattr *head, int len, struct nla_policy *policy)

    \ ``arg``\  tb              Index array to be filled (maxtype+1 elements). \ ``arg``\  maxtype         Maximum attribute type expected and accepted. \ ``arg``\  head            Head of attribute stream. \ ``arg``\  len             Length of attribute stream. \ ``arg``\  policy          Attribute validation policy.

    :param struct nlattr  \*tb:
        *undescribed*

    :param int maxtype:
        *undescribed*

    :param struct nlattr \*head:
        *undescribed*

    :param int len:
        *undescribed*

    :param struct nla_policy \*policy:
        *undescribed*

.. _`nla_parse.description`:

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

.. This file was automatic generated / don't edit.

