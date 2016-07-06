.. -*- coding: utf-8; mode: rst -*-

.. _boarddriversadvanced:

*******************************
Advanced board driver functions
*******************************

This chapter describes the advanced functionality of the NAND driver.
For a list of functions which can be overridden by the board driver see
the documentation of the nand_chip structure.


.. _Multiple_chip_control:

Multiple chip control
=====================

The nand driver can control chip arrays. Therefore the board driver must
provide an own select_chip function. This function must (de)select the
requested chip. The function pointer in the nand_chip structure must be
set before calling nand_scan(). The maxchip parameter of nand_scan()
defines the maximum number of chips to scan for. Make sure that the
select_chip function can handle the requested number of chips.

The nand driver concatenates the chips to one virtual chip and provides
this virtual chip to the MTD layer.

*Note: The driver can only handle linear chip arrays of equally sized
chips. There is no support for parallel arrays which extend the
buswidth.*

*GPIO based example*


.. code-block:: c

    static void board_select_chip (struct mtd_info *mtd, int chip)
    {
        /* Deselect all chips, set all nCE pins high */
        GPIO(BOARD_NAND_NCE) |= 0xff;
        if (chip >= 0)
            GPIO(BOARD_NAND_NCE) &= ~ (1 << chip);
    }

*Address lines based example.* Its assumed that the nCE pins are
connected to an address decoder.


.. code-block:: c

    static void board_select_chip (struct mtd_info *mtd, int chip)
    {
        struct nand_chip *this = mtd_to_nand(mtd);

        /* Deselect all chips */
        this->IO_ADDR_R &= ~BOARD_NAND_ADDR_MASK;
        this->IO_ADDR_W &= ~BOARD_NAND_ADDR_MASK;
        switch (chip) {
        case 0:
            this->IO_ADDR_R |= BOARD_NAND_ADDR_CHIP0;
            this->IO_ADDR_W |= BOARD_NAND_ADDR_CHIP0;
            break;
        ....
        case n:
            this->IO_ADDR_R |= BOARD_NAND_ADDR_CHIPn;
            this->IO_ADDR_W |= BOARD_NAND_ADDR_CHIPn;
            break;
        }
    }


.. _Hardware_ECC_support:

Hardware ECC support
====================


.. _Functions_and_constants:

Functions and constants
-----------------------

The nand driver supports three different types of hardware ECC.

-  NAND_ECC_HW3_256

   Hardware ECC generator providing 3 bytes ECC per 256 byte.

-  NAND_ECC_HW3_512

   Hardware ECC generator providing 3 bytes ECC per 512 byte.

-  NAND_ECC_HW6_512

   Hardware ECC generator providing 6 bytes ECC per 512 byte.

-  NAND_ECC_HW8_512

   Hardware ECC generator providing 6 bytes ECC per 512 byte.

If your hardware generator has a different functionality add it at the
appropriate place in nand_base.c

The board driver must provide following functions:

-  enable_hwecc

   This function is called before reading / writing to the chip. Reset
   or initialize the hardware generator in this function. The function
   is called with an argument which let you distinguish between read and
   write operations.

-  calculate_ecc

   This function is called after read / write from / to the chip.
   Transfer the ECC from the hardware to the buffer. If the option
   NAND_HWECC_SYNDROME is set then the function is only called on
   write. See below.

-  correct_data

   In case of an ECC error this function is called for error detection
   and correction. Return 1 respectively 2 in case the error can be
   corrected. If the error is not correctable return -1. If your
   hardware generator matches the default algorithm of the nand_ecc
   software generator then use the correction function provided by
   nand_ecc instead of implementing duplicated code.


.. _Hardware_ECC_with_syndrome_calculation:

Hardware ECC with syndrome calculation
--------------------------------------

Many hardware ECC implementations provide Reed-Solomon codes and
calculate an error syndrome on read. The syndrome must be converted to a
standard Reed-Solomon syndrome before calling the error correction code
in the generic Reed-Solomon library.

