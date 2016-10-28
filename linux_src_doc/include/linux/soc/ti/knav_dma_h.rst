.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/soc/ti/knav_dma.h

.. _`knav_dma_tx_cfg`:

struct knav_dma_tx_cfg
======================

.. c:type:: struct knav_dma_tx_cfg

    Tx channel configuration

.. _`knav_dma_tx_cfg.definition`:

Definition
----------

.. code-block:: c

    struct knav_dma_tx_cfg {
        bool filt_einfo;
        bool filt_pswords;
        enum knav_dma_tx_priority priority;
    }

.. _`knav_dma_tx_cfg.members`:

Members
-------

filt_einfo
    Filter extended packet info

filt_pswords
    Filter PS words present

priority
    *undescribed*

.. _`knav_dma_rx_cfg`:

struct knav_dma_rx_cfg
======================

.. c:type:: struct knav_dma_rx_cfg

    Rx flow configuration

.. _`knav_dma_rx_cfg.definition`:

Definition
----------

.. code-block:: c

    struct knav_dma_rx_cfg {
        bool einfo_present;
        bool psinfo_present;
        enum knav_dma_rx_err_mode err_mode;
        enum knav_dma_desc_type desc_type;
        bool psinfo_at_sop;
        unsigned int sop_offset;
        unsigned int dst_q;
        enum knav_dma_rx_thresholds thresh;
        unsigned int fdq[KNAV_DMA_FDQ_PER_CHAN];
        unsigned int sz_thresh0;
        unsigned int sz_thresh1;
        unsigned int sz_thresh2;
    }

.. _`knav_dma_rx_cfg.members`:

Members
-------

einfo_present
    Extended packet info present

psinfo_present
    PS words present

err_mode
    *undescribed*

desc_type
    *undescribed*

psinfo_at_sop
    PS word located at start of packet

sop_offset
    Start of packet offset

dst_q
    Destination queue for a given flow

thresh
    Rx flow size threshold

fdq
    Free desc Queue array

sz_thresh0
    RX packet size threshold 0

sz_thresh1
    RX packet size threshold 1

sz_thresh2
    RX packet size threshold 2

.. _`knav_dma_cfg`:

struct knav_dma_cfg
===================

.. c:type:: struct knav_dma_cfg

    Pktdma channel configuration

.. _`knav_dma_cfg.definition`:

Definition
----------

.. code-block:: c

    struct knav_dma_cfg {
        enum dma_transfer_direction direction;
        union u;
    }

.. _`knav_dma_cfg.members`:

Members
-------

direction
    *undescribed*

u
    *undescribed*

.. _`knav_dma_desc`:

struct knav_dma_desc
====================

.. c:type:: struct knav_dma_desc

    Host packet descriptor layout

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
    }

.. _`knav_dma_desc.members`:

Members
-------

desc_info
    Descriptor information like id, type, length

tag_info
    Flow tag info written in during RX

packet_info
    Queue Manager, policy, flags etc

buff_len
    Buffer length in bytes

buff
    Buffer pointer

next_desc
    For chaining the descriptors

orig_len
    length since 'buff_len' can be overwritten

orig_buff
    buff pointer since 'buff' can be overwritten

epib
    Extended packet info block

psdata
    Protocol specific

sw_data
    Software private data not touched by h/w

.. This file was automatic generated / don't edit.

