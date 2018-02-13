.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/via/via-velocity.c

.. _`mac_get_cam_mask`:

mac_get_cam_mask
================

.. c:function:: void mac_get_cam_mask(struct mac_regs __iomem *regs, u8 *mask)

    Read a CAM mask

    :param struct mac_regs __iomem \*regs:
        register block for this velocity

    :param u8 \*mask:
        buffer to store mask

.. _`mac_get_cam_mask.description`:

Description
-----------

Fetch the mask bits of the selected CAM and store them into the
provided mask buffer.

.. _`mac_set_cam_mask`:

mac_set_cam_mask
================

.. c:function:: void mac_set_cam_mask(struct mac_regs __iomem *regs, u8 *mask)

    Set a CAM mask

    :param struct mac_regs __iomem \*regs:
        register block for this velocity

    :param u8 \*mask:
        CAM mask to load

.. _`mac_set_cam_mask.description`:

Description
-----------

Store a new mask into a CAM

.. _`mac_set_cam`:

mac_set_cam
===========

.. c:function:: void mac_set_cam(struct mac_regs __iomem *regs, int idx, const u8 *addr)

    set CAM data

    :param struct mac_regs __iomem \*regs:
        register block of this velocity

    :param int idx:
        Cam index

    :param const u8 \*addr:
        2 or 6 bytes of CAM data

.. _`mac_set_cam.description`:

Description
-----------

Load an address or vlan tag into a CAM

.. _`mac_wol_reset`:

mac_wol_reset
=============

.. c:function:: void mac_wol_reset(struct mac_regs __iomem *regs)

    reset WOL after exiting low power

    :param struct mac_regs __iomem \*regs:
        register block of this velocity

.. _`mac_wol_reset.description`:

Description
-----------

Called after we drop out of wake on lan mode in order to
reset the Wake on lan features. This function doesn't restore
the rest of the logic from the result of sleep/wakeup

.. _`get_chip_name`:

get_chip_name
=============

.. c:function:: const char *get_chip_name(enum chip_type chip_id)

    identifier to name

    :param enum chip_type chip_id:
        *undescribed*

.. _`get_chip_name.description`:

Description
-----------

Given a chip identifier return a suitable description. Returns
a pointer a static string valid while the driver is loaded.

.. _`velocity_set_int_opt`:

velocity_set_int_opt
====================

.. c:function:: void velocity_set_int_opt(int *opt, int val, int min, int max, int def, char *name, const char *devname)

    parser for integer options

    :param int \*opt:
        pointer to option value

    :param int val:
        value the user requested (or -1 for default)

    :param int min:
        lowest value allowed

    :param int max:
        highest value allowed

    :param int def:
        default value

    :param char \*name:
        property name

    :param const char \*devname:
        *undescribed*

.. _`velocity_set_int_opt.description`:

Description
-----------

Set an integer property in the module options. This function does
all the verification and checking as well as reporting so that
we don't duplicate code for each option.

.. _`velocity_set_bool_opt`:

velocity_set_bool_opt
=====================

.. c:function:: void velocity_set_bool_opt(u32 *opt, int val, int def, u32 flag, char *name, const char *devname)

    parser for boolean options

    :param u32 \*opt:
        pointer to option value

    :param int val:
        value the user requested (or -1 for default)

    :param int def:
        default value (yes/no)

    :param u32 flag:
        numeric value to set for true.

    :param char \*name:
        property name

    :param const char \*devname:
        *undescribed*

.. _`velocity_set_bool_opt.description`:

Description
-----------

Set a boolean property in the module options. This function does
all the verification and checking as well as reporting so that
we don't duplicate code for each option.

.. _`velocity_get_options`:

velocity_get_options
====================

.. c:function:: void velocity_get_options(struct velocity_opt *opts, int index, const char *devname)

    set options on device

    :param struct velocity_opt \*opts:
        option structure for the device

    :param int index:
        index of option to use in module options array

    :param const char \*devname:
        device name

.. _`velocity_get_options.description`:

Description
-----------

Turn the module and command options into a single structure
for the current device

.. _`velocity_init_cam_filter`:

velocity_init_cam_filter
========================

