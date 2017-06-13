.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb3/t3_hw.c

.. _`t3_wait_op_done_val`:

t3_wait_op_done_val
===================

.. c:function:: int t3_wait_op_done_val(struct adapter *adapter, int reg, u32 mask, int polarity, int attempts, int delay, u32 *valp)

    wait until an operation is completed

    :param struct adapter \*adapter:
        the adapter performing the operation

    :param int reg:
        the register to check for completion

    :param u32 mask:
        a single-bit field within \ ``reg``\  that indicates completion

    :param int polarity:
        the value of the field when the operation is completed

    :param int attempts:
        number of check iterations

    :param int delay:
        delay in usecs between iterations

    :param u32 \*valp:
        where to store the value of the register at completion time

.. _`t3_wait_op_done_val.description`:

Description
-----------

Wait until an operation is completed by checking a bit in a register
up to \ ``attempts``\  times.  If \ ``valp``\  is not NULL the value of the register
at the time it indicated completion is stored there.  Returns 0 if the
operation completes and -EAGAIN otherwise.

.. _`t3_write_regs`:

t3_write_regs
=============

.. c:function:: void t3_write_regs(struct adapter *adapter, const struct addr_val_pair *p, int n, unsigned int offset)

    write a bunch of registers

    :param struct adapter \*adapter:
        the adapter to program

    :param const struct addr_val_pair \*p:
        an array of register address/register value pairs

    :param int n:
        the number of address/value pairs

    :param unsigned int offset:
        register address offset

.. _`t3_write_regs.description`:

Description
-----------

Takes an array of register address/register value pairs and writes each
value to the corresponding register.  Register addresses are adjusted
by the supplied offset.

.. _`t3_set_reg_field`:

t3_set_reg_field
================

.. c:function:: void t3_set_reg_field(struct adapter *adapter, unsigned int addr, u32 mask, u32 val)

    set a register field to a value

    :param struct adapter \*adapter:
        the adapter to program

    :param unsigned int addr:
        the register address

    :param u32 mask:
        specifies the portion of the register to modify

    :param u32 val:
        the new value for the register field

.. _`t3_set_reg_field.description`:

Description
-----------

Sets a register field specified by the supplied mask to the
given value.

.. _`t3_read_indirect`:

t3_read_indirect
================

.. c:function:: void t3_read_indirect(struct adapter *adap, unsigned int addr_reg, unsigned int data_reg, u32 *vals, unsigned int nregs, unsigned int start_idx)

    read indirectly addressed registers

    :param struct adapter \*adap:
        the adapter

    :param unsigned int addr_reg:
        register holding the indirect address

    :param unsigned int data_reg:
        register holding the value of the indirect register

    :param u32 \*vals:
        where the read register values are stored

    :param unsigned int nregs:
        how many indirect registers to read

    :param unsigned int start_idx:
        index of first indirect register to read

.. _`t3_read_indirect.description`:

Description
-----------

Reads registers that are accessed indirectly through an address/data
register pair.

.. _`t3_mc7_bd_read`:

t3_mc7_bd_read
==============

.. c:function:: int t3_mc7_bd_read(struct mc7 *mc7, unsigned int start, unsigned int n, u64 *buf)

    read from MC7 through backdoor accesses

    :param struct mc7 \*mc7:
        identifies MC7 to read from

    :param unsigned int start:
        index of first 64-bit word to read

    :param unsigned int n:
        number of 64-bit words to read

    :param u64 \*buf:
        where to store the read result

.. _`t3_mc7_bd_read.description`:

Description
-----------

Read n 64-bit words from MC7 starting at word start, using backdoor
accesses.

.. _`t3_mdio_change_bits`:

t3_mdio_change_bits
===================

.. c:function:: int t3_mdio_change_bits(struct cphy *phy, int mmd, int reg, unsigned int clear, unsigned int set)

    modify the value of a PHY register

    :param struct cphy \*phy:
        the PHY to operate on

    :param int mmd:
        the device address

    :param int reg:
        the register address

    :param unsigned int clear:
        what part of the register value to mask off

    :param unsigned int set:
        what part of the register value to set

.. _`t3_mdio_change_bits.description`:

Description
-----------

Changes the value of a PHY register by applying a mask to its current
value and ORing the result with a new value.

.. _`t3_phy_reset`:

t3_phy_reset
============

