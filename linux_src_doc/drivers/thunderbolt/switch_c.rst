.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/switch.c

.. _`tb_port_state`:

tb_port_state
=============

.. c:function:: int tb_port_state(struct tb_port *port)

    get connectedness state of a port

    :param port:
        *undescribed*
    :type port: struct tb_port \*

.. _`tb_port_state.description`:

Description
-----------

The port must have a TB_CAP_PHY (i.e. it should be a real port).

.. _`tb_port_state.return`:

Return
------

Returns an enum tb_port_state on success or an error code on failure.

.. _`tb_wait_for_port`:

tb_wait_for_port
================

.. c:function:: int tb_wait_for_port(struct tb_port *port, bool wait_if_unplugged)

    wait for a port to become ready

    :param port:
        *undescribed*
    :type port: struct tb_port \*

    :param wait_if_unplugged:
        *undescribed*
    :type wait_if_unplugged: bool

.. _`tb_wait_for_port.description`:

Description
-----------

Wait up to 1 second for a port to reach state TB_PORT_UP. If
wait_if_unplugged is set then we also wait if the port is in state
TB_PORT_UNPLUGGED (it takes a while for the device to be registered after
switch resume). Otherwise we only wait if a device is registered but the link
has not yet been established.

.. _`tb_wait_for_port.return`:

Return
------

Returns an error code on failure. Returns 0 if the port is not
connected or failed to reach state TB_PORT_UP within one second. Returns 1
if the port is connected and in state TB_PORT_UP.

.. _`tb_port_add_nfc_credits`:

tb_port_add_nfc_credits
=======================

.. c:function:: int tb_port_add_nfc_credits(struct tb_port *port, int credits)

    add/remove non flow controlled credits to port

    :param port:
        *undescribed*
    :type port: struct tb_port \*

    :param credits:
        *undescribed*
    :type credits: int

.. _`tb_port_add_nfc_credits.description`:

Description
-----------

Change the number of NFC credits allocated to \ ``port``\  by \ ``credits``\ . To remove
NFC credits pass a negative amount of credits.

.. _`tb_port_add_nfc_credits.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_port_clear_counter`:

tb_port_clear_counter
=====================

.. c:function:: int tb_port_clear_counter(struct tb_port *port, int counter)

    clear a counter in TB_CFG_COUNTER

    :param port:
        *undescribed*
    :type port: struct tb_port \*

    :param counter:
        *undescribed*
    :type counter: int

.. _`tb_port_clear_counter.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_init_port`:

tb_init_port
============

.. c:function:: int tb_init_port(struct tb_port *port)

    initialize a port

    :param port:
        *undescribed*
    :type port: struct tb_port \*

.. _`tb_init_port.description`:

Description
-----------

This is a helper method for tb_switch_alloc. Does not check or initialize
any downstream switches.

.. _`tb_init_port.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_switch_reset`:

tb_switch_reset
===============

.. c:function:: int tb_switch_reset(struct tb *tb, u64 route)

    reconfigure route, enable and send TB_CFG_PKG_RESET

    :param tb:
        *undescribed*
    :type tb: struct tb \*

    :param route:
        *undescribed*
    :type route: u64

.. _`tb_switch_reset.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_plug_events_active`:

tb_plug_events_active
=====================

.. c:function:: int tb_plug_events_active(struct tb_switch *sw, bool active)

    enable/disable plug events on a switch

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

    :param active:
        *undescribed*
    :type active: bool

.. _`tb_plug_events_active.description`:

Description
-----------

Also configures a sane plug_events_delay of 255ms.

.. _`tb_plug_events_active.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_switch_alloc`:

tb_switch_alloc
===============

.. c:function:: struct tb_switch *tb_switch_alloc(struct tb *tb, struct device *parent, u64 route)

    allocate a switch

    :param tb:
        Pointer to the owning domain
    :type tb: struct tb \*

    :param parent:
        Parent device for this switch
    :type parent: struct device \*

    :param route:
        Route string for this switch
    :type route: u64

.. _`tb_switch_alloc.description`:

Description
-----------

Allocates and initializes a switch. Will not upload configuration to
the switch. For that you need to call \ :c:func:`tb_switch_configure`\ 
separately. The returned switch should be released by calling
\ :c:func:`tb_switch_put`\ .

.. _`tb_switch_alloc.return`:

Return
------

Pointer to the allocated switch or \ ``NULL``\  in case of failure

.. _`tb_switch_alloc_safe_mode`:

tb_switch_alloc_safe_mode
=========================

