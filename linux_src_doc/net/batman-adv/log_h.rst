.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/log.h

.. _`batadv_dbg_level`:

enum batadv_dbg_level
=====================

.. c:type:: enum batadv_dbg_level

    available log levels

.. _`batadv_dbg_level.definition`:

Definition
----------

.. code-block:: c

    enum batadv_dbg_level {
        BATADV_DBG_BATMAN,
        BATADV_DBG_ROUTES,
        BATADV_DBG_TT,
        BATADV_DBG_BLA,
        BATADV_DBG_DAT,
        BATADV_DBG_NC,
        BATADV_DBG_MCAST,
        BATADV_DBG_TP_METER,
        BATADV_DBG_ALL
    };

.. _`batadv_dbg_level.constants`:

Constants
---------

BATADV_DBG_BATMAN
    OGM and TQ computations related messages

BATADV_DBG_ROUTES
    route added / changed / deleted

BATADV_DBG_TT
    translation table messages

BATADV_DBG_BLA
    bridge loop avoidance messages

BATADV_DBG_DAT
    ARP snooping and DAT related messages

BATADV_DBG_NC
    network coding related messages

BATADV_DBG_MCAST
    multicast related messages

BATADV_DBG_TP_METER
    throughput meter messages

BATADV_DBG_ALL
    the union of all the above log levels

.. This file was automatic generated / don't edit.

