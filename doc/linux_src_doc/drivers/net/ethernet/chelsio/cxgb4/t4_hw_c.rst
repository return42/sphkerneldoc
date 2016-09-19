.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/t4_hw.c

.. _`t4_wait_op_done_val`:

t4_wait_op_done_val
===================

.. c:function:: int t4_wait_op_done_val(struct adapter *adapter, int reg, u32 mask, int polarity, int attempts, int delay, u32 *valp)

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

.. _`t4_wait_op_done_val.description`:

Description
-----------

Wait until an operation is completed by checking a bit in a register
up to \ ``attempts``\  times.  If \ ``valp``\  is not NULL the value of the register
at the time it indicated completion is stored there.  Returns 0 if the
operation completes and -EAGAIN otherwise.

.. _`t4_set_reg_field`:

t4_set_reg_field
================

.. c:function:: void t4_set_reg_field(struct adapter *adapter, unsigned int addr, u32 mask, u32 val)

    set a register field to a value

    :param struct adapter \*adapter:
        the adapter to program

    :param unsigned int addr:
        the register address

    :param u32 mask:
        specifies the portion of the register to modify

    :param u32 val:
        the new value for the register field

.. _`t4_set_reg_field.description`:

Description
-----------

Sets a register field specified by the supplied mask to the
given value.

.. _`t4_read_indirect`:

t4_read_indirect
================

.. c:function:: void t4_read_indirect(struct adapter *adap, unsigned int addr_reg, unsigned int data_reg, u32 *vals, unsigned int nregs, unsigned int start_idx)

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

.. _`t4_read_indirect.description`:

Description
-----------

Reads registers that are accessed indirectly through an address/data
register pair.

.. _`t4_write_indirect`:

t4_write_indirect
=================

.. c:function:: void t4_write_indirect(struct adapter *adap, unsigned int addr_reg, unsigned int data_reg, const u32 *vals, unsigned int nregs, unsigned int start_idx)

    write indirectly addressed registers

    :param struct adapter \*adap:
        the adapter

    :param unsigned int addr_reg:
        register holding the indirect addresses

    :param unsigned int data_reg:
        register holding the value for the indirect registers

    :param const u32 \*vals:
        values to write

    :param unsigned int nregs:
        how many indirect registers to write

    :param unsigned int start_idx:
        address of first indirect register to write

.. _`t4_write_indirect.description`:

Description
-----------

Writes a sequential block of registers that are accessed indirectly
through an address/data register pair.

.. _`t4_record_mbox`:

t4_record_mbox
==============

.. c:function:: void t4_record_mbox(struct adapter *adapter, const __be64 *cmd, unsigned int size, int access, int execute)

    record a Firmware Mailbox Command/Reply in the log

    :param struct adapter \*adapter:
        the adapter

    :param const __be64 \*cmd:
        the Firmware Mailbox Command or Reply

    :param unsigned int size:
        command length in bytes

    :param int access:
        the time (ms) needed to access the Firmware Mailbox

    :param int execute:
        the time (ms) the command spent being executed

.. _`t4_wr_mbox_meat_timeout`:

t4_wr_mbox_meat_timeout
=======================

.. c:function:: int t4_wr_mbox_meat_timeout(struct adapter *adap, int mbox, const void *cmd, int size, void *rpl, bool sleep_ok, int timeout)

    send a command to FW through the given mailbox

    :param struct adapter \*adap:
        the adapter

    :param int mbox:
        index of the mailbox to use

    :param const void \*cmd:
        the command to write

    :param int size:
        command length in bytes

    :param void \*rpl:
        where to optionally store the reply

    :param bool sleep_ok:
        if true we may sleep while awaiting command completion

    :param int timeout:
        time to wait for command to finish before timing out

.. _`t4_wr_mbox_meat_timeout.description`:

Description
-----------

Sends the given command to FW through the selected mailbox and waits
for the FW to execute the command.  If \ ``rpl``\  is not \ ``NULL``\  it is used to
store the FW's reply to the command.  The command and its optional
reply are of the same length.  FW can take up to \ ``FW_CMD_MAX_TIMEOUT``\  ms
to respond.  \ ``sleep_ok``\  determines whether we may sleep while awaiting
the response.  If sleeping is allowed we use progressive backoff
otherwise we spin.

The return value is 0 on success or a negative errno on failure.  A
failure can happen either because we are not able to execute the
command or FW executes it but signals an error.  In the latter case
the return value is the error code indicated by FW (negated).

.. _`t4_memory_rw`:

t4_memory_rw
============

.. c:function:: int t4_memory_rw(struct adapter *adap, int win, int mtype, u32 addr, u32 len, void *hbuf, int dir)

    read/write EDC 0, EDC 1 or MC via PCIE memory window

    :param struct adapter \*adap:
        the adapter

    :param int win:
        PCI-E Memory Window to use

    :param int mtype:
        memory type: MEM_EDC0, MEM_EDC1 or MEM_MC

    :param u32 addr:
        address within indicated memory type

    :param u32 len:
        amount of memory to transfer

    :param void \*hbuf:
        host memory buffer

    :param int dir:
        direction of transfer T4_MEMORY_READ (1) or T4_MEMORY_WRITE (0)

.. _`t4_memory_rw.description`:

Description
-----------

Reads/writes an [almost] arbitrary memory region in the firmware: the
firmware memory address and host buffer must be aligned on 32-bit
boudaries; the length may be arbitrary.  The memory is transferred as
a raw byte sequence from/to the firmware's memory.  If this memory
contains data structures which contain multi-byte integers, it's the
caller's responsibility to perform appropriate byte order conversions.

.. _`t4_get_regs_len`:

t4_get_regs_len
===============

.. c:function:: unsigned int t4_get_regs_len(struct adapter *adapter)

    return the size of the chips register set

    :param struct adapter \*adapter:
        the adapter

.. _`t4_get_regs_len.description`:

Description
-----------

Returns the size of the chip's BAR0 register space.

.. _`t4_get_regs`:

t4_get_regs
===========

.. c:function:: void t4_get_regs(struct adapter *adap, void *buf, size_t buf_size)

    read chip registers into provided buffer

    :param struct adapter \*adap:
        the adapter

    :param void \*buf:
        register buffer

    :param size_t buf_size:
        size (in bytes) of register buffer

.. _`t4_get_regs.description`:

Description
-----------

If the provided register buffer isn't large enough for the chip's
full register range, the register dump will be truncated to the
register buffer's size.

.. _`t4_seeprom_wp`:

t4_seeprom_wp
=============

.. c:function:: int t4_seeprom_wp(struct adapter *adapter, bool enable)

    enable/disable EEPROM write protection

    :param struct adapter \*adapter:
        the adapter

    :param bool enable:
        whether to enable or disable write protection

.. _`t4_seeprom_wp.description`:

Description
-----------

Enables or disables write protection on the serial EEPROM.

.. _`t4_get_raw_vpd_params`:

t4_get_raw_vpd_params
=====================

.. c:function:: int t4_get_raw_vpd_params(struct adapter *adapter, struct vpd_params *p)

    read VPD parameters from VPD EEPROM

    :param struct adapter \*adapter:
        adapter to read

    :param struct vpd_params \*p:
        where to store the parameters

.. _`t4_get_raw_vpd_params.description`:

Description
-----------

Reads card parameters stored in VPD EEPROM.

.. _`t4_get_vpd_params`:

t4_get_vpd_params
=================

.. c:function:: int t4_get_vpd_params(struct adapter *adapter, struct vpd_params *p)

    read VPD parameters & retrieve Core Clock

    :param struct adapter \*adapter:
        adapter to read

    :param struct vpd_params \*p:
        where to store the parameters

.. _`t4_get_vpd_params.description`:

Description
-----------

Reads card parameters stored in VPD EEPROM and retrieves the Core
Clock.  This can only be called after a connection to the firmware
is established.

.. _`sf1_read`:

sf1_read
========

.. c:function:: int sf1_read(struct adapter *adapter, unsigned int byte_cnt, int cont, int lock, u32 *valp)

    read data from the serial flash

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int byte_cnt:
        number of bytes to read

    :param int cont:
        whether another operation will be chained

    :param int lock:
        whether to lock SF for PL access only

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

.. c:function:: int sf1_write(struct adapter *adapter, unsigned int byte_cnt, int cont, int lock, u32 val)

    write data to the serial flash

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int byte_cnt:
        number of bytes to write

    :param int cont:
        whether another operation will be chained

    :param int lock:
        whether to lock SF for PL access only

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

.. _`t4_read_flash`:

t4_read_flash
=============

.. c:function:: int t4_read_flash(struct adapter *adapter, unsigned int addr, unsigned int nwords, u32 *data, int byte_oriented)

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

