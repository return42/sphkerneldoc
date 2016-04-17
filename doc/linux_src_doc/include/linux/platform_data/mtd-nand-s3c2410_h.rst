.. -*- coding: utf-8; mode: rst -*-

==================
mtd-nand-s3c2410.h
==================


.. _`s3c2410_nand_set`:

struct s3c2410_nand_set
=======================

.. c:type:: s3c2410_nand_set

    define a set of one or more nand chips


.. _`s3c2410_nand_set.definition`:

Definition
----------

.. code-block:: c

  struct s3c2410_nand_set {
    unsigned int disable_ecc:1;
    unsigned int flash_bbt:1;
    unsigned int options;
    int nr_chips;
    int nr_partitions;
    char * name;
    int * nr_map;
    struct mtd_partition * partitions;
  };


.. _`s3c2410_nand_set.members`:

Members
-------

:``disable_ecc``:
    Entirely disable ECC - Dangerous

:``flash_bbt``:
    Openmoko u-boot can create a Bad Block Table
    Setting this flag will allow the kernel to
    look for it at boot time and also skip the NAND
    scan.

:``options``:
    Default value to set into 'struct nand_chip' options.

:``nr_chips``:
    Number of chips in this set

:``nr_partitions``:
    Number of partitions pointed to by ``partitions``

:``name``:
    Name of set (optional)

:``nr_map``:
    Map for low-layer logical to physical chip numbers (option)

:``partitions``:
    The mtd partition list




.. _`s3c2410_nand_set.description`:

Description
-----------

define a set of one or more nand chips registered with an unique mtd. Also
allows to pass flag to the underlying NAND layer. 'disable_ecc' will trigger
a warning at boot time.



.. _`s3c_nand_set_platdata`:

s3c_nand_set_platdata
=====================

.. c:function:: void s3c_nand_set_platdata (struct s3c2410_platform_nand *nand)

    register NAND platform data.

    :param struct s3c2410_platform_nand \*nand:
        The NAND platform data to register with s3c_device_nand.



.. _`s3c_nand_set_platdata.description`:

Description
-----------

This function copies the given NAND platform data, ``nand`` and registers
it with the s3c_device_nand. This allows ``nand`` to be __initdata.

