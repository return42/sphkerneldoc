.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/netlink.h

.. _`nla_policy`:

struct nla_policy
=================

.. c:type:: struct nla_policy

    attribute validation policy

.. _`nla_policy.definition`:

Definition
----------

.. code-block:: c

    struct nla_policy {
        u8 type;
        u8 validation_type;
        u16 len;
        union {
            const void *validation_data;
            struct {
                s16 min, max;
            } ;
            int (*validate)(const struct nlattr *attr, struct netlink_ext_ack *extack);
        } ;
    }

.. _`nla_policy.members`:

Members
-------

type
    Type of attribute or NLA_UNSPEC

validation_type
    type of attribute validation done in addition to
    type-specific validation (e.g. range, function call), see
    \ :c:type:`enum nla_policy_validation <nla_policy_validation>`\ 

len
    Type specific length of payload

{unnamed_union}
    anonymous

validation_data
    *undescribed*

{unnamed_struct}
    anonymous

max
    *undescribed*

validate
    *undescribed*

.. _`nla_policy.description`:

Description
-----------

Policies are defined as arrays of this struct, the array must be
accessible by attribute type up to the highest identifier to be expected.

Meaning of \`len' field:
NLA_STRING           Maximum length of string
NLA_NUL_STRING       Maximum length of string (excluding NUL)
NLA_FLAG             Unused
NLA_BINARY           Maximum length of attribute payload
NLA_NESTED,
NLA_NESTED_ARRAY     Length verification is done by checking len of
nested header (or empty); len field is used if
validation_data is also used, for the max attr
number in the nested policy.
NLA_U8, NLA_U16,
NLA_U32, NLA_U64,
NLA_S8, NLA_S16,
NLA_S32, NLA_S64,
NLA_MSECS            Leaving the length field zero will verify the
given type fits, using it verifies minimum length
just like "All other"
NLA_BITFIELD32       Unused
NLA_REJECT           Unused
NLA_EXACT_LEN        Attribute must have exactly this length, otherwise
it is rejected.
NLA_EXACT_LEN_WARN   Attribute should have exactly this length, a warning
is logged if it is longer, shorter is rejected.
All other            Minimum length of attribute payload

Meaning of \`validation_data' field:
NLA_BITFIELD32       This is a 32-bit bitmap/bitselector attribute and
validation data must point to a u32 value of valid
flags
NLA_REJECT           This attribute is always rejected and validation data
may point to a string to report as the error instead
of the generic one in extended ACK.
NLA_NESTED           Points to a nested policy to validate, must also set
\`len' to the max attribute number.
Note that \ :c:func:`nla_parse`\  will validate, but of course not
parse, the nested sub-policies.
NLA_NESTED_ARRAY     Points to a nested policy to validate, must also set
\`len' to the max attribute number. The difference to
NLA_NESTED is the structure - NLA_NESTED has the
nested attributes directly inside, while an array has
the nested attributes at another level down and the
attributes directly in the nesting don't matter.
All other            Unused - but note that it's a union

Meaning of \`min' and \`max' fields, use via NLA_POLICY_MIN, NLA_POLICY_MAX

.. _`nla_policy.and-nla_policy_range`:

and NLA_POLICY_RANGE
--------------------

NLA_U8,
NLA_U16,
NLA_U32,
NLA_U64,
NLA_S8,
NLA_S16,
NLA_S32,
NLA_S64              These are used depending on the validation_type
field, if that is min/max/range then the minimum,
maximum and both are used (respectively) to check
the value of the integer attribute.
Note that in the interest of code simplicity and
struct size both limits are s16, so you cannot
enforce a range that doesn't fall within the range
of s16 - do that as usual in the code instead.
All other            Unused - but note that it's a union

Meaning of \`validate' field, use via NLA_POLICY_VALIDATE_FN:
NLA_BINARY           Validation function called for the attribute,
not compatible with use of the validation_data
as in NLA_BITFIELD32, NLA_REJECT, NLA_NESTED and
NLA_NESTED_ARRAY.
All other            Unused - but note that it's a union

.. _`nla_policy.example`:

Example
-------

.. code-block:: c

    static const struct nla_policy my_policy[ATTR_MAX+1] = {
         [ATTR_FOO] = { .type = NLA_U16 },
         [ATTR_BAR] = { .type = NLA_STRING, .len = BARSIZ },
         [ATTR_BAZ] = { .len = sizeof(struct mystruct) },
         [ATTR_GOO] = { .type = NLA_BITFIELD32, .validation_data = &myvalidflags },
    };


.. _`nl_info`:

struct nl_info
==============

.. c:type:: struct nl_info

    netlink source information

.. _`nl_info.definition`:

Definition
----------

.. code-block:: c

    struct nl_info {
        struct nlmsghdr *nlh;
        struct net *nl_net;
        u32 portid;
        bool skip_notify;
    }

.. _`nl_info.members`:

Members
-------

nlh
    Netlink message header of original request

nl_net
    *undescribed*

portid
    Netlink PORTID of requesting application

skip_notify
    *undescribed*

.. _`nlmsg_msg_size`:

nlmsg_msg_size
==============

.. c:function:: int nlmsg_msg_size(int payload)

    length of netlink message not including padding

    :param payload:
        length of message payload
    :type payload: int

.. _`nlmsg_total_size`:

nlmsg_total_size
================

.. c:function:: int nlmsg_total_size(int payload)

    length of netlink message including padding

    :param payload:
        length of message payload
    :type payload: int

.. _`nlmsg_padlen`:

nlmsg_padlen
============

.. c:function:: int nlmsg_padlen(int payload)

    length of padding at the message's tail

    :param payload:
        length of message payload
    :type payload: int

.. _`nlmsg_data`:

nlmsg_data
==========

.. c:function:: void *nlmsg_data(const struct nlmsghdr *nlh)

    head of message payload

    :param nlh:
        netlink message header
    :type nlh: const struct nlmsghdr \*

.. _`nlmsg_len`:

nlmsg_len
=========

.. c:function:: int nlmsg_len(const struct nlmsghdr *nlh)

    length of message payload

    :param nlh:
        netlink message header
    :type nlh: const struct nlmsghdr \*

.. _`nlmsg_attrdata`:

nlmsg_attrdata
==============

.. c:function:: struct nlattr *nlmsg_attrdata(const struct nlmsghdr *nlh, int hdrlen)

    head of attributes data

    :param nlh:
        netlink message header
    :type nlh: const struct nlmsghdr \*

    :param hdrlen:
        length of family specific header
    :type hdrlen: int

.. _`nlmsg_attrlen`:

nlmsg_attrlen
=============

.. c:function:: int nlmsg_attrlen(const struct nlmsghdr *nlh, int hdrlen)

    length of attributes data

    :param nlh:
        netlink message header
    :type nlh: const struct nlmsghdr \*

    :param hdrlen:
        length of family specific header
    :type hdrlen: int

.. _`nlmsg_ok`:

nlmsg_ok
========

.. c:function:: int nlmsg_ok(const struct nlmsghdr *nlh, int remaining)

    check if the netlink message fits into the remaining bytes

    :param nlh:
        netlink message header
    :type nlh: const struct nlmsghdr \*

    :param remaining:
        number of bytes remaining in message stream
    :type remaining: int

.. _`nlmsg_next`:

nlmsg_next
==========

.. c:function:: struct nlmsghdr *nlmsg_next(const struct nlmsghdr *nlh, int *remaining)

    next netlink message in message stream

    :param nlh:
        netlink message header
    :type nlh: const struct nlmsghdr \*

    :param remaining:
        number of bytes remaining in message stream
    :type remaining: int \*

.. _`nlmsg_next.description`:

Description
-----------

Returns the next netlink message in the message stream and
decrements remaining by the size of the current message.

.. _`nlmsg_parse`:

nlmsg_parse
===========

.. c:function:: int nlmsg_parse(const struct nlmsghdr *nlh, int hdrlen, struct nlattr  *tb, int maxtype, const struct nla_policy *policy, struct netlink_ext_ack *extack)

    parse attributes of a netlink message

    :param nlh:
        netlink message header
    :type nlh: const struct nlmsghdr \*

    :param hdrlen:
        length of family specific header
    :type hdrlen: int

    :param tb:
        destination array with maxtype+1 elements
    :type tb: struct nlattr  \*

    :param maxtype:
        maximum attribute type to be expected
    :type maxtype: int

    :param policy:
        validation policy
    :type policy: const struct nla_policy \*

    :param extack:
        extended ACK report struct
    :type extack: struct netlink_ext_ack \*

.. _`nlmsg_parse.description`:

Description
-----------

See \ :c:func:`nla_parse`\ 

.. _`nlmsg_find_attr`:

nlmsg_find_attr
===============

.. c:function:: struct nlattr *nlmsg_find_attr(const struct nlmsghdr *nlh, int hdrlen, int attrtype)

    find a specific attribute in a netlink message

    :param nlh:
        netlink message header
    :type nlh: const struct nlmsghdr \*

    :param hdrlen:
        length of familiy specific header
    :type hdrlen: int

    :param attrtype:
        type of attribute to look for
    :type attrtype: int

.. _`nlmsg_find_attr.description`:

Description
-----------

Returns the first attribute which matches the specified type.

.. _`nlmsg_validate`:

nlmsg_validate
==============

.. c:function:: int nlmsg_validate(const struct nlmsghdr *nlh, int hdrlen, int maxtype, const struct nla_policy *policy, struct netlink_ext_ack *extack)

    validate a netlink message including attributes

    :param nlh:
        netlinket message header
    :type nlh: const struct nlmsghdr \*

    :param hdrlen:
        length of familiy specific header
    :type hdrlen: int

    :param maxtype:
        maximum attribute type to be expected
    :type maxtype: int

    :param policy:
        validation policy
    :type policy: const struct nla_policy \*

    :param extack:
        extended ACK report struct
    :type extack: struct netlink_ext_ack \*

.. _`nlmsg_report`:

nlmsg_report
============

.. c:function:: int nlmsg_report(const struct nlmsghdr *nlh)

    need to report back to application?

    :param nlh:
        netlink message header
    :type nlh: const struct nlmsghdr \*

.. _`nlmsg_report.description`:

Description
-----------

Returns 1 if a report back to the application is requested.

.. _`nlmsg_for_each_attr`:

nlmsg_for_each_attr
===================

.. c:function::  nlmsg_for_each_attr( pos,  nlh,  hdrlen,  rem)

    iterate over a stream of attributes

    :param pos:
        loop counter, set to current attribute
    :type pos: 

    :param nlh:
        netlink message header
    :type nlh: 

    :param hdrlen:
        length of familiy specific header
    :type hdrlen: 

    :param rem:
        initialized to len, holds bytes currently remaining in stream
    :type rem: 

.. _`nlmsg_put`:

nlmsg_put
=========

.. c:function:: struct nlmsghdr *nlmsg_put(struct sk_buff *skb, u32 portid, u32 seq, int type, int payload, int flags)

    Add a new netlink message to an skb

    :param skb:
        socket buffer to store message in
    :type skb: struct sk_buff \*

    :param portid:
        netlink PORTID of requesting application
    :type portid: u32

    :param seq:
        sequence number of message
    :type seq: u32

    :param type:
        message type
    :type type: int

    :param payload:
        length of message payload
    :type payload: int

    :param flags:
        message flags
    :type flags: int

.. _`nlmsg_put.description`:

Description
-----------

Returns NULL if the tailroom of the skb is insufficient to store
the message header and payload.

.. _`nlmsg_put_answer`:

nlmsg_put_answer
================

.. c:function:: struct nlmsghdr *nlmsg_put_answer(struct sk_buff *skb, struct netlink_callback *cb, int type, int payload, int flags)

    Add a new callback based netlink message to an skb

    :param skb:
        socket buffer to store message in
    :type skb: struct sk_buff \*

    :param cb:
        netlink callback
    :type cb: struct netlink_callback \*

    :param type:
        message type
    :type type: int

    :param payload:
        length of message payload
    :type payload: int

    :param flags:
        message flags
    :type flags: int

.. _`nlmsg_put_answer.description`:

Description
-----------

Returns NULL if the tailroom of the skb is insufficient to store
the message header and payload.

.. _`nlmsg_new`:

nlmsg_new
=========

.. c:function:: struct sk_buff *nlmsg_new(size_t payload, gfp_t flags)

    Allocate a new netlink message

    :param payload:
        size of the message payload
    :type payload: size_t

    :param flags:
        the type of memory to allocate.
    :type flags: gfp_t

.. _`nlmsg_new.description`:

Description
-----------

Use NLMSG_DEFAULT_SIZE if the size of the payload isn't known
and a good default is needed.

.. _`nlmsg_end`:

nlmsg_end
=========

.. c:function:: void nlmsg_end(struct sk_buff *skb, struct nlmsghdr *nlh)

    Finalize a netlink message

    :param skb:
        socket buffer the message is stored in
    :type skb: struct sk_buff \*

    :param nlh:
        netlink message header
    :type nlh: struct nlmsghdr \*

.. _`nlmsg_end.description`:

Description
-----------

Corrects the netlink message header to include the appeneded
attributes. Only necessary if attributes have been added to
the message.

.. _`nlmsg_get_pos`:

nlmsg_get_pos
=============

.. c:function:: void *nlmsg_get_pos(struct sk_buff *skb)

    return current position in netlink message

    :param skb:
        socket buffer the message is stored in
    :type skb: struct sk_buff \*

.. _`nlmsg_get_pos.description`:

Description
-----------

Returns a pointer to the current tail of the message.

.. _`nlmsg_trim`:

nlmsg_trim
==========

.. c:function:: void nlmsg_trim(struct sk_buff *skb, const void *mark)

    Trim message to a mark

    :param skb:
        socket buffer the message is stored in
    :type skb: struct sk_buff \*

    :param mark:
        mark to trim to
    :type mark: const void \*

.. _`nlmsg_trim.description`:

Description
-----------

Trims the message to the provided mark.

.. _`nlmsg_cancel`:

nlmsg_cancel
============

.. c:function:: void nlmsg_cancel(struct sk_buff *skb, struct nlmsghdr *nlh)

    Cancel construction of a netlink message

    :param skb:
        socket buffer the message is stored in
    :type skb: struct sk_buff \*

    :param nlh:
        netlink message header
    :type nlh: struct nlmsghdr \*

.. _`nlmsg_cancel.description`:

Description
-----------

Removes the complete netlink message including all
attributes from the socket buffer again.

.. _`nlmsg_free`:

nlmsg_free
==========

.. c:function:: void nlmsg_free(struct sk_buff *skb)

    free a netlink message

    :param skb:
        socket buffer of netlink message
    :type skb: struct sk_buff \*

.. _`nlmsg_multicast`:

nlmsg_multicast
===============

.. c:function:: int nlmsg_multicast(struct sock *sk, struct sk_buff *skb, u32 portid, unsigned int group, gfp_t flags)

    multicast a netlink message

    :param sk:
        netlink socket to spread messages to
    :type sk: struct sock \*

    :param skb:
        netlink message as socket buffer
    :type skb: struct sk_buff \*

    :param portid:
        own netlink portid to avoid sending to yourself
    :type portid: u32

    :param group:
        multicast group id
    :type group: unsigned int

    :param flags:
        allocation flags
    :type flags: gfp_t

.. _`nlmsg_unicast`:

nlmsg_unicast
=============

.. c:function:: int nlmsg_unicast(struct sock *sk, struct sk_buff *skb, u32 portid)

    unicast a netlink message

    :param sk:
        netlink socket to spread message to
    :type sk: struct sock \*

    :param skb:
        netlink message as socket buffer
    :type skb: struct sk_buff \*

    :param portid:
        netlink portid of the destination socket
    :type portid: u32

.. _`nlmsg_for_each_msg`:

nlmsg_for_each_msg
==================

.. c:function::  nlmsg_for_each_msg( pos,  head,  len,  rem)

    iterate over a stream of messages

    :param pos:
        loop counter, set to current message
    :type pos: 

    :param head:
        head of message stream
    :type head: 

    :param len:
        length of message stream
    :type len: 

    :param rem:
        initialized to len, holds bytes currently remaining in stream
    :type rem: 

.. _`nl_dump_check_consistent`:

nl_dump_check_consistent
========================

.. c:function:: void nl_dump_check_consistent(struct netlink_callback *cb, struct nlmsghdr *nlh)

    check if sequence is consistent and advertise if not

    :param cb:
        netlink callback structure that stores the sequence number
    :type cb: struct netlink_callback \*

    :param nlh:
        netlink message header to write the flag to
    :type nlh: struct nlmsghdr \*

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

.. c:function:: int nla_attr_size(int payload)

    length of attribute not including padding

    :param payload:
        length of payload
    :type payload: int

.. _`nla_total_size`:

nla_total_size
==============

.. c:function:: int nla_total_size(int payload)

    total length of attribute including padding

    :param payload:
        length of payload
    :type payload: int

.. _`nla_padlen`:

nla_padlen
==========

.. c:function:: int nla_padlen(int payload)

    length of padding at the tail of attribute

    :param payload:
        length of payload
    :type payload: int

.. _`nla_type`:

nla_type
========

.. c:function:: int nla_type(const struct nlattr *nla)

    attribute type

    :param nla:
        netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_data`:

