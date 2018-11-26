.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_sdio_ops.c

.. _`rsi_sdio_master_access_msword`:

rsi_sdio_master_access_msword
=============================

.. c:function:: int rsi_sdio_master_access_msword(struct rsi_hw *adapter, u16 ms_word)

    :param adapter:
        *undescribed*
    :type adapter: struct rsi_hw \*

    :param ms_word:
        *undescribed*
    :type ms_word: u16

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

.. _`rsi_process_pkt`:

rsi_process_pkt
===============

.. c:function:: int rsi_process_pkt(struct rsi_common *common)

    This Function reads rx_blocks register and figures out the size of the rx pkt.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_process_pkt.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_init_sdio_slave_regs`:

rsi_init_sdio_slave_regs
========================

.. c:function:: int rsi_init_sdio_slave_regs(struct rsi_hw *adapter)

    This function does the actual initialization of SDBUS slave registers.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

.. _`rsi_init_sdio_slave_regs.return`:

Return
------

status: 0 on success, -1 on failure.

.. _`rsi_interrupt_handler`:

rsi_interrupt_handler
=====================

.. c:function:: void rsi_interrupt_handler(struct rsi_hw *adapter)

    This function read and process SDIO interrupts.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

.. _`rsi_interrupt_handler.return`:

Return
------

None.

.. _`rsi_sdio_determine_event_timeout`:

rsi_sdio_determine_event_timeout
================================

.. c:function:: int rsi_sdio_determine_event_timeout(struct rsi_hw *adapter)

    This Function determines the event timeout duration.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

.. _`rsi_sdio_determine_event_timeout.return`:

Return
------

timeout duration is returned.

.. This file was automatic generated / don't edit.