.. c:function:: int t3_phy_reset(struct cphy *phy, int mmd, int wait)

    reset a PHY block

    :param struct cphy \*phy:
        the PHY to operate on

    :param int mmd:
        the device address of the PHY block to reset

    :param int wait:
        how long to wait for the reset to complete in 1ms increments

.. _`t3_phy_reset.description`:

Description
-----------

Resets a PHY block and optionally waits for the reset to complete.
\ ``mmd``\  should be 0 for 10/100/1000 PHYs and the device address to reset
for 10G PHYs.

.. _`t3_phy_advertise`:

t3_phy_advertise
================

.. c:function:: int t3_phy_advertise(struct cphy *phy, unsigned int advert)

    set the PHY advertisement registers for autoneg

    :param struct cphy \*phy:
        the PHY to operate on

    :param unsigned int advert:
        bitmap of capabilities the PHY should advertise

.. _`t3_phy_advertise.description`:

Description
-----------

Sets a 10/100/1000 PHY's advertisement registers to advertise the
requested capabilities.

.. _`t3_phy_advertise_fiber`:

t3_phy_advertise_fiber
======================

.. c:function:: int t3_phy_advertise_fiber(struct cphy *phy, unsigned int advert)

    set fiber PHY advertisement register

    :param struct cphy \*phy:
        the PHY to operate on

    :param unsigned int advert:
        bitmap of capabilities the PHY should advertise

.. _`t3_phy_advertise_fiber.description`:

Description
-----------

Sets a fiber PHY's advertisement register to advertise the
requested capabilities.

.. _`t3_set_phy_speed_duplex`:

t3_set_phy_speed_duplex
=======================

.. c:function:: int t3_set_phy_speed_duplex(struct cphy *phy, int speed, int duplex)

    force PHY speed and duplex

    :param struct cphy \*phy:
        the PHY to operate on

    :param int speed:
        requested PHY speed

    :param int duplex:
        requested PHY duplex

.. _`t3_set_phy_speed_duplex.description`:

Description
-----------

Force a 10/100/1000 PHY's speed and duplex.  This also disables
auto-negotiation except for GigE, where auto-negotiation is mandatory.

.. _`t3_seeprom_read`:

t3_seeprom_read
===============

.. c:function:: int t3_seeprom_read(struct adapter *adapter, u32 addr, __le32 *data)

    read a VPD EEPROM location

    :param struct adapter \*adapter:
        adapter to read

    :param u32 addr:
        EEPROM address

    :param __le32 \*data:
        where to store the read data

.. _`t3_seeprom_read.description`:

Description
-----------

Read a 32-bit word from a location in VPD EEPROM using the card's PCI
VPD ROM capability.  A zero is written to the flag bit when the
address is written to the control register.  The hardware device will
set the flag to 1 when 4 bytes have been read into the data register.

.. _`t3_seeprom_write`:

t3_seeprom_write
================

.. c:function:: int t3_seeprom_write(struct adapter *adapter, u32 addr, __le32 data)

    write a VPD EEPROM location

    :param struct adapter \*adapter:
        adapter to write

    :param u32 addr:
        EEPROM address

    :param __le32 data:
        value to write

.. _`t3_seeprom_write.description`:

Description
-----------

Write a 32-bit word to a location in VPD EEPROM using the card's PCI
VPD ROM capability.

.. _`t3_seeprom_wp`:

t3_seeprom_wp
=============

.. c:function:: int t3_seeprom_wp(struct adapter *adapter, int enable)

    enable/disable EEPROM write protection

    :param struct adapter \*adapter:
        the adapter

    :param int enable:
        1 to enable write protection, 0 to disable it

.. _`t3_seeprom_wp.description`:

Description
-----------

Enables or disables write protection on the serial EEPROM.

.. _`get_vpd_params`:

get_vpd_params
==============

.. c:function:: int get_vpd_params(struct adapter *adapter, struct vpd_params *p)

    read VPD parameters from VPD EEPROM

    :param struct adapter \*adapter:
        adapter to read

    :param struct vpd_params \*p:
        where to store the parameters

.. _`get_vpd_params.description`:

Description
-----------

Reads card parameters stored in VPD EEPROM.

.. _`sf1_read`:

sf1_read
========

.. c:function:: int sf1_read(struct adapter *adapter, unsigned int byte_cnt, int cont, u32 *valp)

    read data from the serial flash

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int byte_cnt:
        number of bytes to read

    :param int cont:
        whether another operation will be chained

    :param u32 \*valp:
        where to store the read data

