.. -*- coding: utf-8; mode: rst -*-

=========================
Actions and configuration
=========================

Each wireless device and each virtual interface offer a set of
configuration operations and other actions that are invoked by
userspace. Each of these actions is described in the operations
structure, and the parameters these operations use are described
separately.

Additionally, some operations are asynchronous and expect to get status
information via some functions that drivers need to call.

Scanning and BSS list handling with its associated functionality is
described in a separate chapter.


.. toctree::
    :maxdepth: 1

    API-struct-cfg80211-ops
    API-struct-vif-params
    API-struct-key-params
    API-enum-survey-info-flags
    API-struct-survey-info
    API-struct-cfg80211-beacon-data
    API-struct-cfg80211-ap-settings
    API-struct-station-parameters
    API-enum-rate-info-flags
    API-struct-rate-info
    API-struct-station-info
    API-enum-monitor-flags
    API-enum-mpath-info-flags
    API-struct-mpath-info
    API-struct-bss-parameters
    API-struct-ieee80211-txq-params
    API-struct-cfg80211-crypto-settings
    API-struct-cfg80211-auth-request
    API-struct-cfg80211-assoc-request
    API-struct-cfg80211-deauth-request
    API-struct-cfg80211-disassoc-request
    API-struct-cfg80211-ibss-params
    API-struct-cfg80211-connect-params
    API-struct-cfg80211-pmksa
    API-cfg80211-rx-mlme-mgmt
    API-cfg80211-auth-timeout
    API-cfg80211-rx-assoc-resp
    API-cfg80211-assoc-timeout
    API-cfg80211-tx-mlme-mgmt
    API-cfg80211-ibss-joined
    API-cfg80211-connect-result
    API-cfg80211-roamed
    API-cfg80211-disconnected
    API-cfg80211-ready-on-channel
    API-cfg80211-remain-on-channel-expired
    API-cfg80211-new-sta
    API-cfg80211-rx-mgmt
    API-cfg80211-mgmt-tx-status
    API-cfg80211-cqm-rssi-notify
    API-cfg80211-cqm-pktloss-notify
    API-cfg80211-michael-mic-failure




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
