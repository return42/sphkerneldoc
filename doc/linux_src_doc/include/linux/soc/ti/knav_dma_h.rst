.. -*- coding: utf-8; mode: rst -*-

==========
knav_dma.h
==========


.. _`knav_dma_tx_cfg`:

struct knav_dma_tx_cfg
======================

.. c:type:: knav_dma_tx_cfg

    


.. _`knav_dma_tx_cfg.definition`:

Definition
----------

.. code-block:: c

  struct knav_dma_tx_cfg {
    bool filt_einfo;
    bool filt_pswords;
  };


.. _`knav_dma_tx_cfg.members`:

Members
-------

:``filt_einfo``:
    Filter extended packet info

:``filt_pswords``:
    Filter PS words present




.. _`knav_dma_rx_cfg`:

struct knav_dma_rx_cfg
======================

.. c:type:: knav_dma_rx_cfg

    


.. _`knav_dma_rx_cfg.definition`:

Definition
----------

.. code-block:: c

  struct knav_dma_rx_cfg {
    bool einfo_present;
    bool psinfo_present;
    bool psinfo_at_sop;
    unsigned int sop_offset;
    unsigned int dst_q;
    enum knav_dma_rx_thresholds thresh;
    unsigned int sz_thresh0;
    unsigned int sz_thresh1;
    unsigned int sz_thresh2;
  };


.. _`knav_dma_rx_cfg.members`:

Members
-------

:``einfo_present``:
    Extended packet info present

:``psinfo_present``:
    PS words present

:``psinfo_at_sop``:
    PS word located at start of packet

:``sop_offset``:
    Start of packet offset

:``dst_q``:
    Destination queue for a given flow

:``thresh``:
    Rx flow size threshold
    ``fdq``\ []:                        Free desc Queue array

:``sz_thresh0``:
    RX packet size threshold 0

:``sz_thresh1``:
    RX packet size threshold 1

:``sz_thresh2``:
    RX packet size threshold 2




.. _`knav_dma_cfg`:

struct knav_dma_cfg
===================

.. c:type:: knav_dma_cfg

    


.. _`knav_dma_cfg.definition`:

Definition
----------

.. code-block:: c

  struct knav_dma_cfg {
  };


.. _`knav_dma_cfg.members`:

Members
-------




.. _`knav_dma_desc`:

struct knav_dma_desc
====================

.. c:type:: knav_dma_desc

    


.. _`knav_dma_desc.definition`:

Definition
----------

.. code-block:: c

  struct knav_dma_desc {
    __le32 desc_info;
    __le32 tag_info;
    __le32 packet_info;
    __le32 buff_len;
    __le32 buff;
    __le32 next_desc;
    __le32 orig_len;
    __le32 orig_buff;
    __le32 epib[KNAV_DMA_NUM_EPIB_WORDS];
    __le32 psdata[KNAV_DMA_NUM_PS_WORDS];
    u32 sw_data[KNAV_DMA_NUM_SW_DATA_WORDS];
  };


.. _`knav_dma_desc.members`:

Members
-------

:``desc_info``:
    Descriptor information like id, type, length

:``tag_info``:
    Flow tag info written in during RX

:``packet_info``:
    Queue Manager, policy, flags etc

:``buff_len``:
    Buffer length in bytes

:``buff``:
    Buffer pointer

:``next_desc``:
    For chaining the descriptors

:``orig_len``:
    length since 'buff_len' can be overwritten

:``orig_buff``:
    buff pointer since 'buff' can be overwritten

:``epib[KNAV_DMA_NUM_EPIB_WORDS]``:
    Extended packet info block

:``psdata[KNAV_DMA_NUM_PS_WORDS]``:
    Protocol specific

:``sw_data[KNAV_DMA_NUM_SW_DATA_WORDS]``:
    Software private data not touched by h/w


