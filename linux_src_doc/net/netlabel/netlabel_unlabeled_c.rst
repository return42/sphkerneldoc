.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_unlabeled.c

.. _`netlbl_unlhsh_free_iface`:

netlbl_unlhsh_free_iface
========================

.. c:function:: void netlbl_unlhsh_free_iface(struct rcu_head *entry)

    Frees an interface entry from the hash table

    :param entry:
        the entry's RCU field
    :type entry: struct rcu_head \*

.. _`netlbl_unlhsh_free_iface.description`:

Description
-----------

This function is designed to be used as a callback to the \ :c:func:`call_rcu`\ 
function so that memory allocated to a hash table interface entry can be
released safely.  It is important to note that this function does not free
the IPv4 and IPv6 address lists contained as part of an interface entry.  It
is up to the rest of the code to make sure an interface entry is only freed
once it's address lists are empty.

.. _`netlbl_unlhsh_hash`:

netlbl_unlhsh_hash
==================

.. c:function:: u32 netlbl_unlhsh_hash(int ifindex)

    Hashing function for the hash table

    :param ifindex:
        the network interface/device to hash
    :type ifindex: int

.. _`netlbl_unlhsh_hash.description`:

Description
-----------

This is the hashing function for the unlabeled hash table, it returns the
bucket number for the given device/interface.  The caller is responsible for
ensuring that the hash table is protected with either a RCU read lock or
the hash table lock.

.. _`netlbl_unlhsh_search_iface`:

netlbl_unlhsh_search_iface
==========================

.. c:function:: struct netlbl_unlhsh_iface *netlbl_unlhsh_search_iface(int ifindex)

    Search for a matching interface entry

    :param ifindex:
        the network interface
    :type ifindex: int

.. _`netlbl_unlhsh_search_iface.description`:

Description
-----------

Searches the unlabeled connection hash table and returns a pointer to the
interface entry which matches \ ``ifindex``\ , otherwise NULL is returned.  The
caller is responsible for ensuring that the hash table is protected with
either a RCU read lock or the hash table lock.

.. _`netlbl_unlhsh_add_addr4`:

netlbl_unlhsh_add_addr4
=======================

.. c:function:: int netlbl_unlhsh_add_addr4(struct netlbl_unlhsh_iface *iface, const struct in_addr *addr, const struct in_addr *mask, u32 secid)

    Add a new IPv4 address entry to the hash table

    :param iface:
        the associated interface entry
    :type iface: struct netlbl_unlhsh_iface \*

    :param addr:
        IPv4 address in network byte order
    :type addr: const struct in_addr \*

    :param mask:
        IPv4 address mask in network byte order
    :type mask: const struct in_addr \*

    :param secid:
        LSM secid value for entry
    :type secid: u32

.. _`netlbl_unlhsh_add_addr4.description`:

Description
-----------

Add a new address entry into the unlabeled connection hash table using the
interface entry specified by \ ``iface``\ .  On success zero is returned, otherwise
a negative value is returned.

.. _`netlbl_unlhsh_add_addr6`:

netlbl_unlhsh_add_addr6
=======================

.. c:function:: int netlbl_unlhsh_add_addr6(struct netlbl_unlhsh_iface *iface, const struct in6_addr *addr, const struct in6_addr *mask, u32 secid)

    Add a new IPv6 address entry to the hash table

    :param iface:
        the associated interface entry
    :type iface: struct netlbl_unlhsh_iface \*

    :param addr:
        IPv6 address in network byte order
    :type addr: const struct in6_addr \*

    :param mask:
        IPv6 address mask in network byte order
    :type mask: const struct in6_addr \*

    :param secid:
        LSM secid value for entry
    :type secid: u32

.. _`netlbl_unlhsh_add_addr6.description`:

Description
-----------

Add a new address entry into the unlabeled connection hash table using the
interface entry specified by \ ``iface``\ .  On success zero is returned, otherwise
a negative value is returned.

.. _`netlbl_unlhsh_add_iface`:

netlbl_unlhsh_add_iface
=======================

.. c:function:: struct netlbl_unlhsh_iface *netlbl_unlhsh_add_iface(int ifindex)

    Adds a new interface entry to the hash table

    :param ifindex:
        network interface
    :type ifindex: int

.. _`netlbl_unlhsh_add_iface.description`:

Description
-----------

