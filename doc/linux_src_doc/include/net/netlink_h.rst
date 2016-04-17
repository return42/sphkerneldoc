.. -*- coding: utf-8; mode: rst -*-

=========
netlink.h
=========


.. _`nla_policy`:

struct nla_policy
=================

.. c:type:: nla_policy

    attribute validation policy


.. _`nla_policy.definition`:

Definition
----------

.. code-block:: c

  struct nla_policy {
    u16 type;
    u16 len;
  };


.. _`nla_policy.members`:

Members
-------

:``type``:
    Type of attribute or NLA_UNSPEC

:``len``:
    Type specific length of payload




.. _`nla_policy.description`:

Description
-----------

Policies are defined as arrays of this struct, the array must be
accessible by attribute type up to the highest identifier to be expected.

Meaning of `len' field::

   NLA_STRING           Maximum length of string
   NLA_NUL_STRING       Maximum length of string (excluding NUL)
   NLA_FLAG             Unused
   NLA_BINARY           Maximum length of attribute payload
   NLA_NESTED           Don't use `len' field -- length verification is
                        done by checking len of nested header (or empty)
   NLA_NESTED_COMPAT    Minimum length of structure payload
   NLA_U8, NLA_U16,
   NLA_U32, NLA_U64,
   NLA_S8, NLA_S16,
   NLA_S32, NLA_S64,
   NLA_MSECS            Leaving the length field zero will verify the
                        given type fits, using it verifies minimum length
                        just like "All other"
   All other            Minimum length of attribute payload



.. _`nla_policy.example`:

Example
-------

.. code-block:: c

static const struct nla_policy my_policy[ATTR_MAX+1] = {
	[ATTR_FOO] = { .type = NLA_U16 },
	[ATTR_BAR] = { .type = NLA_STRING, .len = BARSIZ },
	[ATTR_BAZ] = { .len = sizeof(struct mystruct) },
};



.. _`nl_info`:

struct nl_info
==============

.. c:type:: nl_info

    netlink source information


.. _`nl_info.definition`:

Definition
----------

.. code-block:: c

  struct nl_info {
    struct nlmsghdr * nlh;
    u32 portid;
  };


.. _`nl_info.members`:

Members
-------

:``nlh``:
    Netlink message header of original request

:``portid``:
    Netlink PORTID of requesting application




.. _`nlmsg_msg_size`:

nlmsg_msg_size
==============

.. c:function:: int nlmsg_msg_size (int payload)

    length of netlink message not including padding

    :param int payload:
        length of message payload



.. _`nlmsg_total_size`:

nlmsg_total_size
================

.. c:function:: int nlmsg_total_size (int payload)

    length of netlink message including padding

    :param int payload:
        length of message payload



.. _`nlmsg_padlen`:

nlmsg_padlen
============

.. c:function:: int nlmsg_padlen (int payload)

    length of padding at the message's tail

    :param int payload:
        length of message payload



.. _`nlmsg_data`:

nlmsg_data
==========

.. c:function:: void *nlmsg_data (const struct nlmsghdr *nlh)

    head of message payload

    :param const struct nlmsghdr \*nlh:
        netlink message header



.. _`nlmsg_len`:

nlmsg_len
=========

.. c:function:: int nlmsg_len (const struct nlmsghdr *nlh)

    length of message payload

    :param const struct nlmsghdr \*nlh:
        netlink message header



.. _`nlmsg_attrdata`:

nlmsg_attrdata
==============

.. c:function:: struct nlattr *nlmsg_attrdata (const struct nlmsghdr *nlh, int hdrlen)

    head of attributes data

    :param const struct nlmsghdr \*nlh:
        netlink message header

    :param int hdrlen:
        length of family specific header



.. _`nlmsg_attrlen`:

nlmsg_attrlen
=============

.. c:function:: int nlmsg_attrlen (const struct nlmsghdr *nlh, int hdrlen)

    length of attributes data

    :param const struct nlmsghdr \*nlh:
        netlink message header

    :param int hdrlen:
        length of family specific header



.. _`nlmsg_ok`:

nlmsg_ok
========

