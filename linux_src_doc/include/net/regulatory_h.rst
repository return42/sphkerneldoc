.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/regulatory.h

.. _`environment_cap`:

enum environment_cap
====================

.. c:type:: enum environment_cap

    Environment parsed from country IE

.. _`environment_cap.definition`:

Definition
----------

.. code-block:: c

    enum environment_cap {
        ENVIRON_ANY,
        ENVIRON_INDOOR,
        ENVIRON_OUTDOOR
    };

.. _`environment_cap.constants`:

Constants
---------

ENVIRON_ANY
    indicates country IE applies to both indoor and
    outdoor operation.

ENVIRON_INDOOR
    indicates country IE applies only to indoor operation

ENVIRON_OUTDOOR
    indicates country IE applies only to outdoor operation

.. _`regulatory_request`:

struct regulatory_request
=========================

.. c:type:: struct regulatory_request

    used to keep track of regulatory requests

.. _`regulatory_request.definition`:

Definition
----------

.. code-block:: c

    struct regulatory_request {
        struct rcu_head rcu_head;
        int wiphy_idx;
        enum nl80211_reg_initiator initiator;
        enum nl80211_user_reg_hint_type user_reg_hint_type;
        char alpha2[2];
        enum nl80211_dfs_regions dfs_region;
        bool intersect;
        bool processed;
        enum environment_cap country_ie_env;
        struct list_head list;
    }

.. _`regulatory_request.members`:

Members
-------

rcu_head
    RCU head struct used to free the request

wiphy_idx
    this is set if this request's initiator is
    \ ``REGDOM_SET_BY_COUNTRY_IE``\  or \ ``REGDOM_SET_BY_DRIVER``\ . This
    can be used by the wireless core to deal with conflicts
    and potentially inform users of which devices specifically
    cased the conflicts.

initiator
    indicates who sent this request, could be any of
    of those set in nl80211_reg_initiator (%NL80211_REGDOM_SET_BY\_\*)

user_reg_hint_type
    if the \ ``initiator``\  was of type
    \ ``NL80211_REGDOM_SET_BY_USER``\ , this classifies the type
    of hint passed. This could be any of the \ ``NL80211_USER_REG_HINT``\ \_\*
    types.

alpha2
    the ISO / IEC 3166 alpha2 country code of the requested
    regulatory domain. We have a few special codes:
    00 - World regulatory domain
    99 - built by driver but a specific alpha2 cannot be determined
    98 - result of an intersection between two regulatory domains
    97 - regulatory domain has not yet been configured

dfs_region
    If CRDA responded with a regulatory domain that requires
    DFS master operation on a known DFS region (NL80211_DFS\_\*),
    dfs_region represents that region. Drivers can use this and the
    \ ``alpha2``\  to adjust their device's DFS parameters as required.

intersect
    indicates whether the wireless core should intersect
    the requested regulatory domain with the presently set regulatory
    domain.

processed
    indicates whether or not this requests has already been
    processed. When the last request is processed it means that the
    currently regulatory domain set on cfg80211 is updated from
    CRDA and can be used by other regulatory requests. When a
    the last request is not yet processed we must yield until it
    is processed before processing any new requests.

country_ie_env
    lets us know if the AP is telling us we are outdoor,
    indoor, or if it doesn't matter

list
    used to insert into the reg_requests_list linked list

.. _`ieee80211_regulatory_flags`:

enum ieee80211_regulatory_flags
===============================

.. c:type:: enum ieee80211_regulatory_flags

    device regulatory flags

.. _`ieee80211_regulatory_flags.definition`:

Definition
----------

.. code-block:: c

    enum ieee80211_regulatory_flags {
        REGULATORY_CUSTOM_REG,
        REGULATORY_STRICT_REG,
        REGULATORY_DISABLE_BEACON_HINTS,
        REGULATORY_COUNTRY_IE_FOLLOW_POWER,
        REGULATORY_COUNTRY_IE_IGNORE,
        REGULATORY_ENABLE_RELAX_NO_IR,
        REGULATORY_IGNORE_STALE_KICKOFF,
        REGULATORY_WIPHY_SELF_MANAGED
    };

.. _`ieee80211_regulatory_flags.constants`:

Constants
---------

REGULATORY_CUSTOM_REG
    tells us the driver for this device
    has its own custom regulatory domain and cannot identify the
    ISO / IEC 3166 alpha2 it belongs to. When this is enabled
    we will disregard the first regulatory hint (when the
    initiator is \ ``REGDOM_SET_BY_CORE``\ ). Drivers that use
    \ :c:func:`wiphy_apply_custom_regulatory`\  should have this flag set
    or the regulatory core will set it for the wiphy.
    If you use \ :c:func:`regulatory_hint`\  \*after\* using
    \ :c:func:`wiphy_apply_custom_regulatory`\  the wireless core will
    clear the REGULATORY_CUSTOM_REG for your wiphy as it would be
    implied that the device somehow gained knowledge of its region.