.. _`t4_read_flash.description`:

Description
-----------

Read the specified number of 32-bit words from the serial flash.
If \ ``byte_oriented``\  is set the read data is stored as a byte array
(i.e., big-endian), otherwise as 32-bit words in the platform's
natural endianness.

.. _`t4_write_flash`:

t4_write_flash
==============

.. c:function:: int t4_write_flash(struct adapter *adapter, unsigned int addr, unsigned int n, const u8 *data)

    write up to a page of data to the serial flash

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int addr:
        the start address to write

    :param unsigned int n:
        length of data to write in bytes

    :param const u8 \*data:
        the data to write

.. _`t4_write_flash.description`:

Description
-----------

Writes up to a page of data (256 bytes) to the serial flash starting
at the given address.  All the data must be written to the same page.

.. _`t4_get_fw_version`:

t4_get_fw_version
=================

.. c:function:: int t4_get_fw_version(struct adapter *adapter, u32 *vers)

    read the firmware version

    :param struct adapter \*adapter:
        the adapter

    :param u32 \*vers:
        where to place the version

.. _`t4_get_fw_version.description`:

Description
-----------

Reads the FW version from flash.

.. _`t4_get_bs_version`:

t4_get_bs_version
=================

.. c:function:: int t4_get_bs_version(struct adapter *adapter, u32 *vers)

    read the firmware bootstrap version

    :param struct adapter \*adapter:
        the adapter

    :param u32 \*vers:
        where to place the version

.. _`t4_get_bs_version.description`:

Description
-----------

Reads the FW Bootstrap version from flash.

.. _`t4_get_tp_version`:

t4_get_tp_version
=================

.. c:function:: int t4_get_tp_version(struct adapter *adapter, u32 *vers)

    read the TP microcode version

    :param struct adapter \*adapter:
        the adapter

    :param u32 \*vers:
        where to place the version

.. _`t4_get_tp_version.description`:

Description
-----------

Reads the TP microcode version from flash.

.. _`t4_get_exprom_version`:

t4_get_exprom_version
=====================

.. c:function:: int t4_get_exprom_version(struct adapter *adap, u32 *vers)

    return the Expansion ROM version (if any)

    :param struct adapter \*adap:
        *undescribed*

    :param u32 \*vers:
        where to place the version

.. _`t4_get_exprom_version.description`:

Description
-----------

Reads the Expansion ROM header from FLASH and returns the version
number (if present) through the \ ``vers``\  return value pointer.  We return
this in the Firmware Version Format since it's convenient.  Return
0 on success, -ENOENT if no Expansion ROM is present.

.. _`t4_check_fw_version`:

t4_check_fw_version
===================

.. c:function:: int t4_check_fw_version(struct adapter *adap)

    check if the FW is supported with this driver

    :param struct adapter \*adap:
        the adapter

.. _`t4_check_fw_version.description`:

Description
-----------

Checks if an adapter's FW is compatible with the driver.  Returns 0
if there's exact match, a negative error if the version could not be
read or there's a major version mismatch

.. _`t4_flash_erase_sectors`:

t4_flash_erase_sectors
======================

.. c:function:: int t4_flash_erase_sectors(struct adapter *adapter, int start, int end)

    erase a range of flash sectors

    :param struct adapter \*adapter:
        the adapter

    :param int start:
        the first sector to erase

    :param int end:
        the last sector to erase

.. _`t4_flash_erase_sectors.description`:

Description
-----------

Erases the sectors in the given inclusive range.

.. _`t4_flash_cfg_addr`:

t4_flash_cfg_addr
=================

.. c:function:: unsigned int t4_flash_cfg_addr(struct adapter *adapter)

    return the address of the flash configuration file

    :param struct adapter \*adapter:
        the adapter

.. _`t4_flash_cfg_addr.description`:

Description
-----------

Return the address within the flash where the Firmware Configuration
File is stored.

.. _`t4_load_fw`:

t4_load_fw
==========

.. c:function:: int t4_load_fw(struct adapter *adap, const u8 *fw_data, unsigned int size)

    download firmware

    :param struct adapter \*adap:
        the adapter

    :param const u8 \*fw_data:
        the firmware image to write

    :param unsigned int size:
        image size

.. _`t4_load_fw.description`:

Description
-----------

Write the supplied firmware image to the card's serial flash.

.. _`t4_phy_fw_ver`:

t4_phy_fw_ver
=============

.. c:function:: int t4_phy_fw_ver(struct adapter *adap, int *phy_fw_ver)

    return current PHY firmware version

    :param struct adapter \*adap:
        the adapter

    :param int \*phy_fw_ver:
        return value buffer for PHY firmware version

.. _`t4_phy_fw_ver.description`:

Description
-----------

Returns the current version of external PHY firmware on the
adapter.

.. _`t4_load_phy_fw`:

t4_load_phy_fw
==============

.. c:function:: int t4_load_phy_fw(struct adapter *adap, int win, spinlock_t *win_lock, int (*phy_fw_version)(const u8 *, size_t), const u8 *phy_fw_data, size_t phy_fw_size)

    download port PHY firmware

    :param struct adapter \*adap:
        the adapter

    :param int win:
        the PCI-E Memory Window index to use for \ :c:func:`t4_memory_rw`\ 

    :param spinlock_t \*win_lock:
        the lock to use to guard the memory copy

    :param int (\*phy_fw_version)(const u8 \*, size_t):
        function to check PHY firmware versions

    :param const u8 \*phy_fw_data:
        the PHY firmware image to write

    :param size_t phy_fw_size:
        image size

.. _`t4_load_phy_fw.description`:

Description
-----------

Transfer the specified PHY firmware to the adapter.  If a non-NULL
\ ``phy_fw_version``\  is supplied, then it will be used to determine if
it's necessary to perform the transfer by comparing the version
of any existing adapter PHY firmware with that of the passed in
PHY firmware image.  If \ ``win_lock``\  is non-NULL then it will be used
around the call to \ :c:func:`t4_memory_rw`\  which transfers the PHY firmware
to the adapter.

A negative error number will be returned if an error occurs.  If
version number support is available and there's no need to upgrade
the firmware, 0 will be returned.  If firmware is successfully
transferred to the adapter, 1 will be retured.

.. _`t4_load_phy_fw.note`:

NOTE
----

some adapters only have local RAM to store the PHY firmware.  As
a result, a RESET of the adapter would cause that RAM to lose its
contents.  Thus, loading PHY firmware on such adapters must happen
after any FW_RESET_CMDs ...

.. _`t4_fwcache`:

t4_fwcache
==========

.. c:function:: int t4_fwcache(struct adapter *adap, enum fw_params_param_dev_fwcache op)

    firmware cache operation

    :param struct adapter \*adap:
        the adapter

    :param enum fw_params_param_dev_fwcache op:
        the operation (flush or flush and invalidate)

.. _`t4_link_l1cfg`:

t4_link_l1cfg
=============

.. c:function:: int t4_link_l1cfg(struct adapter *adap, unsigned int mbox, unsigned int port, struct link_config *lc)

    apply link configuration to MAC/PHY

    :param struct adapter \*adap:
        *undescribed*

    :param unsigned int mbox:
        *undescribed*

    :param unsigned int port:
        *undescribed*

    :param struct link_config \*lc:
        the requested link configuration

.. _`t4_link_l1cfg.description`:

Description
-----------

Set up a port's MAC and PHY according to a desired link configuration.
- If the PHY can auto-negotiate first decide what to advertise, then
enable/disable auto-negotiation as desired, and reset.
- If the PHY does not auto-negotiate just reset it.
- If auto-negotiation is off set the MAC to the proper speed/duplex/FC,
otherwise do it later based on the outcome of auto-negotiation.

.. _`t4_restart_aneg`:

t4_restart_aneg
===============

.. c:function:: int t4_restart_aneg(struct adapter *adap, unsigned int mbox, unsigned int port)

    restart autonegotiation

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mbox to use for the FW command

    :param unsigned int port:
        the port id

.. _`t4_restart_aneg.description`:

Description
-----------

Restarts autonegotiation for the selected port.

.. _`t4_handle_intr_status`:

t4_handle_intr_status
=====================

.. c:function:: int t4_handle_intr_status(struct adapter *adapter, unsigned int reg, const struct intr_info *acts)

    table driven interrupt handler

    :param struct adapter \*adapter:
        the adapter that generated the interrupt

    :param unsigned int reg:
        the interrupt status register to process

    :param const struct intr_info \*acts:
        table of interrupt actions

.. _`t4_handle_intr_status.description`:

Description
-----------

A table driven interrupt handler that applies a set of masks to an
interrupt status word and performs the corresponding actions if the
interrupts described by the mask have occurred.  The actions include
optionally emitting a warning or alert message.  The table is terminated
by an entry specifying mask 0.  Returns the number of fatal interrupt
conditions.

