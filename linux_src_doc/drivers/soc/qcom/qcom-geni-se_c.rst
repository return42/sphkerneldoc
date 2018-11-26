.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/qcom-geni-se.c

.. _`overview`:

Overview
========

Generic Interface (GENI) Serial Engine (SE) Wrapper driver is introduced
to manage GENI firmware based Qualcomm Universal Peripheral (QUP) Wrapper
controller. QUP Wrapper is designed to support various serial bus protocols
like UART, SPI, I2C, I3C, etc.

.. _`hardware-description`:

Hardware description
====================

GENI based QUP is a highly-flexible and programmable module for supporting
a wide range of serial interfaces like UART, SPI, I2C, I3C, etc. A single
QUP module can provide upto 8 serial interfaces, using its internal
serial engines. The actual configuration is determined by the target
platform configuration. The protocol supported by each interface is
determined by the firmware loaded to the serial engine. Each SE consists
of a DMA Engine and GENI sub modules which enable serial engines to
support FIFO and DMA modes of operation.


+-----------------------------------------+
\|QUP Wrapper                              \|
\|         +----------------------------+  \|
--QUP & SE Clocks-->         \| Serial Engine N            \|  +-IO------>
\|         \| ...                        \|  \| Interface
<---Clock Perf.----+    +----+-----------------------+    \|  \|
State Interface  \|    \| Serial Engine 1            \|    \|  \|
\|    \|                            \|    \|  \|
\|    \|                            \|    \|  \|
<--------AHB------->    \|                            \|    \|  \|
\|    \|                            +----+  \|
\|    \|                            \|       \|
\|    \|                            \|       \|
<------SE IRQ------+    +----------------------------+       \|
\|                                         \|
+-----------------------------------------+

Figure 1: GENI based QUP Wrapper

The GENI submodules include primary and secondary sequencers which are
used to drive TX & RX operations. On serial interfaces that operate using
master-slave model, primary sequencer drives both TX & RX operations. On
serial interfaces that operate using peer-to-peer model, primary sequencer
drives TX operation and secondary sequencer drives RX operation.

.. _`software-description`:

Software description
====================

GENI SE Wrapper driver is structured into 2 parts:

geni_wrapper represents QUP Wrapper controller. This part of the driver
manages QUP Wrapper information such as hardware version, clock
performance table that is common to all the internal serial engines.

geni_se represents serial engine. This part of the driver manages serial
engine information such as clocks, containing QUP Wrapper, etc. This part
of driver also supports operations (eg. initialize the concerned serial
engine, select between FIFO and DMA mode of operation etc.) that are
common to all the serial engines and are independent of serial interfaces.

.. _`geni_se_get_qup_hw_version`:

geni_se_get_qup_hw_version
==========================

.. c:function:: u32 geni_se_get_qup_hw_version(struct geni_se *se)

    Read the QUP wrapper Hardware version

    :param se:
        Pointer to the corresponding serial engine.
    :type se: struct geni_se \*

.. _`geni_se_get_qup_hw_version.return`:

Return
------

Hardware Version of the wrapper.

.. _`geni_se_init`:

geni_se_init
============

.. c:function:: void geni_se_init(struct geni_se *se, u32 rx_wm, u32 rx_rfr)

    Initialize the GENI serial engine

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param rx_wm:
        Receive watermark, in units of FIFO words.
    :type rx_wm: u32

    :param rx_rfr:
        *undescribed*
    :type rx_rfr: u32

.. _`geni_se_init.description`:

Description
-----------

This function is used to initialize the GENI serial engine, configure
receive watermark and ready-for-receive watermarks.

.. _`geni_se_select_mode`:

geni_se_select_mode
===================

.. c:function:: void geni_se_select_mode(struct geni_se *se, enum geni_se_xfer_mode mode)

    Select the serial engine transfer mode

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param mode:
        Transfer mode to be selected.
    :type mode: enum geni_se_xfer_mode

.. _`overview`:

Overview
========

GENI FIFO packing is highly configurable. TX/RX packing/unpacking consist
of up to 4 operations, each operation represented by 4 configuration vectors
of 10 bits programmed in GENI_TX_PACKING_CFG0 and GENI_TX_PACKING_CFG1 for
TX FIFO and in GENI_RX_PACKING_CFG0 and GENI_RX_PACKING_CFG1 for RX FIFO.
Refer to below examples for detailed bit-field description.

