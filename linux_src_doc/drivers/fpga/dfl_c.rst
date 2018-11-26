.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/dfl.c

.. _`dfl_fpga_port_ops_get`:

dfl_fpga_port_ops_get
=====================

.. c:function:: struct dfl_fpga_port_ops *dfl_fpga_port_ops_get(struct platform_device *pdev)

    get matched port ops from the global list

    :param pdev:
        platform device to match with associated port ops.
    :type pdev: struct platform_device \*

.. _`dfl_fpga_port_ops_get.return`:

Return
------

matched port ops on success, NULL otherwise.

Please note that must dfl_fpga_port_ops_put after use the port_ops.

.. _`dfl_fpga_port_ops_put`:

dfl_fpga_port_ops_put
=====================

.. c:function:: void dfl_fpga_port_ops_put(struct dfl_fpga_port_ops *ops)

    put port ops

    :param ops:
        port ops.
    :type ops: struct dfl_fpga_port_ops \*

.. _`dfl_fpga_port_ops_add`:

dfl_fpga_port_ops_add
=====================

.. c:function:: void dfl_fpga_port_ops_add(struct dfl_fpga_port_ops *ops)

    add port_ops to global list

    :param ops:
        port ops to add.
    :type ops: struct dfl_fpga_port_ops \*

.. _`dfl_fpga_port_ops_del`:

dfl_fpga_port_ops_del
=====================

.. c:function:: void dfl_fpga_port_ops_del(struct dfl_fpga_port_ops *ops)

    remove port_ops from global list

    :param ops:
        port ops to del.
    :type ops: struct dfl_fpga_port_ops \*

.. _`dfl_fpga_check_port_id`:

dfl_fpga_check_port_id
======================

.. c:function:: int dfl_fpga_check_port_id(struct platform_device *pdev, void *pport_id)

    check the port id

    :param pdev:
        port platform device.
    :type pdev: struct platform_device \*

    :param pport_id:
        port id to compare.
    :type pport_id: void \*

.. _`dfl_fpga_check_port_id.return`:

Return
------

1 if port device matches with given port id, otherwise 0.

.. _`dfl_fpga_dev_feature_uinit`:

dfl_fpga_dev_feature_uinit
==========================

.. c:function:: void dfl_fpga_dev_feature_uinit(struct platform_device *pdev)

    uinit for sub features of dfl feature device

    :param pdev:
        feature device.
    :type pdev: struct platform_device \*

.. _`dfl_fpga_dev_feature_init`:

dfl_fpga_dev_feature_init
=========================

.. c:function:: int dfl_fpga_dev_feature_init(struct platform_device *pdev, struct dfl_feature_driver *feature_drvs)

    init for sub features of dfl feature device

    :param pdev:
        feature device.
    :type pdev: struct platform_device \*

    :param feature_drvs:
        drvs for sub features.
    :type feature_drvs: struct dfl_feature_driver \*

.. _`dfl_fpga_dev_feature_init.description`:

Description
-----------

This function will match sub features with given feature drvs list and
use matched drv to init related sub feature.

.. _`dfl_fpga_dev_feature_init.return`:

Return
------

0 on success, negative error code otherwise.

.. _`dfl_fpga_dev_ops_register`:

dfl_fpga_dev_ops_register
=========================

.. c:function:: int dfl_fpga_dev_ops_register(struct platform_device *pdev, const struct file_operations *fops, struct module *owner)

    register cdev ops for feature dev

    :param pdev:
        feature dev.
    :type pdev: struct platform_device \*

    :param fops:
        file operations for feature dev's cdev.
    :type fops: const struct file_operations \*

    :param owner:
        owning module/driver.
    :type owner: struct module \*

.. _`dfl_fpga_dev_ops_register.return`:

Return
------

0 on success, negative error code otherwise.

.. _`dfl_fpga_dev_ops_unregister`:

dfl_fpga_dev_ops_unregister
===========================

.. c:function:: void dfl_fpga_dev_ops_unregister(struct platform_device *pdev)

    unregister cdev ops for feature dev

    :param pdev:
        feature dev.
    :type pdev: struct platform_device \*

.. _`build_feature_devs_info`:

struct build_feature_devs_info
==============================

.. c:type:: struct build_feature_devs_info

    info collected during feature dev build.

.. _`build_feature_devs_info.definition`:

Definition
----------

.. code-block:: c

    struct build_feature_devs_info {
        struct device *dev;
        struct dfl_fpga_cdev *cdev;
        struct platform_device *feature_dev;
        void __iomem *ioaddr;
        struct list_head sub_features;
        int feature_num;
    }

.. _`build_feature_devs_info.members`:

Members
-------

dev
    device to enumerate.