Add a new, empty, interface entry into the unlabeled connection hash table.
On success a pointer to the new interface entry is returned, on failure NULL
is returned.

.. _`netlbl_unlhsh_add`:

netlbl_unlhsh_add
=================

.. c:function:: int netlbl_unlhsh_add(struct net *net, const char *dev_name, const void *addr, const void *mask, u32 addr_len, u32 secid, struct netlbl_audit *audit_info)

    Adds a new entry to the unlabeled connection hash table

    :param net:
        network namespace
    :type net: struct net \*

    :param dev_name:
        interface name
    :type dev_name: const char \*

    :param addr:
        IP address in network byte order
    :type addr: const void \*

    :param mask:
        address mask in network byte order
    :type mask: const void \*

    :param addr_len:
        length of address/mask (4 for IPv4, 16 for IPv6)
    :type addr_len: u32

    :param secid:
        LSM secid value for the entry
    :type secid: u32

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_unlhsh_add.description`:

Description
-----------

Adds a new entry to the unlabeled connection hash table.  Returns zero on
success, negative values on failure.

.. _`netlbl_unlhsh_remove_addr4`:

netlbl_unlhsh_remove_addr4
==========================

.. c:function:: int netlbl_unlhsh_remove_addr4(struct net *net, struct netlbl_unlhsh_iface *iface, const struct in_addr *addr, const struct in_addr *mask, struct netlbl_audit *audit_info)

    Remove an IPv4 address entry

    :param net:
        network namespace
    :type net: struct net \*

    :param iface:
        interface entry
    :type iface: struct netlbl_unlhsh_iface \*

    :param addr:
        IP address
    :type addr: const struct in_addr \*

    :param mask:
        IP address mask
    :type mask: const struct in_addr \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_unlhsh_remove_addr4.description`:

Description
-----------

Remove an IP address entry from the unlabeled connection hash table.
Returns zero on success, negative values on failure.

.. _`netlbl_unlhsh_remove_addr6`:

netlbl_unlhsh_remove_addr6
==========================

.. c:function:: int netlbl_unlhsh_remove_addr6(struct net *net, struct netlbl_unlhsh_iface *iface, const struct in6_addr *addr, const struct in6_addr *mask, struct netlbl_audit *audit_info)

    Remove an IPv6 address entry

    :param net:
        network namespace
    :type net: struct net \*

    :param iface:
        interface entry
    :type iface: struct netlbl_unlhsh_iface \*

    :param addr:
        IP address
    :type addr: const struct in6_addr \*

    :param mask:
        IP address mask
    :type mask: const struct in6_addr \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_unlhsh_remove_addr6.description`:

Description
-----------

Remove an IP address entry from the unlabeled connection hash table.
Returns zero on success, negative values on failure.

.. _`netlbl_unlhsh_condremove_iface`:

netlbl_unlhsh_condremove_iface
==============================

.. c:function:: void netlbl_unlhsh_condremove_iface(struct netlbl_unlhsh_iface *iface)

    Remove an interface entry

    :param iface:
        the interface entry
    :type iface: struct netlbl_unlhsh_iface \*

.. _`netlbl_unlhsh_condremove_iface.description`:

Description
-----------

Remove an interface entry from the unlabeled connection hash table if it is
empty.  An interface entry is considered to be empty if there are no
address entries assigned to it.

.. _`netlbl_unlhsh_remove`:

netlbl_unlhsh_remove
====================

.. c:function:: int netlbl_unlhsh_remove(struct net *net, const char *dev_name, const void *addr, const void *mask, u32 addr_len, struct netlbl_audit *audit_info)

    Remove an entry from the unlabeled hash table

    :param net:
        network namespace
    :type net: struct net \*

    :param dev_name:
        interface name
    :type dev_name: const char \*

    :param addr:
        IP address in network byte order
    :type addr: const void \*

    :param mask:
        address mask in network byte order
    :type mask: const void \*

    :param addr_len:
        length of address/mask (4 for IPv4, 16 for IPv6)
    :type addr_len: u32

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_unlhsh_remove.description`:

Description
-----------

Removes and existing entry from the unlabeled connection hash table.
Returns zero on success, negative values on failure.

.. _`netlbl_unlhsh_netdev_handler`:

netlbl_unlhsh_netdev_handler
============================

