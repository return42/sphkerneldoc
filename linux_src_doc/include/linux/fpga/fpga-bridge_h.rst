.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fpga/fpga-bridge.h

.. _`fpga_bridge_ops`:

struct fpga_bridge_ops
======================

.. c:type:: struct fpga_bridge_ops

    ops for low level FPGA bridge drivers

.. _`fpga_bridge_ops.definition`:

Definition
----------

.. code-block:: c

    struct fpga_bridge_ops {
        int (*enable_show)(struct fpga_bridge *bridge);
        int (*enable_set)(struct fpga_bridge *bridge, bool enable);
        void (*fpga_bridge_remove)(struct fpga_bridge *bridge);
    }

.. _`fpga_bridge_ops.members`:

Members
-------

enable_show
    returns the FPGA bridge's status

enable_set
    set a FPGA bridge as enabled or disabled

fpga_bridge_remove
    set FPGA into a specific state during driver remove

.. _`fpga_bridge`:

struct fpga_bridge
==================

.. c:type:: struct fpga_bridge

    FPGA bridge structure

.. _`fpga_bridge.definition`:

Definition
----------

.. code-block:: c

    struct fpga_bridge {
        const char *name;
        struct device dev;
        struct mutex mutex;
        const struct fpga_bridge_ops *br_ops;
        struct fpga_image_info *info;
        struct list_head node;
        void *priv;
    }

.. _`fpga_bridge.members`:

Members
-------

name
    name of low level FPGA bridge

dev
    FPGA bridge device

mutex
    enforces exclusive reference to bridge

br_ops
    pointer to struct of FPGA bridge ops

info
    fpga image specific information

node
    FPGA bridge list node

priv
    low level driver private date

.. This file was automatic generated / don't edit.

