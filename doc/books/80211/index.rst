
**Explaining wireless 802.11 networking in the Linux kernel**

**Copyright** 2007-2009 : Johannes Berg

:author:    Berg Johannes
:address:   johannes@sipsolutions.net

This documentation is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 as published by the Free Software
Foundation.

This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this documentation; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330,
Boston, MA 02111-1307 USA

For more details see the file COPYING in the source distribution of Linux.

    These books attempt to give a description of the various subsystems that play a role in 802.11 wireless networking in Linux. Since these books are for kernel developers they
    attempts to document the structures and functions used in the kernel as well as giving a higher-level overview.

    The reader is expected to be familiar with the 802.11 standard as published by the IEEE in 802.11-2007 (or possibly later versions). References to this standard will be given
    as "802.11-2007 8.1.5".


++++++++++++++++++++++
The cfg80211 subsystem
++++++++++++++++++++++
    cfg80211 is the configuration API for 802.11 devices in Linux. It bridges userspace and drivers, and offers some utility functionality associated with 802.11. cfg80211 must,
    directly or indirectly via mac80211, be used by all modern wireless drivers in Linux, so that they offer a consistent API through nl80211. For backward compatibility, cfg80211
    also offers wireless extensions to userspace, but hides them from drivers completely.

    Additionally, cfg80211 contains code to help enforce regulatory spectrum use restrictions.


===================
Device registration
===================

In order for a driver to use cfg80211, it must register the hardware device with cfg80211. This happens through a number of hardware capability structs described below.

The fundamental structure for each device is the 'wiphy', of which each instance describes a physical wireless device connected to the system. Each such wiphy can have zero, one,
or many virtual interfaces associated with it, which need to be identified as such by pointing the network interface's ``ieee80211_ptr`` pointer to a ``struct wireless_dev`` which
further describes the wireless part of the interface, normally this struct is embedded in the network interface's private data area. Drivers can optionally allow creating or
destroying virtual interfaces on the fly, but without at least one or the ability to create some the wireless device isn't useful.

Each wiphy structure contains device capability information, and also has a pointer to the various operations the driver offers. The definitions and structures here describe these
capabilities in detail.


.. toctree::
    :maxdepth: 1

    API-enum-ieee80211-band
    API-enum-ieee80211-channel-flags
    API-struct-ieee80211-channel
    API-enum-ieee80211-rate-flags
    API-struct-ieee80211-rate
    API-struct-ieee80211-sta-ht-cap
    API-struct-ieee80211-supported-band
    API-enum-cfg80211-signal-type
    API-enum-wiphy-params-flags
    API-enum-wiphy-flags
    API-struct-wiphy
    API-struct-wireless-dev
    API-wiphy-new
    API-wiphy-register
    API-wiphy-unregister
    API-wiphy-free
    API-wiphy-name
    API-wiphy-dev
    API-wiphy-priv
    API-priv-to-wiphy
    API-set-wiphy-dev
    API-wdev-priv
    API-struct-ieee80211-iface-limit
    API-struct-ieee80211-iface-combination
    API-cfg80211-check-combinations

=========================
Actions and configuration
=========================

Each wireless device and each virtual interface offer a set of configuration operations and other actions that are invoked by userspace. Each of these actions is described in the
operations structure, and the parameters these operations use are described separately.

Additionally, some operations are asynchronous and expect to get status information via some functions that drivers need to call.

Scanning and BSS list handling with its associated functionality is described in a separate chapter.


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

==============================
Scanning and BSS list handling
==============================

The scanning process itself is fairly simple, but cfg80211 offers quite a bit of helper functionality. To start a scan, the scan operation will be invoked with a scan definition.
This scan definition contains the channels to scan, and the SSIDs to send probe requests for (including the wildcard, if desired). A passive scan is indicated by having no SSIDs to
probe. Additionally, a scan request may contain extra information elements that should be added to the probe request. The IEs are guaranteed to be well-formed, and will not exceed
the maximum length the driver advertised in the wiphy structure.

When scanning finds a BSS, cfg80211 needs to be notified of that, because it is responsible for maintaining the BSS list; the driver should not maintain a list itself. For this
notification, various functions exist.

Since drivers do not maintain a BSS list, there are also a number of functions to search for a BSS and obtain information about it from the BSS structure cfg80211 maintains. The
BSS list is also made available to userspace.


.. toctree::
    :maxdepth: 1

    API-struct-cfg80211-ssid
    API-struct-cfg80211-scan-request
    API-cfg80211-scan-done
    API-struct-cfg80211-bss
    API-struct-cfg80211-inform-bss
    API-cfg80211-inform-bss-frame-data
    API-cfg80211-inform-bss-data
    API-cfg80211-unlink-bss
    API-cfg80211-find-ie
    API-ieee80211-bss-get-ie

