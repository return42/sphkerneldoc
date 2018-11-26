.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/typec/class.c

.. _`typec_altmode_update_active`:

typec_altmode_update_active
===========================

.. c:function:: void typec_altmode_update_active(struct typec_altmode *adev, bool active)

    Report Enter/Exit mode

    :param adev:
        Handle to the alternate mode
    :type adev: struct typec_altmode \*

    :param active:
        True when the mode has been entered
    :type active: bool

.. _`typec_altmode_update_active.description`:

Description
-----------

If a partner or cable plug executes Enter/Exit Mode command successfully, the
drivers use this routine to report the updated state of the mode.

.. _`typec_altmode2port`:

typec_altmode2port
==================

.. c:function:: struct typec_port *typec_altmode2port(struct typec_altmode *alt)

    Alternate Mode to USB Type-C port

    :param alt:
        The Alternate Mode
    :type alt: struct typec_altmode \*

.. _`typec_altmode2port.description`:

Description
-----------

Returns handle to the port that a cable plug or partner with \ ``alt``\  is
connected to.

.. _`typec_unregister_altmode`:

typec_unregister_altmode
========================

.. c:function:: void typec_unregister_altmode(struct typec_altmode *adev)

    Unregister Alternate Mode

    :param adev:
        The alternate mode to be unregistered
    :type adev: struct typec_altmode \*

.. _`typec_unregister_altmode.description`:

Description
-----------

Unregister device created with \ :c:func:`typec_partner_register_altmode`\ ,
\ :c:func:`typec_plug_register_altmode`\  or \ :c:func:`typec_port_register_altmode`\ .

.. _`typec_partner_set_identity`:

typec_partner_set_identity
==========================

.. c:function:: int typec_partner_set_identity(struct typec_partner *partner)

    Report result from Discover Identity command

    :param partner:
        The partner updated identity values
    :type partner: struct typec_partner \*

.. _`typec_partner_set_identity.description`:

Description
-----------

This routine is used to report that the result of Discover Identity USB power
delivery command has become available.

.. _`typec_partner_register_altmode`:

typec_partner_register_altmode
==============================

.. c:function:: struct typec_altmode *typec_partner_register_altmode(struct typec_partner *partner, const struct typec_altmode_desc *desc)

    Register USB Type-C Partner Alternate Mode

    :param partner:
        USB Type-C Partner that supports the alternate mode
    :type partner: struct typec_partner \*

    :param desc:
        Description of the alternate mode
    :type desc: const struct typec_altmode_desc \*

.. _`typec_partner_register_altmode.description`:

Description
-----------

This routine is used to register each alternate mode individually that
\ ``partner``\  has listed in response to Discover SVIDs command. The modes for a
SVID listed in response to Discover Modes command need to be listed in an
array in \ ``desc``\ .

Returns handle to the alternate mode on success or NULL on failure.

.. _`typec_register_partner`:

typec_register_partner
======================

.. c:function:: struct typec_partner *typec_register_partner(struct typec_port *port, struct typec_partner_desc *desc)

    Register a USB Type-C Partner

    :param port:
        The USB Type-C Port the partner is connected to
    :type port: struct typec_port \*

    :param desc:
        Description of the partner
    :type desc: struct typec_partner_desc \*

.. _`typec_register_partner.description`:

Description
-----------

Registers a device for USB Type-C Partner described in \ ``desc``\ .

Returns handle to the partner on success or ERR_PTR on failure.

.. _`typec_unregister_partner`:

typec_unregister_partner
========================

.. c:function:: void typec_unregister_partner(struct typec_partner *partner)

    Unregister a USB Type-C Partner

    :param partner:
        The partner to be unregistered
    :type partner: struct typec_partner \*

.. _`typec_unregister_partner.description`:

Description
-----------

Unregister device created with \ :c:func:`typec_register_partner`\ .

.. _`typec_plug_register_altmode`:

typec_plug_register_altmode
===========================

.. c:function:: struct typec_altmode *typec_plug_register_altmode(struct typec_plug *plug, const struct typec_altmode_desc *desc)

    Register USB Type-C Cable Plug Alternate Mode

    :param plug:
        USB Type-C Cable Plug that supports the alternate mode
    :type plug: struct typec_plug \*

    :param desc:
        Description of the alternate mode
    :type desc: const struct typec_altmode_desc \*

.. _`typec_plug_register_altmode.description`:

Description
-----------

This routine is used to register each alternate mode individually that \ ``plug``\ 
has listed in response to Discover SVIDs command. The modes for a SVID that
the plug lists in response to Discover Modes command need to be listed in an
array in \ ``desc``\ .