The ECC bytes must be placed immediately after the data bytes in order
to make the syndrome generator work. This is contrary to the usual
layout used by software ECC. The separation of data and out of band area
is not longer possible. The nand driver code handles this layout and the
remaining free bytes in the oob area are managed by the autoplacement
code. Provide a matching oob-layout in this case. See rts_from4.c and
diskonchip.c for implementation reference. In those cases we must also
use bad block tables on FLASH, because the ECC layout is interfering
with the bad block marker positions. See bad block table support for
details.


.. _Bad_Block_table_support:

Bad block table support
=======================

Most NAND chips mark the bad blocks at a defined position in the spare
area. Those blocks must not be erased under any circumstances as the bad
block information would be lost. It is possible to check the bad block
mark each time when the blocks are accessed by reading the spare area of
the first page in the block. This is time consuming so a bad block table
is used.

The nand driver supports various types of bad block tables.

-  Per device

   The bad block table contains all bad block information of the device
   which can consist of multiple chips.

-  Per chip

   A bad block table is used per chip and contains the bad block
   information for this particular chip.

-  Fixed offset

   The bad block table is located at a fixed offset in the chip
   (device). This applies to various DiskOnChip devices.

-  Automatic placed

   The bad block table is automatically placed and detected either at
   the end or at the beginning of a chip (device)

-  Mirrored tables

   The bad block table is mirrored on the chip (device) to allow updates
   of the bad block table without data loss.

nand_scan() calls the function nand_default_bbt().
nand_default_bbt() selects appropriate default bad block table
descriptors depending on the chip information which was retrieved by
nand_scan().

The standard policy is scanning the device for bad blocks and build a
ram based bad block table which allows faster access than always
checking the bad block information on the flash chip itself.


.. _Flash_based_tables:

Flash based tables
------------------

It may be desired or necessary to keep a bad block table in FLASH. For
AG-AND chips this is mandatory, as they have no factory marked bad
blocks. They have factory marked good blocks. The marker pattern is
erased when the block is erased to be reused. So in case of powerloss
before writing the pattern back to the chip this block would be lost and
added to the bad blocks. Therefore we scan the chip(s) when we detect
them the first time for good blocks and store this information in a bad
block table before erasing any of the blocks.

The blocks in which the tables are stored are protected against
accidental access by marking them bad in the memory bad block table. The
bad block table management functions are allowed to circumvent this
protection.

The simplest way to activate the FLASH based bad block table support is
to set the option NAND_BBT_USE_FLASH in the bbt_option field of the
nand chip structure before calling nand_scan(). For AG-AND chips is
this done by default. This activates the default FLASH based bad block
table functionality of the NAND driver. The default bad block table
options are

-  Store bad block table per chip

-  Use 2 bits per block

-  Automatic placement at the end of the chip

-  Use mirrored tables with version numbers

-  Reserve 4 blocks at the end of the chip


.. _User_defined_tables:

User defined tables
-------------------

User defined tables are created by filling out a nand_bbt_descr
structure and storing the pointer in the nand_chip structure member
bbt_td before calling nand_scan(). If a mirror table is necessary a
second structure must be created and a pointer to this structure must be
stored in bbt_md inside the nand_chip structure. If the bbt_md member
is set to NULL then only the main table is used and no scan for the
mirrored table is performed.

The most important field in the nand_bbt_descr structure is the
options field. The options define most of the table properties. Use the
predefined constants from nand.h to define the options.

-  Number of bits per block

   The supported number of bits is 1, 2, 4, 8.

-  Table per chip

   Setting the constant NAND_BBT_PERCHIP selects that a bad block
   table is managed for each chip in a chip array. If this option is not
   set then a per device bad block table is used.

-  Table location is absolute

   Use the option constant NAND_BBT_ABSPAGE and define the absolute
   page number where the bad block table starts in the field pages. If
   you have selected bad block tables per chip and you have a multi chip
   array then the start page must be given for each chip in the chip
   array. Note: there is no scan for a table ident pattern performed, so
   the fields pattern, veroffs, offs, len can be left uninitialized

