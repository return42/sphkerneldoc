.. -*- coding: utf-8; mode: rst -*-

======
nand.h
======


.. _`nand_hw_control`:

struct nand_hw_control
======================

.. c:type:: nand_hw_control

    Control structure for hardware controller (e.g ECC generator) shared among independent devices


.. _`nand_hw_control.definition`:

Definition
----------

.. code-block:: c

  struct nand_hw_control {
    spinlock_t lock;
    struct nand_chip * active;
    wait_queue_head_t wq;
  };


.. _`nand_hw_control.members`:

Members
-------

:``lock``:
    protection lock

:``active``:
    the mtd device which holds the controller currently

:``wq``:
    wait queue to sleep on if a NAND operation is in
    progress used instead of the per chip wait queue
    when a hw controller is available.




.. _`nand_ecc_ctrl`:

struct nand_ecc_ctrl
====================

.. c:type:: nand_ecc_ctrl

    Control structure for ECC


.. _`nand_ecc_ctrl.definition`:

Definition
----------

.. code-block:: c

  struct nand_ecc_ctrl {
    nand_ecc_modes_t mode;
    int steps;
    int size;
    int bytes;
    int total;
    int strength;
    int prepad;
    int postpad;
    unsigned int options;
    struct nand_ecclayout * layout;
    void * priv;
    void (* hwctl) (struct mtd_info *mtd, int mode);
    int (* calculate) (struct mtd_info *mtd, const uint8_t *dat,uint8_t *ecc_code);
    int (* correct) (struct mtd_info *mtd, uint8_t *dat, uint8_t *read_ecc,uint8_t *calc_ecc);
    int (* read_page_raw) (struct mtd_info *mtd, struct nand_chip *chip,uint8_t *buf, int oob_required, int page);
    int (* write_page_raw) (struct mtd_info *mtd, struct nand_chip *chip,const uint8_t *buf, int oob_required, int page);
    int (* read_page) (struct mtd_info *mtd, struct nand_chip *chip,uint8_t *buf, int oob_required, int page);
    int (* read_subpage) (struct mtd_info *mtd, struct nand_chip *chip,uint32_t offs, uint32_t len, uint8_t *buf, int page);
    int (* write_subpage) (struct mtd_info *mtd, struct nand_chip *chip,uint32_t offset, uint32_t data_len,const uint8_t *data_buf, int oob_required, int page);
    int (* write_page) (struct mtd_info *mtd, struct nand_chip *chip,const uint8_t *buf, int oob_required, int page);
    int (* write_oob_raw) (struct mtd_info *mtd, struct nand_chip *chip,int page);
    int (* read_oob_raw) (struct mtd_info *mtd, struct nand_chip *chip,int page);
    int (* read_oob) (struct mtd_info *mtd, struct nand_chip *chip, int page);
    int (* write_oob) (struct mtd_info *mtd, struct nand_chip *chip,int page);
  };


.. _`nand_ecc_ctrl.members`:

Members
-------

:``mode``:
    ECC mode

:``steps``:
    number of ECC steps per page

:``size``:
    data bytes per ECC step

:``bytes``:
    ECC bytes per step

:``total``:
    total number of ECC bytes per page

:``strength``:
    max number of correctible bits per ECC step

:``prepad``:
    padding information for syndrome based ECC generators

:``postpad``:
    padding information for syndrome based ECC generators

:``options``:
    ECC specific options (see NAND_ECC_XXX flags defined above)

:``layout``:
    ECC layout control struct pointer

:``priv``:
    pointer to private ECC control data

:``hwctl``:
    function to control hardware ECC generator. Must only
    be provided if an hardware ECC is available

:``calculate``:
    function for ECC calculation or readback from ECC hardware

:``correct``:
    function for ECC correction, matching to ECC generator (sw/hw).
    Should return a positive number representing the number of
    corrected bitflips, -EBADMSG if the number of bitflips exceed
    ECC strength, or any other error code if the error is not
    directly related to correction.
    If -EBADMSG is returned the input buffers should be left
    untouched.

