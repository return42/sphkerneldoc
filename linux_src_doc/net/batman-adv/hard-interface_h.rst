.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/hard-interface.h

.. _`batadv_hard_if_state`:

enum batadv_hard_if_state
=========================

.. c:type:: enum batadv_hard_if_state

    State of a hard interface

.. _`batadv_hard_if_state.definition`:

Definition
----------

.. code-block:: c

    enum batadv_hard_if_state {
        BATADV_IF_NOT_IN_USE,
        BATADV_IF_TO_BE_REMOVED,
        BATADV_IF_INACTIVE,
        BATADV_IF_ACTIVE,
        BATADV_IF_TO_BE_ACTIVATED,
        BATADV_IF_I_WANT_YOU
    };

.. _`batadv_hard_if_state.constants`:

Constants
---------

BATADV_IF_NOT_IN_USE
    interface is not used as slave interface of abatman-adv soft interface

BATADV_IF_TO_BE_REMOVED
    interface will be removed from softinterface

BATADV_IF_INACTIVE
    interface is deactivated

BATADV_IF_ACTIVE
    interface is used

BATADV_IF_TO_BE_ACTIVATED
    interface is getting activated

BATADV_IF_I_WANT_YOU
    interface is queued up (using sysfs) for beingadded as slave interface of a batman-adv soft interface

.. _`batadv_hard_if_bcast`:

enum batadv_hard_if_bcast
=========================

.. c:type:: enum batadv_hard_if_bcast

    broadcast avoidance options

.. _`batadv_hard_if_bcast.definition`:

Definition
----------

.. code-block:: c

    enum batadv_hard_if_bcast {
        BATADV_HARDIF_BCAST_OK,
        BATADV_HARDIF_BCAST_NORECIPIENT,
        BATADV_HARDIF_BCAST_DUPFWD,
        BATADV_HARDIF_BCAST_DUPORIG
    };

.. _`batadv_hard_if_bcast.constants`:

Constants
---------

BATADV_HARDIF_BCAST_OK
    Do broadcast on according hard interface

BATADV_HARDIF_BCAST_NORECIPIENT
    Broadcast not needed, there is no recipient

BATADV_HARDIF_BCAST_DUPFWD
    There is just the neighbor we got it from

BATADV_HARDIF_BCAST_DUPORIG
    There is just the originator

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

    :param hard_iface:
        the hard interface to free
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_primary_if_get_selected`:

batadv_primary_if_get_selected
==============================

.. c:function:: struct batadv_hard_iface *batadv_primary_if_get_selected(struct batadv_priv *bat_priv)

    Get reference to primary interface

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

.. _`batadv_primary_if_get_selected.return`:

Return
------

primary interface (with increased refcnt), otherwise NULL

.. This file was automatic generated / don't edit.

