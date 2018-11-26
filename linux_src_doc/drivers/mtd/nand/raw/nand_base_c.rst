.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/nand_base.c

.. _`nand_release_device`:

nand_release_device
===================

.. c:function:: void nand_release_device(struct mtd_info *mtd)

    [GENERIC] release chip

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

.. _`nand_release_device.description`:

Description
-----------

Release chip lock and wake up anyone waiting on the device.

.. _`nand_block_bad`:

nand_block_bad
==============

.. c:function:: int nand_block_bad(struct nand_chip *chip, loff_t ofs)

    [DEFAULT] Read bad block marker from the chip

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param ofs:
        offset from device start
    :type ofs: loff_t

.. _`nand_block_bad.description`:

Description
-----------

Check, if the block is bad.

.. _`nand_default_block_markbad`:

nand_default_block_markbad
==========================

.. c:function:: int nand_default_block_markbad(struct nand_chip *chip, loff_t ofs)

    [DEFAULT] mark a block bad via bad block marker

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param ofs:
        offset from device start
    :type ofs: loff_t

.. _`nand_default_block_markbad.description`:

Description
-----------

This is the default implementation, which can be overridden by a hardware
specific driver. It provides the details for writing a bad block marker to a
block.

.. _`nand_markbad_bbm`:

nand_markbad_bbm
================

.. c:function:: int nand_markbad_bbm(struct nand_chip *chip, loff_t ofs)

    mark a block by updating the BBM

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param ofs:
        offset of the block to mark bad
    :type ofs: loff_t

.. _`nand_block_markbad_lowlevel`:

nand_block_markbad_lowlevel
===========================

.. c:function:: int nand_block_markbad_lowlevel(struct mtd_info *mtd, loff_t ofs)

    mark a block bad

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param ofs:
        offset from device start
    :type ofs: loff_t

.. _`nand_block_markbad_lowlevel.description`:

Description
-----------

This function performs the generic NAND bad block marking steps (i.e., bad
block table(s) and/or marker(s)). We only allow the hardware driver to
specify how to write bad block markers to OOB (chip->legacy.block_markbad).

.. _`nand_block_markbad_lowlevel.we-try-operations-in-the-following-order`:

We try operations in the following order
----------------------------------------


 (1) erase the affected block, to allow OOB marker to be written cleanly
 (2) write bad block marker to OOB area of affected block (unless flag
     NAND_BBT_NO_OOB_BBM is present)
 (3) update the BBT

Note that we retain the first error encountered in (2) or (3), finish the
procedures, and dump the error in the end.

.. _`nand_check_wp`:

nand_check_wp
=============

.. c:function:: int nand_check_wp(struct mtd_info *mtd)

    [GENERIC] check if the chip is write protected

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

.. _`nand_check_wp.description`:

Description
-----------

Check, if the device is write protected. The function expects, that the
device is already selected.

.. _`nand_block_isreserved`:

nand_block_isreserved
=====================

.. c:function:: int nand_block_isreserved(struct mtd_info *mtd, loff_t ofs)

    [GENERIC] Check if a block is marked reserved.

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param ofs:
        offset from device start
    :type ofs: loff_t

.. _`nand_block_isreserved.description`:

Description
-----------

Check if the block is marked as reserved.

.. _`nand_block_checkbad`:

nand_block_checkbad
===================

.. c:function:: int nand_block_checkbad(struct mtd_info *mtd, loff_t ofs, int allowbbt)

    [GENERIC] Check if a block is marked bad

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param ofs:
        offset from device start
    :type ofs: loff_t

    :param allowbbt:
        1, if its allowed to access the bbt area
    :type allowbbt: int

.. _`nand_block_checkbad.description`:

Description
-----------

Check, if the block is bad. Either by reading the bad block table or
calling of the scan function.

.. _`nand_soft_waitrdy`:

nand_soft_waitrdy
=================

.. c:function:: int nand_soft_waitrdy(struct nand_chip *chip, unsigned long timeout_ms)

    Poll STATUS reg until RDY bit is set to 1

    :param chip:
        NAND chip structure
    :type chip: struct nand_chip \*

    :param timeout_ms:
        Timeout in ms
    :type timeout_ms: unsigned long

.. _`nand_soft_waitrdy.description`:

Description
-----------

Poll the STATUS register using ->exec_op() until the RDY bit becomes 1.
If that does not happen whitin the specified timeout, -ETIMEDOUT is
returned.

This helper is intended to be used when the controller does not have access
to the NAND R/B pin.

Be aware that calling this helper from an ->exec_op() implementation means
->exec_op() must be re-entrant.

Return 0 if the NAND chip is ready, a negative error otherwise.

.. _`panic_nand_get_device`:

panic_nand_get_device
=====================

.. c:function:: void panic_nand_get_device(struct nand_chip *chip, struct mtd_info *mtd, int new_state)

    [GENERIC] Get chip for selected access

    :param chip:
        the nand chip descriptor
    :type chip: struct nand_chip \*

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param new_state:
        the state which is requested
    :type new_state: int

.. _`panic_nand_get_device.description`:

Description
-----------

Used when in panic, no locks are taken.

.. _`nand_get_device`:

nand_get_device
===============

.. c:function:: int nand_get_device(struct mtd_info *mtd, int new_state)

    [GENERIC] Get chip for selected access

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param new_state:
        the state which is requested
    :type new_state: int

.. _`nand_get_device.description`:

Description
-----------

Get the device and lock it for exclusive access

.. _`panic_nand_wait`:

panic_nand_wait
===============

.. c:function:: void panic_nand_wait(struct nand_chip *chip, unsigned long timeo)

    [GENERIC] wait until the command is done

    :param chip:
        NAND chip structure
    :type chip: struct nand_chip \*

    :param timeo:
        timeout
    :type timeo: unsigned long

.. _`panic_nand_wait.description`:

Description
-----------

Wait for command done. This is a helper function for nand_wait used when
we are in interrupt context. May happen when in panic and trying to write
an oops through mtdoops.

.. _`nand_reset_data_interface`:

nand_reset_data_interface
=========================

.. c:function:: int nand_reset_data_interface(struct nand_chip *chip, int chipnr)

    Reset data interface and timings

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param chipnr:
        Internal die id
    :type chipnr: int

.. _`nand_reset_data_interface.description`:

Description
-----------

Reset the Data interface and timings to ONFI mode 0.

