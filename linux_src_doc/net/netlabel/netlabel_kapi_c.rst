.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_kapi.c

.. _`netlbl_cfg_map_del`:

netlbl_cfg_map_del
==================

.. c:function:: int netlbl_cfg_map_del(const char *domain, u16 family, const void *addr, const void *mask, struct netlbl_audit *audit_info)

    Remove a NetLabel/LSM domain mapping

    :param domain:
        the domain mapping to remove
    :type domain: const char \*

    :param family:
        address family
    :type family: u16

    :param addr:
        IP address
    :type addr: const void \*

    :param mask:
        IP address mask
    :type mask: const void \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_map_del.description`:

Description
-----------

Removes a NetLabel/LSM domain mapping.  A \ ``domain``\  value of NULL causes the
default domain mapping to be removed.  Returns zero on success, negative
values on failure.

.. _`netlbl_cfg_unlbl_map_add`:

netlbl_cfg_unlbl_map_add
========================

.. c:function:: int netlbl_cfg_unlbl_map_add(const char *domain, u16 family, const void *addr, const void *mask, struct netlbl_audit *audit_info)

    Add a new unlabeled mapping

    :param domain:
        the domain mapping to add
    :type domain: const char \*

    :param family:
        address family
    :type family: u16

    :param addr:
        IP address
    :type addr: const void \*

    :param mask:
        IP address mask
    :type mask: const void \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_unlbl_map_add.description`:

Description
-----------

Adds a new unlabeled NetLabel/LSM domain mapping.  A \ ``domain``\  value of NULL
causes a new default domain mapping to be added.  Returns zero on success,
negative values on failure.

.. _`netlbl_cfg_unlbl_static_add`:

netlbl_cfg_unlbl_static_add
===========================

.. c:function:: int netlbl_cfg_unlbl_static_add(struct net *net, const char *dev_name, const void *addr, const void *mask, u16 family, u32 secid, struct netlbl_audit *audit_info)

    Adds a new static label

    :param net:
        network namespace
    :type net: struct net \*

    :param dev_name:
        interface name
    :type dev_name: const char \*

    :param addr:
        IP address in network byte order (struct in[6]_addr)
    :type addr: const void \*

    :param mask:
        address mask in network byte order (struct in[6]_addr)
    :type mask: const void \*

    :param family:
        address family
    :type family: u16

    :param secid:
        LSM secid value for the entry
    :type secid: u32

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_unlbl_static_add.description`:

Description
-----------

Adds a new NetLabel static label to be used when protocol provided labels
are not present on incoming traffic.  If \ ``dev_name``\  is NULL then the default
interface will be used.  Returns zero on success, negative values on failure.

.. _`netlbl_cfg_unlbl_static_del`:

netlbl_cfg_unlbl_static_del
===========================

.. c:function:: int netlbl_cfg_unlbl_static_del(struct net *net, const char *dev_name, const void *addr, const void *mask, u16 family, struct netlbl_audit *audit_info)

    Removes an existing static label

    :param net:
        network namespace
    :type net: struct net \*

    :param dev_name:
        interface name
    :type dev_name: const char \*

    :param addr:
        IP address in network byte order (struct in[6]_addr)
    :type addr: const void \*

    :param mask:
        address mask in network byte order (struct in[6]_addr)
    :type mask: const void \*

    :param family:
        address family
    :type family: u16

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_unlbl_static_del.description`:

Description
-----------

Removes an existing NetLabel static label used when protocol provided labels
are not present on incoming traffic.  If \ ``dev_name``\  is NULL then the default
interface will be used.  Returns zero on success, negative values on failure.

.. _`netlbl_cfg_cipsov4_add`:

netlbl_cfg_cipsov4_add
======================