.. _`t4_slow_intr_handler`:

t4_slow_intr_handler
====================

.. c:function:: int t4_slow_intr_handler(struct adapter *adapter)

    control path interrupt handler

    :param struct adapter \*adapter:
        the adapter

.. _`t4_slow_intr_handler.description`:

Description
-----------

T4 interrupt handler for non-data global interrupt events, e.g., errors.
The designation 'slow' is because it involves register reads, while
data interrupts typically don't involve any MMIOs.

.. _`t4_intr_enable`:

t4_intr_enable
==============

.. c:function:: void t4_intr_enable(struct adapter *adapter)

    enable interrupts

    :param struct adapter \*adapter:
        the adapter whose interrupts should be enabled

.. _`t4_intr_enable.description`:

Description
-----------

Enable PF-specific interrupts for the calling function and the top-level
interrupt concentrator for global interrupts.  Interrupts are already
enabled at each module, here we just enable the roots of the interrupt
hierarchies.

.. _`t4_intr_enable.note`:

Note
----

this function should be called only when the driver manages
non PF-specific interrupts from the various HW modules.  Only one PCI
function at a time should be doing this.

.. _`t4_intr_disable`:

t4_intr_disable
===============

.. c:function:: void t4_intr_disable(struct adapter *adapter)

    disable interrupts

    :param struct adapter \*adapter:
        the adapter whose interrupts should be disabled

.. _`t4_intr_disable.description`:

Description
-----------

Disable interrupts.  We only disable the top-level interrupt
concentrators.  The caller must be a PCI function managing global
interrupts.

.. _`t4_config_rss_range`:

t4_config_rss_range
===================

.. c:function:: int t4_config_rss_range(struct adapter *adapter, int mbox, unsigned int viid, int start, int n, const u16 *rspq, unsigned int nrspq)

    configure a portion of the RSS mapping table

    :param struct adapter \*adapter:
        the adapter

    :param int mbox:
        mbox to use for the FW command

    :param unsigned int viid:
        virtual interface whose RSS subtable is to be written

    :param int start:
        start entry in the table to write

    :param int n:
        how many table entries to write

    :param const u16 \*rspq:
        values for the response queue lookup table

    :param unsigned int nrspq:
        number of values in \ ``rspq``\ 

.. _`t4_config_rss_range.description`:

Description
-----------

Programs the selected part of the VI's RSS mapping table with the
provided values.  If \ ``nrspq``\  < \ ``n``\  the supplied values are used repeatedly
until the full table range is populated.

The caller must ensure the values in \ ``rspq``\  are in the range allowed for
\ ``viid``\ .

.. _`t4_config_glbl_rss`:

t4_config_glbl_rss
==================

.. c:function:: int t4_config_glbl_rss(struct adapter *adapter, int mbox, unsigned int mode, unsigned int flags)

    configure the global RSS mode

    :param struct adapter \*adapter:
        the adapter

    :param int mbox:
        mbox to use for the FW command

    :param unsigned int mode:
        global RSS mode

    :param unsigned int flags:
        mode-specific flags

.. _`t4_config_glbl_rss.description`:

Description
-----------

Sets the global RSS mode.

.. _`t4_config_vi_rss`:

t4_config_vi_rss
================

.. c:function:: int t4_config_vi_rss(struct adapter *adapter, int mbox, unsigned int viid, unsigned int flags, unsigned int defq)

    configure per VI RSS settings

    :param struct adapter \*adapter:
        the adapter

    :param int mbox:
        mbox to use for the FW command

    :param unsigned int viid:
        the VI id

    :param unsigned int flags:
        RSS flags

    :param unsigned int defq:
        id of the default RSS queue for the VI.

.. _`t4_config_vi_rss.description`:

Description
-----------

Configures VI-specific RSS properties.

.. _`t4_read_rss`:

t4_read_rss
===========

.. c:function:: int t4_read_rss(struct adapter *adapter, u16 *map)

    read the contents of the RSS mapping table

    :param struct adapter \*adapter:
        the adapter

    :param u16 \*map:
        holds the contents of the RSS mapping table

.. _`t4_read_rss.description`:

Description
-----------

Reads the contents of the RSS hash->queue mapping table.

.. _`t4_fw_tp_pio_rw`:

t4_fw_tp_pio_rw
===============

.. c:function:: void t4_fw_tp_pio_rw(struct adapter *adap, u32 *vals, unsigned int nregs, unsigned int start_index, unsigned int rw)

    Access TP PIO through LDST

    :param struct adapter \*adap:
        the adapter

    :param u32 \*vals:
        where the indirect register values are stored/written

    :param unsigned int nregs:
        how many indirect registers to read/write

    :param unsigned int start_index:
        *undescribed*

    :param unsigned int rw:
        Read (1) or Write (0)

.. _`t4_fw_tp_pio_rw.description`:

Description
-----------

Access TP PIO registers through LDST

.. _`t4_read_rss_key`:

t4_read_rss_key
===============

.. c:function:: void t4_read_rss_key(struct adapter *adap, u32 *key)

    read the global RSS key

    :param struct adapter \*adap:
        the adapter

    :param u32 \*key:
        10-entry array holding the 320-bit RSS key

.. _`t4_read_rss_key.description`:

Description
-----------

Reads the global 320-bit RSS key.

.. _`t4_write_rss_key`:

t4_write_rss_key
================

.. c:function:: void t4_write_rss_key(struct adapter *adap, const u32 *key, int idx)

    program one of the RSS keys

    :param struct adapter \*adap:
        the adapter

    :param const u32 \*key:
        10-entry array holding the 320-bit RSS key

    :param int idx:
        which RSS key to write

.. _`t4_write_rss_key.description`:

Description
-----------

Writes one of the RSS keys with the given 320-bit value.  If \ ``idx``\  is
0..15 the corresponding entry in the RSS key table is written,
otherwise the global RSS key is written.

.. _`t4_read_rss_pf_config`:

t4_read_rss_pf_config
=====================

.. c:function:: void t4_read_rss_pf_config(struct adapter *adapter, unsigned int index, u32 *valp)

    read PF RSS Configuration Table

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int index:
        the entry in the PF RSS table to read

    :param u32 \*valp:
        where to store the returned value

.. _`t4_read_rss_pf_config.description`:

Description
-----------

Reads the PF RSS Configuration Table at the specified index and returns
the value found there.

.. _`t4_read_rss_vf_config`:

t4_read_rss_vf_config
=====================

.. c:function:: void t4_read_rss_vf_config(struct adapter *adapter, unsigned int index, u32 *vfl, u32 *vfh)

    read VF RSS Configuration Table

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int index:
        the entry in the VF RSS table to read

    :param u32 \*vfl:
        where to store the returned VFL

    :param u32 \*vfh:
        where to store the returned VFH

.. _`t4_read_rss_vf_config.description`:

Description
-----------

Reads the VF RSS Configuration Table at the specified index and returns
the (VFL, VFH) values found there.

.. _`t4_read_rss_pf_map`:

t4_read_rss_pf_map
==================

.. c:function:: u32 t4_read_rss_pf_map(struct adapter *adapter)

    read PF RSS Map

    :param struct adapter \*adapter:
        the adapter

.. _`t4_read_rss_pf_map.description`:

Description
-----------

Reads the PF RSS Map register and returns its value.

.. _`t4_read_rss_pf_mask`:

t4_read_rss_pf_mask
===================

.. c:function:: u32 t4_read_rss_pf_mask(struct adapter *adapter)

    read PF RSS Mask

    :param struct adapter \*adapter:
        the adapter

.. _`t4_read_rss_pf_mask.description`:

Description
-----------

Reads the PF RSS Mask register and returns its value.

.. _`t4_tp_get_tcp_stats`:

t4_tp_get_tcp_stats
===================

.. c:function:: void t4_tp_get_tcp_stats(struct adapter *adap, struct tp_tcp_stats *v4, struct tp_tcp_stats *v6)

    read TP's TCP MIB counters

    :param struct adapter \*adap:
        the adapter

    :param struct tp_tcp_stats \*v4:
        holds the TCP/IP counter values

    :param struct tp_tcp_stats \*v6:
        holds the TCP/IPv6 counter values

.. _`t4_tp_get_tcp_stats.description`:

Description
-----------

Returns the values of TP's TCP/IP and TCP/IPv6 MIB counters.
Either \ ``v4``\  or \ ``v6``\  may be \ ``NULL``\  to skip the corresponding stats.

.. _`t4_tp_get_err_stats`:

t4_tp_get_err_stats
===================