.. c:function:: int nlmsg_ok (const struct nlmsghdr *nlh, int remaining)

    check if the netlink message fits into the remaining bytes

    :param const struct nlmsghdr \*nlh:
        netlink message header

    :param int remaining:
        number of bytes remaining in message stream



.. _`nlmsg_next`:

nlmsg_next
==========

.. c:function:: struct nlmsghdr *nlmsg_next (const struct nlmsghdr *nlh, int *remaining)

    next netlink message in message stream

    :param const struct nlmsghdr \*nlh:
        netlink message header

    :param int \*remaining:
        number of bytes remaining in message stream



.. _`nlmsg_next.description`:

Description
-----------

Returns the next netlink message in the message stream and
decrements remaining by the size of the current message.



.. _`nlmsg_parse`:

nlmsg_parse
===========

.. c:function:: int nlmsg_parse (const struct nlmsghdr *nlh, int hdrlen, struct nlattr *tb[], int maxtype, const struct nla_policy *policy)

    parse attributes of a netlink message

    :param const struct nlmsghdr \*nlh:
        netlink message header

    :param int hdrlen:
        length of family specific header

    :param struct nlattr \*tb:
        destination array with maxtype+1 elements

    :param int maxtype:
        maximum attribute type to be expected

    :param const struct nla_policy \*policy:
        validation policy



.. _`nlmsg_parse.description`:

Description
-----------

See :c:func:`nla_parse`



.. _`nlmsg_find_attr`:

nlmsg_find_attr
===============

.. c:function:: struct nlattr *nlmsg_find_attr (const struct nlmsghdr *nlh, int hdrlen, int attrtype)

    find a specific attribute in a netlink message

    :param const struct nlmsghdr \*nlh:
        netlink message header

    :param int hdrlen:
        length of familiy specific header

    :param int attrtype:
        type of attribute to look for



.. _`nlmsg_find_attr.description`:

Description
-----------

Returns the first attribute which matches the specified type.



.. _`nlmsg_validate`:

nlmsg_validate
==============

.. c:function:: int nlmsg_validate (const struct nlmsghdr *nlh, int hdrlen, int maxtype, const struct nla_policy *policy)

    validate a netlink message including attributes

    :param const struct nlmsghdr \*nlh:
        netlinket message header

    :param int hdrlen:
        length of familiy specific header

    :param int maxtype:
        maximum attribute type to be expected

    :param const struct nla_policy \*policy:
        validation policy



.. _`nlmsg_report`:

nlmsg_report
============

.. c:function:: int nlmsg_report (const struct nlmsghdr *nlh)

    need to report back to application?

    :param const struct nlmsghdr \*nlh:
        netlink message header



.. _`nlmsg_report.description`:

Description
-----------

Returns 1 if a report back to the application is requested.



.. _`nlmsg_for_each_attr`:

nlmsg_for_each_attr
===================

.. c:function:: nlmsg_for_each_attr ( pos,  nlh,  hdrlen,  rem)

    iterate over a stream of attributes

    :param pos:
        loop counter, set to current attribute

    :param nlh:
        netlink message header

    :param hdrlen:
        length of familiy specific header

    :param rem:
        initialized to len, holds bytes currently remaining in stream



.. _`nlmsg_put`:

nlmsg_put
=========

.. c:function:: struct nlmsghdr *nlmsg_put (struct sk_buff *skb, u32 portid, u32 seq, int type, int payload, int flags)

    Add a new netlink message to an skb

    :param struct sk_buff \*skb:
        socket buffer to store message in

    :param u32 portid:
        netlink PORTID of requesting application

    :param u32 seq:
        sequence number of message

    :param int type:
        message type

    :param int payload:
        length of message payload

    :param int flags:
        message flags



.. _`nlmsg_put.description`:

Description
-----------

Returns NULL if the tailroom of the skb is insufficient to store
the message header and payload.



.. _`nlmsg_put_answer`:

nlmsg_put_answer
================

