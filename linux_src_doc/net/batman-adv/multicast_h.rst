.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/multicast.h

.. _`batadv_forw_mode`:

enum batadv_forw_mode
=====================

.. c:type:: enum batadv_forw_mode

    the way a packet should be forwarded as

.. _`batadv_forw_mode.definition`:

Definition
----------

.. code-block:: c

    enum batadv_forw_mode {
        BATADV_FORW_ALL,
        BATADV_FORW_SINGLE,
        BATADV_FORW_NONE
    };

.. _`batadv_forw_mode.constants`:

Constants
---------

BATADV_FORW_ALL
    forward the packet to all nodes (currently via classic flooding)

BATADV_FORW_SINGLE
    forward the packet to a single node (currently via the BATMAN unicast routing protocol)

BATADV_FORW_NONE
    don't forward, drop it

.. This file was automatic generated / don't edit.

