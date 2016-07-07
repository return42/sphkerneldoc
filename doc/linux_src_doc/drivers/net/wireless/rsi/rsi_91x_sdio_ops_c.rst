.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_sdio_ops.c

.. _`rsi_sdio_master_access_msword`:

rsi_sdio_master_access_msword
=============================

.. c:function:: int rsi_sdio_master_access_msword(struct rsi_hw *adapter, u16 ms_word)

    :param struct rsi_hw \*adapter:
        *undescribed*

    :param u16 ms_word:
        *undescribed*

.. _`rsi_sdio_master_access_msword.description`:

Description
-----------

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

.. _`rsi_copy_to_card`:

rsi_copy_to_card
================

.. c:function:: int rsi_copy_to_card(struct rsi_common *common, const u8 *fw, u32 len, u32 num_blocks)

    This function includes the actual funtionality of copying the TA firmware to the card.Basically this function includes opening the TA file,reading the TA file and writing their values in blocks of data.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

    :param const u8 \*fw:
        Pointer to the firmware value to be written.

    :param u32 len:
        length of firmware file.

    :param u32 num_blocks:
        Number of blocks to be written to the card.

.. _`rsi_copy_to_card.return`:

Return
------

0 on success and -1 on failure.

.. _`rsi_load_ta_instructions`:

rsi_load_ta_instructions
========================

.. c:function:: int rsi_load_ta_instructions(struct rsi_common *common)

    This function includes the actual funtionality of loading the TA firmware.This function also includes opening the TA file,reading the TA file and writing their value in blocks of data.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_load_ta_instructions.return`:

Return
------

status: 0 on success, -1 on failure.

.. _`rsi_process_pkt`:

rsi_process_pkt
===============

.. c:function:: int rsi_process_pkt(struct rsi_common *common)

    This Function reads rx_blocks register and figures out the size of the rx pkt.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_process_pkt.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_init_sdio_slave_regs`:

rsi_init_sdio_slave_regs
========================

.. c:function:: int rsi_init_sdio_slave_regs(struct rsi_hw *adapter)

    This function does the actual initialization of SDBUS slave registers.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

.. _`rsi_init_sdio_slave_regs.return`:

Return
------

status: 0 on success, -1 on failure.

.. _`rsi_interrupt_handler`:

rsi_interrupt_handler
=====================

.. c:function:: void rsi_interrupt_handler(struct rsi_hw *adapter)

    This function read and process SDIO interrupts.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

.. _`rsi_interrupt_handler.return`:

Return
------

None.

.. _`rsi_sdio_device_init`:

rsi_sdio_device_init
====================

.. c:function:: int rsi_sdio_device_init(struct rsi_common *common)

    This Function Initializes The HAL.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_sdio_device_init.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_read_buffer_status_register`:

rsi_sdio_read_buffer_status_register
====================================

.. c:function:: int rsi_sdio_read_buffer_status_register(struct rsi_hw *adapter, u8 q_num)

    This function is used to the read buffer status register and set relevant fields in rsi_91x_sdiodev struct.

    :param struct rsi_hw \*adapter:
        Pointer to the driver hw structure.

    :param u8 q_num:
        The Q number whose status is to be found.

.. _`rsi_sdio_read_buffer_status_register.return`:

Return
------

status: -1 on failure or else queue full/stop is indicated.

.. _`rsi_sdio_determine_event_timeout`:

rsi_sdio_determine_event_timeout
================================

.. c:function:: int rsi_sdio_determine_event_timeout(struct rsi_hw *adapter)

    This Function determines the event timeout duration.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

.. _`rsi_sdio_determine_event_timeout.return`:

Return
------

timeout duration is returned.

.. This file was automatic generated / don't edit.

