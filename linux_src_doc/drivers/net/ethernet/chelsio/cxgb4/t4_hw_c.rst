.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4/t4_hw.c

.. _`t4_wait_op_done_val`:

t4_wait_op_done_val
===================

.. c:function:: int t4_wait_op_done_val(struct adapter *adapter, int reg, u32 mask, int polarity, int attempts, int delay, u32 *valp)

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param addr_reg:
        register holding the indirect addresses
    :type addr_reg: unsigned int

    :param data_reg:
        register holding the value for the indirect registers
    :type data_reg: unsigned int

    :param vals:
        values to write
    :type vals: const u32 \*

    :param nregs:
        how many indirect registers to write
    :type nregs: unsigned int

    :param start_idx:
        address of first indirect register to write
    :type start_idx: unsigned int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param cmd:
        the Firmware Mailbox Command or Reply
    :type cmd: const __be64 \*

    :param size:
        command length in bytes
    :type size: unsigned int

    :param access:
        the time (ms) needed to access the Firmware Mailbox
    :type access: int

    :param execute:
        the time (ms) the command spent being executed
    :type execute: int

.. _`t4_wr_mbox_meat_timeout`:

t4_wr_mbox_meat_timeout
=======================

.. c:function:: int t4_wr_mbox_meat_timeout(struct adapter *adap, int mbox, const void *cmd, int size, void *rpl, bool sleep_ok, int timeout)

    send a command to FW through the given mailbox

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        index of the mailbox to use
    :type mbox: int

    :param cmd:
        the command to write
    :type cmd: const void \*

    :param size:
        command length in bytes
    :type size: int

    :param rpl:
        where to optionally store the reply
    :type rpl: void \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

    :param timeout:
        time to wait for command to finish before timing out
    :type timeout: int

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

.. _`t4_memory_rw_init`:

t4_memory_rw_init
=================

.. c:function:: int t4_memory_rw_init(struct adapter *adap, int win, int mtype, u32 *mem_off, u32 *mem_base, u32 *mem_aperture)

    Get memory window relative offset, base, and size.

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param win:
        PCI-E Memory Window to use
    :type win: int

    :param mtype:
        memory type: MEM_EDC0, MEM_EDC1, MEM_HMA or MEM_MC
    :type mtype: int

    :param mem_off:
        memory relative offset with respect to \ ``mtype``\ .
    :type mem_off: u32 \*

    :param mem_base:
        configured memory base address.
    :type mem_base: u32 \*

    :param mem_aperture:
        configured memory window aperture.
    :type mem_aperture: u32 \*

.. _`t4_memory_rw_init.description`:

Description
-----------

Get the configured memory window's relative offset, base, and size.

.. _`t4_memory_update_win`:

t4_memory_update_win
====================

.. c:function:: void t4_memory_update_win(struct adapter *adap, int win, u32 addr)

    Move memory window to specified address.

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param win:
        PCI-E Memory Window to use
    :type win: int

    :param addr:
        location to move.
    :type addr: u32

.. _`t4_memory_update_win.description`:

Description
-----------

Move memory window to specified address.

.. _`t4_memory_rw_residual`:

t4_memory_rw_residual
=====================

.. c:function:: void t4_memory_rw_residual(struct adapter *adap, u32 off, u32 addr, u8 *buf, int dir)

    Read/Write residual data.

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param off:
        relative offset within residual to start read/write.
    :type off: u32

    :param addr:
        address within indicated memory type.
    :type addr: u32

    :param buf:
        host memory buffer
    :type buf: u8 \*

    :param dir:
        direction of transfer T4_MEMORY_READ (1) or T4_MEMORY_WRITE (0)
    :type dir: int

.. _`t4_memory_rw_residual.description`:

Description
-----------

Read/Write residual data less than 32-bits.

.. _`t4_memory_rw`:

t4_memory_rw
============

.. c:function:: int t4_memory_rw(struct adapter *adap, int win, int mtype, u32 addr, u32 len, void *hbuf, int dir)

    read/write EDC 0, EDC 1 or MC via PCIE memory window

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param win:
        PCI-E Memory Window to use
    :type win: int

    :param mtype:
        memory type: MEM_EDC0, MEM_EDC1 or MEM_MC
    :type mtype: int

    :param addr:
        address within indicated memory type
    :type addr: u32

    :param len:
        amount of memory to transfer
    :type len: u32

    :param hbuf:
        host memory buffer
    :type hbuf: void \*

    :param dir:
        direction of transfer T4_MEMORY_READ (1) or T4_MEMORY_WRITE (0)
    :type dir: int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4_get_regs_len.description`:

Description
-----------

Returns the size of the chip's BAR0 register space.

.. _`t4_get_regs`:

t4_get_regs
===========

.. c:function:: void t4_get_regs(struct adapter *adap, void *buf, size_t buf_size)

    read chip registers into provided buffer

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param buf:
        register buffer
    :type buf: void \*

    :param buf_size:
        size (in bytes) of register buffer
    :type buf_size: size_t

.. _`t4_get_regs.description`:

Description
-----------

If the provided register buffer isn't large enough for the chip's
full register range, the register dump will be truncated to the
register buffer's size.

.. _`t4_eeprom_ptov`:

t4_eeprom_ptov
==============

.. c:function:: int t4_eeprom_ptov(unsigned int phys_addr, unsigned int fn, unsigned int sz)

    translate a physical EEPROM address to virtual

    :param phys_addr:
        the physical EEPROM address
    :type phys_addr: unsigned int

    :param fn:
        the PCI function number
    :type fn: unsigned int

    :param sz:
        size of function-specific area
    :type sz: unsigned int

.. _`t4_eeprom_ptov.description`:

Description
-----------

Translate a physical EEPROM address to virtual.  The first 1K is
accessed through virtual addresses starting at 31K, the rest is
accessed through virtual addresses starting at 0.

.. _`t4_eeprom_ptov.the-mapping-is-as-follows`:

The mapping is as follows
-------------------------

[0..1K) -> [31K..32K)
[1K..1K+A) -> [31K-A..31K)
[1K+A..ES) -> [0..ES-A-1K)

where A = \ ``fn``\  \* \ ``sz``\ , and ES = EEPROM size.

.. _`t4_seeprom_wp`:

t4_seeprom_wp
=============

.. c:function:: int t4_seeprom_wp(struct adapter *adapter, bool enable)

    enable/disable EEPROM write protection

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param enable:
        whether to enable or disable write protection
    :type enable: bool

.. _`t4_seeprom_wp.description`:

Description
-----------

Enables or disables write protection on the serial EEPROM.

.. _`t4_get_raw_vpd_params`:

t4_get_raw_vpd_params
=====================

.. c:function:: int t4_get_raw_vpd_params(struct adapter *adapter, struct vpd_params *p)

    read VPD parameters from VPD EEPROM

    :param adapter:
        adapter to read
    :type adapter: struct adapter \*

    :param p:
        where to store the parameters
    :type p: struct vpd_params \*

.. _`t4_get_raw_vpd_params.description`:

Description
-----------

Reads card parameters stored in VPD EEPROM.

.. _`t4_get_vpd_params`:

t4_get_vpd_params
=================

.. c:function:: int t4_get_vpd_params(struct adapter *adapter, struct vpd_params *p)

    read VPD parameters & retrieve Core Clock

    :param adapter:
        adapter to read
    :type adapter: struct adapter \*

    :param p:
        where to store the parameters
    :type p: struct vpd_params \*

.. _`t4_get_vpd_params.description`:

Description
-----------

Reads card parameters stored in VPD EEPROM and retrieves the Core
Clock.  This can only be called after a connection to the firmware
is established.

.. _`t4_get_pfres`:

t4_get_pfres
============

.. c:function:: int t4_get_pfres(struct adapter *adapter)

    retrieve VF resource limits

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4_get_pfres.description`:

Description
-----------

Retrieves configured resource limits and capabilities for a physical
function.  The results are stored in \ ``adapter->pfres``\ .

.. _`sf1_read`:

sf1_read
========

.. c:function:: int sf1_read(struct adapter *adapter, unsigned int byte_cnt, int cont, int lock, u32 *valp)

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

    :param lock:
        whether to lock SF for PL access only
    :type lock: int

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

.. c:function:: int sf1_write(struct adapter *adapter, unsigned int byte_cnt, int cont, int lock, u32 val)

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

    :param lock:
        whether to lock SF for PL access only
    :type lock: int

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

.. _`t4_read_flash`:

t4_read_flash
=============

.. c:function:: int t4_read_flash(struct adapter *adapter, unsigned int addr, unsigned int nwords, u32 *data, int byte_oriented)

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param addr:
        the start address to write
    :type addr: unsigned int

    :param n:
        length of data to write in bytes
    :type n: unsigned int

    :param data:
        the data to write
    :type data: const u8 \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param vers:
        where to place the version
    :type vers: u32 \*