.. c:function:: struct tb_switch *tb_switch_alloc_safe_mode(struct tb *tb, struct device *parent, u64 route)

    allocate a switch that is in safe mode

    :param tb:
        Pointer to the owning domain
    :type tb: struct tb \*

    :param parent:
        Parent device for this switch
    :type parent: struct device \*

    :param route:
        Route string for this switch
    :type route: u64

.. _`tb_switch_alloc_safe_mode.description`:

Description
-----------

This creates a switch in safe mode. This means the switch pretty much
lacks all capabilities except DMA configuration port before it is
flashed with a valid NVM firmware.

The returned switch must be released by calling \ :c:func:`tb_switch_put`\ .

.. _`tb_switch_alloc_safe_mode.return`:

Return
------

Pointer to the allocated switch or \ ``NULL``\  in case of failure

.. _`tb_switch_configure`:

tb_switch_configure
===================

.. c:function:: int tb_switch_configure(struct tb_switch *sw)

    Uploads configuration to the switch

    :param sw:
        Switch to configure
    :type sw: struct tb_switch \*

.. _`tb_switch_configure.description`:

Description
-----------

Call this function before the switch is added to the system. It will
upload configuration to the switch and makes it available for the
connection manager to use.

.. _`tb_switch_configure.return`:

Return
------

\ ``0``\  in case of success and negative errno in case of failure

.. _`tb_switch_add`:

tb_switch_add
=============

.. c:function:: int tb_switch_add(struct tb_switch *sw)

    Add a switch to the domain

    :param sw:
        Switch to add
    :type sw: struct tb_switch \*

.. _`tb_switch_add.description`:

Description
-----------

This is the last step in adding switch to the domain. It will read
identification information from DROM and initializes ports so that
they can be used to connect other switches. The switch will be
exposed to the userspace when this function successfully returns. To
remove and release the switch, call \ :c:func:`tb_switch_remove`\ .

.. _`tb_switch_add.return`:

Return
------

\ ``0``\  in case of success and negative errno in case of failure

.. _`tb_switch_remove`:

tb_switch_remove
================

.. c:function:: void tb_switch_remove(struct tb_switch *sw)

    Remove and release a switch

    :param sw:
        Switch to remove
    :type sw: struct tb_switch \*

.. _`tb_switch_remove.description`:

Description
-----------

This will remove the switch from the domain and release it after last
reference count drops to zero. If there are switches connected below
this switch, they will be removed as well.

.. _`tb_sw_set_unplugged`:

tb_sw_set_unplugged
===================

.. c:function:: void tb_sw_set_unplugged(struct tb_switch *sw)

    set is_unplugged on switch and downstream switches

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

.. _`tb_switch_find_by_link_depth`:

tb_switch_find_by_link_depth
============================

.. c:function:: struct tb_switch *tb_switch_find_by_link_depth(struct tb *tb, u8 link, u8 depth)

    Find switch by link and depth

    :param tb:
        Domain the switch belongs
    :type tb: struct tb \*

    :param link:
        Link number the switch is connected
    :type link: u8

    :param depth:
        Depth of the switch in link
    :type depth: u8

.. _`tb_switch_find_by_link_depth.description`:

Description
-----------

Returned switch has reference count increased so the caller needs to
call \ :c:func:`tb_switch_put`\  when done with the switch.

.. _`tb_switch_find_by_uuid`:

tb_switch_find_by_uuid
======================

.. c:function:: struct tb_switch *tb_switch_find_by_uuid(struct tb *tb, const uuid_t *uuid)

    Find switch by UUID

    :param tb:
        Domain the switch belongs
    :type tb: struct tb \*

    :param uuid:
        UUID to look for
    :type uuid: const uuid_t \*

.. _`tb_switch_find_by_uuid.description`:

Description
-----------

Returned switch has reference count increased so the caller needs to
call \ :c:func:`tb_switch_put`\  when done with the switch.

.. _`tb_switch_find_by_route`:

tb_switch_find_by_route
=======================

.. c:function:: struct tb_switch *tb_switch_find_by_route(struct tb *tb, u64 route)

    Find switch by route string

    :param tb:
        Domain the switch belongs
    :type tb: struct tb \*

    :param route:
        Route string to look for
    :type route: u64

.. _`tb_switch_find_by_route.description`:

Description
-----------

Returned switch has reference count increased so the caller needs to
call \ :c:func:`tb_switch_put`\  when done with the switch.

.. This file was automatic generated / don't edit.