.. c:function:: void velocity_init_cam_filter(struct velocity_info *vptr)

    initialise CAM

    :param struct velocity_info \*vptr:
        velocity to program

.. _`velocity_init_cam_filter.description`:

Description
-----------

Initialize the content addressable memory used for filters. Load
appropriately according to the presence of VLAN

.. _`velocity_rx_reset`:

velocity_rx_reset
=================

.. c:function:: void velocity_rx_reset(struct velocity_info *vptr)

    handle a receive reset

    :param struct velocity_info \*vptr:
        velocity we are resetting

.. _`velocity_rx_reset.description`:

Description
-----------

Reset the ownership and status for the receive ring side.
Hand all the receive queue to the NIC.

.. _`velocity_get_opt_media_mode`:

velocity_get_opt_media_mode
===========================

.. c:function:: u32 velocity_get_opt_media_mode(struct velocity_info *vptr)

    get media selection

    :param struct velocity_info \*vptr:
        velocity adapter

.. _`velocity_get_opt_media_mode.description`:

Description
-----------

Get the media mode stored in EEPROM or module options and load
mii_status accordingly. The requested link state information
is also returned.

.. _`safe_disable_mii_autopoll`:

safe_disable_mii_autopoll
=========================

.. c:function:: void safe_disable_mii_autopoll(struct mac_regs __iomem *regs)

    autopoll off

    :param struct mac_regs __iomem \*regs:
        velocity registers

.. _`safe_disable_mii_autopoll.description`:

Description
-----------

Turn off the autopoll and wait for it to disable on the chip

.. _`enable_mii_autopoll`:

enable_mii_autopoll
===================

.. c:function:: void enable_mii_autopoll(struct mac_regs __iomem *regs)

    turn on autopolling

    :param struct mac_regs __iomem \*regs:
        velocity registers

.. _`enable_mii_autopoll.description`:

Description
-----------

Enable the MII link status autopoll feature on the Velocity
hardware. Wait for it to enable.

.. _`velocity_mii_read`:

velocity_mii_read
=================

.. c:function:: int velocity_mii_read(struct mac_regs __iomem *regs, u8 index, u16 *data)

    read MII data

    :param struct mac_regs __iomem \*regs:
        velocity registers

    :param u8 index:
        MII register index

    :param u16 \*data:
        buffer for received data

.. _`velocity_mii_read.description`:

Description
-----------

Perform a single read of an MII 16bit register. Returns zero
on success or -ETIMEDOUT if the PHY did not respond.

.. _`mii_check_media_mode`:

mii_check_media_mode
====================

.. c:function:: u32 mii_check_media_mode(struct mac_regs __iomem *regs)

    check media state

    :param struct mac_regs __iomem \*regs:
        velocity registers

.. _`mii_check_media_mode.description`:

Description
-----------

Check the current MII status and determine the link status
accordingly

.. _`velocity_mii_write`:

velocity_mii_write
==================

.. c:function:: int velocity_mii_write(struct mac_regs __iomem *regs, u8 mii_addr, u16 data)

    write MII data

    :param struct mac_regs __iomem \*regs:
        velocity registers

    :param u8 mii_addr:
        *undescribed*

    :param u16 data:
        16bit data for the MII register

.. _`velocity_mii_write.description`:

Description
-----------

Perform a single write to an MII 16bit register. Returns zero
on success or -ETIMEDOUT if the PHY did not respond.

.. _`set_mii_flow_control`:

set_mii_flow_control
====================

.. c:function:: void set_mii_flow_control(struct velocity_info *vptr)

    flow control setup

    :param struct velocity_info \*vptr:
        velocity interface

.. _`set_mii_flow_control.description`:

Description
-----------

Set up the flow control on this interface according to
the supplied user/eeprom options.

.. _`mii_set_auto_on`:

mii_set_auto_on
===============

.. c:function:: void mii_set_auto_on(struct velocity_info *vptr)

    autonegotiate on

    :param struct velocity_info \*vptr:
        velocity

.. _`mii_set_auto_on.description`:

Description
-----------

Enable autonegotation on this interface

.. _`velocity_set_media_mode`:

velocity_set_media_mode
=======================

