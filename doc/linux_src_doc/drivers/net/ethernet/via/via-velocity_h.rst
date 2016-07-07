.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/via/via-velocity.h

.. _`velocity_get_ip`:

velocity_get_ip
===============

.. c:function:: int velocity_get_ip(struct velocity_info *vptr)

    find an IP address for the device

    :param struct velocity_info \*vptr:
        Velocity to query

.. _`velocity_get_ip.description`:

Description
-----------

Dig out an IP address for this interface so that we can
configure wakeup with WOL for ARP. If there are multiple IP
addresses on this chain then we use the first - multi-IP WOL is not
supported.

.. _`velocity_update_hw_mibs`:

velocity_update_hw_mibs
=======================

.. c:function:: void velocity_update_hw_mibs(struct velocity_info *vptr)

    fetch MIB counters from chip

    :param struct velocity_info \*vptr:
        velocity to update

.. _`velocity_update_hw_mibs.description`:

Description
-----------

The velocity hardware keeps certain counters in the hardware
side. We need to read these when the user asks for statistics
or when they overflow (causing an interrupt). The read of the
statistic clears it, so we keep running master counters in user
space.

.. _`init_flow_control_register`:

init_flow_control_register
==========================

.. c:function:: void init_flow_control_register(struct velocity_info *vptr)

    set up flow control

    :param struct velocity_info \*vptr:
        velocity to configure

.. _`init_flow_control_register.description`:

Description
-----------

Configure the flow control registers for this velocity device.

.. This file was automatic generated / don't edit.

