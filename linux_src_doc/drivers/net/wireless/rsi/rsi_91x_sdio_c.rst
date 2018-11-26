.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/rsi/rsi_91x_sdio.c

.. _`rsi_sdio_set_cmd52_arg`:

rsi_sdio_set_cmd52_arg
======================

.. c:function:: u32 rsi_sdio_set_cmd52_arg(bool rw, u8 func, u8 raw, u32 address, u8 writedata)

    This function prepares cmd 52 read/write arg.

    :param rw:
        Read/write
    :type rw: bool

    :param func:
        function number
    :type func: u8

    :param raw:
        indicates whether to perform read after write
    :type raw: u8

    :param address:
        address to which to read/write
    :type address: u32

    :param writedata:
        data to write
    :type writedata: u8

.. _`rsi_sdio_set_cmd52_arg.return`:

Return
------

argument

.. _`rsi_cmd52writebyte`:

rsi_cmd52writebyte
==================

.. c:function:: int rsi_cmd52writebyte(struct mmc_card *card, u32 address, u8 byte)

    This function issues cmd52 byte write onto the card.

    :param card:
        Pointer to the mmc_card.
    :type card: struct mmc_card \*

    :param address:
        Address to write.
    :type address: u32

    :param byte:
        Data to write.
    :type byte: u8

.. _`rsi_cmd52writebyte.return`:

Return
------

Write status.

.. _`rsi_cmd52readbyte`:

rsi_cmd52readbyte
=================

.. c:function:: int rsi_cmd52readbyte(struct mmc_card *card, u32 address, u8 *byte)

    This function issues cmd52 byte read onto the card.

    :param card:
        Pointer to the mmc_card.
    :type card: struct mmc_card \*

    :param address:
        Address to read from.
    :type address: u32

    :param byte:
        Variable to store read value.
    :type byte: u8 \*

.. _`rsi_cmd52readbyte.return`:

Return
------

Read status.

.. _`rsi_issue_sdiocommand`:

rsi_issue_sdiocommand
=====================

.. c:function:: int rsi_issue_sdiocommand(struct sdio_func *func, u32 opcode, u32 arg, u32 flags, u32 *resp)

    This function issues sdio commands.

    :param func:
        Pointer to the sdio_func structure.
    :type func: struct sdio_func \*

    :param opcode:
        Opcode value.
    :type opcode: u32

    :param arg:
        Arguments to pass.
    :type arg: u32

    :param flags:
        Flags which are set.
    :type flags: u32

    :param resp:
        Pointer to store response.
    :type resp: u32 \*

.. _`rsi_issue_sdiocommand.return`:

Return
------

err: command status as 0 or -1.

.. _`rsi_handle_interrupt`:

rsi_handle_interrupt
====================

.. c:function:: void rsi_handle_interrupt(struct sdio_func *function)

    This function is called upon the occurence of an interrupt.

    :param function:
        Pointer to the sdio_func structure.
    :type function: struct sdio_func \*

.. _`rsi_handle_interrupt.return`:

Return
------

None.

.. _`rsi_reset_card`:

rsi_reset_card
==============

.. c:function:: void rsi_reset_card(struct sdio_func *pfunction)

    This function resets and re-initializes the card.

    :param pfunction:
        Pointer to the sdio_func structure.
    :type pfunction: struct sdio_func \*

.. _`rsi_reset_card.return`:

Return
------

None.

.. _`rsi_setclock`:

rsi_setclock
============

.. c:function:: void rsi_setclock(struct rsi_hw *adapter, u32 freq)

    This function sets the clock frequency.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param freq:
        Clock frequency.
    :type freq: u32

.. _`rsi_setclock.return`:

Return
------

None.

.. _`rsi_setblocklength`:

rsi_setblocklength
==================

.. c:function:: int rsi_setblocklength(struct rsi_hw *adapter, u32 length)

    This function sets the host block length.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param length:
        Block length to be set.
    :type length: u32

.. _`rsi_setblocklength.return`:

Return
------

status: 0 on success, -1 on failure.

.. _`rsi_setupcard`:

rsi_setupcard
=============

.. c:function:: int rsi_setupcard(struct rsi_hw *adapter)

    This function queries and sets the card's features.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

.. _`rsi_setupcard.return`:

Return
------

status: 0 on success, -1 on failure.

.. _`rsi_sdio_read_register`:

rsi_sdio_read_register
======================

.. c:function:: int rsi_sdio_read_register(struct rsi_hw *adapter, u32 addr, u8 *data)

    This function reads one byte of information from a register.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param addr:
        Address of the register.
    :type addr: u32

    :param data:
        Pointer to the data that stores the data read.
    :type data: u8 \*

.. _`rsi_sdio_read_register.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_write_register`:

rsi_sdio_write_register
=======================

