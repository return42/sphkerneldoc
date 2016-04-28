.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-ieee80211-vif:

====================
struct ieee80211_vif
====================

*man struct ieee80211_vif(9)*

*4.6.0-rc5*

per-interface data


Synopsis
========

.. code-block:: c

    struct ieee80211_vif {
      enum nl80211_iftype type;
      struct ieee80211_bss_conf bss_conf;
      u8 addr[ETH_ALEN];
      bool p2p;
      bool csa_active;
      bool mu_mimo_owner;
      u8 cab_queue;
      u8 hw_queue[IEEE80211_NUM_ACS];
      struct ieee80211_txq * txq;
      struct ieee80211_chanctx_conf __rcu * chanctx_conf;
      u32 driver_flags;
    #ifdef CONFIG_MAC80211_DEBUGFS
      struct dentry * debugfs_dir;
    #endif
      unsigned int probe_req_reg;
      u8 drv_priv[0];
    };


Members
=======

type
    type of this virtual interface

bss_conf
    BSS configuration for this interface, either our own or the BSS
    we're associated to

addr[ETH_ALEN]
    address of this interface

p2p
    indicates whether this AP or STA interface is a p2p interface, i.e.
    a GO or p2p-sta respectively

csa_active
    marks whether a channel switch is going on. Internally it is
    write-protected by sdata_lock and local->mtx so holding either is
    fine for read access.

mu_mimo_owner
    indicates interface owns MU-MIMO capability

cab_queue
    content-after-beacon (DTIM beacon really) queue, AP mode only

hw_queue[IEEE80211_NUM_ACS]
    hardware queue for each AC

txq
    the multicast data TX queue (if driver uses the TXQ abstraction)

chanctx_conf
    The channel context this interface is assigned to, or ``NULL`` when
    it is not assigned. This pointer is RCU-protected due to the TX path
    needing to access it; even though the netdev carrier will always be
    off when it is ``NULL`` there can still be races and packets could
    be processed after it switches back to ``NULL``.

driver_flags
    flags/capabilities the driver has for this interface, these need to
    be set (or cleared) when the interface is added or, if supported by
    the driver, the interface type is changed at runtime, mac80211 will
    never touch this field

debugfs_dir
    debugfs dentry, can be used by drivers to create own per interface
    debug files. Note that it will be NULL for the virtual monitor
    interface (if that is requested.)

probe_req_reg
    probe requests should be reported to mac80211 for this interface.

drv_priv[0]
    data area for driver use, will always be aligned to sizeof(void *).


Description
===========

Data in this structure is continually present for driver use during the
life of a virtual interface.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
