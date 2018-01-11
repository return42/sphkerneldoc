.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/pci/netup_unidvb/netup_unidvb_core.c

.. _`netup_dma_regs`:

struct netup_dma_regs
=====================

.. c:type:: struct netup_dma_regs

    the map of DMA module registers

.. _`netup_dma_regs.definition`:

Definition
----------

.. code-block:: c

    struct netup_dma_regs {
        __le32 ctrlstat_set;
        __le32 ctrlstat_clear;
        __le32 start_addr_lo;
        __le32 start_addr_hi;
        __le32 size;
        __le32 timeout;
        __le32 curr_addr_lo;
        __le32 curr_addr_hi;
        __le32 stat_pkt_received;
        __le32 stat_pkt_accepted;
        __le32 stat_pkt_overruns;
        __le32 stat_pkt_underruns;
        __le32 stat_fifo_overruns;
    }

.. _`netup_dma_regs.members`:

Members
-------

ctrlstat_set
    Control register, write to set control bits

ctrlstat_clear
    Control register, write to clear control bits

start_addr_lo
    DMA ring buffer start address, lower part

start_addr_hi
    DMA ring buffer start address, higher part

size
    DMA ring buffer size register
    \* Bits [0-7]:   DMA packet size, 188 bytes
    \* Bits [16-23]: packets count in block, 128 packets
    \* Bits [24-31]: blocks count, 8 blocks

timeout
    DMA timeout in units of 8ns
    For example, value of 375000000 equals to 3 sec

curr_addr_lo
    Current ring buffer head address, lower part

curr_addr_hi
    Current ring buffer head address, higher part

stat_pkt_received
    Statistic register, not tested

stat_pkt_accepted
    Statistic register, not tested

stat_pkt_overruns
    Statistic register, not tested

stat_pkt_underruns
    Statistic register, not tested

stat_fifo_overruns
    Statistic register, not tested

.. This file was automatic generated / don't edit.