Example 1: word_size = 7, packing_mode = 4 x 8, msb_to_lsb = 1

+-----------+-------+-------+-------+-------+
\|           \| vec_0 \| vec_1 \| vec_2 \| vec_3 \|
+-----------+-------+-------+-------+-------+
\| start     \| 0x6   \| 0xe   \| 0x16  \| 0x1e  \|
\| direction \| 1     \| 1     \| 1     \| 1     \|
\| length    \| 6     \| 6     \| 6     \| 6     \|
\| stop      \| 0     \| 0     \| 0     \| 1     \|
+-----------+-------+-------+-------+-------+

Example 2: word_size = 15, packing_mode = 2 x 16, msb_to_lsb = 0

+-----------+-------+-------+-------+-------+
\|           \| vec_0 \| vec_1 \| vec_2 \| vec_3 \|
+-----------+-------+-------+-------+-------+
\| start     \| 0x0   \| 0x8   \| 0x10  \| 0x18  \|
\| direction \| 0     \| 0     \| 0     \| 0     \|
\| length    \| 7     \| 6     \| 7     \| 6     \|
\| stop      \| 0     \| 0     \| 0     \| 1     \|
+-----------+-------+-------+-------+-------+

Example 3: word_size = 23, packing_mode = 1 x 32, msb_to_lsb = 1

+-----------+-------+-------+-------+-------+
\|           \| vec_0 \| vec_1 \| vec_2 \| vec_3 \|
+-----------+-------+-------+-------+-------+
\| start     \| 0x16  \| 0xe   \| 0x6   \| 0x0   \|
\| direction \| 1     \| 1     \| 1     \| 1     \|
\| length    \| 7     \| 7     \| 6     \| 0     \|
\| stop      \| 0     \| 0     \| 1     \| 0     \|
+-----------+-------+-------+-------+-------+

.. _`geni_se_config_packing`:

geni_se_config_packing
======================

.. c:function:: void geni_se_config_packing(struct geni_se *se, int bpw, int pack_words, bool msb_to_lsb, bool tx_cfg, bool rx_cfg)

    Packing configuration of the serial engine

    :param se:
        Pointer to the concerned serial engine
    :type se: struct geni_se \*

    :param bpw:
        Bits of data per transfer word.
    :type bpw: int

    :param pack_words:
        Number of words per fifo element.
    :type pack_words: int

    :param msb_to_lsb:
        Transfer from MSB to LSB or vice-versa.
    :type msb_to_lsb: bool

    :param tx_cfg:
        Flag to configure the TX Packing.
    :type tx_cfg: bool

    :param rx_cfg:
        Flag to configure the RX Packing.
    :type rx_cfg: bool

.. _`geni_se_config_packing.description`:

Description
-----------

This function is used to configure the packing rules for the current
transfer.

.. _`geni_se_resources_off`:

geni_se_resources_off
=====================

