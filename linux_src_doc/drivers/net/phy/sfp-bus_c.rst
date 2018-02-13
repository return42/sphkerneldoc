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

    :param struct sfp_bus \*bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module

    :param const struct sfp_eeprom_id \*id:
        a pointer to the module's \ :c:type:`struct sfp_eeprom_id <sfp_eeprom_id>`\ 

    :param unsigned long \*support:
        optional pointer to an array of unsigned long for the
        ethtool support mask

.. _`sfp_parse_port.description`:

Description
-----------

Parse the EEPROM identification given in \ ``id``\ , and return one of
\ ``PORT_TP``\ , \ ``PORT_FIBRE``\  or \ ``PORT_OTHER``\ . If \ ``support``\  is non-%NULL,
also set the ethtool \ ``ETHTOOL_LINK_MODE_xxx_BIT``\  corresponding with
the connector type.

If the port type is not known, returns \ ``PORT_OTHER``\ .

.. _`sfp_parse_interface`:

sfp_parse_interface
===================

.. c:function:: phy_interface_t sfp_parse_interface(struct sfp_bus *bus, const struct sfp_eeprom_id *id)

    Parse the phy_interface_t

    :param struct sfp_bus \*bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module

    :param const struct sfp_eeprom_id \*id:
        a pointer to the module's \ :c:type:`struct sfp_eeprom_id <sfp_eeprom_id>`\ 

.. _`sfp_parse_interface.description`:

Description
-----------

Derive the phy_interface_t mode for the information found in the
module's identifying EEPROM. There is no standard or defined way
to derive this information, so we use some heuristics.

If the encoding is 64b66b, then the module must be >= 10G, so
return \ ``PHY_INTERFACE_MODE_10GKR``\ .

If it's 8b10b, then it's 1G or slower. If it's definitely a fibre
module, return \ ``PHY_INTERFACE_MODE_1000BASEX``\  mode, otherwise return
\ ``PHY_INTERFACE_MODE_SGMII``\  mode.

If the encoding is not known, return \ ``PHY_INTERFACE_MODE_NA``\ .

.. _`sfp_parse_support`:

sfp_parse_support
=================

.. c:function:: void sfp_parse_support(struct sfp_bus *bus, const struct sfp_eeprom_id *id, unsigned long *support)

    Parse the eeprom id for supported link modes

    :param struct sfp_bus \*bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module

    :param const struct sfp_eeprom_id \*id:
        a pointer to the module's \ :c:type:`struct sfp_eeprom_id <sfp_eeprom_id>`\ 

    :param unsigned long \*support:
        pointer to an array of unsigned long for the ethtool support mask

.. _`sfp_parse_support.description`:

Description
-----------

Parse the EEPROM identification information and derive the supported
ethtool link modes for the module.

.. _`sfp_get_module_info`:

sfp_get_module_info
===================

.. c:function:: int sfp_get_module_info(struct sfp_bus *bus, struct ethtool_modinfo *modinfo)

    Get the ethtool_modinfo for a SFP module

    :param struct sfp_bus \*bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module

    :param struct ethtool_modinfo \*modinfo:
        a \ :c:type:`struct ethtool_modinfo <ethtool_modinfo>`\ 

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

    :param struct sfp_bus \*bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module

    :param struct ethtool_eeprom \*ee:
        a \ :c:type:`struct ethtool_eeprom <ethtool_eeprom>`\ 

    :param u8 \*data:
        buffer to contain the EEPROM data (must be at least \ ``ee``\ ->len bytes)

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

    :param struct sfp_bus \*bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module

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

    :param struct sfp_bus \*bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module

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

    :param struct fwnode_handle \*fwnode:
        firmware node for the SFP bus

    :param struct net_device \*ndev:
        network device associated with the interface

    :param void \*upstream:
        the upstream private data

    :param const struct sfp_upstream_ops \*ops:
        the upstream's \ :c:type:`struct sfp_upstream_ops <sfp_upstream_ops>`\ 

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

    :param struct sfp_bus \*bus:
        a pointer to the \ :c:type:`struct sfp_bus <sfp_bus>`\  structure for the sfp module

.. _`sfp_unregister_upstream.description`:

Description
-----------

Unregister a previously registered upstream connection for the SFP
module. \ ``bus``\  is returned from \ :c:func:`sfp_register_upstream`\ .

.. This file was automatic generated / don't edit.

