.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/micrel/ks8851_mll.c

.. _`pr_fmt`:

pr_fmt
======

.. c:function::  pr_fmt( fmt)

    Copyright (c) 2009 Micrel Inc.

    :param  fmt:
        *undescribed*

.. _`pr_fmt.description`:

Description
-----------

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

.. _`ks_tx_hdr`:

union ks_tx_hdr
===============

.. c:type:: struct ks_tx_hdr

    tx header data

.. _`ks_tx_hdr.definition`:

Definition
----------

.. code-block:: c

    union ks_tx_hdr {
        u8 txb;
        __le16 txw;
    }

.. _`ks_tx_hdr.members`:

Members
-------

txb
    The header as bytes

txw
    The header as 16bit, little-endian words

.. _`ks_tx_hdr.description`:

Description
-----------

A dual representation of the tx header data to allow
access to individual bytes, and to allow 16bit accesses
with 16bit alignment.

.. _`ks_rdreg8`:

ks_rdreg8
=========

.. c:function:: u8 ks_rdreg8(struct ks_net *ks, int offset)

    read 8 bit register from device

    :param struct ks_net \*ks:
        The chip information

    :param int offset:
        The register address

.. _`ks_rdreg8.description`:

Description
-----------

Read a 8bit register from the chip, returning the result

.. _`ks_rdreg16`:

ks_rdreg16
==========

.. c:function:: u16 ks_rdreg16(struct ks_net *ks, int offset)

    read 16 bit register from device

    :param struct ks_net \*ks:
        The chip information

    :param int offset:
        The register address

.. _`ks_rdreg16.description`:

Description
-----------

Read a 16bit register from the chip, returning the result

.. _`ks_wrreg8`:

ks_wrreg8
=========

.. c:function:: void ks_wrreg8(struct ks_net *ks, int offset, u8 value)

    write 8bit register value to chip

    :param struct ks_net \*ks:
        The chip information

    :param int offset:
        The register address

    :param u8 value:
        The value to write

.. _`ks_wrreg16`:

ks_wrreg16
==========

.. c:function:: void ks_wrreg16(struct ks_net *ks, int offset, u16 value)

    write 16bit register value to chip

    :param struct ks_net \*ks:
        The chip information

    :param int offset:
        The register address

    :param u16 value:
        The value to write

.. _`ks_inblk`:

ks_inblk
========

.. c:function:: void ks_inblk(struct ks_net *ks, u16 *wptr, u32 len)

    read a block of data from QMU. This is called after sudo DMA mode enabled.

    :param struct ks_net \*ks:
        The chip state

    :param u16 \*wptr:
        buffer address to save data

    :param u32 len:
        length in byte to read

.. _`ks_outblk`:

ks_outblk
=========

.. c:function:: void ks_outblk(struct ks_net *ks, u16 *wptr, u32 len)

    write data to QMU. This is called after sudo DMA mode enabled.

    :param struct ks_net \*ks:
        The chip information

    :param u16 \*wptr:
        buffer address

    :param u32 len:
        length in byte to write

.. _`ks_tx_fifo_space`:

ks_tx_fifo_space
================

.. c:function:: u16 ks_tx_fifo_space(struct ks_net *ks)

    return the available hardware buffer size.

    :param struct ks_net \*ks:
        The chip information

.. _`ks_save_cmd_reg`:

ks_save_cmd_reg
===============

.. c:function:: void ks_save_cmd_reg(struct ks_net *ks)

    save the command register from the cache.

    :param struct ks_net \*ks:
        The chip information

.. _`ks_restore_cmd_reg`:

ks_restore_cmd_reg
==================

.. c:function:: void ks_restore_cmd_reg(struct ks_net *ks)

    restore the command register from the cache and write to hardware register.

    :param struct ks_net \*ks:
        The chip information

.. _`ks_set_powermode`:

ks_set_powermode
================

.. c:function:: void ks_set_powermode(struct ks_net *ks, unsigned pwrmode)

    set power mode of the device

    :param struct ks_net \*ks:
        The chip information

    :param unsigned pwrmode:
        The power mode value to write to KS_PMECR.

.. _`ks_set_powermode.description`:

Description
-----------

Change the power mode of the chip.

.. _`ks_read_config`:

ks_read_config
==============

.. c:function:: void ks_read_config(struct ks_net *ks)

    read chip configuration of bus width.

    :param struct ks_net \*ks:
        The chip information

.. _`ks_soft_reset`:

ks_soft_reset
=============

.. c:function:: void ks_soft_reset(struct ks_net *ks, unsigned op)

    issue one of the soft reset to the device

    :param struct ks_net \*ks:
        The device state.

    :param unsigned op:
        The bit(s) to set in the GRR

.. _`ks_soft_reset.description`:

Description
-----------

Issue the relevant soft-reset command to the device's GRR register
specified by \ ``op``\ .

Note, the delays are in there as a caution to ensure that the reset
has time to take effect and then complete. Since the datasheet does
not currently specify the exact sequence, we have chosen something
that seems to work with our device.

.. _`ks_read_qmu`:

ks_read_qmu
===========

.. c:function:: void ks_read_qmu(struct ks_net *ks, u16 *buf, u32 len)

    read 1 pkt data from the QMU.

    :param struct ks_net \*ks:
        The chip information

    :param u16 \*buf:
        buffer address to save 1 pkt

    :param u32 len:
        Pkt length

.. _`ks_read_qmu.here-is-the-sequence-to-read-1-pkt`:

Here is the sequence to read 1 pkt
----------------------------------

1. set sudo DMA mode
2. read prepend data
3. read pkt data
4. reset sudo DMA Mode

.. _`ks_rcv`:

ks_rcv
======

.. c:function:: void ks_rcv(struct ks_net *ks, struct net_device *netdev)

    read multiple pkts data from the QMU.

    :param struct ks_net \*ks:
        The chip information

    :param struct net_device \*netdev:
        The network device being opened.

.. _`ks_rcv.description`:

Description
-----------

Read all of header information before reading pkt content.
It is not allowed only port of pkts in QMU after issuing
interrupt ack.

.. _`ks_update_link_status`:

ks_update_link_status
=====================

.. c:function:: void ks_update_link_status(struct net_device *netdev, struct ks_net *ks)

    link status update.

    :param struct net_device \*netdev:
        The network device being opened.

    :param struct ks_net \*ks:
        The chip information

.. _`ks_irq`:

ks_irq
======

.. c:function:: irqreturn_t ks_irq(int irq, void *pw)

    device interrupt handler

    :param int irq:
        Interrupt number passed from the IRQ handler.

    :param void \*pw:
        The private word passed to \ :c:func:`register_irq`\ , our struct ks_net.

.. _`ks_irq.description`:

Description
-----------

This is the handler invoked to find out what happened

Read the interrupt status, work out what needs to be done and then clear
any of the interrupts that are not needed.

.. _`ks_net_open`:

ks_net_open
===========

.. c:function:: int ks_net_open(struct net_device *netdev)

    open network device

    :param struct net_device \*netdev:
        The network device being opened.

.. _`ks_net_open.description`:

Description
-----------

Called when the network device is marked active, such as a user executing
'ifconfig up' on the device.

.. _`ks_net_stop`:

ks_net_stop
===========

.. c:function:: int ks_net_stop(struct net_device *netdev)

    close network device

    :param struct net_device \*netdev:
        The device being closed.

.. _`ks_net_stop.description`:

Description
-----------

Called to close down a network device which has been active. Cancell any
work, shutdown the RX and TX process and then place the chip into a low
power state whilst it is not being used.

.. _`ks_write_qmu`:

ks_write_qmu
============

.. c:function:: void ks_write_qmu(struct ks_net *ks, u8 *pdata, u16 len)

    write 1 pkt data to the QMU.

    :param struct ks_net \*ks:
        The chip information

    :param u8 \*pdata:
        buffer address to save 1 pkt

    :param u16 len:
        Pkt length in byte

.. _`ks_write_qmu.here-is-the-sequence-to-write-1-pkt`:

Here is the sequence to write 1 pkt
-----------------------------------

1. set sudo DMA mode
2. write status/length
3. write pkt data
4. reset sudo DMA Mode
5. reset sudo DMA mode
6. Wait until pkt is out

.. _`ks_start_xmit`:

ks_start_xmit
=============

.. c:function:: int ks_start_xmit(struct sk_buff *skb, struct net_device *netdev)

    transmit packet

    :param struct sk_buff \*skb:
        The buffer to transmit

    :param struct net_device \*netdev:
        The device used to transmit the packet.

.. _`ks_start_xmit.description`:

Description
-----------

Called by the network layer to transmit the \ ``skb``\ .
spin_lock_irqsave is required because tx and rx should be mutual exclusive.
So while tx is in-progress, prevent IRQ interrupt from happenning.

.. _`ks_start_rx`:

ks_start_rx
===========

.. c:function:: void ks_start_rx(struct ks_net *ks)

    ready to serve pkts

    :param struct ks_net \*ks:
        The chip information

.. _`ks_stop_rx`:

ks_stop_rx
==========

.. c:function:: void ks_stop_rx(struct ks_net *ks)

    stop to serve pkts

    :param struct ks_net \*ks:
        The chip information

.. _`ks_set_grpaddr`:

ks_set_grpaddr
==============

.. c:function:: void ks_set_grpaddr(struct ks_net *ks)

    set multicast information

    :param struct ks_net \*ks:
        The chip information

.. _`ks_clear_mcast`:

ks_clear_mcast
==============

.. c:function:: void ks_clear_mcast(struct ks_net *ks)

    clear multicast information

    :param struct ks_net \*ks:
        The chip information
        This routine removes all mcast addresses set in the hardware.

.. _`ks_phy_reg`:

ks_phy_reg
==========

.. c:function:: int ks_phy_reg(int reg)

    convert MII register into a KS8851 register

    :param int reg:
        MII register number.

.. _`ks_phy_reg.description`:

Description
-----------

Return the KS8851 register number for the corresponding MII PHY register
if possible. Return zero if the MII register has no direct mapping to the
KS8851 register set.

.. _`ks_phy_read`:

ks_phy_read
===========

.. c:function:: int ks_phy_read(struct net_device *netdev, int phy_addr, int reg)

    MII interface PHY register read.

    :param struct net_device \*netdev:
        The network device the PHY is on.

    :param int phy_addr:
        Address of PHY (ignored as we only have one)

    :param int reg:
        The register to read.

.. _`ks_phy_read.description`:

Description
-----------

This call reads data from the PHY register specified in \ ``reg``\ . Since the
device does not support all the MII registers, the non-existent values
are always returned as zero.

We return zero for unsupported registers as the MII code does not check
the value returned for any error status, and simply returns it to the
caller. The mii-tool that the driver was tested with takes any -ve error
as real PHY capabilities, thus displaying incorrect data to the user.

.. _`ks_read_selftest`:

ks_read_selftest
================

.. c:function:: int ks_read_selftest(struct ks_net *ks)

    read the selftest memory info.

    :param struct ks_net \*ks:
        The device state

.. _`ks_read_selftest.description`:

Description
-----------

Read and check the TX/RX memory selftest information.

.. This file was automatic generated / don't edit.

