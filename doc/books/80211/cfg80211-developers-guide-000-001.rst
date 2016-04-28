.. -*- coding: utf-8; mode: rst -*-

===================
Device registration
===================

In order for a driver to use cfg80211, it must register the hardware
device with cfg80211. This happens through a number of hardware
capability structs described below.

The fundamental structure for each device is the 'wiphy', of which each
instance describes a physical wireless device connected to the system.
Each such wiphy can have zero, one, or many virtual interfaces
associated with it, which need to be identified as such by pointing the
network interface's ``ieee80211_ptr`` pointer to a
``struct wireless_dev`` which further describes the wireless part of the
interface, normally this struct is embedded in the network interface's
private data area. Drivers can optionally allow creating or destroying
virtual interfaces on the fly, but without at least one or the ability
to create some the wireless device isn't useful.

Each wiphy structure contains device capability information, and also
has a pointer to the various operations the driver offers. The
definitions and structures here describe these capabilities in detail.


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




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