.. c:function:: int rsi_sdio_write_register(struct rsi_hw *adapter, u8 function, u32 addr, u8 *data)

    This function writes one byte of information into a register.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param function:
        Function Number.
    :type function: u8

    :param addr:
        Address of the register.
    :type addr: u32

    :param data:
        Pointer to the data tha has to be written.
    :type data: u8 \*

.. _`rsi_sdio_write_register.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_ack_intr`:

rsi_sdio_ack_intr
=================

.. c:function:: void rsi_sdio_ack_intr(struct rsi_hw *adapter, u8 int_bit)

    This function acks the interrupt received.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param int_bit:
        Interrupt bit to write into register.
    :type int_bit: u8

.. _`rsi_sdio_ack_intr.return`:

Return
------

None.

.. _`rsi_sdio_read_register_multiple`:

rsi_sdio_read_register_multiple
===============================

.. c:function:: int rsi_sdio_read_register_multiple(struct rsi_hw *adapter, u32 addr, u8 *data, u16 count)

    This function read multiple bytes of information from the SD card.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param addr:
        Address of the register.
    :type addr: u32

    :param data:
        Pointer to the read data.
    :type data: u8 \*

    :param count:
        Number of multiple bytes to be read.
    :type count: u16

.. _`rsi_sdio_read_register_multiple.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_write_register_multiple`:

rsi_sdio_write_register_multiple
================================

.. c:function:: int rsi_sdio_write_register_multiple(struct rsi_hw *adapter, u32 addr, u8 *data, u16 count)

    This function writes multiple bytes of information to the SD card.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param addr:
        Address of the register.
    :type addr: u32

    :param data:
        Pointer to the data that has to be written.
    :type data: u8 \*

    :param count:
        Number of multiple bytes to be written.
    :type count: u16

.. _`rsi_sdio_write_register_multiple.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_host_intf_write_pkt`:

rsi_sdio_host_intf_write_pkt
============================

.. c:function:: int rsi_sdio_host_intf_write_pkt(struct rsi_hw *adapter, u8 *pkt, u32 len)

    This function writes the packet to device.

    :param adapter:
        Pointer to the adapter structure.
    :type adapter: struct rsi_hw \*

    :param pkt:
        Pointer to the data to be written on to the device.
    :type pkt: u8 \*

    :param len:
        length of the data to be written on to the device.
    :type len: u32

.. _`rsi_sdio_host_intf_write_pkt.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_sdio_host_intf_read_pkt`:

rsi_sdio_host_intf_read_pkt
===========================

.. c:function:: int rsi_sdio_host_intf_read_pkt(struct rsi_hw *adapter, u8 *pkt, u32 length)

    This function reads the packet

    :param adapter:
        Pointer to the adapter data structure.
    :type adapter: struct rsi_hw \*

    :param pkt:
        Pointer to the packet data to be read from the the device.
    :type pkt: u8 \*

    :param length:
        Length of the data to be read from the device.
    :type length: u32

.. _`rsi_sdio_host_intf_read_pkt.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_init_sdio_interface`:

rsi_init_sdio_interface
=======================

.. c:function:: int rsi_init_sdio_interface(struct rsi_hw *adapter, struct sdio_func *pfunction)

    This function does init specific to SDIO.

    :param adapter:
        Pointer to the adapter data structure.
    :type adapter: struct rsi_hw \*

    :param pfunction:
        *undescribed*
    :type pfunction: struct sdio_func \*

.. _`rsi_init_sdio_interface.return`:

Return
------

0 on success, -1 on failure.

.. _`rsi_probe`:

rsi_probe
=========

.. c:function:: int rsi_probe(struct sdio_func *pfunction, const struct sdio_device_id *id)

    This function is called by kernel when the driver provided Vendor and device IDs are matched. All the initialization work is done here.

    :param pfunction:
        Pointer to the sdio_func structure.
    :type pfunction: struct sdio_func \*

    :param id:
        Pointer to sdio_device_id structure.
    :type id: const struct sdio_device_id \*

.. _`rsi_probe.return`:

Return
------

0 on success, 1 on failure.

.. _`rsi_disconnect`:

rsi_disconnect
==============

.. c:function:: void rsi_disconnect(struct sdio_func *pfunction)

    This function performs the reverse of the probe function.

    :param pfunction:
        Pointer to the sdio_func structure.
    :type pfunction: struct sdio_func \*

.. _`rsi_disconnect.return`:

Return
------

void.

.. _`rsi_module_init`:

rsi_module_init
===============

.. c:function:: int rsi_module_init( void)

    This function registers the sdio module.

    :param void:
        no arguments
    :type void: 

.. _`rsi_module_init.return`:

Return
------

0 on success.

.. _`rsi_module_exit`:

rsi_module_exit
===============

.. c:function:: void rsi_module_exit( void)

    This function unregisters the sdio module.

    :param void:
        no arguments
    :type void: 

.. _`rsi_module_exit.return`:

Return
------

None.

.. This file was automatic generated / don't edit.

