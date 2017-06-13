.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/neterion/s2io.c

.. _`init_shared_mem`:

init_shared_mem
===============

.. c:function:: int init_shared_mem(struct s2io_nic *nic)

    Allocation and Initialization of Memory

    :param struct s2io_nic \*nic:
        Device private variable.

.. _`init_shared_mem.description`:

Description
-----------

The function allocates all the memory areas shared
between the NIC and the driver. This includes Tx descriptors,
Rx descriptors and the statistics block.

.. _`free_shared_mem`:

free_shared_mem
===============

.. c:function:: void free_shared_mem(struct s2io_nic *nic)

    Free the allocated Memory

    :param struct s2io_nic \*nic:
        Device private variable.

.. _`free_shared_mem.description`:

Description
-----------

This function is to free all memory locations allocated by
the \ :c:func:`init_shared_mem`\  function and return it to the kernel.

.. _`s2io_verify_pci_mode`:

s2io_verify_pci_mode
====================

.. c:function:: int s2io_verify_pci_mode(struct s2io_nic *nic)

    :param struct s2io_nic \*nic:
        *undescribed*

.. _`s2io_print_pci_mode`:

s2io_print_pci_mode
===================

.. c:function:: int s2io_print_pci_mode(struct s2io_nic *nic)

    :param struct s2io_nic \*nic:
        *undescribed*

.. _`init_tti`:

init_tti
========

.. c:function:: int init_tti(struct s2io_nic *nic, int link)

    Initialization transmit traffic interrupt scheme

    :param struct s2io_nic \*nic:
        device private variable

    :param int link:
        link status (UP/DOWN) used to enable/disable continuous
        transmit interrupts

.. _`init_tti.description`:

Description
-----------

The function configures transmit traffic interrupts

.. _`init_tti.return-value`:

Return Value
------------

SUCCESS on success and
'-1' on failure

.. _`init_nic`:

init_nic
========

.. c:function:: int init_nic(struct s2io_nic *nic)

    Initialization of hardware

    :param struct s2io_nic \*nic:
        device private variable

.. _`init_nic.description`:

Description
-----------

The function sequentially configures every block
of the H/W from their reset values.

.. _`init_nic.return-value`:

Return Value
------------

SUCCESS on success and
'-1' on failure (endian settings incorrect).

.. _`do_s2io_write_bits`:

do_s2io_write_bits
==================

.. c:function:: void do_s2io_write_bits(u64 value, int flag, void __iomem *addr)

    update alarm bits in alarm register

    :param u64 value:
        alarm bits

    :param int flag:
        interrupt status

    :param void __iomem \*addr:
        address value

.. _`do_s2io_write_bits.description`:

Description
-----------

update alarm bits in alarm register

.. _`do_s2io_write_bits.return-value`:

Return Value
------------

NONE.

.. _`en_dis_able_nic_intrs`:

en_dis_able_nic_intrs
=====================

.. c:function:: void en_dis_able_nic_intrs(struct s2io_nic *nic, u16 mask, int flag)

    Enable or Disable the interrupts

    :param struct s2io_nic \*nic:
        device private variable,

    :param u16 mask:
        A mask indicating which Intr block must be modified and,

    :param int flag:
        A flag indicating whether to enable or disable the Intrs.

.. _`en_dis_able_nic_intrs.description`:

Description
-----------

This function will either disable or enable the interrupts
depending on the flag argument. The mask argument can be used to
enable/disable any Intr block.

.. _`en_dis_able_nic_intrs.return-value`:

Return Value
------------

NONE.

.. _`verify_pcc_quiescent`:

verify_pcc_quiescent
====================

.. c:function:: int verify_pcc_quiescent(struct s2io_nic *sp, int flag)

    Checks for PCC quiescent state

    :param struct s2io_nic \*sp:
        *undescribed*

    :param int flag:
        *undescribed*

.. _`verify_pcc_quiescent.return`:

Return
------

1 If PCC is quiescence
0 If PCC is not quiescence

.. _`verify_xena_quiescence`:

verify_xena_quiescence
======================

.. c:function:: int verify_xena_quiescence(struct s2io_nic *sp)

    Checks whether the H/W is ready

    :param struct s2io_nic \*sp:
        *undescribed*

.. _`verify_xena_quiescence.description`:

Description
-----------

Returns whether the H/W is ready to go or not. Depending
on whether adapter enable bit was written or not the comparison
differs and the calling function passes the input argument flag to
indicate this.

.. _`verify_xena_quiescence.return`:

Return
------

1 If xena is quiescence
0 If Xena is not quiescence

.. _`fix_mac_address`:

fix_mac_address
===============

.. c:function:: void fix_mac_address(struct s2io_nic *sp)

    Fix for Mac addr problem on Alpha platforms

    :param struct s2io_nic \*sp:
        Pointer to device specifc structure
        Description :
        New procedure to clear mac address reading  problems on Alpha platforms

.. _`start_nic`:

start_nic
=========

