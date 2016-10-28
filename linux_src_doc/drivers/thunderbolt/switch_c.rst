.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/switch.c

.. _`tb_port_state`:

tb_port_state
=============

.. c:function:: int tb_port_state(struct tb_port *port)

    get connectedness state of a port

    :param struct tb_port \*port:
        *undescribed*

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

    :param struct tb_port \*port:
        *undescribed*

    :param bool wait_if_unplugged:
        *undescribed*

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

    :param struct tb_port \*port:
        *undescribed*

    :param int credits:
        *undescribed*

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

    :param struct tb_port \*port:
        *undescribed*

    :param int counter:
        *undescribed*

.. _`tb_port_clear_counter.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_init_port`:

tb_init_port
============

.. c:function:: int tb_init_port(struct tb_port *port)

    initialize a port

    :param struct tb_port \*port:
        *undescribed*

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

    :param struct tb \*tb:
        *undescribed*

    :param u64 route:
        *undescribed*

.. _`tb_switch_reset.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_plug_events_active`:

tb_plug_events_active
=====================

.. c:function:: int tb_plug_events_active(struct tb_switch *sw, bool active)

    enable/disable plug events on a switch

    :param struct tb_switch \*sw:
        *undescribed*

    :param bool active:
        *undescribed*

.. _`tb_plug_events_active.description`:

Description
-----------

Also configures a sane plug_events_delay of 255ms.

.. _`tb_plug_events_active.return`:

Return
------

Returns 0 on success or an error code on failure.

.. _`tb_switch_free`:

tb_switch_free
==============

.. c:function:: void tb_switch_free(struct tb_switch *sw)

    free a tb_switch and all downstream switches

    :param struct tb_switch \*sw:
        *undescribed*

.. _`tb_switch_alloc`:

tb_switch_alloc
===============

.. c:function:: struct tb_switch *tb_switch_alloc(struct tb *tb, u64 route)

    allocate and initialize a switch

    :param struct tb \*tb:
        *undescribed*

    :param u64 route:
        *undescribed*

.. _`tb_switch_alloc.return`:

Return
------

Returns a NULL on failure.

.. _`tb_sw_set_unplugged`:

tb_sw_set_unplugged
===================

.. c:function:: void tb_sw_set_unplugged(struct tb_switch *sw)

    set is_unplugged on switch and downstream switches

    :param struct tb_switch \*sw:
        *undescribed*

.. This file was automatic generated / don't edit.

