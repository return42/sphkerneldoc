.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_sdio.c

.. _`rsi_sdio_set_cmd52_arg`:

rsi_sdio_set_cmd52_arg
======================

.. c:function:: u32 rsi_sdio_set_cmd52_arg(bool rw, u8 func, u8 raw, u32 address, u8 writedata)

    :param bool rw:
        *undescribed*

    :param u8 func:
        *undescribed*

    :param u8 raw:
        *undescribed*

    :param u32 address:
        *undescribed*

    :param u8 writedata:
        *undescribed*

.. _`rsi_sdio_set_cmd52_arg.description`:

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

.. _`rsi_cmd52writebyte`:

rsi_cmd52writebyte
==================

.. c:function:: int rsi_cmd52writebyte(struct mmc_card *card, u32 address, u8 byte)

    This function issues cmd52 byte write onto the card.

    :param struct mmc_card \*card:
        Pointer to the mmc_card.

    :param u32 address:
        Address to write.

    :param u8 byte:
        Data to write.

.. _`rsi_cmd52writebyte.return`:

Return
------

Write status.

.. _`rsi_cmd52readbyte`:

rsi_cmd52readbyte
=================

.. c:function:: int rsi_cmd52readbyte(struct mmc_card *card, u32 address, u8 *byte)

    This function issues cmd52 byte read onto the card.

    :param struct mmc_card \*card:
        Pointer to the mmc_card.

    :param u32 address:
        Address to read from.

    :param u8 \*byte:
        Variable to store read value.

.. _`rsi_cmd52readbyte.return`:

Return
------

Read status.

.. _`rsi_issue_sdiocommand`:

rsi_issue_sdiocommand
=====================

.. c:function:: int rsi_issue_sdiocommand(struct sdio_func *func, u32 opcode, u32 arg, u32 flags, u32 *resp)

    This function issues sdio commands.

    :param struct sdio_func \*func:
        Pointer to the sdio_func structure.

    :param u32 opcode:
        Opcode value.

    :param u32 arg:
        Arguments to pass.

    :param u32 flags:
        Flags which are set.

    :param u32 \*resp:
        Pointer to store response.

.. _`rsi_issue_sdiocommand.return`:

Return
------

err: command status as 0 or -1.

.. _`rsi_handle_interrupt`:

rsi_handle_interrupt
====================

.. c:function:: void rsi_handle_interrupt(struct sdio_func *function)

    This function is called upon the occurence of an interrupt.

    :param struct sdio_func \*function:
        Pointer to the sdio_func structure.

.. _`rsi_handle_interrupt.return`:

Return
------

None.

.. _`rsi_reset_card`:

rsi_reset_card
==============

.. c:function:: void rsi_reset_card(struct sdio_func *pfunction)

    This function resets and re-initializes the card.

    :param struct sdio_func \*pfunction:
        Pointer to the sdio_func structure.

.. _`rsi_reset_card.return`:

Return
------

None.

.. _`rsi_setclock`:

rsi_setclock
============

.. c:function:: void rsi_setclock(struct rsi_hw *adapter, u32 freq)

    This function sets the clock frequency.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u32 freq:
        Clock frequency.

.. _`rsi_setclock.return`:

Return
------

None.

.. _`rsi_setblocklength`:

rsi_setblocklength
==================

.. c:function:: int rsi_setblocklength(struct rsi_hw *adapter, u32 length)

    This function sets the host block length.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u32 length:
        Block length to be set.

.. _`rsi_setblocklength.return`:

Return
------

status: 0 on success, -1 on failure.

.. _`rsi_setupcard`:

rsi_setupcard
=============

.. c:function:: int rsi_setupcard(struct rsi_hw *adapter)

    This function queries and sets the card's features.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

.. _`rsi_setupcard.return`:

Return
------

status: 0 on success, -1 on failure.

.. _`rsi_sdio_read_register`:

rsi_sdio_read_register
======================

.. c:function:: int rsi_sdio_read_register(struct rsi_hw *adapter, u32 addr, u8 *data)

    This function reads one byte of information from a register.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u32 addr:
        Address of the register.

    :param u8 \*data:
        Pointer to the data that stores the data read.

.. _`rsi_sdio_read_register.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_write_register`:

rsi_sdio_write_register
=======================