nla_data
========

.. c:function:: void *nla_data(const struct nlattr *nla)

    head of payload

    :param nla:
        netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_len`:

nla_len
=======

.. c:function:: int nla_len(const struct nlattr *nla)

    length of payload

    :param nla:
        netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_ok`:

nla_ok
======

.. c:function:: int nla_ok(const struct nlattr *nla, int remaining)

    check if the netlink attribute fits into the remaining bytes

    :param nla:
        netlink attribute
    :type nla: const struct nlattr \*

    :param remaining:
        number of bytes remaining in attribute stream
    :type remaining: int

.. _`nla_next`:

nla_next
========

.. c:function:: struct nlattr *nla_next(const struct nlattr *nla, int *remaining)

    next netlink attribute in attribute stream

    :param nla:
        netlink attribute
    :type nla: const struct nlattr \*

    :param remaining:
        number of bytes remaining in attribute stream
    :type remaining: int \*

.. _`nla_next.description`:

Description
-----------

Returns the next netlink attribute in the attribute stream and
decrements remaining by the size of the current attribute.

.. _`nla_find_nested`:

nla_find_nested
===============

.. c:function:: struct nlattr *nla_find_nested(const struct nlattr *nla, int attrtype)

    find attribute in a set of nested attributes

    :param nla:
        attribute containing the nested attributes
    :type nla: const struct nlattr \*

    :param attrtype:
        type of attribute to look for
    :type attrtype: int

