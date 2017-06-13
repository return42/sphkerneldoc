.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/nlattr.c

.. _`nla_validate`:

nla_validate
============

.. c:function:: int nla_validate(const struct nlattr *head, int len, int maxtype, const struct nla_policy *policy, struct netlink_ext_ack *extack)

    Validate a stream of attributes

    :param const struct nlattr \*head:
        head of attribute stream

    :param int len:
        length of attribute stream

    :param int maxtype:
        maximum attribute type to be expected

    :param const struct nla_policy \*policy:
        validation policy

    :param struct netlink_ext_ack \*extack:
        extended ACK report struct

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

    :param const struct nla_policy \*p:
        *undescribed*

    :param int n:
        number of policies

.. _`nla_policy_len.description`:

Description
-----------

Determines the max. length of the policy.  It is currently used
to allocated Netlink buffers roughly the size of the actual
message.

Returns 0 on success or a negative error code.

.. _`nla_parse`:

nla_parse
=========

.. c:function:: int nla_parse(struct nlattr **tb, int maxtype, const struct nlattr *head, int len, const struct nla_policy *policy, struct netlink_ext_ack *extack)

    Parse a stream of attributes into a tb buffer

    :param struct nlattr \*\*tb:
        destination array with maxtype+1 elements

    :param int maxtype:
        maximum attribute type to be expected

    :param const struct nlattr \*head:
        head of attribute stream

    :param int len:
        length of attribute stream

    :param const struct nla_policy \*policy:
        validation policy

    :param struct netlink_ext_ack \*extack:
        *undescribed*

.. _`nla_parse.description`:

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

    :param const struct nlattr \*head:
        head of attribute stream

    :param int len:
        length of attribute stream

    :param int attrtype:
        type of attribute to look for

.. _`nla_find.description`:

Description
-----------

Returns the first attribute in the stream matching the specified type.

.. _`nla_strlcpy`:

nla_strlcpy
===========

.. c:function:: size_t nla_strlcpy(char *dst, const struct nlattr *nla, size_t dstsize)

    Copy string attribute payload into a sized buffer

    :param char \*dst:
        where to copy the string to

    :param const struct nlattr \*nla:
        attribute to copy the string from

    :param size_t dstsize:
        size of destination buffer

.. _`nla_strlcpy.description`:

Description
-----------

Copies at most dstsize - 1 bytes into the destination buffer.
The result is always a valid NUL-terminated string. Unlike
strlcpy the destination buffer is always padded out.

Returns the length of the source buffer.

.. _`nla_memcpy`:

nla_memcpy
==========

.. c:function:: int nla_memcpy(void *dest, const struct nlattr *src, int count)

    Copy a netlink attribute into another memory area

    :param void \*dest:
        where to copy to memcpy

    :param const struct nlattr \*src:
        netlink attribute to copy from

    :param int count:
        size of the destination area

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

    :param const struct nlattr \*nla:
        netlink attribute

    :param const void \*data:
        memory area

    :param size_t size:
        size of memory area

.. _`nla_strcmp`:

nla_strcmp
==========

.. c:function:: int nla_strcmp(const struct nlattr *nla, const char *str)

    Compare a string attribute against a string

    :param const struct nlattr \*nla:
        netlink string attribute

    :param const char \*str:
        another string

.. _`__nla_reserve`:

__nla_reserve
=============

.. c:function:: struct nlattr *__nla_reserve(struct sk_buff *skb, int attrtype, int attrlen)

    reserve room for attribute on the skb

    :param struct sk_buff \*skb:
        socket buffer to reserve room on

    :param int attrtype:
        attribute type

    :param int attrlen:
        length of attribute payload

.. _`__nla_reserve.description`:

Description
-----------

Adds a netlink attribute header to a socket buffer and reserves
room for the payload but does not copy it.

The caller is responsible to ensure that the skb provides enough
tailroom for the attribute header and payload.

.. _`__nla_reserve_64bit`:

__nla_reserve_64bit
===================

.. c:function:: struct nlattr *__nla_reserve_64bit(struct sk_buff *skb, int attrtype, int attrlen, int padattr)

    reserve room for attribute on the skb and align it

    :param struct sk_buff \*skb:
        socket buffer to reserve room on

    :param int attrtype:
        attribute type

    :param int attrlen:
        length of attribute payload

    :param int padattr:
        attribute type for the padding

.. _`__nla_reserve_64bit.description`:

Description
-----------

Adds a netlink attribute header to a socket buffer and reserves
room for the payload but does not copy it. It also ensure that this
attribute will have a 64-bit aligned \ :c:func:`nla_data`\  area.

The caller is responsible to ensure that the skb provides enough
tailroom for the attribute header and payload.

.. _`__nla_reserve_nohdr`:

__nla_reserve_nohdr
===================

.. c:function:: void *__nla_reserve_nohdr(struct sk_buff *skb, int attrlen)

    reserve room for attribute without header

    :param struct sk_buff \*skb:
        socket buffer to reserve room on

    :param int attrlen:
        length of attribute payload

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

    :param struct sk_buff \*skb:
        socket buffer to reserve room on

    :param int attrtype:
        attribute type

    :param int attrlen:
        length of attribute payload

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

    :param struct sk_buff \*skb:
        socket buffer to reserve room on

    :param int attrtype:
        attribute type

    :param int attrlen:
        length of attribute payload

    :param int padattr:
        attribute type for the padding

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

    :param struct sk_buff \*skb:
        socket buffer to reserve room on

    :param int attrlen:
        length of attribute payload

.. _`nla_reserve_nohdr.description`:

Description
-----------

Reserves room for attribute payload without a header.

Returns NULL if the tailroom of the skb is insufficient to store
the attribute payload.

.. _`__nla_put`:

__nla_put
=========

.. c:function:: void __nla_put(struct sk_buff *skb, int attrtype, int attrlen, const void *data)

    Add a netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param int attrlen:
        length of attribute payload

    :param const void \*data:
        head of attribute payload

.. _`__nla_put.description`:

Description
-----------

The caller is responsible to ensure that the skb provides enough
tailroom for the attribute header and payload.

.. _`__nla_put_64bit`:

__nla_put_64bit
===============

.. c:function:: void __nla_put_64bit(struct sk_buff *skb, int attrtype, int attrlen, const void *data, int padattr)

    Add a netlink attribute to a socket buffer and align it

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param int attrlen:
        length of attribute payload

    :param const void \*data:
        head of attribute payload

    :param int padattr:
        attribute type for the padding

.. _`__nla_put_64bit.description`:

Description
-----------

The caller is responsible to ensure that the skb provides enough
tailroom for the attribute header and payload.

.. _`__nla_put_nohdr`:

__nla_put_nohdr
===============

.. c:function:: void __nla_put_nohdr(struct sk_buff *skb, int attrlen, const void *data)

    Add a netlink attribute without header

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrlen:
        length of attribute payload

    :param const void \*data:
        head of attribute payload

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

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param int attrlen:
        length of attribute payload

    :param const void \*data:
        head of attribute payload

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

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param int attrlen:
        length of attribute payload

    :param const void \*data:
        head of attribute payload

    :param int padattr:
        attribute type for the padding

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

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrlen:
        length of attribute payload

    :param const void \*data:
        head of attribute payload

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

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrlen:
        length of attribute payload

    :param const void \*data:
        head of attribute payload

.. _`nla_append.description`:

Description
-----------

Returns -EMSGSIZE if the tailroom of the skb is insufficient to store
the attribute payload.

.. This file was automatic generated / don't edit.