Returns 0 for success or negative error code otherwise.

.. _`nand_setup_data_interface`:

nand_setup_data_interface
=========================

.. c:function:: int nand_setup_data_interface(struct nand_chip *chip, int chipnr)

    Setup the best data interface and timings

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param chipnr:
        Internal die id
    :type chipnr: int

.. _`nand_setup_data_interface.description`:

Description
-----------

Find and configure the best data interface and NAND timings supported by
the chip and the driver.
First tries to retrieve supported timing modes from ONFI information,
and if the NAND chip does not support ONFI, relies on the
->onfi_timing_mode_default specified in the nand_ids table.

Returns 0 for success or negative error code otherwise.

.. _`nand_init_data_interface`:

nand_init_data_interface
========================

.. c:function:: int nand_init_data_interface(struct nand_chip *chip)

    find the best data interface and timings

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

.. _`nand_init_data_interface.description`:

Description
-----------

Find the best data interface and NAND timings supported by the chip
and the driver.
First tries to retrieve supported timing modes from ONFI information,
and if the NAND chip does not support ONFI, relies on the
->onfi_timing_mode_default specified in the nand_ids table. After this
function nand_chip->data_interface is initialized with the best timing mode
available.

Returns 0 for success or negative error code otherwise.

.. _`nand_fill_column_cycles`:

nand_fill_column_cycles
=======================

.. c:function:: int nand_fill_column_cycles(struct nand_chip *chip, u8 *addrs, unsigned int offset_in_page)

    fill the column cycles of an address

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param addrs:
        Array of address cycles to fill
    :type addrs: u8 \*

    :param offset_in_page:
        The offset in the page
    :type offset_in_page: unsigned int

.. _`nand_fill_column_cycles.description`:

Description
-----------

Fills the first or the first two bytes of the \ ``addrs``\  field depending
on the NAND bus width and the page size.

Returns the number of cycles needed to encode the column, or a negative
error code in case one of the arguments is invalid.

.. _`nand_read_page_op`:

nand_read_page_op
=================

.. c:function:: int nand_read_page_op(struct nand_chip *chip, unsigned int page, unsigned int offset_in_page, void *buf, unsigned int len)

    Do a READ PAGE operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param page:
        page to read
    :type page: unsigned int

    :param offset_in_page:
        offset within the page
    :type offset_in_page: unsigned int

    :param buf:
        buffer used to store the data
    :type buf: void \*

    :param len:
        length of the buffer
    :type len: unsigned int

.. _`nand_read_page_op.description`:

Description
-----------

This function issues a READ PAGE operation.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_read_param_page_op`:

nand_read_param_page_op
=======================

.. c:function:: int nand_read_param_page_op(struct nand_chip *chip, u8 page, void *buf, unsigned int len)

    Do a READ PARAMETER PAGE operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param page:
        parameter page to read
    :type page: u8

    :param buf:
        buffer used to store the data
    :type buf: void \*

    :param len:
        length of the buffer
    :type len: unsigned int

.. _`nand_read_param_page_op.description`:

Description
-----------

This function issues a READ PARAMETER PAGE operation.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_change_read_column_op`:

nand_change_read_column_op
==========================

.. c:function:: int nand_change_read_column_op(struct nand_chip *chip, unsigned int offset_in_page, void *buf, unsigned int len, bool force_8bit)

    Do a CHANGE READ COLUMN operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param offset_in_page:
        offset within the page
    :type offset_in_page: unsigned int

    :param buf:
        buffer used to store the data
    :type buf: void \*

    :param len:
        length of the buffer
    :type len: unsigned int

    :param force_8bit:
        force 8-bit bus access
    :type force_8bit: bool

.. _`nand_change_read_column_op.description`:

Description
-----------

This function issues a CHANGE READ COLUMN operation.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_read_oob_op`:

nand_read_oob_op
================

.. c:function:: int nand_read_oob_op(struct nand_chip *chip, unsigned int page, unsigned int offset_in_oob, void *buf, unsigned int len)

    Do a READ OOB operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param page:
        page to read
    :type page: unsigned int

    :param offset_in_oob:
        offset within the OOB area
    :type offset_in_oob: unsigned int

    :param buf:
        buffer used to store the data
    :type buf: void \*

    :param len:
        length of the buffer
    :type len: unsigned int

.. _`nand_read_oob_op.description`:

Description
-----------

This function issues a READ OOB operation.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_prog_page_begin_op`:

nand_prog_page_begin_op
=======================

.. c:function:: int nand_prog_page_begin_op(struct nand_chip *chip, unsigned int page, unsigned int offset_in_page, const void *buf, unsigned int len)

    starts a PROG PAGE operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param page:
        page to write
    :type page: unsigned int

    :param offset_in_page:
        offset within the page
    :type offset_in_page: unsigned int

    :param buf:
        buffer containing the data to write to the page
    :type buf: const void \*

    :param len:
        length of the buffer
    :type len: unsigned int

.. _`nand_prog_page_begin_op.description`:

Description
-----------

This function issues the first half of a PROG PAGE operation.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_prog_page_end_op`:

nand_prog_page_end_op
=====================

.. c:function:: int nand_prog_page_end_op(struct nand_chip *chip)

    ends a PROG PAGE operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

.. _`nand_prog_page_end_op.description`:

Description
-----------

This function issues the second half of a PROG PAGE operation.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_prog_page_op`:

nand_prog_page_op
=================

.. c:function:: int nand_prog_page_op(struct nand_chip *chip, unsigned int page, unsigned int offset_in_page, const void *buf, unsigned int len)

    Do a full PROG PAGE operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param page:
        page to write
    :type page: unsigned int

    :param offset_in_page:
        offset within the page
    :type offset_in_page: unsigned int

    :param buf:
        buffer containing the data to write to the page
    :type buf: const void \*

    :param len:
        length of the buffer
    :type len: unsigned int

.. _`nand_prog_page_op.description`:

Description
-----------

This function issues a full PROG PAGE operation.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_change_write_column_op`:

nand_change_write_column_op
===========================

.. c:function:: int nand_change_write_column_op(struct nand_chip *chip, unsigned int offset_in_page, const void *buf, unsigned int len, bool force_8bit)

    Do a CHANGE WRITE COLUMN operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param offset_in_page:
        offset within the page
    :type offset_in_page: unsigned int

    :param buf:
        buffer containing the data to send to the NAND
    :type buf: const void \*

    :param len:
        length of the buffer
    :type len: unsigned int

    :param force_8bit:
        force 8-bit bus access
    :type force_8bit: bool

.. _`nand_change_write_column_op.description`:

Description
-----------

This function issues a CHANGE WRITE COLUMN operation.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_readid_op`:

nand_readid_op
==============

.. c:function:: int nand_readid_op(struct nand_chip *chip, u8 addr, void *buf, unsigned int len)

    Do a READID operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param addr:
        address cycle to pass after the READID command
    :type addr: u8

    :param buf:
        buffer used to store the ID
    :type buf: void \*

    :param len:
        length of the buffer
    :type len: unsigned int

.. _`nand_readid_op.description`:

Description
-----------

This function sends a READID command and reads back the ID returned by the
NAND.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_status_op`:

nand_status_op
==============

.. c:function:: int nand_status_op(struct nand_chip *chip, u8 *status)

    Do a STATUS operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param status:
        out variable to store the NAND status
    :type status: u8 \*

.. _`nand_status_op.description`:

Description
-----------

This function sends a STATUS command and reads back the status returned by
the NAND.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_exit_status_op`:

nand_exit_status_op
===================

.. c:function:: int nand_exit_status_op(struct nand_chip *chip)

    Exit a STATUS operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

.. _`nand_exit_status_op.description`:

Description
-----------

This function sends a READ0 command to cancel the effect of the STATUS
command to avoid reading only the status until a new read command is sent.

This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_erase_op`:

nand_erase_op
=============

.. c:function:: int nand_erase_op(struct nand_chip *chip, unsigned int eraseblock)

    Do an erase operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param eraseblock:
        block to erase
    :type eraseblock: unsigned int

.. _`nand_erase_op.description`:

Description
-----------

This function sends an ERASE command and waits for the NAND to be ready
before returning.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_set_features_op`:

nand_set_features_op
====================

.. c:function:: int nand_set_features_op(struct nand_chip *chip, u8 feature, const void *data)

    Do a SET FEATURES operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param feature:
        feature id
    :type feature: u8

    :param data:
        4 bytes of data
    :type data: const void \*

.. _`nand_set_features_op.description`:

Description
-----------

This function sends a SET FEATURES command and waits for the NAND to be
ready before returning.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_get_features_op`:

nand_get_features_op
====================

.. c:function:: int nand_get_features_op(struct nand_chip *chip, u8 feature, void *data)

    Do a GET FEATURES operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param feature:
        feature id
    :type feature: u8

    :param data:
        4 bytes of data
    :type data: void \*

.. _`nand_get_features_op.description`:

Description
-----------

This function sends a GET FEATURES command and waits for the NAND to be
ready before returning.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_reset_op`:

nand_reset_op
=============

.. c:function:: int nand_reset_op(struct nand_chip *chip)

    Do a reset operation

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

.. _`nand_reset_op.description`:

Description
-----------

This function sends a RESET command and waits for the NAND to be ready
before returning.
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_read_data_op`:

nand_read_data_op
=================

.. c:function:: int nand_read_data_op(struct nand_chip *chip, void *buf, unsigned int len, bool force_8bit)

    Read data from the NAND

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param buf:
        buffer used to store the data
    :type buf: void \*

    :param len:
        length of the buffer
    :type len: unsigned int

    :param force_8bit:
        force 8-bit bus access
    :type force_8bit: bool

.. _`nand_read_data_op.description`:

Description
-----------

This function does a raw data read on the bus. Usually used after launching
another NAND operation like \ :c:func:`nand_read_page_op`\ .
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_write_data_op`:

nand_write_data_op
==================

.. c:function:: int nand_write_data_op(struct nand_chip *chip, const void *buf, unsigned int len, bool force_8bit)

    Write data from the NAND

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param buf:
        buffer containing the data to send on the bus
    :type buf: const void \*

    :param len:
        length of the buffer
    :type len: unsigned int

    :param force_8bit:
        force 8-bit bus access
    :type force_8bit: bool

.. _`nand_write_data_op.description`:

Description
-----------

This function does a raw data write on the bus. Usually used after launching
another NAND operation like \ :c:func:`nand_write_page_begin_op`\ .
This function does not select/unselect the CS line.

Returns 0 on success, a negative error code otherwise.

.. _`nand_op_parser_ctx`:

struct nand_op_parser_ctx
=========================

.. c:type:: struct nand_op_parser_ctx

    Context used by the parser

.. _`nand_op_parser_ctx.definition`:

Definition
----------

.. code-block:: c

    struct nand_op_parser_ctx {
        const struct nand_op_instr *instrs;
        unsigned int ninstrs;
        struct nand_subop subop;
    }

.. _`nand_op_parser_ctx.members`:

Members
-------

instrs
    array of all the instructions that must be addressed

ninstrs
    length of the \ ``instrs``\  array

subop
    Sub-operation to be passed to the NAND controller

.. _`nand_op_parser_ctx.description`:

Description
-----------

This structure is used by the core to split NAND operations into
sub-operations that can be handled by the NAND controller.

.. _`nand_op_parser_must_split_instr`:

nand_op_parser_must_split_instr
===============================

.. c:function:: bool nand_op_parser_must_split_instr(const struct nand_op_parser_pattern_elem *pat, const struct nand_op_instr *instr, unsigned int *start_offset)

    Checks if an instruction must be split

    :param pat:
        the parser pattern element that matches \ ``instr``\ 
    :type pat: const struct nand_op_parser_pattern_elem \*

    :param instr:
        pointer to the instruction to check
    :type instr: const struct nand_op_instr \*

    :param start_offset:
        this is an in/out parameter. If \ ``instr``\  has already been
        split, then \ ``start_offset``\  is the offset from which to start
        (either an address cycle or an offset in the data buffer).
        Conversely, if the function returns true (ie. instr must be
        split), this parameter is updated to point to the first
        data/address cycle that has not been taken care of.
    :type start_offset: unsigned int \*

.. _`nand_op_parser_must_split_instr.description`:

Description
-----------

Some NAND controllers are limited and cannot send X address cycles with a
unique operation, or cannot read/write more than Y bytes at the same time.
In this case, split the instruction that does not fit in a single
controller-operation into two or more chunks.

