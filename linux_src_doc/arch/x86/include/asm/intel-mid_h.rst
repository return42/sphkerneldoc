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
        char name[SFI_NAME_LEN];
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

.. This file was automatic generated / don't edit.