.. _`sf1_read.description`:

Description
-----------

Reads up to 4 bytes of data from the serial flash.  The location of
the read needs to be specified prior to calling this by issuing the
appropriate commands to the serial flash.

.. _`sf1_write`:

sf1_write
=========

.. c:function:: int sf1_write(struct adapter *adapter, unsigned int byte_cnt, int cont, u32 val)

    write data to the serial flash

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int byte_cnt:
        number of bytes to write

    :param int cont:
        whether another operation will be chained

    :param u32 val:
        value to write

.. _`sf1_write.description`:

Description
-----------

Writes up to 4 bytes of data to the serial flash.  The location of
the write needs to be specified prior to calling this by issuing the
appropriate commands to the serial flash.

.. _`flash_wait_op`:

flash_wait_op
=============

.. c:function:: int flash_wait_op(struct adapter *adapter, int attempts, int delay)

    wait for a flash operation to complete

    :param struct adapter \*adapter:
        the adapter

    :param int attempts:
        max number of polls of the status register

    :param int delay:
        delay between polls in ms

.. _`flash_wait_op.description`:

Description
-----------

Wait for a flash operation to complete by polling the status register.

.. _`t3_read_flash`:

t3_read_flash
=============

.. c:function:: int t3_read_flash(struct adapter *adapter, unsigned int addr, unsigned int nwords, u32 *data, int byte_oriented)

    read words from serial flash

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int addr:
        the start address for the read

    :param unsigned int nwords:
        how many 32-bit words to read

    :param u32 \*data:
        where to store the read data

    :param int byte_oriented:
        whether to store data as bytes or as words

.. _`t3_read_flash.description`:

Description
-----------

Read the specified number of 32-bit words from the serial flash.
If \ ``byte_oriented``\  is set the read data is stored as a byte array
(i.e., big-endian), otherwise as 32-bit words in the platform's
natural endianness.

.. _`t3_write_flash`:

t3_write_flash
==============

.. c:function:: int t3_write_flash(struct adapter *adapter, unsigned int addr, unsigned int n, const u8 *data)

    write up to a page of data to the serial flash

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int addr:
        the start address to write

    :param unsigned int n:
        length of data to write

    :param const u8 \*data:
        the data to write

.. _`t3_write_flash.description`:

Description
-----------

Writes up to a page of data (256 bytes) to the serial flash starting
at the given address.

.. _`t3_get_tp_version`:

t3_get_tp_version
=================

.. c:function:: int t3_get_tp_version(struct adapter *adapter, u32 *vers)

    read the tp sram version

    :param struct adapter \*adapter:
        the adapter

    :param u32 \*vers:
        where to place the version

.. _`t3_get_tp_version.description`:

Description
-----------

Reads the protocol sram version from sram.

.. _`t3_check_tpsram_version`:

t3_check_tpsram_version
=======================

.. c:function:: int t3_check_tpsram_version(struct adapter *adapter)

    read the tp sram version

    :param struct adapter \*adapter:
        the adapter

.. _`t3_check_tpsram_version.description`:

Description
-----------

Reads the protocol sram version from flash.

.. _`t3_check_tpsram`:

t3_check_tpsram
===============

.. c:function:: int t3_check_tpsram(struct adapter *adapter, const u8 *tp_sram, unsigned int size)

    check if provided protocol SRAM is compatible with this driver

    :param struct adapter \*adapter:
        the adapter

    :param const u8 \*tp_sram:
        the firmware image to write

    :param unsigned int size:
        image size

.. _`t3_check_tpsram.description`:

Description
-----------

Checks if an adapter's tp sram is compatible with the driver.
Returns 0 if the versions are compatible, a negative error otherwise.

.. _`t3_get_fw_version`:

t3_get_fw_version
=================

.. c:function:: int t3_get_fw_version(struct adapter *adapter, u32 *vers)

    read the firmware version

    :param struct adapter \*adapter:
        the adapter

    :param u32 \*vers:
        where to place the version

.. _`t3_get_fw_version.description`:

Description
-----------

Reads the FW version from flash.

.. _`t3_check_fw_version`:

t3_check_fw_version
===================

.. c:function:: int t3_check_fw_version(struct adapter *adapter)

    check if the FW is compatible with this driver

    :param struct adapter \*adapter:
        the adapter