Returns true if the instruction must be split, false otherwise.
The \ ``start_offset``\  parameter is also updated to the offset at which the next
bundle of instruction must start (if an address or a data instruction).

.. _`nand_op_parser_match_pat`:

nand_op_parser_match_pat
========================

.. c:function:: bool nand_op_parser_match_pat(const struct nand_op_parser_pattern *pat, struct nand_op_parser_ctx *ctx)

    Checks if a pattern matches the instructions remaining in the parser context

    :param pat:
        the pattern to test
    :type pat: const struct nand_op_parser_pattern \*

    :param ctx:
        the parser context structure to match with the pattern \ ``pat``\ 
    :type ctx: struct nand_op_parser_ctx \*

.. _`nand_op_parser_match_pat.description`:

Description
-----------

Check if \ ``pat``\  matches the set or a sub-set of instructions remaining in \ ``ctx``\ .
Returns true if this is the case, false ortherwise. When true is returned,
\ ``ctx->subop``\  is updated with the set of instructions to be passed to the
controller driver.

.. _`nand_op_parser_exec_op`:

nand_op_parser_exec_op
======================

.. c:function:: int nand_op_parser_exec_op(struct nand_chip *chip, const struct nand_op_parser *parser, const struct nand_operation *op, bool check_only)

    exec_op parser

    :param chip:
        the NAND chip
    :type chip: struct nand_chip \*

    :param parser:
        patterns description provided by the controller driver
    :type parser: const struct nand_op_parser \*

    :param op:
        the NAND operation to address
    :type op: const struct nand_operation \*

    :param check_only:
        when true, the function only checks if \ ``op``\  can be handled but
        does not execute the operation
    :type check_only: bool

.. _`nand_op_parser_exec_op.description`:

Description
-----------

Helper function designed to ease integration of NAND controller drivers that
only support a limited set of instruction sequences. The supported sequences
are described in \ ``parser``\ , and the framework takes care of splitting \ ``op``\  into
multiple sub-operations (if required) and pass them back to the ->exec()
callback of the matching pattern if \ ``check_only``\  is set to false.

NAND controller drivers should call this function from their own ->exec_op()
implementation.

Returns 0 on success, a negative error code otherwise. A failure can be
caused by an unsupported operation (none of the supported patterns is able
to handle the requested operation), or an error returned by one of the
matching pattern->exec() hook.

.. _`nand_subop_get_addr_start_off`:

nand_subop_get_addr_start_off
=============================

.. c:function:: unsigned int nand_subop_get_addr_start_off(const struct nand_subop *subop, unsigned int instr_idx)

    Get the start offset in an address array

    :param subop:
        The entire sub-operation
    :type subop: const struct nand_subop \*

    :param instr_idx:
        Index of the instruction inside the sub-operation
    :type instr_idx: unsigned int

.. _`nand_subop_get_addr_start_off.description`:

Description
-----------

During driver development, one could be tempted to directly use the
->addr.addrs field of address instructions. This is wrong as address
instructions might be split.

Given an address instruction, returns the offset of the first cycle to issue.

.. _`nand_subop_get_num_addr_cyc`:

nand_subop_get_num_addr_cyc
===========================

.. c:function:: unsigned int nand_subop_get_num_addr_cyc(const struct nand_subop *subop, unsigned int instr_idx)

    Get the remaining address cycles to assert

    :param subop:
        The entire sub-operation
    :type subop: const struct nand_subop \*

    :param instr_idx:
        Index of the instruction inside the sub-operation
    :type instr_idx: unsigned int

.. _`nand_subop_get_num_addr_cyc.description`:

Description
-----------

During driver development, one could be tempted to directly use the
->addr->naddrs field of a data instruction. This is wrong as instructions
might be split.

Given an address instruction, returns the number of address cycle to issue.

.. _`nand_subop_get_data_start_off`:

nand_subop_get_data_start_off
=============================

.. c:function:: unsigned int nand_subop_get_data_start_off(const struct nand_subop *subop, unsigned int instr_idx)

    Get the start offset in a data array

    :param subop:
        The entire sub-operation
    :type subop: const struct nand_subop \*

    :param instr_idx:
        Index of the instruction inside the sub-operation
    :type instr_idx: unsigned int

.. _`nand_subop_get_data_start_off.description`:

Description
-----------

During driver development, one could be tempted to directly use the
->data->buf.{in,out} field of data instructions. This is wrong as data
instructions might be split.

Given a data instruction, returns the offset to start from.

.. _`nand_subop_get_data_len`:

nand_subop_get_data_len
=======================

.. c:function:: unsigned int nand_subop_get_data_len(const struct nand_subop *subop, unsigned int instr_idx)

    Get the number of bytes to retrieve

    :param subop:
        The entire sub-operation
    :type subop: const struct nand_subop \*

    :param instr_idx:
        Index of the instruction inside the sub-operation
    :type instr_idx: unsigned int

.. _`nand_subop_get_data_len.description`:

Description
-----------

During driver development, one could be tempted to directly use the
->data->len field of a data instruction. This is wrong as data instructions
might be split.

Returns the length of the chunk of data to send/receive.

.. _`nand_reset`:

nand_reset
==========

.. c:function:: int nand_reset(struct nand_chip *chip, int chipnr)

    Reset and initialize a NAND device

    :param chip:
        The NAND chip
    :type chip: struct nand_chip \*

    :param chipnr:
        Internal die id
    :type chipnr: int

.. _`nand_reset.description`:

Description
-----------

Save the timings data structure, then apply SDR timings mode 0 (see
nand_reset_data_interface for details), do the reset operation, and
apply back the previous timings.

Returns 0 on success, a negative error code otherwise.

.. _`nand_get_features`:

nand_get_features
=================

.. c:function:: int nand_get_features(struct nand_chip *chip, int addr, u8 *subfeature_param)

    wrapper to perform a GET_FEATURE

    :param chip:
        NAND chip info structure
    :type chip: struct nand_chip \*

    :param addr:
        feature address
    :type addr: int

    :param subfeature_param:
        the subfeature parameters, a four bytes array
    :type subfeature_param: u8 \*

.. _`nand_get_features.description`:

Description
-----------

Returns 0 for success, a negative error otherwise. Returns -ENOTSUPP if the
operation cannot be handled.

.. _`nand_set_features`:

nand_set_features
=================