REGULATORY_STRICT_REG
    tells us that the wiphy for this device
    has regulatory domain that it wishes to be considered as the
    superset for regulatory rules. After this device gets its regulatory
    domain programmed further regulatory hints shall only be considered
    for this device to enhance regulatory compliance, forcing the
    device to only possibly use subsets of the original regulatory
    rules. For example if channel 13 and 14 are disabled by this
    device's regulatory domain no user specified regulatory hint which
    has these channels enabled would enable them for this wiphy,
    the device's original regulatory domain will be trusted as the
    base. You can program the superset of regulatory rules for this
    wiphy with \ :c:func:`regulatory_hint`\  for cards programmed with an
    ISO3166-alpha2 country code. wiphys that use \ :c:func:`regulatory_hint`\ 
    will have their wiphy->regd programmed once the regulatory
    domain is set, and all other regulatory hints will be ignored
    until their own regulatory domain gets programmed.

REGULATORY_DISABLE_BEACON_HINTS
    enable this if your driver needs to
    ensure that passive scan flags and beaconing flags may not be lifted by
    cfg80211 due to regulatory beacon hints. For more information on beacon
    hints read the documenation for \ :c:func:`regulatory_hint_found_beacon`\ 

REGULATORY_COUNTRY_IE_FOLLOW_POWER
    for devices that have a preference
    that even though they may have programmed their own custom power
    setting prior to wiphy registration, they want to ensure their channel
    power settings are updated for this connection with the power settings
    derived from the regulatory domain. The regulatory domain used will be
    based on the ISO3166-alpha2 from country IE provided through
    \ :c:func:`regulatory_hint_country_ie`\ 

REGULATORY_COUNTRY_IE_IGNORE
    for devices that have a preference to ignore
    all country IE information processed by the regulatory core. This will
    override \ ``REGULATORY_COUNTRY_IE_FOLLOW_POWER``\  as all country IEs will
    be ignored.

REGULATORY_ENABLE_RELAX_NO_IR
    for devices that wish to allow the
    NO_IR relaxation, which enables transmissions on channels on which
    otherwise initiating radiation is not allowed. This will enable the
    relaxations enabled under the CFG80211_REG_RELAX_NO_IR configuration
    option

REGULATORY_IGNORE_STALE_KICKOFF
    the regulatory core will \_not\_ make sure
    all interfaces on this wiphy reside on allowed channels. If this flag
    is not set, upon a regdomain change, the interfaces are given a grace
    period (currently 60 seconds) to disconnect or move to an allowed
    channel. Interfaces on forbidden channels are forcibly disconnected.

REGULATORY_WIPHY_SELF_MANAGED
    for devices that employ wiphy-specific
    regdom management. These devices will ignore all regdom changes not
    originating from their own wiphy.
    A self-managed wiphys only employs regulatory information obtained from
    the FW and driver and does not use other cfg80211 sources like
    beacon-hints, country-code IEs and hints from other devices on the same
    system. Conversely, a self-managed wiphy does not share its regulatory
    hints with other devices in the system. If a system contains several
    devices, one or more of which are self-managed, there might be
    contradictory regulatory settings between them. Usage of flag is
    generally discouraged. Only use it if the FW/driver is incompatible
    with non-locally originated hints.

.. _`ieee80211_regulatory_flags.currently-these-types-of-interfaces-are-supported-for-enforcement`:

Currently these types of interfaces are supported for enforcement
-----------------------------------------------------------------

NL80211_IFTYPE_ADHOC, NL80211_IFTYPE_STATION, NL80211_IFTYPE_AP,
NL80211_IFTYPE_AP_VLAN, NL80211_IFTYPE_MONITOR,
NL80211_IFTYPE_P2P_CLIENT, NL80211_IFTYPE_P2P_GO,
NL80211_IFTYPE_P2P_DEVICE. The flag will be set by default if a device
includes any modes unsupported for enforcement checking.

.. _`ieee80211_regulatory_flags.this-flag-is-incompatible-with-the-flags`:

This flag is incompatible with the flags
----------------------------------------

%REGULATORY_CUSTOM_REG,
\ ``REGULATORY_STRICT_REG``\ , \ ``REGULATORY_COUNTRY_IE_FOLLOW_POWER``\ ,
\ ``REGULATORY_COUNTRY_IE_IGNORE``\  and \ ``REGULATORY_DISABLE_BEACON_HINTS``\ .
Mixing any of the above flags with this flag will result in a failure
to register the wiphy. This flag implies
\ ``REGULATORY_DISABLE_BEACON_HINTS``\  and \ ``REGULATORY_COUNTRY_IE_IGNORE``\ .

.. This file was automatic generated / don't edit.