.. c:function:: struct nlmsghdr *nlmsg_put_answer (struct sk_buff *skb, struct netlink_callback *cb, int type, int payload, int flags)

    Add a new callback based netlink message to an skb

    :param struct sk_buff \*skb:
        socket buffer to store message in

    :param struct netlink_callback \*cb:
        netlink callback

    :param int type:
        message type

    :param int payload:
        length of message payload

    :param int flags:
        message flags



.. _`nlmsg_put_answer.description`:

Description
-----------

Returns NULL if the tailroom of the skb is insufficient to store
the message header and payload.



.. _`nlmsg_new`:

nlmsg_new
=========

.. c:function:: struct sk_buff *nlmsg_new (size_t payload, gfp_t flags)

    Allocate a new netlink message

    :param size_t payload:
        size of the message payload

    :param gfp_t flags:
        the type of memory to allocate.



.. _`nlmsg_new.description`:

Description
-----------

Use NLMSG_DEFAULT_SIZE if the size of the payload isn't known
and a good default is needed.



.. _`nlmsg_end`:

nlmsg_end
=========

.. c:function:: void nlmsg_end (struct sk_buff *skb, struct nlmsghdr *nlh)

    Finalize a netlink message

    :param struct sk_buff \*skb:
        socket buffer the message is stored in

    :param struct nlmsghdr \*nlh:
        netlink message header



.. _`nlmsg_end.description`:

Description
-----------

Corrects the netlink message header to include the appeneded
attributes. Only necessary if attributes have been added to
the message.



.. _`nlmsg_get_pos`:

nlmsg_get_pos
=============

.. c:function:: void *nlmsg_get_pos (struct sk_buff *skb)

    return current position in netlink message

    :param struct sk_buff \*skb:
        socket buffer the message is stored in



.. _`nlmsg_get_pos.description`:

Description
-----------

Returns a pointer to the current tail of the message.



.. _`nlmsg_trim`:

nlmsg_trim
==========

.. c:function:: void nlmsg_trim (struct sk_buff *skb, const void *mark)

    Trim message to a mark

    :param struct sk_buff \*skb:
        socket buffer the message is stored in

    :param const void \*mark:
        mark to trim to



.. _`nlmsg_trim.description`:

Description
-----------

Trims the message to the provided mark.



.. _`nlmsg_cancel`:

nlmsg_cancel
============

.. c:function:: void nlmsg_cancel (struct sk_buff *skb, struct nlmsghdr *nlh)

    Cancel construction of a netlink message

    :param struct sk_buff \*skb:
        socket buffer the message is stored in

    :param struct nlmsghdr \*nlh:
        netlink message header



.. _`nlmsg_cancel.description`:

Description
-----------

Removes the complete netlink message including all
attributes from the socket buffer again.



.. _`nlmsg_free`:

nlmsg_free
==========

.. c:function:: void nlmsg_free (struct sk_buff *skb)

    free a netlink message

    :param struct sk_buff \*skb:
        socket buffer of netlink message



.. _`nlmsg_multicast`:

nlmsg_multicast
===============

.. c:function:: int nlmsg_multicast (struct sock *sk, struct sk_buff *skb, u32 portid, unsigned int group, gfp_t flags)

    multicast a netlink message

    :param struct sock \*sk:
        netlink socket to spread messages to

    :param struct sk_buff \*skb:
        netlink message as socket buffer

    :param u32 portid:
        own netlink portid to avoid sending to yourself

    :param unsigned int group:
        multicast group id

    :param gfp_t flags:
        allocation flags



.. _`nlmsg_unicast`:

nlmsg_unicast
=============

.. c:function:: int nlmsg_unicast (struct sock *sk, struct sk_buff *skb, u32 portid)

    unicast a netlink message

    :param struct sock \*sk:
        netlink socket to spread message to

    :param struct sk_buff \*skb:
        netlink message as socket buffer

    :param u32 portid:
        netlink portid of the destination socket



.. _`nlmsg_for_each_msg`:

nlmsg_for_each_msg
==================

.. c:function:: nlmsg_for_each_msg ( pos,  head,  len,  rem)

    iterate over a stream of messages

    :param pos:
        loop counter, set to current message

    :param head:
        head of message stream

    :param len:
        length of message stream

    :param rem:
        initialized to len, holds bytes currently remaining in stream



