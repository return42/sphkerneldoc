.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/typec/typec.c

.. _`typec_altmode_update_active`:

typec_altmode_update_active
===========================

.. c:function:: void typec_altmode_update_active(struct typec_altmode *alt, int mode, bool active)

    Report Enter/Exit mode

    :param struct typec_altmode \*alt:
        Handle to the alternate mode

    :param int mode:
        Mode index

    :param bool active:
        True when the mode has been entered

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

    :param struct typec_altmode \*alt:
        The Alternate Mode

.. _`typec_altmode2port.description`:

Description
-----------

Returns handle to the port that a cable plug or partner with \ ``alt``\  is
connected to.

.. _`typec_unregister_altmode`:

typec_unregister_altmode
========================

.. c:function:: void typec_unregister_altmode(struct typec_altmode *alt)

    Unregister Alternate Mode

    :param struct typec_altmode \*alt:
        The alternate mode to be unregistered

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

    :param struct typec_partner \*partner:
        The partner updated identity values

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

    :param struct typec_partner \*partner:
        USB Type-C Partner that supports the alternate mode

    :param const struct typec_altmode_desc \*desc:
        Description of the alternate mode

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

    :param struct typec_port \*port:
        The USB Type-C Port the partner is connected to

    :param struct typec_partner_desc \*desc:
        Description of the partner

.. _`typec_register_partner.description`:

Description
-----------

Registers a device for USB Type-C Partner described in \ ``desc``\ .

Returns handle to the partner on success or NULL on failure.

.. _`typec_unregister_partner`:

typec_unregister_partner
========================

.. c:function:: void typec_unregister_partner(struct typec_partner *partner)

    Unregister a USB Type-C Partner

    :param struct typec_partner \*partner:
        The partner to be unregistered

.. _`typec_unregister_partner.description`:

Description
-----------

Unregister device created with \ :c:func:`typec_register_partner`\ .

.. _`typec_plug_register_altmode`:

typec_plug_register_altmode
===========================

.. c:function:: struct typec_altmode *typec_plug_register_altmode(struct typec_plug *plug, const struct typec_altmode_desc *desc)

    Register USB Type-C Cable Plug Alternate Mode

    :param struct typec_plug \*plug:
        USB Type-C Cable Plug that supports the alternate mode

    :param const struct typec_altmode_desc \*desc:
        Description of the alternate mode

.. _`typec_plug_register_altmode.description`:

Description
-----------

This routine is used to register each alternate mode individually that \ ``plug``\ 
has listed in response to Discover SVIDs command. The modes for a SVID that
the plug lists in response to Discover Modes command need to be listed in an
array in \ ``desc``\ .

Returns handle to the alternate mode on success or NULL on failure.

.. _`typec_register_plug`:

typec_register_plug
===================

.. c:function:: struct typec_plug *typec_register_plug(struct typec_cable *cable, struct typec_plug_desc *desc)

    Register a USB Type-C Cable Plug

    :param struct typec_cable \*cable:
        USB Type-C Cable with the plug

    :param struct typec_plug_desc \*desc:
        Description of the cable plug

.. _`typec_register_plug.description`:

Description
-----------

Registers a device for USB Type-C Cable Plug described in \ ``desc``\ . A USB Type-C
Cable Plug represents a plug with electronics in it that can response to USB
Power Delivery SOP Prime or SOP Double Prime packages.

Returns handle to the cable plug on success or NULL on failure.

.. _`typec_unregister_plug`:

typec_unregister_plug
=====================

.. c:function:: void typec_unregister_plug(struct typec_plug *plug)

    Unregister a USB Type-C Cable Plug

    :param struct typec_plug \*plug:
        The cable plug to be unregistered

.. _`typec_unregister_plug.description`:

Description
-----------

Unregister device created with \ :c:func:`typec_register_plug`\ .

.. _`typec_cable_set_identity`:

typec_cable_set_identity
========================