.. _`nla_find_nested.description`:

Description
-----------

Returns the first attribute which matches the specified type.

.. _`nla_parse_nested`:

nla_parse_nested
================

.. c:function:: int nla_parse_nested(struct nlattr  *tb, int maxtype, const struct nlattr *nla, const struct nla_policy *policy, struct netlink_ext_ack *extack)

    parse nested attributes

    :param tb:
        destination array with maxtype+1 elements
    :type tb: struct nlattr  \*

    :param maxtype:
        maximum attribute type to be expected
    :type maxtype: int

    :param nla:
        attribute containing the nested attributes
    :type nla: const struct nlattr \*

    :param policy:
        validation policy
    :type policy: const struct nla_policy \*

    :param extack:
        extended ACK report struct
    :type extack: struct netlink_ext_ack \*

.. _`nla_parse_nested.description`:

Description
-----------

See \ :c:func:`nla_parse`\ 

.. _`nla_put_u8`:

nla_put_u8
==========

.. c:function:: int nla_put_u8(struct sk_buff *skb, int attrtype, u8 value)

    Add a u8 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: u8

.. _`nla_put_u16`:

nla_put_u16
===========

.. c:function:: int nla_put_u16(struct sk_buff *skb, int attrtype, u16 value)

    Add a u16 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: u16