.. c:function:: void t4_tp_get_err_stats(struct adapter *adap, struct tp_err_stats *st)

    read TP's error MIB counters

    :param struct adapter \*adap:
        the adapter

    :param struct tp_err_stats \*st:
        holds the counter values

.. _`t4_tp_get_err_stats.description`:

Description
-----------

Returns the values of TP's error counters.

.. _`t4_tp_get_cpl_stats`:

t4_tp_get_cpl_stats
===================

.. c:function:: void t4_tp_get_cpl_stats(struct adapter *adap, struct tp_cpl_stats *st)

    read TP's CPL MIB counters

    :param struct adapter \*adap:
        the adapter

    :param struct tp_cpl_stats \*st:
        holds the counter values

.. _`t4_tp_get_cpl_stats.description`:

Description
-----------

Returns the values of TP's CPL counters.

.. _`t4_tp_get_rdma_stats`:

t4_tp_get_rdma_stats
====================

.. c:function:: void t4_tp_get_rdma_stats(struct adapter *adap, struct tp_rdma_stats *st)

    read TP's RDMA MIB counters

    :param struct adapter \*adap:
        the adapter

    :param struct tp_rdma_stats \*st:
        holds the counter values

.. _`t4_tp_get_rdma_stats.description`:

Description
-----------

Returns the values of TP's RDMA counters.

.. _`t4_get_fcoe_stats`:

t4_get_fcoe_stats
=================

.. c:function:: void t4_get_fcoe_stats(struct adapter *adap, unsigned int idx, struct tp_fcoe_stats *st)

    read TP's FCoE MIB counters for a port

    :param struct adapter \*adap:
        the adapter

    :param unsigned int idx:
        the port index

    :param struct tp_fcoe_stats \*st:
        holds the counter values

.. _`t4_get_fcoe_stats.description`:

Description
-----------

Returns the values of TP's FCoE counters for the selected port.

.. _`t4_get_usm_stats`:

t4_get_usm_stats
================

.. c:function:: void t4_get_usm_stats(struct adapter *adap, struct tp_usm_stats *st)

    read TP's non-TCP DDP MIB counters

    :param struct adapter \*adap:
        the adapter

    :param struct tp_usm_stats \*st:
        holds the counter values

.. _`t4_get_usm_stats.description`:

Description
-----------

Returns the values of TP's counters for non-TCP directly-placed packets.

.. _`t4_read_mtu_tbl`:

t4_read_mtu_tbl
===============

.. c:function:: void t4_read_mtu_tbl(struct adapter *adap, u16 *mtus, u8 *mtu_log)

    returns the values in the HW path MTU table

    :param struct adapter \*adap:
        the adapter

    :param u16 \*mtus:
        where to store the MTU values

    :param u8 \*mtu_log:
        where to store the MTU base-2 log (may be \ ``NULL``\ )

.. _`t4_read_mtu_tbl.description`:

Description
-----------

Reads the HW path MTU table.

.. _`t4_read_cong_tbl`:

t4_read_cong_tbl
================

.. c:function:: void t4_read_cong_tbl(struct adapter *adap, u16 incr[NMTUS][NCCTRL_WIN])

    reads the congestion control table

    :param struct adapter \*adap:
        the adapter

    :param u16 incr:
        where to store the alpha values

.. _`t4_read_cong_tbl.description`:

Description
-----------

Reads the additive increments programmed into the HW congestion
control table.

.. _`t4_tp_wr_bits_indirect`:

t4_tp_wr_bits_indirect
======================

.. c:function:: void t4_tp_wr_bits_indirect(struct adapter *adap, unsigned int addr, unsigned int mask, unsigned int val)

    set/clear bits in an indirect TP register

    :param struct adapter \*adap:
        the adapter

    :param unsigned int addr:
        the indirect TP register address

    :param unsigned int mask:
        specifies the field within the register to modify

    :param unsigned int val:
        new value for the field

.. _`t4_tp_wr_bits_indirect.description`:

Description
-----------

Sets a field of an indirect TP register to the given value.

.. _`init_cong_ctrl`:

init_cong_ctrl
==============

.. c:function:: void init_cong_ctrl(unsigned short *a, unsigned short *b)

    initialize congestion control parameters

    :param unsigned short \*a:
        the alpha values for congestion control

    :param unsigned short \*b:
        the beta values for congestion control

.. _`init_cong_ctrl.description`:

Description
-----------

Initialize the congestion control parameters.

.. _`t4_load_mtus`:

t4_load_mtus
============

.. c:function:: void t4_load_mtus(struct adapter *adap, const unsigned short *mtus, const unsigned short *alpha, const unsigned short *beta)

    write the MTU and congestion control HW tables

    :param struct adapter \*adap:
        the adapter

    :param const unsigned short \*mtus:
        the values for the MTU table

    :param const unsigned short \*alpha:
        the values for the congestion control alpha parameter

    :param const unsigned short \*beta:
        the values for the congestion control beta parameter

.. _`t4_load_mtus.description`:

Description
-----------

Write the HW MTU table with the supplied MTUs and the high-speed
congestion control table with the supplied alpha, beta, and MTUs.
We write the two tables together because the additive increments
depend on the MTUs.

.. _`t4_get_chan_txrate`:

t4_get_chan_txrate
==================

.. c:function:: void t4_get_chan_txrate(struct adapter *adap, u64 *nic_rate, u64 *ofld_rate)

    get the current per channel Tx rates

    :param struct adapter \*adap:
        the adapter

    :param u64 \*nic_rate:
        rates for NIC traffic

    :param u64 \*ofld_rate:
        rates for offloaded traffic

.. _`t4_get_chan_txrate.description`:

Description
-----------

Return the current Tx rates in bytes/s for NIC and offloaded traffic
for each channel.

.. _`t4_set_trace_filter`:

t4_set_trace_filter
===================

.. c:function:: int t4_set_trace_filter(struct adapter *adap, const struct trace_params *tp, int idx, int enable)

    configure one of the tracing filters

    :param struct adapter \*adap:
        the adapter

    :param const struct trace_params \*tp:
        the desired trace filter parameters

    :param int idx:
        which filter to configure

    :param int enable:
        whether to enable or disable the filter

.. _`t4_set_trace_filter.description`:

Description
-----------

Configures one of the tracing filters available in HW.  If \ ``enable``\  is
\ ``0``\  \ ``tp``\  is not examined and may be \ ``NULL``\ . The user is responsible to
set the single/multiple trace mode by writing to MPS_TRC_CFG_A register

.. _`t4_get_trace_filter`:

t4_get_trace_filter
===================

.. c:function:: void t4_get_trace_filter(struct adapter *adap, struct trace_params *tp, int idx, int *enabled)

    query one of the tracing filters

    :param struct adapter \*adap:
        the adapter

    :param struct trace_params \*tp:
        the current trace filter parameters

    :param int idx:
        which trace filter to query

    :param int \*enabled:
        non-zero if the filter is enabled

.. _`t4_get_trace_filter.description`:

Description
-----------

Returns the current settings of one of the HW tracing filters.

.. _`t4_pmtx_get_stats`:

t4_pmtx_get_stats
=================

.. c:function:: void t4_pmtx_get_stats(struct adapter *adap, u32 cnt[], u64 cycles[])

    returns the HW stats from PMTX

    :param struct adapter \*adap:
        the adapter

    :param u32 cnt:
        where to store the count statistics

    :param u64 cycles:
        where to store the cycle statistics

.. _`t4_pmtx_get_stats.description`:

Description
-----------

Returns performance statistics from PMTX.

.. _`t4_pmrx_get_stats`:

t4_pmrx_get_stats
=================

.. c:function:: void t4_pmrx_get_stats(struct adapter *adap, u32 cnt[], u64 cycles[])

    returns the HW stats from PMRX

    :param struct adapter \*adap:
        the adapter

    :param u32 cnt:
        where to store the count statistics

    :param u64 cycles:
        where to store the cycle statistics

.. _`t4_pmrx_get_stats.description`:

Description
-----------

Returns performance statistics from PMRX.

.. _`t4_get_mps_bg_map`:

t4_get_mps_bg_map
=================

.. c:function:: unsigned int t4_get_mps_bg_map(struct adapter *adap, int idx)

    return the buffer groups associated with a port

    :param struct adapter \*adap:
        the adapter

    :param int idx:
        the port index

.. _`t4_get_mps_bg_map.description`:

Description
-----------

Returns a bitmap indicating which MPS buffer groups are associated
with the given port.  Bit i is set if buffer group i is used by the
port.

.. _`t4_get_port_type_description`:

t4_get_port_type_description
============================

.. c:function:: const char *t4_get_port_type_description(enum fw_port_type port_type)

    return Port Type string description

    :param enum fw_port_type port_type:
        firmware Port Type enumeration