=================
Utility functions
=================

cfg80211 offers a number of utility functions that can be useful.


.. toctree::
    :maxdepth: 1

    API-ieee80211-channel-to-frequency
    API-ieee80211-frequency-to-channel
    API-ieee80211-get-channel
    API-ieee80211-get-response-rate
    API-ieee80211-hdrlen
    API-ieee80211-get-hdrlen-from-skb
    API-struct-ieee80211-radiotap-iterator

=================
Data path helpers
=================

In addition to generic utilities, cfg80211 also offers functions that help implement the data path for devices that do not do the 802.11/802.3 conversion on the device.


.. toctree::
    :maxdepth: 1

    API-ieee80211-data-to-8023
    API-ieee80211-data-from-8023
    API-ieee80211-amsdu-to-8023s
    API-cfg80211-classify8021d

=====================================
Regulatory enforcement infrastructure
=====================================

TODO


.. toctree::
    :maxdepth: 1

    API-regulatory-hint
    API-wiphy-apply-custom-regulatory
    API-freq-reg-info

==================
RFkill integration
==================

RFkill integration in cfg80211 is almost invisible to drivers, as cfg80211 automatically registers an rfkill instance for each wireless device it knows about. Soft kill is also
translated into disconnecting and turning all interfaces off, drivers are expected to turn off the device when all interfaces are down.

However, devices may have a hard RFkill line, in which case they also need to interact with the rfkill subsystem, via cfg80211. They can do this with a few helper functions
documented here.


.. toctree::
    :maxdepth: 1

    API-wiphy-rfkill-set-hw-state
    API-wiphy-rfkill-start-polling
    API-wiphy-rfkill-stop-polling

=========
Test mode
=========

Test mode is a set of utility functions to allow drivers to interact with driver-specific tools to aid, for instance, factory programming.

This chapter describes how drivers interact with it, for more information see the nl80211 book's chapter on it.


.. toctree::
    :maxdepth: 1

    API-cfg80211-testmode-alloc-reply-skb
    API-cfg80211-testmode-reply
    API-cfg80211-testmode-alloc-event-skb
    API-cfg80211-testmode-event

++++++++++++++++++++++
The mac80211 subsystem
++++++++++++++++++++++
    mac80211 is the Linux stack for 802.11 hardware that implements only partial functionality in hard- or firmware. This document defines the interface between mac80211 and
    low-level hardware drivers.

    If you're reading this document and not the header file itself, it will be incomplete because not all documentation has been converted yet.


+++++++++++++++++++++++++++++++++++
The basic mac80211 driver interface
+++++++++++++++++++++++++++++++++++
You should read and understand the information contained within this part of the book while implementing a driver. In some chapters, advanced usage is noted, that may be skipped at
first.

This part of the book only covers station and monitor mode functionality, additional information required to implement the other modes is covered in the second part of the book.


.. _basics:

=======================
Basic hardware handling
=======================

TBD

This chapter shall contain information on getting a hw struct allocated and registered with mac80211.

Since it is required to allocate rates/modes before registering a hw struct, this chapter shall also contain information on setting up the rate/mode structs.

Additionally, some discussion about the callbacks and the general programming model should be in here, including the definition of ieee80211_ops which will be referred to a lot.

Finally, a discussion of hardware capabilities should be done with references to other parts of the book.


.. toctree::
    :maxdepth: 1

    API-struct-ieee80211-hw
    API-enum-ieee80211-hw-flags
    API-SET-IEEE80211-DEV
    API-SET-IEEE80211-PERM-ADDR
    API-struct-ieee80211-ops
    API-ieee80211-alloc-hw
    API-ieee80211-register-hw
    API-ieee80211-unregister-hw
    API-ieee80211-free-hw

.. _phy-handling:

=================
PHY configuration
=================

TBD

This chapter should describe PHY handling including start/stop callbacks and the various structures used.


.. toctree::
    :maxdepth: 1

    API-struct-ieee80211-conf
    API-enum-ieee80211-conf-flags

.. _iface-handling:

==================
Virtual interfaces
==================

TBD

This chapter should describe virtual interface basics that are relevant to the driver (VLANs, MGMT etc are not.) It should explain the use of the add_iface/remove_iface callbacks
as well as the interface configuration callbacks.

Things related to AP mode should be discussed there.

Things related to supporting multiple interfaces should be in the appropriate chapter, a BIG FAT note should be here about this though and the recommendation to allow only a single
interface in STA mode at first!


.. toctree::
    :maxdepth: 1

    API-struct-ieee80211-vif

.. _rx-tx:

===============================
Receive and transmit processing
===============================


what should be here
===================

TBD

This should describe the receive and transmit paths in mac80211/the drivers as well as transmit status handling.


Frame format
============

As a general rule, when frames are passed between mac80211 and the driver, they start with the IEEE 802.11 header and include the same octets that are sent over the air except for
the FCS which should be calculated by the hardware.

There are, however, various exceptions to this rule for advanced features:

The first exception is for hardware encryption and decryption offload where the IV/ICV may or may not be generated in hardware.

Secondly, when the hardware handles fragmentation, the frame handed to the driver from mac80211 is the MSDU, not the MPDU.


Packet alignment
================

Drivers always need to pass packets that are aligned to two-byte boundaries to the stack.

Additionally, should, if possible, align the payload data in a way that guarantees that the contained IP header is aligned to a four-byte boundary. In the case of regular frames,
this simply means aligning the payload to a four-byte boundary (because either the IP header is directly contained, or IV/RFC1042 headers that have a length divisible by four are
in front of it). If the payload data is not properly aligned and the architecture doesn't support efficient unaligned operations, mac80211 will align the data.

With A-MSDU frames, however, the payload data address must yield two modulo four because there are 14-byte 802.3 headers within the A-MSDU frames that push the IP header further
back to a multiple of four again. Thankfully, the specs were sane enough this time around to require padding each A-MSDU subframe to a length that is a multiple of four.

Padding like Atheros hardware adds which is between the 802.11 header and the payload is not supported, the driver is required to move the 802.11 header to be directly in front of
the payload in that case.


Calling into mac80211 from interrupts
=====================================

Only ``ieee80211_tx_status_irqsafe`` and ``ieee80211_rx_irqsafe`` can be called in hardware interrupt context. The low-level driver must not call any other functions in hardware
interrupt context. If there is a need for such call, the low-level driver should first ACK the interrupt and perform the IEEE 802.11 code call after this, e.g. from a scheduled
workqueue or even tasklet function.

NOTE: If the driver opts to use the ``_irqsafe`` functions, it may not also use the non-IRQ-safe functions!


functions/definitions
=====================


.. toctree::
    :maxdepth: 1

    API-struct-ieee80211-rx-status
    API-enum-mac80211-rx-flags
    API-enum-mac80211-tx-info-flags
    API-enum-mac80211-tx-control-flags
    API-enum-mac80211-rate-control-flags
    API-struct-ieee80211-tx-rate
    API-struct-ieee80211-tx-info
    API-ieee80211-tx-info-clear-status
    API-ieee80211-rx
    API-ieee80211-rx-ni
    API-ieee80211-rx-irqsafe
    API-ieee80211-tx-status
    API-ieee80211-tx-status-ni
    API-ieee80211-tx-status-irqsafe
    API-ieee80211-rts-get
    API-ieee80211-rts-duration
    API-ieee80211-ctstoself-get
    API-ieee80211-ctstoself-duration
    API-ieee80211-generic-frame-duration
    API-ieee80211-wake-queue
    API-ieee80211-stop-queue
    API-ieee80211-wake-queues
    API-ieee80211-stop-queues
    API-ieee80211-queue-stopped

.. _filters:

===============
Frame filtering
===============

mac80211 requires to see many management frames for proper operation, and users may want to see many more frames when in monitor mode. However, for best CPU usage and power
consumption, having as few frames as possible percolate through the stack is desirable. Hence, the hardware should filter as much as possible.

To achieve this, mac80211 uses filter flags (see below) to tell the driver's ``configure_filter`` function which frames should be passed to mac80211 and which should be filtered
out.

Before ``configure_filter`` is invoked, the ``prepare_multicast`` callback is invoked with the parameters ``mc_count`` and ``mc_list`` for the combined multicast address list of
all virtual interfaces. It's use is optional, and it returns a u64 that is passed to ``configure_filter``. Additionally, ``configure_filter`` has the arguments ``changed_flags``
telling which flags were changed and ``total_flags`` with the new flag states.

If your device has no multicast address filters your driver will need to check both the ``FIF_ALLMULTI`` flag and the ``mc_count`` parameter to see whether multicast frames should
be accepted or dropped.

All unsupported flags in ``total_flags`` must be cleared. Hardware does not support a flag if it is incapable of _passing_ the frame to the stack. Otherwise the driver must
ignore the flag, but not clear it. You must _only_ clear the flag (announce no support for the flag to mac80211) if you are not able to pass the packet type to the stack (so the
hardware always filters it). So for example, you should clear ``FIF_CONTROL``, if your hardware always filters control frames. If your hardware always passes control frames to the
kernel and is incapable of filtering them, you do _not_ clear the ``FIF_CONTROL`` flag. This rule applies to all other FIF flags as well.


