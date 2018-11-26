.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb3/t3_hw.c

.. _`t3_wait_op_done_val`:

t3_wait_op_done_val
===================

.. c:function:: int t3_wait_op_done_val(struct adapter *adapter, int reg, u32 mask, int polarity, int attempts, int delay, u32 *valp)

    wait until an operation is completed

    :param adapter:
        the adapter performing the operation
    :type adapter: struct adapter \*

    :param reg:
        the register to check for completion
    :type reg: int

    :param mask:
        a single-bit field within \ ``reg``\  that indicates completion
    :type mask: u32

    :param polarity:
        the value of the field when the operation is completed
    :type polarity: int

    :param attempts:
        number of check iterations
    :type attempts: int

    :param delay:
        delay in usecs between iterations
    :type delay: int

    :param valp:
        where to store the value of the register at completion time
    :type valp: u32 \*

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

    :param adapter:
        the adapter to program
    :type adapter: struct adapter \*

    :param p:
        an array of register address/register value pairs
    :type p: const struct addr_val_pair \*

    :param n:
        the number of address/value pairs
    :type n: int

    :param offset:
        register address offset
    :type offset: unsigned int

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

    :param adapter:
        the adapter to program
    :type adapter: struct adapter \*

    :param addr:
        the register address
    :type addr: unsigned int

    :param mask:
        specifies the portion of the register to modify
    :type mask: u32

    :param val:
        the new value for the register field
    :type val: u32

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param addr_reg:
        register holding the indirect address
    :type addr_reg: unsigned int

    :param data_reg:
        register holding the value of the indirect register
    :type data_reg: unsigned int

    :param vals:
        where the read register values are stored
    :type vals: u32 \*

    :param nregs:
        how many indirect registers to read
    :type nregs: unsigned int

    :param start_idx:
        index of first indirect register to read
    :type start_idx: unsigned int

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

    :param mc7:
        identifies MC7 to read from
    :type mc7: struct mc7 \*

    :param start:
        index of first 64-bit word to read
    :type start: unsigned int

    :param n:
        number of 64-bit words to read
    :type n: unsigned int

    :param buf:
        where to store the read result
    :type buf: u64 \*

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

    :param phy:
        the PHY to operate on
    :type phy: struct cphy \*

    :param mmd:
        the device address
    :type mmd: int

    :param reg:
        the register address
    :type reg: int

    :param clear:
        what part of the register value to mask off
    :type clear: unsigned int

    :param set:
        what part of the register value to set
    :type set: unsigned int

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

    :param phy:
        the PHY to operate on
    :type phy: struct cphy \*

    :param mmd:
        the device address of the PHY block to reset
    :type mmd: int

    :param wait:
        how long to wait for the reset to complete in 1ms increments
    :type wait: int

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

    :param phy:
        the PHY to operate on
    :type phy: struct cphy \*

    :param advert:
        bitmap of capabilities the PHY should advertise
    :type advert: unsigned int

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

    :param phy:
        the PHY to operate on
    :type phy: struct cphy \*

    :param advert:
        bitmap of capabilities the PHY should advertise
    :type advert: unsigned int

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

    :param phy:
        the PHY to operate on
    :type phy: struct cphy \*

    :param speed:
        requested PHY speed
    :type speed: int

    :param duplex:
        requested PHY duplex
    :type duplex: int

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

    :param adapter:
        adapter to read
    :type adapter: struct adapter \*

    :param addr:
        EEPROM address
    :type addr: u32

    :param data:
        where to store the read data
    :type data: __le32 \*

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

    :param adapter:
        adapter to write
    :type adapter: struct adapter \*

    :param addr:
        EEPROM address
    :type addr: u32

    :param data:
        value to write
    :type data: __le32

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param enable:
        1 to enable write protection, 0 to disable it
    :type enable: int

.. _`t3_seeprom_wp.description`:

Description
-----------

Enables or disables write protection on the serial EEPROM.

.. _`get_vpd_params`:

get_vpd_params
==============

.. c:function:: int get_vpd_params(struct adapter *adapter, struct vpd_params *p)

    read VPD parameters from VPD EEPROM

    :param adapter:
        adapter to read
    :type adapter: struct adapter \*

    :param p:
        where to store the parameters
    :type p: struct vpd_params \*

.. _`get_vpd_params.description`:

Description
-----------

Reads card parameters stored in VPD EEPROM.

.. _`sf1_read`:

sf1_read
========