.. c:function:: int netlbl_cfg_cipsov4_add(struct cipso_v4_doi *doi_def, struct netlbl_audit *audit_info)

    Add a new CIPSOv4 DOI definition

    :param doi_def:
        CIPSO DOI definition
    :type doi_def: struct cipso_v4_doi \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_cipsov4_add.description`:

Description
-----------

Add a new CIPSO DOI definition as defined by \ ``doi_def``\ .  Returns zero on
success and negative values on failure.

.. _`netlbl_cfg_cipsov4_del`:

netlbl_cfg_cipsov4_del
======================

.. c:function:: void netlbl_cfg_cipsov4_del(u32 doi, struct netlbl_audit *audit_info)

    Remove an existing CIPSOv4 DOI definition

    :param doi:
        CIPSO DOI
    :type doi: u32

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_cipsov4_del.description`:

Description
-----------

Remove an existing CIPSO DOI definition matching \ ``doi``\ .  Returns zero on
success and negative values on failure.

.. _`netlbl_cfg_cipsov4_map_add`:

netlbl_cfg_cipsov4_map_add
==========================

.. c:function:: int netlbl_cfg_cipsov4_map_add(u32 doi, const char *domain, const struct in_addr *addr, const struct in_addr *mask, struct netlbl_audit *audit_info)

    Add a new CIPSOv4 DOI mapping

    :param doi:
        the CIPSO DOI
    :type doi: u32

    :param domain:
        the domain mapping to add
    :type domain: const char \*

    :param addr:
        IP address
    :type addr: const struct in_addr \*

    :param mask:
        IP address mask
    :type mask: const struct in_addr \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_cipsov4_map_add.description`:

Description
-----------

Add a new NetLabel/LSM domain mapping for the given CIPSO DOI to the NetLabel
subsystem.  A \ ``domain``\  value of NULL adds a new default domain mapping.
Returns zero on success, negative values on failure.

.. _`netlbl_cfg_calipso_add`:

netlbl_cfg_calipso_add
======================

.. c:function:: int netlbl_cfg_calipso_add(struct calipso_doi *doi_def, struct netlbl_audit *audit_info)

    Add a new CALIPSO DOI definition

    :param doi_def:
        CALIPSO DOI definition
    :type doi_def: struct calipso_doi \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_calipso_add.description`:

Description
-----------

Add a new CALIPSO DOI definition as defined by \ ``doi_def``\ .  Returns zero on
success and negative values on failure.

.. _`netlbl_cfg_calipso_del`:

netlbl_cfg_calipso_del
======================

.. c:function:: void netlbl_cfg_calipso_del(u32 doi, struct netlbl_audit *audit_info)

    Remove an existing CALIPSO DOI definition

    :param doi:
        CALIPSO DOI
    :type doi: u32

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_calipso_del.description`:

Description
-----------

Remove an existing CALIPSO DOI definition matching \ ``doi``\ .  Returns zero on
success and negative values on failure.

.. _`netlbl_cfg_calipso_map_add`:

netlbl_cfg_calipso_map_add
==========================

.. c:function:: int netlbl_cfg_calipso_map_add(u32 doi, const char *domain, const struct in6_addr *addr, const struct in6_addr *mask, struct netlbl_audit *audit_info)

    Add a new CALIPSO DOI mapping

    :param doi:
        the CALIPSO DOI
    :type doi: u32

    :param domain:
        the domain mapping to add
    :type domain: const char \*

    :param addr:
        IP address
    :type addr: const struct in6_addr \*

    :param mask:
        IP address mask
    :type mask: const struct in6_addr \*

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_cfg_calipso_map_add.description`:

Description
-----------

Add a new NetLabel/LSM domain mapping for the given CALIPSO DOI to the
NetLabel subsystem.  A \ ``domain``\  value of NULL adds a new default domain
mapping.  Returns zero on success, negative values on failure.

.. _`_netlbl_catmap_getnode`:

\_netlbl_catmap_getnode
=======================