.. c:function:: int start_nic(struct s2io_nic *nic)

    Turns the device on

    :param struct s2io_nic \*nic:
        device private variable.

.. _`start_nic.description`:

Description
-----------

This function actually turns the device on. Before this  function is
called,all Registers are configured from their reset states
and shared memory is allocated but the NIC is still quiescent. On
calling this function, the device interrupts are cleared and the NIC is
literally switched on by writing into the adapter control register.

.. _`start_nic.return-value`:

Return Value
------------

SUCCESS on success and -1 on failure.

.. _`s2io_txdl_getskb`:

s2io_txdl_getskb
================

.. c:function:: struct sk_buff *s2io_txdl_getskb(struct fifo_info *fifo_data, struct TxD *txdlp, int get_off)

    Get the skb from txdl, unmap and return skb

    :param struct fifo_info \*fifo_data:
        *undescribed*

    :param struct TxD \*txdlp:
        *undescribed*

    :param int get_off:
        *undescribed*

.. _`free_tx_buffers`:

free_tx_buffers
===============

.. c:function:: void free_tx_buffers(struct s2io_nic *nic)

    Free all queued Tx buffers

    :param struct s2io_nic \*nic:
        device private variable.

.. _`free_tx_buffers.description`:

Description
-----------

Free all queued Tx buffers.

.. _`free_tx_buffers.return-value`:

Return Value
------------

void

.. _`stop_nic`:

stop_nic
========

.. c:function:: void stop_nic(struct s2io_nic *nic)

    To stop the nic \ ``nic``\  ; device private variable.

    :param struct s2io_nic \*nic:
        *undescribed*

.. _`stop_nic.description`:

Description
-----------

This function does exactly the opposite of what the \ :c:func:`start_nic`\ 
function does. This function is called to stop the device.

.. _`stop_nic.return-value`:

Return Value
------------

void.

.. _`fill_rx_buffers`:

fill_rx_buffers
===============

.. c:function:: int fill_rx_buffers(struct s2io_nic *nic, struct ring_info *ring, int from_card_up)

    Allocates the Rx side skbs

    :param struct s2io_nic \*nic:
        *undescribed*

    :param struct ring_info \*ring:
        *undescribed*

    :param int from_card_up:
        If this is true, we will map the buffer to get
        the dma address for buf0 and buf1 to give it to the card.
        Else we will sync the already mapped buffer to give it to the card.

.. _`fill_rx_buffers.description`:

Description
-----------

The function allocates Rx side skbs and puts the physical
address of these buffers into the RxD buffer pointers, so that the NIC
can DMA the received frame into these locations.
The NIC supports 3 receive modes, viz
1. single buffer,
2. three buffer and
3. Five buffer modes.
Each mode defines how many fragments the received frame will be split
up into by the NIC. The frame is split into L3 header, L4 Header,
L4 payload in three buffer mode and in 5 buffer mode, L4 payload itself
is split into 3 fragments. As of now only single buffer mode is
supported.

.. _`fill_rx_buffers.return-value`:

Return Value
------------

SUCCESS on success or an appropriate -ve value on failure.

.. _`free_rx_buffers`:

free_rx_buffers
===============

.. c:function:: void free_rx_buffers(struct s2io_nic *sp)

    Frees all Rx buffers

    :param struct s2io_nic \*sp:
        device private variable.

.. _`free_rx_buffers.description`:

Description
-----------

This function will free all Rx buffers allocated by host.

.. _`free_rx_buffers.return-value`:

Return Value
------------

NONE.

.. _`s2io_poll_msix`:

s2io_poll_msix
==============

.. c:function:: int s2io_poll_msix(struct napi_struct *napi, int budget)

    Rx interrupt handler for NAPI support

    :param struct napi_struct \*napi:
        pointer to the napi structure.

    :param int budget:
        The number of packets that were budgeted to be processed
        during  one pass through the 'Poll" function.

.. _`s2io_poll_msix.description`:

Description
-----------

Comes into picture only if NAPI support has been incorporated. It does
the same thing that rx_intr_handler does, but not in a interrupt context
also It will process only a given number of packets.

.. _`s2io_poll_msix.return-value`:

Return value
------------

0 on success and 1 if there are No Rx packets to be processed.

.. _`s2io_netpoll`:

s2io_netpoll
============

.. c:function:: void s2io_netpoll(struct net_device *dev)

    netpoll event handler entry point

    :param struct net_device \*dev:
        pointer to the device structure.

.. _`s2io_netpoll.description`:

Description
-----------

This function will be called by upper layer to check for events on the
interface in situations where interrupts are disabled. It is used for
specific in-kernel networking tasks, such as remote consoles and kernel
debugging over the network (example netdump in RedHat).

.. _`rx_intr_handler`:

rx_intr_handler
===============

.. c:function:: int rx_intr_handler(struct ring_info *ring_data, int budget)

    Rx interrupt handler

    :param struct ring_info \*ring_data:
        *undescribed*

    :param int budget:
        budget for napi processing.