Returns handle to the alternate mode on success or ERR_PTR on failure.

.. _`typec_register_plug`:

typec_register_plug
===================

.. c:function:: struct typec_plug *typec_register_plug(struct typec_cable *cable, struct typec_plug_desc *desc)

    Register a USB Type-C Cable Plug

    :param cable:
        USB Type-C Cable with the plug
    :type cable: struct typec_cable \*

    :param desc:
        Description of the cable plug
    :type desc: struct typec_plug_desc \*

.. _`typec_register_plug.description`:

Description
-----------

Registers a device for USB Type-C Cable Plug described in \ ``desc``\ . A USB Type-C
Cable Plug represents a plug with electronics in it that can response to USB
Power Delivery SOP Prime or SOP Double Prime packages.

Returns handle to the cable plug on success or ERR_PTR on failure.

.. _`typec_unregister_plug`:

typec_unregister_plug
=====================

.. c:function:: void typec_unregister_plug(struct typec_plug *plug)

    Unregister a USB Type-C Cable Plug

    :param plug:
        The cable plug to be unregistered
    :type plug: struct typec_plug \*

.. _`typec_unregister_plug.description`:

Description
-----------

Unregister device created with \ :c:func:`typec_register_plug`\ .

.. _`typec_cable_set_identity`:

typec_cable_set_identity
========================

.. c:function:: int typec_cable_set_identity(struct typec_cable *cable)

    Report result from Discover Identity command

    :param cable:
        The cable updated identity values
    :type cable: struct typec_cable \*

.. _`typec_cable_set_identity.description`:

Description
-----------

This routine is used to report that the result of Discover Identity USB power
delivery command has become available.

.. _`typec_register_cable`:

typec_register_cable
====================

.. c:function:: struct typec_cable *typec_register_cable(struct typec_port *port, struct typec_cable_desc *desc)

    Register a USB Type-C Cable

    :param port:
        The USB Type-C Port the cable is connected to
    :type port: struct typec_port \*

    :param desc:
        Description of the cable
    :type desc: struct typec_cable_desc \*

.. _`typec_register_cable.description`:

Description
-----------

Registers a device for USB Type-C Cable described in \ ``desc``\ . The cable will be
parent for the optional cable plug devises.

Returns handle to the cable on success or ERR_PTR on failure.

.. _`typec_unregister_cable`:

typec_unregister_cable
======================

.. c:function:: void typec_unregister_cable(struct typec_cable *cable)

    Unregister a USB Type-C Cable

    :param cable:
        The cable to be unregistered
    :type cable: struct typec_cable \*

.. _`typec_unregister_cable.description`:

Description
-----------

Unregister device created with \ :c:func:`typec_register_cable`\ .

.. _`typec_set_data_role`:

typec_set_data_role
===================

.. c:function:: void typec_set_data_role(struct typec_port *port, enum typec_data_role role)

    Report data role change

    :param port:
        The USB Type-C Port where the role was changed
    :type port: struct typec_port \*

    :param role:
        The new data role
    :type role: enum typec_data_role

.. _`typec_set_data_role.description`:

Description
-----------

This routine is used by the port drivers to report data role changes.

.. _`typec_set_pwr_role`:

typec_set_pwr_role
==================

.. c:function:: void typec_set_pwr_role(struct typec_port *port, enum typec_role role)

    Report power role change

    :param port:
        The USB Type-C Port where the role was changed
    :type port: struct typec_port \*

    :param role:
        The new data role
    :type role: enum typec_role

.. _`typec_set_pwr_role.description`:

Description
-----------

This routine is used by the port drivers to report power role changes.

.. _`typec_set_vconn_role`:

typec_set_vconn_role
====================

.. c:function:: void typec_set_vconn_role(struct typec_port *port, enum typec_role role)

    Report VCONN source change

    :param port:
        The USB Type-C Port which VCONN role changed
    :type port: struct typec_port \*

    :param role:
        Source when \ ``port``\  is sourcing VCONN, or Sink when it's not
    :type role: enum typec_role

.. _`typec_set_vconn_role.description`:

Description
-----------

This routine is used by the port drivers to report if the VCONN source is
changes.

.. _`typec_set_pwr_opmode`:

typec_set_pwr_opmode
====================

.. c:function:: void typec_set_pwr_opmode(struct typec_port *port, enum typec_pwr_opmode opmode)

    Report changed power operation mode

    :param port:
        The USB Type-C Port where the mode was changed
    :type port: struct typec_port \*

    :param opmode:
        New power operation mode
    :type opmode: enum typec_pwr_opmode