.. _`t4_get_port_stats_offset`:

t4_get_port_stats_offset
========================

.. c:function:: void t4_get_port_stats_offset(struct adapter *adap, int idx, struct port_stats *stats, struct port_stats *offset)

    collect port stats relative to a previous snapshot

    :param struct adapter \*adap:
        The adapter

    :param int idx:
        The port

    :param struct port_stats \*stats:
        Current stats to fill

    :param struct port_stats \*offset:
        Previous stats snapshot

.. _`t4_get_port_stats`:

t4_get_port_stats
=================

.. c:function:: void t4_get_port_stats(struct adapter *adap, int idx, struct port_stats *p)

    collect port statistics

    :param struct adapter \*adap:
        the adapter

    :param int idx:
        the port index

    :param struct port_stats \*p:
        the stats structure to fill

.. _`t4_get_port_stats.description`:

Description
-----------

Collect statistics related to the given port from HW.

.. _`t4_get_lb_stats`:

t4_get_lb_stats
===============

.. c:function:: void t4_get_lb_stats(struct adapter *adap, int idx, struct lb_port_stats *p)

    collect loopback port statistics

    :param struct adapter \*adap:
        the adapter

    :param int idx:
        the loopback port index

    :param struct lb_port_stats \*p:
        the stats structure to fill

.. _`t4_get_lb_stats.description`:

Description
-----------

Return HW statistics for the given loopback port.

.. _`t4_mdio_rd`:

t4_mdio_rd
==========

.. c:function:: int t4_mdio_rd(struct adapter *adap, unsigned int mbox, unsigned int phy_addr, unsigned int mmd, unsigned int reg, u16 *valp)

    read a PHY register through MDIO

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int phy_addr:
        the PHY address

    :param unsigned int mmd:
        the PHY MMD to access (0 for clause 22 PHYs)

    :param unsigned int reg:
        the register to read

    :param u16 \*valp:
        where to store the value

.. _`t4_mdio_rd.description`:

Description
-----------

Issues a FW command through the given mailbox to read a PHY register.

.. _`t4_mdio_wr`:

t4_mdio_wr
==========

.. c:function:: int t4_mdio_wr(struct adapter *adap, unsigned int mbox, unsigned int phy_addr, unsigned int mmd, unsigned int reg, u16 val)

    write a PHY register through MDIO

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int phy_addr:
        the PHY address

    :param unsigned int mmd:
        the PHY MMD to access (0 for clause 22 PHYs)

    :param unsigned int reg:
        the register to write

    :param u16 val:
        *undescribed*

.. _`t4_mdio_wr.description`:

Description
-----------

Issues a FW command through the given mailbox to write a PHY register.

.. _`t4_sge_decode_idma_state`:

t4_sge_decode_idma_state
========================

.. c:function:: void t4_sge_decode_idma_state(struct adapter *adapter, int state)

    decode the idma state

    :param struct adapter \*adapter:
        *undescribed*

    :param int state:
        the state idma is stuck in

.. _`t4_sge_ctxt_flush`:

t4_sge_ctxt_flush
=================

.. c:function:: int t4_sge_ctxt_flush(struct adapter *adap, unsigned int mbox)

    flush the SGE context cache

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

.. _`t4_sge_ctxt_flush.description`:

Description
-----------

Issues a FW command through the given mailbox to flush the
SGE context cache.

.. _`t4_fw_hello`:

t4_fw_hello
===========

.. c:function:: int t4_fw_hello(struct adapter *adap, unsigned int mbox, unsigned int evt_mbox, enum dev_master master, enum dev_state *state)

    establish communication with FW

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int evt_mbox:
        mailbox to receive async FW events

    :param enum dev_master master:
        specifies the caller's willingness to be the device master

    :param enum dev_state \*state:
        returns the current device state (if non-NULL)

.. _`t4_fw_hello.description`:

Description
-----------

Issues a command to establish communication with FW.  Returns either
an error (negative integer) or the mailbox of the Master PF.

.. _`t4_fw_bye`:

t4_fw_bye
=========

.. c:function:: int t4_fw_bye(struct adapter *adap, unsigned int mbox)

    end communication with FW

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

.. _`t4_fw_bye.description`:

Description
-----------

Issues a command to terminate communication with FW.

.. _`t4_early_init`:

t4_early_init
=============

.. c:function:: int t4_early_init(struct adapter *adap, unsigned int mbox)

    ask FW to initialize the device

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

.. _`t4_early_init.description`:

Description
-----------

Issues a command to FW to partially initialize the device.  This
performs initialization that generally doesn't depend on user input.

.. _`t4_fw_reset`:

t4_fw_reset
===========

.. c:function:: int t4_fw_reset(struct adapter *adap, unsigned int mbox, int reset)

    issue a reset to FW

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param int reset:
        specifies the type of reset to perform

.. _`t4_fw_reset.description`:

Description
-----------

Issues a reset command of the specified type to FW.

.. _`t4_fw_halt`:

t4_fw_halt
==========

.. c:function:: int t4_fw_halt(struct adapter *adap, unsigned int mbox, int force)

    issue a reset/halt to FW and put uP into RESET

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW RESET command (if desired)

    :param int force:
        force uP into RESET even if FW RESET command fails

.. _`t4_fw_halt.description`:

Description
-----------

Issues a RESET command to firmware (if desired) with a HALT indication
and then puts the microprocessor into RESET state.  The RESET command
will only be issued if a legitimate mailbox is provided (mbox <=
PCIE_FW_MASTER_M).

This is generally used in order for the host to safely manipulate the
adapter without fear of conflicting with whatever the firmware might
be doing.  The only way out of this state is to RESTART the firmware
...

.. _`t4_fw_restart`:

t4_fw_restart
=============

.. c:function:: int t4_fw_restart(struct adapter *adap, unsigned int mbox, int reset)

    restart the firmware by taking the uP out of RESET

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        *undescribed*

    :param int reset:
        if we want to do a RESET to restart things

.. _`t4_fw_restart.description`:

Description
-----------

Restart firmware previously halted by \ :c:func:`t4_fw_halt`\ .  On successful
return the previous PF Master remains as the new PF Master and there
is no need to issue a new HELLO command, etc.

.. _`t4_fw_restart.we-do-this-in-two-ways`:

We do this in two ways
----------------------


1. If we're dealing with newer firmware we'll simply want to take
the chip's microprocessor out of RESET.  This will cause the
firmware to start up from its start vector.  And then we'll loop
until the firmware indicates it's started again (PCIE_FW.HALT
reset to 0) or we timeout.

2. If we're dealing with older firmware then we'll need to RESET
the chip since older firmware won't recognize the PCIE_FW.HALT
flag and automatically RESET itself on startup.

.. _`t4_fw_upgrade`:

t4_fw_upgrade
=============

.. c:function:: int t4_fw_upgrade(struct adapter *adap, unsigned int mbox, const u8 *fw_data, unsigned int size, int force)

    perform all of the steps necessary to upgrade FW

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW RESET command (if desired)

    :param const u8 \*fw_data:
        the firmware image to write

    :param unsigned int size:
        image size

    :param int force:
        force upgrade even if firmware doesn't cooperate

.. _`t4_fw_upgrade.description`:

Description
-----------

Perform all of the steps necessary for upgrading an adapter's
firmware image.  Normally this requires the cooperation of the
existing firmware in order to halt all existing activities
but if an invalid mailbox token is passed in we skip that step
(though we'll still put the adapter microprocessor into RESET in
that case).

On successful return the new firmware will have been loaded and
the adapter will have been fully RESET losing all previous setup
state.  On unsuccessful return the adapter may be completely hosed ...
positive errno indicates that the adapter is ~probably~ intact, a
negative errno indicates that things are looking bad ...

.. _`t4_fl_pkt_align`:

t4_fl_pkt_align
===============

.. c:function:: int t4_fl_pkt_align(struct adapter *adap)

    return the fl packet alignment

    :param struct adapter \*adap:
        the adapter

.. _`t4_fl_pkt_align.description`:

Description
-----------

T4 has a single field to specify the packing and padding boundary.
T5 onwards has separate fields for this and hence the alignment for
next packet offset is maximum of these two.

.. _`t4_fixup_host_params`:

t4_fixup_host_params
====================

.. c:function:: int t4_fixup_host_params(struct adapter *adap, unsigned int page_size, unsigned int cache_line_size)

    fix up host-dependent parameters

    :param struct adapter \*adap:
        the adapter

    :param unsigned int page_size:
        the host's Base Page Size

    :param unsigned int cache_line_size:
        the host's Cache Line Size

.. _`t4_fixup_host_params.description`:

Description
-----------

Various registers in T4 contain values which are dependent on the
host's Base Page and Cache Line Sizes.  This function will fix all of
those registers with the appropriate values as passed in ...