.. toctree::
    :maxdepth: 1

    API-enum-ieee80211-filter-flags

.. _workqueue:

======================
The mac80211 workqueue
======================

mac80211 provides its own workqueue for drivers and internal mac80211 use. The workqueue is a single threaded workqueue and can only be accessed by helpers for sanity checking.
Drivers must ensure all work added onto the mac80211 workqueue should be cancelled on the driver ``stop`` callback.

mac80211 will flushed the workqueue upon interface removal and during suspend.

All work performed on the mac80211 workqueue must not acquire the RTNL lock.


.. toctree::
    :maxdepth: 1

    API-ieee80211-queue-work
    API-ieee80211-queue-delayed-work

.. _advanced:

+++++++++++++++++++++++++
Advanced driver interface
+++++++++++++++++++++++++
Information contained within this part of the book is of interest only for advanced interaction of mac80211 with drivers to exploit more hardware capabilities and improve
performance.


.. _led-support:

===========
LED support
===========

Mac80211 supports various ways of blinking LEDs. Wherever possible, device LEDs should be exposed as LED class devices and hooked up to the appropriate trigger, which will then be
triggered appropriately by mac80211.


.. toctree::
    :maxdepth: 1

    API-ieee80211-get-tx-led-name
    API-ieee80211-get-rx-led-name
    API-ieee80211-get-assoc-led-name
    API-ieee80211-get-radio-led-name
    API-struct-ieee80211-tpt-blink
    API-enum-ieee80211-tpt-led-trigger-flags
    API-ieee80211-create-tpt-led-trigger

.. _hardware-crypto-offload:

============================
Hardware crypto acceleration
============================

mac80211 is capable of taking advantage of many hardware acceleration designs for encryption and decryption operations.

The ``set_key`` callback in the ``struct ieee80211_ops`` for a given device is called to enable hardware acceleration of encryption and decryption. The callback takes a ``sta``
parameter that will be NULL for default keys or keys used for transmission only, or point to the station information for the peer for individual keys. Multiple transmission keys
with the same key index may be used when VLANs are configured for an access point.

When transmitting, the TX control data will use the ``hw_key_idx`` selected by the driver by modifying the ``struct ieee80211_key_conf`` pointed to by the ``key`` parameter to the
``set_key`` function.

The ``set_key`` call for the ``SET_KEY`` command should return 0 if the key is now in use, -``EOPNOTSUPP`` or -``ENOSPC`` if it couldn't be added; if you return 0 then hw_key_idx
must be assigned to the hardware key index, you are free to use the full u8 range.

Note that in the case that the ``IEEE80211_HW_SW_CRYPTO_CONTROL`` flag is set, mac80211 will not automatically fall back to software crypto if enabling hardware crypto failed. The
``set_key`` call may also return the value 1 to permit this specific key/algorithm to be done in software.

When the cmd is ``DISABLE_KEY`` then it must succeed.

Note that it is permissible to not decrypt a frame even if a key for it has been uploaded to hardware, the stack will not make any decision based on whether a key has been uploaded
or not but rather based on the receive flags.

The ``struct ieee80211_key_conf`` structure pointed to by the ``key`` parameter is guaranteed to be valid until another call to ``set_key`` removes it, but it can only be used as a
cookie to differentiate keys.

In TKIP some HW need to be provided a phase 1 key, for RX decryption acceleration (i.e. iwlwifi). Those drivers should provide update_tkip_key handler. The ``update_tkip_key``
call updates the driver with the new phase 1 key. This happens every time the iv16 wraps around (every 65536 packets). The ``set_key`` call will happen only once for each key
(unless the AP did rekeying), it will not include a valid phase 1 key. The valid phase 1 key is provided by update_tkip_key only. The trigger that makes mac80211 call this
handler is software decryption with wrap around of iv16.

The ``set_default_unicast_key`` call updates the default WEP key index configured to the hardware for WEP encryption type. This is required for devices that support offload of data
packets (e.g. ARP responses).


.. toctree::
    :maxdepth: 1

    API-enum-set-key-cmd
    API-struct-ieee80211-key-conf
    API-enum-ieee80211-key-flags
    API-ieee80211-get-tkip-p1k
    API-ieee80211-get-tkip-p1k-iv
    API-ieee80211-get-tkip-p2k

.. _powersave:

=================
Powersave support
=================

mac80211 has support for various powersave implementations.