-  Table location is automatically detected

   The table can either be located in the first or the last good blocks
   of the chip (device). Set NAND_BBT_LASTBLOCK to place the bad block
   table at the end of the chip (device). The bad block tables are
   marked and identified by a pattern which is stored in the spare area
   of the first page in the block which holds the bad block table. Store
   a pointer to the pattern in the pattern field. Further the length of
   the pattern has to be stored in len and the offset in the spare area
   must be given in the offs member of the nand_bbt_descr structure.
   For mirrored bad block tables different patterns are mandatory.

-  Table creation

   Set the option NAND_BBT_CREATE to enable the table creation if no
   table can be found during the scan. Usually this is done only once if
   a new chip is found.

-  Table write support

   Set the option NAND_BBT_WRITE to enable the table write support.
   This allows the update of the bad block table(s) in case a block has
   to be marked bad due to wear. The MTD interface function
   block_markbad is calling the update function of the bad block table.
   If the write support is enabled then the table is updated on FLASH.

   Note: Write support should only be enabled for mirrored tables with
   version control.

-  Table version control

   Set the option NAND_BBT_VERSION to enable the table version
   control. It's highly recommended to enable this for mirrored tables
   with write support. It makes sure that the risk of losing the bad
   block table information is reduced to the loss of the information
   about the one worn out block which should be marked bad. The version
   is stored in 4 consecutive bytes in the spare area of the device. The
   position of the version number is defined by the member veroffs in
   the bad block table descriptor.

-  Save block contents on write

   In case that the block which holds the bad block table does contain
   other useful information, set the option NAND_BBT_SAVECONTENT. When
   the bad block table is written then the whole block is read the bad
   block table is updated and the block is erased and everything is
   written back. If this option is not set only the bad block table is
   written and everything else in the block is ignored and erased.

-  Number of reserved blocks

   For automatic placement some blocks must be reserved for bad block
   table storage. The number of reserved blocks is defined in the
   maxblocks member of the bad block table description structure.
   Reserving 4 blocks for mirrored tables should be a reasonable number.
   This also limits the number of blocks which are scanned for the bad
   block table ident pattern.


.. _Spare_area_placement:

Spare area (auto)placement
==========================

The nand driver implements different possibilities for placement of
filesystem data in the spare area,

-  Placement defined by fs driver

-  Automatic placement

The default placement function is automatic placement. The nand driver
has built in default placement schemes for the various chiptypes. If due
to hardware ECC functionality the default placement does not fit then
the board driver can provide a own placement scheme.

File system drivers can provide a own placement scheme which is used
instead of the default placement scheme.

Placement schemes are defined by a nand_oobinfo structure


.. code-block:: c

    struct nand_oobinfo {
        int useecc;
        int eccbytes;
        int eccpos[24];
        int oobfree[8][2];
    };

-  useecc

   The useecc member controls the ecc and placement function. The header
   file include/mtd/mtd-abi.h contains constants to select ecc and
   placement. MTD_NANDECC_OFF switches off the ecc complete. This is
   not recommended and available for testing and diagnosis only.
   MTD_NANDECC_PLACE selects caller defined placement,
   MTD_NANDECC_AUTOPLACE selects automatic placement.

-  eccbytes

   The eccbytes member defines the number of ecc bytes per page.

-  eccpos

   The eccpos array holds the byte offsets in the spare area where the
   ecc codes are placed.

-  oobfree

   The oobfree array defines the areas in the spare area which can be
   used for automatic placement. The information is given in the format
   {offset, size}. offset defines the start of the usable area, size the
   length in bytes. More than one area can be defined. The list is
   terminated by an {0, 0} entry.


.. _Placement_defined_by_fs_driver:

Placement defined by fs driver
------------------------------