.. _`nla_put_be16`:

nla_put_be16
============

.. c:function:: int nla_put_be16(struct sk_buff *skb, int attrtype, __be16 value)

    Add a \__be16 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: __be16

.. _`nla_put_net16`:

nla_put_net16
=============

.. c:function:: int nla_put_net16(struct sk_buff *skb, int attrtype, __be16 value)

    Add 16-bit network byte order netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: __be16

.. _`nla_put_le16`:

nla_put_le16
============

.. c:function:: int nla_put_le16(struct sk_buff *skb, int attrtype, __le16 value)

    Add a \__le16 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: __le16

.. _`nla_put_u32`:

nla_put_u32
===========

.. c:function:: int nla_put_u32(struct sk_buff *skb, int attrtype, u32 value)

    Add a u32 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: u32

.. _`nla_put_be32`:

nla_put_be32
============

.. c:function:: int nla_put_be32(struct sk_buff *skb, int attrtype, __be32 value)

    Add a \__be32 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: __be32

.. _`nla_put_net32`:

nla_put_net32
=============

.. c:function:: int nla_put_net32(struct sk_buff *skb, int attrtype, __be32 value)

    Add 32-bit network byte order netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: __be32

.. _`nla_put_le32`:

nla_put_le32
============

.. c:function:: int nla_put_le32(struct sk_buff *skb, int attrtype, __le32 value)

    Add a \__le32 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: __le32

