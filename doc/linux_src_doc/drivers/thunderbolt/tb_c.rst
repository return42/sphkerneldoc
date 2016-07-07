.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/tb.c

.. _`tb_scan_switch`:

tb_scan_switch
==============

.. c:function:: void tb_scan_switch(struct tb_switch *sw)

    scan for and initialize downstream switches

    :param struct tb_switch \*sw:
        *undescribed*

.. _`tb_scan_port`:

tb_scan_port
============

.. c:function:: void tb_scan_port(struct tb_port *port)

    check for and initialize switches below port

    :param struct tb_port \*port:
        *undescribed*

.. _`tb_free_invalid_tunnels`:

tb_free_invalid_tunnels
=======================

.. c:function:: void tb_free_invalid_tunnels(struct tb *tb)

    destroy tunnels of devices that have gone away

    :param struct tb \*tb:
        *undescribed*

.. _`tb_free_unplugged_children`:

tb_free_unplugged_children
==========================

.. c:function:: void tb_free_unplugged_children(struct tb_switch *sw)

    traverse hierarchy and free unplugged switches

    :param struct tb_switch \*sw:
        *undescribed*

.. _`tb_find_pci_up_port`:

tb_find_pci_up_port
===================

.. c:function:: struct tb_port *tb_find_pci_up_port(struct tb_switch *sw)

    return the first PCIe up port on \ ``sw``\  or NULL

    :param struct tb_switch \*sw:
        *undescribed*

.. _`tb_find_unused_down_port`:

tb_find_unused_down_port
========================

.. c:function:: struct tb_port *tb_find_unused_down_port(struct tb_switch *sw)

    return the first inactive PCIe down port on \ ``sw``\ 

    :param struct tb_switch \*sw:
        *undescribed*

.. _`tb_activate_pcie_devices`:

tb_activate_pcie_devices
========================

.. c:function:: void tb_activate_pcie_devices(struct tb *tb)

    scan for and activate PCIe devices

    :param struct tb \*tb:
        *undescribed*

.. _`tb_activate_pcie_devices.description`:

Description
-----------

This method is somewhat ad hoc. For now it only supports one device
per port and only devices at depth 1.

.. _`tb_handle_hotplug`:

tb_handle_hotplug
=================

.. c:function:: void tb_handle_hotplug(struct work_struct *work)

    handle hotplug event

    :param struct work_struct \*work:
        *undescribed*

.. _`tb_handle_hotplug.description`:

Description
-----------

Executes on tb->wq.

.. _`tb_schedule_hotplug_handler`:

tb_schedule_hotplug_handler
===========================

.. c:function:: void tb_schedule_hotplug_handler(void *data, u64 route, u8 port, bool unplug)

    callback function for the control channel

    :param void \*data:
        *undescribed*

    :param u64 route:
        *undescribed*

    :param u8 port:
        *undescribed*

    :param bool unplug:
        *undescribed*

.. _`tb_schedule_hotplug_handler.description`:

Description
-----------

Delegates to tb_handle_hotplug.

.. _`thunderbolt_shutdown_and_free`:

thunderbolt_shutdown_and_free
=============================

.. c:function:: void thunderbolt_shutdown_and_free(struct tb *tb)

    shutdown everything

    :param struct tb \*tb:
        *undescribed*

.. _`thunderbolt_shutdown_and_free.description`:

Description
-----------

Free all switches and the config channel.

Used in the error path of thunderbolt_alloc_and_start.

.. _`thunderbolt_alloc_and_start`:

thunderbolt_alloc_and_start
===========================

.. c:function:: struct tb *thunderbolt_alloc_and_start(struct tb_nhi *nhi)

    setup the thunderbolt bus

    :param struct tb_nhi \*nhi:
        *undescribed*

.. _`thunderbolt_alloc_and_start.description`:

Description
-----------

Allocates a tb_cfg control channel, initializes the root switch, enables
plug events and activates pci devices.

.. _`thunderbolt_alloc_and_start.return`:

Return
------

Returns NULL on error.

.. This file was automatic generated / don't edit.