.. c:function:: int geni_se_resources_off(struct geni_se *se)

    Turn off resources associated with the serial engine

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_resources_off.return`:

Return
------

0 on success, standard Linux error codes on failure/error.

.. _`geni_se_resources_on`:

geni_se_resources_on
====================

.. c:function:: int geni_se_resources_on(struct geni_se *se)

    Turn on resources associated with the serial engine

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

.. _`geni_se_resources_on.return`:

Return
------

0 on success, standard Linux error codes on failure/error.

.. _`geni_se_clk_tbl_get`:

geni_se_clk_tbl_get
===================

.. c:function:: int geni_se_clk_tbl_get(struct geni_se *se, unsigned long **tbl)

    Get the clock table to program DFS

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param tbl:
        Table in which the output is returned.
    :type tbl: unsigned long \*\*

.. _`geni_se_clk_tbl_get.description`:

Description
-----------

This function is called by the protocol drivers to determine the different
clock frequencies supported by serial engine core clock. The protocol
drivers use the output to determine the clock frequency index to be
programmed into DFS.

.. _`geni_se_clk_tbl_get.return`:

Return
------

number of valid performance levels in the table on success,
standard Linux error codes on failure.

.. _`geni_se_clk_freq_match`:

geni_se_clk_freq_match
======================

.. c:function:: int geni_se_clk_freq_match(struct geni_se *se, unsigned long req_freq, unsigned int *index, unsigned long *res_freq, bool exact)

    Get the matching or closest SE clock frequency

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param req_freq:
        Requested clock frequency.
    :type req_freq: unsigned long

    :param index:
        Index of the resultant frequency in the table.
    :type index: unsigned int \*

    :param res_freq:
        Resultant frequency of the source clock.
    :type res_freq: unsigned long \*

    :param exact:
        Flag to indicate exact multiple requirement of the requested
        frequency.
    :type exact: bool

.. _`geni_se_clk_freq_match.description`:

Description
-----------

This function is called by the protocol drivers to determine the best match
of the requested frequency as provided by the serial engine clock in order
to meet the performance requirements.

.. _`geni_se_clk_freq_match.if-we-return-success`:

If we return success
--------------------

- if \ ``exact``\  is true  then \ ``res_freq``\  / <an_integer> == \ ``req_freq``\ 
- if \ ``exact``\  is false then \ ``res_freq``\  / <an_integer> <= \ ``req_freq``\ 

.. _`geni_se_clk_freq_match.return`:

Return
------

0 on success, standard Linux error codes on failure.

.. _`geni_se_tx_dma_prep`:

geni_se_tx_dma_prep
===================

.. c:function:: int geni_se_tx_dma_prep(struct geni_se *se, void *buf, size_t len, dma_addr_t *iova)

    Prepare the serial engine for TX DMA transfer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param buf:
        Pointer to the TX buffer.
    :type buf: void \*

    :param len:
        Length of the TX buffer.
    :type len: size_t

    :param iova:
        Pointer to store the mapped DMA address.
    :type iova: dma_addr_t \*

.. _`geni_se_tx_dma_prep.description`:

Description
-----------

This function is used to prepare the buffers for DMA TX.

.. _`geni_se_tx_dma_prep.return`:

Return
------

0 on success, standard Linux error codes on failure.

.. _`geni_se_rx_dma_prep`:

geni_se_rx_dma_prep
===================

.. c:function:: int geni_se_rx_dma_prep(struct geni_se *se, void *buf, size_t len, dma_addr_t *iova)

    Prepare the serial engine for RX DMA transfer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param buf:
        Pointer to the RX buffer.
    :type buf: void \*

    :param len:
        Length of the RX buffer.
    :type len: size_t

    :param iova:
        Pointer to store the mapped DMA address.
    :type iova: dma_addr_t \*

.. _`geni_se_rx_dma_prep.description`:

Description
-----------

This function is used to prepare the buffers for DMA RX.

.. _`geni_se_rx_dma_prep.return`:

Return
------

0 on success, standard Linux error codes on failure.

.. _`geni_se_tx_dma_unprep`:

geni_se_tx_dma_unprep
=====================

.. c:function:: void geni_se_tx_dma_unprep(struct geni_se *se, dma_addr_t iova, size_t len)

    Unprepare the serial engine after TX DMA transfer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param iova:
        DMA address of the TX buffer.
    :type iova: dma_addr_t

    :param len:
        Length of the TX buffer.
    :type len: size_t

.. _`geni_se_tx_dma_unprep.description`:

Description
-----------

This function is used to unprepare the DMA buffers after DMA TX.

.. _`geni_se_rx_dma_unprep`:

geni_se_rx_dma_unprep
=====================

.. c:function:: void geni_se_rx_dma_unprep(struct geni_se *se, dma_addr_t iova, size_t len)

    Unprepare the serial engine after RX DMA transfer

    :param se:
        Pointer to the concerned serial engine.
    :type se: struct geni_se \*

    :param iova:
        DMA address of the RX buffer.
    :type iova: dma_addr_t

    :param len:
        Length of the RX buffer.
    :type len: size_t

.. _`geni_se_rx_dma_unprep.description`:

Description
-----------

This function is used to unprepare the DMA buffers after DMA RX.

.. This file was automatic generated / don't edit.