.. _`rx_intr_handler.description`:

Description
-----------

If the interrupt is because of a received frame or if the
receive ring contains fresh as yet un-processed frames,this function is
called. It picks out the RxD at which place the last Rx processing had
stopped and sends the skb to the OSM's Rx handler and then increments
the offset.

.. _`rx_intr_handler.return-value`:

Return Value
------------

No. of napi packets processed.

.. _`tx_intr_handler`:

tx_intr_handler
===============

.. c:function:: void tx_intr_handler(struct fifo_info *fifo_data)

    Transmit interrupt handler

    :param struct fifo_info \*fifo_data:
        *undescribed*

.. _`tx_intr_handler.description`:

Description
-----------

If an interrupt was raised to indicate DMA complete of the
Tx packet, this function is called. It identifies the last TxD
whose buffer was freed and frees all skbs whose data have already
DMA'ed into the NICs internal memory.

.. _`tx_intr_handler.return-value`:

Return Value
------------

NONE

.. _`s2io_mdio_write`:

s2io_mdio_write
===============

.. c:function:: void s2io_mdio_write(u32 mmd_type, u64 addr, u16 value, struct net_device *dev)

    Function to write in to MDIO registers

    :param u32 mmd_type:
        MMD type value (PMA/PMD/WIS/PCS/PHYXS)

    :param u64 addr:
        address value

    :param u16 value:
        data value

    :param struct net_device \*dev:
        pointer to net_device structure

.. _`s2io_mdio_write.description`:

Description
-----------

This function is used to write values to the MDIO registers
NONE

.. _`s2io_mdio_read`:

s2io_mdio_read
==============

.. c:function:: u64 s2io_mdio_read(u32 mmd_type, u64 addr, struct net_device *dev)

    Function to write in to MDIO registers

    :param u32 mmd_type:
        MMD type value (PMA/PMD/WIS/PCS/PHYXS)

    :param u64 addr:
        address value

    :param struct net_device \*dev:
        pointer to net_device structure

.. _`s2io_mdio_read.description`:

Description
-----------

This function is used to read values to the MDIO registers
NONE

.. _`s2io_chk_xpak_counter`:

s2io_chk_xpak_counter
=====================

.. c:function:: void s2io_chk_xpak_counter(u64 *counter, u64 *regs_stat, u32 index, u16 flag, u16 type)

    Function to check the status of the xpak counters

    :param u64 \*counter:
        counter value to be updated

    :param u64 \*regs_stat:
        *undescribed*

    :param u32 index:
        *undescribed*

    :param u16 flag:
        flag to indicate the status

    :param u16 type:
        counter type

.. _`s2io_chk_xpak_counter.description`:

Description
-----------

This function is to check the status of the xpak counters value
NONE

.. _`s2io_updt_xpak_counter`:

s2io_updt_xpak_counter
======================

.. c:function:: void s2io_updt_xpak_counter(struct net_device *dev)

    Function to update the xpak counters

    :param struct net_device \*dev:
        pointer to net_device struct

.. _`s2io_updt_xpak_counter.description`:

Description
-----------

This function is to upate the status of the xpak counters value
NONE

.. _`wait_for_cmd_complete`:

wait_for_cmd_complete
=====================

.. c:function:: int wait_for_cmd_complete(void __iomem *addr, u64 busy_bit, int bit_state)

    waits for a command to complete.

    :param void __iomem \*addr:
        *undescribed*

    :param u64 busy_bit:
        *undescribed*

    :param int bit_state:
        *undescribed*

.. _`wait_for_cmd_complete.description`:

Description
-----------

Function that waits for a command to Write into RMAC
ADDR DATA registers to be completed and returns either success or
error depending on whether the command was complete or not.

.. _`wait_for_cmd_complete.return-value`:

Return value
------------

SUCCESS on success and FAILURE on failure.

.. _`check_pci_device_id`:

check_pci_device_id
===================

.. c:function:: u16 check_pci_device_id(u16 id)

    Checks if the device id is supported

    :param u16 id:
        device id

.. _`check_pci_device_id.description`:

Description
-----------

Function to check if the pci device id is supported by driver.

.. _`check_pci_device_id.return-value`:

Return value
------------

Actual device id if supported else PCI_ANY_ID

.. _`s2io_reset`:

s2io_reset
==========

.. c:function:: void s2io_reset(struct s2io_nic *sp)

    Resets the card.

    :param struct s2io_nic \*sp:
        private member of the device structure.

.. _`s2io_reset.description`:

Description
-----------

Function to Reset the card. This function then also
restores the previously saved PCI configuration space registers as
the card reset also resets the configuration space.

.. _`s2io_reset.return-value`:

Return value
------------

void.

.. _`s2io_set_swapper`:

s2io_set_swapper
================

.. c:function:: int s2io_set_swapper(struct s2io_nic *sp)

    to set the swapper controle on the card

    :param struct s2io_nic \*sp:
        private member of the device structure,
        pointer to the s2io_nic structure.

