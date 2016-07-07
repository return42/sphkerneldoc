.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/ps3.h

.. _`ps3_dma_region`:

struct ps3_dma_region
=====================

.. c:type:: struct ps3_dma_region

    A per device dma state variables structure

.. _`ps3_dma_region.definition`:

Definition
----------

.. code-block:: c

    struct ps3_dma_region {
        struct ps3_system_bus_device *dev;
        const struct ps3_dma_region_ops *region_ops;
        unsigned char ioid;
        enum ps3_dma_page_size page_size;
        enum ps3_dma_region_type region_type;
        unsigned long len;
        unsigned long offset;
        unsigned long bus_addr;
        struct chunk_list;
    }

.. _`ps3_dma_region.members`:

Members
-------

dev
    *undescribed*

region_ops
    struct ps3_dma_region_ops - dma region operations

ioid
    The IOID of the device who owns this region

page_size
    The ioc pagesize.

region_type
    The HV region type.

len
    The length in bytes of the region.

offset
    The offset from the start of memory of the region.

bus_addr
    The 'translated' bus address of the region.

chunk_list
    Opaque variable used by the ioc page manager.

.. _`ps3_mmio_region`:

struct ps3_mmio_region
======================

.. c:type:: struct ps3_mmio_region

    a per device mmio state variables structure

.. _`ps3_mmio_region.definition`:

Definition
----------

.. code-block:: c

    struct ps3_mmio_region {
        struct ps3_system_bus_device *dev;
        const struct ps3_mmio_region_ops *mmio_ops;
        unsigned long bus_addr;
        unsigned long len;
        enum ps3_mmio_page_size page_size;
        unsigned long lpar_addr;
    }

.. _`ps3_mmio_region.members`:

Members
-------

dev
    *undescribed*

mmio_ops
    *undescribed*

bus_addr
    *undescribed*

len
    *undescribed*

page_size
    *undescribed*

lpar_addr
    *undescribed*

.. _`ps3_mmio_region.description`:

Description
-----------

Current systems can be supported with a single region per device.

.. _`ps3_system_bus_device`:

struct ps3_system_bus_device
============================

.. c:type:: struct ps3_system_bus_device

    a device on the system bus

.. _`ps3_system_bus_device.definition`:

Definition
----------

.. code-block:: c

    struct ps3_system_bus_device {
        enum ps3_match_id match_id;
        enum ps3_match_sub_id match_sub_id;
        enum ps3_system_bus_device_type dev_type;
        u64 bus_id;
        u64 dev_id;
        unsigned int interrupt_id;
        struct ps3_dma_region *d_region;
        struct ps3_mmio_region *m_region;
        unsigned int port_number;
        struct lpm;
        struct device core;
        void *driver_priv;
    }

.. _`ps3_system_bus_device.members`:

Members
-------

match_id
    *undescribed*

match_sub_id
    *undescribed*

dev_type
    *undescribed*

bus_id
    *undescribed*

dev_id
    *undescribed*

interrupt_id
    *undescribed*

d_region
    *undescribed*

m_region
    *undescribed*

port_number
    *undescribed*

lpm
    *undescribed*

core
    *undescribed*

driver_priv
    *undescribed*

.. _`ps3_system_bus_driver`:

struct ps3_system_bus_driver
============================

.. c:type:: struct ps3_system_bus_driver

    a driver for a device on the system bus

.. _`ps3_system_bus_driver.definition`:

Definition
----------

.. code-block:: c

    struct ps3_system_bus_driver {
        enum ps3_match_id match_id;
        enum ps3_match_sub_id match_sub_id;
        struct device_driver core;
        int (* probe) (struct ps3_system_bus_device *);
        int (* remove) (struct ps3_system_bus_device *);
        int (* shutdown) (struct ps3_system_bus_device *);
    }

.. _`ps3_system_bus_driver.members`:

Members
-------

match_id
    *undescribed*

match_sub_id
    *undescribed*

core
    *undescribed*

probe
    *undescribed*

remove
    *undescribed*

shutdown
    *undescribed*

.. _`ps3_system_bus_set_drvdata`:

ps3_system_bus_set_drvdata
==========================

.. c:function:: void ps3_system_bus_set_drvdata(struct ps3_system_bus_device *dev, void *data)

    :param struct ps3_system_bus_device \*dev:
        device structure

    :param void \*data:
        Data to set

.. _`ps3_lpm_rights`:

enum ps3_lpm_rights
===================

.. c:type:: enum ps3_lpm_rights

    Rigths granted by the system policy module.

.. _`ps3_lpm_rights.definition`:

Definition
----------

.. code-block:: c

    enum ps3_lpm_rights {
        PS3_LPM_RIGHTS_USE_LPM,
        PS3_LPM_RIGHTS_USE_TB
    };

.. _`ps3_lpm_rights.constants`:

Constants
---------

PS3_LPM_RIGHTS_USE_LPM
    The right to use the lpm.

PS3_LPM_RIGHTS_USE_TB
    The right to use the internal trace buffer.

.. _`ps3_lpm_tb_type`:

enum ps3_lpm_tb_type
====================

.. c:type:: enum ps3_lpm_tb_type

    Type of trace buffer lv1 should use.

.. _`ps3_lpm_tb_type.definition`:

Definition
----------

.. code-block:: c

    enum ps3_lpm_tb_type {
        PS3_LPM_TB_TYPE_NONE,
        PS3_LPM_TB_TYPE_INTERNAL
    };

.. _`ps3_lpm_tb_type.constants`:

Constants
---------

PS3_LPM_TB_TYPE_NONE
    Do not use a trace buffer.

PS3_LPM_TB_TYPE_INTERNAL
    *undescribed*

.. This file was automatic generated / don't edit.

