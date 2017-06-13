.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/bridge_loop_avoidance.h

.. _`batadv_bla_is_loopdetect_mac`:

batadv_bla_is_loopdetect_mac
============================

.. c:function:: bool batadv_bla_is_loopdetect_mac(const uint8_t *mac)

    check if the mac address is from a loop detect frame sent by bridge loop avoidance

    :param const uint8_t \*mac:
        mac address to check

.. _`batadv_bla_is_loopdetect_mac.return`:

Return
------

true if the it looks like a loop detect frame
(mac starts with BA:BE), false otherwise

.. This file was automatic generated / don't edit.