:``read_page_raw``:
    function to read a raw page without ECC. This function
    should hide the specific layout used by the ECC
    controller and always return contiguous in-band and
    out-of-band data even if they're not stored
    contiguously on the NAND chip (e.g.
    NAND_ECC_HW_SYNDROME interleaves in-band and
    out-of-band data).

:``write_page_raw``:
    function to write a raw page without ECC. This function
    should hide the specific layout used by the ECC
    controller and consider the passed data as contiguous
    in-band and out-of-band data. ECC controller is
    responsible for doing the appropriate transformations
    to adapt to its specific layout (e.g.
    NAND_ECC_HW_SYNDROME interleaves in-band and
    out-of-band data).

:``read_page``:
    function to read a page according to the ECC generator
    requirements; returns maximum number of bitflips corrected in
    any single ECC step, 0 if bitflips uncorrectable, -EIO hw error

:``read_subpage``:
    function to read parts of the page covered by ECC;
    returns same as :c:func:`read_page`

:``write_subpage``:
    function to write parts of the page covered by ECC.

:``write_page``:
    function to write a page according to the ECC generator
    requirements.

:``write_oob_raw``:
    function to write chip OOB data without ECC

:``read_oob_raw``:
    function to read chip OOB data without ECC

:``read_oob``:
    function to read chip OOB data

:``write_oob``:
    function to write chip OOB data




.. _`nand_buffers`:

struct nand_buffers
===================

.. c:type:: nand_buffers

    buffer structure for read/write


.. _`nand_buffers.definition`:

Definition
----------

.. code-block:: c

  struct nand_buffers {
    uint8_t * ecccalc;
    uint8_t * ecccode;
    uint8_t * databuf;
  };


.. _`nand_buffers.members`:

Members
-------

:``ecccalc``:
    buffer pointer for calculated ECC, size is oobsize.

:``ecccode``:
    buffer pointer for ECC read from flash, size is oobsize.

:``databuf``:
    buffer pointer for data, size is (page size + oobsize).




.. _`nand_buffers.description`:

Description
-----------

Do not change the order of buffers. databuf and oobrbuf must be in
consecutive order.



.. _`nand_chip`:

struct nand_chip
================

.. c:type:: nand_chip

    NAND Private Flash Chip Data


.. _`nand_chip.definition`:

Definition
----------

.. code-block:: c

  struct nand_chip {
    struct mtd_info mtd;
    void __iomem * IO_ADDR_R;
    void __iomem * IO_ADDR_W;
    uint8_t (* read_byte) (struct mtd_info *mtd);
    u16 (* read_word) (struct mtd_info *mtd);
    void (* write_byte) (struct mtd_info *mtd, uint8_t byte);
    void (* write_buf) (struct mtd_info *mtd, const uint8_t *buf, int len);
    void (* read_buf) (struct mtd_info *mtd, uint8_t *buf, int len);
    void (* select_chip) (struct mtd_info *mtd, int chip);
    int (* block_bad) (struct mtd_info *mtd, loff_t ofs);
    int (* block_markbad) (struct mtd_info *mtd, loff_t ofs);
    void (* cmd_ctrl) (struct mtd_info *mtd, int dat, unsigned int ctrl);
    int (* dev_ready) (struct mtd_info *mtd);
    void (* cmdfunc) (struct mtd_info *mtd, unsigned command, int column,int page_addr);
    int(* waitfunc) (struct mtd_info *mtd, struct nand_chip *this);
    int (* erase) (struct mtd_info *mtd, int page);
    int (* scan_bbt) (struct mtd_info *mtd);
    int (* errstat) (struct mtd_info *mtd, struct nand_chip *this, int state,int status, int page);
    int (* write_page) (struct mtd_info *mtd, struct nand_chip *chip,uint32_t offset, int data_len, const uint8_t *buf,int oob_required, int page, int cached, int raw);
    int (* onfi_set_features) (struct mtd_info *mtd, struct nand_chip *chip,int feature_addr, uint8_t *subfeature_para);
    int (* onfi_get_features) (struct mtd_info *mtd, struct nand_chip *chip,int feature_addr, uint8_t *subfeature_para);
    int (* setup_read_retry) (struct mtd_info *mtd, int retry_mode);
    int chip_delay;
    unsigned int options;
    unsigned int bbt_options;
    int page_shift;
    int phys_erase_shift;
    int bbt_erase_shift;
    int chip_shift;
    int numchips;
    uint64_t chipsize;
    int pagemask;
    int pagebuf;
    unsigned int pagebuf_bitflips;
    int subpagesize;
    uint8_t bits_per_cell;
    uint16_t ecc_strength_ds;
    uint16_t ecc_step_ds;
    int onfi_timing_mode_default;
    int badblockpos;
    int badblockbits;
    int onfi_version;
    int jedec_version;
    union {unnamed_union};
    int read_retries;
    flstate_t state;
    uint8_t * oob_poi;
    struct nand_hw_control * controller;
    struct nand_ecc_ctrl ecc;
    struct nand_buffers * buffers;
    struct nand_hw_control hwcontrol;
    uint8_t * bbt;
    struct nand_bbt_descr * bbt_td;
    struct nand_bbt_descr * bbt_md;
    struct nand_bbt_descr * badblock_pattern;
    void * priv;
  };