.. c:function:: int sf1_read(struct adapter *adapter, unsigned int byte_cnt, int cont, u32 *valp)

    read data from the serial flash

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param byte_cnt:
        number of bytes to read
    :type byte_cnt: unsigned int

    :param cont:
        whether another operation will be chained
    :type cont: int

    :param valp:
        where to store the read data
    :type valp: u32 \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param byte_cnt:
        number of bytes to write
    :type byte_cnt: unsigned int

    :param cont:
        whether another operation will be chained
    :type cont: int

    :param val:
        value to write
    :type val: u32

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param attempts:
        max number of polls of the status register
    :type attempts: int

    :param delay:
        delay between polls in ms
    :type delay: int

.. _`flash_wait_op.description`:

Description
-----------

Wait for a flash operation to complete by polling the status register.

.. _`t3_read_flash`:

t3_read_flash
=============

.. c:function:: int t3_read_flash(struct adapter *adapter, unsigned int addr, unsigned int nwords, u32 *data, int byte_oriented)

    read words from serial flash

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param addr:
        the start address for the read
    :type addr: unsigned int

    :param nwords:
        how many 32-bit words to read
    :type nwords: unsigned int

    :param data:
        where to store the read data
    :type data: u32 \*

    :param byte_oriented:
        whether to store data as bytes or as words
    :type byte_oriented: int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param addr:
        the start address to write
    :type addr: unsigned int

    :param n:
        length of data to write
    :type n: unsigned int

    :param data:
        the data to write
    :type data: const u8 \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param vers:
        where to place the version
    :type vers: u32 \*

.. _`t3_get_tp_version.description`:

Description
-----------

Reads the protocol sram version from sram.

.. _`t3_check_tpsram_version`:

t3_check_tpsram_version
=======================