.. _`s2io_set_swapper.description`:

Description
-----------

Function to set the swapper control on the card
correctly depending on the 'endianness' of the system.

.. _`s2io_set_swapper.return-value`:

Return value
------------

SUCCESS on success and FAILURE on failure.

.. _`s2io_open`:

s2io_open
=========

.. c:function:: int s2io_open(struct net_device *dev)

    open entry point of the driver

    :param struct net_device \*dev:
        pointer to the device structure.

.. _`s2io_open.description`:

Description
-----------

This function is the open entry point of the driver. It mainly calls a
function to allocate Rx buffers and inserts them into the buffer
descriptors and then enables the Rx part of the NIC.

.. _`s2io_open.return-value`:

Return value
------------

0 on success and an appropriate (-)ve integer as defined in errno.h
file on failure.

.. _`s2io_close`:

s2io_close
==========

.. c:function:: int s2io_close(struct net_device *dev)

    close entry point of the driver

    :param struct net_device \*dev:
        device pointer.

.. _`s2io_close.description`:

Description
-----------

This is the stop entry point of the driver. It needs to undo exactly
whatever was done by the open entry point,thus it's usually referred to
as the close function.Among other things this function mainly stops the
Rx side of the NIC and frees all the Rx buffers in the Rx rings.

.. _`s2io_close.return-value`:

Return value
------------

0 on success and an appropriate (-)ve integer as defined in errno.h
file on failure.

.. _`s2io_xmit`:

s2io_xmit
=========

.. c:function:: netdev_tx_t s2io_xmit(struct sk_buff *skb, struct net_device *dev)

    Tx entry point of te driver

    :param struct sk_buff \*skb:
        the socket buffer containing the Tx data.

    :param struct net_device \*dev:
        device pointer.
        Description :
        This function is the Tx entry point of the driver. S2IO NIC supports
        certain protocol assist features on Tx side, namely  CSO, S/G, LSO.

.. _`s2io_xmit.note`:

NOTE
----

when device can't queue the pkt,just the trans_start variable will
not be upadted.

.. _`s2io_xmit.return-value`:

Return value
------------

0 on success & 1 on failure.

.. _`do_s2io_chk_alarm_bit`:

do_s2io_chk_alarm_bit
=====================

.. c:function:: int do_s2io_chk_alarm_bit(u64 value, void __iomem *addr, unsigned long long *cnt)

    Check for alarm and incrment the counter

    :param u64 value:
        alarm bits

    :param void __iomem \*addr:
        address value

    :param unsigned long long \*cnt:
        counter variable

.. _`do_s2io_chk_alarm_bit.description`:

Description
-----------

Check for alarm and increment the counter

.. _`do_s2io_chk_alarm_bit.return-value`:

Return Value
------------

1 - if alarm bit set
0 - if alarm bit is not set

.. _`s2io_handle_errors`:

s2io_handle_errors
==================

.. c:function:: void s2io_handle_errors(void *dev_id)

    Xframe error indication handler

    :param void \*dev_id:
        *undescribed*

.. _`s2io_handle_errors.description`:

Description
-----------

Handle alarms such as loss of link, single or
double ECC errors, critical and serious errors.

.. _`s2io_handle_errors.return-value`:

Return Value
------------

NONE

.. _`s2io_isr`:

s2io_isr
========

.. c:function:: irqreturn_t s2io_isr(int irq, void *dev_id)

    ISR handler of the device .

    :param int irq:
        the irq of the device.

    :param void \*dev_id:
        a void pointer to the dev structure of the NIC.

.. _`s2io_isr.description`:

Description
-----------

This function is the ISR handler of the device. It
identifies the reason for the interrupt and calls the relevant
service routines. As a contongency measure, this ISR allocates the
recv buffers, if their numbers are below the panic value which is
presently set to 25% of the original number of rcv buffers allocated.

.. _`s2io_isr.irq_handled`:

IRQ_HANDLED
-----------

will be returned if IRQ was handled by this routine

.. _`s2io_isr.irq_none`:

IRQ_NONE
--------

will be returned if interrupt is not from our device

.. _`s2io_updt_stats`:

s2io_updt_stats
===============

.. c:function:: void s2io_updt_stats(struct s2io_nic *sp)

    :param struct s2io_nic \*sp:
        *undescribed*

.. _`s2io_get_stats`:

s2io_get_stats
==============

.. c:function:: struct net_device_stats *s2io_get_stats(struct net_device *dev)

    Updates the device statistics structure.

    :param struct net_device \*dev:
        pointer to the device structure.

.. _`s2io_get_stats.description`:

Description
-----------

This function updates the device statistics structure in the s2io_nic
structure and returns a pointer to the same.

.. _`s2io_get_stats.return-value`:

Return value
------------

pointer to the updated net_device_stats structure.

.. _`s2io_set_multicast`:

s2io_set_multicast
==================

