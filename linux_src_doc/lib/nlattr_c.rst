.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/nlattr.c

.. _`nla_validate`:

nla_validate
============

.. c:function:: int nla_validate(const struct nlattr *head, int len, int maxtype, const struct nla_policy *policy, struct netlink_ext_ack *extack)

    Validate a stream of attributes

    :param head:
        head of attribute stream
    :type head: const struct nlattr \*

    :param len:
        length of attribute stream
    :type len: int

    :param maxtype:
        maximum attribute type to be expected
    :type maxtype: int

    :param policy:
        validation policy
    :type policy: const struct nla_policy \*

    :param extack:
        extended ACK report struct
    :type extack: struct netlink_ext_ack \*

.. _`nla_validate.description`:

Description
-----------

Validates all attributes in the specified attribute stream against the
specified policy. Attributes with a type exceeding maxtype will be
ignored. See documenation of struct nla_policy for more details.

Returns 0 on success or a negative error code.

.. _`nla_policy_len`:

nla_policy_len
==============

.. c:function:: int nla_policy_len(const struct nla_policy *p, int n)

    Determin the max. length of a policy

    :param p:
        *undescribed*
    :type p: const struct nla_policy \*

    :param n:
        number of policies
    :type n: int

.. _`nla_policy_len.description`:

Description
-----------

Determines the max. length of the policy.  It is currently used
to allocated Netlink buffers roughly the size of the actual
message.

Returns 0 on success or a negative error code.

.. _`__nla_parse`:

\__nla_parse
============

.. c:function:: int __nla_parse(struct nlattr **tb, int maxtype, const struct nlattr *head, int len, bool strict, const struct nla_policy *policy, struct netlink_ext_ack *extack)

    Parse a stream of attributes into a tb buffer

    :param tb:
        destination array with maxtype+1 elements
    :type tb: struct nlattr \*\*

    :param maxtype:
        maximum attribute type to be expected
    :type maxtype: int

    :param head:
        head of attribute stream
    :type head: const struct nlattr \*

    :param len:
        length of attribute stream
    :type len: int

    :param strict:
        *undescribed*
    :type strict: bool

    :param policy:
        validation policy
    :type policy: const struct nla_policy \*

    :param extack:
        *undescribed*
    :type extack: struct netlink_ext_ack \*

.. _`__nla_parse.description`:

Description
-----------

Parses a stream of attributes and stores a pointer to each attribute in
the tb array accessible via the attribute type. Attributes with a type
exceeding maxtype will be silently ignored for backwards compatibility
reasons. policy may be set to NULL if no validation is required.

Returns 0 on success or a negative error code.

.. _`nla_find`:

nla_find
========

.. c:function:: struct nlattr *nla_find(const struct nlattr *head, int len, int attrtype)

    Find a specific attribute in a stream of attributes

    :param head:
        head of attribute stream
    :type head: const struct nlattr \*

    :param len:
        length of attribute stream
    :type len: int

    :param attrtype:
        type of attribute to look for
    :type attrtype: int

.. _`nla_find.description`:

Description
-----------

Returns the first attribute in the stream matching the specified type.

.. _`nla_strlcpy`:

nla_strlcpy
===========

.. c:function:: size_t nla_strlcpy(char *dst, const struct nlattr *nla, size_t dstsize)

    Copy string attribute payload into a sized buffer

    :param dst:
        where to copy the string to
    :type dst: char \*

    :param nla:
        attribute to copy the string from
    :type nla: const struct nlattr \*

    :param dstsize:
        size of destination buffer
    :type dstsize: size_t

.. _`nla_strlcpy.description`:

Description
-----------

Copies at most dstsize - 1 bytes into the destination buffer.
The result is always a valid NUL-terminated string. Unlike
strlcpy the destination buffer is always padded out.

Returns the length of the source buffer.

.. _`nla_strdup`:

nla_strdup
==========

.. c:function:: char *nla_strdup(const struct nlattr *nla, gfp_t flags)

    Copy string attribute payload into a newly allocated buffer

    :param nla:
        attribute to copy the string from
    :type nla: const struct nlattr \*

    :param flags:
        the type of memory to allocate (see kmalloc).
    :type flags: gfp_t

.. _`nla_strdup.description`:

Description
-----------

Returns a pointer to the allocated buffer or NULL on error.

.. _`nla_memcpy`:

nla_memcpy
==========

.. c:function:: int nla_memcpy(void *dest, const struct nlattr *src, int count)

    Copy a netlink attribute into another memory area

    :param dest:
        where to copy to memcpy
    :type dest: void \*

    :param src:
        netlink attribute to copy from
    :type src: const struct nlattr \*

    :param count:
        size of the destination area
    :type count: int

.. _`nla_memcpy.note`:

Note
----

The number of bytes copied is limited by the length of
attribute's payload. memcpy

Returns the number of bytes copied.

.. _`nla_memcmp`:

nla_memcmp
==========

.. c:function:: int nla_memcmp(const struct nlattr *nla, const void *data, size_t size)

    Compare an attribute with sized memory area

    :param nla:
        netlink attribute
    :type nla: const struct nlattr \*

    :param data:
        memory area
    :type data: const void \*

    :param size:
        size of memory area
    :type size: size_t

.. _`nla_strcmp`:

nla_strcmp
==========

.. c:function:: int nla_strcmp(const struct nlattr *nla, const char *str)

    Compare a string attribute against a string

    :param nla:
        netlink string attribute
    :type nla: const struct nlattr \*

    :param str:
        another string
    :type str: const char \*

.. _`__nla_reserve`:

\__nla_reserve
==============

.. c:function:: struct nlattr *__nla_reserve(struct sk_buff *skb, int attrtype, int attrlen)

    reserve room for attribute on the skb

    :param skb:
        socket buffer to reserve room on
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param attrlen:
        length of attribute payload
    :type attrlen: int

.. _`__nla_reserve.description`:

Description
-----------

Adds a netlink attribute header to a socket buffer and reserves
room for the payload but does not copy it.

The caller is responsible to ensure that the skb provides enough
tailroom for the attribute header and payload.

.. _`__nla_reserve_64bit`:

\__nla_reserve_64bit
====================

.. c:function:: struct nlattr *__nla_reserve_64bit(struct sk_buff *skb, int attrtype, int attrlen, int padattr)

    reserve room for attribute on the skb and align it

    :param skb:
        socket buffer to reserve room on
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param attrlen:
        length of attribute payload
    :type attrlen: int

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`__nla_reserve_64bit.description`:

Description
-----------

Adds a netlink attribute header to a socket buffer and reserves
room for the payload but does not copy it. It also ensure that this
attribute will have a 64-bit aligned \ :c:func:`nla_data`\  area.

The caller is responsible to ensure that the skb provides enough
tailroom for the attribute header and payload.

.. _`__nla_reserve_nohdr`:

\__nla_reserve_nohdr
====================

.. c:function:: void *__nla_reserve_nohdr(struct sk_buff *skb, int attrlen)

    reserve room for attribute without header

    :param skb:
        socket buffer to reserve room on
    :type skb: struct sk_buff \*

    :param attrlen:
        length of attribute payload
    :type attrlen: int

.. _`__nla_reserve_nohdr.description`:

Description
-----------

Reserves room for attribute payload without a header.

The caller is responsible to ensure that the skb provides enough
tailroom for the payload.

.. _`nla_reserve`:

nla_reserve
===========

.. c:function:: struct nlattr *nla_reserve(struct sk_buff *skb, int attrtype, int attrlen)

    reserve room for attribute on the skb

    :param skb:
        socket buffer to reserve room on
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param attrlen:
        length of attribute payload
    :type attrlen: int

.. _`nla_reserve.description`:

Description
-----------

Adds a netlink attribute header to a socket buffer and reserves
room for the payload but does not copy it.

Returns NULL if the tailroom of the skb is insufficient to store
the attribute header and payload.

.. _`nla_reserve_64bit`:

nla_reserve_64bit
=================

.. c:function:: struct nlattr *nla_reserve_64bit(struct sk_buff *skb, int attrtype, int attrlen, int padattr)

    reserve room for attribute on the skb and align it

    :param skb:
        socket buffer to reserve room on
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param attrlen:
        length of attribute payload
    :type attrlen: int

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`nla_reserve_64bit.description`:

Description
-----------

