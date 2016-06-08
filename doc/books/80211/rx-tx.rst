.. -*- coding: utf-8; mode: rst -*-

.. _rx-tx:

*******************************
Receive and transmit processing
*******************************


what should be here
===================

TBD

This should describe the receive and transmit paths in mac80211/the
drivers as well as transmit status handling.


Frame format
============


.. kernel-doc:: include/net/mac80211.h
    :doc: Frame format

Packet alignment
================


.. kernel-doc:: net/mac80211/rx.c
    :doc: Packet alignment

Calling into mac80211 from interrupts
=====================================


.. kernel-doc:: include/net/mac80211.h
    :doc: Calling mac80211 from interrupts

functions/definitions
=====================


.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_rx_status

.. kernel-doc:: include/net/mac80211.h
    :functions: mac80211_rx_flags

.. kernel-doc:: include/net/mac80211.h
    :functions: mac80211_tx_info_flags

.. kernel-doc:: include/net/mac80211.h
    :functions: mac80211_tx_control_flags

.. kernel-doc:: include/net/mac80211.h
    :functions: mac80211_rate_control_flags

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_tx_rate

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_tx_info

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_tx_info_clear_status

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_rx

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_rx_ni

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_rx_irqsafe

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_tx_status

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_tx_status_ni

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_tx_status_irqsafe

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_rts_get

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_rts_duration

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_ctstoself_get

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_ctstoself_duration

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_generic_frame_duration

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_wake_queue

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_stop_queue

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_wake_queues

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_stop_queues

.. kernel-doc:: include/net/mac80211.h
    :functions: ieee80211_queue_stopped



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