First, it can support hardware that handles all powersaving by itself, such hardware should simply set the ``IEEE80211_HW_SUPPORTS_PS`` hardware flag. In that case, it will be told
about the desired powersave mode with the ``IEEE80211_CONF_PS`` flag depending on the association status. The hardware must take care of sending nullfunc frames when necessary,
i.e. when entering and leaving powersave mode. The hardware is required to look at the AID in beacons and signal to the AP that it woke up when it finds traffic directed to it.

``IEEE80211_CONF_PS`` flag enabled means that the powersave mode defined in IEEE 802.11-2007 section 11.2 is enabled. This is not to be confused with hardware wakeup and sleep
states. Driver is responsible for waking up the hardware before issuing commands to the hardware and putting it back to sleep at appropriate times.

When PS is enabled, hardware needs to wakeup for beacons and receive the buffered multicast/broadcast frames after the beacon. Also it must be possible to send frames and receive
the acknowledment frame.

Other hardware designs cannot send nullfunc frames by themselves and also need software support for parsing the TIM bitmap. This is also supported by mac80211 by combining the
``IEEE80211_HW_SUPPORTS_PS`` and ``IEEE80211_HW_PS_NULLFUNC_STACK`` flags. The hardware is of course still required to pass up beacons. The hardware is still required to handle
waking up for multicast traffic; if it cannot the driver must handle that as best as it can, mac80211 is too slow to do that.

Dynamic powersave is an extension to normal powersave in which the hardware stays awake for a user-specified period of time after sending a frame so that reply frames need not be
buffered and therefore delayed to the next wakeup. It's compromise of getting good enough latency when there's data traffic and still saving significantly power in idle periods.

Dynamic powersave is simply supported by mac80211 enabling and disabling PS based on traffic. Driver needs to only set ``IEEE80211_HW_SUPPORTS_PS`` flag and mac80211 will handle
everything automatically. Additionally, hardware having support for the dynamic PS feature may set the ``IEEE80211_HW_SUPPORTS_DYNAMIC_PS`` flag to indicate that it can support
dynamic PS mode itself. The driver needs to look at the ``dynamic_ps_timeout`` hardware configuration value and use it that value whenever ``IEEE80211_CONF_PS`` is set. In this
case mac80211 will disable dynamic PS feature in stack and will just keep ``IEEE80211_CONF_PS`` enabled whenever user has enabled powersave.

Driver informs U-APSD client support by enabling ``IEEE80211_VIF_SUPPORTS_UAPSD`` flag. The mode is configured through the uapsd parameter in ``conf_tx`` operation. Hardware needs
to send the QoS Nullfunc frames and stay awake until the service period has ended. To utilize U-APSD, dynamic powersave is disabled for voip AC and all frames from that AC are
transmitted with powersave enabled.

Note: U-APSD client mode is not yet supported with ``IEEE80211_HW_PS_NULLFUNC_STACK``.


.. _beacon-filter:

=====================
Beacon filter support
=====================

Some hardware have beacon filter support to reduce host cpu wakeups which will reduce system power consumption. It usually works so that the firmware creates a checksum of the
beacon but omits all constantly changing elements (TSF, TIM etc). Whenever the checksum changes the beacon is forwarded to the host, otherwise it will be just dropped. That way the
host will only receive beacons where some relevant information (for example ERP protection or WMM settings) have changed.

Beacon filter support is advertised with the ``IEEE80211_VIF_BEACON_FILTER`` interface capability. The driver needs to enable beacon filter support whenever power save is enabled,
that is ``IEEE80211_CONF_PS`` is set. When power save is enabled, the stack will not check for beacon loss and the driver needs to notify about loss of beacons with
``ieee80211_beacon_loss``.

The time (or number of beacons missed) until the firmware notifies the driver of a beacon loss event (which in turn causes the driver to call ``ieee80211_beacon_loss``) should be
configurable and will be controlled by mac80211 and the roaming algorithm in the future.

Since there may be constantly changing information elements that nothing in the software stack cares about, we will, in the future, have mac80211 tell the driver which information
elements are interesting in the sense that we want to see changes in them. This will include - a list of information element IDs - a list of OUIs for the vendor information element

Ideally, the hardware would filter out any beacons without changes in the requested elements, but if it cannot support that it may, at the expense of some efficiency, filter out
only a subset. For example, if the device doesn't support checking for OUIs it should pass up all changes in all vendor information elements.

Note that change, for the sake of simplification, also includes information elements appearing or disappearing from the beacon.

Some hardware supports an “ignore list” instead, just make sure nothing that was requested is on the ignore list, and include commonly changing information element IDs in the
ignore list, for example 11 (BSS load) and the various vendor-assigned IEs with unknown contents (128, 129, 133-136, 149, 150, 155, 156, 173, 176, 178, 179, 219); for forward
compatibility it could also include some currently unused IDs.

