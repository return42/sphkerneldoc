.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-bss-parameters:

=====================
struct bss_parameters
=====================

*man struct bss_parameters(9)*

*4.6.0-rc5*

BSS parameters


Synopsis
========

.. code-block:: c

    struct bss_parameters {
      int use_cts_prot;
      int use_short_preamble;
      int use_short_slot_time;
      const u8 * basic_rates;
      u8 basic_rates_len;
      int ap_isolate;
      int ht_opmode;
      s8 p2p_ctwindow;
      s8 p2p_opp_ps;
    };


Members
=======

use_cts_prot
    Whether to use CTS protection (0 = no, 1 = yes, -1 = do not change)

use_short_preamble
    Whether the use of short preambles is allowed (0 = no, 1 = yes, -1 =
    do not change)

use_short_slot_time
    Whether the use of short slot time is allowed (0 = no, 1 = yes, -1 =
    do not change)

basic_rates
    basic rates in IEEE 802.11 format (or NULL for no change)

basic_rates_len
    number of basic rates

ap_isolate
    do not forward packets between connected stations

ht_opmode
    HT Operation mode (u16 = opmode, -1 = do not change)

p2p_ctwindow
    P2P CT Window (-1 = no change)

p2p_opp_ps
    P2P opportunistic PS (-1 = no change)


Description
===========

Used to change BSS parameters (mainly for AP mode).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