.. c:function:: int typec_cable_set_identity(struct typec_cable *cable)

    Report result from Discover Identity command

    :param struct typec_cable \*cable:
        The cable updated identity values

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

    :param struct typec_port \*port:
        The USB Type-C Port the cable is connected to

    :param struct typec_cable_desc \*desc:
        Description of the cable

.. _`typec_register_cable.description`:

Description
-----------

Registers a device for USB Type-C Cable described in \ ``desc``\ . The cable will be
parent for the optional cable plug devises.

Returns handle to the cable on success or NULL on failure.

.. _`typec_unregister_cable`:

typec_unregister_cable
======================

.. c:function:: void typec_unregister_cable(struct typec_cable *cable)

    Unregister a USB Type-C Cable

    :param struct typec_cable \*cable:
        The cable to be unregistered

.. _`typec_unregister_cable.description`:

Description
-----------

Unregister device created with \ :c:func:`typec_register_cable`\ .

.. _`typec_set_data_role`:

typec_set_data_role
===================

.. c:function:: void typec_set_data_role(struct typec_port *port, enum typec_data_role role)

    Report data role change

    :param struct typec_port \*port:
        The USB Type-C Port where the role was changed

    :param enum typec_data_role role:
        The new data role

.. _`typec_set_data_role.description`:

Description
-----------

This routine is used by the port drivers to report data role changes.

.. _`typec_set_pwr_role`:

typec_set_pwr_role
==================

.. c:function:: void typec_set_pwr_role(struct typec_port *port, enum typec_role role)

    Report power role change

    :param struct typec_port \*port:
        The USB Type-C Port where the role was changed

    :param enum typec_role role:
        The new data role

.. _`typec_set_pwr_role.description`:

Description
-----------

This routine is used by the port drivers to report power role changes.

.. _`typec_set_vconn_role`:

typec_set_vconn_role
====================

.. c:function:: void typec_set_vconn_role(struct typec_port *port, enum typec_role role)

    Report VCONN source change

    :param struct typec_port \*port:
        The USB Type-C Port which VCONN role changed

    :param enum typec_role role:
        Source when \ ``port``\  is sourcing VCONN, or Sink when it's not

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

    :param struct typec_port \*port:
        The USB Type-C Port where the mode was changed

    :param enum typec_pwr_opmode opmode:
        New power operation mode

.. _`typec_set_pwr_opmode.description`:

Description
-----------

This routine is used by the port drivers to report changed power operation
mode in \ ``port``\ . The modes are USB (default), 1.5A, 3.0A as defined in USB
Type-C specification, and "USB Power Delivery" when the power levels are
negotiated with methods defined in USB Power Delivery specification.

.. _`typec_port_register_altmode`:

typec_port_register_altmode
===========================

.. c:function:: struct typec_altmode *typec_port_register_altmode(struct typec_port *port, const struct typec_altmode_desc *desc)

    Register USB Type-C Port Alternate Mode

    :param struct typec_port \*port:
        USB Type-C Port that supports the alternate mode

    :param const struct typec_altmode_desc \*desc:
        Description of the alternate mode

.. _`typec_port_register_altmode.description`:

Description
-----------

This routine is used to register an alternate mode that \ ``port``\  is capable of
supporting.

Returns handle to the alternate mode on success or NULL on failure.

.. _`typec_register_port`:

typec_register_port
===================

.. c:function:: struct typec_port *typec_register_port(struct device *parent, const struct typec_capability *cap)

    Register a USB Type-C Port

    :param struct device \*parent:
        Parent device

    :param const struct typec_capability \*cap:
        Description of the port

.. _`typec_register_port.description`:

Description
-----------

Registers a device for USB Type-C Port described in \ ``cap``\ .

Returns handle to the port on success or NULL on failure.

.. _`typec_unregister_port`:

typec_unregister_port
=====================

.. c:function:: void typec_unregister_port(struct typec_port *port)

    Unregister a USB Type-C Port

    :param struct typec_port \*port:
        The port to be unregistered

.. _`typec_unregister_port.description`:

Description
-----------

Unregister device created with \ :c:func:`typec_register_port`\ .

.. This file was automatic generated / don't edit.