.. _`t3_check_fw_version.description`:

Description
-----------

Checks if an adapter's FW is compatible with the driver.  Returns 0
if the versions are compatible, a negative error otherwise.

.. _`t3_flash_erase_sectors`:

t3_flash_erase_sectors
======================

.. c:function:: int t3_flash_erase_sectors(struct adapter *adapter, int start, int end)

    erase a range of flash sectors

    :param struct adapter \*adapter:
        the adapter

    :param int start:
        the first sector to erase

    :param int end:
        the last sector to erase

.. _`t3_flash_erase_sectors.description`:

Description
-----------

Erases the sectors in the given range.

.. _`t3_load_fw`:

t3_load_fw
==========

.. c:function:: int t3_load_fw(struct adapter *adapter, const u8 *fw_data, unsigned int size)

    download firmware

    :param struct adapter \*adapter:
        the adapter

    :param const u8 \*fw_data:
        the firmware image to write

    :param unsigned int size:
        image size

.. _`t3_load_fw.description`:

Description
-----------

Write the supplied firmware image to the card's serial flash.

.. _`t3_load_fw.the-fw-image-has-the-following-sections`:

The FW image has the following sections
---------------------------------------

@size - 8 bytes of code and
data, followed by 4 bytes of FW version, followed by the 32-bit
1's complement checksum of the whole image.

.. _`t3_cim_ctl_blk_read`:

t3_cim_ctl_blk_read
===================

.. c:function:: int t3_cim_ctl_blk_read(struct adapter *adap, unsigned int addr, unsigned int n, unsigned int *valp)

    read a block from CIM control region

    :param struct adapter \*adap:
        the adapter

    :param unsigned int addr:
        the start address within the CIM control region

    :param unsigned int n:
        number of words to read

    :param unsigned int \*valp:
        where to store the result

.. _`t3_cim_ctl_blk_read.description`:

Description
-----------

Reads a block of 4-byte words from the CIM control region.

.. _`t3_link_changed`:

t3_link_changed
===============

.. c:function:: void t3_link_changed(struct adapter *adapter, int port_id)

    handle interface link changes

    :param struct adapter \*adapter:
        the adapter

    :param int port_id:
        the port index that changed link state

.. _`t3_link_changed.description`:

Description
-----------

Called when a port's link settings change to propagate the new values
to the associated PHY and MAC.  After performing the common tasks it
invokes an OS-specific handler.

.. _`t3_link_start`:

t3_link_start
=============

.. c:function:: int t3_link_start(struct cphy *phy, struct cmac *mac, struct link_config *lc)

    apply link configuration to MAC/PHY

    :param struct cphy \*phy:
        the PHY to setup

    :param struct cmac \*mac:
        the MAC to setup

    :param struct link_config \*lc:
        the requested link configuration

.. _`t3_link_start.description`:

Description
-----------

Set up a port's MAC and PHY according to a desired link configuration.
- If the PHY can auto-negotiate first decide what to advertise, then
enable/disable auto-negotiation as desired, and reset.
- If the PHY does not auto-negotiate just reset it.
- If auto-negotiation is off set the MAC to the proper speed/duplex/FC,
otherwise do it later based on the outcome of auto-negotiation.

.. _`t3_set_vlan_accel`:

t3_set_vlan_accel
=================

.. c:function:: void t3_set_vlan_accel(struct adapter *adapter, unsigned int ports, int on)

    control HW VLAN extraction

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int ports:
        bitmap of adapter ports to operate on

    :param int on:
        enable (1) or disable (0) HW VLAN extraction

.. _`t3_set_vlan_accel.description`:

Description
-----------

Enables or disables HW extraction of VLAN tags for the given port.

.. _`t3_handle_intr_status`:

t3_handle_intr_status
=====================

.. c:function:: int t3_handle_intr_status(struct adapter *adapter, unsigned int reg, unsigned int mask, const struct intr_info *acts, unsigned long *stats)

    table driven interrupt handler

    :param struct adapter \*adapter:
        the adapter that generated the interrupt

    :param unsigned int reg:
        the interrupt status register to process

    :param unsigned int mask:
        a mask to apply to the interrupt status

    :param const struct intr_info \*acts:
        table of interrupt actions

    :param unsigned long \*stats:
        statistics counters tracking interrupt occurrences

.. _`t3_handle_intr_status.description`:

Description
-----------

