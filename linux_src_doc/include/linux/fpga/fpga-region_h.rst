.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fpga/fpga-region.h

.. _`fpga_region`:

struct fpga_region
==================

.. c:type:: struct fpga_region

    FPGA Region structure

.. _`fpga_region.definition`:

Definition
----------

.. code-block:: c

    struct fpga_region {
        struct device dev;
        struct mutex mutex;
        struct list_head bridge_list;
        struct fpga_manager *mgr;
        struct fpga_image_info *info;
        void *priv;
        int (*get_bridges)(struct fpga_region *region);
        const struct attribute_group **groups;
    }

.. _`fpga_region.members`:

Members
-------

dev
    FPGA Region device

mutex
    enforces exclusive reference to region

bridge_list
    list of FPGA bridges specified in region

mgr
    FPGA manager

info
    FPGA image info

priv
    private data

get_bridges
    optional function to get bridges to a list

groups
    optional attribute groups.

.. This file was automatic generated / don't edit.