In addition to these capabilities, hardware should support notifying the host of changes in the beacon RSSI. This is relevant to implement roaming when no traffic is flowing (when
traffic is flowing we see the RSSI of the received data packets). This can consist in notifying the host when the RSSI changes significantly or when it drops below or rises above
configurable thresholds. In the future these thresholds will also be configured by mac80211 (which gets them from userspace) to implement them as the roaming algorithm requires.

If the hardware cannot implement this, the driver should ask it to periodically pass beacon frames to the host so that software can do the signal strength threshold checking.


.. toctree::
    :maxdepth: 1

    API-ieee80211-beacon-loss

.. _qos:

===============================
Multiple queues and QoS support
===============================

TBD


.. toctree::
    :maxdepth: 1

    API-struct-ieee80211-tx-queue-params

.. _AP:

=========================
Access point mode support
=========================

TBD

Some parts of the if_conf should be discussed here instead

Insert notes about VLAN interfaces with hw crypto here or in the hw crypto chapter.


.. _ps-client:

support for powersaving clients
===============================

In order to implement AP and P2P GO modes, mac80211 has support for client powersaving, both “legacy” PS (PS-Poll/null data) and uAPSD. There currently is no support for sAPSD.

There is one assumption that mac80211 makes, namely that a client will not poll with PS-Poll and trigger with uAPSD at the same time. Both are supported, and both can be used by
the same client, but they can't be used concurrently by the same client. This simplifies the driver code.

The first thing to keep in mind is that there is a flag for complete driver implementation: ``IEEE80211_HW_AP_LINK_PS``. If this flag is set, mac80211 expects the driver to handle
most of the state machine for powersaving clients and will ignore the PM bit in incoming frames. Drivers then use ``ieee80211_sta_ps_transition`` to inform mac80211 of stations'
powersave transitions. In this mode, mac80211 also doesn't handle PS-Poll/uAPSD.

In the mode without ``IEEE80211_HW_AP_LINK_PS``, mac80211 will check the PM bit in incoming frames for client powersave transitions. When a station goes to sleep, we will stop
transmitting to it. There is, however, a race condition: a station might go to sleep while there is data buffered on hardware queues. If the device has support for this it will
reject frames, and the driver should give the frames back to mac80211 with the ``IEEE80211_TX_STAT_TX_FILTERED`` flag set which will cause mac80211 to retry the frame when the
station wakes up. The driver is also notified of powersave transitions by calling its ``sta_notify`` callback.

When the station is asleep, it has three choices: it can wake up, it can PS-Poll, or it can possibly start a uAPSD service period. Waking up is implemented by simply transmitting
all buffered (and filtered) frames to the station. This is the easiest case. When the station sends a PS-Poll or a uAPSD trigger frame, mac80211 will inform the driver of this with
the ``allow_buffered_frames`` callback; this callback is optional. mac80211 will then transmit the frames as usual and set the ``IEEE80211_TX_CTL_NO_PS_BUFFER`` on each frame. The
last frame in the service period (or the only response to a PS-Poll) also has ``IEEE80211_TX_STATUS_EOSP`` set to indicate that it ends the service period; as this frame must have
TX status report it also sets ``IEEE80211_TX_CTL_REQ_TX_STATUS``. When TX status is reported for this frame, the service period is marked has having ended and a new one can be
started by the peer.

Additionally, non-bufferable MMPDUs can also be transmitted by mac80211 with the ``IEEE80211_TX_CTL_NO_PS_BUFFER`` set in them.

Another race condition can happen on some devices like iwlwifi when there are frames queued for the station and it wakes up or polls; the frames that are already queued could end
up being transmitted first instead, causing reordering and/or wrong processing of the EOSP. The cause is that allowing frames to be transmitted to a certain station is out-of-band
communication to the device. To allow this problem to be solved, the driver can call ``ieee80211_sta_block_awake`` if frames are buffered when it is notified that the station went
to sleep. When all these frames have been filtered (see above), it must call the function again to indicate that the station is no longer blocked.

If the driver buffers frames in the driver for aggregation in any way, it must use the ``ieee80211_sta_set_buffered`` call when it is notified of the station going to sleep to
inform mac80211 of any TIDs that have frames buffered. Note that when a station wakes up this information is reset (hence the requirement to call it when informed of the station
going to sleep). Then, when a service period starts for any reason, ``release_buffered_frames`` is called with the number of frames to be released and which TIDs they are to come
from. In this case, the driver is responsible for setting the EOSP (for uAPSD) and MORE_DATA bits in the released frames, to help the ``more_data`` parameter is passed to tell the
driver if there is more data on other TIDs -- the TIDs to release frames from are ignored since mac80211 doesn't know how many frames the buffers for those TIDs contain.

