.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/phy_device.c

.. _`phy_register_fixup`:

phy_register_fixup
==================

.. c:function:: int phy_register_fixup(const char *bus_id, u32 phy_uid, u32 phy_uid_mask, int (*) run (struct phy_device *)

    creates a new phy_fixup and adds it to the list

    :param const char \*bus_id:
        A string which matches phydev->mdio.dev.bus_id (or PHY_ANY_ID)

    :param u32 phy_uid:
        Used to match against phydev->phy_id (the UID of the PHY)
        It can also be PHY_ANY_UID

    :param u32 phy_uid_mask:
        Applied to phydev->phy_id and fixup->phy_uid before
        comparison

    :param (int (\*) run (struct phy_device \*):
        The actual code to be run when a matching PHY is found

.. _`get_phy_c45_ids`:

get_phy_c45_ids
===============

.. c:function:: int get_phy_c45_ids(struct mii_bus *bus, int addr, u32 *phy_id, struct phy_c45_device_ids *c45_ids)

    reads the specified addr for its 802.3-c45 IDs.

    :param struct mii_bus \*bus:
        the target MII bus

    :param int addr:
        PHY address on the MII bus

    :param u32 \*phy_id:
        where to store the ID retrieved.

    :param struct phy_c45_device_ids \*c45_ids:
        where to store the c45 ID information.

.. _`get_phy_c45_ids.description`:

Description
-----------

If the PHY devices-in-package appears to be valid, it and the
corresponding identifiers are stored in \ ``c45_ids``\ , zero is stored
in \ ``phy_id``\ .  Otherwise 0xffffffff is stored in \ ``phy_id``\ .  Returns
zero on success.

.. _`get_phy_id`:

get_phy_id
==========

.. c:function:: int get_phy_id(struct mii_bus *bus, int addr, u32 *phy_id, bool is_c45, struct phy_c45_device_ids *c45_ids)

    reads the specified addr for its ID.

    :param struct mii_bus \*bus:
        the target MII bus

    :param int addr:
        PHY address on the MII bus

    :param u32 \*phy_id:
        where to store the ID retrieved.

    :param bool is_c45:
        If true the PHY uses the 802.3 clause 45 protocol

    :param struct phy_c45_device_ids \*c45_ids:
        where to store the c45 ID information.

.. _`get_phy_id.description`:

Description
-----------

In the case of a 802.3-c22 PHY, reads the ID registers
of the PHY at \ ``addr``\  on the \ ``bus``\ , stores it in \ ``phy_id``\  and returns
zero on success.

In the case of a 802.3-c45 PHY, \ :c:func:`get_phy_c45_ids`\  is invoked, and
its return value is in turn returned.

.. _`get_phy_device`:

get_phy_device
==============

.. c:function:: struct phy_device *get_phy_device(struct mii_bus *bus, int addr, bool is_c45)

    reads the specified PHY device and returns its \ ``phy_device``\  struct

    :param struct mii_bus \*bus:
        the target MII bus

    :param int addr:
        PHY address on the MII bus

    :param bool is_c45:
        If true the PHY uses the 802.3 clause 45 protocol

.. _`get_phy_device.description`:

Description
-----------

Reads the ID registers of the PHY at \ ``addr``\  on the
\ ``bus``\ , then allocates and returns the phy_device to represent it.

.. _`phy_device_register`:

phy_device_register
===================

.. c:function:: int phy_device_register(struct phy_device *phydev)

    Register the phy device on the MDIO bus

    :param struct phy_device \*phydev:
        phy_device structure to be added to the MDIO bus

.. _`phy_device_remove`:

phy_device_remove
=================

.. c:function:: void phy_device_remove(struct phy_device *phydev)

    Remove a previously registered phy device from the MDIO bus

    :param struct phy_device \*phydev:
        phy_device structure to remove

.. _`phy_device_remove.description`:

Description
-----------

This doesn't free the phy_device itself, it merely reverses the effects
of \ :c:func:`phy_device_register`\ . Use \ :c:func:`phy_device_free`\  to free the device
after calling this function.

.. _`phy_find_first`:

phy_find_first
==============

.. c:function:: struct phy_device *phy_find_first(struct mii_bus *bus)

    finds the first PHY device on the bus

    :param struct mii_bus \*bus:
        the target MII bus

.. _`phy_prepare_link`:

phy_prepare_link
================

.. c:function:: void phy_prepare_link(struct phy_device *phydev, void (*) handler (struct net_device *)

    prepares the PHY layer to monitor link status

    :param struct phy_device \*phydev:
        target phy_device struct

    :param (void (\*) handler (struct net_device \*):
        callback function for link status change notifications

.. _`phy_prepare_link.description`:

Description
-----------

Tells the PHY infrastructure to handle the
gory details on monitoring link status (whether through
polling or an interrupt), and to call back to the
connected device driver when the link status changes.
If you want to monitor your own link state, don't call
this function.

.. _`phy_connect_direct`:

phy_connect_direct
==================

.. c:function:: int phy_connect_direct(struct net_device *dev, struct phy_device *phydev, void (*) handler (struct net_device *, phy_interface_t interface)

    connect an ethernet device to a specific phy_device

    :param struct net_device \*dev:
        the network device to connect

    :param struct phy_device \*phydev:
        the pointer to the phy device

    :param (void (\*) handler (struct net_device \*):
        callback function for state change notifications

    :param phy_interface_t interface:
        PHY device's interface

.. _`phy_connect`:

phy_connect
===========

.. c:function:: struct phy_device *phy_connect(struct net_device *dev, const char *bus_id, void (*) handler (struct net_device *, phy_interface_t interface)

    connect an ethernet device to a PHY device

    :param struct net_device \*dev:
        the network device to connect

    :param const char \*bus_id:
        the id string of the PHY device to connect

    :param (void (\*) handler (struct net_device \*):
        callback function for state change notifications

    :param phy_interface_t interface:
        PHY device's interface

.. _`phy_connect.description`:

Description
-----------

Convenience function for connecting ethernet
devices to PHY devices.  The default behavior is for
the PHY infrastructure to handle everything, and only notify
the connected driver when the link status changes.  If you
don't want, or can't use the provided functionality, you may
choose to call only the subset of functions which provide
the desired functionality.

.. _`phy_disconnect`:

phy_disconnect
==============

.. c:function:: void phy_disconnect(struct phy_device *phydev)

    disable interrupts, stop state machine, and detach a PHY device

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_poll_reset`:

phy_poll_reset
==============

.. c:function:: int phy_poll_reset(struct phy_device *phydev)

    Safely wait until a PHY reset has properly completed

    :param struct phy_device \*phydev:
        The PHY device to poll

.. _`phy_poll_reset.description`:

Description
-----------

According to IEEE 802.3, Section 2, Subsection 22.2.4.1.1, as
published in 2008, a PHY reset may take up to 0.5 seconds.  The MII BMCR
register must be polled until the BMCR_RESET bit clears.

Furthermore, any attempts to write to PHY registers may have no effect
or even generate MDIO bus errors until this is complete.

Some PHYs (such as the Marvell 88E1111) don't entirely conform to the
standard and do not fully reset after the BMCR_RESET bit is set, and may
even \*REQUIRE\* a soft-reset to properly restart autonegotiation.  In an
effort to support such broken PHYs, this function is separate from the
standard \ :c:func:`phy_init_hw`\  which will zero all the other bits in the BMCR
and reapply all driver-specific and board-specific fixups.

.. _`phy_attach_direct`:

phy_attach_direct
=================

.. c:function:: int phy_attach_direct(struct net_device *dev, struct phy_device *phydev, u32 flags, phy_interface_t interface)

    attach a network device to a given PHY device pointer

    :param struct net_device \*dev:
        network device to attach

    :param struct phy_device \*phydev:
        Pointer to phy_device to attach

    :param u32 flags:
        PHY device's dev_flags

    :param phy_interface_t interface:
        PHY device's interface

.. _`phy_attach_direct.description`:

Description
-----------

Called by drivers to attach to a particular PHY
device. The phy_device is found, and properly hooked up
to the phy_driver.  If no driver is attached, then a
generic driver is used.  The phy_device is given a ptr to
the attaching device, and given a callback for link status
change.  The phy_device is returned to the attaching driver.
This function takes a reference on the phy device.

.. _`phy_attach`:

phy_attach
==========

.. c:function:: struct phy_device *phy_attach(struct net_device *dev, const char *bus_id, phy_interface_t interface)

    attach a network device to a particular PHY device

    :param struct net_device \*dev:
        network device to attach

    :param const char \*bus_id:
        Bus ID of PHY device to attach

    :param phy_interface_t interface:
        PHY device's interface

.. _`phy_attach.description`:

Description
-----------

Same as \ :c:func:`phy_attach_direct`\  except that a PHY bus_id
string is passed instead of a pointer to a struct phy_device.

.. _`phy_detach`:

phy_detach
==========

.. c:function:: void phy_detach(struct phy_device *phydev)

    detach a PHY device from its network device

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`phy_detach.description`:

Description
-----------

This detaches the phy device from its network device and the phy
driver, and drops the reference count taken in \ :c:func:`phy_attach_direct`\ .

.. _`genphy_config_advert`:

genphy_config_advert
====================

.. c:function:: int genphy_config_advert(struct phy_device *phydev)

    sanitize and advertise auto-negotiation parameters

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`genphy_config_advert.description`:

Description
-----------

Writes MII_ADVERTISE with the appropriate values,
after sanitizing the values to make sure we only advertise
what is supported.  Returns < 0 on error, 0 if the PHY's advertisement
hasn't changed, and > 0 if it has changed.

.. _`genphy_setup_forced`:

genphy_setup_forced
===================

.. c:function:: int genphy_setup_forced(struct phy_device *phydev)

    configures/forces speed/duplex from \ ``phydev``\ 

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`genphy_setup_forced.description`:

Description
-----------

Configures MII_BMCR to force speed/duplex
to the values in phydev. Assumes that the values are valid.
Please see \ :c:func:`phy_sanitize_settings`\ .

.. _`genphy_restart_aneg`:

genphy_restart_aneg
===================

.. c:function:: int genphy_restart_aneg(struct phy_device *phydev)

    Enable and Restart Autonegotiation

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`genphy_config_aneg`:

genphy_config_aneg
==================

.. c:function:: int genphy_config_aneg(struct phy_device *phydev)

    restart auto-negotiation or write BMCR

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`genphy_config_aneg.description`:

Description
-----------

If auto-negotiation is enabled, we configure the
advertising, and then restart auto-negotiation.  If it is not
enabled, then we write the BMCR.

.. _`genphy_aneg_done`:

genphy_aneg_done
================

.. c:function:: int genphy_aneg_done(struct phy_device *phydev)

    return auto-negotiation status

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`genphy_aneg_done.description`:

Description
-----------

Reads the status register and returns 0 either if
auto-negotiation is incomplete, or if there was an error.
Returns BMSR_ANEGCOMPLETE if auto-negotiation is done.

.. _`genphy_update_link`:

genphy_update_link
==================

.. c:function:: int genphy_update_link(struct phy_device *phydev)

    update link status in \ ``phydev``\ 

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`genphy_update_link.description`:

Description
-----------

Update the value in phydev->link to reflect the
current link value.  In order to do this, we need to read
the status register twice, keeping the second value.

.. _`genphy_read_status`:

genphy_read_status
==================

.. c:function:: int genphy_read_status(struct phy_device *phydev)

    check the link status and update current link state

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`genphy_read_status.description`:

Description
-----------

Check the link, then figure out the current state
by comparing what we advertise with what the link partner
advertises.  Start by checking the gigabit possibilities,
then move on to 10/100.

.. _`genphy_soft_reset`:

genphy_soft_reset
=================

.. c:function:: int genphy_soft_reset(struct phy_device *phydev)

    software reset the PHY via BMCR_RESET bit

    :param struct phy_device \*phydev:
        target phy_device struct

.. _`genphy_soft_reset.description`:

Description
-----------

Perform a software PHY reset using the standard
BMCR_RESET bit and poll for the reset bit to be cleared.

.. _`genphy_soft_reset.return`:

Return
------

0 on success, < 0 on failure

.. _`phy_probe`:

phy_probe
=========

.. c:function:: int phy_probe(struct device *dev)

    probe and init a PHY device

    :param struct device \*dev:
        device to probe and init

.. _`phy_probe.description`:

Description
-----------

Take care of setting up the phy_device structure,
set the state to READY (the driver's init function should
set it to STARTING if needed).

.. _`phy_driver_register`:

phy_driver_register
===================

.. c:function:: int phy_driver_register(struct phy_driver *new_driver, struct module *owner)

    register a phy_driver with the PHY layer

    :param struct phy_driver \*new_driver:
        new phy_driver to register

    :param struct module \*owner:
        module owning this PHY

.. This file was automatic generated / don't edit.

