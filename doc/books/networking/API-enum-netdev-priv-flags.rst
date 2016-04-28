.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-netdev-priv-flags:

======================
enum netdev_priv_flags
======================

*man enum netdev_priv_flags(9)*

*4.6.0-rc5*

``struct net_device`` priv_flags


Synopsis
========

.. code-block:: c

    enum netdev_priv_flags {
      IFF_802_1Q_VLAN,
      IFF_EBRIDGE,
      IFF_BONDING,
      IFF_ISATAP,
      IFF_WAN_HDLC,
      IFF_XMIT_DST_RELEASE,
      IFF_DONT_BRIDGE,
      IFF_DISABLE_NETPOLL,
      IFF_MACVLAN_PORT,
      IFF_BRIDGE_PORT,
      IFF_OVS_DATAPATH,
      IFF_TX_SKB_SHARING,
      IFF_UNICAST_FLT,
      IFF_TEAM_PORT,
      IFF_SUPP_NOFCS,
      IFF_LIVE_ADDR_CHANGE,
      IFF_MACVLAN,
      IFF_XMIT_DST_RELEASE_PERM,
      IFF_IPVLAN_MASTER,
      IFF_IPVLAN_SLAVE,
      IFF_L3MDEV_MASTER,
      IFF_NO_QUEUE,
      IFF_OPENVSWITCH,
      IFF_L3MDEV_SLAVE,
      IFF_TEAM,
      IFF_RXFH_CONFIGURED,
      IFF_PHONY_HEADROOM,
      IFF_MACSEC
    };


Constants
=========

IFF_802_1Q_VLAN
    802.1Q VLAN device

IFF_EBRIDGE
    Ethernet bridging device

IFF_BONDING
    bonding master or slave

IFF_ISATAP
    ISATAP interface (RFC4214)

IFF_WAN_HDLC
    WAN HDLC device

IFF_XMIT_DST_RELEASE
    ``dev_hard_start_xmit`` is allowed to release skb->dst

IFF_DONT_BRIDGE
    disallow bridging this ether dev

IFF_DISABLE_NETPOLL
    disable netpoll at run-time

IFF_MACVLAN_PORT
    device used as macvlan port

IFF_BRIDGE_PORT
    device used as bridge port

IFF_OVS_DATAPATH
    device used as Open vSwitch datapath port

IFF_TX_SKB_SHARING
    The interface supports sharing skbs on transmit

IFF_UNICAST_FLT
    Supports unicast filtering

IFF_TEAM_PORT
    device used as team port

IFF_SUPP_NOFCS
    device supports sending custom FCS

IFF_LIVE_ADDR_CHANGE
    device supports hardware address change when it's running

IFF_MACVLAN
    Macvlan device

IFF_XMIT_DST_RELEASE_PERM
    IFF_XMIT_DST_RELEASE not taking into account underlying stacked
    devices

IFF_IPVLAN_MASTER
    IPvlan master device

IFF_IPVLAN_SLAVE
    IPvlan slave device

IFF_L3MDEV_MASTER
    device is an L3 master device

IFF_NO_QUEUE
    device can run without qdisc attached

IFF_OPENVSWITCH
    device is a Open vSwitch master

IFF_L3MDEV_SLAVE
    device is enslaved to an L3 master device

IFF_TEAM
    device is a team device

IFF_RXFH_CONFIGURED
    device has had Rx Flow indirection table configured

IFF_PHONY_HEADROOM
    the headroom value is controlled by an external entity (i.e. the
    master device for bridged veth)

IFF_MACSEC
    device is a MACsec device


Description
===========

These are the ``struct net_device``, they are only set internally by
drivers and used in the kernel. These flags are invisible to userspace;
this means that the order of these flags can change during any kernel
release.

You should have a pretty good reason to be extending these flags.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