.. c:function:: int t3_check_tpsram_version(struct adapter *adapter)

    read the tp sram version

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t3_check_tpsram_version.description`:

Description
-----------

Reads the protocol sram version from flash.

.. _`t3_check_tpsram`:

t3_check_tpsram
===============

.. c:function:: int t3_check_tpsram(struct adapter *adapter, const u8 *tp_sram, unsigned int size)

    check if provided protocol SRAM is compatible with this driver

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param tp_sram:
        the firmware image to write
    :type tp_sram: const u8 \*

    :param size:
        image size
    :type size: unsigned int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param vers:
        where to place the version
    :type vers: u32 \*

.. _`t3_get_fw_version.description`:

Description
-----------

Reads the FW version from flash.

.. _`t3_check_fw_version`:

t3_check_fw_version
===================

.. c:function:: int t3_check_fw_version(struct adapter *adapter)

    check if the FW is compatible with this driver

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param start:
        the first sector to erase
    :type start: int

    :param end:
        the last sector to erase
    :type end: int

.. _`t3_flash_erase_sectors.description`:

Description
-----------

Erases the sectors in the given range.

.. _`t3_load_fw`:

t3_load_fw
==========

.. c:function:: int t3_load_fw(struct adapter *adapter, const u8 *fw_data, unsigned int size)

    download firmware

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param fw_data:
        the firmware image to write
    :type fw_data: const u8 \*

    :param size:
        image size
    :type size: unsigned int

.. _`t3_load_fw.description`:

Description
-----------

Write the supplied firmware image to the card's serial flash.

.. _`t3_load_fw.the-fw-image-has-the-following-sections`:

The FW image has the following sections
---------------------------------------

\ ``size``\  - 8 bytes of code and
data, followed by 4 bytes of FW version, followed by the 32-bit
1's complement checksum of the whole image.

.. _`t3_cim_ctl_blk_read`:

t3_cim_ctl_blk_read
===================

.. c:function:: int t3_cim_ctl_blk_read(struct adapter *adap, unsigned int addr, unsigned int n, unsigned int *valp)

    read a block from CIM control region

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param addr:
        the start address within the CIM control region
    :type addr: unsigned int

    :param n:
        number of words to read
    :type n: unsigned int

    :param valp:
        where to store the result
    :type valp: unsigned int \*

.. _`t3_cim_ctl_blk_read.description`:

Description
-----------

Reads a block of 4-byte words from the CIM control region.

.. _`t3_link_changed`:

t3_link_changed
===============

.. c:function:: void t3_link_changed(struct adapter *adapter, int port_id)

    handle interface link changes

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param port_id:
        the port index that changed link state
    :type port_id: int

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

    :param phy:
        the PHY to setup
    :type phy: struct cphy \*

    :param mac:
        the MAC to setup
    :type mac: struct cmac \*

    :param lc:
        the requested link configuration
    :type lc: struct link_config \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param ports:
        bitmap of adapter ports to operate on
    :type ports: unsigned int

    :param on:
        enable (1) or disable (0) HW VLAN extraction
    :type on: int

.. _`t3_set_vlan_accel.description`:

Description
-----------

Enables or disables HW extraction of VLAN tags for the given port.

.. _`t3_handle_intr_status`:

t3_handle_intr_status
=====================

.. c:function:: int t3_handle_intr_status(struct adapter *adapter, unsigned int reg, unsigned int mask, const struct intr_info *acts, unsigned long *stats)

    table driven interrupt handler

    :param adapter:
        the adapter that generated the interrupt
    :type adapter: struct adapter \*

    :param reg:
        the interrupt status register to process
    :type reg: unsigned int

    :param mask:
        a mask to apply to the interrupt status
    :type mask: unsigned int

    :param acts:
        table of interrupt actions
    :type acts: const struct intr_info \*

    :param stats:
        statistics counters tracking interrupt occurrences
    :type stats: unsigned long \*

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

    :param adapter:
        the adapter whose interrupts should be enabled
    :type adapter: struct adapter \*

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

    :param adapter:
        the adapter whose interrupts should be disabled
    :type adapter: struct adapter \*

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

    :param adapter:
        the adapter whose interrupts should be cleared
    :type adapter: struct adapter \*

.. _`t3_intr_clear.description`:

Description
-----------

Clears all interrupts.

.. _`t3_port_intr_enable`:

t3_port_intr_enable
===================

.. c:function:: void t3_port_intr_enable(struct adapter *adapter, int idx)

    enable port-specific interrupts

    :param adapter:
        associated adapter
    :type adapter: struct adapter \*

    :param idx:
        index of port whose interrupts should be enabled
    :type idx: int

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

    :param adapter:
        associated adapter
    :type adapter: struct adapter \*

    :param idx:
        index of port whose interrupts should be disabled
    :type idx: int

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

    :param adapter:
        associated adapter
    :type adapter: struct adapter \*

    :param idx:
        index of port whose interrupts to clear
    :type idx: int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param id:
        the context id
    :type id: unsigned int

    :param type:
        the context type
    :type type: unsigned int

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

    :param adap:
        *undescribed*
    :type adap: struct adapter \*

    :param id:
        the context id
    :type id: unsigned int

    :param type:
        the context type
    :type type: unsigned int

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

    :param adapter:
        the adapter to configure
    :type adapter: struct adapter \*

    :param id:
        the context id
    :type id: unsigned int

    :param gts_enable:
        whether to enable GTS for the context
    :type gts_enable: int

    :param type:
        the egress context type
    :type type: enum sge_context_type

    :param respq:
        associated response queue
    :type respq: int

    :param base_addr:
        base address of queue
    :type base_addr: u64

    :param size:
        number of queue entries
    :type size: unsigned int

    :param token:
        uP token
    :type token: unsigned int

    :param gen:
        initial generation value for the context
    :type gen: int

    :param cidx:
        consumer pointer
    :type cidx: unsigned int

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

    :param adapter:
        the adapter to configure
    :type adapter: struct adapter \*

    :param id:
        the context id
    :type id: unsigned int

    :param gts_enable:
        whether to enable GTS for the context
    :type gts_enable: int

    :param base_addr:
        base address of queue
    :type base_addr: u64

    :param size:
        number of queue entries
    :type size: unsigned int

    :param bsize:
        size of each buffer for this queue
    :type bsize: unsigned int

    :param cong_thres:
        threshold to signal congestion to upstream producers
    :type cong_thres: unsigned int

    :param gen:
        initial generation value for the context
    :type gen: int

    :param cidx:
        consumer pointer
    :type cidx: unsigned int

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

    :param adapter:
        the adapter to configure
    :type adapter: struct adapter \*

    :param id:
        the context id
    :type id: unsigned int

    :param irq_vec_idx:
        MSI-X interrupt vector index, 0 if no MSI-X, -1 if no IRQ
    :type irq_vec_idx: int

    :param base_addr:
        base address of queue
    :type base_addr: u64

    :param size:
        number of queue entries
    :type size: unsigned int

    :param fl_thres:
        threshold for selecting the normal or jumbo free list
    :type fl_thres: unsigned int

    :param gen:
        initial generation value for the context
    :type gen: int

    :param cidx:
        consumer pointer
    :type cidx: unsigned int

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

    :param adapter:
        the adapter to configure
    :type adapter: struct adapter \*

    :param id:
        the context id
    :type id: unsigned int

    :param base_addr:
        base address of queue
    :type base_addr: u64

    :param size:
        number of queue entries
    :type size: unsigned int

    :param rspq:
        response queue for async notifications
    :type rspq: int

    :param ovfl_mode:
        CQ overflow mode
    :type ovfl_mode: int

    :param credits:
        completion queue credits
    :type credits: unsigned int

    :param credit_thres:
        the credit threshold
    :type credit_thres: unsigned int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param id:
        the egress context id
    :type id: unsigned int

    :param enable:
        enable (1) or disable (0) the context
    :type enable: int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param id:
        the free list context id
    :type id: unsigned int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param id:
        the response queue context id
    :type id: unsigned int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param id:
        the completion queue context id
    :type id: unsigned int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param id:
        the context id
    :type id: unsigned int

    :param op:
        the operation to perform
    :type op: unsigned int

    :param credits:
        *undescribed*
    :type credits: unsigned int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param rss_config:
        RSS settings (written to TP_RSS_CONFIG)
    :type rss_config: unsigned int

    :param cpus:
        values for the CPU lookup table (0xff terminated)
    :type cpus: const u8 \*

    :param rspq:
        values for the response queue lookup table (0xffff terminated)
    :type rspq: const u16 \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param enable:
        1 to select offload mode, 0 for regular NIC
    :type enable: int

.. _`t3_tp_set_offload_mode.description`:

Description
-----------

Switches TP to NIC/offload mode.

.. _`pm_num_pages`:

pm_num_pages
============

.. c:function:: unsigned int pm_num_pages(unsigned int mem_size, unsigned int pg_size)

    calculate the number of pages of the payload memory

    :param mem_size:
        the size of the payload memory
    :type mem_size: unsigned int

    :param pg_size:
        the size of each payload memory page
    :type pg_size: unsigned int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param p:
        the TP parameters
    :type p: const struct tp_params \*

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

    :param adap:
        the adapter to set
    :type adap: struct adapter \*

    :param core_clk:
        the core clock frequency in Hz
    :type core_clk: unsigned int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param size:
        the receive coalescing size
    :type size: unsigned int

    :param psh:
        whether a set PSH bit should deliver coalesced data
    :type psh: int

.. _`t3_tp_set_coalescing_size.description`:

Description
-----------

Set the receive coalescing size and PSH bit handling.

.. _`t3_tp_set_max_rxsize`:

t3_tp_set_max_rxsize
====================

.. c:function:: void t3_tp_set_max_rxsize(struct adapter *adap, unsigned int size)

    set the max receive size

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param size:
        the max receive size
    :type size: unsigned int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mtus:
        the unrestricted values for the MTU table
    :type mtus: unsigned short

    :param alpha:
        *undescribed*
    :type alpha: unsigned short

    :param beta:
        the values for the congestion control beta parameter
    :type beta: unsigned short

    :param mtu_cap:
        the maximum permitted effective MTU
    :type mtu_cap: unsigned short

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param tps:
        holds the returned counter values
    :type tps: struct tp_mib_stats \*

.. _`t3_tp_get_mib_stats.description`:

Description
-----------

Returns the values of TP's MIB counters.

.. _`t3_set_proto_sram`:

t3_set_proto_sram
=================

.. c:function:: int t3_set_proto_sram(struct adapter *adap, const u8 *data)

    set the contents of the protocol sram

    :param adap:
        *undescribed*
    :type adap: struct adapter \*

    :param data:
        the protocol image
    :type data: const u8 \*

.. _`t3_set_proto_sram.description`:

Description
-----------

Write the contents of the protocol SRAM.

.. _`t3_config_sched`:

t3_config_sched
===============

.. c:function:: int t3_config_sched(struct adapter *adap, unsigned int kbps, int sched)

    configure a HW traffic scheduler

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param kbps:
        target rate in Kbps
    :type kbps: unsigned int

    :param sched:
        the scheduler index
    :type sched: int

.. _`t3_config_sched.description`:

Description
-----------

Configure a HW scheduler for the target rate

.. _`get_pci_mode`:

get_pci_mode
============

.. c:function:: void get_pci_mode(struct adapter *adapter, struct pci_params *p)

    determine a card's PCI mode

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param p:
        where to store the PCI settings
    :type p: struct pci_params \*

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

    :param lc:
        structure holding the link state
    :type lc: struct link_config \*

    :param caps:
        *undescribed*
    :type caps: unsigned int

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

    :param cfg:
        the MC7 configuration
    :type cfg: u32

.. _`mc7_calc_size.description`:

Description
-----------

Calculates the size of an MC7 memory in bytes from the value of its
configuration register.

.. This file was automatic generated / don't edit.