.. _`t4_get_fw_version.description`:

Description
-----------

Reads the FW version from flash.

.. _`t4_get_bs_version`:

t4_get_bs_version
=================

.. c:function:: int t4_get_bs_version(struct adapter *adapter, u32 *vers)

    read the firmware bootstrap version

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param vers:
        where to place the version
    :type vers: u32 \*

.. _`t4_get_bs_version.description`:

Description
-----------

Reads the FW Bootstrap version from flash.

.. _`t4_get_tp_version`:

t4_get_tp_version
=================

.. c:function:: int t4_get_tp_version(struct adapter *adapter, u32 *vers)

    read the TP microcode version

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param vers:
        where to place the version
    :type vers: u32 \*

.. _`t4_get_tp_version.description`:

Description
-----------

Reads the TP microcode version from flash.

.. _`t4_get_exprom_version`:

t4_get_exprom_version
=====================

.. c:function:: int t4_get_exprom_version(struct adapter *adap, u32 *vers)

    return the Expansion ROM version (if any)

    :param adap:
        *undescribed*
    :type adap: struct adapter \*

    :param vers:
        where to place the version
    :type vers: u32 \*

.. _`t4_get_exprom_version.description`:

Description
-----------

Reads the Expansion ROM header from FLASH and returns the version
number (if present) through the \ ``vers``\  return value pointer.  We return
this in the Firmware Version Format since it's convenient.  Return
0 on success, -ENOENT if no Expansion ROM is present.

.. _`t4_get_vpd_version`:

t4_get_vpd_version
==================

.. c:function:: int t4_get_vpd_version(struct adapter *adapter, u32 *vers)

    return the VPD version

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param vers:
        where to place the version
    :type vers: u32 \*

.. _`t4_get_vpd_version.description`:

Description
-----------

