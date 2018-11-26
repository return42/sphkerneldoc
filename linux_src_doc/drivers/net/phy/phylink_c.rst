.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/phylink.c

.. _`phylink`:

struct phylink
==============

.. c:type:: struct phylink

    internal data type for phylink

.. _`phylink.definition`:

Definition
----------

.. code-block:: c

    struct phylink {
    }

.. _`phylink.members`:

Members
-------

void
    no arguments

.. _`phylink_set_port_modes`:

phylink_set_port_modes
======================

.. c:function:: void phylink_set_port_modes(unsigned long *mask)

    set the port type modes in the ethtool mask

    :param mask:
        ethtool link mode mask
    :type mask: unsigned long \*

.. _`phylink_set_port_modes.description`:

Description
-----------

Sets all the port type modes in the ethtool mask.  MAC drivers should
use this in their 'validate' callback.

.. _`phylink_create`:

phylink_create
==============

.. c:function:: struct phylink *phylink_create(struct net_device *ndev, struct fwnode_handle *fwnode, phy_interface_t iface, const struct phylink_mac_ops *ops)

    create a phylink instance

    :param ndev:
        a pointer to the \ :c:type:`struct net_device <net_device>`\ 
    :type ndev: struct net_device \*

    :param fwnode:
        a pointer to a \ :c:type:`struct fwnode_handle <fwnode_handle>`\  describing the network
        interface
    :type fwnode: struct fwnode_handle \*

    :param iface:
        the desired link mode defined by \ :c:type:`typedef phy_interface_t <phy_interface_t>`\ 
    :type iface: phy_interface_t

    :param ops:
        a pointer to a \ :c:type:`struct phylink_mac_ops <phylink_mac_ops>`\  for the MAC.
    :type ops: const struct phylink_mac_ops \*

.. _`phylink_create.description`:

Description
-----------

Create a new phylink instance, and parse the link parameters found in \ ``np``\ .
This will parse in-band modes, fixed-link or SFP configuration.

Returns a pointer to a \ :c:type:`struct phylink <phylink>`\ , or an error-pointer value. Users
must use \ :c:func:`IS_ERR`\  to check for errors from this function.

.. _`phylink_destroy`:

phylink_destroy
===============

.. c:function:: void phylink_destroy(struct phylink *pl)

    cleanup and destroy the phylink instance

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

.. _`phylink_destroy.description`:

Description
-----------

Destroy a phylink instance. Any PHY that has been attached must have been
cleaned up via \ :c:func:`phylink_disconnect_phy`\  prior to calling this function.

.. _`phylink_connect_phy`:

phylink_connect_phy
===================

.. c:function:: int phylink_connect_phy(struct phylink *pl, struct phy_device *phy)

    connect a PHY to the phylink instance

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param phy:
        a pointer to a \ :c:type:`struct phy_device <phy_device>`\ .
    :type phy: struct phy_device \*

.. _`phylink_connect_phy.description`:

Description
-----------

Connect \ ``phy``\  to the phylink instance specified by \ ``pl``\  by calling
\ :c:func:`phy_attach_direct`\ . Configure the \ ``phy``\  according to the MAC driver's
capabilities, start the PHYLIB state machine and enable any interrupts
that the PHY supports.

This updates the phylink's ethtool supported and advertising link mode
masks.

Returns 0 on success or a negative errno.

.. _`phylink_of_phy_connect`:

phylink_of_phy_connect
======================

.. c:function:: int phylink_of_phy_connect(struct phylink *pl, struct device_node *dn, u32 flags)

    connect the PHY specified in the DT mode.

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param dn:
        a pointer to a \ :c:type:`struct device_node <device_node>`\ .
    :type dn: struct device_node \*

    :param flags:
        PHY-specific flags to communicate to the PHY device driver
    :type flags: u32

.. _`phylink_of_phy_connect.description`:

Description
-----------

Connect the phy specified in the device node \ ``dn``\  to the phylink instance
specified by \ ``pl``\ . Actions specified in \ :c:func:`phylink_connect_phy`\  will be
performed.

Returns 0 on success or a negative errno.

.. _`phylink_disconnect_phy`:

phylink_disconnect_phy
======================

.. c:function:: void phylink_disconnect_phy(struct phylink *pl)

    disconnect any PHY attached to the phylink instance.

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

.. _`phylink_disconnect_phy.description`:

Description
-----------

Disconnect any current PHY from the phylink instance described by \ ``pl``\ .

.. _`phylink_fixed_state_cb`:

phylink_fixed_state_cb
======================