.. _`t4_fw_initialize`:

t4_fw_initialize
================

.. c:function:: int t4_fw_initialize(struct adapter *adap, unsigned int mbox)

    ask FW to initialize the device

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

.. _`t4_fw_initialize.description`:

Description
-----------

Issues a command to FW to partially initialize the device.  This
performs initialization that generally doesn't depend on user input.

.. _`t4_query_params_rw`:

t4_query_params_rw
==================

.. c:function:: int t4_query_params_rw(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int nparams, const u32 *params, u32 *val, int rw)

    query FW or device parameters

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF

    :param unsigned int vf:
        the VF

    :param unsigned int nparams:
        the number of parameters

    :param const u32 \*params:
        the parameter names

    :param u32 \*val:
        the parameter values

    :param int rw:
        Write and read flag

.. _`t4_query_params_rw.description`:

Description
-----------

Reads the value of FW or device parameters.  Up to 7 parameters can be
queried at once.

.. _`t4_set_params_timeout`:

t4_set_params_timeout
=====================

.. c:function:: int t4_set_params_timeout(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int nparams, const u32 *params, const u32 *val, int timeout)

    sets FW or device parameters

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF

    :param unsigned int vf:
        the VF

    :param unsigned int nparams:
        the number of parameters

    :param const u32 \*params:
        the parameter names

    :param const u32 \*val:
        the parameter values

    :param int timeout:
        the timeout time

.. _`t4_set_params_timeout.description`:

Description
-----------

Sets the value of FW or device parameters.  Up to 7 parameters can be
specified at once.

.. _`t4_set_params`:

t4_set_params
=============

.. c:function:: int t4_set_params(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int nparams, const u32 *params, const u32 *val)

    sets FW or device parameters

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF

    :param unsigned int vf:
        the VF

    :param unsigned int nparams:
        the number of parameters

    :param const u32 \*params:
        the parameter names

    :param const u32 \*val:
        the parameter values

.. _`t4_set_params.description`:

Description
-----------

Sets the value of FW or device parameters.  Up to 7 parameters can be
specified at once.

.. _`t4_cfg_pfvf`:

t4_cfg_pfvf
===========

.. c:function:: int t4_cfg_pfvf(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int txq, unsigned int txq_eth_ctrl, unsigned int rxqi, unsigned int rxq, unsigned int tc, unsigned int vi, unsigned int cmask, unsigned int pmask, unsigned int nexact, unsigned int rcaps, unsigned int wxcaps)

    configure PF/VF resource limits

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF being configured

    :param unsigned int vf:
        the VF being configured

    :param unsigned int txq:
        the max number of egress queues

    :param unsigned int txq_eth_ctrl:
        the max number of egress Ethernet or control queues

    :param unsigned int rxqi:
        the max number of interrupt-capable ingress queues

    :param unsigned int rxq:
        the max number of interruptless ingress queues

    :param unsigned int tc:
        the PCI traffic class

    :param unsigned int vi:
        the max number of virtual interfaces

    :param unsigned int cmask:
        the channel access rights mask for the PF/VF

    :param unsigned int pmask:
        the port access rights mask for the PF/VF

    :param unsigned int nexact:
        the maximum number of exact MPS filters

    :param unsigned int rcaps:
        read capabilities

    :param unsigned int wxcaps:
        write/execute capabilities

.. _`t4_cfg_pfvf.description`:

Description
-----------

Configures resource limits and capabilities for a physical or virtual
function.

.. _`t4_alloc_vi`:

t4_alloc_vi
===========

.. c:function:: int t4_alloc_vi(struct adapter *adap, unsigned int mbox, unsigned int port, unsigned int pf, unsigned int vf, unsigned int nmac, u8 *mac, unsigned int *rss_size)

    allocate a virtual interface

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int port:
        physical port associated with the VI

    :param unsigned int pf:
        the PF owning the VI

    :param unsigned int vf:
        the VF owning the VI

    :param unsigned int nmac:
        number of MAC addresses needed (1 to 5)

    :param u8 \*mac:
        the MAC addresses of the VI

    :param unsigned int \*rss_size:
        size of RSS table slice associated with this VI

.. _`t4_alloc_vi.description`:

Description
-----------

Allocates a virtual interface for the given physical port.  If \ ``mac``\  is
not \ ``NULL``\  it contains the MAC addresses of the VI as assigned by FW.
\ ``mac``\  should be large enough to hold \ ``nmac``\  Ethernet addresses, they are
stored consecutively so the space needed is \ ``nmac``\  \* 6 bytes.
Returns a negative error number or the non-negative VI id.

.. _`t4_free_vi`:

t4_free_vi
==========

.. c:function:: int t4_free_vi(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int viid)

    free a virtual interface

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF owning the VI

    :param unsigned int vf:
        the VF owning the VI

    :param unsigned int viid:
        virtual interface identifiler

.. _`t4_free_vi.description`:

Description
-----------

Free a previously allocated virtual interface.

.. _`t4_set_rxmode`:

t4_set_rxmode
=============

.. c:function:: int t4_set_rxmode(struct adapter *adap, unsigned int mbox, unsigned int viid, int mtu, int promisc, int all_multi, int bcast, int vlanex, bool sleep_ok)

    set Rx properties of a virtual interface

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int viid:
        the VI id

    :param int mtu:
        the new MTU or -1

    :param int promisc:
        1 to enable promiscuous mode, 0 to disable it, -1 no change

    :param int all_multi:
        1 to enable all-multi mode, 0 to disable it, -1 no change

    :param int bcast:
        1 to enable broadcast Rx, 0 to disable it, -1 no change

    :param int vlanex:
        1 to enable HW VLAN extraction, 0 to disable it, -1 no change

    :param bool sleep_ok:
        if true we may sleep while awaiting command completion

.. _`t4_set_rxmode.description`:

Description
-----------

Sets Rx properties of a virtual interface.

.. _`t4_alloc_mac_filt`:

t4_alloc_mac_filt
=================

.. c:function:: int t4_alloc_mac_filt(struct adapter *adap, unsigned int mbox, unsigned int viid, bool free, unsigned int naddr, const u8 **addr, u16 *idx, u64 *hash, bool sleep_ok)

    allocates exact-match filters for MAC addresses

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int viid:
        the VI id

    :param bool free:
        if true any existing filters for this VI id are first removed

    :param unsigned int naddr:
        the number of MAC addresses to allocate filters for (up to 7)

    :param const u8 \*\*addr:
        the MAC address(es)

    :param u16 \*idx:
        where to store the index of each allocated filter

    :param u64 \*hash:
        pointer to hash address filter bitmap

    :param bool sleep_ok:
        call is allowed to sleep

.. _`t4_alloc_mac_filt.description`:

Description
-----------

Allocates an exact-match filter for each of the supplied addresses and
sets it to the corresponding address.  If \ ``idx``\  is not \ ``NULL``\  it should
have at least \ ``naddr``\  entries, each of which will be set to the index of
the filter allocated for the corresponding MAC address.  If a filter
could not be allocated for an address its index is set to 0xffff.
If \ ``hash``\  is not \ ``NULL``\  addresses that fail to allocate an exact filter
are hashed and update the hash filter bitmap pointed at by \ ``hash``\ .

Returns a negative error number or the number of filters allocated.

.. _`t4_free_mac_filt`:

t4_free_mac_filt
================

.. c:function:: int t4_free_mac_filt(struct adapter *adap, unsigned int mbox, unsigned int viid, unsigned int naddr, const u8 **addr, bool sleep_ok)

    frees exact-match filters of given MAC addresses

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int viid:
        the VI id

    :param unsigned int naddr:
        the number of MAC addresses to allocate filters for (up to 7)

    :param const u8 \*\*addr:
        the MAC address(es)

    :param bool sleep_ok:
        call is allowed to sleep

.. _`t4_free_mac_filt.description`:

Description
-----------

Frees the exact-match filter for each of the supplied addresses

Returns a negative error number or the number of filters freed.

.. _`t4_change_mac`:

t4_change_mac
=============

.. c:function:: int t4_change_mac(struct adapter *adap, unsigned int mbox, unsigned int viid, int idx, const u8 *addr, bool persist, bool add_smt)

    modifies the exact-match filter for a MAC address

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int viid:
        the VI id

    :param int idx:
        index of existing filter for old value of MAC address, or -1

    :param const u8 \*addr:
        the new MAC address value

    :param bool persist:
        whether a new MAC allocation should be persistent

    :param bool add_smt:
        if true also add the address to the HW SMT

.. _`t4_change_mac.description`:

Description
-----------

