.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/mpc5xxx_clocks.c

.. _`mpc5xxx_get_bus_frequency`:

mpc5xxx_get_bus_frequency
=========================

.. c:function:: unsigned long mpc5xxx_get_bus_frequency(struct device_node *node)

    Find the bus frequency for a device

    :param node:
        device node
    :type node: struct device_node \*

.. _`mpc5xxx_get_bus_frequency.description`:

Description
-----------

Returns bus frequency (IPS on MPC512x, IPB on MPC52xx),
or 0 if the bus frequency cannot be found.

.. This file was automatic generated / don't edit.