.. _`nand_chip.members`:

Members
-------

:``mtd``:
    MTD device registered to the MTD framework

:``IO_ADDR_R``:
    [BOARDSPECIFIC] address to read the 8 I/O lines of the
    flash device

:``IO_ADDR_W``:
    [BOARDSPECIFIC] address to write the 8 I/O lines of the
    flash device.

:``read_byte``:
    [REPLACEABLE] read one byte from the chip

:``read_word``:
    [REPLACEABLE] read one word from the chip

:``write_byte``:
    [REPLACEABLE] write a single byte to the chip on the
    low 8 I/O lines

:``write_buf``:
    [REPLACEABLE] write data from the buffer to the chip

:``read_buf``:
    [REPLACEABLE] read data from the chip into the buffer

:``select_chip``:
    [REPLACEABLE] select chip nr

:``block_bad``:
    [REPLACEABLE] check if a block is bad, using OOB markers

:``block_markbad``:
    [REPLACEABLE] mark a block bad

:``cmd_ctrl``:
    [BOARDSPECIFIC] hardwarespecific function for controlling
    ALE/CLE/nCE. Also used to write command and address

:``dev_ready``:
    [BOARDSPECIFIC] hardwarespecific function for accessing
    device ready/busy line. If set to NULL no access to
    ready/busy is available and the ready/busy information
    is read from the chip status register.

:``cmdfunc``:
    [REPLACEABLE] hardwarespecific function for writing
    commands to the chip.

:``waitfunc``:
    [REPLACEABLE] hardwarespecific function for wait on
    ready.

:``erase``:
    [REPLACEABLE] erase function

:``scan_bbt``:
    [REPLACEABLE] function to scan bad block table

:``errstat``:
    [OPTIONAL] hardware specific function to perform
    additional error status checks (determine if errors are
    correctable).

:``write_page``:
    [REPLACEABLE] High-level page write function

:``onfi_set_features``:
    [REPLACEABLE] set the features for ONFI nand

:``onfi_get_features``:
    [REPLACEABLE] get the features for ONFI nand

:``setup_read_retry``:
    [FLASHSPECIFIC] flash (vendor) specific function for
    setting the read-retry mode. Mostly needed for MLC NAND.

:``chip_delay``:
    [BOARDSPECIFIC] chip dependent delay for transferring
    data from array to read regs (tR).

:``options``:
    [BOARDSPECIFIC] various chip options. They can partly
    be set to inform nand_scan about special functionality.
    See the defines for further explanation.

:``bbt_options``:
    [INTERN] bad block specific options. All options used
    here must come from bbm.h. By default, these options
    will be copied to the appropriate nand_bbt_descr's.

:``page_shift``:
    [INTERN] number of address bits in a page (column
    address bits).