.. c:function:: struct netlbl_lsm_catmap *_netlbl_catmap_getnode(struct netlbl_lsm_catmap **catmap, u32 offset, unsigned int cm_flags, gfp_t gfp_flags)

    Get a individual node from a catmap

    :param catmap:
        pointer to the category bitmap
    :type catmap: struct netlbl_lsm_catmap \*\*

    :param offset:
        the requested offset
    :type offset: u32

    :param cm_flags:
        catmap flags, see \_CM_F\_\*
    :type cm_flags: unsigned int

    :param gfp_flags:
        memory allocation flags
    :type gfp_flags: gfp_t

.. _`_netlbl_catmap_getnode.description`:

Description
-----------

Iterate through the catmap looking for the node associated with \ ``offset``\ .
If the \_CM_F_ALLOC flag is set in \ ``cm_flags``\  and there is no associated node,
one will be created and inserted into the catmap.  If the \_CM_F_WALK flag is
set in \ ``cm_flags``\  and there is no associated node, the next highest node will
be returned.  Returns a pointer to the node on success, NULL on failure.

.. _`netlbl_catmap_walk`:

netlbl_catmap_walk
==================

.. c:function:: int netlbl_catmap_walk(struct netlbl_lsm_catmap *catmap, u32 offset)

    Walk a LSM secattr catmap looking for a bit

    :param catmap:
        the category bitmap
    :type catmap: struct netlbl_lsm_catmap \*

    :param offset:
        the offset to start searching at, in bits
    :type offset: u32

.. _`netlbl_catmap_walk.description`:

Description
-----------

This function walks a LSM secattr category bitmap starting at \ ``offset``\  and
returns the spot of the first set bit or -ENOENT if no bits are set.

.. _`netlbl_catmap_walkrng`:

netlbl_catmap_walkrng
=====================

.. c:function:: int netlbl_catmap_walkrng(struct netlbl_lsm_catmap *catmap, u32 offset)

    Find the end of a string of set bits

    :param catmap:
        the category bitmap
    :type catmap: struct netlbl_lsm_catmap \*

    :param offset:
        the offset to start searching at, in bits
    :type offset: u32

.. _`netlbl_catmap_walkrng.description`:

Description
-----------

This function walks a LSM secattr category bitmap starting at \ ``offset``\  and
returns the spot of the first cleared bit or -ENOENT if the offset is past
the end of the bitmap.

.. _`netlbl_catmap_getlong`:

netlbl_catmap_getlong
=====================

.. c:function:: int netlbl_catmap_getlong(struct netlbl_lsm_catmap *catmap, u32 *offset, unsigned long *bitmap)

    Export an unsigned long bitmap

    :param catmap:
        pointer to the category bitmap
    :type catmap: struct netlbl_lsm_catmap \*

    :param offset:
        pointer to the requested offset
    :type offset: u32 \*

    :param bitmap:
        the exported bitmap
    :type bitmap: unsigned long \*

.. _`netlbl_catmap_getlong.description`:

Description
-----------

Export a bitmap with an offset greater than or equal to \ ``offset``\  and return
it in \ ``bitmap``\ .  The \ ``offset``\  must be aligned to an unsigned long and will be
updated on return if different from what was requested; if the catmap is
empty at the requested offset and beyond, the \ ``offset``\  is set to (u32)-1.
Returns zero on sucess, negative values on failure.

.. _`netlbl_catmap_setbit`:

netlbl_catmap_setbit
====================

.. c:function:: int netlbl_catmap_setbit(struct netlbl_lsm_catmap **catmap, u32 bit, gfp_t flags)

    Set a bit in a LSM secattr catmap

    :param catmap:
        pointer to the category bitmap
    :type catmap: struct netlbl_lsm_catmap \*\*

    :param bit:
        the bit to set
    :type bit: u32

    :param flags:
        memory allocation flags
    :type flags: gfp_t

.. _`netlbl_catmap_setbit.description`:

Description
-----------

Set the bit specified by \ ``bit``\  in \ ``catmap``\ .  Returns zero on success,
negative values on failure.

.. _`netlbl_catmap_setrng`:

netlbl_catmap_setrng
====================

.. c:function:: int netlbl_catmap_setrng(struct netlbl_lsm_catmap **catmap, u32 start, u32 end, gfp_t flags)

    Set a range of bits in a LSM secattr catmap

    :param catmap:
        pointer to the category bitmap
    :type catmap: struct netlbl_lsm_catmap \*\*

    :param start:
        the starting bit
    :type start: u32

    :param end:
        the last bit in the string
    :type end: u32

    :param flags:
        memory allocation flags
    :type flags: gfp_t

.. _`netlbl_catmap_setrng.description`:

Description
-----------

Set a range of bits, starting at \ ``start``\  and ending with \ ``end``\ .  Returns zero
on success, negative values on failure.

.. _`netlbl_catmap_setlong`:

netlbl_catmap_setlong
=====================

.. c:function:: int netlbl_catmap_setlong(struct netlbl_lsm_catmap **catmap, u32 offset, unsigned long bitmap, gfp_t flags)

    Import an unsigned long bitmap

    :param catmap:
        pointer to the category bitmap
    :type catmap: struct netlbl_lsm_catmap \*\*

    :param offset:
        offset to the start of the imported bitmap
    :type offset: u32

    :param bitmap:
        the bitmap to import
    :type bitmap: unsigned long

    :param flags:
        memory allocation flags
    :type flags: gfp_t

.. _`netlbl_catmap_setlong.description`:

Description
-----------

Import the bitmap specified in \ ``bitmap``\  into \ ``catmap``\ , using the offset
in \ ``offset``\ .  The offset must be aligned to an unsigned long.  Returns zero
on success, negative values on failure.

.. _`netlbl_bitmap_walk`:

netlbl_bitmap_walk
==================

.. c:function:: int netlbl_bitmap_walk(const unsigned char *bitmap, u32 bitmap_len, u32 offset, u8 state)

    Walk a bitmap looking for a bit

    :param bitmap:
        the bitmap
    :type bitmap: const unsigned char \*

    :param bitmap_len:
        length in bits
    :type bitmap_len: u32

    :param offset:
        starting offset
    :type offset: u32

    :param state:
        if non-zero, look for a set (1) bit else look for a cleared (0) bit
    :type state: u8

.. _`netlbl_bitmap_walk.description`:

Description
-----------

Starting at \ ``offset``\ , walk the bitmap from left to right until either the
desired bit is found or we reach the end.  Return the bit offset, -1 if
not found, or -2 if error.

.. _`netlbl_bitmap_setbit`:

netlbl_bitmap_setbit
====================

.. c:function:: void netlbl_bitmap_setbit(unsigned char *bitmap, u32 bit, u8 state)

    Sets a single bit in a bitmap

    :param bitmap:
        the bitmap
    :type bitmap: unsigned char \*

    :param bit:
        the bit
    :type bit: u32

    :param state:
        if non-zero, set the bit (1) else clear the bit (0)
    :type state: u8

.. _`netlbl_bitmap_setbit.description`:

Description
-----------

Set a single bit in the bitmask.  Returns zero on success, negative values
on error.

.. _`netlbl_enabled`:

netlbl_enabled
==============

.. c:function:: int netlbl_enabled( void)

    Determine if the NetLabel subsystem is enabled

    :param void:
        no arguments
    :type void: 

.. _`netlbl_enabled.description`:

Description
-----------

The LSM can use this function to determine if it should use NetLabel
security attributes in it's enforcement mechanism.  Currently, NetLabel is
considered to be enabled when it's configuration contains a valid setup for
at least one labeled protocol (i.e. NetLabel can understand incoming
labeled packets of at least one type); otherwise NetLabel is considered to
be disabled.

