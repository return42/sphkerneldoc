.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dma/xilinx_dma.h

.. _`xilinx_vdma_config`:

struct xilinx_vdma_config
=========================

.. c:type:: struct xilinx_vdma_config

    VDMA Configuration structure

.. _`xilinx_vdma_config.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_vdma_config {
        int frm_dly;
        int gen_lock;
        int master;
        int frm_cnt_en;
        int park;
        int park_frm;
        int coalesc;
        int delay;
        int reset;
        int ext_fsync;
    }

.. _`xilinx_vdma_config.members`:

Members
-------

frm_dly
    Frame delay

gen_lock
    Whether in gen-lock mode

master
    Master that it syncs to

frm_cnt_en
    Enable frame count enable

park
    Whether wants to park

park_frm
    Frame to park on

coalesc
    Interrupt coalescing threshold

delay
    Delay counter

reset
    Reset Channel

ext_fsync
    External Frame Sync source

.. This file was automatic generated / don't edit.

