.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/iwpm_util.h

.. _`iwpm_get_nlmsg_request`:

iwpm_get_nlmsg_request
======================

.. c:function:: struct iwpm_nlmsg_request *iwpm_get_nlmsg_request(__u32 nlmsg_seq, u8 nl_client, gfp_t gfp)

    Allocate and initialize netlink message request

    :param nlmsg_seq:
        Sequence number of the netlink message
    :type nlmsg_seq: __u32

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

    :param gfp:
        Indicates how the memory for the request should be allocated
    :type gfp: gfp_t

.. _`iwpm_get_nlmsg_request.description`:

Description
-----------

Returns the newly allocated netlink request object if successful,
otherwise returns NULL

.. _`iwpm_free_nlmsg_request`:

iwpm_free_nlmsg_request
=======================

.. c:function:: void iwpm_free_nlmsg_request(struct kref *kref)

    Deallocate netlink message request

    :param kref:
        Holds reference of netlink message request
    :type kref: struct kref \*

.. _`iwpm_find_nlmsg_request`:

iwpm_find_nlmsg_request
=======================

.. c:function:: struct iwpm_nlmsg_request *iwpm_find_nlmsg_request(__u32 echo_seq)

    Find netlink message request in the request list

    :param echo_seq:
        Sequence number of the netlink request to find
    :type echo_seq: __u32

.. _`iwpm_find_nlmsg_request.description`:

Description
-----------

Returns the found netlink message request,
if not found, returns NULL

.. _`iwpm_wait_complete_req`:

iwpm_wait_complete_req
======================

.. c:function:: int iwpm_wait_complete_req(struct iwpm_nlmsg_request *nlmsg_request)

    Block while servicing the netlink request

    :param nlmsg_request:
        Netlink message request to service
    :type nlmsg_request: struct iwpm_nlmsg_request \*

.. _`iwpm_wait_complete_req.description`:

Description
-----------

Wakes up, after the request is completed or expired
Returns 0 if the request is complete without error

.. _`iwpm_get_nlmsg_seq`:

iwpm_get_nlmsg_seq
==================

.. c:function:: int iwpm_get_nlmsg_seq( void)

    Get the sequence number for a netlink message to send to the port mapper

    :param void:
        no arguments
    :type void: 

.. _`iwpm_get_nlmsg_seq.description`:

Description
-----------

Returns the sequence number for the netlink message.

.. _`iwpm_add_remote_info`:

iwpm_add_remote_info
====================

.. c:function:: void iwpm_add_remote_info(struct iwpm_remote_info *reminfo)

    Add remote address info of the connecting peer to the remote info hash table

    :param reminfo:
        The remote info to be added
    :type reminfo: struct iwpm_remote_info \*

.. _`iwpm_valid_client`:

iwpm_valid_client
=================

.. c:function:: int iwpm_valid_client(u8 nl_client)

    Check if the port mapper client is valid

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

.. _`iwpm_valid_client.description`:

Description
-----------

Valid clients need to call \ :c:func:`iwpm_init`\  before using
the port mapper

.. _`iwpm_set_valid`:

iwpm_set_valid
==============

.. c:function:: void iwpm_set_valid(u8 nl_client, int valid)

    Set the port mapper client to valid or not

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

    :param valid:
        1 if valid or 0 if invalid
    :type valid: int

.. _`iwpm_check_registration`:

iwpm_check_registration
=======================

.. c:function:: u32 iwpm_check_registration(u8 nl_client, u32 reg)

    Check if the client registration matches the given one

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

    :param reg:
        The given registration type to compare with
    :type reg: u32

.. _`iwpm_check_registration.description`:

Description
-----------

Call \ :c:func:`iwpm_register_pid`\  to register a client
Returns true if the client registration matches reg,
otherwise returns false

.. _`iwpm_set_registration`:

iwpm_set_registration
=====================

.. c:function:: void iwpm_set_registration(u8 nl_client, u32 reg)

    Set the client registration

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

    :param reg:
        Registration type to set
    :type reg: u32

.. _`iwpm_get_registration`:

iwpm_get_registration
=====================

.. c:function:: u32 iwpm_get_registration(u8 nl_client)

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

.. _`iwpm_get_registration.description`:

Description
-----------