.. _`nla_put_u64_64bit`:

nla_put_u64_64bit
=================

.. c:function:: int nla_put_u64_64bit(struct sk_buff *skb, int attrtype, u64 value, int padattr)

    Add a u64 netlink attribute to a skb and align it

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: u64

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`nla_put_be64`:

nla_put_be64
============

.. c:function:: int nla_put_be64(struct sk_buff *skb, int attrtype, __be64 value, int padattr)

    Add a \__be64 netlink attribute to a socket buffer and align it

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: __be64

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`nla_put_net64`:

nla_put_net64
=============

.. c:function:: int nla_put_net64(struct sk_buff *skb, int attrtype, __be64 value, int padattr)

    Add 64-bit network byte order nlattr to a skb and align it

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: __be64

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`nla_put_le64`:

nla_put_le64
============

.. c:function:: int nla_put_le64(struct sk_buff *skb, int attrtype, __le64 value, int padattr)

    Add a \__le64 netlink attribute to a socket buffer and align it

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: __le64

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`nla_put_s8`:

nla_put_s8
==========

.. c:function:: int nla_put_s8(struct sk_buff *skb, int attrtype, s8 value)

    Add a s8 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: s8

.. _`nla_put_s16`:

nla_put_s16
===========

.. c:function:: int nla_put_s16(struct sk_buff *skb, int attrtype, s16 value)

    Add a s16 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: s16

