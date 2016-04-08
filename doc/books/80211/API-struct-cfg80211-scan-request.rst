
.. _API-struct-cfg80211-scan-request:

============================
struct cfg80211_scan_request
============================

*man struct cfg80211_scan_request(9)*

*4.6.0-rc1*

scan request description


Synopsis
========

.. code-block:: c

    struct cfg80211_scan_request {
      struct cfg80211_ssid * ssids;
      int n_ssids;
      u32 n_channels;
      enum nl80211_bss_scan_width scan_width;
      const u8 * ie;
      size_t ie_len;
      u32 flags;
      u32 rates[IEEE80211_NUM_BANDS];
      struct wireless_dev * wdev;
      u8 mac_addr[ETH_ALEN];
      u8 mac_addr_mask[ETH_ALEN];
      struct wiphy * wiphy;
      unsigned long scan_start;
      bool aborted;
      bool notified;
      bool no_cck;
      struct ieee80211_channel * channels[0];
    };


Members
=======

ssids
    SSIDs to scan for (active scan only)

n_ssids
    number of SSIDs

n_channels
    total number of channels to scan

scan_width
    channel width for scanning

ie
    optional information element(s) to add into Probe Request or ``NULL``

ie_len
    length of ie in octets

flags
    bit field of flags controlling operation

rates[IEEE80211_NUM_BANDS]
    bitmap of rates to advertise for each band

wdev
    the wireless device to scan for

mac_addr[ETH_ALEN]
    MAC address used with randomisation

mac_addr_mask[ETH_ALEN]
    MAC address mask used with randomisation, bits that are 0 in the mask should be randomised, bits that are 1 should be taken from the ``mac_addr``

wiphy
    the wiphy this was for

scan_start
    time (in jiffies) when the scan started

aborted
    (internal) scan request was notified as aborted

notified
    (internal) scan request was notified as done or aborted

no_cck
    used to send probe requests at non CCK rate in 2GHz band

channels[0]
    channels to scan on.