.. c:function:: int phylink_fixed_state_cb(struct phylink *pl, void (*cb)(struct net_device *dev, struct phylink_link_state *state))

    allow setting a fixed link callback

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param void (\*cb)(struct net_device \*dev, struct phylink_link_state \*state):
        callback to execute to determine the fixed link state.

.. _`phylink_fixed_state_cb.description`:

Description
-----------

The MAC driver should call this driver when the state of its link
can be determined through e.g: an out of band MMIO register.

.. _`phylink_mac_change`:

phylink_mac_change
==================

.. c:function:: void phylink_mac_change(struct phylink *pl, bool up)

    notify phylink of a change in MAC state

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param up:
        indicates whether the link is currently up.
    :type up: bool

.. _`phylink_mac_change.description`:

Description
-----------

The MAC driver should call this driver when the state of its link
changes (eg, link failure, new negotiation results, etc.)

.. _`phylink_start`:

phylink_start
=============

.. c:function:: void phylink_start(struct phylink *pl)

    start a phylink instance

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

.. _`phylink_start.description`:

Description
-----------

Start the phylink instance specified by \ ``pl``\ , configuring the MAC for the
desired link mode(s) and negotiation style. This should be called from the
network device driver's \ :c:type:`struct net_device_ops <net_device_ops>`\  \ :c:func:`ndo_open`\  method.

.. _`phylink_stop`:

phylink_stop
============

.. c:function:: void phylink_stop(struct phylink *pl)

    stop a phylink instance

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

.. _`phylink_stop.description`:

Description
-----------

Stop the phylink instance specified by \ ``pl``\ . This should be called from the
network device driver's \ :c:type:`struct net_device_ops <net_device_ops>`\  \ :c:func:`ndo_stop`\  method.  The
network device's carrier state should not be changed prior to calling this
function.

.. _`phylink_ethtool_get_wol`:

phylink_ethtool_get_wol
=======================

.. c:function:: void phylink_ethtool_get_wol(struct phylink *pl, struct ethtool_wolinfo *wol)

    get the wake on lan parameters for the PHY

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param wol:
        a pointer to \ :c:type:`struct ethtool_wolinfo <ethtool_wolinfo>`\  to hold the read parameters
    :type wol: struct ethtool_wolinfo \*

.. _`phylink_ethtool_get_wol.description`:

Description
-----------

Read the wake on lan parameters from the PHY attached to the phylink
instance specified by \ ``pl``\ . If no PHY is currently attached, report no
support for wake on lan.

.. _`phylink_ethtool_set_wol`:

phylink_ethtool_set_wol
=======================

.. c:function:: int phylink_ethtool_set_wol(struct phylink *pl, struct ethtool_wolinfo *wol)

    set wake on lan parameters

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param wol:
        a pointer to \ :c:type:`struct ethtool_wolinfo <ethtool_wolinfo>`\  for the desired parameters
    :type wol: struct ethtool_wolinfo \*

.. _`phylink_ethtool_set_wol.description`:

Description
-----------

Set the wake on lan parameters for the PHY attached to the phylink
instance specified by \ ``pl``\ . If no PHY is attached, returns \ ``EOPNOTSUPP``\ 
error.

Returns zero on success or negative errno code.

.. _`phylink_ethtool_ksettings_get`:

phylink_ethtool_ksettings_get
=============================

.. c:function:: int phylink_ethtool_ksettings_get(struct phylink *pl, struct ethtool_link_ksettings *kset)

    get the current link settings

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param kset:
        a pointer to a \ :c:type:`struct ethtool_link_ksettings <ethtool_link_ksettings>`\  to hold link settings
    :type kset: struct ethtool_link_ksettings \*

.. _`phylink_ethtool_ksettings_get.description`:

Description
-----------

Read the current link settings for the phylink instance specified by \ ``pl``\ .
This will be the link settings read from the MAC, PHY or fixed link
settings depending on the current negotiation mode.

.. _`phylink_ethtool_ksettings_set`:

phylink_ethtool_ksettings_set
=============================

.. c:function:: int phylink_ethtool_ksettings_set(struct phylink *pl, const struct ethtool_link_ksettings *kset)

    set the link settings

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param kset:
        a pointer to a \ :c:type:`struct ethtool_link_ksettings <ethtool_link_ksettings>`\  for the desired modes
    :type kset: const struct ethtool_link_ksettings \*

.. _`phylink_ethtool_nway_reset`:

phylink_ethtool_nway_reset
==========================