.. _`nla_put_s32`:

nla_put_s32
===========

.. c:function:: int nla_put_s32(struct sk_buff *skb, int attrtype, s32 value)

    Add a s32 netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: s32

.. _`nla_put_s64`:

nla_put_s64
===========

.. c:function:: int nla_put_s64(struct sk_buff *skb, int attrtype, s64 value, int padattr)

    Add a s64 netlink attribute to a socket buffer and align it

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param value:
        numeric value
    :type value: s64

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`nla_put_string`:

nla_put_string
==============

.. c:function:: int nla_put_string(struct sk_buff *skb, int attrtype, const char *str)

    Add a string netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param str:
        NUL terminated string
    :type str: const char \*

.. _`nla_put_flag`:

nla_put_flag
============

.. c:function:: int nla_put_flag(struct sk_buff *skb, int attrtype)

    Add a flag netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

.. _`nla_put_msecs`:

nla_put_msecs
=============

.. c:function:: int nla_put_msecs(struct sk_buff *skb, int attrtype, unsigned long njiffies, int padattr)

    Add a msecs netlink attribute to a skb and align it

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param njiffies:
        number of jiffies to convert to msecs
    :type njiffies: unsigned long

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`nla_put_in_addr`:

nla_put_in_addr
===============

.. c:function:: int nla_put_in_addr(struct sk_buff *skb, int attrtype, __be32 addr)

    Add an IPv4 address netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param addr:
        IPv4 address
    :type addr: __be32

.. _`nla_put_in6_addr`:

nla_put_in6_addr
================

.. c:function:: int nla_put_in6_addr(struct sk_buff *skb, int attrtype, const struct in6_addr *addr)

    Add an IPv6 address netlink attribute to a socket buffer

    :param skb:
        socket buffer to add attribute to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type
    :type attrtype: int

    :param addr:
        IPv6 address
    :type addr: const struct in6_addr \*

.. _`nla_get_u32`:

nla_get_u32
===========

.. c:function:: u32 nla_get_u32(const struct nlattr *nla)

    return payload of u32 attribute

    :param nla:
        u32 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_be32`:

nla_get_be32
============

.. c:function:: __be32 nla_get_be32(const struct nlattr *nla)

    return payload of \__be32 attribute

    :param nla:
        \__be32 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_le32`:

nla_get_le32
============

