.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_usb_ops.c

.. _`rsi_copy_to_card`:

rsi_copy_to_card
================

.. c:function:: int rsi_copy_to_card(struct rsi_common *common, const u8 *fw, u32 len, u32 num_blocks)

    :param struct rsi_common \*common:
        *undescribed*

    :param const u8 \*fw:
        *undescribed*

    :param u32 len:
        *undescribed*

    :param u32 num_blocks:
        *undescribed*

.. _`rsi_copy_to_card.description`:

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

.. _`rsi_usb_rx_thread`:

rsi_usb_rx_thread
=================

.. c:function:: void rsi_usb_rx_thread(struct rsi_common *common)

    This is a kernel thread to receive the packets from the USB device.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_usb_rx_thread.return`:

Return
------

None.

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

.. _`rsi_usb_device_init`:

rsi_usb_device_init
===================

.. c:function:: int rsi_usb_device_init(struct rsi_common *common)

    This Function Initializes The HAL.

    :param struct rsi_common \*common:
        Pointer to the driver private structure.

.. _`rsi_usb_device_init.return`:

Return
------

0 on success, -1 on failure.

.. This file was automatic generated / don't edit.