cdev
    the container device for all feature devices.

feature_dev
    current feature device.

ioaddr
    header register region address of feature device in enumeration.

sub_features
    a sub features linked list for feature device in enumeration.

feature_num
    number of sub features for feature device in enumeration.

.. _`dfl_feature_info`:

struct dfl_feature_info
=======================

.. c:type:: struct dfl_feature_info

    sub feature info collected during feature dev build

.. _`dfl_feature_info.definition`:

Definition
----------

.. code-block:: c

    struct dfl_feature_info {
        u64 fid;
        struct resource mmio_res;
        void __iomem *ioaddr;
        struct list_head node;
    }

.. _`dfl_feature_info.members`:

Members
-------

fid
    id of this sub feature.

mmio_res
    mmio resource of this sub feature.

ioaddr
    mapped base address of mmio resource.

node
    node in sub_features linked list.

.. _`parse_feature`:

parse_feature
=============

.. c:function:: int parse_feature(struct build_feature_devs_info *binfo, struct dfl_fpga_enum_dfl *dfl, resource_size_t ofst)

    parse a feature on given device feature list

    :param binfo:
        build feature devices information.
    :type binfo: struct build_feature_devs_info \*

    :param dfl:
        device feature list to parse
    :type dfl: struct dfl_fpga_enum_dfl \*

    :param ofst:
        offset to feature header on this device feature list
    :type ofst: resource_size_t

.. _`dfl_fpga_enum_info_add_dfl`:

dfl_fpga_enum_info_add_dfl
==========================

.. c:function:: int dfl_fpga_enum_info_add_dfl(struct dfl_fpga_enum_info *info, resource_size_t start, resource_size_t len, void __iomem *ioaddr)

    add info of a device feature list to enum info

    :param info:
        ptr to dfl_fpga_enum_info
    :type info: struct dfl_fpga_enum_info \*

    :param start:
        mmio resource address of the device feature list.
    :type start: resource_size_t

    :param len:
        mmio resource length of the device feature list.
    :type len: resource_size_t

    :param ioaddr:
        mapped mmio resource address of the device feature list.
    :type ioaddr: void __iomem \*

.. _`dfl_fpga_enum_info_add_dfl.description`:

Description
-----------

One FPGA device may have one or more Device Feature Lists (DFLs), use this
function to add information of each DFL to common data structure for next
step enumeration.

.. _`dfl_fpga_enum_info_add_dfl.return`:

Return
------

0 on success, negative error code otherwise.

.. _`dfl_fpga_feature_devs_enumerate`:

dfl_fpga_feature_devs_enumerate
===============================

.. c:function:: struct dfl_fpga_cdev *dfl_fpga_feature_devs_enumerate(struct dfl_fpga_enum_info *info)

    enumerate feature devices

    :param info:
        information for enumeration.
    :type info: struct dfl_fpga_enum_info \*

.. _`dfl_fpga_feature_devs_enumerate.description`:

Description
-----------

This function creates a container device (base FPGA region), enumerates
feature devices based on the enumeration info and creates platform devices
under the container device.

.. _`dfl_fpga_feature_devs_enumerate.return`:

Return
------

dfl_fpga_cdev struct on success, -errno on failure

.. _`dfl_fpga_feature_devs_remove`:

dfl_fpga_feature_devs_remove
============================

.. c:function:: void dfl_fpga_feature_devs_remove(struct dfl_fpga_cdev *cdev)

    remove all feature devices

    :param cdev:
        fpga container device.
    :type cdev: struct dfl_fpga_cdev \*

.. _`dfl_fpga_feature_devs_remove.description`:

Description
-----------

Remove the container device and all feature devices under given container
devices.

.. _`__dfl_fpga_cdev_find_port`:

\__dfl_fpga_cdev_find_port
==========================

.. c:function:: struct platform_device *__dfl_fpga_cdev_find_port(struct dfl_fpga_cdev *cdev, void *data, int (*match)(struct platform_device *, void *))

    find a port under given container device

    :param cdev:
        container device
    :type cdev: struct dfl_fpga_cdev \*

    :param data:
        data passed to match function
    :type data: void \*

    :param int (\*match)(struct platform_device \*, void \*):
        match function used to find specific port from the port device list

.. _`__dfl_fpga_cdev_find_port.description`:

Description
-----------

Find a port device under container device. This function needs to be
invoked with lock held.

.. _`__dfl_fpga_cdev_find_port.return`:

Return
------

pointer to port's platform device if successful, NULL otherwise.

.. _`__dfl_fpga_cdev_find_port.note`:

NOTE
----

you will need to drop the device reference with \ :c:func:`put_device`\  after use.

.. This file was automatic generated / don't edit.