.. c:function:: int netlbl_unlhsh_netdev_handler(struct notifier_block *this, unsigned long event, void *ptr)

    Network device notification handler

    :param this:
        notifier block
    :type this: struct notifier_block \*

    :param event:
        the event
    :type event: unsigned long

    :param ptr:
        the netdevice notifier info (cast to void)
    :type ptr: void \*

.. _`netlbl_unlhsh_netdev_handler.description`:

Description
-----------

Handle network device events, although at present all we care about is a
network device going away.  In the case of a device going away we clear any
related entries from the unlabeled connection hash table.

.. _`netlbl_unlabel_acceptflg_set`:

netlbl_unlabel_acceptflg_set
============================

.. c:function:: void netlbl_unlabel_acceptflg_set(u8 value, struct netlbl_audit *audit_info)

    Set the unlabeled accept flag

    :param value:
        desired value
    :type value: u8

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_unlabel_acceptflg_set.description`:

Description
-----------

Set the value of the unlabeled accept flag to \ ``value``\ .

.. _`netlbl_unlabel_addrinfo_get`:

netlbl_unlabel_addrinfo_get
===========================

.. c:function:: int netlbl_unlabel_addrinfo_get(struct genl_info *info, void **addr, void **mask, u32 *len)

    Get the IPv4/6 address information

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

    :param addr:
        the IP address
    :type addr: void \*\*

    :param mask:
        the IP address mask
    :type mask: void \*\*

    :param len:
        the address length
    :type len: u32 \*

.. _`netlbl_unlabel_addrinfo_get.description`:

Description
-----------

Examine the Generic NETLINK message and extract the IP address information.
Returns zero on success, negative values on failure.

.. _`netlbl_unlabel_accept`:

netlbl_unlabel_accept
=====================

.. c:function:: int netlbl_unlabel_accept(struct sk_buff *skb, struct genl_info *info)

    Handle an ACCEPT message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_unlabel_accept.description`:

Description
-----------

Process a user generated ACCEPT message and set the accept flag accordingly.
Returns zero on success, negative values on failure.

.. _`netlbl_unlabel_list`:

netlbl_unlabel_list
===================

.. c:function:: int netlbl_unlabel_list(struct sk_buff *skb, struct genl_info *info)

    Handle a LIST message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_unlabel_list.description`:

Description
-----------

Process a user generated LIST message and respond with the current status.
Returns zero on success, negative values on failure.

.. _`netlbl_unlabel_staticadd`:

netlbl_unlabel_staticadd
========================

.. c:function:: int netlbl_unlabel_staticadd(struct sk_buff *skb, struct genl_info *info)

    Handle a STATICADD message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_unlabel_staticadd.description`:

Description
-----------

Process a user generated STATICADD message and add a new unlabeled
connection entry to the hash table.  Returns zero on success, negative
values on failure.

.. _`netlbl_unlabel_staticadddef`:

netlbl_unlabel_staticadddef
===========================

.. c:function:: int netlbl_unlabel_staticadddef(struct sk_buff *skb, struct genl_info *info)

    Handle a STATICADDDEF message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_unlabel_staticadddef.description`:

Description
-----------

Process a user generated STATICADDDEF message and add a new default
unlabeled connection entry.  Returns zero on success, negative values on
failure.

.. _`netlbl_unlabel_staticremove`:

netlbl_unlabel_staticremove
===========================

.. c:function:: int netlbl_unlabel_staticremove(struct sk_buff *skb, struct genl_info *info)

    Handle a STATICREMOVE message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_unlabel_staticremove.description`:

Description
-----------

Process a user generated STATICREMOVE message and remove the specified
unlabeled connection entry.  Returns zero on success, negative values on
failure.

.. _`netlbl_unlabel_staticremovedef`:

netlbl_unlabel_staticremovedef
==============================

.. c:function:: int netlbl_unlabel_staticremovedef(struct sk_buff *skb, struct genl_info *info)

    Handle a STATICREMOVEDEF message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param info:
        the Generic NETLINK info block
    :type info: struct genl_info \*

.. _`netlbl_unlabel_staticremovedef.description`:

Description
-----------

Process a user generated STATICREMOVEDEF message and remove the default
unlabeled connection entry.  Returns zero on success, negative values on
failure.

.. _`netlbl_unlabel_staticlist_gen`:

netlbl_unlabel_staticlist_gen
=============================