.. _`typec_set_pwr_opmode.description`:

Description
-----------

This routine is used by the port drivers to report changed power operation
mode in \ ``port``\ . The modes are USB (default), 1.5A, 3.0A as defined in USB
Type-C specification, and "USB Power Delivery" when the power levels are
negotiated with methods defined in USB Power Delivery specification.

.. _`typec_find_port_power_role`:

typec_find_port_power_role
==========================

.. c:function:: int typec_find_port_power_role(const char *name)

    Get the typec port power capability

    :param name:
        port power capability string
    :type name: const char \*

.. _`typec_find_port_power_role.description`:

Description
-----------

This routine is used to find the typec_port_type by its string name.

Returns typec_port_type if success, otherwise negative error code.

.. _`typec_find_power_role`:

typec_find_power_role
=====================

.. c:function:: int typec_find_power_role(const char *name)

    Find the typec one specific power role

    :param name:
        power role string
    :type name: const char \*

.. _`typec_find_power_role.description`:

Description
-----------

This routine is used to find the typec_role by its string name.

Returns typec_role if success, otherwise negative error code.

.. _`typec_find_port_data_role`:

typec_find_port_data_role
=========================

.. c:function:: int typec_find_port_data_role(const char *name)

    Get the typec port data capability

    :param name:
        port data capability string
    :type name: const char \*

.. _`typec_find_port_data_role.description`:

Description
-----------

This routine is used to find the typec_port_data by its string name.

Returns typec_port_data if success, otherwise negative error code.

.. _`typec_set_orientation`:

typec_set_orientation
=====================

.. c:function:: int typec_set_orientation(struct typec_port *port, enum typec_orientation orientation)

    Set USB Type-C cable plug orientation

    :param port:
        USB Type-C Port
    :type port: struct typec_port \*

    :param orientation:
        USB Type-C cable plug orientation
    :type orientation: enum typec_orientation

.. _`typec_set_orientation.description`:

Description
-----------

Set cable plug orientation for \ ``port``\ .

.. _`typec_get_orientation`:

typec_get_orientation
=====================

.. c:function:: enum typec_orientation typec_get_orientation(struct typec_port *port)

    Get USB Type-C cable plug orientation

    :param port:
        USB Type-C Port
    :type port: struct typec_port \*

.. _`typec_get_orientation.description`:

Description
-----------

Get current cable plug orientation for \ ``port``\ .

.. _`typec_set_mode`:

typec_set_mode
==============

.. c:function:: int typec_set_mode(struct typec_port *port, int mode)

    Set mode of operation for USB Type-C connector

    :param port:
        USB Type-C connector
    :type port: struct typec_port \*

    :param mode:
        Accessory Mode, USB Operation or Safe State
    :type mode: int

.. _`typec_set_mode.description`:

Description
-----------

Configure \ ``port``\  for Accessory Mode \ ``mode``\ . This function will configure the
muxes needed for \ ``mode``\ .

.. _`typec_port_register_altmode`:

typec_port_register_altmode
===========================

.. c:function:: struct typec_altmode *typec_port_register_altmode(struct typec_port *port, const struct typec_altmode_desc *desc)

    Register USB Type-C Port Alternate Mode

    :param port:
        USB Type-C Port that supports the alternate mode
    :type port: struct typec_port \*

    :param desc:
        Description of the alternate mode
    :type desc: const struct typec_altmode_desc \*

.. _`typec_port_register_altmode.description`:

Description
-----------

This routine is used to register an alternate mode that \ ``port``\  is capable of
supporting.

Returns handle to the alternate mode on success or ERR_PTR on failure.

.. _`typec_register_port`:

typec_register_port
===================

.. c:function:: struct typec_port *typec_register_port(struct device *parent, const struct typec_capability *cap)

    Register a USB Type-C Port

    :param parent:
        Parent device
    :type parent: struct device \*

    :param cap:
        Description of the port
    :type cap: const struct typec_capability \*

.. _`typec_register_port.description`:

Description
-----------

Registers a device for USB Type-C Port described in \ ``cap``\ .

Returns handle to the port on success or ERR_PTR on failure.

.. _`typec_unregister_port`:

typec_unregister_port
=====================

.. c:function:: void typec_unregister_port(struct typec_port *port)

    Unregister a USB Type-C Port

    :param port:
        The port to be unregistered
    :type port: struct typec_port \*

.. _`typec_unregister_port.description`:

Description
-----------

Unregister device created with \ :c:func:`typec_register_port`\ .

.. This file was automatic generated / don't edit.

