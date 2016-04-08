
.. _API-enum-wiphy-flags:

================
enum wiphy_flags
================

*man enum wiphy_flags(9)*

*4.6.0-rc1*

wiphy capability flags


Synopsis
========

.. code-block:: c

    enum wiphy_flags {
      WIPHY_FLAG_NETNS_OK,
      WIPHY_FLAG_PS_ON_BY_DEFAULT,
      WIPHY_FLAG_4ADDR_AP,
      WIPHY_FLAG_4ADDR_STATION,
      WIPHY_FLAG_CONTROL_PORT_PROTOCOL,
      WIPHY_FLAG_IBSS_RSN,
      WIPHY_FLAG_MESH_AUTH,
      WIPHY_FLAG_SUPPORTS_SCHED_SCAN,
      WIPHY_FLAG_SUPPORTS_FW_ROAM,
      WIPHY_FLAG_AP_UAPSD,
      WIPHY_FLAG_SUPPORTS_TDLS,
      WIPHY_FLAG_TDLS_EXTERNAL_SETUP,
      WIPHY_FLAG_HAVE_AP_SME,
      WIPHY_FLAG_REPORTS_OBSS,
      WIPHY_FLAG_AP_PROBE_RESP_OFFLOAD,
      WIPHY_FLAG_OFFCHAN_TX,
      WIPHY_FLAG_HAS_REMAIN_ON_CHANNEL,
      WIPHY_FLAG_SUPPORTS_5_10_MHZ,
      WIPHY_FLAG_HAS_CHANNEL_SWITCH
    };


Constants
=========

WIPHY_FLAG_NETNS_OK
    if not set, do not allow changing the netns of this wiphy at all

WIPHY_FLAG_PS_ON_BY_DEFAULT
    if set to true, powersave will be enabled by default -- this flag will be set depending on the kernel's default on ``wiphy_new``, but can be changed by the driver if it has a
    good reason to override the default

WIPHY_FLAG_4ADDR_AP
    supports 4addr mode even on AP (with a single station on a VLAN interface)

WIPHY_FLAG_4ADDR_STATION
    supports 4addr mode even as a station

WIPHY_FLAG_CONTROL_PORT_PROTOCOL
    This device supports setting the control port protocol ethertype. The device also honours the control_port_no_encrypt flag.

WIPHY_FLAG_IBSS_RSN
    The device supports IBSS RSN.

WIPHY_FLAG_MESH_AUTH
    The device supports mesh authentication by routing auth frames to userspace. See ``NL80211_MESH_SETUP_USERSPACE_AUTH``.

WIPHY_FLAG_SUPPORTS_SCHED_SCAN
    The device supports scheduled scans.

WIPHY_FLAG_SUPPORTS_FW_ROAM
    The device supports roaming feature in the firmware.

WIPHY_FLAG_AP_UAPSD
    The device supports uapsd on AP.

WIPHY_FLAG_SUPPORTS_TDLS
    The device supports TDLS (802.11z) operation.

WIPHY_FLAG_TDLS_EXTERNAL_SETUP
    The device does not handle TDLS (802.11z) link setup/discovery operations internally. Setup, discovery and teardown packets should be sent through the ``NL80211_CMD_TDLS_MGMT``
    command. When this flag is not set, ``NL80211_CMD_TDLS_OPER`` should be used for asking the driver/firmware to perform a TDLS operation.

WIPHY_FLAG_HAVE_AP_SME
    device integrates AP SME

WIPHY_FLAG_REPORTS_OBSS
    the device will report beacons from other BSSes when there are virtual interfaces in AP mode by calling ``cfg80211_report_obss_beacon``.

WIPHY_FLAG_AP_PROBE_RESP_OFFLOAD
    When operating as an AP, the device responds to probe-requests in hardware.

WIPHY_FLAG_OFFCHAN_TX
    Device supports direct off-channel TX.

WIPHY_FLAG_HAS_REMAIN_ON_CHANNEL
    Device supports remain-on-channel call.

WIPHY_FLAG_SUPPORTS_5_10_MHZ
    Device supports 5 MHz and 10 MHz channels.

WIPHY_FLAG_HAS_CHANNEL_SWITCH
    Device supports channel switch in beaconing mode (AP, IBSS, Mesh, ...).