.. c:function:: __le32 nla_get_le32(const struct nlattr *nla)

    return payload of \__le32 attribute

    :param nla:
        \__le32 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_u16`:

nla_get_u16
===========

.. c:function:: u16 nla_get_u16(const struct nlattr *nla)

    return payload of u16 attribute

    :param nla:
        u16 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_be16`:

nla_get_be16
============

.. c:function:: __be16 nla_get_be16(const struct nlattr *nla)

    return payload of \__be16 attribute

    :param nla:
        \__be16 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_le16`:

nla_get_le16
============

.. c:function:: __le16 nla_get_le16(const struct nlattr *nla)

    return payload of \__le16 attribute

    :param nla:
        \__le16 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_u8`:

nla_get_u8
==========

.. c:function:: u8 nla_get_u8(const struct nlattr *nla)

    return payload of u8 attribute

    :param nla:
        u8 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_u64`:

nla_get_u64
===========

.. c:function:: u64 nla_get_u64(const struct nlattr *nla)

    return payload of u64 attribute

    :param nla:
        u64 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_be64`:

nla_get_be64
============

.. c:function:: __be64 nla_get_be64(const struct nlattr *nla)

    return payload of \__be64 attribute

    :param nla:
        \__be64 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_le64`:

nla_get_le64
============

.. c:function:: __le64 nla_get_le64(const struct nlattr *nla)

    return payload of \__le64 attribute

    :param nla:
        \__le64 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_s32`:

nla_get_s32
===========

.. c:function:: s32 nla_get_s32(const struct nlattr *nla)

    return payload of s32 attribute

    :param nla:
        s32 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_s16`:

nla_get_s16
===========

.. c:function:: s16 nla_get_s16(const struct nlattr *nla)

    return payload of s16 attribute

    :param nla:
        s16 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_s8`:

nla_get_s8
==========

.. c:function:: s8 nla_get_s8(const struct nlattr *nla)

    return payload of s8 attribute

    :param nla:
        s8 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_s64`:

nla_get_s64
===========

.. c:function:: s64 nla_get_s64(const struct nlattr *nla)

    return payload of s64 attribute

    :param nla:
        s64 netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_flag`:

nla_get_flag
============

.. c:function:: int nla_get_flag(const struct nlattr *nla)

    return payload of flag attribute

    :param nla:
        flag netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_msecs`:

nla_get_msecs
=============

.. c:function:: unsigned long nla_get_msecs(const struct nlattr *nla)

    return payload of msecs attribute

    :param nla:
        msecs netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_msecs.description`:

Description
-----------

Returns the number of milliseconds in jiffies.

.. _`nla_get_in_addr`:

nla_get_in_addr
===============