A table driven interrupt handler that applies a set of masks to an
interrupt status word and performs the corresponding actions if the
interrupts described by the mask have occurred.  The actions include
optionally printing a warning or alert message, and optionally
incrementing a stat counter.  The table is terminated by an entry
specifying mask 0.  Returns the number of fatal interrupt conditions.

.. _`t3_intr_enable`:

t3_intr_enable
==============

.. c:function:: void t3_intr_enable(struct adapter *adapter)

    enable interrupts

    :param struct adapter \*adapter:
        the adapter whose interrupts should be enabled

.. _`t3_intr_enable.description`:

Description
-----------

Enable interrupts by setting the interrupt enable registers of the
various HW modules and then enabling the top-level interrupt
concentrator.

.. _`t3_intr_disable`:

t3_intr_disable
===============

.. c:function:: void t3_intr_disable(struct adapter *adapter)

    disable a card's interrupts

    :param struct adapter \*adapter:
        the adapter whose interrupts should be disabled

.. _`t3_intr_disable.description`:

Description
-----------

Disable interrupts.  We only disable the top-level interrupt
concentrator and the SGE data interrupts.

.. _`t3_intr_clear`:

t3_intr_clear
=============

.. c:function:: void t3_intr_clear(struct adapter *adapter)

    clear all interrupts

    :param struct adapter \*adapter:
        the adapter whose interrupts should be cleared

.. _`t3_intr_clear.description`:

Description
-----------

Clears all interrupts.

.. _`t3_port_intr_enable`:

t3_port_intr_enable
===================

.. c:function:: void t3_port_intr_enable(struct adapter *adapter, int idx)

    enable port-specific interrupts

    :param struct adapter \*adapter:
        associated adapter

    :param int idx:
        index of port whose interrupts should be enabled

.. _`t3_port_intr_enable.description`:

Description
-----------

Enable port-specific (i.e., MAC and PHY) interrupts for the given
adapter port.

.. _`t3_port_intr_disable`:

t3_port_intr_disable
====================

.. c:function:: void t3_port_intr_disable(struct adapter *adapter, int idx)

    disable port-specific interrupts

    :param struct adapter \*adapter:
        associated adapter

    :param int idx:
        index of port whose interrupts should be disabled

.. _`t3_port_intr_disable.description`:

Description
-----------

Disable port-specific (i.e., MAC and PHY) interrupts for the given
adapter port.

.. _`t3_port_intr_clear`:

t3_port_intr_clear
==================

.. c:function:: void t3_port_intr_clear(struct adapter *adapter, int idx)

    clear port-specific interrupts

    :param struct adapter \*adapter:
        associated adapter

    :param int idx:
        index of port whose interrupts to clear

.. _`t3_port_intr_clear.description`:

Description
-----------

Clear port-specific (i.e., MAC and PHY) interrupts for the given
adapter port.

.. _`t3_sge_write_context`:

t3_sge_write_context
====================

.. c:function:: int t3_sge_write_context(struct adapter *adapter, unsigned int id, unsigned int type)

    write an SGE context

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int id:
        the context id

    :param unsigned int type:
        the context type

.. _`t3_sge_write_context.description`:

Description
-----------

Program an SGE context with the values already loaded in the
CONTEXT_DATA? registers.

.. _`clear_sge_ctxt`:

clear_sge_ctxt
==============

.. c:function:: int clear_sge_ctxt(struct adapter *adap, unsigned int id, unsigned int type)

    completely clear an SGE context

    :param struct adapter \*adap:
        *undescribed*

    :param unsigned int id:
        the context id

    :param unsigned int type:
        the context type

.. _`clear_sge_ctxt.description`:

Description
-----------

Completely clear an SGE context.  Used predominantly at post-reset
initialization.  Note in particular that we don't skip writing to any
"sensitive bits" in the contexts the way that \ :c:func:`t3_sge_write_context`\ 
does ...

.. _`t3_sge_init_ecntxt`:

t3_sge_init_ecntxt
==================

.. c:function:: int t3_sge_init_ecntxt(struct adapter *adapter, unsigned int id, int gts_enable, enum sge_context_type type, int respq, u64 base_addr, unsigned int size, unsigned int token, int gen, unsigned int cidx)

    initialize an SGE egress context

    :param struct adapter \*adapter:
        the adapter to configure

    :param unsigned int id:
        the context id

    :param int gts_enable:
        whether to enable GTS for the context

    :param enum sge_context_type type:
        the egress context type

    :param int respq:
        associated response queue

    :param u64 base_addr:
        base address of queue

    :param unsigned int size:
        number of queue entries

    :param unsigned int token:
        uP token

    :param int gen:
        initial generation value for the context

    :param unsigned int cidx:
        consumer pointer