If the driver also implement GO mode, where absence periods may shorten service periods (or abort PS-Poll responses), it must filter those response frames except in the case of
frames that are buffered in the driver -- those must remain buffered to avoid reordering. Because it is possible that no frames are released in this case, the driver must call
``ieee80211_sta_eosp`` to indicate to mac80211 that the service period ended anyway.

Finally, if frames from multiple TIDs are released from mac80211 but the driver might reorder them, it must clear & set the flags appropriately (only the last frame may have
``IEEE80211_TX_STATUS_EOSP``) and also take care of the EOSP and MORE_DATA bits in the frame. The driver may also use ``ieee80211_sta_eosp`` in this case.

Note that if the driver ever buffers frames other than QoS-data frames, it must take care to never send a non-QoS-data frame as the last frame in a service period, adding a
QoS-nulldata frame after a non-QoS-data frame if needed.


.. toctree::
    :maxdepth: 1

    API-ieee80211-get-buffered-bc
    API-ieee80211-beacon-get
    API-ieee80211-sta-eosp
    API-enum-ieee80211-frame-release-type
    API-ieee80211-sta-ps-transition
    API-ieee80211-sta-ps-transition-ni
    API-ieee80211-sta-set-buffered
    API-ieee80211-sta-block-awake

.. _multi-iface:

======================================
Supporting multiple virtual interfaces
======================================

TBD

Note: WDS with identical MAC address should almost always be OK

Insert notes about having multiple virtual interfaces with different MAC addresses here, note which configurations are supported by mac80211, add notes about supporting hw crypto
with it.


.. toctree::
    :maxdepth: 1

    API-ieee80211-iterate-active-interfaces
    API-ieee80211-iterate-active-interfaces-atomic

.. _station-handling:

================
Station handling
================

TODO


.. toctree::
    :maxdepth: 1

    API-struct-ieee80211-sta
    API-enum-sta-notify-cmd
    API-ieee80211-find-sta
    API-ieee80211-find-sta-by-ifaddr

.. _hardware-scan-offload:

=====================
Hardware scan offload
=====================

TBD


.. toctree::
    :maxdepth: 1

    API-ieee80211-scan-completed

.. _aggregation:

===========
Aggregation
===========


TX A-MPDU aggregation
=====================

Aggregation on the TX side requires setting the hardware flag ``IEEE80211_HW_AMPDU_AGGREGATION``. The driver will then be handed packets with a flag indicating A-MPDU aggregation.
The driver or device is responsible for actually aggregating the frames, as well as deciding how many and which to aggregate.

When TX aggregation is started by some subsystem (usually the rate control algorithm would be appropriate) by calling the ``ieee80211_start_tx_ba_session`` function, the driver
will be notified via its ``ampdu_action`` function, with the ``IEEE80211_AMPDU_TX_START`` action.

In response to that, the driver is later required to call the ``ieee80211_start_tx_ba_cb_irqsafe`` function, which will really start the aggregation session after the peer has also
responded. If the peer responds negatively, the session will be stopped again right away. Note that it is possible for the aggregation session to be stopped before the driver has
indicated that it is done setting it up, in which case it must not indicate the setup completion.

Also note that, since we also need to wait for a response from the peer, the driver is notified of the completion of the handshake by the ``IEEE80211_AMPDU_TX_OPERATIONAL`` action
to the ``ampdu_action`` callback.

Similarly, when the aggregation session is stopped by the peer or something calling ``ieee80211_stop_tx_ba_session``, the driver's ``ampdu_action`` function will be called with the
action ``IEEE80211_AMPDU_TX_STOP``. In this case, the call must not fail, and the driver must later call ``ieee80211_stop_tx_ba_cb_irqsafe``. Note that the sta can get destroyed
before the BA tear down is complete.


RX A-MPDU aggregation
=====================

Aggregation on the RX side requires only implementing the ``ampdu_action`` callback that is invoked to start/stop any block-ack sessions for RX aggregation.

When RX aggregation is started by the peer, the driver is notified via ``ampdu_action`` function, with the ``IEEE80211_AMPDU_RX_START`` action, and may reject the request in which
case a negative response is sent to the peer, if it accepts it a positive response is sent.

While the session is active, the device/driver are required to de-aggregate frames and pass them up one by one to mac80211, which will handle the reorder buffer.

When the aggregation session is stopped again by the peer or ourselves, the driver's ``ampdu_action`` function will be called with the action ``IEEE80211_AMPDU_RX_STOP``. In this
case, the call must not fail.


.. toctree::
    :maxdepth: 1

    API-enum-ieee80211-ampdu-mlme-action

.. _smps:

=====================================
Spatial Multiplexing Powersave (SMPS)
=====================================

SMPS (Spatial multiplexing power save) is a mechanism to conserve power in an 802.11n implementation. For details on the mechanism and rationale, please refer to 802.11 (as amended
by 802.11n-2009) “11.2.3 SM power save”.

The mac80211 implementation is capable of sending action frames to update the AP about the station's SMPS mode, and will instruct the driver to enter the specific mode. It will
also announce the requested SMPS mode during the association handshake. Hardware support for this feature is required, and can be indicated by hardware flags.

The default mode will be “automatic”, which nl80211/cfg80211 defines to be dynamic SMPS in (regular) powersave, and SMPS turned off otherwise.

To support this feature, the driver must set the appropriate hardware support flags, and handle the SMPS flag to the ``config`` operation. It will then with this mechanism be
instructed to enter the requested SMPS mode while associated to an HT AP.


.. toctree::
    :maxdepth: 1

    API-ieee80211-request-smps
    API-enum-ieee80211-smps-mode

.. _rate-control:

++++++++++++++++++++++
Rate control interface
++++++++++++++++++++++
TBD

This part of the book describes the rate control algorithm interface and how it relates to mac80211 and drivers.


.. _ratecontrol-api:

================
Rate Control API
================

TBD


.. toctree::
    :maxdepth: 1

    API-ieee80211-start-tx-ba-session
    API-ieee80211-start-tx-ba-cb-irqsafe
    API-ieee80211-stop-tx-ba-session
    API-ieee80211-stop-tx-ba-cb-irqsafe
    API-enum-ieee80211-rate-control-changed
    API-struct-ieee80211-tx-rate-control
    API-rate-control-send-low

.. _internal:

+++++++++
Internals
+++++++++
TBD

This part of the book describes mac80211 internals.


.. _key-handling:

============
Key handling
============


Key handling basics
===================

Key handling in mac80211 is done based on per-interface (sub_if_data) keys and per-station keys. Since each station belongs to an interface, each station key also belongs to that
interface.

Hardware acceleration is done on a best-effort basis for algorithms that are implemented in software, for each key the hardware is asked to enable that key for offloading but if it
cannot do that the key is simply kept for software encryption (unless it is for an algorithm that isn't implemented in software). There is currently no way of knowing whether a key
is handled in SW or HW except by looking into debugfs.

All key management is internally protected by a mutex. Within all other parts of mac80211, key references are, just as STA structure references, protected by RCU. Note, however,
that some things are unprotected, namely the key->sta dereferences within the hardware acceleration functions. This means that ``sta_info_destroy`` must remove the key which waits
for an RCU grace period.


MORE TBD
========

TBD


.. _rx-processing:

==================
Receive processing
==================

TBD


.. _tx-processing:

===================
Transmit processing
===================

TBD


.. _sta-info:

=====================
Station info handling
=====================


Programming information
=======================


.. toctree::
    :maxdepth: 1

    API-struct-sta-info
    API-enum-ieee80211-sta-info-flags

STA information lifetime rules
==============================

STA info structures (``struct sta_info``) are managed in a hash table for faster lookup and a list for iteration. They are managed using RCU, i.e. access to the list and hash table
is protected by RCU.

Upon allocating a STA info structure with ``sta_info_alloc``, the caller owns that structure. It must then insert it into the hash table using either ``sta_info_insert`` or
``sta_info_insert_rcu``; only in the latter case (which acquires an rcu read section but must not be called from within one) will the pointer still be valid after the call. Note
that the caller may not do much with the STA info before inserting it, in particular, it may not start any mesh peer link management or add encryption keys.

When the insertion fails (``sta_info_insert``) returns non-zero), the structure will have been freed by ``sta_info_insert``!

Station entries are added by mac80211 when you establish a link with a peer. This means different things for the different type of interfaces we support. For a regular station this
mean we add the AP sta when we receive an association response from the AP. For IBSS this occurs when get to know about a peer on the same IBSS. For WDS we add the sta for the peer
immediately upon device open. When using AP mode we add stations for each respective station upon request from userspace through nl80211.

In order to remove a STA info structure, various sta_info_destroy_⋆() calls are available.

There is no concept of ownership on a STA entry, each structure is owned by the global hash table/list until it is removed. All users of the structure need to be RCU protected so
that the structure won't be freed before they are done using it.


.. _aggregation-internals:

===========
Aggregation
===========


.. toctree::
    :maxdepth: 1

    API-struct-sta-ampdu-mlme
    API-struct-tid-ampdu-tx
    API-struct-tid-ampdu-rx

.. _synchronisation:

===============
Synchronisation
===============

TBD

Locking, lots of RCU
