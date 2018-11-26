.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/synopsys_edac.c

.. _`ecc_error_info`:

struct ecc_error_info
=====================

.. c:type:: struct ecc_error_info

    ECC error log information

.. _`ecc_error_info.definition`:

Definition
----------

.. code-block:: c

    struct ecc_error_info {
        u32 row;
        u32 col;
        u32 bank;
        u32 bitpos;
        u32 data;
    }

.. _`ecc_error_info.members`:

Members
-------

row
    Row number

col
    Column number

bank
    Bank number

bitpos
    Bit position

data
    Data causing the error

.. _`synps_ecc_status`:

struct synps_ecc_status
=======================

.. c:type:: struct synps_ecc_status

    ECC status information to report

.. _`synps_ecc_status.definition`:

Definition
----------

.. code-block:: c

    struct synps_ecc_status {
        u32 ce_cnt;
        u32 ue_cnt;
        struct ecc_error_info ceinfo;
        struct ecc_error_info ueinfo;
    }

.. _`synps_ecc_status.members`:

Members
-------

ce_cnt
    Correctable error count

ue_cnt
    Uncorrectable error count

ceinfo
    Correctable error log information

ueinfo
    Uncorrectable error log information

.. _`synps_edac_priv`:

struct synps_edac_priv
======================

.. c:type:: struct synps_edac_priv

    DDR memory controller private instance data

.. _`synps_edac_priv.definition`:

Definition
----------

.. code-block:: c

    struct synps_edac_priv {
        void __iomem *baseaddr;
        char message[SYNPS_EDAC_MSG_SIZE];
        struct synps_ecc_status stat;
        u32 ce_cnt;
        u32 ue_cnt;
    }

.. _`synps_edac_priv.members`:

Members
-------

baseaddr
    Base address of the DDR controller

message
    Buffer for framing the event specific info

stat
    ECC status information

ce_cnt
    Correctable Error count

ue_cnt
    Uncorrectable Error count

.. _`synps_edac_geterror_info`:

synps_edac_geterror_info
========================

.. c:function:: int synps_edac_geterror_info(void __iomem *base, struct synps_ecc_status *p)

    Get the current ecc error info

    :param base:
        Pointer to the base address of the ddr memory controller
    :type base: void __iomem \*

    :param p:
        Pointer to the synopsys ecc status structure
    :type p: struct synps_ecc_status \*

.. _`synps_edac_geterror_info.description`:

Description
-----------

Determines there is any ecc error or not

.. _`synps_edac_geterror_info.return`:

Return
------

one if there is no error otherwise returns zero

.. _`synps_edac_handle_error`:

synps_edac_handle_error
=======================

.. c:function:: void synps_edac_handle_error(struct mem_ctl_info *mci, struct synps_ecc_status *p)

    Handle controller error types CE and UE

    :param mci:
        Pointer to the edac memory controller instance
    :type mci: struct mem_ctl_info \*

    :param p:
        Pointer to the synopsys ecc status structure
    :type p: struct synps_ecc_status \*

.. _`synps_edac_handle_error.description`:

Description
-----------

Handles the controller ECC correctable and un correctable error.

.. _`synps_edac_check`:

synps_edac_check
================

.. c:function:: void synps_edac_check(struct mem_ctl_info *mci)

    Check controller for ECC errors

    :param mci:
        Pointer to the edac memory controller instance
    :type mci: struct mem_ctl_info \*

.. _`synps_edac_check.description`:

Description
-----------

Used to check and post ECC errors. Called by the polling thread

.. _`synps_edac_get_dtype`:

synps_edac_get_dtype
====================

.. c:function:: enum dev_type synps_edac_get_dtype(const void __iomem *base)

    Return the controller memory width

    :param base:
        Pointer to the ddr memory controller base address
    :type base: const void __iomem \*

.. _`synps_edac_get_dtype.description`:

Description
-----------

Get the EDAC device type width appropriate for the current controller
configuration.

.. _`synps_edac_get_dtype.return`:

Return
------

a device type width enumeration.

.. _`synps_edac_get_eccstate`:

synps_edac_get_eccstate
=======================

.. c:function:: bool synps_edac_get_eccstate(void __iomem *base)

    Return the controller ecc enable/disable status

    :param base:
        Pointer to the ddr memory controller base address
    :type base: void __iomem \*

.. _`synps_edac_get_eccstate.description`:

Description
-----------

Get the ECC enable/disable status for the controller

.. _`synps_edac_get_eccstate.return`:

Return
------

a ecc status boolean i.e true/false - enabled/disabled.

.. _`synps_edac_get_memsize`:

synps_edac_get_memsize
======================

.. c:function:: u32 synps_edac_get_memsize( void)

    reads the size of the attached memory device

    :param void:
        no arguments
    :type void: 

.. _`synps_edac_get_memsize.return`:

Return
------

the memory size in bytes

.. _`synps_edac_get_mtype`:

synps_edac_get_mtype
====================

.. c:function:: enum mem_type synps_edac_get_mtype(const void __iomem *base)

    Returns controller memory type

    :param base:
        pointer to the synopsys ecc status structure
    :type base: const void __iomem \*

.. _`synps_edac_get_mtype.description`:

Description
-----------

Get the EDAC memory type appropriate for the current controller
configuration.

.. _`synps_edac_get_mtype.return`:

Return
------

a memory type enumeration.

.. _`synps_edac_init_csrows`:

synps_edac_init_csrows
======================

.. c:function:: int synps_edac_init_csrows(struct mem_ctl_info *mci)

    Initialize the cs row data

    :param mci:
        Pointer to the edac memory controller instance
    :type mci: struct mem_ctl_info \*

.. _`synps_edac_init_csrows.description`:

Description
-----------

Initializes the chip select rows associated with the EDAC memory
controller instance

.. _`synps_edac_init_csrows.return`:

Return
------

Unconditionally 0.

.. _`synps_edac_mc_init`:

synps_edac_mc_init
==================

.. c:function:: int synps_edac_mc_init(struct mem_ctl_info *mci, struct platform_device *pdev)

    Initialize driver instance

    :param mci:
        Pointer to the edac memory controller instance
    :type mci: struct mem_ctl_info \*

    :param pdev:
        Pointer to the platform_device struct
    :type pdev: struct platform_device \*

.. _`synps_edac_mc_init.description`:

Description
-----------

Performs initialization of the EDAC memory controller instance and
related driver-private data associated with the memory controller the
instance is bound to.

.. _`synps_edac_mc_init.return`:

Return
------

Always zero.

.. _`synps_edac_mc_probe`:

synps_edac_mc_probe
===================

.. c:function:: int synps_edac_mc_probe(struct platform_device *pdev)

    Check controller and bind driver

    :param pdev:
        Pointer to the platform_device struct
    :type pdev: struct platform_device \*

.. _`synps_edac_mc_probe.description`:

Description
-----------

Probes a specific controller instance for binding with the driver.

.. _`synps_edac_mc_probe.return`:

Return
------

0 if the controller instance was successfully bound to the
driver; otherwise, < 0 on error.

.. _`synps_edac_mc_remove`:

synps_edac_mc_remove
====================

.. c:function:: int synps_edac_mc_remove(struct platform_device *pdev)

    Unbind driver from controller

    :param pdev:
        Pointer to the platform_device struct
    :type pdev: struct platform_device \*

.. _`synps_edac_mc_remove.return`:

Return
------

Unconditionally 0

.. This file was automatic generated / don't edit.

