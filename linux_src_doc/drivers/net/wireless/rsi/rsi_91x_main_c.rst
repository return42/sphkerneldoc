.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_main.c

.. _`pr_fmt`:

pr_fmt
======

.. c:function::  pr_fmt( fmt)

    :param fmt:
        *undescribed*
    :type fmt: 

.. _`pr_fmt.description`:

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

.. _`rsi_dbg`:

rsi_dbg
=======

.. c:function:: void rsi_dbg(u32 zone, const char *fmt,  ...)

    This function outputs informational messages.

    :param zone:
        Zone of interest for output message.
    :type zone: u32

    :param fmt:
        printf-style format for output message.
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`rsi_dbg.return`:

Return
------

none

.. _`rsi_prepare_skb`:

rsi_prepare_skb
===============

.. c:function:: struct sk_buff *rsi_prepare_skb(struct rsi_common *common, u8 *buffer, u32 pkt_len, u8 extended_desc)

    This function prepares the skb.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param buffer:
        Pointer to the packet data.
    :type buffer: u8 \*

    :param pkt_len:
        Length of the packet.
    :type pkt_len: u32

    :param extended_desc:
        Extended descriptor.
    :type extended_desc: u8

.. _`rsi_prepare_skb.return`:

Return
------

Successfully skb.

.. _`rsi_read_pkt`:

rsi_read_pkt
============

.. c:function:: int rsi_read_pkt(struct rsi_common *common, u8 *rx_pkt, s32 rcv_pkt_len)

    This function reads frames from the card.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

    :param rx_pkt:
        *undescribed*
    :type rx_pkt: u8 \*

    :param rcv_pkt_len:
        Received pkt length. In case of USB it is 0.
    :type rcv_pkt_len: s32

.. _`rsi_read_pkt.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_tx_scheduler_thread`:

rsi_tx_scheduler_thread
=======================

.. c:function:: void rsi_tx_scheduler_thread(struct rsi_common *common)

    This function is a kernel thread to send the packets to the device.

    :param common:
        Pointer to the driver private structure.
    :type common: struct rsi_common \*

.. _`rsi_tx_scheduler_thread.return`:

Return
------

None.

.. _`rsi_91x_init`:

rsi_91x_init
============

.. c:function:: struct rsi_hw *rsi_91x_init(u16 oper_mode)

    This function initializes os interface operations.

    :param oper_mode:
        *undescribed*
    :type oper_mode: u16

.. _`rsi_91x_init.return`:

Return
------

Pointer to the adapter structure on success, NULL on failure .

.. _`rsi_91x_deinit`:

rsi_91x_deinit
==============

.. c:function:: void rsi_91x_deinit(struct rsi_hw *adapter)

    This function de-intializes os intf operations.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

.. _`rsi_91x_deinit.return`:

Return
------

None.

.. _`rsi_91x_hal_module_init`:

rsi_91x_hal_module_init
=======================

.. c:function:: int rsi_91x_hal_module_init( void)

    This function is invoked when the module is loaded into the kernel. It registers the client driver.

    :param void:
        no arguments
    :type void: 

.. _`rsi_91x_hal_module_init.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_91x_hal_module_exit`:

rsi_91x_hal_module_exit
=======================

.. c:function:: void rsi_91x_hal_module_exit( void)

    This function is called at the time of removing/unloading the module. It unregisters the client driver.

    :param void:
        no arguments
    :type void: 

.. _`rsi_91x_hal_module_exit.return`:

Return
------

None.

.. This file was automatic generated / don't edit.