:``phys_erase_shift``:
    [INTERN] number of address bits in a physical eraseblock

:``bbt_erase_shift``:
    [INTERN] number of address bits in a bbt entry

:``chip_shift``:
    [INTERN] number of address bits in one chip

:``numchips``:
    [INTERN] number of physical chips

:``chipsize``:
    [INTERN] the size of one chip for multichip arrays

:``pagemask``:
    [INTERN] page number mask = number of (pages / chip) - 1

:``pagebuf``:
    [INTERN] holds the pagenumber which is currently in
    data_buf.

:``pagebuf_bitflips``:
    [INTERN] holds the bitflip count for the page which is
    currently in data_buf.

:``subpagesize``:
    [INTERN] holds the subpagesize

:``bits_per_cell``:
    [INTERN] number of bits per cell. i.e., 1 means SLC.

:``ecc_strength_ds``:
    [INTERN] ECC correctability from the datasheet.
    Minimum amount of bit errors per ``ecc_step_ds`` guaranteed
    to be correctable. If unknown, set to zero.

:``ecc_step_ds``:
    [INTERN] ECC step required by the ``ecc_strength_ds``\ ,
    also from the datasheet. It is the recommended ECC step
    size, if known; if unknown, set to zero.

:``onfi_timing_mode_default``:
    [INTERN] default ONFI timing mode. This field is
    either deduced from the datasheet if the NAND
    chip is not ONFI compliant or set to 0 if it is
    (an ONFI chip is always configured in mode 0
    after a NAND reset)

:``badblockpos``:
    [INTERN] position of the bad block marker in the oob
    area.

:``badblockbits``:
    [INTERN] minimum number of set bits in a good block's
    bad block marker position; i.e., BBM == 11110111b is
    not bad when badblockbits == 7

:``onfi_version``:
    [INTERN] holds the chip ONFI version (BCD encoded),
    non 0 if ONFI supported.

:``jedec_version``:
    [INTERN] holds the chip JEDEC version (BCD encoded),
    non 0 if JEDEC supported.

:``{unnamed_union}``:
    anonymous

:``read_retries``:
    [INTERN] the number of read retry modes supported

:``state``:
    [INTERN] the current state of the NAND device

:``oob_poi``:
    "poison value buffer," used for laying out OOB data
    before writing

:``controller``:
    [REPLACEABLE] a pointer to a hardware controller
    structure which is shared among multiple independent
    devices.

:``ecc``:
    [BOARDSPECIFIC] ECC control structure

:``buffers``:
    buffer structure for read/write

:``hwcontrol``:
    platform-specific hardware control structure

:``bbt``:
    [INTERN] bad block table pointer

:``bbt_td``:
    [REPLACEABLE] bad block table descriptor for flash
    lookup.

:``bbt_md``:
    [REPLACEABLE] bad block table mirror descriptor

:``badblock_pattern``:
    [REPLACEABLE] bad block scan pattern used for initial
    bad block scan.

:``priv``:
    [OPTIONAL] pointer to private chip data




.. _`nand_flash_dev`:

struct nand_flash_dev
=====================

.. c:type:: nand_flash_dev

    NAND Flash Device ID Structure


.. _`nand_flash_dev.definition`:

Definition
----------

.. code-block:: c

  struct nand_flash_dev {
    char * name;
    union ecc;
    int onfi_timing_mode_default;
  };


.. _`nand_flash_dev.members`:

Members
-------

:``name``:
    a human-readable name of the NAND chip

:``ecc``:
    ECC correctability and step information from the datasheet.
    ``ecc``\ .strength_ds: The ECC correctability from the datasheet, same as the
    ``ecc_strength_ds`` in nand_chip{}.

    ``ecc``\ .step_ds: The ECC step required by the ``ecc``\ .strength_ds, same as the
    ``ecc_step_ds`` in nand_chip{}, also from the datasheet.
    For example, the "4bit ECC for each 512Byte" can be set with
    NAND_ECC_INFO(4, 512).

