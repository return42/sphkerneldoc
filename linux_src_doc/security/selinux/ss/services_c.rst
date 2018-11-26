.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/selinux/ss/services.c

.. _`security_compute_av`:

security_compute_av
===================

.. c:function:: void security_compute_av(struct selinux_state *state, u32 ssid, u32 tsid, u16 orig_tclass, struct av_decision *avd, struct extended_perms *xperms)

    Compute access vector decisions.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param orig_tclass:
        *undescribed*
    :type orig_tclass: u16

    :param avd:
        access vector decisions
    :type avd: struct av_decision \*

    :param xperms:
        extended permissions
    :type xperms: struct extended_perms \*

.. _`security_compute_av.description`:

Description
-----------

Compute a set of access vector decisions based on the
SID pair (@ssid, \ ``tsid``\ ) for the permissions in \ ``tclass``\ .

.. _`security_sid_to_context`:

security_sid_to_context
=======================

.. c:function:: int security_sid_to_context(struct selinux_state *state, u32 sid, char **scontext, u32 *scontext_len)

    Obtain a context for a given SID.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param sid:
        security identifier, SID
    :type sid: u32

    :param scontext:
        security context
    :type scontext: char \*\*

    :param scontext_len:
        length in bytes
    :type scontext_len: u32 \*

.. _`security_sid_to_context.description`:

Description
-----------

Write the string representation of the context associated with \ ``sid``\ 
into a dynamically allocated string of the correct size.  Set \ ``scontext``\ 
to point to this string and set \ ``scontext_len``\  to the length of the string.

.. _`security_context_to_sid`:

security_context_to_sid
=======================

.. c:function:: int security_context_to_sid(struct selinux_state *state, const char *scontext, u32 scontext_len, u32 *sid, gfp_t gfp)

    Obtain a SID for a given security context.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param scontext:
        security context
    :type scontext: const char \*

    :param scontext_len:
        length in bytes
    :type scontext_len: u32

    :param sid:
        security identifier, SID
    :type sid: u32 \*

    :param gfp:
        context for the allocation
    :type gfp: gfp_t

.. _`security_context_to_sid.description`:

Description
-----------

Obtains a SID associated with the security context that
has the string representation specified by \ ``scontext``\ .
Returns -%EINVAL if the context is invalid, -%ENOMEM if insufficient
memory is available, or 0 on success.

.. _`security_context_to_sid_default`:

security_context_to_sid_default
===============================

.. c:function:: int security_context_to_sid_default(struct selinux_state *state, const char *scontext, u32 scontext_len, u32 *sid, u32 def_sid, gfp_t gfp_flags)

    Obtain a SID for a given security context, falling back to specified default if needed.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param scontext:
        security context
    :type scontext: const char \*

    :param scontext_len:
        length in bytes
    :type scontext_len: u32

    :param sid:
        security identifier, SID
    :type sid: u32 \*

    :param def_sid:
        default SID to assign on error
    :type def_sid: u32

    :param gfp_flags:
        *undescribed*
    :type gfp_flags: gfp_t

.. _`security_context_to_sid_default.description`:

Description
-----------

Obtains a SID associated with the security context that
has the string representation specified by \ ``scontext``\ .
The default SID is passed to the MLS layer to be used to allow
kernel labeling of the MLS field if the MLS field is not present
(for upgrading to MLS without full relabel).
Implicitly forces adding of the context even if it cannot be mapped yet.
Returns -%EINVAL if the context is invalid, -%ENOMEM if insufficient
memory is available, or 0 on success.

.. _`security_transition_sid`:

security_transition_sid
=======================

.. c:function:: int security_transition_sid(struct selinux_state *state, u32 ssid, u32 tsid, u16 tclass, const struct qstr *qstr, u32 *out_sid)

    Compute the SID for a new subject/object.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param tclass:
        target security class
    :type tclass: u16

    :param qstr:
        *undescribed*
    :type qstr: const struct qstr \*

    :param out_sid:
        security identifier for new subject/object
    :type out_sid: u32 \*

