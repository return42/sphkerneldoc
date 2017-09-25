.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/devices/spear_smi.c

.. _`spear_smi`:

struct spear_smi
================

.. c:type:: struct spear_smi

    Structure for SMI Device

.. _`spear_smi.definition`:

Definition
----------

.. code-block:: c

    struct spear_smi {
        struct clk *clk;
        u32 status;
        unsigned long clk_rate;
        struct mutex lock;
        void __iomem *io_base;
        struct platform_device *pdev;
        wait_queue_head_t cmd_complete;
        u32 num_flashes;
        struct spear_snor_flash *flash[MAX_NUM_FLASH_CHIP];
    }

.. _`spear_smi.members`:

Members
-------

clk
    functional clock

status
    current status register of SMI.

clk_rate
    functional clock rate of SMI (default: SMI_MAX_CLOCK_FREQ)

lock
    lock to prevent parallel access of SMI.

io_base
    base address for registers of SMI.

pdev
    platform device

cmd_complete
    queue to wait for command completion of NOR-flash.

num_flashes
    number of flashes actually present on board.

flash
    separate structure for each Serial NOR-flash attached to SMI.

.. _`spear_snor_flash`:

struct spear_snor_flash
=======================

.. c:type:: struct spear_snor_flash

    Structure for Serial NOR Flash

.. _`spear_snor_flash.definition`:

Definition
----------

.. code-block:: c

    struct spear_snor_flash {
        u32 bank;
        u32 dev_id;
        struct mutex lock;
        struct mtd_info mtd;
        u32 num_parts;
        struct mtd_partition *parts;
        u32 page_size;
        void __iomem *base_addr;
        u8 erase_cmd;
        u8 fast_mode;
    }

.. _`spear_snor_flash.members`:

Members
-------

bank
    Bank number(0, 1, 2, 3) for each NOR-flash.

dev_id
    Device ID of NOR-flash.

lock
    lock to manage flash read, write and erase operations

mtd
    MTD info for each NOR-flash.

num_parts
    Total number of partition in each bank of NOR-flash.

parts
    Partition info for each bank of NOR-flash.

page_size
    Page size of NOR-flash.

base_addr
    Base address of NOR-flash.

erase_cmd
    erase command may vary on different flash types

fast_mode
    flash supports read in fast mode

.. _`spear_smi_read_sr`:

spear_smi_read_sr
=================

.. c:function:: int spear_smi_read_sr(struct spear_smi *dev, u32 bank)

    Read status register of flash through SMI

    :param struct spear_smi \*dev:
        structure of SMI information.

    :param u32 bank:
        bank to which flash is connected

.. _`spear_smi_read_sr.description`:

Description
-----------

This routine will return the status register of the flash chip present at the
given bank.

.. _`spear_smi_wait_till_ready`:

spear_smi_wait_till_ready
=========================

.. c:function:: int spear_smi_wait_till_ready(struct spear_smi *dev, u32 bank, unsigned long timeout)

    wait till flash is ready

    :param struct spear_smi \*dev:
        structure of SMI information.

    :param u32 bank:
        flash corresponding to this bank

    :param unsigned long timeout:
        timeout for busy wait condition

.. _`spear_smi_wait_till_ready.description`:

Description
-----------

This routine checks for WIP (write in progress) bit in Status register
If successful the routine returns 0 else -EBUSY

.. _`spear_smi_int_handler`:

spear_smi_int_handler
=====================

.. c:function:: irqreturn_t spear_smi_int_handler(int irq, void *dev_id)

    SMI Interrupt Handler.

    :param int irq:
        irq number

    :param void \*dev_id:
        structure of SMI device, embedded in dev_id.

.. _`spear_smi_int_handler.description`:

Description
-----------

The handler clears all interrupt conditions and records the status in
dev->status which is used by the driver later.

.. _`spear_smi_hw_init`:

spear_smi_hw_init
=================

.. c:function:: void spear_smi_hw_init(struct spear_smi *dev)

    initializes the smi controller.

    :param struct spear_smi \*dev:
        structure of smi device

.. _`spear_smi_hw_init.description`:

Description
-----------

this routine initializes the smi controller wit the default values

.. _`get_flash_index`:

get_flash_index
===============

.. c:function:: int get_flash_index(u32 flash_id)

    match chip id from a flash list.

    :param u32 flash_id:
        a valid nor flash chip id obtained from board.

.. _`get_flash_index.description`:

Description
-----------

