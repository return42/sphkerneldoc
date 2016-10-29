.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/broadcom/brcm80211/brcmfmac/fwil_types.h

.. _`brcmf_tdls_iovar_le`:

struct brcmf_tdls_iovar_le
==========================

.. c:type:: struct brcmf_tdls_iovar_le

    common structure for tdls iovars.

.. _`brcmf_tdls_iovar_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_tdls_iovar_le {
        u8 ea[ETH_ALEN];
        u8 mode;
        __le16 chanspec;
        __le32 pad;
    }

.. _`brcmf_tdls_iovar_le.members`:

Members
-------

ea
    ether address of peer station.

mode
    mode value depending on specific tdls iovar.

chanspec
    channel specification.

pad
    unused (for future use).

.. _`brcmf_join_pref_params`:

struct brcmf_join_pref_params
=============================

.. c:type:: struct brcmf_join_pref_params

    parameters for preferred join selection.

.. _`brcmf_join_pref_params.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_join_pref_params {
        u8 type;
        u8 len;
        u8 rssi_gain;
        u8 band;
    }

.. _`brcmf_join_pref_params.members`:

Members
-------

type
    preference type (see enum brcmf_join_pref_types).

len
    length of bytes following (currently always 2).

rssi_gain
    signal gain for selection (only when \ ``type``\  is RSSI_DELTA).

band
    band to which selection preference applies.
    This is used if \ ``type``\  is BAND or RSSI_DELTA.

.. _`brcmf_fil_wowl_pattern_le`:

struct brcmf_fil_wowl_pattern_le
================================

.. c:type:: struct brcmf_fil_wowl_pattern_le

    wowl pattern configuration struct.

.. _`brcmf_fil_wowl_pattern_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_fil_wowl_pattern_le {
        u8 cmd[4];
        __le32 masksize;
        __le32 offset;
        __le32 patternoffset;
        __le32 patternsize;
        __le32 id;
        __le32 reasonsize;
        __le32 type;
    }

.. _`brcmf_fil_wowl_pattern_le.members`:

Members
-------

cmd
    "add", "del" or "clr".

masksize
    Size of the mask in #of bytes

offset
    Pattern byte offset in packet

patternoffset
    Offset of start of pattern. Starting from field masksize.

patternsize
    Size of the pattern itself in #of bytes

id
    id

reasonsize
    Size of the wakeup reason code

type
    Type of pattern (enum brcmf_wowl_pattern_type)

.. _`brcmf_fil_country_le`:

struct brcmf_fil_country_le
===========================

.. c:type:: struct brcmf_fil_country_le

    country configuration structure.

.. _`brcmf_fil_country_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_fil_country_le {
        char country_abbrev[BRCMF_COUNTRY_BUF_SZ];
        __le32 rev;
        char ccode[BRCMF_COUNTRY_BUF_SZ];
    }

.. _`brcmf_fil_country_le.members`:

Members
-------

country_abbrev
    null-terminated country code used in the country IE.

rev
    revision specifier for ccode. on set, -1 indicates unspecified.

ccode
    null-terminated built-in country code.

.. _`brcmf_rev_info_le`:

struct brcmf_rev_info_le
========================

.. c:type:: struct brcmf_rev_info_le

    device revision info.