.. c:function:: int nand_set_features(struct nand_chip *chip, int addr, u8 *subfeature_param)

    wrapper to perform a SET_FEATURE

    :param chip:
        NAND chip info structure
    :type chip: struct nand_chip \*

    :param addr:
        feature address
    :type addr: int

    :param subfeature_param:
        the subfeature parameters, a four bytes array
    :type subfeature_param: u8 \*

.. _`nand_set_features.description`:

Description
-----------

Returns 0 for success, a negative error otherwise. Returns -ENOTSUPP if the
operation cannot be handled.

.. _`nand_check_erased_buf`:

nand_check_erased_buf
=====================

.. c:function:: int nand_check_erased_buf(void *buf, int len, int bitflips_threshold)

    check if a buffer contains (almost) only 0xff data

    :param buf:
        buffer to test
    :type buf: void \*

    :param len:
        buffer length
    :type len: int

    :param bitflips_threshold:
        maximum number of bitflips
    :type bitflips_threshold: int

.. _`nand_check_erased_buf.description`:

Description
-----------

Check if a buffer contains only 0xff, which means the underlying region
has been erased and is ready to be programmed.
The bitflips_threshold specify the maximum number of bitflips before
considering the region is not erased.

.. _`nand_check_erased_buf.note`:

Note
----

The logic of this function has been extracted from the memweight
implementation, except that nand_check_erased_buf function exit before
testing the whole buffer if the number of bitflips exceed the
bitflips_threshold value.

Returns a positive number of bitflips less than or equal to
bitflips_threshold, or -ERROR_CODE for bitflips in excess of the
threshold.

.. _`nand_check_erased_ecc_chunk`:

nand_check_erased_ecc_chunk
===========================

.. c:function:: int nand_check_erased_ecc_chunk(void *data, int datalen, void *ecc, int ecclen, void *extraoob, int extraooblen, int bitflips_threshold)

    check if an ECC chunk contains (almost) only 0xff data

    :param data:
        data buffer to test
    :type data: void \*

    :param datalen:
        data length
    :type datalen: int

    :param ecc:
        ECC buffer
    :type ecc: void \*

    :param ecclen:
        ECC length
    :type ecclen: int

    :param extraoob:
        extra OOB buffer
    :type extraoob: void \*

    :param extraooblen:
        extra OOB length
    :type extraooblen: int

    :param bitflips_threshold:
        maximum number of bitflips
    :type bitflips_threshold: int

.. _`nand_check_erased_ecc_chunk.description`:

Description
-----------

Check if a data buffer and its associated ECC and OOB data contains only
0xff pattern, which means the underlying region has been erased and is
ready to be programmed.
The bitflips_threshold specify the maximum number of bitflips before
considering the region as not erased.

.. _`nand_check_erased_ecc_chunk.note`:

Note
----

1/ ECC algorithms are working on pre-defined block sizes which are usually
   different from the NAND page size. When fixing bitflips, ECC engines will
   report the number of errors per chunk, and the NAND core infrastructure
   expect you to return the maximum number of bitflips for the whole page.
   This is why you should always use this function on a single chunk and
   not on the whole page. After checking each chunk you should update your
   max_bitflips value accordingly.
2/ When checking for bitflips in erased pages you should not only check
   the payload data but also their associated ECC data, because a user might
   have programmed almost all bits to 1 but a few. In this case, we
   shouldn't consider the chunk as erased, and checking ECC bytes prevent
   this case.
3/ The extraoob argument is optional, and should be used if some of your OOB
   data are protected by the ECC engine.
   It could also be used if you support subpages and want to attach some
   extra OOB data to an ECC chunk.

Returns a positive number of bitflips less than or equal to
bitflips_threshold, or -ERROR_CODE for bitflips in excess of the
threshold. In case of success, the passed buffers are filled with 0xff.

.. _`nand_read_page_raw_notsupp`:

nand_read_page_raw_notsupp
==========================

.. c:function:: int nand_read_page_raw_notsupp(struct nand_chip *chip, u8 *buf, int oob_required, int page)

    dummy read raw page function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store read data
    :type buf: u8 \*

    :param oob_required:
        caller requires OOB data read to chip->oob_poi
    :type oob_required: int

    :param page:
        page number to read
    :type page: int

.. _`nand_read_page_raw_notsupp.description`:

Description
-----------

Returns -ENOTSUPP unconditionally.

.. _`nand_read_page_raw`:

nand_read_page_raw
==================