.. c:function:: int netlbl_unlabel_staticlist_gen(u32 cmd, const struct netlbl_unlhsh_iface *iface, const struct netlbl_unlhsh_addr4 *addr4, const struct netlbl_unlhsh_addr6 *addr6, void *arg)

    Generate messages for STATICLIST[DEF]

    :param cmd:
        command/message
    :type cmd: u32

    :param iface:
        the interface entry
    :type iface: const struct netlbl_unlhsh_iface \*

    :param addr4:
        the IPv4 address entry
    :type addr4: const struct netlbl_unlhsh_addr4 \*

    :param addr6:
        the IPv6 address entry
    :type addr6: const struct netlbl_unlhsh_addr6 \*

    :param arg:
        the netlbl_unlhsh_walk_arg structure
    :type arg: void \*

.. _`netlbl_unlabel_staticlist_gen.description`:

Description
-----------

This function is designed to be used to generate a response for a
STATICLIST or STATICLISTDEF message.  When called either \ ``addr4``\  or \ ``addr6``\ 
can be specified, not both, the other unspecified entry should be set to
NULL by the caller.  Returns the size of the message on success, negative
values on failure.

.. _`netlbl_unlabel_staticlist`:

netlbl_unlabel_staticlist
=========================

.. c:function:: int netlbl_unlabel_staticlist(struct sk_buff *skb, struct netlink_callback *cb)

    Handle a STATICLIST message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param cb:
        the NETLINK callback
    :type cb: struct netlink_callback \*

.. _`netlbl_unlabel_staticlist.description`:

Description
-----------

Process a user generated STATICLIST message and dump the unlabeled
connection hash table in a form suitable for use in a kernel generated
STATICLIST message.  Returns the length of \ ``skb``\ .

.. _`netlbl_unlabel_staticlistdef`:

netlbl_unlabel_staticlistdef
============================

.. c:function:: int netlbl_unlabel_staticlistdef(struct sk_buff *skb, struct netlink_callback *cb)

    Handle a STATICLISTDEF message

    :param skb:
        the NETLINK buffer
    :type skb: struct sk_buff \*

    :param cb:
        the NETLINK callback
    :type cb: struct netlink_callback \*

.. _`netlbl_unlabel_staticlistdef.description`:

Description
-----------

Process a user generated STATICLISTDEF message and dump the default
unlabeled connection entry in a form suitable for use in a kernel generated
STATICLISTDEF message.  Returns the length of \ ``skb``\ .

.. _`netlbl_unlabel_genl_init`:

netlbl_unlabel_genl_init
========================

.. c:function:: int netlbl_unlabel_genl_init( void)

    Register the Unlabeled NetLabel component

    :param void:
        no arguments
    :type void: 

.. _`netlbl_unlabel_genl_init.description`:

Description
-----------

Register the unlabeled packet NetLabel component with the Generic NETLINK
mechanism.  Returns zero on success, negative values on failure.

.. _`netlbl_unlabel_init`:

netlbl_unlabel_init
===================

.. c:function:: int netlbl_unlabel_init(u32 size)

    Initialize the unlabeled connection hash table

    :param size:
        the number of bits to use for the hash buckets
    :type size: u32

.. _`netlbl_unlabel_init.description`:

Description
-----------

Initializes the unlabeled connection hash table and registers a network
device notification handler.  This function should only be called by the
NetLabel subsystem itself during initialization.  Returns zero on success,
non-zero values on error.

.. _`netlbl_unlabel_getattr`:

netlbl_unlabel_getattr
======================

.. c:function:: int netlbl_unlabel_getattr(const struct sk_buff *skb, u16 family, struct netlbl_lsm_secattr *secattr)

    Get the security attributes for an unlabled packet

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param family:
        protocol family
    :type family: u16

    :param secattr:
        the security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`netlbl_unlabel_getattr.description`:

Description
-----------

Determine the security attributes, if any, for an unlabled packet and return
them in \ ``secattr``\ .  Returns zero on success and negative values on failure.

.. _`netlbl_unlabel_defconf`:

netlbl_unlabel_defconf
======================

.. c:function:: int netlbl_unlabel_defconf( void)

    Set the default config to allow unlabeled packets

    :param void:
        no arguments
    :type void: 

.. _`netlbl_unlabel_defconf.description`:

Description
-----------

Set the default NetLabel configuration to allow incoming unlabeled packets
and to send unlabeled network traffic by default.

.. This file was automatic generated / don't edit.