.. c:function:: int phylink_ethtool_nway_reset(struct phylink *pl)

    restart negotiation

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

.. _`phylink_ethtool_nway_reset.description`:

Description
-----------

Restart negotiation for the phylink instance specified by \ ``pl``\ . This will
cause any attached phy to restart negotiation with the link partner, and
if the MAC is in a BaseX mode, the MAC will also be requested to restart
negotiation.

Returns zero on success, or negative error code.

.. _`phylink_ethtool_get_pauseparam`:

phylink_ethtool_get_pauseparam
==============================

.. c:function:: void phylink_ethtool_get_pauseparam(struct phylink *pl, struct ethtool_pauseparam *pause)

    get the current pause parameters

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param pause:
        a pointer to a \ :c:type:`struct ethtool_pauseparam <ethtool_pauseparam>`\ 
    :type pause: struct ethtool_pauseparam \*

.. _`phylink_ethtool_set_pauseparam`:

phylink_ethtool_set_pauseparam
==============================

.. c:function:: int phylink_ethtool_set_pauseparam(struct phylink *pl, struct ethtool_pauseparam *pause)

    set the current pause parameters

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param pause:
        a pointer to a \ :c:type:`struct ethtool_pauseparam <ethtool_pauseparam>`\ 
    :type pause: struct ethtool_pauseparam \*

.. _`phylink_get_eee_err`:

phylink_get_eee_err
===================

.. c:function:: int phylink_get_eee_err(struct phylink *pl)

    read the energy efficient ethernet error counter

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ .
    :type pl: struct phylink \*

.. _`phylink_get_eee_err.description`:

Description
-----------

Read the Energy Efficient Ethernet error counter from the PHY associated
with the phylink instance specified by \ ``pl``\ .

Returns positive error counter value, or negative error code.

.. _`phylink_ethtool_get_eee`:

phylink_ethtool_get_eee
=======================

.. c:function:: int phylink_ethtool_get_eee(struct phylink *pl, struct ethtool_eee *eee)

    read the energy efficient ethernet parameters

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param eee:
        a pointer to a \ :c:type:`struct ethtool_eee <ethtool_eee>`\  for the read parameters
    :type eee: struct ethtool_eee \*

.. _`phylink_ethtool_set_eee`:

phylink_ethtool_set_eee
=======================

.. c:function:: int phylink_ethtool_set_eee(struct phylink *pl, struct ethtool_eee *eee)

    set the energy efficient ethernet parameters

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param eee:
        a pointer to a \ :c:type:`struct ethtool_eee <ethtool_eee>`\  for the desired parameters
    :type eee: struct ethtool_eee \*

.. _`phylink_mii_ioctl`:

phylink_mii_ioctl
=================

.. c:function:: int phylink_mii_ioctl(struct phylink *pl, struct ifreq *ifr, int cmd)

    generic mii ioctl interface

    :param pl:
        a pointer to a \ :c:type:`struct phylink <phylink>`\  returned from \ :c:func:`phylink_create`\ 
    :type pl: struct phylink \*

    :param ifr:
        a pointer to a \ :c:type:`struct ifreq <ifreq>`\  for socket ioctls
    :type ifr: struct ifreq \*

    :param cmd:
        ioctl cmd to execute
    :type cmd: int

.. _`phylink_mii_ioctl.description`:

Description
-----------

Perform the specified MII ioctl on the PHY attached to the phylink instance
specified by \ ``pl``\ . If no PHY is attached, emulate the presence of the PHY.

.. _`phylink_mii_ioctl.return`:

Return
------

zero on success or negative error code.

\ ``SIOCGMIIPHY``\ :
 read register from the current PHY.
\ ``SIOCGMIIREG``\ :
 read register from the specified PHY.
\ ``SIOCSMIIREG``\ :
 set a register on the specified PHY.

.. _`phylink_helper_basex_speed`:

phylink_helper_basex_speed
==========================

.. c:function:: void phylink_helper_basex_speed(struct phylink_link_state *state)

    1000BaseX/2500BaseX helper

    :param state:
        a pointer to a \ :c:type:`struct phylink_link_state <phylink_link_state>`\ 
    :type state: struct phylink_link_state \*

.. _`phylink_helper_basex_speed.description`:

Description
-----------

Inspect the interface mode, advertising mask or forced speed and
decide whether to run at 2.5Gbit or 1Gbit appropriately, switching
the interface mode to suit.  \ ``state->interface``\  is appropriately
updated, and the advertising mask has the "other" baseX_Full flag
cleared.

.. This file was automatic generated / don't edit.