.. c:function:: int nand_read_page_raw(struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [INTERN] read raw page data without ecc

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store read data
    :type buf: uint8_t \*

    :param oob_required:
        caller requires OOB data read to chip->oob_poi
    :type oob_required: int

    :param page:
        page number to read
    :type page: int

.. _`nand_read_page_raw.description`:

Description
-----------

Not for syndrome calculating ECC controllers, which use a special oob layout.

.. _`nand_read_page_raw_syndrome`:

nand_read_page_raw_syndrome
===========================

.. c:function:: int nand_read_page_raw_syndrome(struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [INTERN] read raw page data without ecc

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store read data
    :type buf: uint8_t \*

    :param oob_required:
        caller requires OOB data read to chip->oob_poi
    :type oob_required: int

    :param page:
        page number to read
    :type page: int

.. _`nand_read_page_raw_syndrome.description`:

Description
-----------

We need a special oob layout and handling even when OOB isn't used.

.. _`nand_read_page_swecc`:

nand_read_page_swecc
====================

.. c:function:: int nand_read_page_swecc(struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] software ECC based page read function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store read data
    :type buf: uint8_t \*

    :param oob_required:
        caller requires OOB data read to chip->oob_poi
    :type oob_required: int

    :param page:
        page number to read
    :type page: int

.. _`nand_read_subpage`:

nand_read_subpage
=================

.. c:function:: int nand_read_subpage(struct nand_chip *chip, uint32_t data_offs, uint32_t readlen, uint8_t *bufpoi, int page)

    [REPLACEABLE] ECC based sub-page read function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param data_offs:
        offset of requested data within the page
    :type data_offs: uint32_t

    :param readlen:
        data length
    :type readlen: uint32_t

    :param bufpoi:
        buffer to store read data
    :type bufpoi: uint8_t \*

    :param page:
        page number to read
    :type page: int

.. _`nand_read_page_hwecc`:

nand_read_page_hwecc
====================

.. c:function:: int nand_read_page_hwecc(struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC based page read function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store read data
    :type buf: uint8_t \*

    :param oob_required:
        caller requires OOB data read to chip->oob_poi
    :type oob_required: int

    :param page:
        page number to read
    :type page: int

.. _`nand_read_page_hwecc.description`:

Description
-----------

Not for syndrome calculating ECC controllers which need a special oob layout.

.. _`nand_read_page_hwecc_oob_first`:

nand_read_page_hwecc_oob_first
==============================

.. c:function:: int nand_read_page_hwecc_oob_first(struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hw ecc, read oob first

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store read data
    :type buf: uint8_t \*

    :param oob_required:
        caller requires OOB data read to chip->oob_poi
    :type oob_required: int

    :param page:
        page number to read
    :type page: int

.. _`nand_read_page_hwecc_oob_first.description`:

Description
-----------

Hardware ECC for large page chips, require OOB to be read first. For this
ECC mode, the write_page method is re-used from ECC_HW. These methods
read/write ECC from the OOB area, unlike the ECC_HW_SYNDROME support with
multiple ECC steps, follows the "infix ECC" scheme and reads/writes ECC from
the data area, by overwriting the NAND manufacturer bad block markings.

.. _`nand_read_page_syndrome`:

nand_read_page_syndrome
=======================

.. c:function:: int nand_read_page_syndrome(struct nand_chip *chip, uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC syndrome based page read

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        buffer to store read data
    :type buf: uint8_t \*

    :param oob_required:
        caller requires OOB data read to chip->oob_poi
    :type oob_required: int

    :param page:
        page number to read
    :type page: int

.. _`nand_read_page_syndrome.description`:

Description
-----------

The hw generator calculates the error syndrome automatically. Therefore we
need a special oob layout and handling.

.. _`nand_transfer_oob`:

nand_transfer_oob
=================

.. c:function:: uint8_t *nand_transfer_oob(struct mtd_info *mtd, uint8_t *oob, struct mtd_oob_ops *ops, size_t len)

    [INTERN] Transfer oob to client buffer

    :param mtd:
        mtd info structure
    :type mtd: struct mtd_info \*

    :param oob:
        oob destination address
    :type oob: uint8_t \*

    :param ops:
        oob ops structure
    :type ops: struct mtd_oob_ops \*

    :param len:
        size of oob to transfer
    :type len: size_t

.. _`nand_setup_read_retry`:

nand_setup_read_retry
=====================

.. c:function:: int nand_setup_read_retry(struct nand_chip *chip, int retry_mode)

    [INTERN] Set the READ RETRY mode

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param retry_mode:
        the retry mode to use
    :type retry_mode: int

.. _`nand_setup_read_retry.description`:

Description
-----------

Some vendors supply a special command to shift the Vt threshold, to be used
when there are too many bitflips in a page (i.e., ECC error). After setting
a new threshold, the host should retry reading the page.

.. _`nand_do_read_ops`:

nand_do_read_ops
================

.. c:function:: int nand_do_read_ops(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [INTERN] Read data with ECC

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param from:
        offset to read from
    :type from: loff_t

    :param ops:
        oob ops structure
    :type ops: struct mtd_oob_ops \*

.. _`nand_do_read_ops.description`:

Description
-----------

Internal function. Called with chip held.

.. _`nand_read_oob_std`:

nand_read_oob_std
=================

.. c:function:: int nand_read_oob_std(struct nand_chip *chip, int page)

    [REPLACEABLE] the most common OOB data read function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param page:
        page number to read
    :type page: int

.. _`nand_read_oob_syndrome`:

nand_read_oob_syndrome
======================

.. c:function:: int nand_read_oob_syndrome(struct nand_chip *chip, int page)

    [REPLACEABLE] OOB data read function for HW ECC with syndromes

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param page:
        page number to read
    :type page: int

.. _`nand_write_oob_std`:

nand_write_oob_std
==================

.. c:function:: int nand_write_oob_std(struct nand_chip *chip, int page)

    [REPLACEABLE] the most common OOB data write function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param page:
        page number to write
    :type page: int

.. _`nand_write_oob_syndrome`:

nand_write_oob_syndrome
=======================

.. c:function:: int nand_write_oob_syndrome(struct nand_chip *chip, int page)

    [REPLACEABLE] OOB data write function for HW ECC with syndrome - only for large page flash

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param page:
        page number to write
    :type page: int

.. _`nand_do_read_oob`:

nand_do_read_oob
================

.. c:function:: int nand_do_read_oob(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [INTERN] NAND read out-of-band

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param from:
        offset to read from
    :type from: loff_t

    :param ops:
        oob operations description structure
    :type ops: struct mtd_oob_ops \*

.. _`nand_do_read_oob.description`:

Description
-----------

NAND read out-of-band data from the spare area.

.. _`nand_read_oob`:

nand_read_oob
=============

.. c:function:: int nand_read_oob(struct mtd_info *mtd, loff_t from, struct mtd_oob_ops *ops)

    [MTD Interface] NAND read data and/or out-of-band

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param from:
        offset to read from
    :type from: loff_t

    :param ops:
        oob operation description structure
    :type ops: struct mtd_oob_ops \*

.. _`nand_read_oob.description`:

Description
-----------

NAND read data and/or out-of-band data.

.. _`nand_write_page_raw_notsupp`:

nand_write_page_raw_notsupp
===========================

.. c:function:: int nand_write_page_raw_notsupp(struct nand_chip *chip, const u8 *buf, int oob_required, int page)

    dummy raw page write function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const u8 \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page number to write
    :type page: int

.. _`nand_write_page_raw_notsupp.description`:

Description
-----------

Returns -ENOTSUPP unconditionally.

.. _`nand_write_page_raw`:

nand_write_page_raw
===================

.. c:function:: int nand_write_page_raw(struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [INTERN] raw page write function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page number to write
    :type page: int

.. _`nand_write_page_raw.description`:

Description
-----------

Not for syndrome calculating ECC controllers, which use a special oob layout.

.. _`nand_write_page_raw_syndrome`:

nand_write_page_raw_syndrome
============================

.. c:function:: int nand_write_page_raw_syndrome(struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [INTERN] raw page write function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page number to write
    :type page: int

.. _`nand_write_page_raw_syndrome.description`:

Description
-----------

We need a special oob layout and handling even when ECC isn't checked.

.. _`nand_write_page_swecc`:

nand_write_page_swecc
=====================

.. c:function:: int nand_write_page_swecc(struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] software ECC based page write function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page number to write
    :type page: int

.. _`nand_write_page_hwecc`:

nand_write_page_hwecc
=====================

.. c:function:: int nand_write_page_hwecc(struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC based page write function

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page number to write
    :type page: int

.. _`nand_write_subpage_hwecc`:

nand_write_subpage_hwecc
========================

.. c:function:: int nand_write_subpage_hwecc(struct nand_chip *chip, uint32_t offset, uint32_t data_len, const uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC based subpage write

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param offset:
        column address of subpage within the page
    :type offset: uint32_t

    :param data_len:
        data length
    :type data_len: uint32_t

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page number to write
    :type page: int

.. _`nand_write_page_syndrome`:

nand_write_page_syndrome
========================

.. c:function:: int nand_write_page_syndrome(struct nand_chip *chip, const uint8_t *buf, int oob_required, int page)

    [REPLACEABLE] hardware ECC syndrome based page write

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param buf:
        data buffer
    :type buf: const uint8_t \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page number to write
    :type page: int

.. _`nand_write_page_syndrome.description`:

Description
-----------

The hw generator calculates the error syndrome automatically. Therefore we
need a special oob layout and handling.

.. _`nand_write_page`:

nand_write_page
===============

.. c:function:: int nand_write_page(struct mtd_info *mtd, struct nand_chip *chip, uint32_t offset, int data_len, const uint8_t *buf, int oob_required, int page, int raw)

    write one page

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param chip:
        NAND chip descriptor
    :type chip: struct nand_chip \*

    :param offset:
        address offset within the page
    :type offset: uint32_t

    :param data_len:
        length of actual data to be written
    :type data_len: int

    :param buf:
        the data to write
    :type buf: const uint8_t \*

    :param oob_required:
        must write chip->oob_poi to OOB
    :type oob_required: int

    :param page:
        page number to write
    :type page: int

    :param raw:
        use _raw version of write_page
    :type raw: int

.. _`nand_fill_oob`:

nand_fill_oob
=============

.. c:function:: uint8_t *nand_fill_oob(struct mtd_info *mtd, uint8_t *oob, size_t len, struct mtd_oob_ops *ops)

    [INTERN] Transfer client buffer to oob

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param oob:
        oob data buffer
    :type oob: uint8_t \*

    :param len:
        oob data write length
    :type len: size_t

    :param ops:
        oob ops structure
    :type ops: struct mtd_oob_ops \*

.. _`nand_do_write_ops`:

nand_do_write_ops
=================

.. c:function:: int nand_do_write_ops(struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [INTERN] NAND write with ECC

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param to:
        offset to write to
    :type to: loff_t

    :param ops:
        oob operations description structure
    :type ops: struct mtd_oob_ops \*

.. _`nand_do_write_ops.description`:

Description
-----------

NAND write with ECC.

.. _`panic_nand_write`:

panic_nand_write
================

.. c:function:: int panic_nand_write(struct mtd_info *mtd, loff_t to, size_t len, size_t *retlen, const uint8_t *buf)

    [MTD Interface] NAND write with ECC

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param to:
        offset to write to
    :type to: loff_t

    :param len:
        number of bytes to write
    :type len: size_t

    :param retlen:
        pointer to variable to store the number of written bytes
    :type retlen: size_t \*

    :param buf:
        the data to write
    :type buf: const uint8_t \*

.. _`panic_nand_write.description`:

Description
-----------

NAND write with ECC. Used when performing writes in interrupt context, this
may for example be called by mtdoops when writing an oops while in panic.

.. _`nand_do_write_oob`:

nand_do_write_oob
=================

.. c:function:: int nand_do_write_oob(struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [MTD Interface] NAND write out-of-band

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param to:
        offset to write to
    :type to: loff_t

    :param ops:
        oob operation description structure
    :type ops: struct mtd_oob_ops \*

.. _`nand_do_write_oob.description`:

Description
-----------

NAND write out-of-band.

.. _`nand_write_oob`:

nand_write_oob
==============

.. c:function:: int nand_write_oob(struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops)

    [MTD Interface] NAND write data and/or out-of-band

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param to:
        offset to write to
    :type to: loff_t

    :param ops:
        oob operation description structure
    :type ops: struct mtd_oob_ops \*

.. _`single_erase`:

single_erase
============

.. c:function:: int single_erase(struct nand_chip *chip, int page)

    [GENERIC] NAND standard block erase command function

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param page:
        the page address of the block which will be erased
    :type page: int

.. _`single_erase.description`:

Description
-----------

Standard erase command for NAND chips. Returns NAND status.

.. _`nand_erase`:

nand_erase
==========

.. c:function:: int nand_erase(struct mtd_info *mtd, struct erase_info *instr)

    [MTD Interface] erase block(s)

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param instr:
        erase instruction
    :type instr: struct erase_info \*

.. _`nand_erase.description`:

Description
-----------

Erase one ore more blocks.

.. _`nand_erase_nand`:

nand_erase_nand
===============

.. c:function:: int nand_erase_nand(struct nand_chip *chip, struct erase_info *instr, int allowbbt)

    [INTERN] erase block(s)

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param instr:
        erase instruction
    :type instr: struct erase_info \*

    :param allowbbt:
        allow erasing the bbt area
    :type allowbbt: int

.. _`nand_erase_nand.description`:

Description
-----------

Erase one ore more blocks.

.. _`nand_sync`:

nand_sync
=========

.. c:function:: void nand_sync(struct mtd_info *mtd)

    [MTD Interface] sync

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

.. _`nand_sync.description`:

Description
-----------

Sync is actually a wait for chip ready function.

.. _`nand_block_isbad`:

nand_block_isbad
================

.. c:function:: int nand_block_isbad(struct mtd_info *mtd, loff_t offs)

    [MTD Interface] Check if block at offset is bad

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param offs:
        offset relative to mtd start
    :type offs: loff_t

.. _`nand_block_markbad`:

nand_block_markbad
==================

.. c:function:: int nand_block_markbad(struct mtd_info *mtd, loff_t ofs)

    [MTD Interface] Mark block at the given offset as bad

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param ofs:
        offset relative to mtd start
    :type ofs: loff_t

.. _`nand_max_bad_blocks`:

nand_max_bad_blocks
===================

.. c:function:: int nand_max_bad_blocks(struct mtd_info *mtd, loff_t ofs, size_t len)

    [MTD Interface] Max number of bad blocks for an mtd

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

    :param ofs:
        offset relative to mtd start
    :type ofs: loff_t

    :param len:
        length of mtd
    :type len: size_t

.. _`nand_suspend`:

nand_suspend
============

.. c:function:: int nand_suspend(struct mtd_info *mtd)

    [MTD Interface] Suspend the NAND flash

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

.. _`nand_resume`:

nand_resume
===========

.. c:function:: void nand_resume(struct mtd_info *mtd)

    [MTD Interface] Resume the NAND flash

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

.. _`nand_shutdown`:

nand_shutdown
=============

.. c:function:: void nand_shutdown(struct mtd_info *mtd)

    [MTD Interface] Finish the current NAND operation and prevent further operations

    :param mtd:
        MTD device structure
    :type mtd: struct mtd_info \*

.. _`nand_scan_ident`:

nand_scan_ident
===============

.. c:function:: int nand_scan_ident(struct nand_chip *chip, unsigned int maxchips, struct nand_flash_dev *table)

    Scan for the NAND device

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param maxchips:
        number of chips to scan for
    :type maxchips: unsigned int

    :param table:
        alternative NAND ID table
    :type table: struct nand_flash_dev \*

.. _`nand_scan_ident.description`:

Description
-----------

This is the first phase of the normal \ :c:func:`nand_scan`\  function. It reads the
flash ID and sets up MTD fields accordingly.

This helper used to be called directly from controller drivers that needed
to tweak some ECC-related parameters before \ :c:func:`nand_scan_tail`\ . This separation
prevented dynamic allocations during this phase which was unconvenient and
as been banned for the benefit of the ->init_ecc()/cleanup_ecc() hooks.

.. _`nand_check_ecc_caps`:

nand_check_ecc_caps
===================

.. c:function:: int nand_check_ecc_caps(struct nand_chip *chip, const struct nand_ecc_caps *caps, int oobavail)

    check the sanity of preset ECC settings

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param caps:
        ECC caps info structure
    :type caps: const struct nand_ecc_caps \*

    :param oobavail:
        OOB size that the ECC engine can use
    :type oobavail: int

.. _`nand_check_ecc_caps.description`:

Description
-----------

When ECC step size and strength are already set, check if they are supported
by the controller and the calculated ECC bytes fit within the chip's OOB.
On success, the calculated ECC bytes is set.

.. _`nand_match_ecc_req`:

nand_match_ecc_req
==================

.. c:function:: int nand_match_ecc_req(struct nand_chip *chip, const struct nand_ecc_caps *caps, int oobavail)

    meet the chip's requirement with least ECC bytes

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param caps:
        ECC engine caps info structure
    :type caps: const struct nand_ecc_caps \*

    :param oobavail:
        OOB size that the ECC engine can use
    :type oobavail: int

.. _`nand_match_ecc_req.description`:

Description
-----------

If a chip's ECC requirement is provided, try to meet it with the least
number of ECC bytes (i.e. with the largest number of OOB-free bytes).
On success, the chosen ECC settings are set.

.. _`nand_maximize_ecc`:

nand_maximize_ecc
=================

.. c:function:: int nand_maximize_ecc(struct nand_chip *chip, const struct nand_ecc_caps *caps, int oobavail)

    choose the max ECC strength available

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param caps:
        ECC engine caps info structure
    :type caps: const struct nand_ecc_caps \*

    :param oobavail:
        OOB size that the ECC engine can use
    :type oobavail: int

.. _`nand_maximize_ecc.description`:

Description
-----------

Choose the max ECC strength that is supported on the controller, and can fit
within the chip's OOB.  On success, the chosen ECC settings are set.

.. _`nand_ecc_choose_conf`:

nand_ecc_choose_conf
====================

.. c:function:: int nand_ecc_choose_conf(struct nand_chip *chip, const struct nand_ecc_caps *caps, int oobavail)

    Set the ECC strength and ECC step size

    :param chip:
        nand chip info structure
    :type chip: struct nand_chip \*

    :param caps:
        ECC engine caps info structure
    :type caps: const struct nand_ecc_caps \*

    :param oobavail:
        OOB size that the ECC engine can use
    :type oobavail: int

.. _`nand_ecc_choose_conf.description`:

Description
-----------

Choose the ECC configuration according to following logic

1. If both ECC step size and ECC strength are already set (usually by DT)
   then check if it is supported by this controller.
2. If NAND_ECC_MAXIMIZE is set, then select maximum ECC strength.
3. Otherwise, try to match the ECC step size and ECC strength closest
   to the chip's requirement. If available OOB size can't fit the chip
   requirement then fallback to the maximum ECC step size and ECC strength.

On success, the chosen ECC settings are set.

.. _`nand_scan_tail`:

nand_scan_tail
==============

.. c:function:: int nand_scan_tail(struct nand_chip *chip)

    Scan for the NAND device

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

.. _`nand_scan_tail.description`:

Description
-----------

This is the second phase of the normal \ :c:func:`nand_scan`\  function. It fills out
all the uninitialized function pointers with the defaults and scans for a
bad block table if appropriate.

.. _`nand_scan_with_ids`:

nand_scan_with_ids
==================

.. c:function:: int nand_scan_with_ids(struct nand_chip *chip, unsigned int maxchips, struct nand_flash_dev *ids)

    [NAND Interface] Scan for the NAND device

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

    :param maxchips:
        number of chips to scan for.
    :type maxchips: unsigned int

    :param ids:
        optional flash IDs table
    :type ids: struct nand_flash_dev \*

.. _`nand_scan_with_ids.description`:

Description
-----------

This fills out all the uninitialized function pointers with the defaults.
The flash ID is read and the mtd/chip structures are filled with the
appropriate values.

.. _`nand_cleanup`:

nand_cleanup
============

.. c:function:: void nand_cleanup(struct nand_chip *chip)

    [NAND Interface] Free resources held by the NAND device

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

.. _`nand_release`:

nand_release
============

.. c:function:: void nand_release(struct nand_chip *chip)

    [NAND Interface] Unregister the MTD device and free resources held by the NAND device

    :param chip:
        NAND chip object
    :type chip: struct nand_chip \*

.. This file was automatic generated / don't edit.