.. _`brcmf_rev_info_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_rev_info_le {
        __le32 vendorid;
        __le32 deviceid;
        __le32 radiorev;
        __le32 chiprev;
        __le32 corerev;
        __le32 boardid;
        __le32 boardvendor;
        __le32 boardrev;
        __le32 driverrev;
        __le32 ucoderev;
        __le32 bus;
        __le32 chipnum;
        __le32 phytype;
        __le32 phyrev;
        __le32 anarev;
        __le32 chippkg;
        __le32 nvramrev;
    }

.. _`brcmf_rev_info_le.members`:

Members
-------

vendorid
    PCI vendor id.

deviceid
    device id of chip.

radiorev
    radio revision.

chiprev
    chip revision.

corerev
    core revision.

boardid
    board identifier (usu. PCI sub-device id).

boardvendor
    board vendor (usu. PCI sub-vendor id).

boardrev
    board revision.

driverrev
    driver version.

ucoderev
    microcode version.

bus
    bus type.

chipnum
    chip number.

phytype
    phy type.

phyrev
    phy revision.

anarev
    anacore rev.

chippkg
    chip package info.

nvramrev
    nvram revision number.

.. _`brcmf_assoclist_le`:

struct brcmf_assoclist_le
=========================

.. c:type:: struct brcmf_assoclist_le

    request assoc list.

.. _`brcmf_assoclist_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_assoclist_le {
        __le32 count;
        u8 mac[BRCMF_MAX_ASSOCLIST][ETH_ALEN];
    }

.. _`brcmf_assoclist_le.members`:

Members
-------

count
    indicates number of stations.

mac
    MAC addresses of stations.

.. _`brcmf_wowl_wakeind_le`:

struct brcmf_wowl_wakeind_le
============================

.. c:type:: struct brcmf_wowl_wakeind_le

    Wakeup indicators

.. _`brcmf_wowl_wakeind_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_wowl_wakeind_le {
        __le32 pci_wakeind;
        __le32 ucode_wakeind;
    }

.. _`brcmf_wowl_wakeind_le.members`:

Members
-------

pci_wakeind
    Whether PCI PMECSR PMEStatus bit was set.

ucode_wakeind
    What wakeup-event indication was set by ucode

.. _`brcmf_wowl_wakeind_le.note`:

Note
----

note both fields contain same information.

.. _`brcmf_pmksa`:

struct brcmf_pmksa
==================

.. c:type:: struct brcmf_pmksa

    PMK Security Association

.. _`brcmf_pmksa.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_pmksa {
        u8 bssid[ETH_ALEN];
        u8 pmkid[WLAN_PMKID_LEN];
    }

.. _`brcmf_pmksa.members`:

Members
-------

bssid
    The AP's BSSID.

pmkid
    he PMK material itself.

.. _`brcmf_pmk_list_le`:

struct brcmf_pmk_list_le
========================

.. c:type:: struct brcmf_pmk_list_le

    List of pmksa's.

.. _`brcmf_pmk_list_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_pmk_list_le {
        __le32 npmk;
        struct brcmf_pmksa pmk[BRCMF_MAXPMKID];
    }

.. _`brcmf_pmk_list_le.members`:

Members
-------

npmk
    Number of pmksa's.

pmk
    PMK SA information.

.. _`brcmf_pno_param_le`:

struct brcmf_pno_param_le
=========================

.. c:type:: struct brcmf_pno_param_le

    PNO scan configuration parameters

.. _`brcmf_pno_param_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_pno_param_le {
        __le32 version;
        __le32 scan_freq;
        __le32 lost_network_timeout;
        __le16 flags;
        __le16 rssi_margin;
        u8 bestn;
        u8 mscan;
        u8 repeat;
        u8 exp;
        __le32 slow_freq;
    }

.. _`brcmf_pno_param_le.members`:

Members
-------

version
    PNO parameters version.

scan_freq
    scan frequency.

lost_network_timeout
    #sec. to declare discovered network as lost.

flags
    Bit field to control features of PFN such as sort criteria auto
    enable switch and background scan.

rssi_margin
    Margin to avoid jitter for choosing a PFN based on RSSI sort
    criteria.

bestn
    number of best networks in each scan.

mscan
    number of scans recorded.

repeat
    minimum number of scan intervals before scan frequency changes
    in adaptive scan.

exp
    exponent of 2 for maximum scan interval.

slow_freq
    slow scan period.

.. _`brcmf_pno_net_param_le`:

struct brcmf_pno_net_param_le
=============================

.. c:type:: struct brcmf_pno_net_param_le

    scan parameters per preferred network.

