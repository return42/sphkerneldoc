.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/intel-mid.h

.. _`mid_sd_board_info`:

struct mid_sd_board_info
========================

.. c:type:: struct mid_sd_board_info

    template for SD device creation

.. _`mid_sd_board_info.definition`:

Definition
----------

.. code-block:: c

    struct mid_sd_board_info {
        char name;
        int bus_num;
        unsigned short addr;
        u32 max_clk;
        void *platform_data;
    }

.. _`mid_sd_board_info.members`:

Members
-------

name
    identifies the driver

bus_num
    board-specific identifier for a given SD controller

addr
    *undescribed*

max_clk
    the maximum frequency device supports

platform_data
    the particular data stored there is driver-specific

.. _`intel_mid_ops`:

struct intel_mid_ops
====================

.. c:type:: struct intel_mid_ops

    Interface between intel-mid & sub archs

.. _`intel_mid_ops.definition`:

Definition
----------

.. code-block:: c

    struct intel_mid_ops {
        void (*arch_setup)(void);
    }

.. _`intel_mid_ops.members`:

Members
-------

arch_setup
    arch_setup function to re-initialize platform
    structures (x86_init, x86_platform_init)

.. _`intel_mid_ops.description`:

Description
-----------

This structure can be extended if any new interface is required
between intel-mid & its sub arch files.

.. This file was automatic generated / don't edit.

