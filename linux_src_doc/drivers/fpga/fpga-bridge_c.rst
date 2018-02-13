.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/fpga-bridge.c

.. _`fpga_bridge_enable`:

fpga_bridge_enable
==================

.. c:function:: int fpga_bridge_enable(struct fpga_bridge *bridge)

    Enable transactions on the bridge

    :param struct fpga_bridge \*bridge:
        FPGA bridge

.. _`fpga_bridge_enable.return`:

Return
------

0 for success, error code otherwise.

.. _`fpga_bridge_disable`:

fpga_bridge_disable
===================

.. c:function:: int fpga_bridge_disable(struct fpga_bridge *bridge)

    Disable transactions on the bridge

    :param struct fpga_bridge \*bridge:
        FPGA bridge

.. _`fpga_bridge_disable.return`:

Return
------

0 for success, error code otherwise.

.. _`of_fpga_bridge_get`:

of_fpga_bridge_get
==================

.. c:function:: struct fpga_bridge *of_fpga_bridge_get(struct device_node *np, struct fpga_image_info *info)

    get an exclusive reference to a fpga bridge

    :param struct device_node \*np:
        node pointer of a FPGA bridge

    :param struct fpga_image_info \*info:
        fpga image specific information

.. _`of_fpga_bridge_get.description`:

Description
-----------

Return fpga_bridge struct if successful.
Return -EBUSY if someone already has a reference to the bridge.
Return -ENODEV if \ ``np``\  is not a FPGA Bridge.

.. _`fpga_bridge_get`:

fpga_bridge_get
===============

.. c:function:: struct fpga_bridge *fpga_bridge_get(struct device *dev, struct fpga_image_info *info)

    get an exclusive reference to a fpga bridge

    :param struct device \*dev:
        parent device that fpga bridge was registered with

    :param struct fpga_image_info \*info:
        *undescribed*

.. _`fpga_bridge_get.description`:

Description
-----------

Given a device, get an exclusive reference to a fpga bridge.

.. _`fpga_bridge_get.return`:

Return
------

fpga manager struct or \ :c:func:`IS_ERR`\  condition containing error code.

.. _`fpga_bridge_put`:

fpga_bridge_put
===============

.. c:function:: void fpga_bridge_put(struct fpga_bridge *bridge)

    release a reference to a bridge

    :param struct fpga_bridge \*bridge:
        FPGA bridge

.. _`fpga_bridges_enable`:

fpga_bridges_enable
===================

.. c:function:: int fpga_bridges_enable(struct list_head *bridge_list)

    enable bridges in a list

    :param struct list_head \*bridge_list:
        list of FPGA bridges

.. _`fpga_bridges_enable.description`:

Description
-----------

Enable each bridge in the list.  If list is empty, do nothing.

Return 0 for success or empty bridge list; return error code otherwise.

.. _`fpga_bridges_disable`:

fpga_bridges_disable
====================

.. c:function:: int fpga_bridges_disable(struct list_head *bridge_list)

    disable bridges in a list

    :param struct list_head \*bridge_list:
        list of FPGA bridges

.. _`fpga_bridges_disable.description`:

Description
-----------

Disable each bridge in the list.  If list is empty, do nothing.

Return 0 for success or empty bridge list; return error code otherwise.

.. _`fpga_bridges_put`:

fpga_bridges_put
================

.. c:function:: void fpga_bridges_put(struct list_head *bridge_list)

    put bridges

    :param struct list_head \*bridge_list:
        list of FPGA bridges

.. _`fpga_bridges_put.description`:

Description
-----------

For each bridge in the list, put the bridge and remove it from the list.
If list is empty, do nothing.

.. _`of_fpga_bridge_get_to_list`:

of_fpga_bridge_get_to_list
==========================

.. c:function:: int of_fpga_bridge_get_to_list(struct device_node *np, struct fpga_image_info *info, struct list_head *bridge_list)

    get a bridge, add it to a list

    :param struct device_node \*np:
        node pointer of a FPGA bridge

    :param struct fpga_image_info \*info:
        fpga image specific information

    :param struct list_head \*bridge_list:
        list of FPGA bridges

.. _`of_fpga_bridge_get_to_list.description`:

Description
-----------

Get an exclusive reference to the bridge and and it to the list.

Return 0 for success, error code from \ :c:func:`of_fpga_bridge_get`\  othewise.

.. _`fpga_bridge_get_to_list`:

fpga_bridge_get_to_list
=======================

.. c:function:: int fpga_bridge_get_to_list(struct device *dev, struct fpga_image_info *info, struct list_head *bridge_list)

    given device, get a bridge, add it to a list

    :param struct device \*dev:
        FPGA bridge device

    :param struct fpga_image_info \*info:
        fpga image specific information

    :param struct list_head \*bridge_list:
        list of FPGA bridges

.. _`fpga_bridge_get_to_list.description`:

Description
-----------

Get an exclusive reference to the bridge and and it to the list.

Return 0 for success, error code from \ :c:func:`fpga_bridge_get`\  othewise.

.. _`fpga_bridge_register`:

fpga_bridge_register
====================

.. c:function:: int fpga_bridge_register(struct device *dev, const char *name, const struct fpga_bridge_ops *br_ops, void *priv)

    register a fpga bridge driver

    :param struct device \*dev:
        FPGA bridge device from pdev

    :param const char \*name:
        FPGA bridge name

    :param const struct fpga_bridge_ops \*br_ops:
        pointer to structure of fpga bridge ops

    :param void \*priv:
        FPGA bridge private data

.. _`fpga_bridge_register.return`:

Return
------

0 for success, error code otherwise.

.. _`fpga_bridge_unregister`:

fpga_bridge_unregister
======================

.. c:function:: void fpga_bridge_unregister(struct device *dev)

    unregister a fpga bridge driver

    :param struct device \*dev:
        FPGA bridge device from pdev

.. This file was automatic generated / don't edit.

