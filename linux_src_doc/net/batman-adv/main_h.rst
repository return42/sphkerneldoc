.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/main.h

.. _`batadv_tp_max_num`:

BATADV_TP_MAX_NUM
=================

.. c:function::  BATADV_TP_MAX_NUM()

    maximum number of simultaneously active tp sessions

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

.. This file was automatic generated / don't edit.

