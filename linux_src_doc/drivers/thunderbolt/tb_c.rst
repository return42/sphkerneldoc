.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/tb.c

.. _`tb_cm`:

struct tb_cm
============

.. c:type:: struct tb_cm

    Simple Thunderbolt connection manager

.. _`tb_cm.definition`:

Definition
----------

.. code-block:: c

    struct tb_cm {
        struct list_head tunnel_list;
        bool hotplug_active;
    }

.. _`tb_cm.members`:

Members
-------

tunnel_list
    List of active tunnels

hotplug_active
    tb_handle_hotplug will stop progressing plug
    events and exit if this is not set (it needs to
    acquire the lock one more time). Used to drain wq
    after cfg has been paused.

.. _`tb_scan_switch`:

tb_scan_switch
==============

.. c:function:: void tb_scan_switch(struct tb_switch *sw)

    scan for and initialize downstream switches

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

.. _`tb_scan_port`:

tb_scan_port
============

.. c:function:: void tb_scan_port(struct tb_port *port)

    check for and initialize switches below port

    :param port:
        *undescribed*
    :type port: struct tb_port \*

.. _`tb_free_invalid_tunnels`:

tb_free_invalid_tunnels
=======================

.. c:function:: void tb_free_invalid_tunnels(struct tb *tb)

    destroy tunnels of devices that have gone away

    :param tb:
        *undescribed*
    :type tb: struct tb \*

.. _`tb_free_unplugged_children`:

tb_free_unplugged_children
==========================

.. c:function:: void tb_free_unplugged_children(struct tb_switch *sw)

    traverse hierarchy and free unplugged switches

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

.. _`tb_find_pci_up_port`:

tb_find_pci_up_port
===================

.. c:function:: struct tb_port *tb_find_pci_up_port(struct tb_switch *sw)

    return the first PCIe up port on \ ``sw``\  or NULL

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

.. _`tb_find_unused_down_port`:

tb_find_unused_down_port
========================

.. c:function:: struct tb_port *tb_find_unused_down_port(struct tb_switch *sw)

    return the first inactive PCIe down port on \ ``sw``\ 

    :param sw:
        *undescribed*
    :type sw: struct tb_switch \*

.. _`tb_activate_pcie_devices`:

tb_activate_pcie_devices
========================

.. c:function:: void tb_activate_pcie_devices(struct tb *tb)

    scan for and activate PCIe devices

    :param tb:
        *undescribed*
    :type tb: struct tb \*

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

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`tb_handle_hotplug.description`:

Description
-----------

Executes on tb->wq.

.. _`tb_handle_event`:

tb_handle_event
===============

.. c:function:: void tb_handle_event(struct tb *tb, enum tb_cfg_pkg_type type, const void *buf, size_t size)

    callback function for the control channel

    :param tb:
        *undescribed*
    :type tb: struct tb \*

    :param type:
        *undescribed*
    :type type: enum tb_cfg_pkg_type

    :param buf:
        *undescribed*
    :type buf: const void \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`tb_handle_event.description`:

Description
-----------

Delegates to tb_handle_hotplug.

.. This file was automatic generated / don't edit.