.. _`security_transition_sid.description`:

Description
-----------

Compute a SID to use for labeling a new subject or object in the
class \ ``tclass``\  based on a SID pair (@ssid, \ ``tsid``\ ).
Return -%EINVAL if any of the parameters are invalid, -%ENOMEM
if insufficient memory is available, or \ ``0``\  if the new SID was
computed successfully.

.. _`security_member_sid`:

security_member_sid
===================

.. c:function:: int security_member_sid(struct selinux_state *state, u32 ssid, u32 tsid, u16 tclass, u32 *out_sid)

    Compute the SID for member selection.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param tclass:
        target security class
    :type tclass: u16

    :param out_sid:
        security identifier for selected member
    :type out_sid: u32 \*

.. _`security_member_sid.description`:

Description
-----------

Compute a SID to use when selecting a member of a polyinstantiated
object of class \ ``tclass``\  based on a SID pair (@ssid, \ ``tsid``\ ).
Return -%EINVAL if any of the parameters are invalid, -%ENOMEM
if insufficient memory is available, or \ ``0``\  if the SID was
computed successfully.

.. _`security_change_sid`:

security_change_sid
===================

.. c:function:: int security_change_sid(struct selinux_state *state, u32 ssid, u32 tsid, u16 tclass, u32 *out_sid)

    Compute the SID for object relabeling.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param ssid:
        source security identifier
    :type ssid: u32

    :param tsid:
        target security identifier
    :type tsid: u32

    :param tclass:
        target security class
    :type tclass: u16

    :param out_sid:
        security identifier for selected member
    :type out_sid: u32 \*

.. _`security_change_sid.description`:

Description
-----------

Compute a SID to use for relabeling an object of class \ ``tclass``\ 
based on a SID pair (@ssid, \ ``tsid``\ ).
Return -%EINVAL if any of the parameters are invalid, -%ENOMEM
if insufficient memory is available, or \ ``0``\  if the SID was
computed successfully.

.. _`security_load_policy`:

security_load_policy
====================

.. c:function:: int security_load_policy(struct selinux_state *state, void *data, size_t len)

    Load a security policy configuration.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param data:
        binary policy data
    :type data: void \*

    :param len:
        length of data in bytes
    :type len: size_t

.. _`security_load_policy.description`:

Description
-----------

Load a new set of security policy configuration data,
validate it and convert the SID table as necessary.
This function will flush the access vector cache after
loading the new policy.

.. _`security_port_sid`:

security_port_sid
=================

.. c:function:: int security_port_sid(struct selinux_state *state, u8 protocol, u16 port, u32 *out_sid)

    Obtain the SID for a port.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param protocol:
        protocol number
    :type protocol: u8

    :param port:
        port number
    :type port: u16

    :param out_sid:
        security identifier
    :type out_sid: u32 \*

.. _`security_ib_pkey_sid`:

security_ib_pkey_sid
====================

.. c:function:: int security_ib_pkey_sid(struct selinux_state *state, u64 subnet_prefix, u16 pkey_num, u32 *out_sid)

    Obtain the SID for a pkey.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param subnet_prefix:
        Subnet Prefix
    :type subnet_prefix: u64

    :param pkey_num:
        pkey number
    :type pkey_num: u16

    :param out_sid:
        security identifier
    :type out_sid: u32 \*

.. _`security_ib_endport_sid`:

security_ib_endport_sid
=======================

.. c:function:: int security_ib_endport_sid(struct selinux_state *state, const char *dev_name, u8 port_num, u32 *out_sid)

    Obtain the SID for a subnet management interface.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param dev_name:
        device name
    :type dev_name: const char \*

    :param port_num:
        *undescribed*
    :type port_num: u8

    :param out_sid:
        security identifier
    :type out_sid: u32 \*

.. _`security_netif_sid`:

security_netif_sid
==================

