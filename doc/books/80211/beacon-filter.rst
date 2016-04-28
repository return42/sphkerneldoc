.. -*- coding: utf-8; mode: rst -*-

.. _beacon-filter:

=====================
Beacon filter support
=====================

Some hardware have beacon filter support to reduce host cpu wakeups
which will reduce system power consumption. It usually works so that the
firmware creates a checksum of the beacon but omits all constantly
changing elements (TSF, TIM etc). Whenever the checksum changes the
beacon is forwarded to the host, otherwise it will be just dropped. That
way the host will only receive beacons where some relevant information
(for example ERP protection or WMM settings) have changed.

Beacon filter support is advertised with the
``IEEE80211_VIF_BEACON_FILTER`` interface capability. The driver needs
to enable beacon filter support whenever power save is enabled, that is
``IEEE80211_CONF_PS`` is set. When power save is enabled, the stack will
not check for beacon loss and the driver needs to notify about loss of
beacons with ``ieee80211_beacon_loss``.

The time (or number of beacons missed) until the firmware notifies the
driver of a beacon loss event (which in turn causes the driver to call
``ieee80211_beacon_loss``) should be configurable and will be controlled
by mac80211 and the roaming algorithm in the future.

Since there may be constantly changing information elements that nothing
in the software stack cares about, we will, in the future, have mac80211
tell the driver which information elements are interesting in the sense
that we want to see changes in them. This will include - a list of
information element IDs - a list of OUIs for the vendor information
element

Ideally, the hardware would filter out any beacons without changes in
the requested elements, but if it cannot support that it may, at the
expense of some efficiency, filter out only a subset. For example, if
the device doesn't support checking for OUIs it should pass up all
changes in all vendor information elements.

Note that change, for the sake of simplification, also includes
information elements appearing or disappearing from the beacon.

Some hardware supports an “ignore list” instead, just make sure nothing
that was requested is on the ignore list, and include commonly changing
information element IDs in the ignore list, for example 11 (BSS load)
and the various vendor-assigned IEs with unknown contents (128, 129,
133-136, 149, 150, 155, 156, 173, 176, 178, 179, 219); for forward
compatibility it could also include some currently unused IDs.

In addition to these capabilities, hardware should support notifying the
host of changes in the beacon RSSI. This is relevant to implement
roaming when no traffic is flowing (when traffic is flowing we see the
RSSI of the received data packets). This can consist in notifying the
host when the RSSI changes significantly or when it drops below or rises
above configurable thresholds. In the future these thresholds will also
be configured by mac80211 (which gets them from userspace) to implement
them as the roaming algorithm requires.

If the hardware cannot implement this, the driver should ask it to
periodically pass beacon frames to the host so that software can do the
signal strength threshold checking.


.. toctree::
    :maxdepth: 1

    API-ieee80211-beacon-loss




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