.. c:function:: int velocity_set_media_mode(struct velocity_info *vptr, u32 mii_status)

    set media mode

    :param struct velocity_info \*vptr:
        *undescribed*

    :param u32 mii_status:
        old MII link state

.. _`velocity_set_media_mode.description`:

Description
-----------

Check the media link state and configure the flow control
PHY and also velocity hardware setup accordingly. In particular
we need to set up CD polling and frame bursting.

.. _`velocity_print_link_status`:

velocity_print_link_status
==========================

.. c:function:: void velocity_print_link_status(struct velocity_info *vptr)

    link status reporting

    :param struct velocity_info \*vptr:
        velocity to report on

.. _`velocity_print_link_status.description`:

Description
-----------

Turn the link status of the velocity card into a kernel log
description of the new link state, detailing speed and duplex
status

.. _`enable_flow_control_ability`:

enable_flow_control_ability
===========================

.. c:function:: void enable_flow_control_ability(struct velocity_info *vptr)

    flow control

    :param struct velocity_info \*vptr:
        veloity to configure

.. _`enable_flow_control_ability.description`:

Description
-----------

Set up flow control according to the flow control options
determined by the eeprom/configuration.

.. _`velocity_soft_reset`:

velocity_soft_reset
===================

.. c:function:: int velocity_soft_reset(struct velocity_info *vptr)

    soft reset

    :param struct velocity_info \*vptr:
        velocity to reset

.. _`velocity_soft_reset.description`:

Description
-----------

Kick off a soft reset of the velocity adapter and then poll
until the reset sequence has completed before returning.

.. _`velocity_set_multi`:

velocity_set_multi
==================

.. c:function:: void velocity_set_multi(struct net_device *dev)

    filter list change callback

    :param struct net_device \*dev:
        network device

.. _`velocity_set_multi.description`:

Description
-----------

Called by the network layer when the filter lists need to change
for a velocity adapter. Reload the CAMs with the new address
filter ruleset.

.. _`mii_init`:

mii_init
========

.. c:function:: void mii_init(struct velocity_info *vptr, u32 mii_status)

    set up MII

    :param struct velocity_info \*vptr:
        velocity adapter

    :param u32 mii_status:
        links tatus

.. _`mii_init.description`:

Description
-----------

Set up the PHY for the current link state.

.. _`setup_queue_timers`:

setup_queue_timers
==================

.. c:function:: void setup_queue_timers(struct velocity_info *vptr)

    Setup interrupt timers

    :param struct velocity_info \*vptr:
        *undescribed*

.. _`setup_queue_timers.description`:

Description
-----------