.. c:function:: void s2io_set_multicast(struct net_device *dev)

    entry point for multicast address enable/disable.

    :param struct net_device \*dev:
        pointer to the device structure

.. _`s2io_set_multicast.description`:

Description
-----------

This function is a driver entry point which gets called by the kernel
whenever multicast addresses must be enabled/disabled. This also gets
called to set/reset promiscuous mode. Depending on the deivce flag, we
determine, if multicast address must be enabled or if promiscuous mode
is to be disabled etc.

.. _`s2io_set_multicast.return-value`:

Return value
------------

void.

.. _`s2io_set_mac_addr`:

s2io_set_mac_addr
=================

.. c:function:: int s2io_set_mac_addr(struct net_device *dev, void *p)

    driver entry point

    :param struct net_device \*dev:
        *undescribed*

    :param void \*p:
        *undescribed*

.. _`do_s2io_prog_unicast`:

do_s2io_prog_unicast
====================

.. c:function:: int do_s2io_prog_unicast(struct net_device *dev, u8 *addr)

    Programs the Xframe mac address

    :param struct net_device \*dev:
        pointer to the device structure.

    :param u8 \*addr:
        a uchar pointer to the new mac address which is to be set.
        Description : This procedure will program the Xframe to receive
        frames with new Mac Address

.. _`do_s2io_prog_unicast.return-value`:

Return value
------------

SUCCESS on success and an appropriate (-)ve integer
as defined in errno.h file on failure.

.. _`s2io_ethtool_set_link_ksettings`:

s2io_ethtool_set_link_ksettings
===============================

.. c:function:: int s2io_ethtool_set_link_ksettings(struct net_device *dev, const struct ethtool_link_ksettings *cmd)

    Sets different link parameters.

    :param struct net_device \*dev:
        *undescribed*

    :param const struct ethtool_link_ksettings \*cmd:
        pointer to the structure with parameters given by ethtool to set
        link information.

.. _`s2io_ethtool_set_link_ksettings.description`:

Description
-----------

The function sets different link parameters provided by the user onto
the NIC.

.. _`s2io_ethtool_set_link_ksettings.return-value`:

Return value
------------

0 on success.

.. _`s2io_ethtool_get_link_ksettings`:

s2io_ethtool_get_link_ksettings
===============================

.. c:function:: int s2io_ethtool_get_link_ksettings(struct net_device *dev, struct ethtool_link_ksettings *cmd)

    Return link specific information.

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_link_ksettings \*cmd:
        pointer to the structure with parameters given by ethtool
        to return link information.

.. _`s2io_ethtool_get_link_ksettings.description`:

Description
-----------

Returns link specific information like speed, duplex etc.. to ethtool.
Return value :
return 0 on success.

.. _`s2io_ethtool_gdrvinfo`:

s2io_ethtool_gdrvinfo
=====================

.. c:function:: void s2io_ethtool_gdrvinfo(struct net_device *dev, struct ethtool_drvinfo *info)

    Returns driver specific information.

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_drvinfo \*info:
        pointer to the structure with parameters given by ethtool to
        return driver information.

.. _`s2io_ethtool_gdrvinfo.description`:

Description
-----------

Returns driver specefic information like name, version etc.. to ethtool.

.. _`s2io_ethtool_gdrvinfo.return-value`:

Return value
------------

void

.. _`s2io_ethtool_gregs`:

s2io_ethtool_gregs
==================

.. c:function:: void s2io_ethtool_gregs(struct net_device *dev, struct ethtool_regs *regs, void *space)

    dumps the entire space of Xfame into the buffer.

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_regs \*regs:
        pointer to the structure with parameters given by ethtool for
        dumping the registers.

    :param void \*space:
        *undescribed*

.. _`s2io_ethtool_gregs.description`:

Description
-----------

Dumps the entire register space of xFrame NIC into the user given
buffer area.
Return value :
void .

.. _`s2io_ethtool_set_led`:

s2io_ethtool_set_led
====================

.. c:function:: int s2io_ethtool_set_led(struct net_device *dev, enum ethtool_phys_id_state state)

    To physically identify the nic on the system.

    :param struct net_device \*dev:
        network device

    :param enum ethtool_phys_id_state state:
        led setting

.. _`s2io_ethtool_set_led.description`:

Description
-----------

Used to physically identify the NIC on the system.
The Link LED will blink for a time specified by the user for
identification.

.. _`s2io_ethtool_set_led.note`:

NOTE
----

The Link has to be Up to be able to blink the LED. Hence
identification is possible only if it's link is up.

.. _`s2io_ethtool_getpause_data`:

s2io_ethtool_getpause_data
==========================

.. c:function:: void s2io_ethtool_getpause_data(struct net_device *dev, struct ethtool_pauseparam *ep)

    Pause frame frame generation and reception.

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_pauseparam \*ep:
        pointer to the structure with pause parameters given by ethtool.

.. _`s2io_ethtool_getpause_data.description`:

Description
-----------