.. c:function:: int security_netif_sid(struct selinux_state *state, char *name, u32 *if_sid)

    Obtain the SID for a network interface.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param name:
        interface name
    :type name: char \*

    :param if_sid:
        interface SID
    :type if_sid: u32 \*

.. _`security_node_sid`:

security_node_sid
=================

.. c:function:: int security_node_sid(struct selinux_state *state, u16 domain, void *addrp, u32 addrlen, u32 *out_sid)

    Obtain the SID for a node (host).

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param domain:
        communication domain aka address family
    :type domain: u16

    :param addrp:
        address
    :type addrp: void \*

    :param addrlen:
        address length in bytes
    :type addrlen: u32

    :param out_sid:
        security identifier
    :type out_sid: u32 \*

.. _`security_get_user_sids`:

security_get_user_sids
======================

.. c:function:: int security_get_user_sids(struct selinux_state *state, u32 fromsid, char *username, u32 **sids, u32 *nel)

    Obtain reachable SIDs for a user.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param fromsid:
        starting SID
    :type fromsid: u32

    :param username:
        username
    :type username: char \*

    :param sids:
        array of reachable SIDs for user
    :type sids: u32 \*\*

    :param nel:
        number of elements in \ ``sids``\ 
    :type nel: u32 \*

.. _`security_get_user_sids.description`:

Description
-----------

Generate the set of SIDs for legal security contexts
for a given user that can be reached by \ ``fromsid``\ .
Set \*@sids to point to a dynamically allocated
array containing the set of SIDs.  Set \*@nel to the
number of elements in the array.

.. _`__security_genfs_sid`:

\__security_genfs_sid
=====================

.. c:function:: int __security_genfs_sid(struct selinux_state *state, const char *fstype, char *path, u16 orig_sclass, u32 *sid)

    Helper to obtain a SID for a file in a filesystem

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param fstype:
        filesystem type
    :type fstype: const char \*

    :param path:
        path from root of mount
    :type path: char \*

    :param orig_sclass:
        *undescribed*
    :type orig_sclass: u16

    :param sid:
        SID for path
    :type sid: u32 \*

.. _`__security_genfs_sid.description`:

Description
-----------

Obtain a SID to use for a file in a filesystem that
cannot support xattr or use a fixed labeling behavior like
transition SIDs or task SIDs.

The caller must acquire the policy_rwlock before calling this function.

.. _`security_genfs_sid`:

security_genfs_sid
==================

.. c:function:: int security_genfs_sid(struct selinux_state *state, const char *fstype, char *path, u16 orig_sclass, u32 *sid)

    Obtain a SID for a file in a filesystem

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param fstype:
        filesystem type
    :type fstype: const char \*

    :param path:
        path from root of mount
    :type path: char \*

    :param orig_sclass:
        *undescribed*
    :type orig_sclass: u16

    :param sid:
        SID for path
    :type sid: u32 \*

.. _`security_genfs_sid.description`:

Description
-----------

Acquire policy_rwlock before calling \__security_genfs_sid() and release
it afterward.

.. _`security_fs_use`:

security_fs_use
===============

.. c:function:: int security_fs_use(struct selinux_state *state, struct super_block *sb)

    Determine how to handle labeling for a filesystem.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param sb:
        superblock in question
    :type sb: struct super_block \*

.. _`security_net_peersid_resolve`:

security_net_peersid_resolve
============================

.. c:function:: int security_net_peersid_resolve(struct selinux_state *state, u32 nlbl_sid, u32 nlbl_type, u32 xfrm_sid, u32 *peer_sid)

    Compare and resolve two network peer SIDs

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param nlbl_sid:
        NetLabel SID
    :type nlbl_sid: u32

    :param nlbl_type:
        NetLabel labeling protocol type
    :type nlbl_type: u32

    :param xfrm_sid:
        XFRM SID
    :type xfrm_sid: u32

    :param peer_sid:
        *undescribed*
    :type peer_sid: u32 \*

.. _`security_net_peersid_resolve.description`:

Description
-----------

