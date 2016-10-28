.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/main.h

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

BATADV_DBG_ALL
    the union of all the above log levels

.. _`batadv_compare_eth`:

batadv_compare_eth
==================

.. c:function:: bool batadv_compare_eth(const void *data1, const void *data2)

    Compare two not u16 aligned Ethernet addresses

    :param const void \*data1:
        Pointer to a six-byte array containing the Ethernet address

    :param const void \*data2:
        Pointer other six-byte array containing the Ethernet address

.. _`batadv_compare_eth.note`:

note
----

can't use \ :c:func:`ether_addr_equal`\  as it requires aligned memory

.. _`batadv_compare_eth.return`:

Return
------

true if they are the same ethernet addr

.. _`batadv_has_timed_out`:

batadv_has_timed_out
====================

.. c:function:: bool batadv_has_timed_out(unsigned long timestamp, unsigned int timeout)

    compares current time (jiffies) and timestamp + timeout

    :param unsigned long timestamp:
        base value to compare with (in jiffies)

    :param unsigned int timeout:
        added to base value before comparing (in milliseconds)

.. _`batadv_has_timed_out.return`:

Return
------

true if current time is after timestamp + timeout

.. _`batadv_sum_counter`:

batadv_sum_counter
==================

.. c:function:: u64 batadv_sum_counter(struct batadv_priv *bat_priv, size_t idx)

    Sum the cpu-local counters for index 'idx'

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param size_t idx:
        index of counter to sum up

.. _`batadv_sum_counter.return`:

Return
------

sum of all cpu-local counters

.. This file was automatic generated / don't edit.