Modifies an exact-match filter and sets it to the new MAC address.
Note that in general it is not possible to modify the value of a given
filter so the generic way to modify an address filter is to free the one
being used by the old address value and allocate a new filter for the
new address value.  \ ``idx``\  can be -1 if the address is a new addition.

Returns a negative error number or the index of the filter with the new
MAC value.

.. _`t4_set_addr_hash`:

t4_set_addr_hash
================

.. c:function:: int t4_set_addr_hash(struct adapter *adap, unsigned int mbox, unsigned int viid, bool ucast, u64 vec, bool sleep_ok)

    program the MAC inexact-match hash filter

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int viid:
        the VI id

    :param bool ucast:
        whether the hash filter should also match unicast addresses

    :param u64 vec:
        the value to be written to the hash filter

    :param bool sleep_ok:
        call is allowed to sleep

.. _`t4_set_addr_hash.description`:

Description
-----------

Sets the 64-bit inexact-match hash filter for a virtual interface.

.. _`t4_enable_vi_params`:

t4_enable_vi_params
===================

.. c:function:: int t4_enable_vi_params(struct adapter *adap, unsigned int mbox, unsigned int viid, bool rx_en, bool tx_en, bool dcb_en)

    enable/disable a virtual interface

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int viid:
        the VI id

    :param bool rx_en:
        1=enable Rx, 0=disable Rx

    :param bool tx_en:
        1=enable Tx, 0=disable Tx

    :param bool dcb_en:
        1=enable delivery of Data Center Bridging messages.

.. _`t4_enable_vi_params.description`:

Description
-----------

Enables/disables a virtual interface.  Note that setting DCB Enable
only makes sense when enabling a Virtual Interface ...

.. _`t4_enable_vi`:

t4_enable_vi
============

.. c:function:: int t4_enable_vi(struct adapter *adap, unsigned int mbox, unsigned int viid, bool rx_en, bool tx_en)

    enable/disable a virtual interface

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int viid:
        the VI id

    :param bool rx_en:
        1=enable Rx, 0=disable Rx

    :param bool tx_en:
        1=enable Tx, 0=disable Tx

.. _`t4_enable_vi.description`:

Description
-----------

Enables/disables a virtual interface.

.. _`t4_identify_port`:

t4_identify_port
================

.. c:function:: int t4_identify_port(struct adapter *adap, unsigned int mbox, unsigned int viid, unsigned int nblinks)

    identify a VI's port by blinking its LED

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int viid:
        the VI id

    :param unsigned int nblinks:
        how many times to blink LED at 2.5 Hz

.. _`t4_identify_port.description`:

Description
-----------

Identifies a VI's port by blinking its LED.

.. _`t4_iq_stop`:

t4_iq_stop
==========

.. c:function:: int t4_iq_stop(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int iqtype, unsigned int iqid, unsigned int fl0id, unsigned int fl1id)

    stop an ingress queue and its FLs

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF owning the queues

    :param unsigned int vf:
        the VF owning the queues

    :param unsigned int iqtype:
        the ingress queue type (FW_IQ_TYPE_FL_INT_CAP, etc.)

    :param unsigned int iqid:
        ingress queue id

    :param unsigned int fl0id:
        FL0 queue id or 0xffff if no attached FL0

    :param unsigned int fl1id:
        FL1 queue id or 0xffff if no attached FL1

.. _`t4_iq_stop.description`:

Description
-----------

Stops an ingress queue and its associated FLs, if any.  This causes
any current or future data/messages destined for these queues to be
tossed.

.. _`t4_iq_free`:

t4_iq_free
==========

.. c:function:: int t4_iq_free(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int iqtype, unsigned int iqid, unsigned int fl0id, unsigned int fl1id)

    free an ingress queue and its FLs

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF owning the queues

    :param unsigned int vf:
        the VF owning the queues

    :param unsigned int iqtype:
        the ingress queue type

    :param unsigned int iqid:
        ingress queue id

    :param unsigned int fl0id:
        FL0 queue id or 0xffff if no attached FL0

    :param unsigned int fl1id:
        FL1 queue id or 0xffff if no attached FL1

.. _`t4_iq_free.description`:

Description
-----------

Frees an ingress queue and its associated FLs, if any.

.. _`t4_eth_eq_free`:

t4_eth_eq_free
==============

.. c:function:: int t4_eth_eq_free(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int eqid)

    free an Ethernet egress queue

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF owning the queue

    :param unsigned int vf:
        the VF owning the queue

    :param unsigned int eqid:
        egress queue id

.. _`t4_eth_eq_free.description`:

Description
-----------

Frees an Ethernet egress queue.

.. _`t4_ctrl_eq_free`:

t4_ctrl_eq_free
===============

.. c:function:: int t4_ctrl_eq_free(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int eqid)

    free a control egress queue

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF owning the queue

    :param unsigned int vf:
        the VF owning the queue

    :param unsigned int eqid:
        egress queue id

.. _`t4_ctrl_eq_free.description`:

Description
-----------

Frees a control egress queue.

.. _`t4_ofld_eq_free`:

t4_ofld_eq_free
===============

.. c:function:: int t4_ofld_eq_free(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int eqid)

    free an offload egress queue

    :param struct adapter \*adap:
        the adapter

    :param unsigned int mbox:
        mailbox to use for the FW command

    :param unsigned int pf:
        the PF owning the queue

    :param unsigned int vf:
        the VF owning the queue

    :param unsigned int eqid:
        egress queue id

.. _`t4_ofld_eq_free.description`:

Description
-----------

Frees a control egress queue.

.. _`t4_link_down_rc_str`:

t4_link_down_rc_str
===================

.. c:function:: const char *t4_link_down_rc_str(unsigned char link_down_rc)

    return a string for a Link Down Reason Code

    :param unsigned char link_down_rc:
        Link Down Reason Code

.. _`t4_link_down_rc_str.description`:

Description
-----------

Returns a string representation of the Link Down Reason Code.

.. _`t4_handle_get_port_info`:

t4_handle_get_port_info
=======================

.. c:function:: void t4_handle_get_port_info(struct port_info *pi, const __be64 *rpl)

    process a FW reply message

    :param struct port_info \*pi:
        the port info

    :param const __be64 \*rpl:
        start of the FW message

.. _`t4_handle_get_port_info.description`:

Description
-----------

Processes a GET_PORT_INFO FW reply message.

.. _`t4_handle_fw_rpl`:

t4_handle_fw_rpl
================

.. c:function:: int t4_handle_fw_rpl(struct adapter *adap, const __be64 *rpl)

    process a FW reply message

    :param struct adapter \*adap:
        the adapter

    :param const __be64 \*rpl:
        start of the FW message

.. _`t4_handle_fw_rpl.description`:

Description
-----------

Processes a FW message, such as link state change messages.

.. _`init_link_config`:

init_link_config
================

.. c:function:: void init_link_config(struct link_config *lc, unsigned int caps)

    initialize a link's SW state

    :param struct link_config \*lc:
        structure holding the link state

    :param unsigned int caps:
        link capabilities

.. _`init_link_config.description`:

Description
-----------

Initializes the SW state maintained for each link, including the link's
capabilities and default speed/flow-control/autonegotiation settings.

.. _`t4_prep_adapter`:

t4_prep_adapter
===============

.. c:function:: int t4_prep_adapter(struct adapter *adapter)

    prepare SW and HW for operation

    :param struct adapter \*adapter:
        the adapter

.. _`t4_prep_adapter.description`:

Description
-----------

Initialize adapter SW state for the various HW modules, set initial
values for some adapter tunables, take PHYs out of reset, and
initialize the MDIO interface.

.. _`t4_bar2_sge_qregs`:

t4_bar2_sge_qregs
=================

.. c:function:: int t4_bar2_sge_qregs(struct adapter *adapter, unsigned int qid, enum t4_bar2_qtype qtype, int user, u64 *pbar2_qoffset, unsigned int *pbar2_qid)

    return BAR2 SGE Queue register information

    :param struct adapter \*adapter:
        the adapter

    :param unsigned int qid:
        the Queue ID

    :param enum t4_bar2_qtype qtype:
        the Ingress or Egress type for \ ``qid``\ 

    :param int user:
        true if this request is for a user mode queue

    :param u64 \*pbar2_qoffset:
        BAR2 Queue Offset

    :param unsigned int \*pbar2_qid:
        BAR2 Queue ID or 0 for Queue ID inferred SGE Queues

.. _`t4_bar2_sge_qregs.description`:

Description
-----------

Returns the BAR2 SGE Queue Registers information associated with the
indicated Absolute Queue ID.  These are passed back in return value
pointers.  \ ``qtype``\  should be T4_BAR2_QTYPE_EGRESS for Egress Queue
and T4_BAR2_QTYPE_INGRESS for Ingress Queues.