.. _`brcmf_pno_net_param_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_pno_net_param_le {
        struct brcmf_ssid_le ssid;
        __le32 flags;
        __le32 infra;
        __le32 auth;
        __le32 wpa_auth;
        __le32 wsec;
    }

.. _`brcmf_pno_net_param_le.members`:

Members
-------

ssid
    ssid name and its length.

flags
    bit2: hidden.

infra
    BSS vs IBSS.

auth
    Open vs Closed.

wpa_auth
    WPA type.

wsec
    wsec value.

.. _`brcmf_pno_net_info_le`:

struct brcmf_pno_net_info_le
============================

.. c:type:: struct brcmf_pno_net_info_le

    information per found network.

.. _`brcmf_pno_net_info_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_pno_net_info_le {
        u8 bssid[ETH_ALEN];
        u8 channel;
        u8 SSID_len;
        u8 SSID[32];
        __le16 RSSI;
        __le16 timestamp;
    }

.. _`brcmf_pno_net_info_le.members`:

Members
-------

bssid
    BSS network identifier.

channel
    channel number only.

SSID_len
    length of ssid.

SSID
    ssid characters.

RSSI
    receive signal strength (in dBm).

timestamp
    age in seconds.

.. _`brcmf_pno_scanresults_le`:

struct brcmf_pno_scanresults_le
===============================

.. c:type:: struct brcmf_pno_scanresults_le

    result returned in PNO NET FOUND event.

.. _`brcmf_pno_scanresults_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_pno_scanresults_le {
        __le32 version;
        __le32 status;
        __le32 count;
    }

.. _`brcmf_pno_scanresults_le.members`:

Members
-------

version
    PNO version identifier.

status
    indicates completion status of PNO scan.

count
    amount of brcmf_pno_net_info_le entries appended.

.. _`brcmf_pno_macaddr_le`:

struct brcmf_pno_macaddr_le
===========================

.. c:type:: struct brcmf_pno_macaddr_le

    to configure PNO macaddr randomization.

.. _`brcmf_pno_macaddr_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_pno_macaddr_le {
        u8 version;
        u8 flags;
        u8 mac[ETH_ALEN];
    }

.. _`brcmf_pno_macaddr_le.members`:

Members
-------

version
    PNO version identifier.

flags
    Flags defining how mac addrss should be used.

mac
    MAC address.

.. _`brcmf_pktcnt_le`:

struct brcmf_pktcnt_le
======================

.. c:type:: struct brcmf_pktcnt_le

    packet counters.

.. _`brcmf_pktcnt_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_pktcnt_le {
        __le32 rx_good_pkt;
        __le32 rx_bad_pkt;
        __le32 tx_good_pkt;
        __le32 tx_bad_pkt;
        __le32 rx_ocast_good_pkt;
    }

.. _`brcmf_pktcnt_le.members`:

Members
-------

rx_good_pkt
    packets (MSDUs & MMPDUs) received from this station

rx_bad_pkt
    failed rx packets

tx_good_pkt
    packets (MSDUs & MMPDUs) transmitted to this station

tx_bad_pkt
    failed tx packets

rx_ocast_good_pkt
    unicast packets destined for others

.. _`brcmf_gtk_keyinfo_le`:

struct brcmf_gtk_keyinfo_le
===========================

.. c:type:: struct brcmf_gtk_keyinfo_le

    GTP rekey data

.. _`brcmf_gtk_keyinfo_le.definition`:

Definition
----------

.. code-block:: c

    struct brcmf_gtk_keyinfo_le {
        u8 kck[BRCMF_RSN_KCK_LENGTH];
        u8 kek[BRCMF_RSN_KEK_LENGTH];
        u8 replay_counter[BRCMF_RSN_REPLAY_LEN];
    }

.. _`brcmf_gtk_keyinfo_le.members`:

Members
-------

kck
    key confirmation key.

kek
    key encryption key.

replay_counter
    replay counter.

.. This file was automatic generated / don't edit.