Reads the VPD via the Firmware interface (thus this can only be called
once we're ready to issue Firmware commands).  The format of the
VPD version is adapter specific.  Returns 0 on success, an error on
failure.

Note that early versions of the Firmware didn't include the ability
to retrieve the VPD version, so we zero-out the return-value parameter
in that case to avoid leaving it with garbage in it.

Also note that the Firmware will return its cached copy of the VPD
Revision ID, not the actual Revision ID as written in the Serial
EEPROM.  This is only an issue if a new VPD has been written and the
Firmware/Chip haven't yet gone through a RESET sequence.  So it's best
to defer calling this routine till after a FW_RESET_CMD has been issued
if the Host Driver will be performing a full adapter initialization.

.. _`t4_get_scfg_version`:

t4_get_scfg_version
===================

.. c:function:: int t4_get_scfg_version(struct adapter *adapter, u32 *vers)

    return the Serial Configuration version

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param vers:
        where to place the version
    :type vers: u32 \*

.. _`t4_get_scfg_version.description`:

Description
-----------

Reads the Serial Configuration Version via the Firmware interface
(thus this can only be called once we're ready to issue Firmware
commands).  The format of the Serial Configuration version is
adapter specific.  Returns 0 on success, an error on failure.

Note that early versions of the Firmware didn't include the ability
to retrieve the Serial Configuration version, so we zero-out the
return-value parameter in that case to avoid leaving it with
garbage in it.

Also note that the Firmware will return its cached copy of the Serial
Initialization Revision ID, not the actual Revision ID as written in
the Serial EEPROM.  This is only an issue if a new VPD has been written
and the Firmware/Chip haven't yet gone through a RESET sequence.  So
it's best to defer calling this routine till after a FW_RESET_CMD has
been issued if the Host Driver will be performing a full adapter
initialization.

.. _`t4_get_version_info`:

t4_get_version_info
===================

.. c:function:: int t4_get_version_info(struct adapter *adapter)

    extract various chip/firmware version information

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4_get_version_info.description`:

Description
-----------

Reads various chip/firmware version numbers and stores them into the
adapter Adapter Parameters structure.  If any of the efforts fails
the first failure will be returned, but all of the version numbers
will be read.

.. _`t4_dump_version_info`:

t4_dump_version_info
====================

.. c:function:: void t4_dump_version_info(struct adapter *adapter)

    dump all of the adapter configuration IDs

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4_dump_version_info.description`:

Description
-----------

Dumps all of the various bits of adapter configuration version/revision
IDs information.  This is typically called at some point after
\ :c:func:`t4_get_version_info`\  has been called.

.. _`t4_check_fw_version`:

t4_check_fw_version
===================

.. c:function:: int t4_check_fw_version(struct adapter *adap)

    check if the FW is supported with this driver

    :param adap:
        the adapter
    :type adap: struct adapter \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param start:
        the first sector to erase
    :type start: int

    :param end:
        the last sector to erase
    :type end: int

.. _`t4_flash_erase_sectors.description`:

Description
-----------

Erases the sectors in the given inclusive range.

.. _`t4_flash_cfg_addr`:

t4_flash_cfg_addr
=================

.. c:function:: unsigned int t4_flash_cfg_addr(struct adapter *adapter)

    return the address of the flash configuration file

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param fw_data:
        the firmware image to write
    :type fw_data: const u8 \*

    :param size:
        image size
    :type size: unsigned int

.. _`t4_load_fw.description`:

Description
-----------

Write the supplied firmware image to the card's serial flash.

.. _`t4_phy_fw_ver`:

t4_phy_fw_ver
=============

.. c:function:: int t4_phy_fw_ver(struct adapter *adap, int *phy_fw_ver)

    return current PHY firmware version

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param phy_fw_ver:
        return value buffer for PHY firmware version
    :type phy_fw_ver: int \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param win:
        the PCI-E Memory Window index to use for \ :c:func:`t4_memory_rw`\ 
    :type win: int

    :param win_lock:
        the lock to use to guard the memory copy
    :type win_lock: spinlock_t \*

    :param int (\*phy_fw_version)(const u8 \*, size_t):
        function to check PHY firmware versions

    :param phy_fw_data:
        the PHY firmware image to write
    :type phy_fw_data: const u8 \*

    :param phy_fw_size:
        image size
    :type phy_fw_size: size_t

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param op:
        the operation (flush or flush and invalidate)
    :type op: enum fw_params_param_dev_fwcache

.. _`fwcaps16_to_caps32`:

fwcaps16_to_caps32
==================

.. c:function:: fw_port_cap32_t fwcaps16_to_caps32(fw_port_cap16_t caps16)

    convert 16-bit Port Capabilities to 32-bits

    :param caps16:
        a 16-bit Port Capabilities value
    :type caps16: fw_port_cap16_t

.. _`fwcaps16_to_caps32.description`:

Description
-----------

Returns the equivalent 32-bit Port Capabilities value.

.. _`fwcaps32_to_caps16`:

fwcaps32_to_caps16
==================

.. c:function:: fw_port_cap16_t fwcaps32_to_caps16(fw_port_cap32_t caps32)

    convert 32-bit Port Capabilities to 16-bits

    :param caps32:
        a 32-bit Port Capabilities value
    :type caps32: fw_port_cap32_t

.. _`fwcaps32_to_caps16.description`:

Description
-----------

Returns the equivalent 16-bit Port Capabilities value.  Note that
not all 32-bit Port Capabilities can be represented in the 16-bit
Port Capabilities and some fields/values may not make it.

.. _`t4_link_l1cfg_core`:

t4_link_l1cfg_core
==================

.. c:function:: int t4_link_l1cfg_core(struct adapter *adapter, unsigned int mbox, unsigned int port, struct link_config *lc, bool sleep_ok, int timeout)

    apply link configuration to MAC/PHY

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param mbox:
        the Firmware Mailbox to use
    :type mbox: unsigned int

    :param port:
        the Port ID
    :type port: unsigned int

    :param lc:
        the Port's Link Configuration
    :type lc: struct link_config \*

    :param sleep_ok:
        *undescribed*
    :type sleep_ok: bool

    :param timeout:
        *undescribed*
    :type timeout: int

.. _`t4_link_l1cfg_core.description`:

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mbox to use for the FW command
    :type mbox: unsigned int

    :param port:
        the port id
    :type port: unsigned int

.. _`t4_restart_aneg.description`:

Description
-----------

Restarts autonegotiation for the selected port.

.. _`t4_handle_intr_status`:

t4_handle_intr_status
=====================

.. c:function:: int t4_handle_intr_status(struct adapter *adapter, unsigned int reg, const struct intr_info *acts)

    table driven interrupt handler

    :param adapter:
        the adapter that generated the interrupt
    :type adapter: struct adapter \*

    :param reg:
        the interrupt status register to process
    :type reg: unsigned int

    :param acts:
        table of interrupt actions
    :type acts: const struct intr_info \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

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

    :param adapter:
        the adapter whose interrupts should be enabled
    :type adapter: struct adapter \*

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

    :param adapter:
        the adapter whose interrupts should be disabled
    :type adapter: struct adapter \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param mbox:
        mbox to use for the FW command
    :type mbox: int

    :param viid:
        virtual interface whose RSS subtable is to be written
    :type viid: unsigned int

    :param start:
        start entry in the table to write
    :type start: int

    :param n:
        how many table entries to write
    :type n: int

    :param rspq:
        values for the response queue lookup table
    :type rspq: const u16 \*

    :param nrspq:
        number of values in \ ``rspq``\ 
    :type nrspq: unsigned int

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param mbox:
        mbox to use for the FW command
    :type mbox: int

    :param mode:
        global RSS mode
    :type mode: unsigned int

    :param flags:
        mode-specific flags
    :type flags: unsigned int

.. _`t4_config_glbl_rss.description`:

Description
-----------

Sets the global RSS mode.

.. _`t4_config_vi_rss`:

t4_config_vi_rss
================

.. c:function:: int t4_config_vi_rss(struct adapter *adapter, int mbox, unsigned int viid, unsigned int flags, unsigned int defq)

    configure per VI RSS settings

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param mbox:
        mbox to use for the FW command
    :type mbox: int

    :param viid:
        the VI id
    :type viid: unsigned int

    :param flags:
        RSS flags
    :type flags: unsigned int

    :param defq:
        id of the default RSS queue for the VI.
    :type defq: unsigned int

.. _`t4_config_vi_rss.description`:

Description
-----------

Configures VI-specific RSS properties.

.. _`t4_read_rss`:

t4_read_rss
===========

.. c:function:: int t4_read_rss(struct adapter *adapter, u16 *map)

    read the contents of the RSS mapping table

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param map:
        holds the contents of the RSS mapping table
    :type map: u16 \*

.. _`t4_read_rss.description`:

Description
-----------

Reads the contents of the RSS hash->queue mapping table.

.. _`t4_tp_fw_ldst_rw`:

t4_tp_fw_ldst_rw
================

.. c:function:: int t4_tp_fw_ldst_rw(struct adapter *adap, int cmd, u32 *vals, unsigned int nregs, unsigned int start_index, unsigned int rw, bool sleep_ok)

    Access TP indirect register through LDST

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param cmd:
        TP fw ldst address space type
    :type cmd: int

    :param vals:
        where the indirect register values are stored/written
    :type vals: u32 \*

    :param nregs:
        how many indirect registers to read/write
    :type nregs: unsigned int

    :param start_index:
        *undescribed*
    :type start_index: unsigned int

    :param rw:
        Read (1) or Write (0)
    :type rw: unsigned int

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_fw_ldst_rw.description`:

Description
-----------

Access TP indirect registers through LDST

.. _`t4_tp_indirect_rw`:

t4_tp_indirect_rw
=================

.. c:function:: void t4_tp_indirect_rw(struct adapter *adap, u32 reg_addr, u32 reg_data, u32 *buff, u32 nregs, u32 start_index, int rw, bool sleep_ok)

    Read/Write TP indirect register through LDST or backdoor

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param reg_addr:
        Address Register
    :type reg_addr: u32

    :param reg_data:
        Data register
    :type reg_data: u32

    :param buff:
        where the indirect register values are stored/written
    :type buff: u32 \*

    :param nregs:
        how many indirect registers to read/write
    :type nregs: u32

    :param start_index:
        index of first indirect register to read/write
    :type start_index: u32

    :param rw:
        READ(1) or WRITE(0)
    :type rw: int

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_indirect_rw.description`:

Description
-----------

Read/Write TP indirect registers through LDST if possible.
Else, use backdoor access

.. _`t4_tp_pio_read`:

t4_tp_pio_read
==============

.. c:function:: void t4_tp_pio_read(struct adapter *adap, u32 *buff, u32 nregs, u32 start_index, bool sleep_ok)

    Read TP PIO registers

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param buff:
        where the indirect register values are written
    :type buff: u32 \*

    :param nregs:
        how many indirect registers to read
    :type nregs: u32

    :param start_index:
        index of first indirect register to read
    :type start_index: u32

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_pio_read.description`:

Description
-----------

Read TP PIO Registers

.. _`t4_tp_pio_write`:

t4_tp_pio_write
===============

.. c:function:: void t4_tp_pio_write(struct adapter *adap, u32 *buff, u32 nregs, u32 start_index, bool sleep_ok)

    Write TP PIO registers

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param buff:
        where the indirect register values are stored
    :type buff: u32 \*

    :param nregs:
        how many indirect registers to write
    :type nregs: u32

    :param start_index:
        index of first indirect register to write
    :type start_index: u32

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_pio_write.description`:

Description
-----------

Write TP PIO Registers

.. _`t4_tp_tm_pio_read`:

t4_tp_tm_pio_read
=================

.. c:function:: void t4_tp_tm_pio_read(struct adapter *adap, u32 *buff, u32 nregs, u32 start_index, bool sleep_ok)

    Read TP TM PIO registers

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param buff:
        where the indirect register values are written
    :type buff: u32 \*

    :param nregs:
        how many indirect registers to read
    :type nregs: u32

    :param start_index:
        index of first indirect register to read
    :type start_index: u32

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_tm_pio_read.description`:

Description
-----------

Read TP TM PIO Registers

.. _`t4_tp_mib_read`:

t4_tp_mib_read
==============

.. c:function:: void t4_tp_mib_read(struct adapter *adap, u32 *buff, u32 nregs, u32 start_index, bool sleep_ok)

    Read TP MIB registers

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param buff:
        where the indirect register values are written
    :type buff: u32 \*

    :param nregs:
        how many indirect registers to read
    :type nregs: u32

    :param start_index:
        index of first indirect register to read
    :type start_index: u32

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_mib_read.description`:

Description
-----------

Read TP MIB Registers

.. _`t4_read_rss_key`:

t4_read_rss_key
===============

.. c:function:: void t4_read_rss_key(struct adapter *adap, u32 *key, bool sleep_ok)

    read the global RSS key

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param key:
        10-entry array holding the 320-bit RSS key
    :type key: u32 \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_read_rss_key.description`:

Description
-----------

Reads the global 320-bit RSS key.

.. _`t4_write_rss_key`:

t4_write_rss_key
================

.. c:function:: void t4_write_rss_key(struct adapter *adap, const u32 *key, int idx, bool sleep_ok)

    program one of the RSS keys

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param key:
        10-entry array holding the 320-bit RSS key
    :type key: const u32 \*

    :param idx:
        which RSS key to write
    :type idx: int

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_write_rss_key.description`:

Description
-----------

Writes one of the RSS keys with the given 320-bit value.  If \ ``idx``\  is
0..15 the corresponding entry in the RSS key table is written,
otherwise the global RSS key is written.

.. _`t4_read_rss_pf_config`:

t4_read_rss_pf_config
=====================

.. c:function:: void t4_read_rss_pf_config(struct adapter *adapter, unsigned int index, u32 *valp, bool sleep_ok)

    read PF RSS Configuration Table

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param index:
        the entry in the PF RSS table to read
    :type index: unsigned int

    :param valp:
        where to store the returned value
    :type valp: u32 \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_read_rss_pf_config.description`:

Description
-----------

Reads the PF RSS Configuration Table at the specified index and returns
the value found there.

.. _`t4_read_rss_vf_config`:

t4_read_rss_vf_config
=====================

.. c:function:: void t4_read_rss_vf_config(struct adapter *adapter, unsigned int index, u32 *vfl, u32 *vfh, bool sleep_ok)

    read VF RSS Configuration Table

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param index:
        the entry in the VF RSS table to read
    :type index: unsigned int

    :param vfl:
        where to store the returned VFL
    :type vfl: u32 \*

    :param vfh:
        where to store the returned VFH
    :type vfh: u32 \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_read_rss_vf_config.description`:

Description
-----------

Reads the VF RSS Configuration Table at the specified index and returns
the (VFL, VFH) values found there.

.. _`t4_read_rss_pf_map`:

t4_read_rss_pf_map
==================

.. c:function:: u32 t4_read_rss_pf_map(struct adapter *adapter, bool sleep_ok)

    read PF RSS Map

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_read_rss_pf_map.description`:

Description
-----------

Reads the PF RSS Map register and returns its value.

.. _`t4_read_rss_pf_mask`:

t4_read_rss_pf_mask
===================

.. c:function:: u32 t4_read_rss_pf_mask(struct adapter *adapter, bool sleep_ok)

    read PF RSS Mask

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_read_rss_pf_mask.description`:

Description
-----------

Reads the PF RSS Mask register and returns its value.

.. _`t4_tp_get_tcp_stats`:

t4_tp_get_tcp_stats
===================

.. c:function:: void t4_tp_get_tcp_stats(struct adapter *adap, struct tp_tcp_stats *v4, struct tp_tcp_stats *v6, bool sleep_ok)

    read TP's TCP MIB counters

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param v4:
        holds the TCP/IP counter values
    :type v4: struct tp_tcp_stats \*

    :param v6:
        holds the TCP/IPv6 counter values
    :type v6: struct tp_tcp_stats \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_get_tcp_stats.description`:

Description
-----------

Returns the values of TP's TCP/IP and TCP/IPv6 MIB counters.
Either \ ``v4``\  or \ ``v6``\  may be \ ``NULL``\  to skip the corresponding stats.

.. _`t4_tp_get_err_stats`:

t4_tp_get_err_stats
===================

.. c:function:: void t4_tp_get_err_stats(struct adapter *adap, struct tp_err_stats *st, bool sleep_ok)

    read TP's error MIB counters

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param st:
        holds the counter values
    :type st: struct tp_err_stats \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_get_err_stats.description`:

Description
-----------

Returns the values of TP's error counters.

.. _`t4_tp_get_cpl_stats`:

t4_tp_get_cpl_stats
===================

.. c:function:: void t4_tp_get_cpl_stats(struct adapter *adap, struct tp_cpl_stats *st, bool sleep_ok)

    read TP's CPL MIB counters

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param st:
        holds the counter values
    :type st: struct tp_cpl_stats \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_get_cpl_stats.description`:

Description
-----------

Returns the values of TP's CPL counters.

.. _`t4_tp_get_rdma_stats`:

t4_tp_get_rdma_stats
====================

.. c:function:: void t4_tp_get_rdma_stats(struct adapter *adap, struct tp_rdma_stats *st, bool sleep_ok)

    read TP's RDMA MIB counters

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param st:
        holds the counter values
    :type st: struct tp_rdma_stats \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_tp_get_rdma_stats.description`:

Description
-----------

Returns the values of TP's RDMA counters.

.. _`t4_get_fcoe_stats`:

t4_get_fcoe_stats
=================

.. c:function:: void t4_get_fcoe_stats(struct adapter *adap, unsigned int idx, struct tp_fcoe_stats *st, bool sleep_ok)

    read TP's FCoE MIB counters for a port

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param idx:
        the port index
    :type idx: unsigned int

    :param st:
        holds the counter values
    :type st: struct tp_fcoe_stats \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_get_fcoe_stats.description`:

Description
-----------

Returns the values of TP's FCoE counters for the selected port.

.. _`t4_get_usm_stats`:

t4_get_usm_stats
================

.. c:function:: void t4_get_usm_stats(struct adapter *adap, struct tp_usm_stats *st, bool sleep_ok)

    read TP's non-TCP DDP MIB counters

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param st:
        holds the counter values
    :type st: struct tp_usm_stats \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_get_usm_stats.description`:

Description
-----------

Returns the values of TP's counters for non-TCP directly-placed packets.

.. _`t4_read_mtu_tbl`:

t4_read_mtu_tbl
===============

.. c:function:: void t4_read_mtu_tbl(struct adapter *adap, u16 *mtus, u8 *mtu_log)

    returns the values in the HW path MTU table

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mtus:
        where to store the MTU values
    :type mtus: u16 \*

    :param mtu_log:
        where to store the MTU base-2 log (may be \ ``NULL``\ )
    :type mtu_log: u8 \*

.. _`t4_read_mtu_tbl.description`:

Description
-----------

Reads the HW path MTU table.

.. _`t4_read_cong_tbl`:

t4_read_cong_tbl
================

.. c:function:: void t4_read_cong_tbl(struct adapter *adap, u16 incr)

    reads the congestion control table

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param incr:
        where to store the alpha values
    :type incr: u16

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param addr:
        the indirect TP register address
    :type addr: unsigned int

    :param mask:
        specifies the field within the register to modify
    :type mask: unsigned int

    :param val:
        new value for the field
    :type val: unsigned int

.. _`t4_tp_wr_bits_indirect.description`:

Description
-----------

Sets a field of an indirect TP register to the given value.

.. _`init_cong_ctrl`:

init_cong_ctrl
==============

.. c:function:: void init_cong_ctrl(unsigned short *a, unsigned short *b)

    initialize congestion control parameters

    :param a:
        the alpha values for congestion control
    :type a: unsigned short \*

    :param b:
        the beta values for congestion control
    :type b: unsigned short \*

.. _`init_cong_ctrl.description`:

Description
-----------

Initialize the congestion control parameters.

.. _`t4_load_mtus`:

t4_load_mtus
============

.. c:function:: void t4_load_mtus(struct adapter *adap, const unsigned short *mtus, const unsigned short *alpha, const unsigned short *beta)

    write the MTU and congestion control HW tables

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mtus:
        the values for the MTU table
    :type mtus: const unsigned short \*

    :param alpha:
        the values for the congestion control alpha parameter
    :type alpha: const unsigned short \*

    :param beta:
        the values for the congestion control beta parameter
    :type beta: const unsigned short \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param nic_rate:
        rates for NIC traffic
    :type nic_rate: u64 \*

    :param ofld_rate:
        rates for offloaded traffic
    :type ofld_rate: u64 \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param tp:
        the desired trace filter parameters
    :type tp: const struct trace_params \*

    :param idx:
        which filter to configure
    :type idx: int

    :param enable:
        whether to enable or disable the filter
    :type enable: int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param tp:
        the current trace filter parameters
    :type tp: struct trace_params \*

    :param idx:
        which trace filter to query
    :type idx: int

    :param enabled:
        non-zero if the filter is enabled
    :type enabled: int \*

.. _`t4_get_trace_filter.description`:

Description
-----------

Returns the current settings of one of the HW tracing filters.

.. _`t4_pmtx_get_stats`:

t4_pmtx_get_stats
=================

.. c:function:: void t4_pmtx_get_stats(struct adapter *adap, u32 cnt, u64 cycles)

    returns the HW stats from PMTX

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param cnt:
        where to store the count statistics
    :type cnt: u32

    :param cycles:
        where to store the cycle statistics
    :type cycles: u64

.. _`t4_pmtx_get_stats.description`:

Description
-----------

Returns performance statistics from PMTX.

.. _`t4_pmrx_get_stats`:

t4_pmrx_get_stats
=================

.. c:function:: void t4_pmrx_get_stats(struct adapter *adap, u32 cnt, u64 cycles)

    returns the HW stats from PMRX

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param cnt:
        where to store the count statistics
    :type cnt: u32

    :param cycles:
        where to store the cycle statistics
    :type cycles: u64

.. _`t4_pmrx_get_stats.description`:

Description
-----------

Returns performance statistics from PMRX.

.. _`compute_mps_bg_map`:

compute_mps_bg_map
==================

.. c:function:: unsigned int compute_mps_bg_map(struct adapter *adapter, int pidx)

    compute the MPS Buffer Group Map for a Port

    :param adapter:
        *undescribed*
    :type adapter: struct adapter \*

    :param pidx:
        the port index
    :type pidx: int

.. _`compute_mps_bg_map.description`:

Description
-----------

Computes and returns a bitmap indicating which MPS buffer groups are
associated with the given Port.  Bit i is set if buffer group i is
used by the Port.

.. _`t4_get_mps_bg_map`:

t4_get_mps_bg_map
=================

.. c:function:: unsigned int t4_get_mps_bg_map(struct adapter *adapter, int pidx)

    return the buffer groups associated with a port

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param pidx:
        the port index
    :type pidx: int

.. _`t4_get_mps_bg_map.description`:

Description
-----------

Returns a bitmap indicating which MPS buffer groups are associated
with the given Port.  Bit i is set if buffer group i is used by the
Port.

.. _`t4_get_tp_ch_map`:

t4_get_tp_ch_map
================

.. c:function:: unsigned int t4_get_tp_ch_map(struct adapter *adap, int pidx)

    return TP ingress channels associated with a port

    :param adap:
        *undescribed*
    :type adap: struct adapter \*

    :param pidx:
        the port index
    :type pidx: int

.. _`t4_get_tp_ch_map.description`:

Description
-----------

Returns a bitmap indicating which TP Ingress Channels are associated
with a given Port.  Bit i is set if TP Ingress Channel i is used by
the Port.

.. _`t4_get_port_type_description`:

t4_get_port_type_description
============================

.. c:function:: const char *t4_get_port_type_description(enum fw_port_type port_type)

    return Port Type string description

    :param port_type:
        firmware Port Type enumeration
    :type port_type: enum fw_port_type

.. _`t4_get_port_stats_offset`:

t4_get_port_stats_offset
========================

.. c:function:: void t4_get_port_stats_offset(struct adapter *adap, int idx, struct port_stats *stats, struct port_stats *offset)

    collect port stats relative to a previous snapshot

    :param adap:
        The adapter
    :type adap: struct adapter \*

    :param idx:
        The port
    :type idx: int

    :param stats:
        Current stats to fill
    :type stats: struct port_stats \*

    :param offset:
        Previous stats snapshot
    :type offset: struct port_stats \*

.. _`t4_get_port_stats`:

t4_get_port_stats
=================

.. c:function:: void t4_get_port_stats(struct adapter *adap, int idx, struct port_stats *p)

    collect port statistics

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param idx:
        the port index
    :type idx: int

    :param p:
        the stats structure to fill
    :type p: struct port_stats \*

.. _`t4_get_port_stats.description`:

Description
-----------

Collect statistics related to the given port from HW.

.. _`t4_get_lb_stats`:

t4_get_lb_stats
===============

.. c:function:: void t4_get_lb_stats(struct adapter *adap, int idx, struct lb_port_stats *p)

    collect loopback port statistics

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param idx:
        the loopback port index
    :type idx: int

    :param p:
        the stats structure to fill
    :type p: struct lb_port_stats \*

.. _`t4_get_lb_stats.description`:

Description
-----------

Return HW statistics for the given loopback port.

.. _`t4_mdio_rd`:

t4_mdio_rd
==========

.. c:function:: int t4_mdio_rd(struct adapter *adap, unsigned int mbox, unsigned int phy_addr, unsigned int mmd, unsigned int reg, u16 *valp)

    read a PHY register through MDIO

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param phy_addr:
        the PHY address
    :type phy_addr: unsigned int

    :param mmd:
        the PHY MMD to access (0 for clause 22 PHYs)
    :type mmd: unsigned int

    :param reg:
        the register to read
    :type reg: unsigned int

    :param valp:
        where to store the value
    :type valp: u16 \*

.. _`t4_mdio_rd.description`:

Description
-----------

Issues a FW command through the given mailbox to read a PHY register.

.. _`t4_mdio_wr`:

t4_mdio_wr
==========

.. c:function:: int t4_mdio_wr(struct adapter *adap, unsigned int mbox, unsigned int phy_addr, unsigned int mmd, unsigned int reg, u16 val)

    write a PHY register through MDIO

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param phy_addr:
        the PHY address
    :type phy_addr: unsigned int

    :param mmd:
        the PHY MMD to access (0 for clause 22 PHYs)
    :type mmd: unsigned int

    :param reg:
        the register to write
    :type reg: unsigned int

    :param val:
        *undescribed*
    :type val: u16

.. _`t4_mdio_wr.description`:

Description
-----------

Issues a FW command through the given mailbox to write a PHY register.

.. _`t4_sge_decode_idma_state`:

t4_sge_decode_idma_state
========================

.. c:function:: void t4_sge_decode_idma_state(struct adapter *adapter, int state)

    decode the idma state

    :param adapter:
        *undescribed*
    :type adapter: struct adapter \*

    :param state:
        the state idma is stuck in
    :type state: int

.. _`t4_sge_ctxt_flush`:

t4_sge_ctxt_flush
=================

.. c:function:: int t4_sge_ctxt_flush(struct adapter *adap, unsigned int mbox, int ctxt_type)

    flush the SGE context cache

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param ctxt_type:
        *undescribed*
    :type ctxt_type: int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param evt_mbox:
        mailbox to receive async FW events
    :type evt_mbox: unsigned int

    :param master:
        specifies the caller's willingness to be the device master
    :type master: enum dev_master

    :param state:
        returns the current device state (if non-NULL)
    :type state: enum dev_state \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

.. _`t4_fw_bye.description`:

Description
-----------

Issues a command to terminate communication with FW.

.. _`t4_early_init`:

t4_early_init
=============

.. c:function:: int t4_early_init(struct adapter *adap, unsigned int mbox)

    ask FW to initialize the device

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param reset:
        specifies the type of reset to perform
    :type reset: int

.. _`t4_fw_reset.description`:

Description
-----------

Issues a reset command of the specified type to FW.

.. _`t4_fw_halt`:

t4_fw_halt
==========

.. c:function:: int t4_fw_halt(struct adapter *adap, unsigned int mbox, int force)

    issue a reset/halt to FW and put uP into RESET

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW RESET command (if desired)
    :type mbox: unsigned int

    :param force:
        force uP into RESET even if FW RESET command fails
    :type force: int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        *undescribed*
    :type mbox: unsigned int

    :param reset:
        if we want to do a RESET to restart things
    :type reset: int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW RESET command (if desired)
    :type mbox: unsigned int

    :param fw_data:
        the firmware image to write
    :type fw_data: const u8 \*

    :param size:
        image size
    :type size: unsigned int

    :param force:
        force upgrade even if firmware doesn't cooperate
    :type force: int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param page_size:
        the host's Base Page Size
    :type page_size: unsigned int

    :param cache_line_size:
        the host's Cache Line Size
    :type cache_line_size: unsigned int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

.. _`t4_fw_initialize.description`:

Description
-----------

Issues a command to FW to partially initialize the device.  This
performs initialization that generally doesn't depend on user input.

.. _`t4_query_params_rw`:

t4_query_params_rw
==================

.. c:function:: int t4_query_params_rw(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int nparams, const u32 *params, u32 *val, int rw, bool sleep_ok)

    query FW or device parameters

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF
    :type pf: unsigned int

    :param vf:
        the VF
    :type vf: unsigned int

    :param nparams:
        the number of parameters
    :type nparams: unsigned int

    :param params:
        the parameter names
    :type params: const u32 \*

    :param val:
        the parameter values
    :type val: u32 \*

    :param rw:
        Write and read flag
    :type rw: int

    :param sleep_ok:
        if true, we may sleep awaiting mbox cmd completion
    :type sleep_ok: bool

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF
    :type pf: unsigned int

    :param vf:
        the VF
    :type vf: unsigned int

    :param nparams:
        the number of parameters
    :type nparams: unsigned int

    :param params:
        the parameter names
    :type params: const u32 \*

    :param val:
        the parameter values
    :type val: const u32 \*

    :param timeout:
        the timeout time
    :type timeout: int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF
    :type pf: unsigned int

    :param vf:
        the VF
    :type vf: unsigned int

    :param nparams:
        the number of parameters
    :type nparams: unsigned int

    :param params:
        the parameter names
    :type params: const u32 \*

    :param val:
        the parameter values
    :type val: const u32 \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF being configured
    :type pf: unsigned int

    :param vf:
        the VF being configured
    :type vf: unsigned int

    :param txq:
        the max number of egress queues
    :type txq: unsigned int

    :param txq_eth_ctrl:
        the max number of egress Ethernet or control queues
    :type txq_eth_ctrl: unsigned int

    :param rxqi:
        the max number of interrupt-capable ingress queues
    :type rxqi: unsigned int

    :param rxq:
        the max number of interruptless ingress queues
    :type rxq: unsigned int

    :param tc:
        the PCI traffic class
    :type tc: unsigned int

    :param vi:
        the max number of virtual interfaces
    :type vi: unsigned int

    :param cmask:
        the channel access rights mask for the PF/VF
    :type cmask: unsigned int

    :param pmask:
        the port access rights mask for the PF/VF
    :type pmask: unsigned int

    :param nexact:
        the maximum number of exact MPS filters
    :type nexact: unsigned int

    :param rcaps:
        read capabilities
    :type rcaps: unsigned int

    :param wxcaps:
        write/execute capabilities
    :type wxcaps: unsigned int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param port:
        physical port associated with the VI
    :type port: unsigned int

    :param pf:
        the PF owning the VI
    :type pf: unsigned int

    :param vf:
        the VF owning the VI
    :type vf: unsigned int

    :param nmac:
        number of MAC addresses needed (1 to 5)
    :type nmac: unsigned int

    :param mac:
        the MAC addresses of the VI
    :type mac: u8 \*

    :param rss_size:
        size of RSS table slice associated with this VI
    :type rss_size: unsigned int \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF owning the VI
    :type pf: unsigned int

    :param vf:
        the VF owning the VI
    :type vf: unsigned int

    :param viid:
        virtual interface identifiler
    :type viid: unsigned int

.. _`t4_free_vi.description`:

Description
-----------

Free a previously allocated virtual interface.

.. _`t4_set_rxmode`:

t4_set_rxmode
=============

.. c:function:: int t4_set_rxmode(struct adapter *adap, unsigned int mbox, unsigned int viid, int mtu, int promisc, int all_multi, int bcast, int vlanex, bool sleep_ok)

    set Rx properties of a virtual interface

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param viid:
        the VI id
    :type viid: unsigned int

    :param mtu:
        the new MTU or -1
    :type mtu: int

    :param promisc:
        1 to enable promiscuous mode, 0 to disable it, -1 no change
    :type promisc: int

    :param all_multi:
        1 to enable all-multi mode, 0 to disable it, -1 no change
    :type all_multi: int

    :param bcast:
        1 to enable broadcast Rx, 0 to disable it, -1 no change
    :type bcast: int

    :param vlanex:
        1 to enable HW VLAN extraction, 0 to disable it, -1 no change
    :type vlanex: int

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_set_rxmode.description`:

Description
-----------

Sets Rx properties of a virtual interface.

.. _`t4_free_encap_mac_filt`:

t4_free_encap_mac_filt
======================

.. c:function:: int t4_free_encap_mac_filt(struct adapter *adap, unsigned int viid, int idx, bool sleep_ok)

    frees MPS entry at given index

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param viid:
        the VI id
    :type viid: unsigned int

    :param idx:
        index of MPS entry to be freed
    :type idx: int

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

.. _`t4_free_encap_mac_filt.description`:

Description
-----------

Frees the MPS entry at supplied index

Returns a negative error number or zero on success

.. _`t4_free_raw_mac_filt`:

t4_free_raw_mac_filt
====================

.. c:function:: int t4_free_raw_mac_filt(struct adapter *adap, unsigned int viid, const u8 *addr, const u8 *mask, unsigned int idx, u8 lookup_type, u8 port_id, bool sleep_ok)

    Frees a raw mac entry in mps tcam

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param viid:
        the VI id
    :type viid: unsigned int

    :param addr:
        the MAC address
    :type addr: const u8 \*

    :param mask:
        the mask
    :type mask: const u8 \*

    :param idx:
        index of the entry in mps tcam
    :type idx: unsigned int

    :param lookup_type:
        MAC address for inner (1) or outer (0) header
    :type lookup_type: u8

    :param port_id:
        the port index
    :type port_id: u8

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

.. _`t4_free_raw_mac_filt.description`:

Description
-----------

Removes the mac entry at the specified index using raw mac interface.

Returns a negative error number on failure.

.. _`t4_alloc_encap_mac_filt`:

t4_alloc_encap_mac_filt
=======================

.. c:function:: int t4_alloc_encap_mac_filt(struct adapter *adap, unsigned int viid, const u8 *addr, const u8 *mask, unsigned int vni, unsigned int vni_mask, u8 dip_hit, u8 lookup_type, bool sleep_ok)

    Adds a mac entry in mps tcam with VNI support

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param viid:
        the VI id
    :type viid: unsigned int

    :param addr:
        *undescribed*
    :type addr: const u8 \*

    :param mask:
        the mask
    :type mask: const u8 \*

    :param vni:
        the VNI id for the tunnel protocol
    :type vni: unsigned int

    :param vni_mask:
        mask for the VNI id
    :type vni_mask: unsigned int

    :param dip_hit:
        to enable DIP match for the MPS entry
    :type dip_hit: u8

    :param lookup_type:
        MAC address for inner (1) or outer (0) header
    :type lookup_type: u8

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

.. _`t4_alloc_encap_mac_filt.description`:

Description
-----------

Allocates an MPS entry with specified MAC address and VNI value.

Returns a negative error number or the allocated index for this mac.

.. _`t4_alloc_raw_mac_filt`:

t4_alloc_raw_mac_filt
=====================

.. c:function:: int t4_alloc_raw_mac_filt(struct adapter *adap, unsigned int viid, const u8 *addr, const u8 *mask, unsigned int idx, u8 lookup_type, u8 port_id, bool sleep_ok)

    Adds a mac entry in mps tcam

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param viid:
        the VI id
    :type viid: unsigned int

    :param addr:
        *undescribed*
    :type addr: const u8 \*

    :param mask:
        the mask
    :type mask: const u8 \*

    :param idx:
        index at which to add this entry
    :type idx: unsigned int

    :param lookup_type:
        MAC address for inner (1) or outer (0) header
    :type lookup_type: u8

    :param port_id:
        the port index
    :type port_id: u8

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

.. _`t4_alloc_raw_mac_filt.description`:

Description
-----------

Adds the mac entry at the specified index using raw mac interface.

Returns a negative error number or the allocated index for this mac.

.. _`t4_alloc_mac_filt`:

t4_alloc_mac_filt
=================

.. c:function:: int t4_alloc_mac_filt(struct adapter *adap, unsigned int mbox, unsigned int viid, bool free, unsigned int naddr, const u8 **addr, u16 *idx, u64 *hash, bool sleep_ok)

    allocates exact-match filters for MAC addresses

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param viid:
        the VI id
    :type viid: unsigned int

    :param free:
        if true any existing filters for this VI id are first removed
    :type free: bool

    :param naddr:
        the number of MAC addresses to allocate filters for (up to 7)
    :type naddr: unsigned int

    :param addr:
        the MAC address(es)
    :type addr: const u8 \*\*

    :param idx:
        where to store the index of each allocated filter
    :type idx: u16 \*

    :param hash:
        pointer to hash address filter bitmap
    :type hash: u64 \*

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param viid:
        the VI id
    :type viid: unsigned int

    :param naddr:
        the number of MAC addresses to allocate filters for (up to 7)
    :type naddr: unsigned int

    :param addr:
        the MAC address(es)
    :type addr: const u8 \*\*

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param viid:
        the VI id
    :type viid: unsigned int

    :param idx:
        index of existing filter for old value of MAC address, or -1
    :type idx: int

    :param addr:
        the new MAC address value
    :type addr: const u8 \*

    :param persist:
        whether a new MAC allocation should be persistent
    :type persist: bool

    :param add_smt:
        if true also add the address to the HW SMT
    :type add_smt: bool

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param viid:
        the VI id
    :type viid: unsigned int

    :param ucast:
        whether the hash filter should also match unicast addresses
    :type ucast: bool

    :param vec:
        the value to be written to the hash filter
    :type vec: u64

    :param sleep_ok:
        call is allowed to sleep
    :type sleep_ok: bool

.. _`t4_set_addr_hash.description`:

Description
-----------

Sets the 64-bit inexact-match hash filter for a virtual interface.

.. _`t4_enable_vi_params`:

t4_enable_vi_params
===================

.. c:function:: int t4_enable_vi_params(struct adapter *adap, unsigned int mbox, unsigned int viid, bool rx_en, bool tx_en, bool dcb_en)

    enable/disable a virtual interface

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param viid:
        the VI id
    :type viid: unsigned int

    :param rx_en:
        1=enable Rx, 0=disable Rx
    :type rx_en: bool

    :param tx_en:
        1=enable Tx, 0=disable Tx
    :type tx_en: bool

    :param dcb_en:
        1=enable delivery of Data Center Bridging messages.
    :type dcb_en: bool

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param viid:
        the VI id
    :type viid: unsigned int

    :param rx_en:
        1=enable Rx, 0=disable Rx
    :type rx_en: bool

    :param tx_en:
        1=enable Tx, 0=disable Tx
    :type tx_en: bool

.. _`t4_enable_vi.description`:

Description
-----------

Enables/disables a virtual interface.

.. _`t4_enable_pi_params`:

t4_enable_pi_params
===================

.. c:function:: int t4_enable_pi_params(struct adapter *adap, unsigned int mbox, struct port_info *pi, bool rx_en, bool tx_en, bool dcb_en)

    enable/disable a Port's Virtual Interface

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pi:
        the Port Information structure
    :type pi: struct port_info \*

    :param rx_en:
        1=enable Rx, 0=disable Rx
    :type rx_en: bool

    :param tx_en:
        1=enable Tx, 0=disable Tx
    :type tx_en: bool

    :param dcb_en:
        1=enable delivery of Data Center Bridging messages.
    :type dcb_en: bool

.. _`t4_enable_pi_params.description`:

Description
-----------

Enables/disables a Port's Virtual Interface.  Note that setting DCB
Enable only makes sense when enabling a Virtual Interface ...
If the Virtual Interface enable/disable operation is successful,
we notify the OS-specific code of a potential Link Status change
via the OS Contract API \ :c:func:`t4_os_link_changed`\ .

.. _`t4_identify_port`:

t4_identify_port
================

.. c:function:: int t4_identify_port(struct adapter *adap, unsigned int mbox, unsigned int viid, unsigned int nblinks)

    identify a VI's port by blinking its LED

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param viid:
        the VI id
    :type viid: unsigned int

    :param nblinks:
        how many times to blink LED at 2.5 Hz
    :type nblinks: unsigned int

.. _`t4_identify_port.description`:

Description
-----------

Identifies a VI's port by blinking its LED.

.. _`t4_iq_stop`:

t4_iq_stop
==========

.. c:function:: int t4_iq_stop(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int iqtype, unsigned int iqid, unsigned int fl0id, unsigned int fl1id)

    stop an ingress queue and its FLs

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF owning the queues
    :type pf: unsigned int

    :param vf:
        the VF owning the queues
    :type vf: unsigned int

    :param iqtype:
        the ingress queue type (FW_IQ_TYPE_FL_INT_CAP, etc.)
    :type iqtype: unsigned int

    :param iqid:
        ingress queue id
    :type iqid: unsigned int

    :param fl0id:
        FL0 queue id or 0xffff if no attached FL0
    :type fl0id: unsigned int

    :param fl1id:
        FL1 queue id or 0xffff if no attached FL1
    :type fl1id: unsigned int

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF owning the queues
    :type pf: unsigned int

    :param vf:
        the VF owning the queues
    :type vf: unsigned int

    :param iqtype:
        the ingress queue type
    :type iqtype: unsigned int

    :param iqid:
        ingress queue id
    :type iqid: unsigned int

    :param fl0id:
        FL0 queue id or 0xffff if no attached FL0
    :type fl0id: unsigned int

    :param fl1id:
        FL1 queue id or 0xffff if no attached FL1
    :type fl1id: unsigned int

.. _`t4_iq_free.description`:

Description
-----------

Frees an ingress queue and its associated FLs, if any.

.. _`t4_eth_eq_free`:

t4_eth_eq_free
==============

.. c:function:: int t4_eth_eq_free(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int eqid)

    free an Ethernet egress queue

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF owning the queue
    :type pf: unsigned int

    :param vf:
        the VF owning the queue
    :type vf: unsigned int

    :param eqid:
        egress queue id
    :type eqid: unsigned int

.. _`t4_eth_eq_free.description`:

Description
-----------

Frees an Ethernet egress queue.

.. _`t4_ctrl_eq_free`:

t4_ctrl_eq_free
===============

.. c:function:: int t4_ctrl_eq_free(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int eqid)

    free a control egress queue

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF owning the queue
    :type pf: unsigned int

    :param vf:
        the VF owning the queue
    :type vf: unsigned int

    :param eqid:
        egress queue id
    :type eqid: unsigned int

.. _`t4_ctrl_eq_free.description`:

Description
-----------

Frees a control egress queue.

.. _`t4_ofld_eq_free`:

t4_ofld_eq_free
===============

.. c:function:: int t4_ofld_eq_free(struct adapter *adap, unsigned int mbox, unsigned int pf, unsigned int vf, unsigned int eqid)

    free an offload egress queue

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param pf:
        the PF owning the queue
    :type pf: unsigned int

    :param vf:
        the VF owning the queue
    :type vf: unsigned int

    :param eqid:
        egress queue id
    :type eqid: unsigned int

.. _`t4_ofld_eq_free.description`:

Description
-----------

Frees a control egress queue.

.. _`t4_link_down_rc_str`:

t4_link_down_rc_str
===================

.. c:function:: const char *t4_link_down_rc_str(unsigned char link_down_rc)

    return a string for a Link Down Reason Code

    :param link_down_rc:
        Link Down Reason Code
    :type link_down_rc: unsigned char

.. _`t4_link_down_rc_str.description`:

Description
-----------

Returns a string representation of the Link Down Reason Code.

.. _`fwcap_to_speed`:

fwcap_to_speed
==============

.. c:function:: unsigned int fwcap_to_speed(fw_port_cap32_t caps)

    :param caps:
        *undescribed*
    :type caps: fw_port_cap32_t

.. _`fwcap_to_fwspeed`:

fwcap_to_fwspeed
================

.. c:function:: fw_port_cap32_t fwcap_to_fwspeed(fw_port_cap32_t acaps)

    return highest speed in Port Capabilities

    :param acaps:
        advertised Port Capabilities
    :type acaps: fw_port_cap32_t

.. _`fwcap_to_fwspeed.description`:

Description
-----------

Get the highest speed for the port from the advertised Port
Capabilities.  It will be either the highest speed from the list of
speeds or whatever user has set using ethtool.

.. _`lstatus_to_fwcap`:

lstatus_to_fwcap
================

.. c:function:: fw_port_cap32_t lstatus_to_fwcap(u32 lstatus)

    translate old lstatus to 32-bit Port Capabilities

    :param lstatus:
        old FW_PORT_ACTION_GET_PORT_INFO lstatus value
    :type lstatus: u32

.. _`lstatus_to_fwcap.description`:

Description
-----------

Translates old FW_PORT_ACTION_GET_PORT_INFO lstatus field into new
32-bit Port Capabilities value.

.. _`t4_handle_get_port_info`:

t4_handle_get_port_info
=======================

.. c:function:: void t4_handle_get_port_info(struct port_info *pi, const __be64 *rpl)

    process a FW reply message

    :param pi:
        the port info
    :type pi: struct port_info \*

    :param rpl:
        start of the FW message
    :type rpl: const __be64 \*

.. _`t4_handle_get_port_info.description`:

Description
-----------

Processes a GET_PORT_INFO FW reply message.

.. _`t4_update_port_info`:

t4_update_port_info
===================

.. c:function:: int t4_update_port_info(struct port_info *pi)

    retrieve and update port information if changed

    :param pi:
        the port_info
    :type pi: struct port_info \*

.. _`t4_update_port_info.description`:

Description
-----------

We issue a Get Port Information Command to the Firmware and, if
successful, we check to see if anything is different from what we
last recorded and update things accordingly.

.. _`t4_get_link_params`:

t4_get_link_params
==================

.. c:function:: int t4_get_link_params(struct port_info *pi, unsigned int *link_okp, unsigned int *speedp, unsigned int *mtup)

    retrieve basic link parameters for given port

    :param pi:
        the port
    :type pi: struct port_info \*

    :param link_okp:
        value return pointer for link up/down
    :type link_okp: unsigned int \*

    :param speedp:
        value return pointer for speed (Mb/s)
    :type speedp: unsigned int \*

    :param mtup:
        value return pointer for mtu
    :type mtup: unsigned int \*

.. _`t4_get_link_params.retrieves-basic-link-parameters-for-a-port`:

Retrieves basic link parameters for a port
------------------------------------------

link up/down, speed (Mb/s),
and MTU for a specified port.  A negative error is returned on
failure; 0 on success.

.. _`t4_handle_fw_rpl`:

t4_handle_fw_rpl
================

.. c:function:: int t4_handle_fw_rpl(struct adapter *adap, const __be64 *rpl)

    process a FW reply message

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param rpl:
        start of the FW message
    :type rpl: const __be64 \*

.. _`t4_handle_fw_rpl.description`:

Description
-----------

Processes a FW message, such as link state change messages.

.. _`init_link_config`:

init_link_config
================

.. c:function:: void init_link_config(struct link_config *lc, fw_port_cap32_t pcaps, fw_port_cap32_t acaps)

    initialize a link's SW state

    :param lc:
        pointer to structure holding the link state
    :type lc: struct link_config \*

    :param pcaps:
        link Port Capabilities
    :type pcaps: fw_port_cap32_t

    :param acaps:
        link current Advertised Port Capabilities
    :type acaps: fw_port_cap32_t

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4_prep_adapter.description`:

Description
-----------

Initialize adapter SW state for the various HW modules, set initial
values for some adapter tunables, take PHYs out of reset, and
initialize the MDIO interface.

.. _`t4_shutdown_adapter`:

t4_shutdown_adapter
===================

.. c:function:: int t4_shutdown_adapter(struct adapter *adapter)

    shut down adapter, host & wire

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4_shutdown_adapter.description`:

Description
-----------

Perform an emergency shutdown of the adapter and stop it from
continuing any further communication on the ports or DMA to the
host.  This is typically used when the adapter and/or firmware
have crashed and we want to prevent any further accidental
communication with the rest of the world.  This will also force
the port Link Status to go down -- if register writes work --
which should help our peers figure out that we're down.

.. _`t4_bar2_sge_qregs`:

t4_bar2_sge_qregs
=================

.. c:function:: int t4_bar2_sge_qregs(struct adapter *adapter, unsigned int qid, enum t4_bar2_qtype qtype, int user, u64 *pbar2_qoffset, unsigned int *pbar2_qid)

    return BAR2 SGE Queue register information

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param qid:
        the Queue ID
    :type qid: unsigned int

    :param qtype:
        the Ingress or Egress type for \ ``qid``\ 
    :type qtype: enum t4_bar2_qtype

    :param user:
        true if this request is for a user mode queue
    :type user: int

    :param pbar2_qoffset:
        BAR2 Queue Offset
    :type pbar2_qoffset: u64 \*

    :param pbar2_qid:
        BAR2 Queue ID or 0 for Queue ID inferred SGE Queues
    :type pbar2_qid: unsigned int \*

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


\*@pbar2_qoffset: the BAR2 Offset of the \ ``qid``\  Registers
\*@pbar2_qid: the BAR2 SGE Queue ID or 0 of \ ``qid``\ 

If the returned BAR2 Queue ID is 0, then BAR2 SGE registers which
require the "Inferred Queue ID" ability may be used.  E.g. the
Write Combining Doorbell Buffer. If the BAR2 Queue ID is not 0,
then these "Inferred Queue ID" register may not be used.

.. _`t4_init_devlog_params`:

t4_init_devlog_params
=====================

.. c:function:: int t4_init_devlog_params(struct adapter *adap)

    initialize adapter->params.devlog

    :param adap:
        the adapter
    :type adap: struct adapter \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

.. _`t4_init_sge_params.description`:

Description
-----------

Initialize various fields of the adapter's SGE Parameters structure.

.. _`t4_init_tp_params`:

t4_init_tp_params
=================

.. c:function:: int t4_init_tp_params(struct adapter *adap, bool sleep_ok)

    initialize adap->params.tp

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_init_tp_params.description`:

Description
-----------

Initialize various fields of the adapter's TP Parameters structure.

.. _`t4_filter_field_shift`:

t4_filter_field_shift
=====================

.. c:function:: int t4_filter_field_shift(const struct adapter *adap, int filter_sel)

    calculate filter field shift

    :param adap:
        the adapter
    :type adap: const struct adapter \*

    :param filter_sel:
        the desired field (from TP_VLAN_PRI_MAP bits)
    :type filter_sel: int

.. _`t4_filter_field_shift.description`:

Description
-----------

Return the shift position of a filter field within the Compressed
Filter Tuple.  The filter field is specified via its selection bit
within TP_VLAN_PRI_MAL (filter mode).  E.g. F_VLAN.

.. _`t4_init_portinfo`:

t4_init_portinfo
================

.. c:function:: int t4_init_portinfo(struct port_info *pi, int mbox, int port, int pf, int vf, u8 mac)

    allocate a virtual interface and initialize port_info

    :param pi:
        the port_info
    :type pi: struct port_info \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: int

    :param port:
        physical port associated with the VI
    :type port: int

    :param pf:
        the PF owning the VI
    :type pf: int

    :param vf:
        the VF owning the VI
    :type vf: int

    :param mac:
        the MAC address of the VI
    :type mac: u8

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param base:
        holds the queue base addresses in bytes
    :type base: u16 \*

    :param size:
        holds the queue sizes in bytes
    :type size: u16 \*

    :param thres:
        holds the queue full thresholds in bytes
    :type thres: u16 \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param qid:
        the queue index
    :type qid: unsigned int

    :param data:
        where to store the queue contents
    :type data: u32 \*

    :param n:
        capacity of \ ``data``\  in 32-bit words
    :type n: size_t

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param qid:
        the queue index
    :type qid: unsigned int

    :param data:
        where to store the queue contents
    :type data: u32 \*

    :param n:
        capacity of \ ``data``\  in 32-bit words
    :type n: size_t

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param addr:
        the start address within the CIM address space
    :type addr: unsigned int

    :param n:
        number of words to read
    :type n: unsigned int

    :param valp:
        where to store the result
    :type valp: unsigned int \*

.. _`t4_cim_read.description`:

Description
-----------

Reads a block of 4-byte words from the CIM intenal address space.

.. _`t4_cim_write`:

t4_cim_write
============

.. c:function:: int t4_cim_write(struct adapter *adap, unsigned int addr, unsigned int n, const unsigned int *valp)

    write a block into CIM internal address space

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param addr:
        the start address within the CIM address space
    :type addr: unsigned int

    :param n:
        number of words to write
    :type n: unsigned int

    :param valp:
        set of values to write
    :type valp: const unsigned int \*

.. _`t4_cim_write.description`:

Description
-----------

Writes a block of 4-byte words into the CIM intenal address space.

.. _`t4_cim_read_la`:

t4_cim_read_la
==============

.. c:function:: int t4_cim_read_la(struct adapter *adap, u32 *la_buf, unsigned int *wrptr)

    read CIM LA capture buffer

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param la_buf:
        where to store the LA data
    :type la_buf: u32 \*

    :param wrptr:
        the HW write pointer within the capture buffer
    :type wrptr: unsigned int \*

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

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param la_buf:
        where to store the LA data
    :type la_buf: u64 \*

    :param wrptr:
        the HW write pointer within the capture buffer
    :type wrptr: unsigned int \*

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

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param idma:
        the adapter IDMA Monitor state
    :type idma: struct sge_idma_monitor_state \*

.. _`t4_idma_monitor_init.description`:

Description
-----------

Initialize the state of an SGE Ingress DMA Monitor.

.. _`t4_idma_monitor`:

t4_idma_monitor
===============

.. c:function:: void t4_idma_monitor(struct adapter *adapter, struct sge_idma_monitor_state *idma, int hz, int ticks)

    monitor SGE Ingress DMA state

    :param adapter:
        the adapter
    :type adapter: struct adapter \*

    :param idma:
        the adapter IDMA Monitor state
    :type idma: struct sge_idma_monitor_state \*

    :param hz:
        number of ticks/second
    :type hz: int

    :param ticks:
        number of ticks since the last IDMA Monitor call
    :type ticks: int

.. _`t4_load_cfg`:

t4_load_cfg
===========

.. c:function:: int t4_load_cfg(struct adapter *adap, const u8 *cfg_data, unsigned int size)

    download config file

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param cfg_data:
        the cfg text file to write
    :type cfg_data: const u8 \*

    :param size:
        text file size
    :type size: unsigned int

.. _`t4_load_cfg.description`:

Description
-----------

Write the supplied config text file to the card's serial flash.

.. _`t4_set_vf_mac_acl`:

t4_set_vf_mac_acl
=================

.. c:function:: int t4_set_vf_mac_acl(struct adapter *adapter, unsigned int vf, unsigned int naddr, u8 *addr)

    Set MAC address for the specified VF

    :param adapter:
        The adapter
    :type adapter: struct adapter \*

    :param vf:
        one of the VFs instantiated by the specified PF
    :type vf: unsigned int

    :param naddr:
        the number of MAC addresses
    :type naddr: unsigned int

    :param addr:
        the MAC address(es) to be set to the specified VF
    :type addr: u8 \*

.. _`t4_read_pace_tbl`:

t4_read_pace_tbl
================

.. c:function:: void t4_read_pace_tbl(struct adapter *adap, unsigned int pace_vals)

    read the pace table

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param pace_vals:
        holds the returned values
    :type pace_vals: unsigned int

.. _`t4_read_pace_tbl.description`:

Description
-----------

Returns the values of TP's pace table in microseconds.

.. _`t4_get_tx_sched`:

t4_get_tx_sched
===============

.. c:function:: void t4_get_tx_sched(struct adapter *adap, unsigned int sched, unsigned int *kbps, unsigned int *ipg, bool sleep_ok)

    get the configuration of a Tx HW traffic scheduler

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param sched:
        the scheduler index
    :type sched: unsigned int

    :param kbps:
        the byte rate in Kbps
    :type kbps: unsigned int \*

    :param ipg:
        the interpacket delay in tenths of nanoseconds
    :type ipg: unsigned int \*

    :param sleep_ok:
        if true we may sleep while awaiting command completion
    :type sleep_ok: bool

.. _`t4_get_tx_sched.description`:

Description
-----------

Return the current configuration of a HW Tx scheduler.

.. _`t4_sge_ctxt_rd_bd`:

t4_sge_ctxt_rd_bd
=================

.. c:function:: int t4_sge_ctxt_rd_bd(struct adapter *adap, unsigned int cid, enum ctxt_type ctype, u32 *data)

    read an SGE context bypassing FW

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param cid:
        the context id
    :type cid: unsigned int

    :param ctype:
        the context type
    :type ctype: enum ctxt_type

    :param data:
        where to store the context data
    :type data: u32 \*

.. _`t4_sge_ctxt_rd_bd.description`:

Description
-----------

Reads an SGE context directly, bypassing FW.  This is only for
debugging when FW is unavailable.

.. _`t4_i2c_rd`:

t4_i2c_rd
=========

.. c:function:: int t4_i2c_rd(struct adapter *adap, unsigned int mbox, int port, unsigned int devid, unsigned int offset, unsigned int len, u8 *buf)

    read I2C data from adapter

    :param adap:
        the adapter
    :type adap: struct adapter \*

    :param mbox:
        *undescribed*
    :type mbox: unsigned int

    :param port:
        Port number if per-port device; <0 if not
    :type port: int

    :param devid:
        per-port device ID or absolute device ID
    :type devid: unsigned int

    :param offset:
        byte offset into device I2C space
    :type offset: unsigned int

    :param len:
        byte length of I2C space data
    :type len: unsigned int

    :param buf:
        buffer in which to return I2C data
    :type buf: u8 \*

.. _`t4_i2c_rd.description`:

Description
-----------

Reads the I2C data from the indicated device and location.

.. _`t4_set_vlan_acl`:

t4_set_vlan_acl
===============

.. c:function:: int t4_set_vlan_acl(struct adapter *adap, unsigned int mbox, unsigned int vf, u16 vlan)

    Set a VLAN id for the specified VF

    :param adap:
        *undescribed*
    :type adap: struct adapter \*

    :param mbox:
        mailbox to use for the FW command
    :type mbox: unsigned int

    :param vf:
        one of the VFs instantiated by the specified PF
    :type vf: unsigned int

    :param vlan:
        The vlanid to be set
    :type vlan: u16

.. This file was automatic generated / don't edit.