This may return an error which indicates that BAR2 SGE Queue
registers aren't available.  If an error is not returned, then the

.. _`t4_bar2_sge_qregs.following-values-are-returned`:

following values are returned
-----------------------------


\*\ ``pbar2_qoffset``\ : the BAR2 Offset of the \ ``qid``\  Registers
\*\ ``pbar2_qid``\ : the BAR2 SGE Queue ID or 0 of \ ``qid``\ 

If the returned BAR2 Queue ID is 0, then BAR2 SGE registers which
require the "Inferred Queue ID" ability may be used.  E.g. the
Write Combining Doorbell Buffer. If the BAR2 Queue ID is not 0,
then these "Inferred Queue ID" register may not be used.

.. _`t4_init_devlog_params`:

t4_init_devlog_params
=====================

.. c:function:: int t4_init_devlog_params(struct adapter *adap)

    initialize adapter->params.devlog

    :param struct adapter \*adap:
        the adapter

.. _`t4_init_devlog_params.description`:

Description
-----------

Initialize various fields of the adapter's Firmware Device Log
Parameters structure.

.. _`t4_init_sge_params`:

t4_init_sge_params
==================

.. c:function:: int t4_init_sge_params(struct adapter *adapter)

    initialize adap->params.sge

    :param struct adapter \*adapter:
        the adapter

.. _`t4_init_sge_params.description`:

Description
-----------

Initialize various fields of the adapter's SGE Parameters structure.

.. _`t4_init_tp_params`:

t4_init_tp_params
=================

.. c:function:: int t4_init_tp_params(struct adapter *adap)

    initialize adap->params.tp

    :param struct adapter \*adap:
        the adapter

.. _`t4_init_tp_params.description`:

Description
-----------

Initialize various fields of the adapter's TP Parameters structure.

.. _`t4_filter_field_shift`:

t4_filter_field_shift
=====================

.. c:function:: int t4_filter_field_shift(const struct adapter *adap, int filter_sel)

    calculate filter field shift

    :param const struct adapter \*adap:
        the adapter

    :param int filter_sel:
        the desired field (from TP_VLAN_PRI_MAP bits)

.. _`t4_filter_field_shift.description`:

Description
-----------

Return the shift position of a filter field within the Compressed
Filter Tuple.  The filter field is specified via its selection bit
within TP_VLAN_PRI_MAL (filter mode).  E.g. F_VLAN.

.. _`t4_init_portinfo`:

t4_init_portinfo
================

.. c:function:: int t4_init_portinfo(struct port_info *pi, int mbox, int port, int pf, int vf, u8 mac[])

    allocate a virtual interface amd initialize port_info

    :param struct port_info \*pi:
        the port_info

    :param int mbox:
        mailbox to use for the FW command

    :param int port:
        physical port associated with the VI

    :param int pf:
        the PF owning the VI

    :param int vf:
        the VF owning the VI

    :param u8 mac:
        the MAC address of the VI

.. _`t4_init_portinfo.description`:

Description
-----------

Allocates a virtual interface for the given physical port.  If \ ``mac``\  is
not \ ``NULL``\  it contains the MAC address of the VI as assigned by FW.
\ ``mac``\  should be large enough to hold an Ethernet address.
Returns < 0 on error.

.. _`t4_read_cimq_cfg`:

t4_read_cimq_cfg
================

.. c:function:: void t4_read_cimq_cfg(struct adapter *adap, u16 *base, u16 *size, u16 *thres)

    read CIM queue configuration

    :param struct adapter \*adap:
        the adapter

    :param u16 \*base:
        holds the queue base addresses in bytes

    :param u16 \*size:
        holds the queue sizes in bytes

    :param u16 \*thres:
        holds the queue full thresholds in bytes

.. _`t4_read_cimq_cfg.description`:

Description
-----------

Returns the current configuration of the CIM queues, starting with
the IBQs, then the OBQs.

.. _`t4_read_cim_ibq`:

t4_read_cim_ibq
===============

.. c:function:: int t4_read_cim_ibq(struct adapter *adap, unsigned int qid, u32 *data, size_t n)

    read the contents of a CIM inbound queue

    :param struct adapter \*adap:
        the adapter

    :param unsigned int qid:
        the queue index

    :param u32 \*data:
        where to store the queue contents

    :param size_t n:
        capacity of \ ``data``\  in 32-bit words

.. _`t4_read_cim_ibq.description`:

Description
-----------

Reads the contents of the selected CIM queue starting at address 0 up
to the capacity of \ ``data``\ .  \ ``n``\  must be a multiple of 4.  Returns < 0 on
error and the number of 32-bit words actually read on success.

.. _`t4_read_cim_obq`:

t4_read_cim_obq
===============

.. c:function:: int t4_read_cim_obq(struct adapter *adap, unsigned int qid, u32 *data, size_t n)

    read the contents of a CIM outbound queue

    :param struct adapter \*adap:
        the adapter

    :param unsigned int qid:
        the queue index

    :param u32 \*data:
        where to store the queue contents

    :param size_t n:
        capacity of \ ``data``\  in 32-bit words

.. _`t4_read_cim_obq.description`:

Description
-----------

Reads the contents of the selected CIM queue starting at address 0 up
to the capacity of \ ``data``\ .  \ ``n``\  must be a multiple of 4.  Returns < 0 on
error and the number of 32-bit words actually read on success.

.. _`t4_cim_read`:

t4_cim_read
===========

.. c:function:: int t4_cim_read(struct adapter *adap, unsigned int addr, unsigned int n, unsigned int *valp)

    read a block from CIM internal address space

    :param struct adapter \*adap:
        the adapter

    :param unsigned int addr:
        the start address within the CIM address space

    :param unsigned int n:
        number of words to read

    :param unsigned int \*valp:
        where to store the result

.. _`t4_cim_read.description`:

Description
-----------

Reads a block of 4-byte words from the CIM intenal address space.

.. _`t4_cim_write`:

t4_cim_write
============

.. c:function:: int t4_cim_write(struct adapter *adap, unsigned int addr, unsigned int n, const unsigned int *valp)

    write a block into CIM internal address space

    :param struct adapter \*adap:
        the adapter

    :param unsigned int addr:
        the start address within the CIM address space

    :param unsigned int n:
        number of words to write

    :param const unsigned int \*valp:
        set of values to write

.. _`t4_cim_write.description`:

Description
-----------

Writes a block of 4-byte words into the CIM intenal address space.

.. _`t4_cim_read_la`:

t4_cim_read_la
==============

.. c:function:: int t4_cim_read_la(struct adapter *adap, u32 *la_buf, unsigned int *wrptr)

    read CIM LA capture buffer

    :param struct adapter \*adap:
        the adapter

    :param u32 \*la_buf:
        where to store the LA data

    :param unsigned int \*wrptr:
        the HW write pointer within the capture buffer

.. _`t4_cim_read_la.description`:

Description
-----------

Reads the contents of the CIM LA buffer with the most recent entry at
the end of the returned data and with the entry at \ ``wrptr``\  first.
We try to leave the LA in the running state we find it in.

.. _`t4_tp_read_la`:

t4_tp_read_la
=============

.. c:function:: void t4_tp_read_la(struct adapter *adap, u64 *la_buf, unsigned int *wrptr)

    read TP LA capture buffer

    :param struct adapter \*adap:
        the adapter

    :param u64 \*la_buf:
        where to store the LA data

    :param unsigned int \*wrptr:
        the HW write pointer within the capture buffer

.. _`t4_tp_read_la.description`:

Description
-----------

Reads the contents of the TP LA buffer with the most recent entry at
the end of the returned data and with the entry at \ ``wrptr``\  first.
We leave the LA in the running state we find it in.

.. _`t4_idma_monitor_init`:

t4_idma_monitor_init
====================

.. c:function:: void t4_idma_monitor_init(struct adapter *adapter, struct sge_idma_monitor_state *idma)

    initialize SGE Ingress DMA Monitor

    :param struct adapter \*adapter:
        the adapter

    :param struct sge_idma_monitor_state \*idma:
        the adapter IDMA Monitor state

.. _`t4_idma_monitor_init.description`:

Description
-----------

Initialize the state of an SGE Ingress DMA Monitor.

.. _`t4_idma_monitor`:

t4_idma_monitor
===============

.. c:function:: void t4_idma_monitor(struct adapter *adapter, struct sge_idma_monitor_state *idma, int hz, int ticks)

    monitor SGE Ingress DMA state

    :param struct adapter \*adapter:
        the adapter

    :param struct sge_idma_monitor_state \*idma:
        the adapter IDMA Monitor state

    :param int hz:
        number of ticks/second

    :param int ticks:
        number of ticks since the last IDMA Monitor call

.. This file was automatic generated / don't edit.

