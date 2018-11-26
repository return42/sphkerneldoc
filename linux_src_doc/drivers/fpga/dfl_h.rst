.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/dfl.h

.. _`dfl_fpga_port_ops`:

struct dfl_fpga_port_ops
========================

.. c:type:: struct dfl_fpga_port_ops

    port ops

.. _`dfl_fpga_port_ops.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fpga_port_ops {
        const char *name;
        struct module *owner;
        struct list_head node;
        int (*get_id)(struct platform_device *pdev);
        int (*enable_set)(struct platform_device *pdev, bool enable);
    }

.. _`dfl_fpga_port_ops.members`:

Members
-------

name
    name of this port ops, to match with port platform device.

owner
    pointer to the module which owns this port ops.

node
    node to link port ops to global list.

get_id
    get port id from hardware.

enable_set
    enable/disable the port.

.. _`dfl_feature_driver`:

struct dfl_feature_driver
=========================

.. c:type:: struct dfl_feature_driver

    sub feature's driver

.. _`dfl_feature_driver.definition`:

Definition
----------

.. code-block:: c

    struct dfl_feature_driver {
        u64 id;
        const struct dfl_feature_ops *ops;
    }

.. _`dfl_feature_driver.members`:

Members
-------

id
    sub feature id.

ops
    ops of this sub feature.

.. _`dfl_feature`:

struct dfl_feature
==================

.. c:type:: struct dfl_feature

    sub feature of the feature devices

.. _`dfl_feature.definition`:

Definition
----------

.. code-block:: c

    struct dfl_feature {
        u64 id;
        int resource_index;
        void __iomem *ioaddr;
        const struct dfl_feature_ops *ops;
    }

.. _`dfl_feature.members`:

Members
-------

id
    sub feature id.

resource_index
    each sub feature has one mmio resource for its registers.
    this index is used to find its mmio resource from the
    feature dev (platform device)'s reources.

ioaddr
    mapped mmio resource address.

ops
    ops of this sub feature.

.. _`dfl_feature_platform_data`:

struct dfl_feature_platform_data
================================

.. c:type:: struct dfl_feature_platform_data

    platform data for feature devices

.. _`dfl_feature_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct dfl_feature_platform_data {
        struct list_head node;
        struct mutex lock;
        struct cdev cdev;
        struct platform_device *dev;
        struct dfl_fpga_cdev *dfl_cdev;
        unsigned int disable_count;
        unsigned long dev_status;
        void *private;
        int num;
        struct dfl_feature features[0];
    }

.. _`dfl_feature_platform_data.members`:

Members
-------

node
    node to link feature devs to container device's port_dev_list.

lock
    mutex to protect platform data.

cdev
    cdev of feature dev.

dev
    ptr to platform device linked with this platform data.

dfl_cdev
    ptr to container device.

disable_count
    count for port disable.

dev_status
    dev status (e.g. DEV_STATUS_IN_USE).

private
    ptr to feature dev private data.

num
    number for sub features.

features
    sub features of this feature dev.

.. _`dfl_fpga_enum_info`:

struct dfl_fpga_enum_info
=========================

.. c:type:: struct dfl_fpga_enum_info

    DFL FPGA enumeration information

.. _`dfl_fpga_enum_info.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fpga_enum_info {
        struct device *dev;
        struct list_head dfls;
    }

.. _`dfl_fpga_enum_info.members`:

Members
-------

dev
    parent device.

dfls
    list of device feature lists.

.. _`dfl_fpga_enum_dfl`:

struct dfl_fpga_enum_dfl
========================

.. c:type:: struct dfl_fpga_enum_dfl

    DFL FPGA enumeration device feature list info

.. _`dfl_fpga_enum_dfl.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fpga_enum_dfl {
        resource_size_t start;
        resource_size_t len;
        void __iomem *ioaddr;
        struct list_head node;
    }

.. _`dfl_fpga_enum_dfl.members`:

Members
-------

start
    base address of this device feature list.

len
    size of this device feature list.

ioaddr
    mapped base address of this device feature list.

node
    node in list of device feature lists.

.. _`dfl_fpga_cdev`:

struct dfl_fpga_cdev
====================

.. c:type:: struct dfl_fpga_cdev

    container device of DFL based FPGA

.. _`dfl_fpga_cdev.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fpga_cdev {
        struct device *parent;
        struct fpga_region *region;
        struct device *fme_dev;
        struct mutex lock;
        struct list_head port_dev_list;
    }

.. _`dfl_fpga_cdev.members`:

Members
-------

parent
    parent device of this container device.

region
    base fpga region.

fme_dev
    FME feature device under this container device.

lock
    mutex lock to protect the port device list.

port_dev_list
    list of all port feature devices under this container device.

.. This file was automatic generated / don't edit.