Adds a netlink attribute header to a socket buffer and reserves
room for the payload but does not copy it. It also ensure that this
attribute will have a 64-bit aligned \ :c:func:`nla_data`\  area.

Returns NULL if the tailroom of the skb is insufficient to store
the attribute header and payload.

.. _`nla_reserve_nohdr`:

nla_reserve_nohdr
=================

.. c:function:: void *nla_reserve_nohdr(struct sk_buff *skb, int attrlen)

    reserve room for attribute without header

    :param skb:
        socket buffer to reserve room on
    :type skb: struct sk_buff \*

    :param attrlen:
        length of attribute payload
    :type attrlen: int

.. _`nla_reserve_nohdr.description`:

Description
-----------

Reserves room for attribute payload without a header.

Returns NULL if the tailroom of the skb is insufficient to store
the attribute payload.

.. _`__nla_put`:

\__nla_put
==========

.. c:function:: void __nla_put(struct sk_buff *skb, int attrtype, int attrlen, const void *data)

    Add a netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param attrlen:
        length of attribute payload
    :type attrlen: int

    :param data:
        head of attribute payload
    :type data: const void \*

.. _`__nla_put.description`:

Description
-----------

The caller is responsible to ensure that the skb provides enough
tailroom for the attribute header and payload.

.. _`__nla_put_64bit`:

\__nla_put_64bit
================

.. c:function:: void __nla_put_64bit(struct sk_buff *skb, int attrtype, int attrlen, const void *data, int padattr)

    Add a netlink attribute to a socket buffer and align it

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param attrlen:
        length of attribute payload
    :type attrlen: int

    :param data:
        head of attribute payload
    :type data: const void \*

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`__nla_put_64bit.description`:

Description
-----------

The caller is responsible to ensure that the skb provides enough
tailroom for the attribute header and payload.

.. _`__nla_put_nohdr`:

\__nla_put_nohdr
================

.. c:function:: void __nla_put_nohdr(struct sk_buff *skb, int attrlen, const void *data)

    Add a netlink attribute without header

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrlen:
        length of attribute payload
    :type attrlen: int

    :param data:
        head of attribute payload
    :type data: const void \*

.. _`__nla_put_nohdr.description`:

Description
-----------

The caller is responsible to ensure that the skb provides enough
tailroom for the attribute payload.

.. _`nla_put`:

nla_put
=======

.. c:function:: int nla_put(struct sk_buff *skb, int attrtype, int attrlen, const void *data)

    Add a netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param attrlen:
        length of attribute payload
    :type attrlen: int

    :param data:
        head of attribute payload
    :type data: const void \*

.. _`nla_put.description`:

Description
-----------

Returns -EMSGSIZE if the tailroom of the skb is insufficient to store
the attribute header and payload.

.. _`nla_put_64bit`:

nla_put_64bit
=============

.. c:function:: int nla_put_64bit(struct sk_buff *skb, int attrtype, int attrlen, const void *data, int padattr)

    Add a netlink attribute to a socket buffer and align it

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param attrlen:
        length of attribute payload
    :type attrlen: int

    :param data:
        head of attribute payload
    :type data: const void \*

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`nla_put_64bit.description`:

Description
-----------

Returns -EMSGSIZE if the tailroom of the skb is insufficient to store
the attribute header and payload.

.. _`nla_put_nohdr`:

nla_put_nohdr
=============

.. c:function:: int nla_put_nohdr(struct sk_buff *skb, int attrlen, const void *data)

    Add a netlink attribute without header

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrlen:
        length of attribute payload
    :type attrlen: int

    :param data:
        head of attribute payload
    :type data: const void \*

.. _`nla_put_nohdr.description`:

Description
-----------

Returns -EMSGSIZE if the tailroom of the skb is insufficient to store
the attribute payload.

.. _`nla_append`:

nla_append
==========

.. c:function:: int nla_append(struct sk_buff *skb, int attrlen, const void *data)

    Add a netlink attribute without header or padding

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrlen:
        length of attribute payload
    :type attrlen: int

    :param data:
        head of attribute payload
    :type data: const void \*

.. _`nla_append.description`:

Description
-----------

Returns -EMSGSIZE if the tailroom of the skb is insufficient to store
the attribute payload.

.. This file was automatic generated / don't edit.