.. _`t3_sge_init_ecntxt.description`:

Description
-----------

Initialize an SGE egress context and make it ready for use.  If the
platform allows concurrent context operations, the caller is
responsible for appropriate locking.

.. _`t3_sge_init_flcntxt`:

t3_sge_init_flcntxt
===================

.. c:function:: int t3_sge_init_flcntxt(struct adapter *adapter, unsigned int id, int gts_enable, u64 base_addr, unsigned int size, unsigned int bsize, unsigned int cong_thres, int gen, unsigned int cidx)

    initialize an SGE free-buffer list context

    :param struct adapter \*adapter:
        the adapter to configure

    :param unsigned int id:
        the context id

    :param int gts_enable:
        whether to enable GTS for the context

    :param u64 base_addr:
        base address of queue

    :param unsigned int size:
        number of queue entries

    :param unsigned int bsize:
        size of each buffer for this queue

    :param unsigned int cong_thres:
        threshold to signal congestion to upstream producers

    :param int gen:
        initial generation value for the context

    :param unsigned int cidx:
        consumer pointer

.. _`t3_sge_init_flcntxt.description`:

Description
-----------

Initialize an SGE free list context and make it ready for use.  The
caller is responsible for ensuring only one context operation occurs
at a time.

.. _`t3_sge_init_rspcntxt`:

t3_sge_init_rspcntxt
====================

.. c:function:: int t3_sge_init_rspcntxt(struct adapter *adapter, unsigned int id, int irq_vec_idx, u64 base_addr, unsigned int size, unsigned int fl_thres, int gen, unsigned int cidx)

    initialize an SGE response queue context

    :param struct adapter \*adapter:
        the adapter to configure

    :param unsigned int id:
        the context id

    :param int irq_vec_idx:
        MSI-X interrupt vector index, 0 if no MSI-X, -1 if no IRQ

    :param u64 base_addr:
        base address of queue

    :param unsigned int size:
        number of queue entries

    :param unsigned int fl_thres:
        threshold for selecting the normal or jumbo free list

    :param int gen:
        initial generation value for the context

    :param unsigned int cidx:
        consumer pointer

.. _`t3_sge_init_rspcntxt.description`:

Description
-----------

Initialize an SGE response queue context and make it ready for use.
The caller is responsible for ensuring only one context operation
occurs at a time.

.. _`t3_sge_init_cqcntxt`:

t3_sge_init_cqcntxt
===================

.. c:function:: int t3_sge_init_cqcntxt(struct adapter *adapter, unsigned int id, u64 base_addr, unsigned int size, int rspq, int ovfl_mode, unsigned int credits, unsigned int credit_thres)

    initialize an SGE completion queue context

    :param struct adapter \*adapter:
        the adapter to configure

    :param unsigned int id:
        the context id

    :param u64 base_addr:
        base address of queue

    :param unsigned int size:
        number of queue entries

    :param int rspq:
        response queue for async notifications

    :param int ovfl_mode:
        CQ overflow mode

    :param unsigned int credits:
        completion queue credits

    :param unsigned int credit_thres:
        the credit threshold

.. _`t3_sge_init_cqcntxt.description`:

Description
-----------

Initialize an SGE completion queue context and make it ready for use.
The caller is responsible for ensuring only one context operation
occurs at a time.

.. _`t3_sge_enable_ecntxt`:

t3_sge_enable_ecntxt
====================

.. c:function:: int t3_sge_enable_ecntxt(struct adapter *adapter, unsigned int id, int enable)

    enable/disable an SGE egress context

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int id:
        the egress context id

    :param int enable:
        enable (1) or disable (0) the context

.. _`t3_sge_enable_ecntxt.description`:

Description
-----------

Enable or disable an SGE egress context.  The caller is responsible for
ensuring only one context operation occurs at a time.

.. _`t3_sge_disable_fl`:

t3_sge_disable_fl
=================

.. c:function:: int t3_sge_disable_fl(struct adapter *adapter, unsigned int id)

    disable an SGE free-buffer list

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int id:
        the free list context id