.. _`netlbl_sock_setattr`:

netlbl_sock_setattr
===================

.. c:function:: int netlbl_sock_setattr(struct sock *sk, u16 family, const struct netlbl_lsm_secattr *secattr)

    Label a socket using the correct protocol

    :param sk:
        the socket to label
    :type sk: struct sock \*

    :param family:
        protocol family
    :type family: u16

    :param secattr:
        the security attributes
    :type secattr: const struct netlbl_lsm_secattr \*

.. _`netlbl_sock_setattr.description`:

Description
-----------

Attach the correct label to the given socket using the security attributes
specified in \ ``secattr``\ .  This function requires exclusive access to \ ``sk``\ ,
which means it either needs to be in the process of being created or locked.
Returns zero on success, -EDESTADDRREQ if the domain is configured to use
network address selectors (can't blindly label the socket), and negative
values on all other failures.

.. _`netlbl_sock_delattr`:

netlbl_sock_delattr
===================

.. c:function:: void netlbl_sock_delattr(struct sock *sk)

    Delete all the NetLabel labels on a socket

    :param sk:
        the socket
    :type sk: struct sock \*

.. _`netlbl_sock_delattr.description`:

Description
-----------

Remove all the NetLabel labeling from \ ``sk``\ .  The caller is responsible for
ensuring that \ ``sk``\  is locked.

.. _`netlbl_sock_getattr`:

netlbl_sock_getattr
===================

.. c:function:: int netlbl_sock_getattr(struct sock *sk, struct netlbl_lsm_secattr *secattr)

    Determine the security attributes of a sock

    :param sk:
        the sock
    :type sk: struct sock \*

    :param secattr:
        the security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`netlbl_sock_getattr.description`:

Description
-----------

Examines the given sock to see if any NetLabel style labeling has been
applied to the sock, if so it parses the socket label and returns the
security attributes in \ ``secattr``\ .  Returns zero on success, negative values
on failure.

.. _`netlbl_conn_setattr`:

netlbl_conn_setattr
===================

.. c:function:: int netlbl_conn_setattr(struct sock *sk, struct sockaddr *addr, const struct netlbl_lsm_secattr *secattr)

    Label a connected socket using the correct protocol

    :param sk:
        the socket to label
    :type sk: struct sock \*

    :param addr:
        the destination address
    :type addr: struct sockaddr \*

    :param secattr:
        the security attributes
    :type secattr: const struct netlbl_lsm_secattr \*

.. _`netlbl_conn_setattr.description`:

Description
-----------

Attach the correct label to the given connected socket using the security
attributes specified in \ ``secattr``\ .  The caller is responsible for ensuring
that \ ``sk``\  is locked.  Returns zero on success, negative values on failure.

.. _`netlbl_req_setattr`:

netlbl_req_setattr
==================

.. c:function:: int netlbl_req_setattr(struct request_sock *req, const struct netlbl_lsm_secattr *secattr)

    Label a request socket using the correct protocol

    :param req:
        the request socket to label
    :type req: struct request_sock \*

    :param secattr:
        the security attributes
    :type secattr: const struct netlbl_lsm_secattr \*

.. _`netlbl_req_setattr.description`:

Description
-----------

Attach the correct label to the given socket using the security attributes
specified in \ ``secattr``\ .  Returns zero on success, negative values on failure.

.. _`netlbl_req_delattr`:

netlbl_req_delattr
==================

.. c:function:: void netlbl_req_delattr(struct request_sock *req)

    Delete all the NetLabel labels on a socket

    :param req:
        the socket
    :type req: struct request_sock \*

.. _`netlbl_req_delattr.description`:

Description
-----------

Remove all the NetLabel labeling from \ ``req``\ .

.. _`netlbl_skbuff_setattr`:

netlbl_skbuff_setattr
=====================

.. c:function:: int netlbl_skbuff_setattr(struct sk_buff *skb, u16 family, const struct netlbl_lsm_secattr *secattr)

    Label a packet using the correct protocol

    :param skb:
        the packet
    :type skb: struct sk_buff \*

    :param family:
        protocol family
    :type family: u16

    :param secattr:
        the security attributes
    :type secattr: const struct netlbl_lsm_secattr \*

.. _`netlbl_skbuff_setattr.description`:

Description
-----------

Attach the correct label to the given packet using the security attributes
specified in \ ``secattr``\ .  Returns zero on success, negative values on failure.

.. _`netlbl_skbuff_getattr`:

netlbl_skbuff_getattr
=====================

.. c:function:: int netlbl_skbuff_getattr(const struct sk_buff *skb, u16 family, struct netlbl_lsm_secattr *secattr)

    Determine the security attributes of a packet

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param family:
        protocol family
    :type family: u16

    :param secattr:
        the security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`netlbl_skbuff_getattr.description`:

Description
-----------

Examines the given packet to see if a recognized form of packet labeling
is present, if so it parses the packet label and returns the security
attributes in \ ``secattr``\ .  Returns zero on success, negative values on
failure.

.. _`netlbl_skbuff_err`:

netlbl_skbuff_err
=================

.. c:function:: void netlbl_skbuff_err(struct sk_buff *skb, u16 family, int error, int gateway)

    Handle a LSM error on a sk_buff

    :param skb:
        the packet
    :type skb: struct sk_buff \*

    :param family:
        the family
    :type family: u16

    :param error:
        the error code
    :type error: int

    :param gateway:
        true if host is acting as a gateway, false otherwise
    :type gateway: int

.. _`netlbl_skbuff_err.description`:

Description
-----------

Deal with a LSM problem when handling the packet in \ ``skb``\ , typically this is
a permission denied problem (-EACCES).  The correct action is determined
according to the packet's labeling protocol.

.. _`netlbl_cache_invalidate`:

netlbl_cache_invalidate
=======================

.. c:function:: void netlbl_cache_invalidate( void)

    Invalidate all of the NetLabel protocol caches

    :param void:
        no arguments
    :type void: 

.. _`netlbl_cache_invalidate.description`:

Description
-----------

For all of the NetLabel protocols that support some form of label mapping
cache, invalidate the cache.  Returns zero on success, negative values on
error.

.. _`netlbl_cache_add`:

netlbl_cache_add
================

.. c:function:: int netlbl_cache_add(const struct sk_buff *skb, u16 family, const struct netlbl_lsm_secattr *secattr)

    Add an entry to a NetLabel protocol cache

    :param skb:
        the packet
    :type skb: const struct sk_buff \*

    :param family:
        the family
    :type family: u16

    :param secattr:
        the packet's security attributes
    :type secattr: const struct netlbl_lsm_secattr \*

.. _`netlbl_cache_add.description`:

Description
-----------

Add the LSM security attributes for the given packet to the underlying
NetLabel protocol's label mapping cache.  Returns zero on success, negative
values on error.

.. _`netlbl_audit_start`:

netlbl_audit_start
==================

.. c:function:: struct audit_buffer *netlbl_audit_start(int type, struct netlbl_audit *audit_info)

    Start an audit message

    :param type:
        audit message type
    :type type: int

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_audit_start.description`:

Description
-----------

Start an audit message using the type specified in \ ``type``\  and fill the audit
message with some fields common to all NetLabel audit messages.  This
function should only be used by protocol engines, not LSMs.  Returns a
pointer to the audit buffer on success, NULL on failure.

.. _`netlbl_init`:

netlbl_init
===========

.. c:function:: int netlbl_init( void)

    Initialize NetLabel

    :param void:
        no arguments
    :type void: 

.. _`netlbl_init.description`:

Description
-----------

Perform the required NetLabel initialization before first use.

.. This file was automatic generated / don't edit.

