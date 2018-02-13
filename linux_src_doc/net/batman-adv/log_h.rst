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

.. _`_batadv_dbg`:

\_batadv_dbg
============

.. c:function::  _batadv_dbg( type,  bat_priv,  ratelimited,  fmt,  arg...)

    Store debug output with(out) ratelimiting

    :param  type:
        type of debug message

    :param  bat_priv:
        the bat priv with all the soft interface information

    :param  ratelimited:
        whether output should be rate limited

    :param  fmt:
        format string

.. _`batadv_dbg`:

batadv_dbg
==========

.. c:function::  batadv_dbg( type,  bat_priv,  arg...)

    Store debug output without ratelimiting

    :param  type:
        type of debug message

    :param  bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_dbg_ratelimited`:

batadv_dbg_ratelimited
======================

.. c:function::  batadv_dbg_ratelimited( type,  bat_priv,  arg...)

    Store debug output with ratelimiting

    :param  type:
        type of debug message

    :param  bat_priv:
        the bat priv with all the soft interface information

.. _`batadv_info`:

batadv_info
===========

.. c:function::  batadv_info( net_dev,  fmt,  arg...)

    Store message in debug buffer and print it to kmsg buffer

    :param  net_dev:
        the soft interface net device

    :param  fmt:
        format string

.. _`batadv_err`:

batadv_err
==========

.. c:function::  batadv_err( net_dev,  fmt,  arg...)

    Store error in debug buffer and print it to kmsg buffer

    :param  net_dev:
        the soft interface net device

    :param  fmt:
        format string

.. This file was automatic generated / don't edit.

