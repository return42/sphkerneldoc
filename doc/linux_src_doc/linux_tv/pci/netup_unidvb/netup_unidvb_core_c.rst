.. -*- coding: utf-8; mode: rst -*-

===================
netup_unidvb_core.c
===================



.. _xref_struct_netup_dma_regs:

struct netup_dma_regs
=====================

.. c:type:: struct netup_dma_regs

    the map of DMA module registers



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
  };



Members
-------

:``__le32 ctrlstat_set``:
    Control register, write to set control bits

:``__le32 ctrlstat_clear``:
    Control register, write to clear control bits

:``__le32 start_addr_lo``:
    DMA ring buffer start address, lower part

:``__le32 start_addr_hi``:
    DMA ring buffer start address, higher part

:``__le32 size``:
    DMA ring buffer size register

:``__le32 timeout``:
    DMA timeout in units of 8ns

:``__le32 curr_addr_lo``:
    Current ring buffer head address, lower part

:``__le32 curr_addr_hi``:
    Current ring buffer head address, higher part

:``__le32 stat_pkt_received``:
    Statistic register, not tested

:``__le32 stat_pkt_accepted``:
    Statistic register, not tested

:``__le32 stat_pkt_overruns``:
    Statistic register, not tested

:``__le32 stat_pkt_underruns``:
    Statistic register, not tested

:``__le32 stat_fifo_overruns``:
    Statistic register, not tested