.. c:function:: int rsi_sdio_write_register(struct rsi_hw *adapter, u8 function, u32 addr, u8 *data)

    This function writes one byte of information into a register.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u8 function:
        Function Number.

    :param u32 addr:
        Address of the register.

    :param u8 \*data:
        Pointer to the data tha has to be written.

.. _`rsi_sdio_write_register.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_ack_intr`:

rsi_sdio_ack_intr
=================

.. c:function:: void rsi_sdio_ack_intr(struct rsi_hw *adapter, u8 int_bit)

    This function acks the interrupt received.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u8 int_bit:
        Interrupt bit to write into register.

.. _`rsi_sdio_ack_intr.return`:

Return
------

None.

.. _`rsi_sdio_read_register_multiple`:

rsi_sdio_read_register_multiple
===============================

.. c:function:: int rsi_sdio_read_register_multiple(struct rsi_hw *adapter, u32 addr, u32 count, u8 *data)

    This function read multiple bytes of information from the SD card.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u32 addr:
        Address of the register.

    :param u32 count:
        Number of multiple bytes to be read.

    :param u8 \*data:
        Pointer to the read data.

.. _`rsi_sdio_read_register_multiple.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_write_register_multiple`:

rsi_sdio_write_register_multiple
================================

.. c:function:: int rsi_sdio_write_register_multiple(struct rsi_hw *adapter, u32 addr, u8 *data, u32 count)

    This function writes multiple bytes of information to the SD card.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u32 addr:
        Address of the register.

    :param u8 \*data:
        Pointer to the data that has to be written.

    :param u32 count:
        Number of multiple bytes to be written.

.. _`rsi_sdio_write_register_multiple.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_host_intf_write_pkt`:

rsi_sdio_host_intf_write_pkt
============================

.. c:function:: int rsi_sdio_host_intf_write_pkt(struct rsi_hw *adapter, u8 *pkt, u32 len)

    This function writes the packet to device.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter structure.

    :param u8 \*pkt:
        Pointer to the data to be written on to the device.

    :param u32 len:
        length of the data to be written on to the device.

.. _`rsi_sdio_host_intf_write_pkt.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_host_intf_read_pkt`:

rsi_sdio_host_intf_read_pkt
===========================

.. c:function:: int rsi_sdio_host_intf_read_pkt(struct rsi_hw *adapter, u8 *pkt, u32 length)

    This function reads the packet

    :param struct rsi_hw \*adapter:
        Pointer to the adapter data structure.

    :param u8 \*pkt:
        Pointer to the packet data to be read from the the device.

    :param u32 length:
        Length of the data to be read from the device.

.. _`rsi_sdio_host_intf_read_pkt.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_init_sdio_interface`:

rsi_init_sdio_interface
=======================

.. c:function:: int rsi_init_sdio_interface(struct rsi_hw *adapter, struct sdio_func *pfunction)

    This function does init specific to SDIO.

    :param struct rsi_hw \*adapter:
        Pointer to the adapter data structure.

    :param struct sdio_func \*pfunction:
        *undescribed*

.. _`rsi_init_sdio_interface.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_probe`:

rsi_probe
=========

.. c:function:: int rsi_probe(struct sdio_func *pfunction, const struct sdio_device_id *id)

    This function is called by kernel when the driver provided Vendor and device IDs are matched. All the initialization work is done here.

    :param struct sdio_func \*pfunction:
        Pointer to the sdio_func structure.

    :param const struct sdio_device_id \*id:
        Pointer to sdio_device_id structure.

.. _`rsi_probe.return`:

Return
------

0 on success, 1 on failure.

.. _`rsi_disconnect`:

rsi_disconnect
==============

.. c:function:: void rsi_disconnect(struct sdio_func *pfunction)

    This function performs the reverse of the probe function.

    :param struct sdio_func \*pfunction:
        Pointer to the sdio_func structure.

.. _`rsi_disconnect.return`:

Return
------

void.

.. _`rsi_module_init`:

rsi_module_init
===============

.. c:function:: int rsi_module_init( void)

    This function registers the sdio module.

    :param  void:
        no arguments

.. _`rsi_module_init.return`:

Return
------

0 on success.

.. _`rsi_module_exit`:

rsi_module_exit
===============

.. c:function:: void rsi_module_exit( void)

    This function unregisters the sdio module.

    :param  void:
        no arguments

.. _`rsi_module_exit.return`:

Return
------

None.

.. This file was automatic generated / don't edit.