try to validate the chip id by matching from a list, if not found then simply
returns negative. In case of success returns index in to the flash devices
array.

.. _`spear_smi_write_enable`:

spear_smi_write_enable
======================

.. c:function:: int spear_smi_write_enable(struct spear_smi *dev, u32 bank)

    Enable the flash to do write operation

    :param struct spear_smi \*dev:
        structure of SMI device

    :param u32 bank:
        enable write for flash connected to this bank

.. _`spear_smi_write_enable.description`:

Description
-----------

Set write enable latch with Write Enable command.
Returns 0 on success.

.. _`spear_smi_erase_sector`:

spear_smi_erase_sector
======================

.. c:function:: int spear_smi_erase_sector(struct spear_smi *dev, u32 bank, u32 command, u32 bytes)

    erase one sector of flash

    :param struct spear_smi \*dev:
        structure of SMI information

    :param u32 bank:
        bank to which this command needs to be send

    :param u32 command:
        erase command to be send

    :param u32 bytes:
        size of command

.. _`spear_smi_erase_sector.description`:

Description
-----------

Erase one sector of flash memory at offset \`\`offset'' which is any
address within the sector which should be erased.
Returns 0 if successful, non-zero otherwise.

.. _`spear_mtd_erase`:

spear_mtd_erase
===============

.. c:function:: int spear_mtd_erase(struct mtd_info *mtd, struct erase_info *e_info)

    perform flash erase operation as requested by user

    :param struct mtd_info \*mtd:
        Provides the memory characteristics

    :param struct erase_info \*e_info:
        Provides the erase information

.. _`spear_mtd_erase.description`:

Description
-----------

Erase an address range on the flash chip. The address range may extend
one or more erase sectors. Return an error is there is a problem erasing.

.. _`spear_mtd_read`:

spear_mtd_read
==============

.. c:function:: int spear_mtd_read(struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, u8 *buf)

    performs flash read operation as requested by the user

    :param struct mtd_info \*mtd:
        MTD information of the memory bank

    :param loff_t from:
        Address from which to start read

    :param size_t len:
        Number of bytes to be read

    :param size_t \*retlen:
        Fills the Number of bytes actually read

    :param u8 \*buf:
        Fills this after reading

.. _`spear_mtd_read.description`:

Description
-----------

Read an address range from the flash chip. The address range
may be any size provided it is within the physical boundaries.
Returns 0 on success, non zero otherwise

.. _`spear_mtd_write`:

spear_mtd_write
===============

.. c:function:: int spear_mtd_write(struct mtd_info *mtd, loff_t to, size_t len, size_t *retlen, const u8 *buf)

    performs write operation as requested by the user.

    :param struct mtd_info \*mtd:
        MTD information of the memory bank.

    :param loff_t to:
        Address to write.

    :param size_t len:
        Number of bytes to be written.

    :param size_t \*retlen:
        Number of bytes actually wrote.

    :param const u8 \*buf:
        Buffer from which the data to be taken.

.. _`spear_mtd_write.description`:

Description
-----------

Write an address range to the flash chip. Data must be written in
flash_page_size chunks. The address range may be any size provided
it is within the physical boundaries.
Returns 0 on success, non zero otherwise

.. _`spear_smi_probe_flash`:

spear_smi_probe_flash
=====================

.. c:function:: int spear_smi_probe_flash(struct spear_smi *dev, u32 bank)

    Detects the NOR Flash chip.

    :param struct spear_smi \*dev:
        structure of SMI information.

    :param u32 bank:
        bank on which flash must be probed

.. _`spear_smi_probe_flash.description`:

Description
-----------

This routine will check whether there exists a flash chip on a given memory
bank ID.
Return index of the probed flash in flash devices structure

.. _`spear_smi_probe`:

spear_smi_probe
===============

.. c:function:: int spear_smi_probe(struct platform_device *pdev)

    Entry routine

    :param struct platform_device \*pdev:
        platform device structure

.. _`spear_smi_probe.description`:

Description
-----------

This is the first routine which gets invoked during booting and does all
initialization/allocation work. The routine looks for available memory banks,
and do proper init for any found one.
Returns 0 on success, non zero otherwise

.. _`spear_smi_remove`:

spear_smi_remove
================

.. c:function:: int spear_smi_remove(struct platform_device *pdev)

    Exit routine

    :param struct platform_device \*pdev:
        platform device structure

.. _`spear_smi_remove.description`:

Description
-----------

free all allocations and delete the partitions.

.. This file was automatic generated / don't edit.