.. c:function:: __be32 nla_get_in_addr(const struct nlattr *nla)

    return payload of IPv4 address attribute

    :param nla:
        IPv4 address netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_in6_addr`:

nla_get_in6_addr
================

.. c:function:: struct in6_addr nla_get_in6_addr(const struct nlattr *nla)

    return payload of IPv6 address attribute

    :param nla:
        IPv6 address netlink attribute
    :type nla: const struct nlattr \*

.. _`nla_get_bitfield32`:

nla_get_bitfield32
==================

.. c:function:: struct nla_bitfield32 nla_get_bitfield32(const struct nlattr *nla)

    return payload of 32 bitfield attribute

    :param nla:
        nla_bitfield32 attribute
    :type nla: const struct nlattr \*

.. _`nla_memdup`:

nla_memdup
==========

.. c:function:: void *nla_memdup(const struct nlattr *src, gfp_t gfp)

    duplicate attribute memory (kmemdup)

    :param src:
        netlink attribute to duplicate from
    :type src: const struct nlattr \*

    :param gfp:
        GFP mask
    :type gfp: gfp_t

.. _`nla_nest_start`:

nla_nest_start
==============

.. c:function:: struct nlattr *nla_nest_start(struct sk_buff *skb, int attrtype)

    Start a new level of nested attributes

    :param skb:
        socket buffer to add attributes to
    :type skb: struct sk_buff \*

    :param attrtype:
        attribute type of container
    :type attrtype: int

.. _`nla_nest_start.description`:

Description
-----------

Returns the container attribute

.. _`nla_nest_end`:

nla_nest_end
============

.. c:function:: int nla_nest_end(struct sk_buff *skb, struct nlattr *start)

    Finalize nesting of attributes

    :param skb:
        socket buffer the attributes are stored in
    :type skb: struct sk_buff \*

    :param start:
        container attribute
    :type start: struct nlattr \*

.. _`nla_nest_end.description`:

Description
-----------

Corrects the container attribute header to include the all
appeneded attributes.

Returns the total data length of the skb.

.. _`nla_nest_cancel`:

nla_nest_cancel
===============

.. c:function:: void nla_nest_cancel(struct sk_buff *skb, struct nlattr *start)

    Cancel nesting of attributes

    :param skb:
        socket buffer the message is stored in
    :type skb: struct sk_buff \*

    :param start:
        container attribute
    :type start: struct nlattr \*

.. _`nla_nest_cancel.description`:

Description
-----------

Removes the container attribute and including all nested
attributes. Returns -EMSGSIZE

.. _`nla_validate_nested`:

nla_validate_nested
===================

.. c:function:: int nla_validate_nested(const struct nlattr *start, int maxtype, const struct nla_policy *policy, struct netlink_ext_ack *extack)

    Validate a stream of nested attributes

    :param start:
        container attribute
    :type start: const struct nlattr \*

    :param maxtype:
        maximum attribute type to be expected
    :type maxtype: int

    :param policy:
        validation policy
    :type policy: const struct nla_policy \*

    :param extack:
        extended ACK report struct
    :type extack: struct netlink_ext_ack \*

.. _`nla_validate_nested.description`:

Description
-----------

Validates all attributes in the nested attribute stream against the
specified policy. Attributes with a type exceeding maxtype will be
ignored. See documenation of struct nla_policy for more details.

Returns 0 on success or a negative error code.

.. _`nla_need_padding_for_64bit`:

nla_need_padding_for_64bit
==========================

.. c:function:: bool nla_need_padding_for_64bit(struct sk_buff *skb)

    test 64-bit alignment of the next attribute

    :param skb:
        socket buffer the message is stored in
    :type skb: struct sk_buff \*

.. _`nla_need_padding_for_64bit.description`:

Description
-----------

Return true if padding is needed to align the next attribute (nla_data()) to
a 64-bit aligned area.

.. _`nla_align_64bit`:

nla_align_64bit
===============

.. c:function:: int nla_align_64bit(struct sk_buff *skb, int padattr)

    64-bit align the \ :c:func:`nla_data`\  of next attribute

    :param skb:
        socket buffer the message is stored in
    :type skb: struct sk_buff \*

    :param padattr:
        attribute type for the padding
    :type padattr: int

.. _`nla_align_64bit.description`:

Description
-----------

Conditionally emit a padding netlink attribute in order to make
the next attribute we emit have a 64-bit aligned \ :c:func:`nla_data`\  area.
This will only be done in architectures which do not have
CONFIG_HAVE_EFFICIENT_UNALIGNED_ACCESS defined.

Returns zero on success or a negative error code.

.. _`nla_total_size_64bit`:

nla_total_size_64bit
====================

.. c:function:: int nla_total_size_64bit(int payload)

    total length of attribute including padding

    :param payload:
        length of payload
    :type payload: int

.. _`nla_for_each_attr`:

nla_for_each_attr
=================

.. c:function::  nla_for_each_attr( pos,  head,  len,  rem)

    iterate over a stream of attributes

    :param pos:
        loop counter, set to current attribute
    :type pos: 

    :param head:
        head of attribute stream
    :type head: 

    :param len:
        length of attribute stream
    :type len: 

    :param rem:
        initialized to len, holds bytes currently remaining in stream
    :type rem: 

.. _`nla_for_each_nested`:

nla_for_each_nested
===================

.. c:function::  nla_for_each_nested( pos,  nla,  rem)

    iterate over nested attributes

    :param pos:
        loop counter, set to current attribute
    :type pos: 

    :param nla:
        attribute containing the nested attributes
    :type nla: 

    :param rem:
        initialized to len, holds bytes currently remaining in stream
    :type rem: 

.. _`nla_is_last`:

nla_is_last
===========

.. c:function:: bool nla_is_last(const struct nlattr *nla, int rem)

    Test if attribute is last in stream

    :param nla:
        attribute to test
    :type nla: const struct nlattr \*

    :param rem:
        bytes remaining in stream
    :type rem: int

.. This file was automatic generated / don't edit.