.. _`nl_dump_check_consistent`:

nl_dump_check_consistent
========================

.. c:function:: void nl_dump_check_consistent (struct netlink_callback *cb, struct nlmsghdr *nlh)

    check if sequence is consistent and advertise if not

    :param struct netlink_callback \*cb:
        netlink callback structure that stores the sequence number

    :param struct nlmsghdr \*nlh:
        netlink message header to write the flag to



.. _`nl_dump_check_consistent.description`:

Description
-----------

This function checks if the sequence (generation) number changed during dump
and if it did, advertises it in the netlink message header.

The correct way to use it is to set cb->seq to the generation counter when
all locks for dumping have been acquired, and then call this function for
each message that is generated.

Note that due to initialisation concerns, 0 is an invalid sequence number
and must not be used by code that uses this functionality.



.. _`nla_attr_size`:

nla_attr_size
=============

.. c:function:: int nla_attr_size (int payload)

    length of attribute not including padding

    :param int payload:
        length of payload



.. _`nla_total_size`:

nla_total_size
==============

.. c:function:: int nla_total_size (int payload)

    total length of attribute including padding

    :param int payload:
        length of payload



.. _`nla_padlen`:

nla_padlen
==========

.. c:function:: int nla_padlen (int payload)

    length of padding at the tail of attribute

    :param int payload:
        length of payload



.. _`nla_type`:

nla_type
========

.. c:function:: int nla_type (const struct nlattr *nla)

    attribute type

    :param const struct nlattr \*nla:
        netlink attribute



.. _`nla_data`:

nla_data
========

.. c:function:: void *nla_data (const struct nlattr *nla)

    head of payload

    :param const struct nlattr \*nla:
        netlink attribute



.. _`nla_len`:

nla_len
=======

.. c:function:: int nla_len (const struct nlattr *nla)

    length of payload

    :param const struct nlattr \*nla:
        netlink attribute



.. _`nla_ok`:

nla_ok
======

.. c:function:: int nla_ok (const struct nlattr *nla, int remaining)

    check if the netlink attribute fits into the remaining bytes

    :param const struct nlattr \*nla:
        netlink attribute

    :param int remaining:
        number of bytes remaining in attribute stream



.. _`nla_next`:

nla_next
========

.. c:function:: struct nlattr *nla_next (const struct nlattr *nla, int *remaining)

    next netlink attribute in attribute stream

    :param const struct nlattr \*nla:
        netlink attribute

    :param int \*remaining:
        number of bytes remaining in attribute stream



.. _`nla_next.description`:

Description
-----------

Returns the next netlink attribute in the attribute stream and
decrements remaining by the size of the current attribute.



.. _`nla_find_nested`:

nla_find_nested
===============

.. c:function:: struct nlattr *nla_find_nested (const struct nlattr *nla, int attrtype)

    find attribute in a set of nested attributes

    :param const struct nlattr \*nla:
        attribute containing the nested attributes

    :param int attrtype:
        type of attribute to look for



.. _`nla_find_nested.description`:

Description
-----------

Returns the first attribute which matches the specified type.



.. _`nla_parse_nested`:

nla_parse_nested
================

.. c:function:: int nla_parse_nested (struct nlattr *tb[], int maxtype, const struct nlattr *nla, const struct nla_policy *policy)

    parse nested attributes

    :param struct nlattr \*tb:
        destination array with maxtype+1 elements

    :param int maxtype:
        maximum attribute type to be expected

    :param const struct nlattr \*nla:
        attribute containing the nested attributes

    :param const struct nla_policy \*policy:
        validation policy



.. _`nla_parse_nested.description`:

Description
-----------

See :c:func:`nla_parse`



.. _`nla_put_u8`:

nla_put_u8
==========

.. c:function:: int nla_put_u8 (struct sk_buff *skb, int attrtype, u8 value)

    Add a u8 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param u8 value:
        numeric value



.. _`nla_put_u16`:

nla_put_u16
===========