.. _`t3_sge_disable_fl.description`:

Description
-----------

Disable an SGE free-buffer list.  The caller is responsible for
ensuring only one context operation occurs at a time.

.. _`t3_sge_disable_rspcntxt`:

t3_sge_disable_rspcntxt
=======================

.. c:function:: int t3_sge_disable_rspcntxt(struct adapter *adapter, unsigned int id)

    disable an SGE response queue

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int id:
        the response queue context id

.. _`t3_sge_disable_rspcntxt.description`:

Description
-----------

Disable an SGE response queue.  The caller is responsible for
ensuring only one context operation occurs at a time.

.. _`t3_sge_disable_cqcntxt`:

t3_sge_disable_cqcntxt
======================

.. c:function:: int t3_sge_disable_cqcntxt(struct adapter *adapter, unsigned int id)

    disable an SGE completion queue

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int id:
        the completion queue context id

.. _`t3_sge_disable_cqcntxt.description`:

Description
-----------

Disable an SGE completion queue.  The caller is responsible for
ensuring only one context operation occurs at a time.

.. _`t3_sge_cqcntxt_op`:

t3_sge_cqcntxt_op
=================

.. c:function:: int t3_sge_cqcntxt_op(struct adapter *adapter, unsigned int id, unsigned int op, unsigned int credits)

    perform an operation on a completion queue context

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int id:
        the context id

    :param unsigned int op:
        the operation to perform

    :param unsigned int credits:
        *undescribed*

.. _`t3_sge_cqcntxt_op.description`:

Description
-----------

Perform the selected operation on an SGE completion queue context.
The caller is responsible for ensuring only one context operation
occurs at a time.

.. _`t3_config_rss`:

t3_config_rss
=============

.. c:function:: void t3_config_rss(struct adapter *adapter, unsigned int rss_config, const u8 *cpus, const u16 *rspq)

    configure Rx packet steering

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int rss_config:
        RSS settings (written to TP_RSS_CONFIG)

    :param const u8 \*cpus:
        values for the CPU lookup table (0xff terminated)

    :param const u16 \*rspq:
        values for the response queue lookup table (0xffff terminated)

.. _`t3_config_rss.description`:

Description
-----------

Programs the receive packet steering logic.  \ ``cpus``\  and \ ``rspq``\  provide
the values for the CPU and response queue lookup tables.  If they
provide fewer values than the size of the tables the supplied values
are used repeatedly until the tables are fully populated.

.. _`t3_tp_set_offload_mode`:

t3_tp_set_offload_mode
======================

.. c:function:: void t3_tp_set_offload_mode(struct adapter *adap, int enable)

    put TP in NIC/offload mode

    :param struct adapter \*adap:
        the adapter

    :param int enable:
        1 to select offload mode, 0 for regular NIC

.. _`t3_tp_set_offload_mode.description`:

Description
-----------

Switches TP to NIC/offload mode.

.. _`pm_num_pages`:

pm_num_pages
============

.. c:function:: unsigned int pm_num_pages(unsigned int mem_size, unsigned int pg_size)

    calculate the number of pages of the payload memory

    :param unsigned int mem_size:
        the size of the payload memory

    :param unsigned int pg_size:
        the size of each payload memory page

.. _`pm_num_pages.description`:

Description
-----------

Calculate the number of pages, each of the given size, that fit in a
memory of the specified size, respecting the HW requirement that the
number of pages must be a multiple of 24.

.. _`partition_mem`:

partition_mem
=============

.. c:function:: void partition_mem(struct adapter *adap, const struct tp_params *p)

    partition memory and configure TP memory settings

    :param struct adapter \*adap:
        the adapter

    :param const struct tp_params \*p:
        the TP parameters

.. _`partition_mem.description`:

Description
-----------

Partitions context and payload memory and configures TP's memory
registers.

.. _`tp_set_timers`:

tp_set_timers
=============

.. c:function:: void tp_set_timers(struct adapter *adap, unsigned int core_clk)

    set TP timing parameters

    :param struct adapter \*adap:
        the adapter to set

    :param unsigned int core_clk:
        the core clock frequency in Hz

.. _`tp_set_timers.description`:

Description
-----------

Set TP's timing parameters, such as the various timer resolutions and
the TCP timer values.

.. _`t3_tp_set_coalescing_size`:

t3_tp_set_coalescing_size
=========================

