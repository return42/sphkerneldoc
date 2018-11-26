.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/dfl-fme-pr.h

.. _`dfl_fme_region`:

struct dfl_fme_region
=====================

.. c:type:: struct dfl_fme_region

    FME fpga region data structure

.. _`dfl_fme_region.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fme_region {
        struct platform_device *region;
        struct list_head node;
        int port_id;
    }

.. _`dfl_fme_region.members`:

Members
-------

region
    platform device of the FPGA region.

node
    used to link fme_region to a list.

port_id
    indicate which port this region connected to.

.. _`dfl_fme_region_pdata`:

struct dfl_fme_region_pdata
===========================

.. c:type:: struct dfl_fme_region_pdata

    platform data for FME region platform device.

.. _`dfl_fme_region_pdata.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fme_region_pdata {
        struct platform_device *mgr;
        struct platform_device *br;
        int region_id;
    }

.. _`dfl_fme_region_pdata.members`:

Members
-------

mgr
    platform device of the FPGA manager.

br
    platform device of the FPGA bridge.

region_id
    region id (same as port_id).

.. _`dfl_fme_bridge`:

struct dfl_fme_bridge
=====================

.. c:type:: struct dfl_fme_bridge

    FME fpga bridge data structure

.. _`dfl_fme_bridge.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fme_bridge {
        struct platform_device *br;
        struct list_head node;
    }

.. _`dfl_fme_bridge.members`:

Members
-------

br
    platform device of the FPGA bridge.

node
    used to link fme_bridge to a list.

.. _`dfl_fme_br_pdata`:

struct dfl_fme_br_pdata
=======================

.. c:type:: struct dfl_fme_br_pdata

    platform data for FME bridge platform device.

.. _`dfl_fme_br_pdata.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fme_br_pdata {
        struct dfl_fpga_cdev *cdev;
        int port_id;
    }

.. _`dfl_fme_br_pdata.members`:

Members
-------

cdev
    container device.

port_id
    port id.

.. _`dfl_fme_mgr_pdata`:

struct dfl_fme_mgr_pdata
========================

.. c:type:: struct dfl_fme_mgr_pdata

    platform data for FME manager platform device.

.. _`dfl_fme_mgr_pdata.definition`:

Definition
----------

.. code-block:: c

    struct dfl_fme_mgr_pdata {
        void __iomem *ioaddr;
    }

.. _`dfl_fme_mgr_pdata.members`:

Members
-------

ioaddr
    mapped io address for FME manager platform device.

.. This file was automatic generated / don't edit.

