.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/omap_l3_noc.h

.. _`l3_masters_data`:

struct l3_masters_data
======================

.. c:type:: struct l3_masters_data

    L3 Master information

.. _`l3_masters_data.definition`:

Definition
----------

.. code-block:: c

    struct l3_masters_data {
        u32 id;
        char *name;
    }

.. _`l3_masters_data.members`:

Members
-------

id
    ID of the L3 Master

name
    master name

.. _`l3_target_data`:

struct l3_target_data
=====================

.. c:type:: struct l3_target_data

    L3 Target information

.. _`l3_target_data.definition`:

Definition
----------

.. code-block:: c

    struct l3_target_data {
        u32 offset;
        char *name;
    }

.. _`l3_target_data.members`:

Members
-------

offset
    Offset from base for L3 Target

name
    Target name

.. _`l3_target_data.description`:

Description
-----------

Target information is organized indexed by bit field definitions.

.. _`l3_flagmux_data`:

struct l3_flagmux_data
======================

.. c:type:: struct l3_flagmux_data

    Flag Mux information

.. _`l3_flagmux_data.definition`:

Definition
----------

.. code-block:: c

    struct l3_flagmux_data {
        u32 offset;
        struct l3_target_data *l3_targ;
        u8 num_targ_data;
        u32 mask_app_bits;
        u32 mask_dbg_bits;
    }

.. _`l3_flagmux_data.members`:

Members
-------

offset
    offset from base for flagmux register

l3_targ
    array indexed by flagmux index (bit offset) pointing to the
    target data. unsupported ones are marked with
    L3_TARGET_NOT_SUPPORTED

num_targ_data
    number of entries in target data

mask_app_bits
    ignore these from raw application irq status

mask_dbg_bits
    ignore these from raw debug irq status

.. _`omap_l3`:

struct omap_l3
==============

.. c:type:: struct omap_l3

    Description of data relevant for L3 bus.

.. _`omap_l3.definition`:

Definition
----------

.. code-block:: c

    struct omap_l3 {
        struct device *dev;
        void __iomem  *l3_base[MAX_L3_MODULES];
        struct l3_flagmux_data **l3_flagmux;
        int num_modules;
        struct l3_masters_data *l3_masters;
        int num_masters;
        u32 mst_addr_mask;
        int debug_irq;
        int app_irq;
    }

.. _`omap_l3.members`:

Members
-------

dev
    device representing the bus (populated runtime)

l3_base
    base addresses of modules (populated runtime if 0)
    if set to L3_BASE_IS_SUBMODULE, then uses previous
    module index as the base address

l3_flagmux
    *undescribed*

num_modules
    number of clock domains / modules.

l3_masters
    array pointing to master data containing name and register
    offset for the master.

num_masters
    *undescribed*

mst_addr_mask
    Mask representing MSTADDR information of NTTP packet

debug_irq
    irq number of the debug interrupt (populated runtime)

app_irq
    irq number of the application interrupt (populated runtime)

.. This file was automatic generated / don't edit.

