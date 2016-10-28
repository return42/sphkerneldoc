.. -*- coding: utf-8; mode: rst -*-

.. _basicboarddriver:

******************
Basic board driver
******************

For most boards it will be sufficient to provide just the basic
functions and fill out some really board dependent members in the nand
chip description structure.


.. _Basic_defines:

Basic defines
=============

At least you have to provide a nand_chip structure and a storage for
the ioremap'ed chip address. You can allocate the nand_chip structure
using kmalloc or you can allocate it statically. The NAND chip structure
embeds an mtd structure which will be registered to the MTD subsystem.
You can extract a pointer to the mtd structure from a nand_chip pointer
using the nand_to_mtd() helper.

Kmalloc based example


.. code-block:: c

    static struct mtd_info *board_mtd;
    static void __iomem *baseaddr;

Static example


.. code-block:: c

    static struct nand_chip board_chip;
    static void __iomem *baseaddr;


.. _Partition_defines:

Partition defines
=================

If you want to divide your device into partitions, then define a
partitioning scheme suitable to your board.


.. code-block:: c

    #define NUM_PARTITIONS 2
    static struct mtd_partition partition_info[] = {
        { .name = "Flash partition 1",
          .offset =  0,
          .size =    8 * 1024 * 1024 },
        { .name = "Flash partition 2",
          .offset =  MTDPART_OFS_NEXT,
          .size =    MTDPART_SIZ_FULL },
    };


.. _Hardware_control_functions:

Hardware control function
=========================

The hardware control function provides access to the control pins of the
NAND chip(s). The access can be done by GPIO pins or by address lines.
If you use address lines, make sure that the timing requirements are
met.

*GPIO based example*


.. code-block:: c

    static void board_hwcontrol(struct mtd_info *mtd, int cmd)
    {
        switch(cmd){
            case NAND_CTL_SETCLE: /* Set CLE pin high */ break;
            case NAND_CTL_CLRCLE: /* Set CLE pin low */ break;
            case NAND_CTL_SETALE: /* Set ALE pin high */ break;
            case NAND_CTL_CLRALE: /* Set ALE pin low */ break;
            case NAND_CTL_SETNCE: /* Set nCE pin low */ break;
            case NAND_CTL_CLRNCE: /* Set nCE pin high */ break;
        }
    }

*Address lines based example.* It's assumed that the nCE pin is driven
by a chip select decoder.


.. code-block:: c

    static void board_hwcontrol(struct mtd_info *mtd, int cmd)
    {
        struct nand_chip *this = mtd_to_nand(mtd);
        switch(cmd){
            case NAND_CTL_SETCLE: this->IO_ADDR_W |= CLE_ADRR_BIT;  break;
            case NAND_CTL_CLRCLE: this->IO_ADDR_W &= ~CLE_ADRR_BIT; break;
            case NAND_CTL_SETALE: this->IO_ADDR_W |= ALE_ADRR_BIT;  break;
            case NAND_CTL_CLRALE: this->IO_ADDR_W &= ~ALE_ADRR_BIT; break;
        }
    }


.. _Device_ready_function:

Device ready function
=====================

If the hardware interface has the ready busy pin of the NAND chip
connected to a GPIO or other accessible I/O pin, this function is used
to read back the state of the pin. The function has no arguments and
should return 0, if the device is busy (R/B pin is low) and 1, if the
device is ready (R/B pin is high). If the hardware interface does not
give access to the ready busy pin, then the function must not be defined
and the function pointer this->dev_ready is set to NULL.


.. _Init_function:

Init function
=============

The init function allocates memory and sets up all the board specific
parameters and function pointers. When everything is set up nand_scan()
is called. This function tries to detect and identify then chip. If a
chip is found all the internal data fields are initialized accordingly.
The structure(s) have to be zeroed out first and then filled with the
necessary information about the device.


.. code-block:: c

    static int __init board_init (void)
    {
        struct nand_chip *this;
        int err = 0;

        /* Allocate memory for MTD device structure and private data */
        this = kzalloc(sizeof(struct nand_chip), GFP_KERNEL);
        if (!this) {
            printk ("Unable to allocate NAND MTD device structure.\\n");
            err = -ENOMEM;
            goto out;
        }

        board_mtd = nand_to_mtd(this);

        /* map physical address */
        baseaddr = ioremap(CHIP_PHYSICAL_ADDRESS, 1024);
        if (!baseaddr) {
            printk("Ioremap to access NAND chip failed\\n");
            err = -EIO;
            goto out_mtd;
        }

        /* Set address of NAND IO lines */
        this->IO_ADDR_R = baseaddr;
        this->IO_ADDR_W = baseaddr;
        /* Reference hardware control function */
        this->hwcontrol = board_hwcontrol;
        /* Set command delay time, see datasheet for correct value */
        this->chip_delay = CHIP_DEPENDEND_COMMAND_DELAY;
        /* Assign the device ready function, if available */
        this->dev_ready = board_dev_ready;
        this->eccmode = NAND_ECC_SOFT;

        /* Scan to find existence of the device */
        if (nand_scan (board_mtd, 1)) {
            err = -ENXIO;
            goto out_ior;
        }

        add_mtd_partitions(board_mtd, partition_info, NUM_PARTITIONS);
        goto out;

    out_ior:
        iounmap(baseaddr);
    out_mtd:
        kfree (this);
    out:
        return err;
    }
    module_init(board_init);


.. _Exit_function:

Exit function
=============

The exit function is only necessary if the driver is compiled as a
module. It releases all resources which are held by the chip driver and
unregisters the partitions in the MTD layer.


.. code-block:: c

    #ifdef MODULE
    static void __exit board_cleanup (void)
    {
        /* Release resources, unregister device */
        nand_release (board_mtd);

        /* unmap physical address */
        iounmap(baseaddr);

        /* Free the MTD device structure */
        kfree (mtd_to_nand(board_mtd));
    }
    module_exit(board_cleanup);
    #endif




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
