.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/sfp-bus.c

.. _`sfp_bus`:

struct sfp_bus
==============

.. c:type:: struct sfp_bus

    internal representation of a sfp bus

.. _`sfp_bus.definition`:

Definition
----------

.. code-block:: c

    struct sfp_bus {
    }

.. _`sfp_bus.members`:

Members
-------

void
    no arguments

.. _`sfp_parse_port`:

sfp_parse_port
==============

.. c:function:: int sfp_parse_port(struct sfp_bus *bus, const struct sfp_eeprom_id *id, unsigned long *support)

    Parse the EEPROM base ID, setting the port type

    :param bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module
    :type bus: struct sfp_bus \*

    :param id:
        a pointer to the module's \ :c:type:`struct sfp_eeprom_id <sfp_eeprom_id>`\ 
    :type id: const struct sfp_eeprom_id \*

    :param support:
        optional pointer to an array of unsigned long for the
        ethtool support mask
    :type support: unsigned long \*

.. _`sfp_parse_port.description`:

Description
-----------

Parse the EEPROM identification given in \ ``id``\ , and return one of
\ ``PORT_TP``\ , \ ``PORT_FIBRE``\  or \ ``PORT_OTHER``\ . If \ ``support``\  is non-%NULL,
also set the ethtool \ ``ETHTOOL_LINK_MODE_xxx_BIT``\  corresponding with
the connector type.

If the port type is not known, returns \ ``PORT_OTHER``\ .

.. _`sfp_parse_support`:

sfp_parse_support
=================

.. c:function:: void sfp_parse_support(struct sfp_bus *bus, const struct sfp_eeprom_id *id, unsigned long *support)

    Parse the eeprom id for supported link modes

    :param bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module
    :type bus: struct sfp_bus \*

    :param id:
        a pointer to the module's \ :c:type:`struct sfp_eeprom_id <sfp_eeprom_id>`\ 
    :type id: const struct sfp_eeprom_id \*

    :param support:
        pointer to an array of unsigned long for the ethtool support mask
    :type support: unsigned long \*

.. _`sfp_parse_support.description`:

Description
-----------

Parse the EEPROM identification information and derive the supported
ethtool link modes for the module.

.. _`sfp_select_interface`:

sfp_select_interface
====================

.. c:function:: phy_interface_t sfp_select_interface(struct sfp_bus *bus, const struct sfp_eeprom_id *id, unsigned long *link_modes)

    Select appropriate phy_interface_t mode

    :param bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module
    :type bus: struct sfp_bus \*

    :param id:
        a pointer to the module's \ :c:type:`struct sfp_eeprom_id <sfp_eeprom_id>`\ 
    :type id: const struct sfp_eeprom_id \*

    :param link_modes:
        ethtool link modes mask
    :type link_modes: unsigned long \*

.. _`sfp_select_interface.description`:

Description
-----------

Derive the phy_interface_t mode for the information found in the
module's identifying EEPROM and the link modes mask. There is no
standard or defined way to derive this information, so we decide
based upon the link mode mask.

.. _`sfp_get_module_info`:

sfp_get_module_info
===================

.. c:function:: int sfp_get_module_info(struct sfp_bus *bus, struct ethtool_modinfo *modinfo)

    Get the ethtool_modinfo for a SFP module

    :param bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module
    :type bus: struct sfp_bus \*

    :param modinfo:
        a \ :c:type:`struct ethtool_modinfo <ethtool_modinfo>`\ 
    :type modinfo: struct ethtool_modinfo \*

.. _`sfp_get_module_info.description`:

Description
-----------

Fill in the type and eeprom_len parameters in \ ``modinfo``\  for a module on
the sfp bus specified by \ ``bus``\ .

Returns 0 on success or a negative errno number.

.. _`sfp_get_module_eeprom`:

sfp_get_module_eeprom
=====================

.. c:function:: int sfp_get_module_eeprom(struct sfp_bus *bus, struct ethtool_eeprom *ee, u8 *data)

    Read the SFP module EEPROM

    :param bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module
    :type bus: struct sfp_bus \*

    :param ee:
        a \ :c:type:`struct ethtool_eeprom <ethtool_eeprom>`\ 
    :type ee: struct ethtool_eeprom \*

    :param data:
        buffer to contain the EEPROM data (must be at least \ ``ee->len``\  bytes)
    :type data: u8 \*

.. _`sfp_get_module_eeprom.description`:

Description
-----------

Read the EEPROM as specified by the supplied \ ``ee``\ . See the documentation
for \ :c:type:`struct ethtool_eeprom <ethtool_eeprom>`\  for the region to be read.

Returns 0 on success or a negative errno number.

.. _`sfp_upstream_start`:

sfp_upstream_start
==================

.. c:function:: void sfp_upstream_start(struct sfp_bus *bus)

    Inform the SFP that the network device is up

    :param bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module
    :type bus: struct sfp_bus \*

.. _`sfp_upstream_start.description`:

Description
-----------

Inform the SFP socket that the network device is now up, so that the
module can be enabled by allowing TX_DISABLE to be deasserted. This
should be called from the network device driver's \ :c:type:`struct net_device_ops <net_device_ops>`\ 
\ :c:func:`ndo_open`\  method.

.. _`sfp_upstream_stop`:

sfp_upstream_stop
=================

.. c:function:: void sfp_upstream_stop(struct sfp_bus *bus)

    Inform the SFP that the network device is down

    :param bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module
    :type bus: struct sfp_bus \*

.. _`sfp_upstream_stop.description`:

Description
-----------

Inform the SFP socket that the network device is now up, so that the
module can be disabled by asserting TX_DISABLE, disabling the laser
in optical modules. This should be called from the network device
driver's \ :c:type:`struct net_device_ops <net_device_ops>`\  \ :c:func:`ndo_stop`\  method.

.. _`sfp_register_upstream`:

sfp_register_upstream
=====================

.. c:function:: struct sfp_bus *sfp_register_upstream(struct fwnode_handle *fwnode, struct net_device *ndev, void *upstream, const struct sfp_upstream_ops *ops)

    Register the neighbouring device

    :param fwnode:
        firmware node for the SFP bus
    :type fwnode: struct fwnode_handle \*

    :param ndev:
        network device associated with the interface
    :type ndev: struct net_device \*

    :param upstream:
        the upstream private data
    :type upstream: void \*

    :param ops:
        the upstream's \ :c:type:`struct sfp_upstream_ops <sfp_upstream_ops>`\ 
    :type ops: const struct sfp_upstream_ops \*

.. _`sfp_register_upstream.description`:

Description
-----------

Register the upstream device (eg, PHY) with the SFP bus. MAC drivers
should use phylink, which will call this function for them. Returns
a pointer to the allocated \ :c:type:`struct sfp_bus <sfp_bus>`\ .

On error, returns \ ``NULL``\ .

.. _`sfp_unregister_upstream`:

sfp_unregister_upstream
=======================

.. c:function:: void sfp_unregister_upstream(struct sfp_bus *bus)

    Unregister sfp bus

    :param bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module
    :type bus: struct sfp_bus \*

.. _`sfp_unregister_upstream.description`:

Description
-----------

Unregister a previously registered upstream connection for the SFP
module. \ ``bus``\  is returned from \ :c:func:`sfp_register_upstream`\ .

.. This file was automatic generated / don't edit.