Returns the client registration type

.. _`iwpm_send_mapinfo`:

iwpm_send_mapinfo
=================

.. c:function:: int iwpm_send_mapinfo(u8 nl_client, int iwpm_pid)

    Send local and mapped IPv4/IPv6 address info of a client to the user space port mapper

    :param nl_client:
        The index of the netlink client
    :type nl_client: u8

    :param iwpm_pid:
        The pid of the user space port mapper
    :type iwpm_pid: int

.. _`iwpm_send_mapinfo.description`:

Description
-----------

If successful, returns the number of sent mapping info records

.. _`iwpm_mapinfo_available`:

iwpm_mapinfo_available
======================

.. c:function:: int iwpm_mapinfo_available( void)

    Check if any mapping info records is available in the hash table

    :param void:
        no arguments
    :type void: 

.. _`iwpm_mapinfo_available.description`:

Description
-----------

Returns 1 if mapping information is available, otherwise returns 0

.. _`iwpm_compare_sockaddr`:

iwpm_compare_sockaddr
=====================

.. c:function:: int iwpm_compare_sockaddr(struct sockaddr_storage *a_sockaddr, struct sockaddr_storage *b_sockaddr)

    Compare two sockaddr storage structs

    :param a_sockaddr:
        *undescribed*
    :type a_sockaddr: struct sockaddr_storage \*

    :param b_sockaddr:
        *undescribed*
    :type b_sockaddr: struct sockaddr_storage \*

.. _`iwpm_compare_sockaddr.description`:

Description
-----------

Returns 0 if they are holding the same ip/tcp address info,
otherwise returns 1

.. _`iwpm_validate_nlmsg_attr`:

iwpm_validate_nlmsg_attr
========================

.. c:function:: int iwpm_validate_nlmsg_attr(struct nlattr  *nltb, int nla_count)

    Check for NULL netlink attributes

    :param nltb:
        Holds address of each netlink message attributes
    :type nltb: struct nlattr  \*

    :param nla_count:
        Number of netlink message attributes
    :type nla_count: int

.. _`iwpm_validate_nlmsg_attr.description`:

Description
-----------

Returns error if any of the nla_count attributes is NULL

.. _`iwpm_create_nlmsg`:

iwpm_create_nlmsg
=================

.. c:function:: struct sk_buff *iwpm_create_nlmsg(u32 nl_op, struct nlmsghdr **nlh, int nl_client)

    Allocate skb and form a netlink message

    :param nl_op:
        Netlink message opcode
    :type nl_op: u32

    :param nlh:
        Holds address of the netlink message header in skb
    :type nlh: struct nlmsghdr \*\*

    :param nl_client:
        The index of the netlink client
    :type nl_client: int

.. _`iwpm_create_nlmsg.description`:

Description
-----------

Returns the newly allcated skb, or NULL if the tailroom of the skb
is insufficient to store the message header and payload

.. _`iwpm_parse_nlmsg`:

iwpm_parse_nlmsg
================

.. c:function:: int iwpm_parse_nlmsg(struct netlink_callback *cb, int policy_max, const struct nla_policy *nlmsg_policy, struct nlattr  *nltb, const char *msg_type)

    Validate and parse the received netlink message

    :param cb:
        Netlink callback structure
    :type cb: struct netlink_callback \*

    :param policy_max:
        Maximum attribute type to be expected
    :type policy_max: int

    :param nlmsg_policy:
        Validation policy
    :type nlmsg_policy: const struct nla_policy \*

    :param nltb:
        Array to store policy_max parsed elements
    :type nltb: struct nlattr  \*

    :param msg_type:
        Type of netlink message
    :type msg_type: const char \*

.. _`iwpm_parse_nlmsg.description`:

Description
-----------

Returns 0 on success or a negative error code

.. _`iwpm_print_sockaddr`:

iwpm_print_sockaddr
===================

.. c:function:: void iwpm_print_sockaddr(struct sockaddr_storage *sockaddr, char *msg)

    Print IPv4/IPv6 address and TCP port

    :param sockaddr:
        Socket address to print
    :type sockaddr: struct sockaddr_storage \*

    :param msg:
        Message to print
    :type msg: char \*

.. This file was automatic generated / don't edit.