.. c:function:: int t3_tp_set_coalescing_size(struct adapter *adap, unsigned int size, int psh)

    set receive coalescing size

    :param struct adapter \*adap:
        the adapter

    :param unsigned int size:
        the receive coalescing size

    :param int psh:
        whether a set PSH bit should deliver coalesced data

.. _`t3_tp_set_coalescing_size.description`:

Description
-----------

Set the receive coalescing size and PSH bit handling.

.. _`t3_tp_set_max_rxsize`:

t3_tp_set_max_rxsize
====================

.. c:function:: void t3_tp_set_max_rxsize(struct adapter *adap, unsigned int size)

    set the max receive size

    :param struct adapter \*adap:
        the adapter

    :param unsigned int size:
        the max receive size

.. _`t3_tp_set_max_rxsize.description`:

Description
-----------

Set TP's max receive size.  This is the limit that applies when
receive coalescing is disabled.

.. _`t3_load_mtus`:

t3_load_mtus
============

.. c:function:: void t3_load_mtus(struct adapter *adap, unsigned short mtus, unsigned short alpha, unsigned short beta, unsigned short mtu_cap)

    write the MTU and congestion control HW tables

    :param struct adapter \*adap:
        the adapter

    :param unsigned short mtus:
        the unrestricted values for the MTU table

    :param unsigned short alpha:
        *undescribed*

    :param unsigned short beta:
        the values for the congestion control beta parameter

    :param unsigned short mtu_cap:
        the maximum permitted effective MTU

.. _`t3_load_mtus.description`:

Description
-----------

Write the MTU table with the supplied MTUs capping each at \ :c:type:`struct mtu_cap <mtu_cap>`\ .
Update the high-speed congestion control table with the supplied alpha,
beta, and MTUs.

.. _`t3_tp_get_mib_stats`:

t3_tp_get_mib_stats
===================

.. c:function:: void t3_tp_get_mib_stats(struct adapter *adap, struct tp_mib_stats *tps)

    read TP's MIB counters

    :param struct adapter \*adap:
        the adapter

    :param struct tp_mib_stats \*tps:
        holds the returned counter values

.. _`t3_tp_get_mib_stats.description`:

Description
-----------

Returns the values of TP's MIB counters.

.. _`t3_set_proto_sram`:

t3_set_proto_sram
=================

.. c:function:: int t3_set_proto_sram(struct adapter *adap, const u8 *data)

    set the contents of the protocol sram

    :param struct adapter \*adap:
        *undescribed*

    :param const u8 \*data:
        the protocol image

.. _`t3_set_proto_sram.description`:

Description
-----------

Write the contents of the protocol SRAM.

.. _`t3_config_sched`:

t3_config_sched
===============

.. c:function:: int t3_config_sched(struct adapter *adap, unsigned int kbps, int sched)

    configure a HW traffic scheduler

    :param struct adapter \*adap:
        the adapter

    :param unsigned int kbps:
        target rate in Kbps

    :param int sched:
        the scheduler index

.. _`t3_config_sched.description`:

Description
-----------

Configure a HW scheduler for the target rate

.. _`get_pci_mode`:

get_pci_mode
============

.. c:function:: void get_pci_mode(struct adapter *adapter, struct pci_params *p)

    determine a card's PCI mode

    :param struct adapter \*adapter:
        the adapter

    :param struct pci_params \*p:
        where to store the PCI settings

.. _`get_pci_mode.description`:

Description
-----------

Determines a card's PCI mode and associated parameters, such as speed
and width.

.. _`init_link_config`:

init_link_config
================

.. c:function:: void init_link_config(struct link_config *lc, unsigned int caps)

    initialize a link's SW state

    :param struct link_config \*lc:
        structure holding the link state

    :param unsigned int caps:
        *undescribed*

.. _`init_link_config.description`:

Description
-----------

Initializes the SW state maintained for each link, including the link's
capabilities and default speed/duplex/flow-control/autonegotiation
settings.

.. _`mc7_calc_size`:

mc7_calc_size
=============

.. c:function:: unsigned int mc7_calc_size(u32 cfg)

    calculate MC7 memory size

    :param u32 cfg:
        the MC7 configuration

.. _`mc7_calc_size.description`:

Description
-----------

Calculates the size of an MC7 memory in bytes from the value of its
configuration register.

.. This file was automatic generated / don't edit.