The calling function provides a pointer to a nand_oobinfo structure
which defines the ecc placement. For writes the caller must provide a
spare area buffer along with the data buffer. The spare area buffer size
is (number of pages) * (size of spare area). For reads the buffer size
is (number of pages) * ((size of spare area) + (number of ecc steps per
page) * sizeof (int)). The driver stores the result of the ecc check for
each tuple in the spare buffer. The storage sequence is

<spare data page 0><ecc result 0>...<ecc result n>

...

<spare data page n><ecc result 0>...<ecc result n>

This is a legacy mode used by YAFFS1.

If the spare area buffer is NULL then only the ECC placement is done
according to the given scheme in the nand_oobinfo structure.


.. _Automatic_placement:

Automatic placement
-------------------

Automatic placement uses the built in defaults to place the ecc bytes in
the spare area. If filesystem data have to be stored / read into the
spare area then the calling function must provide a buffer. The buffer
size per page is determined by the oobfree array in the nand_oobinfo
structure.

If the spare area buffer is NULL then only the ECC placement is done
according to the default builtin scheme.


.. _Spare_area_autoplacement_default:

Spare area autoplacement default schemes
========================================


.. _pagesize_256:

256 byte pagesize
-----------------



.. flat-table::
    :header-rows:  0
    :stub-columns: 0


    -  .. row 1

       -  Offset

       -  Content

       -  Comment

    -  .. row 2

       -  0x00

       -  ECC byte 0

       -  Error correction code byte 0

    -  .. row 3

       -  0x01

       -  ECC byte 1

       -  Error correction code byte 1

    -  .. row 4

       -  0x02

       -  ECC byte 2

       -  Error correction code byte 2

    -  .. row 5

       -  0x03

       -  Autoplace 0

       -  

    -  .. row 6

       -  0x04

       -  Autoplace 1

       -  

    -  .. row 7

       -  0x05

       -  Bad block marker

       -  If any bit in this byte is zero, then this block is bad. This
          applies only to the first page in a block. In the remaining pages
          this byte is reserved

    -  .. row 8

       -  0x06

       -  Autoplace 2

       -  

    -  .. row 9

       -  0x07

       -  Autoplace 3

       -  



.. _pagesize_512:

512 byte pagesize
-----------------



.. flat-table::
    :header-rows:  0
    :stub-columns: 0


    -  .. row 1

       -  Offset

       -  Content

       -  Comment

    -  .. row 2

       -  0x00

       -  ECC byte 0

       -  Error correction code byte 0 of the lower 256 Byte data in this
          page

    -  .. row 3

       -  0x01

       -  ECC byte 1

       -  Error correction code byte 1 of the lower 256 Bytes of data in
          this page

    -  .. row 4

       -  0x02

       -  ECC byte 2

       -  Error correction code byte 2 of the lower 256 Bytes of data in
          this page

    -  .. row 5

       -  0x03

       -  ECC byte 3

       -  Error correction code byte 0 of the upper 256 Bytes of data in
          this page

    -  .. row 6

       -  0x04

       -  reserved

       -  reserved

    -  .. row 7

       -  0x05

       -  Bad block marker

       -  If any bit in this byte is zero, then this block is bad. This
          applies only to the first page in a block. In the remaining pages
          this byte is reserved

    -  .. row 8

       -  0x06

       -  ECC byte 4

       -  Error correction code byte 1 of the upper 256 Bytes of data in
          this page

    -  .. row 9

       -  0x07

       -  ECC byte 5

       -  Error correction code byte 2 of the upper 256 Bytes of data in
          this page

    -  .. row 10

       -  0x08 - 0x0F

       -  Autoplace 0 - 7

       -  



.. _pagesize_2048:

2048 byte pagesize
------------------