Compare the \ ``nlbl_sid``\  and \ ``xfrm_sid``\  values and if the two SIDs can be
resolved into a single SID it is returned via \ ``peer_sid``\  and the function
returns zero.  Otherwise \ ``peer_sid``\  is set to SECSID_NULL and the function
returns a negative value.  A table summarizing the behavior is below:

\| function return \|      \ ``sid``\ 
------------------------------+-----------------+-----------------
no peer labels                \|        0        \|    SECSID_NULL
single peer label             \|        0        \|    <peer_label>
multiple, consistent labels   \|        0        \|    <peer_label>
multiple, inconsistent labels \|    -<errno>     \|    SECSID_NULL

.. _`security_policycap_supported`:

security_policycap_supported
============================

.. c:function:: int security_policycap_supported(struct selinux_state *state, unsigned int req_cap)

    Check for a specific policy capability

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param req_cap:
        capability
    :type req_cap: unsigned int

.. _`security_policycap_supported.description`:

Description
-----------

This function queries the currently loaded policy to see if it supports the
capability specified by \ ``req_cap``\ .  Returns true (1) if the capability is
supported, false (0) if it isn't supported.

.. _`security_netlbl_cache_add`:

security_netlbl_cache_add
=========================

.. c:function:: void security_netlbl_cache_add(struct netlbl_lsm_secattr *secattr, u32 sid)

    Add an entry to the NetLabel cache

    :param secattr:
        the NetLabel packet security attributes
    :type secattr: struct netlbl_lsm_secattr \*

    :param sid:
        the SELinux SID
    :type sid: u32

.. _`security_netlbl_cache_add.description`:

Description
-----------

Attempt to cache the context in \ ``ctx``\ , which was derived from the packet in
\ ``skb``\ , in the NetLabel subsystem cache.  This function assumes \ ``secattr``\  has
already been initialized.

.. _`security_netlbl_secattr_to_sid`:

security_netlbl_secattr_to_sid
==============================

.. c:function:: int security_netlbl_secattr_to_sid(struct selinux_state *state, struct netlbl_lsm_secattr *secattr, u32 *sid)

    Convert a NetLabel secattr to a SELinux SID

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param secattr:
        the NetLabel packet security attributes
    :type secattr: struct netlbl_lsm_secattr \*

    :param sid:
        the SELinux SID
    :type sid: u32 \*

.. _`security_netlbl_secattr_to_sid.description`:

Description
-----------

Convert the given NetLabel security attributes in \ ``secattr``\  into a
SELinux SID.  If the \ ``secattr``\  field does not contain a full SELinux
SID/context then use SECINITSID_NETMSG as the foundation.  If possible the
'cache' field of \ ``secattr``\  is set and the CACHE flag is set; this is to
allow the \ ``secattr``\  to be used by NetLabel to cache the secattr to SID
conversion for future lookups.  Returns zero on success, negative values on
failure.

.. _`security_netlbl_sid_to_secattr`:

security_netlbl_sid_to_secattr
==============================

.. c:function:: int security_netlbl_sid_to_secattr(struct selinux_state *state, u32 sid, struct netlbl_lsm_secattr *secattr)

    Convert a SELinux SID to a NetLabel secattr

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param sid:
        the SELinux SID
    :type sid: u32

    :param secattr:
        the NetLabel packet security attributes
    :type secattr: struct netlbl_lsm_secattr \*

.. _`security_netlbl_sid_to_secattr.description`:

Description
-----------

Convert the given SELinux SID in \ ``sid``\  into a NetLabel security attribute.
Returns zero on success, negative values on failure.

.. _`security_read_policy`:

security_read_policy
====================

.. c:function:: int security_read_policy(struct selinux_state *state, void **data, size_t *len)

    read the policy.

    :param state:
        *undescribed*
    :type state: struct selinux_state \*

    :param data:
        binary policy data
    :type data: void \*\*

    :param len:
        length of data in bytes
    :type len: size_t \*

.. This file was automatic generated / don't edit.

