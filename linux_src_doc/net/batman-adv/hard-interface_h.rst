.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/hard-interface.h

.. _`batadv_hard_if_cleanup`:

enum batadv_hard_if_cleanup
===========================

.. c:type:: enum batadv_hard_if_cleanup

    Cleanup modi for soft_iface after slave removal

.. _`batadv_hard_if_cleanup.definition`:

Definition
----------

.. code-block:: c

    enum batadv_hard_if_cleanup {
        BATADV_IF_CLEANUP_KEEP,
        BATADV_IF_CLEANUP_AUTO
    };

.. _`batadv_hard_if_cleanup.constants`:

Constants
---------

BATADV_IF_CLEANUP_KEEP
    Don't automatically delete soft-interface

BATADV_IF_CLEANUP_AUTO
    Delete soft-interface after last slave was removed

.. _`batadv_hardif_put`:

batadv_hardif_put
=================

.. c:function:: void batadv_hardif_put(struct batadv_hard_iface *hard_iface)

    decrement the hard interface refcounter and possibly release it

    :param struct batadv_hard_iface \*hard_iface:
        the hard interface to free

.. This file was automatic generated / don't edit.