Returns the Pause frame generation and reception capability of the NIC.

.. _`s2io_ethtool_getpause_data.return-value`:

Return value
------------

void

.. _`s2io_ethtool_setpause_data`:

s2io_ethtool_setpause_data
==========================

.. c:function:: int s2io_ethtool_setpause_data(struct net_device *dev, struct ethtool_pauseparam *ep)

    set/reset pause frame generation.

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_pauseparam \*ep:
        pointer to the structure with pause parameters given by ethtool.

.. _`s2io_ethtool_setpause_data.description`:

Description
-----------

It can be used to set or reset Pause frame generation or reception
support of the NIC.

.. _`s2io_ethtool_setpause_data.return-value`:

Return value
------------

int, returns 0 on Success

.. _`s2io_dev_id`:

S2IO_DEV_ID
===========

.. c:function::  S2IO_DEV_ID()

    reads 4 bytes of data from user given offset.

.. _`s2io_dev_id.description`:

Description
-----------

Will read 4 bytes of data from the user given offset and return the
read data.

.. _`s2io_dev_id.note`:

NOTE
----

Will allow to read only part of the EEPROM visible through the
I2C bus.

.. _`s2io_dev_id.return-value`:

Return value
------------

-1 on failure and 0 on success.

.. _`write_eeprom`:

write_eeprom
============

.. c:function:: int write_eeprom(struct s2io_nic *sp, int off, u64 data, int cnt)

    actually writes the relevant part of the data value.

    :param struct s2io_nic \*sp:
        private member of the device structure, which is a pointer to the
        s2io_nic structure.

    :param int off:
        offset at which the data must be written

    :param u64 data:
        The data that is to be written

    :param int cnt:
        Number of bytes of the data that are actually to be written into
        the Eeprom. (max of 3)

.. _`write_eeprom.description`:

Description
-----------

Actually writes the relevant part of the data value into the Eeprom
through the I2C bus.

.. _`write_eeprom.return-value`:

Return value
------------

0 on success, -1 on failure.

.. _`s2io_ethtool_geeprom`:

s2io_ethtool_geeprom
====================

.. c:function:: int s2io_ethtool_geeprom(struct net_device *dev, struct ethtool_eeprom *eeprom, u8 *data_buf)

    reads the value stored in the Eeprom.

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_eeprom \*eeprom:
        pointer to the user level structure provided by ethtool,
        containing all relevant information.

    :param u8 \*data_buf:
        user defined value to be written into Eeprom.

.. _`s2io_ethtool_geeprom.description`:

Description
-----------

Reads the values stored in the Eeprom at given offset
for a given length. Stores these values int the input argument data
buffer 'data_buf' and returns these to the caller (ethtool.)

.. _`s2io_ethtool_geeprom.return-value`:

Return value
------------

int  0 on success

.. _`s2io_ethtool_seeprom`:

s2io_ethtool_seeprom
====================

.. c:function:: int s2io_ethtool_seeprom(struct net_device *dev, struct ethtool_eeprom *eeprom, u8 *data_buf)

    tries to write the user provided value in Eeprom

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_eeprom \*eeprom:
        pointer to the user level structure provided by ethtool,
        containing all relevant information.
        \ ``data_buf``\  ; user defined value to be written into Eeprom.

    :param u8 \*data_buf:
        *undescribed*

.. _`s2io_ethtool_seeprom.description`:

Description
-----------

Tries to write the user provided value in the Eeprom, at the offset
given by the user.

.. _`s2io_ethtool_seeprom.return-value`:

Return value
------------

0 on success, -EFAULT on failure.

.. _`s2io_register_test`:

s2io_register_test
==================

.. c:function:: int s2io_register_test(struct s2io_nic *sp, uint64_t *data)

    reads and writes into all clock domains.

    :param struct s2io_nic \*sp:
        private member of the device structure, which is a pointer to the
        s2io_nic structure.

    :param uint64_t \*data:
        variable that returns the result of each of the test conducted b
        by the driver.

.. _`s2io_register_test.description`:

Description
-----------

Read and write into all clock domains. The NIC has 3 clock domains,
see that registers in all the three regions are accessible.

.. _`s2io_register_test.return-value`:

Return value
------------

0 on success.

.. _`s2io_eeprom_test`:

s2io_eeprom_test
================

.. c:function:: int s2io_eeprom_test(struct s2io_nic *sp, uint64_t *data)

    to verify that EEprom in the xena can be programmed.

    :param struct s2io_nic \*sp:
        private member of the device structure, which is a pointer to the
        s2io_nic structure.

    :param uint64_t \*data:
        variable that returns the result of each of the test conducted by
        the driver.

.. _`s2io_eeprom_test.description`:

Description
-----------

Verify that EEPROM in the xena can be programmed using I2C_CONTROL
register.

.. _`s2io_eeprom_test.return-value`:

Return value
------------

0 on success.

.. _`s2io_bist_test`:

s2io_bist_test
==============

