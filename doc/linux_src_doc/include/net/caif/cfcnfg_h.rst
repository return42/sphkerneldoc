.. -*- coding: utf-8; mode: rst -*-

========
cfcnfg.h
========


.. _`cfcnfg_phy_preference`:

enum cfcnfg_phy_preference
==========================

.. c:type:: cfcnfg_phy_preference

    Physical preference HW Abstraction


.. _`cfcnfg_phy_preference.definition`:

Definition
----------

.. code-block:: c

    enum cfcnfg_phy_preference {
      CFPHYPREF_UNSPECIFIED,
      CFPHYPREF_LOW_LAT,
      CFPHYPREF_HIGH_BW,
      CFPHYPREF_LOOP
    };


.. _`cfcnfg_phy_preference.constants`:

Constants
---------

:``CFPHYPREF_UNSPECIFIED``:
    Default physical interface

:``CFPHYPREF_LOW_LAT``:
    Default physical interface for low-latency
    traffic

:``CFPHYPREF_HIGH_BW``:
    Default physical interface for high-bandwidth
    traffic

:``CFPHYPREF_LOOP``:
    TEST only Loopback interface simulating modem
    responses.


.. _`get_cfcnfg`:

get_cfcnfg
==========

.. c:function:: struct cfcnfg *get_cfcnfg (struct net *net)

    Get the CAIF configuration object given network.

    :param struct net \*net:
        Network for the CAIF configuration object.



.. _`cfcnfg_create`:

cfcnfg_create
=============

.. c:function:: struct cfcnfg *cfcnfg_create ( void)

    Create the CAIF configuration object.

    :param void:
        no arguments



.. _`cfcnfg_remove`:

cfcnfg_remove
=============

.. c:function:: void cfcnfg_remove (struct cfcnfg *cfg)

    Remove the CFCNFG object

    :param struct cfcnfg \*cfg:
        config object



.. _`cfcnfg_add_phy_layer`:

cfcnfg_add_phy_layer
====================

.. c:function:: void cfcnfg_add_phy_layer (struct cfcnfg *cnfg, struct net_device *dev, struct cflayer *phy_layer, enum cfcnfg_phy_preference pref, struct cflayer *link_support, bool fcs, int head_room)

    Adds a physical layer to the CAIF stack.

    :param struct cfcnfg \*cnfg:
        Pointer to a CAIF configuration object, created by
        :c:func:`cfcnfg_create`.

    :param struct net_device \*dev:
        Pointer to link layer device

    :param struct cflayer \*phy_layer:
        Specify the physical layer. The transmit function
        MUST be set in the structure.

    :param enum cfcnfg_phy_preference pref:
        The phy (link layer) preference.

    :param struct cflayer \*link_support:
        Protocol implementation for link layer specific protocol.

    :param bool fcs:
        Specify if checksum is used in CAIF Framing Layer.

    :param int head_room:
        Head space needed by link specific protocol.



.. _`cfcnfg_del_phy_layer`:

cfcnfg_del_phy_layer
====================

.. c:function:: int cfcnfg_del_phy_layer (struct cfcnfg *cnfg, struct cflayer *phy_layer)

    Deletes an phy layer from the CAIF stack.

    :param struct cfcnfg \*cnfg:
        Pointer to a CAIF configuration object, created by
        :c:func:`cfcnfg_create`.

    :param struct cflayer \*phy_layer:
        Adaptation layer to be removed.



.. _`cfcnfg_set_phy_state`:

cfcnfg_set_phy_state
====================

.. c:function:: int cfcnfg_set_phy_state (struct cfcnfg *cnfg, struct cflayer *phy_layer, bool up)

    Set the state of the physical interface device.

    :param struct cfcnfg \*cnfg:
        Configuration object

    :param struct cflayer \*phy_layer:
        Physical Layer representation

    :param bool up:
        State of device

