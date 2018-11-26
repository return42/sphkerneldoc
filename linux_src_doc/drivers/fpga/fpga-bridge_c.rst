.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/fpga-bridge.c

.. _`fpga_bridge_enable`:

fpga_bridge_enable
==================

.. c:function:: int fpga_bridge_enable(struct fpga_bridge *bridge)

    Enable transactions on the bridge

    :param bridge:
        FPGA bridge
    :type bridge: struct fpga_bridge \*

.. _`fpga_bridge_enable.return`:

Return
------

0 for success, error code otherwise.

.. _`fpga_bridge_disable`:

fpga_bridge_disable
===================

.. c:function:: int fpga_bridge_disable(struct fpga_bridge *bridge)

    Disable transactions on the bridge

    :param bridge:
        FPGA bridge
    :type bridge: struct fpga_bridge \*

.. _`fpga_bridge_disable.return`:

Return
------

0 for success, error code otherwise.

.. _`of_fpga_bridge_get`:

of_fpga_bridge_get
==================

.. c:function:: struct fpga_bridge *of_fpga_bridge_get(struct device_node *np, struct fpga_image_info *info)

    get an exclusive reference to a fpga bridge

    :param np:
        node pointer of a FPGA bridge
    :type np: struct device_node \*

    :param info:
        fpga image specific information
    :type info: struct fpga_image_info \*

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

    :param dev:
        parent device that fpga bridge was registered with
    :type dev: struct device \*

    :param info:
        fpga manager info
    :type info: struct fpga_image_info \*

.. _`fpga_bridge_get.description`:

Description
-----------

Given a device, get an exclusive reference to a fpga bridge.

.. _`fpga_bridge_get.return`:

Return
------

fpga bridge struct or \ :c:func:`IS_ERR`\  condition containing error code.

.. _`fpga_bridge_put`:

fpga_bridge_put
===============

.. c:function:: void fpga_bridge_put(struct fpga_bridge *bridge)

    release a reference to a bridge

    :param bridge:
        FPGA bridge
    :type bridge: struct fpga_bridge \*

.. _`fpga_bridges_enable`:

fpga_bridges_enable
===================

.. c:function:: int fpga_bridges_enable(struct list_head *bridge_list)

    enable bridges in a list

    :param bridge_list:
        list of FPGA bridges
    :type bridge_list: struct list_head \*

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

    :param bridge_list:
        list of FPGA bridges
    :type bridge_list: struct list_head \*

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

    :param bridge_list:
        list of FPGA bridges
    :type bridge_list: struct list_head \*

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

    :param np:
        node pointer of a FPGA bridge
    :type np: struct device_node \*

    :param info:
        fpga image specific information
    :type info: struct fpga_image_info \*

    :param bridge_list:
        list of FPGA bridges
    :type bridge_list: struct list_head \*

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

    :param dev:
        FPGA bridge device
    :type dev: struct device \*

    :param info:
        fpga image specific information
    :type info: struct fpga_image_info \*

    :param bridge_list:
        list of FPGA bridges
    :type bridge_list: struct list_head \*

.. _`fpga_bridge_get_to_list.description`:

Description
-----------

Get an exclusive reference to the bridge and and it to the list.

Return 0 for success, error code from \ :c:func:`fpga_bridge_get`\  othewise.

.. _`fpga_bridge_create`:

fpga_bridge_create
==================

.. c:function:: struct fpga_bridge *fpga_bridge_create(struct device *dev, const char *name, const struct fpga_bridge_ops *br_ops, void *priv)

    create and initialize a struct fpga_bridge

    :param dev:
        FPGA bridge device from pdev
    :type dev: struct device \*

    :param name:
        FPGA bridge name
    :type name: const char \*

    :param br_ops:
        pointer to structure of fpga bridge ops
    :type br_ops: const struct fpga_bridge_ops \*

    :param priv:
        FPGA bridge private data
    :type priv: void \*

.. _`fpga_bridge_create.description`:

Description
-----------

The caller of this function is responsible for freeing the bridge with
\ :c:func:`fpga_bridge_free`\ .  Using \ :c:func:`devm_fpga_bridge_create`\  instead is recommended.

.. _`fpga_bridge_create.return`:

Return
------

struct fpga_bridge or NULL

.. _`fpga_bridge_free`:

fpga_bridge_free
================

.. c:function:: void fpga_bridge_free(struct fpga_bridge *bridge)

    free a fpga bridge created by \ :c:func:`fpga_bridge_create`\ 

    :param bridge:
        FPGA bridge struct
    :type bridge: struct fpga_bridge \*

.. _`devm_fpga_bridge_create`:

devm_fpga_bridge_create
=======================

.. c:function:: struct fpga_bridge *devm_fpga_bridge_create(struct device *dev, const char *name, const struct fpga_bridge_ops *br_ops, void *priv)

    create and init a managed struct fpga_bridge

    :param dev:
        FPGA bridge device from pdev
    :type dev: struct device \*

    :param name:
        FPGA bridge name
    :type name: const char \*

    :param br_ops:
        pointer to structure of fpga bridge ops
    :type br_ops: const struct fpga_bridge_ops \*

    :param priv:
        FPGA bridge private data
    :type priv: void \*

.. _`devm_fpga_bridge_create.description`:

Description
-----------

This function is intended for use in a FPGA bridge driver's probe function.
After the bridge driver creates the struct with \ :c:func:`devm_fpga_bridge_create`\ , it
should register the bridge with \ :c:func:`fpga_bridge_register`\ .  The bridge driver's
remove function should call \ :c:func:`fpga_bridge_unregister`\ .  The bridge struct
allocated with this function will be freed automatically on driver detach.
This includes the case of a probe function returning error before calling
\ :c:func:`fpga_bridge_register`\ , the struct will still get cleaned up.

.. _`devm_fpga_bridge_create.return`:

Return
------

struct fpga_bridge or NULL

.. _`fpga_bridge_register`:

fpga_bridge_register
====================

.. c:function:: int fpga_bridge_register(struct fpga_bridge *bridge)

    register a FPGA bridge

    :param bridge:
        FPGA bridge struct
    :type bridge: struct fpga_bridge \*

.. _`fpga_bridge_register.return`:

Return
------

0 for success, error code otherwise.

.. _`fpga_bridge_unregister`:

fpga_bridge_unregister
======================

.. c:function:: void fpga_bridge_unregister(struct fpga_bridge *bridge)

    unregister a FPGA bridge

    :param bridge:
        FPGA bridge struct
    :type bridge: struct fpga_bridge \*

.. _`fpga_bridge_unregister.description`:

Description
-----------

This function is intended for use in a FPGA bridge driver's remove function.

.. This file was automatic generated / don't edit.