.. c:function:: int s2io_bist_test(struct s2io_nic *sp, uint64_t *data)

    invokes the MemBist test of the card .

    :param struct s2io_nic \*sp:
        private member of the device structure, which is a pointer to the
        s2io_nic structure.

    :param uint64_t \*data:
        variable that returns the result of each of the test conducted by
        the driver.

.. _`s2io_bist_test.description`:

Description
-----------

This invokes the MemBist test of the card. We give around
2 secs time for the Test to complete. If it's still not complete
within this peiod, we consider that the test failed.

.. _`s2io_bist_test.return-value`:

Return value
------------

0 on success and -1 on failure.

.. _`s2io_link_test`:

s2io_link_test
==============

.. c:function:: int s2io_link_test(struct s2io_nic *sp, uint64_t *data)

    verifies the link state of the nic \ ``sp``\  ; private member of the device structure, which is a pointer to the s2io_nic structure.

    :param struct s2io_nic \*sp:
        *undescribed*

    :param uint64_t \*data:
        variable that returns the result of each of the test conducted by
        the driver.

.. _`s2io_link_test.description`:

Description
-----------

The function verifies the link state of the NIC and updates the input
argument 'data' appropriately.

.. _`s2io_link_test.return-value`:

Return value
------------

0 on success.

.. _`s2io_rldram_test`:

s2io_rldram_test
================

.. c:function:: int s2io_rldram_test(struct s2io_nic *sp, uint64_t *data)

    offline test for access to the RldRam chip on the NIC

    :param struct s2io_nic \*sp:
        private member of the device structure, which is a pointer to the
        s2io_nic structure.

    :param uint64_t \*data:
        variable that returns the result of each of the test
        conducted by the driver.

.. _`s2io_rldram_test.description`:

Description
-----------

This is one of the offline test that tests the read and write
access to the RldRam chip on the NIC.

.. _`s2io_rldram_test.return-value`:

Return value
------------

0 on success.

.. _`s2io_ethtool_test`:

s2io_ethtool_test
=================

.. c:function:: void s2io_ethtool_test(struct net_device *dev, struct ethtool_test *ethtest, uint64_t *data)

    conducts 6 tsets to determine the health of card.

    :param struct net_device \*dev:
        *undescribed*

    :param struct ethtool_test \*ethtest:
        pointer to a ethtool command specific structure that will be
        returned to the user.

    :param uint64_t \*data:
        variable that returns the result of each of the test
        conducted by the driver.

.. _`s2io_ethtool_test.description`:

Description
-----------

This function conducts 6 tests ( 4 offline and 2 online) to determine
the health of the card.

.. _`s2io_ethtool_test.return-value`:

Return value
------------

void

.. _`s2io_ioctl`:

s2io_ioctl
==========

.. c:function:: int s2io_ioctl(struct net_device *dev, struct ifreq *rq, int cmd)

    Entry point for the Ioctl

    :param struct net_device \*dev:
        Device pointer.

    :param struct ifreq \*rq:
        *undescribed*

    :param int cmd:
        This is used to distinguish between the different commands that
        can be passed to the IOCTL functions.

.. _`s2io_ioctl.description`:

Description
-----------

Currently there are no special functionality supported in IOCTL, hence
function always return EOPNOTSUPPORTED

.. _`s2io_change_mtu`:

s2io_change_mtu
===============

.. c:function:: int s2io_change_mtu(struct net_device *dev, int new_mtu)

    entry point to change MTU size for the device.

    :param struct net_device \*dev:
        device pointer.

    :param int new_mtu:
        the new MTU size for the device.

.. _`s2io_change_mtu.description`:

Description
-----------

A driver entry point to change MTU size for the device.
Before changing the MTU the device must be stopped.

.. _`s2io_change_mtu.return-value`:

Return value
------------

0 on success and an appropriate (-)ve integer as defined in errno.h
file on failure.

.. _`s2io_set_link`:

s2io_set_link
=============

.. c:function:: void s2io_set_link(struct work_struct *work)

    Set the LInk status

    :param struct work_struct \*work:
        *undescribed*

.. _`s2io_set_link.description`:

Description
-----------

Sets the link status for the adapter

.. _`s2io_restart_nic`:

s2io_restart_nic
================

.. c:function:: void s2io_restart_nic(struct work_struct *work)

    Resets the NIC.

    :param struct work_struct \*work:
        *undescribed*

.. _`s2io_restart_nic.description`:

Description
-----------

This function is scheduled to be run by the s2io_tx_watchdog
function after 0.5 secs to reset the NIC. The idea is to reduce
the run time of the watch dog routine which is run holding a
spin lock.

.. _`s2io_tx_watchdog`:

s2io_tx_watchdog
================

.. c:function:: void s2io_tx_watchdog(struct net_device *dev)

    Watchdog for transmit side.

    :param struct net_device \*dev:
        Pointer to net device structure

.. _`s2io_tx_watchdog.description`:

Description
-----------