:``onfi_timing_mode_default``:
    the default ONFI timing mode entered after a NAND
    reset. Should be deduced from timings described
    in the datasheet.




.. _`nand_manufacturers`:

struct nand_manufacturers
=========================

.. c:type:: nand_manufacturers

    NAND Flash Manufacturer ID Structure


.. _`nand_manufacturers.definition`:

Definition
----------

.. code-block:: c

  struct nand_manufacturers {
    int id;
    char * name;
  };


.. _`nand_manufacturers.members`:

Members
-------

:``id``:
    manufacturer ID code of device.

:``name``:
    Manufacturer name




.. _`platform_nand_chip`:

struct platform_nand_chip
=========================

.. c:type:: platform_nand_chip

    chip level device structure


.. _`platform_nand_chip.definition`:

Definition
----------

.. code-block:: c

  struct platform_nand_chip {
    int nr_chips;
    int chip_offset;
    int nr_partitions;
    struct mtd_partition * partitions;
    int chip_delay;
    unsigned int options;
    unsigned int bbt_options;
    const char ** part_probe_types;
  };


.. _`platform_nand_chip.members`:

Members
-------

:``nr_chips``:
    max. number of chips to scan for

:``chip_offset``:
    chip number offset

:``nr_partitions``:
    number of partitions pointed to by partitions (or zero)

:``partitions``:
    mtd partition list

:``chip_delay``:
    R/B delay value in us

:``options``:
    Option flags, e.g. 16bit buswidth

:``bbt_options``:
    BBT option flags, e.g. NAND_BBT_USE_FLASH

:``part_probe_types``:
    NULL-terminated array of probe types




.. _`platform_nand_ctrl`:

struct platform_nand_ctrl
=========================

.. c:type:: platform_nand_ctrl

    controller level device structure


.. _`platform_nand_ctrl.definition`:

Definition
----------

.. code-block:: c

  struct platform_nand_ctrl {
    int (* probe) (struct platform_device *pdev);
    void (* remove) (struct platform_device *pdev);
    void (* hwcontrol) (struct mtd_info *mtd, int cmd);
    int (* dev_ready) (struct mtd_info *mtd);
    void (* select_chip) (struct mtd_info *mtd, int chip);
    void (* cmd_ctrl) (struct mtd_info *mtd, int dat, unsigned int ctrl);
    void (* write_buf) (struct mtd_info *mtd, const uint8_t *buf, int len);
    void (* read_buf) (struct mtd_info *mtd, uint8_t *buf, int len);
    unsigned char (* read_byte) (struct mtd_info *mtd);
    void * priv;
  };


.. _`platform_nand_ctrl.members`:

Members
-------

:``probe``:
    platform specific function to probe/setup hardware

:``remove``:
    platform specific function to remove/teardown hardware

:``hwcontrol``:
    platform specific hardware control structure

:``dev_ready``:
    platform specific function to read ready/busy pin

:``select_chip``:
    platform specific chip select function

:``cmd_ctrl``:
    platform specific function for controlling
    ALE/CLE/nCE. Also used to write command and address

:``write_buf``:
    platform specific function for write buffer

:``read_buf``:
    platform specific function for read buffer

:``read_byte``:
    platform specific function to read one byte from chip

:``priv``:
    private data to transport driver specific settings




.. _`platform_nand_ctrl.description`:

Description
-----------

All fields are optional and depend on the hardware driver requirements



.. _`platform_nand_data`:

struct platform_nand_data
=========================

.. c:type:: platform_nand_data

    container structure for platform-specific data


.. _`platform_nand_data.definition`:

Definition
----------

.. code-block:: c

  struct platform_nand_data {
    struct platform_nand_chip chip;
    struct platform_nand_ctrl ctrl;
  };


.. _`platform_nand_data.members`:

Members
-------

:``chip``:
    chip level chip structure

:``ctrl``:
    controller level device structure




.. _`nand_opcode_8bits`:

nand_opcode_8bits
=================

.. c:function:: int nand_opcode_8bits (unsigned int command)

    :param unsigned int command:
        opcode to check