.. flat-table::
    :header-rows:  0
    :stub-columns: 0


    -  .. row 1

       -  Offset

       -  Content

       -  Comment

    -  .. row 2

       -  0x00

       -  Bad block marker

       -  If any bit in this byte is zero, then this block is bad. This
          applies only to the first page in a block. In the remaining pages
          this byte is reserved

    -  .. row 3

       -  0x01

       -  Reserved

       -  Reserved

    -  .. row 4

       -  0x02-0x27

       -  Autoplace 0 - 37

       -  

    -  .. row 5

       -  0x28

       -  ECC byte 0

       -  Error correction code byte 0 of the first 256 Byte data in this
          page

    -  .. row 6

       -  0x29

       -  ECC byte 1

       -  Error correction code byte 1 of the first 256 Bytes of data in
          this page

    -  .. row 7

       -  0x2A

       -  ECC byte 2

       -  Error correction code byte 2 of the first 256 Bytes data in this
          page

    -  .. row 8

       -  0x2B

       -  ECC byte 3

       -  Error correction code byte 0 of the second 256 Bytes of data in
          this page

    -  .. row 9

       -  0x2C

       -  ECC byte 4

       -  Error correction code byte 1 of the second 256 Bytes of data in
          this page

    -  .. row 10

       -  0x2D

       -  ECC byte 5

       -  Error correction code byte 2 of the second 256 Bytes of data in
          this page

    -  .. row 11

       -  0x2E

       -  ECC byte 6

       -  Error correction code byte 0 of the third 256 Bytes of data in
          this page

    -  .. row 12

       -  0x2F

       -  ECC byte 7

       -  Error correction code byte 1 of the third 256 Bytes of data in
          this page

    -  .. row 13

       -  0x30

       -  ECC byte 8

       -  Error correction code byte 2 of the third 256 Bytes of data in
          this page

    -  .. row 14

       -  0x31

       -  ECC byte 9

       -  Error correction code byte 0 of the fourth 256 Bytes of data in
          this page

    -  .. row 15

       -  0x32

       -  ECC byte 10

       -  Error correction code byte 1 of the fourth 256 Bytes of data in
          this page

    -  .. row 16

       -  0x33

       -  ECC byte 11

       -  Error correction code byte 2 of the fourth 256 Bytes of data in
          this page

    -  .. row 17

       -  0x34

       -  ECC byte 12

       -  Error correction code byte 0 of the fifth 256 Bytes of data in
          this page

    -  .. row 18

       -  0x35

       -  ECC byte 13

       -  Error correction code byte 1 of the fifth 256 Bytes of data in
          this page

    -  .. row 19

       -  0x36

       -  ECC byte 14

       -  Error correction code byte 2 of the fifth 256 Bytes of data in
          this page

    -  .. row 20

       -  0x37

       -  ECC byte 15

       -  Error correction code byte 0 of the sixt 256 Bytes of data in this
          page

    -  .. row 21

       -  0x38

       -  ECC byte 16

       -  Error correction code byte 1 of the sixt 256 Bytes of data in this
          page

    -  .. row 22

       -  0x39

       -  ECC byte 17

       -  Error correction code byte 2 of the sixt 256 Bytes of data in this
          page

    -  .. row 23

       -  0x3A

       -  ECC byte 18

       -  Error correction code byte 0 of the seventh 256 Bytes of data in
          this page

    -  .. row 24

       -  0x3B

       -  ECC byte 19

       -  Error correction code byte 1 of the seventh 256 Bytes of data in
          this page

    -  .. row 25

       -  0x3C

       -  ECC byte 20

       -  Error correction code byte 2 of the seventh 256 Bytes of data in
          this page

    -  .. row 26

       -  0x3D

       -  ECC byte 21

       -  Error correction code byte 0 of the eighth 256 Bytes of data in
          this page

    -  .. row 27

       -  0x3E

       -  ECC byte 22

       -  Error correction code byte 1 of the eighth 256 Bytes of data in
          this page

    -  .. row 28

       -  0x3F

       -  ECC byte 23

       -  Error correction code byte 2 of the eighth 256 Bytes of data in
          this page




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