This function is triggered if the Tx Queue is stopped
for a pre-defined amount of time when the Interface is still up.
If the Interface is jammed in such a situation, the hardware is
reset (by s2io_close) and restarted again (by s2io_open) to
overcome any problem that might have been caused in the hardware.

.. _`s2io_tx_watchdog.return-value`:

Return value
------------

void

.. _`rx_osm_handler`:

rx_osm_handler
==============

.. c:function:: int rx_osm_handler(struct ring_info *ring_data, struct RxD_t *rxdp)

    To perform some OS related operations on SKB.

    :param struct ring_info \*ring_data:
        *undescribed*

    :param struct RxD_t \*rxdp:
        *undescribed*

.. _`rx_osm_handler.description`:

Description
-----------

This function is called by the Rx interrupt serivce routine to perform
some OS related operations on the SKB before passing it to the upper
layers. It mainly checks if the checksum is OK, if so adds it to the
SKBs cksum variable, increments the Rx packet count and passes the SKB
to the upper layer. If the checksum is wrong, it increments the Rx
packet error count, frees the SKB and returns error.

.. _`rx_osm_handler.return-value`:

Return value
------------

SUCCESS on success and -1 on failure.

.. _`s2io_link`:

s2io_link
=========

.. c:function:: void s2io_link(struct s2io_nic *sp, int link)

    stops/starts the Tx queue.

    :param struct s2io_nic \*sp:
        private member of the device structure, which is a pointer to the
        s2io_nic structure.

    :param int link:
        inidicates whether link is UP/DOWN.

.. _`s2io_link.description`:

Description
-----------

This function stops/starts the Tx queue depending on whether the link
status of the NIC is is down or up. This is called by the Alarm
interrupt handler whenever a link change interrupt comes up.

.. _`s2io_link.return-value`:

Return value
------------

void.

.. _`s2io_init_pci`:

s2io_init_pci
=============

.. c:function:: void s2io_init_pci(struct s2io_nic *sp)

    Initialization of PCI and PCI-X configuration registers .

    :param struct s2io_nic \*sp:
        private member of the device structure, which is a pointer to the
        s2io_nic structure.

.. _`s2io_init_pci.description`:

Description
-----------

This function initializes a few of the PCI and PCI-X configuration registers
with recommended values.

.. _`s2io_init_pci.return-value`:

Return value
------------

void

.. _`rts_ds_steer`:

rts_ds_steer
============

.. c:function:: int rts_ds_steer(struct s2io_nic *nic, u8 ds_codepoint, u8 ring)

    Receive traffic steering based on IPv4 or IPv6 TOS or Traffic class respectively.

    :param struct s2io_nic \*nic:
        device private variable

    :param u8 ds_codepoint:
        *undescribed*

    :param u8 ring:
        *undescribed*

.. _`rts_ds_steer.description`:

Description
-----------

The function configures the receive steering to
desired receive ring.

.. _`rts_ds_steer.return-value`:

Return Value
------------

SUCCESS on success and
'-1' on failure (endian settings incorrect).

.. _`s2io_init_nic`:

s2io_init_nic
=============

.. c:function:: int s2io_init_nic(struct pci_dev *pdev, const struct pci_device_id *pre)

    Initialization of the adapter .

    :param struct pci_dev \*pdev:
        structure containing the PCI related information of the device.

    :param const struct pci_device_id \*pre:
        List of PCI devices supported by the driver listed in s2io_tbl.

.. _`s2io_init_nic.description`:

Description
-----------

The function initializes an adapter identified by the pci_dec structure.
All OS related initialization including memory and device structure and
initlaization of the device private variable is done. Also the swapper
control register is initialized to enable read and write into the I/O
registers of the device.

.. _`s2io_init_nic.return-value`:

Return value
------------

returns 0 on success and negative on failure.

.. _`s2io_rem_nic`:

s2io_rem_nic
============

.. c:function:: void s2io_rem_nic(struct pci_dev *pdev)

    Free the PCI device

    :param struct pci_dev \*pdev:
        structure containing the PCI related information of the device.

.. _`s2io_rem_nic.description`:

Description
-----------

This function is called by the Pci subsystem to release a
PCI device and free up all resource held up by the device. This could
be in response to a Hot plug event or when the driver is to be removed
from memory.

.. _`s2io_io_error_detected`:

s2io_io_error_detected
======================

.. c:function:: pci_ers_result_t s2io_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        Pointer to PCI device

    :param pci_channel_state_t state:
        The current pci connection state

.. _`s2io_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`s2io_io_slot_reset`:

s2io_io_slot_reset
==================

.. c:function:: pci_ers_result_t s2io_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`s2io_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot.
At this point, the card has exprienced a hard reset,
followed by fixups by BIOS, and has its config space
set up identically to what it was at cold boot.

.. _`s2io_io_resume`:

s2io_io_resume
==============

.. c:function:: void s2io_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`s2io_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells
us that its OK to resume normal operation.

.. This file was automatic generated / don't edit.