.. c:function:: int nla_put_u16 (struct sk_buff *skb, int attrtype, u16 value)

    Add a u16 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param u16 value:
        numeric value



.. _`nla_put_be16`:

nla_put_be16
============

.. c:function:: int nla_put_be16 (struct sk_buff *skb, int attrtype, __be16 value)

    Add a __be16 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __be16 value:
        numeric value



.. _`nla_put_net16`:

nla_put_net16
=============

.. c:function:: int nla_put_net16 (struct sk_buff *skb, int attrtype, __be16 value)

    Add 16-bit network byte order netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __be16 value:
        numeric value



.. _`nla_put_le16`:

nla_put_le16
============

.. c:function:: int nla_put_le16 (struct sk_buff *skb, int attrtype, __le16 value)

    Add a __le16 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __le16 value:
        numeric value



.. _`nla_put_u32`:

nla_put_u32
===========

.. c:function:: int nla_put_u32 (struct sk_buff *skb, int attrtype, u32 value)

    Add a u32 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param u32 value:
        numeric value



.. _`nla_put_be32`:

nla_put_be32
============

.. c:function:: int nla_put_be32 (struct sk_buff *skb, int attrtype, __be32 value)

    Add a __be32 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __be32 value:
        numeric value



.. _`nla_put_net32`:

nla_put_net32
=============

.. c:function:: int nla_put_net32 (struct sk_buff *skb, int attrtype, __be32 value)

    Add 32-bit network byte order netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __be32 value:
        numeric value



.. _`nla_put_le32`:

nla_put_le32
============

.. c:function:: int nla_put_le32 (struct sk_buff *skb, int attrtype, __le32 value)

    Add a __le32 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __le32 value:
        numeric value



.. _`nla_put_u64`:

nla_put_u64
===========

.. c:function:: int nla_put_u64 (struct sk_buff *skb, int attrtype, u64 value)

    Add a u64 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param u64 value:
        numeric value



.. _`nla_put_be64`:

nla_put_be64
============

.. c:function:: int nla_put_be64 (struct sk_buff *skb, int attrtype, __be64 value)

    Add a __be64 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __be64 value:
        numeric value



.. _`nla_put_net64`:

nla_put_net64
=============

.. c:function:: int nla_put_net64 (struct sk_buff *skb, int attrtype, __be64 value)

    Add 64-bit network byte order netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __be64 value:
        numeric value



.. _`nla_put_le64`:

nla_put_le64
============

.. c:function:: int nla_put_le64 (struct sk_buff *skb, int attrtype, __le64 value)

    Add a __le64 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __le64 value:
        numeric value



.. _`nla_put_s8`:

nla_put_s8
==========

.. c:function:: int nla_put_s8 (struct sk_buff *skb, int attrtype, s8 value)

    Add a s8 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param s8 value:
        numeric value



.. _`nla_put_s16`:

nla_put_s16
===========

.. c:function:: int nla_put_s16 (struct sk_buff *skb, int attrtype, s16 value)

    Add a s16 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param s16 value:
        numeric value



.. _`nla_put_s32`:

nla_put_s32
===========

.. c:function:: int nla_put_s32 (struct sk_buff *skb, int attrtype, s32 value)

    Add a s32 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param s32 value:
        numeric value



.. _`nla_put_s64`:

nla_put_s64
===========

.. c:function:: int nla_put_s64 (struct sk_buff *skb, int attrtype, s64 value)

    Add a s64 netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param s64 value:
        numeric value



.. _`nla_put_string`:

nla_put_string
==============

.. c:function:: int nla_put_string (struct sk_buff *skb, int attrtype, const char *str)

    Add a string netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param const char \*str:
        NUL terminated string



.. _`nla_put_flag`:

nla_put_flag
============

.. c:function:: int nla_put_flag (struct sk_buff *skb, int attrtype)

    Add a flag netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type



.. _`nla_put_msecs`:

nla_put_msecs
=============

.. c:function:: int nla_put_msecs (struct sk_buff *skb, int attrtype, unsigned long njiffies)

    Add a msecs netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param unsigned long njiffies:
        number of jiffies to convert to msecs



