
.. _defines:

=========
Constants
=========

This chapter describes the constants which might be relevant for a driver developer.


.. _Chip_option_constants:

Chip option constants
=====================


.. _Constants_for_chip_id_table:

Constants for chip id table
---------------------------

These constants are defined in nand.h. They are ored together to describe the chip functionality.


.. code-block:: c

    /* Buswitdh is 16 bit */
    #define NAND_BUSWIDTH_16    0x00000002
    /* Device supports partial programming without padding */
    #define NAND_NO_PADDING     0x00000004
    /* Chip has cache program function */
    #define NAND_CACHEPRG       0x00000008
    /* Chip has copy back function */
    #define NAND_COPYBACK       0x00000010
    /* AND Chip which has 4 banks and a confusing page / block
     * assignment. See Renesas datasheet for further information */
    #define NAND_IS_AND     0x00000020
    /* Chip has a array of 4 pages which can be read without
     * additional ready /busy waits */
    #define NAND_4PAGE_ARRAY    0x00000040


.. _Constants_for_runtime_options:

Constants for runtime options
-----------------------------

These constants are defined in nand.h. They are ored together to describe the functionality.


.. code-block:: c

    /* The hw ecc generator provides a syndrome instead a ecc value on read
     * This can only work if we have the ecc bytes directly behind the
     * data bytes. Applies for DOC and AG-AND Renesas HW Reed Solomon generators */
    #define NAND_HWECC_SYNDROME 0x00020000


.. _EEC_selection_constants:

ECC selection constants
=======================

Use these constants to select the ECC algorithm.


.. code-block:: c

    /* No ECC. Usage is not recommended ! */
    #define NAND_ECC_NONE       0
    /* Software ECC 3 byte ECC per 256 Byte data */
    #define NAND_ECC_SOFT       1
    /* Hardware ECC 3 byte ECC per 256 Byte data */
    #define NAND_ECC_HW3_256    2
    /* Hardware ECC 3 byte ECC per 512 Byte data */
    #define NAND_ECC_HW3_512    3
    /* Hardware ECC 6 byte ECC per 512 Byte data */
    #define NAND_ECC_HW6_512    4
    /* Hardware ECC 6 byte ECC per 512 Byte data */
    #define NAND_ECC_HW8_512    6


.. _Hardware_control_related_constants:

Hardware control related constants
==================================

These constants describe the requested hardware access function when the boardspecific hardware control function is called


.. code-block:: c

    /* Select the chip by setting nCE to low */
    #define NAND_CTL_SETNCE     1
    /* Deselect the chip by setting nCE to high */
    #define NAND_CTL_CLRNCE     2
    /* Select the command latch by setting CLE to high */
    #define NAND_CTL_SETCLE     3
    /* Deselect the command latch by setting CLE to low */
    #define NAND_CTL_CLRCLE     4
    /* Select the address latch by setting ALE to high */
    #define NAND_CTL_SETALE     5
    /* Deselect the address latch by setting ALE to low */
    #define NAND_CTL_CLRALE     6
    /* Set write protection by setting WP to high. Not used! */
    #define NAND_CTL_SETWP      7
    /* Clear write protection by setting WP to low. Not used! */
    #define NAND_CTL_CLRWP      8


.. _Bad_block_table_constants:

Bad block table related constants
=================================

These constants describe the options used for bad block table descriptors.


.. code-block:: c

    /* Options for the bad block table descriptors */

    /* The number of bits used per block in the bbt on the device */
    #define NAND_BBT_NRBITS_MSK 0x0000000F
    #define NAND_BBT_1BIT       0x00000001
    #define NAND_BBT_2BIT       0x00000002
    #define NAND_BBT_4BIT       0x00000004
    #define NAND_BBT_8BIT       0x00000008
    /* The bad block table is in the last good block of the device */
    #define NAND_BBT_LASTBLOCK  0x00000010
    /* The bbt is at the given page, else we must scan for the bbt */
    #define NAND_BBT_ABSPAGE    0x00000020
    /* bbt is stored per chip on multichip devices */
    #define NAND_BBT_PERCHIP    0x00000080
    /* bbt has a version counter at offset veroffs */
    #define NAND_BBT_VERSION    0x00000100
    /* Create a bbt if none axists */
    #define NAND_BBT_CREATE     0x00000200
    /* Write bbt if necessary */
    #define NAND_BBT_WRITE      0x00001000
    /* Read and write back block contents when writing bbt */
    #define NAND_BBT_SAVECONTENT    0x00002000