Setup interrupt frequency during suppression (timeout if the frame
count isn't filled).

.. _`setup_adaptive_interrupts`:

setup_adaptive_interrupts
=========================

.. c:function:: void setup_adaptive_interrupts(struct velocity_info *vptr)

    Setup interrupt suppression

    :param struct velocity_info \*vptr:
        *undescribed*

.. _`setup_adaptive_interrupts.description`:

Description
-----------

\ ``vptr``\  velocity adapter

The velocity is able to suppress interrupt during high interrupt load.
This function turns on that feature.

.. _`velocity_init_registers`:

velocity_init_registers
=======================

.. c:function:: void velocity_init_registers(struct velocity_info *vptr, enum velocity_init_type type)

    initialise MAC registers

    :param struct velocity_info \*vptr:
        velocity to init

    :param enum velocity_init_type type:
        type of initialisation (hot or cold)

.. _`velocity_init_registers.description`:

Description
-----------

Initialise the MAC on a reset or on first set up on the
hardware.

.. _`velocity_init_dma_rings`:

velocity_init_dma_rings
=======================

.. c:function:: int velocity_init_dma_rings(struct velocity_info *vptr)

    set up DMA rings

    :param struct velocity_info \*vptr:
        Velocity to set up

.. _`velocity_init_dma_rings.description`:

Description
-----------

Allocate PCI mapped DMA rings for the receive and transmit layer
to use.

.. _`velocity_alloc_rx_buf`:

velocity_alloc_rx_buf
=====================

.. c:function:: int velocity_alloc_rx_buf(struct velocity_info *vptr, int idx)

    allocate aligned receive buffer

    :param struct velocity_info \*vptr:
        velocity

    :param int idx:
        ring index

.. _`velocity_alloc_rx_buf.description`:

Description
-----------

Allocate a new full sized buffer for the reception of a frame and
map it into PCI space for the hardware to use. The hardware
requires \*64\* byte alignment of the buffer which makes life
less fun than would be ideal.

.. _`velocity_free_rd_ring`:

velocity_free_rd_ring
=====================

.. c:function:: void velocity_free_rd_ring(struct velocity_info *vptr)

    free receive ring

    :param struct velocity_info \*vptr:
        velocity to clean up

.. _`velocity_free_rd_ring.description`:

Description
-----------

Free the receive buffers for each ring slot and any
attached socket buffers that need to go away.

.. _`velocity_init_rd_ring`:

velocity_init_rd_ring
=====================

.. c:function:: int velocity_init_rd_ring(struct velocity_info *vptr)

    set up receive ring

    :param struct velocity_info \*vptr:
        velocity to configure

.. _`velocity_init_rd_ring.description`:

Description
-----------

Allocate and set up the receive buffers for each ring slot and
assign them to the network adapter.

.. _`velocity_init_td_ring`:

velocity_init_td_ring
=====================

.. c:function:: int velocity_init_td_ring(struct velocity_info *vptr)

    set up transmit ring

    :param struct velocity_info \*vptr:
        velocity

.. _`velocity_init_td_ring.description`:

Description
-----------

Set up the transmit ring and chain the ring pointers together.
Returns zero on success or a negative posix errno code for
failure.

.. _`velocity_free_dma_rings`:

velocity_free_dma_rings
=======================

.. c:function:: void velocity_free_dma_rings(struct velocity_info *vptr)

    free PCI ring pointers

    :param struct velocity_info \*vptr:
        Velocity to free from

.. _`velocity_free_dma_rings.description`:

Description
-----------

Clean up the PCI ring buffers allocated to this velocity.

.. _`velocity_free_tx_buf`:

velocity_free_tx_buf
====================

.. c:function:: void velocity_free_tx_buf(struct velocity_info *vptr, struct velocity_td_info *tdinfo, struct tx_desc *td)

    free transmit buffer

    :param struct velocity_info \*vptr:
        velocity

    :param struct velocity_td_info \*tdinfo:
        buffer

    :param struct tx_desc \*td:
        *undescribed*

.. _`velocity_free_tx_buf.description`:

Description
-----------

Release an transmit buffer. If the buffer was preallocated then
recycle it, if not then unmap the buffer.

.. _`velocity_free_td_ring`:

velocity_free_td_ring
=====================

.. c:function:: void velocity_free_td_ring(struct velocity_info *vptr)

    free td ring

    :param struct velocity_info \*vptr:
        velocity

.. _`velocity_free_td_ring.description`:

Description
-----------

Free up the transmit ring for this particular velocity adapter.
We free the ring contents but not the ring itself.

.. _`velocity_error`:

velocity_error
==============

.. c:function:: void velocity_error(struct velocity_info *vptr, int status)

    handle error from controller

    :param struct velocity_info \*vptr:
        velocity

    :param int status:
        card status

.. _`velocity_error.description`:

Description
-----------

Process an error report from the hardware and attempt to recover
the card itself. At the moment we cannot recover from some
theoretically impossible errors but this could be fixed using
the pci_device_failed logic to bounce the hardware

.. _`velocity_tx_srv`:

velocity_tx_srv
===============

.. c:function:: int velocity_tx_srv(struct velocity_info *vptr)

    transmit interrupt service \ ``vptr``\ ; Velocity

    :param struct velocity_info \*vptr:
        *undescribed*

.. _`velocity_tx_srv.description`:

Description
-----------

Scan the queues looking for transmitted packets that
we can complete and clean up. Update any statistics as
necessary/

.. _`velocity_rx_csum`:

velocity_rx_csum
================

.. c:function:: void velocity_rx_csum(struct rx_desc *rd, struct sk_buff *skb)

    checksum process

    :param struct rx_desc \*rd:
        receive packet descriptor

    :param struct sk_buff \*skb:
        network layer packet buffer

.. _`velocity_rx_csum.description`:

Description
-----------

Process the status bits for the received packet and determine
if the checksum was computed and verified by the hardware

.. _`velocity_rx_copy`:

velocity_rx_copy
================

.. c:function:: int velocity_rx_copy(struct sk_buff **rx_skb, int pkt_size, struct velocity_info *vptr)

    in place Rx copy for small packets

    :param struct sk_buff \*\*rx_skb:
        network layer packet buffer candidate

    :param int pkt_size:
        received data size

    :param struct velocity_info \*vptr:
        *undescribed*

.. _`velocity_rx_copy.description`:

Description
-----------

Replace the current skb that is scheduled for Rx processing by a
shorter, immediately allocated skb, if the received packet is small
enough. This function returns a negative value if the received
packet is too big or if memory is exhausted.

.. _`velocity_iph_realign`:

velocity_iph_realign
====================

.. c:function:: void velocity_iph_realign(struct velocity_info *vptr, struct sk_buff *skb, int pkt_size)

    IP header alignment

    :param struct velocity_info \*vptr:
        velocity we are handling

    :param struct sk_buff \*skb:
        network layer packet buffer

    :param int pkt_size:
        received data size

.. _`velocity_iph_realign.description`:

Description
-----------

Align IP header on a 2 bytes boundary. This behavior can be
configured by the user.

.. _`velocity_receive_frame`:

velocity_receive_frame
======================

.. c:function:: int velocity_receive_frame(struct velocity_info *vptr, int idx)

    received packet processor

    :param struct velocity_info \*vptr:
        velocity we are handling

    :param int idx:
        ring index

.. _`velocity_receive_frame.description`:

Description
-----------

A packet has arrived. We process the packet and if appropriate
pass the frame up the network stack

.. _`velocity_rx_srv`:

velocity_rx_srv
===============

.. c:function:: int velocity_rx_srv(struct velocity_info *vptr, int budget_left)

    service RX interrupt

    :param struct velocity_info \*vptr:
        velocity

    :param int budget_left:
        *undescribed*

.. _`velocity_rx_srv.description`:

Description
-----------

Walk the receive ring of the velocity adapter and remove
any received packets from the receive queue. Hand the ring
slots back to the adapter for reuse.

.. _`velocity_intr`:

velocity_intr
=============

.. c:function:: irqreturn_t velocity_intr(int irq, void *dev_instance)

    interrupt callback

    :param int irq:
        interrupt number

    :param void \*dev_instance:
        interrupting device

.. _`velocity_intr.description`:

Description
-----------

Called whenever an interrupt is generated by the velocity
adapter IRQ line. We may not be the source of the interrupt
and need to identify initially if we are, and if not exit as
efficiently as possible.

.. _`velocity_open`:

velocity_open
=============

.. c:function:: int velocity_open(struct net_device *dev)

    interface activation callback

    :param struct net_device \*dev:
        network layer device to open

.. _`velocity_open.description`:

Description
-----------

Called when the network layer brings the interface up. Returns
a negative posix error code on failure, or zero on success.

All the ring allocation and set up is done on open for this
adapter to minimise memory usage when inactive

.. _`velocity_shutdown`:

velocity_shutdown
=================

.. c:function:: void velocity_shutdown(struct velocity_info *vptr)

    shut down the chip

    :param struct velocity_info \*vptr:
        velocity to deactivate

.. _`velocity_shutdown.description`:

Description
-----------

Shuts down the internal operations of the velocity and
disables interrupts, autopolling, transmit and receive

.. _`velocity_change_mtu`:

velocity_change_mtu
===================

.. c:function:: int velocity_change_mtu(struct net_device *dev, int new_mtu)

    MTU change callback

    :param struct net_device \*dev:
        network device

    :param int new_mtu:
        desired MTU

.. _`velocity_change_mtu.description`:

Description
-----------

Handle requests from the networking layer for MTU change on
this interface. It gets called on a change by the network layer.
Return zero for success or negative posix error code.

.. _`velocity_poll_controller`:

velocity_poll_controller
========================

.. c:function:: void velocity_poll_controller(struct net_device *dev)

    Velocity Poll controller function

    :param struct net_device \*dev:
        network device

.. _`velocity_poll_controller.description`:

Description
-----------


Used by NETCONSOLE and other diagnostic tools to allow network I/P
with interrupts disabled.

.. _`velocity_mii_ioctl`:

velocity_mii_ioctl
==================

.. c:function:: int velocity_mii_ioctl(struct net_device *dev, struct ifreq *ifr, int cmd)

    MII ioctl handler

    :param struct net_device \*dev:
        network device

    :param struct ifreq \*ifr:
        the ifreq block for the ioctl

    :param int cmd:
        the command

.. _`velocity_mii_ioctl.description`:

Description
-----------

Process MII requests made via ioctl from the network layer. These
are used by tools like kudzu to interrogate the link state of the
hardware

.. _`velocity_ioctl`:

velocity_ioctl
==============

.. c:function:: int velocity_ioctl(struct net_device *dev, struct ifreq *rq, int cmd)

    ioctl entry point

    :param struct net_device \*dev:
        network device

    :param struct ifreq \*rq:
        interface request ioctl

    :param int cmd:
        command code

.. _`velocity_ioctl.description`:

Description
-----------

Called when the user issues an ioctl request to the network
device in question. The velocity interface supports MII.

.. _`velocity_get_stats`:

velocity_get_stats
==================

.. c:function:: struct net_device_stats *velocity_get_stats(struct net_device *dev)

    statistics callback

    :param struct net_device \*dev:
        network device

.. _`velocity_get_stats.description`:

Description
-----------

Callback from the network layer to allow driver statistics
to be resynchronized with hardware collected state. In the
case of the velocity we need to pull the MIB counters from
the hardware into the counters before letting the network
layer display them.

.. _`velocity_close`:

velocity_close
==============

.. c:function:: int velocity_close(struct net_device *dev)

    close adapter callback

    :param struct net_device \*dev:
        network device

.. _`velocity_close.description`:

Description
-----------

Callback from the network layer when the velocity is being
deactivated by the network layer

.. _`velocity_xmit`:

velocity_xmit
=============

.. c:function:: netdev_tx_t velocity_xmit(struct sk_buff *skb, struct net_device *dev)

    transmit packet callback

    :param struct sk_buff \*skb:
        buffer to transmit

    :param struct net_device \*dev:
        network device

.. _`velocity_xmit.description`:

Description
-----------

Called by the networ layer to request a packet is queued to
the velocity. Returns zero on success.

.. _`velocity_init_info`:

velocity_init_info
==================

.. c:function:: void velocity_init_info(struct velocity_info *vptr, const struct velocity_info_tbl *info)

    init private data

    :param struct velocity_info \*vptr:
        Velocity info

    :param const struct velocity_info_tbl \*info:
        Board type

.. _`velocity_init_info.description`:

Description
-----------

Set up the initial velocity_info struct for the device that has been
discovered.

.. _`velocity_get_pci_info`:

velocity_get_pci_info
=====================

.. c:function:: int velocity_get_pci_info(struct velocity_info *vptr)

    retrieve PCI info for device

    :param struct velocity_info \*vptr:
        velocity device

.. _`velocity_get_pci_info.description`:

Description
-----------

Retrieve the PCI configuration space data that interests us from
the kernel PCI layer

.. _`velocity_get_platform_info`:

velocity_get_platform_info
==========================

.. c:function:: int velocity_get_platform_info(struct velocity_info *vptr)

    retrieve platform info for device

    :param struct velocity_info \*vptr:
        velocity device

.. _`velocity_get_platform_info.description`:

Description
-----------

Retrieve the Platform configuration data that interests us

.. _`velocity_print_info`:

velocity_print_info
===================

.. c:function:: void velocity_print_info(struct velocity_info *vptr)

    per driver data

    :param struct velocity_info \*vptr:
        velocity

.. _`velocity_print_info.description`:

Description
-----------

Print per driver data as the kernel driver finds Velocity
hardware

.. _`velocity_probe`:

velocity_probe
==============

.. c:function:: int velocity_probe(struct device *dev, int irq, const struct velocity_info_tbl *info, enum velocity_bus_type bustype)

    set up discovered velocity device

    :param struct device \*dev:
        *undescribed*

    :param int irq:
        *undescribed*

    :param const struct velocity_info_tbl \*info:
        *undescribed*

    :param enum velocity_bus_type bustype:
        bus that device is connected to

.. _`velocity_probe.description`:

Description
-----------

Configure a discovered adapter from scratch. Return a negative
errno error code on failure paths.

.. _`velocity_remove`:

velocity_remove
===============

.. c:function:: int velocity_remove(struct device *dev)

    device unplug

    :param struct device \*dev:
        device being removed

.. _`velocity_remove.description`:

Description
-----------

Device unload callback. Called on an unplug or on module
unload for each active device that is present. Disconnects
the device from the network layer and frees all the resources

.. _`wol_calc_crc`:

wol_calc_crc
============

.. c:function:: u16 wol_calc_crc(int size, u8 *pattern, u8 *mask_pattern)

    WOL CRC

    :param int size:
        *undescribed*

    :param u8 \*pattern:
        data pattern

    :param u8 \*mask_pattern:
        mask

.. _`wol_calc_crc.description`:

Description
-----------

Compute the wake on lan crc hashes for the packet header
we are interested in.

.. _`velocity_set_wol`:

velocity_set_wol
================

.. c:function:: int velocity_set_wol(struct velocity_info *vptr)

    set up for wake on lan

    :param struct velocity_info \*vptr:
        velocity to set WOL status on

.. _`velocity_set_wol.description`:

Description
-----------

Set a card up for wake on lan either by unicast or by
ARP packet.

.. _`velocity_set_wol.fixme`:

FIXME
-----

check static buffer is safe here

.. _`velocity_save_context`:

velocity_save_context
=====================

.. c:function:: void velocity_save_context(struct velocity_info *vptr, struct velocity_context *context)

    save registers

    :param struct velocity_info \*vptr:
        velocity

    :param struct velocity_context \*context:
        buffer for stored context

.. _`velocity_save_context.description`:

Description
-----------

Retrieve the current configuration from the velocity hardware
and stash it in the context structure, for use by the context
restore functions. This allows us to save things we need across
power down states

.. _`velocity_restore_context`:

velocity_restore_context
========================

.. c:function:: void velocity_restore_context(struct velocity_info *vptr, struct velocity_context *context)

    restore registers

    :param struct velocity_info \*vptr:
        velocity

    :param struct velocity_context \*context:
        buffer for stored context

.. _`velocity_restore_context.description`:

Description
-----------

Reload the register configuration from the velocity context
created by velocity_save_context.

.. _`velocity_ethtool_up`:

velocity_ethtool_up
===================

.. c:function:: int velocity_ethtool_up(struct net_device *dev)

    pre hook for ethtool

    :param struct net_device \*dev:
        network device

.. _`velocity_ethtool_up.description`:

Description
-----------

Called before an ethtool operation. We need to make sure the
chip is out of D3 state before we poke at it.

.. _`velocity_ethtool_down`:

velocity_ethtool_down
=====================

.. c:function:: void velocity_ethtool_down(struct net_device *dev)

    post hook for ethtool

    :param struct net_device \*dev:
        network device

.. _`velocity_ethtool_down.description`:

Description
-----------

Called after an ethtool operation. Restore the chip back to D3
state if it isn't running.

.. _`velocity_init_module`:

velocity_init_module
====================

.. c:function:: int velocity_init_module( void)

    load time function

    :param  void:
        no arguments

.. _`velocity_init_module.description`:

Description
-----------

Called when the velocity module is loaded. The PCI driver
is registered with the PCI layer, and in turn will call
the probe functions for each velocity adapter installed
in the system.

.. _`velocity_cleanup_module`:

velocity_cleanup_module
=======================

.. c:function:: void __exit velocity_cleanup_module( void)

    module unload

    :param  void:
        no arguments

.. _`velocity_cleanup_module.description`:

Description
-----------

When the velocity hardware is unloaded this function is called.
It will clean up the notifiers and the unregister the PCI
driver interface for this hardware. This in turn cleans up
all discovered interfaces before returning from the function

.. This file was automatic generated / don't edit.