.. _`nla_put_in_addr`:

nla_put_in_addr
===============

.. c:function:: int nla_put_in_addr (struct sk_buff *skb, int attrtype, __be32 addr)

    Add an IPv4 address netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param __be32 addr:
        IPv4 address



.. _`nla_put_in6_addr`:

nla_put_in6_addr
================

.. c:function:: int nla_put_in6_addr (struct sk_buff *skb, int attrtype, const struct in6_addr *addr)

    Add an IPv6 address netlink attribute to a socket buffer

    :param struct sk_buff \*skb:
        socket buffer to add attribute to

    :param int attrtype:
        attribute type

    :param const struct in6_addr \*addr:
        IPv6 address



.. _`nla_get_u32`:

nla_get_u32
===========

.. c:function:: u32 nla_get_u32 (const struct nlattr *nla)

    return payload of u32 attribute

    :param const struct nlattr \*nla:
        u32 netlink attribute



.. _`nla_get_be32`:

nla_get_be32
============

.. c:function:: __be32 nla_get_be32 (const struct nlattr *nla)

    return payload of __be32 attribute

    :param const struct nlattr \*nla:
        __be32 netlink attribute



.. _`nla_get_le32`:

nla_get_le32
============

.. c:function:: __le32 nla_get_le32 (const struct nlattr *nla)

    return payload of __le32 attribute

    :param const struct nlattr \*nla:
        __le32 netlink attribute



.. _`nla_get_u16`:

nla_get_u16
===========

.. c:function:: u16 nla_get_u16 (const struct nlattr *nla)

    return payload of u16 attribute

    :param const struct nlattr \*nla:
        u16 netlink attribute



.. _`nla_get_be16`:

nla_get_be16
============

.. c:function:: __be16 nla_get_be16 (const struct nlattr *nla)

    return payload of __be16 attribute

    :param const struct nlattr \*nla:
        __be16 netlink attribute



.. _`nla_get_le16`:

nla_get_le16
============

.. c:function:: __le16 nla_get_le16 (const struct nlattr *nla)

    return payload of __le16 attribute

    :param const struct nlattr \*nla:
        __le16 netlink attribute



.. _`nla_get_u8`:

nla_get_u8
==========

.. c:function:: u8 nla_get_u8 (const struct nlattr *nla)

    return payload of u8 attribute

    :param const struct nlattr \*nla:
        u8 netlink attribute



.. _`nla_get_u64`:

nla_get_u64
===========

.. c:function:: u64 nla_get_u64 (const struct nlattr *nla)

    return payload of u64 attribute

    :param const struct nlattr \*nla:
        u64 netlink attribute



.. _`nla_get_be64`:

nla_get_be64
============

.. c:function:: __be64 nla_get_be64 (const struct nlattr *nla)

    return payload of __be64 attribute

    :param const struct nlattr \*nla:
        __be64 netlink attribute



.. _`nla_get_le64`:

nla_get_le64
============

.. c:function:: __le64 nla_get_le64 (const struct nlattr *nla)

    return payload of __le64 attribute

    :param const struct nlattr \*nla:
        __le64 netlink attribute



.. _`nla_get_s32`:

nla_get_s32
===========

.. c:function:: s32 nla_get_s32 (const struct nlattr *nla)

    return payload of s32 attribute

    :param const struct nlattr \*nla:
        s32 netlink attribute



.. _`nla_get_s16`:

nla_get_s16
===========

.. c:function:: s16 nla_get_s16 (const struct nlattr *nla)

    return payload of s16 attribute

    :param const struct nlattr \*nla:
        s16 netlink attribute



.. _`nla_get_s8`:

nla_get_s8
==========

.. c:function:: s8 nla_get_s8 (const struct nlattr *nla)

    return payload of s8 attribute

    :param const struct nlattr \*nla:
        s8 netlink attribute



.. _`nla_get_s64`:

nla_get_s64
===========

.. c:function:: s64 nla_get_s64 (const struct nlattr *nla)

    return payload of s64 attribute

    :param const struct nlattr \*nla:
        s64 netlink attribute



.. _`nla_get_flag`:

nla_get_flag
============

.. c:function:: int nla_get_flag (const struct nlattr *nla)

    return payload of flag attribute

    :param const struct nlattr \*nla:
        flag netlink attribute



.. _`nla_get_msecs`:

nla_get_msecs
=============

.. c:function:: unsigned long nla_get_msecs (const struct nlattr *nla)

    return payload of msecs attribute

    :param const struct nlattr \*nla:
        msecs netlink attribute



.. _`nla_get_msecs.description`:

Description
-----------

Returns the number of milliseconds in jiffies.



.. _`nla_get_in_addr`:

nla_get_in_addr
===============

.. c:function:: __be32 nla_get_in_addr (const struct nlattr *nla)

    return payload of IPv4 address attribute

    :param const struct nlattr \*nla:
        IPv4 address netlink attribute



.. _`nla_get_in6_addr`:

nla_get_in6_addr
================

.. c:function:: struct in6_addr nla_get_in6_addr (const struct nlattr *nla)

    return payload of IPv6 address attribute

    :param const struct nlattr \*nla:
        IPv6 address netlink attribute



.. _`nla_nest_start`:

nla_nest_start
==============

.. c:function:: struct nlattr *nla_nest_start (struct sk_buff *skb, int attrtype)

    Start a new level of nested attributes

    :param struct sk_buff \*skb:
        socket buffer to add attributes to

    :param int attrtype:
        attribute type of container



.. _`nla_nest_start.description`:

Description
-----------

Returns the container attribute



.. _`nla_nest_end`:

nla_nest_end
============

.. c:function:: int nla_nest_end (struct sk_buff *skb, struct nlattr *start)

    Finalize nesting of attributes

    :param struct sk_buff \*skb:
        socket buffer the attributes are stored in

    :param struct nlattr \*start:
        container attribute



.. _`nla_nest_end.description`:

Description
-----------

Corrects the container attribute header to include the all
appeneded attributes.

Returns the total data length of the skb.



.. _`nla_nest_cancel`:

nla_nest_cancel
===============

.. c:function:: void nla_nest_cancel (struct sk_buff *skb, struct nlattr *start)

    Cancel nesting of attributes

    :param struct sk_buff \*skb:
        socket buffer the message is stored in

    :param struct nlattr \*start:
        container attribute



.. _`nla_nest_cancel.description`:

Description
-----------

Removes the container attribute and including all nested
attributes. Returns -EMSGSIZE



.. _`nla_validate_nested`:

nla_validate_nested
===================

.. c:function:: int nla_validate_nested (const struct nlattr *start, int maxtype, const struct nla_policy *policy)

    Validate a stream of nested attributes

    :param const struct nlattr \*start:
        container attribute

    :param int maxtype:
        maximum attribute type to be expected

    :param const struct nla_policy \*policy:
        validation policy



.. _`nla_validate_nested.description`:

Description
-----------

Validates all attributes in the nested attribute stream against the
specified policy. Attributes with a type exceeding maxtype will be
ignored. See documenation of struct nla_policy for more details.

Returns 0 on success or a negative error code.



.. _`nla_for_each_attr`:

nla_for_each_attr
=================

.. c:function:: nla_for_each_attr ( pos,  head,  len,  rem)

    iterate over a stream of attributes

    :param pos:
        loop counter, set to current attribute

    :param head:
        head of attribute stream

    :param len:
        length of attribute stream

    :param rem:
        initialized to len, holds bytes currently remaining in stream



.. _`nla_for_each_nested`:

nla_for_each_nested
===================

.. c:function:: nla_for_each_nested ( pos,  nla,  rem)

    iterate over nested attributes

    :param pos:
        loop counter, set to current attribute

    :param nla:
        attribute containing the nested attributes

    :param rem:
        initialized to len, holds bytes currently remaining in stream



.. _`nla_is_last`:

nla_is_last
===========

.. c:function:: bool nla_is_last (const struct nlattr *nla, int rem)

    Test if attribute is last in stream

    :param const struct nlattr \*nla:
        attribute to test

    :param int rem:
        bytes remaining in stream

