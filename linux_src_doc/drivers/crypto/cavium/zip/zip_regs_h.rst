.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/zip/zip_regs.h

.. _`zip_int_vec_e`:

enum zip_int_vec_e
==================

.. c:type:: enum zip_int_vec_e

    ZIP MSI-X Vector Enumeration, enumerates the MSI-X interrupt vectors.

.. _`zip_int_vec_e.definition`:

Definition
----------

.. code-block:: c

    enum zip_int_vec_e {
        ZIP_INT_VEC_E_ECCE,
        ZIP_INT_VEC_E_FIFE,
        ZIP_INT_VEC_E_QUE0_DONE,
        ZIP_INT_VEC_E_QUE0_ERR,
        ZIP_INT_VEC_E_QUE1_DONE,
        ZIP_INT_VEC_E_QUE1_ERR,
        ZIP_INT_VEC_E_QUE2_DONE,
        ZIP_INT_VEC_E_QUE2_ERR,
        ZIP_INT_VEC_E_QUE3_DONE,
        ZIP_INT_VEC_E_QUE3_ERR,
        ZIP_INT_VEC_E_QUE4_DONE,
        ZIP_INT_VEC_E_QUE4_ERR,
        ZIP_INT_VEC_E_QUE5_DONE,
        ZIP_INT_VEC_E_QUE5_ERR,
        ZIP_INT_VEC_E_QUE6_DONE,
        ZIP_INT_VEC_E_QUE6_ERR,
        ZIP_INT_VEC_E_QUE7_DONE,
        ZIP_INT_VEC_E_QUE7_ERR,
        ZIP_INT_VEC_E_ENUM_LAST
    };

.. _`zip_int_vec_e.constants`:

Constants
---------

ZIP_INT_VEC_E_ECCE
    *undescribed*

ZIP_INT_VEC_E_FIFE
    *undescribed*

ZIP_INT_VEC_E_QUE0_DONE
    *undescribed*

ZIP_INT_VEC_E_QUE0_ERR
    *undescribed*

ZIP_INT_VEC_E_QUE1_DONE
    *undescribed*

ZIP_INT_VEC_E_QUE1_ERR
    *undescribed*

ZIP_INT_VEC_E_QUE2_DONE
    *undescribed*

ZIP_INT_VEC_E_QUE2_ERR
    *undescribed*

ZIP_INT_VEC_E_QUE3_DONE
    *undescribed*

ZIP_INT_VEC_E_QUE3_ERR
    *undescribed*

ZIP_INT_VEC_E_QUE4_DONE
    *undescribed*

ZIP_INT_VEC_E_QUE4_ERR
    *undescribed*

ZIP_INT_VEC_E_QUE5_DONE
    *undescribed*

ZIP_INT_VEC_E_QUE5_ERR
    *undescribed*

ZIP_INT_VEC_E_QUE6_DONE
    *undescribed*

ZIP_INT_VEC_E_QUE6_ERR
    *undescribed*

ZIP_INT_VEC_E_QUE7_DONE
    *undescribed*

ZIP_INT_VEC_E_QUE7_ERR
    *undescribed*

ZIP_INT_VEC_E_ENUM_LAST
    *undescribed*

.. _`zip_zptr_addr_s`:

union zip_zptr_addr_s
=====================

.. c:type:: struct zip_zptr_addr_s

    ZIP Generic Pointer Structure for ADDR.

.. _`zip_zptr_addr_s.definition`:

Definition
----------

.. code-block:: c

    union zip_zptr_addr_s {
        u64 u_reg64;
        struct {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_49_63 : 15;
            u64 addr : 49;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 addr : 49;
            u64 reserved_49_63 : 15;
    #endif
        } s;
    }

.. _`zip_zptr_addr_s.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_zptr_addr_s.description`:

Description
-----------

It is the generic format of pointers in ZIP_INST_S.

.. _`zip_zptr_ctl_s`:

union zip_zptr_ctl_s
====================

.. c:type:: struct zip_zptr_ctl_s

    ZIP Generic Pointer Structure for CTL.

.. _`zip_zptr_ctl_s.definition`:

Definition
----------

.. code-block:: c

    union zip_zptr_ctl_s {
        u64 u_reg64;
        struct {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_112_127 : 16;
            u64 length : 16;
            u64 reserved_67_95 : 29;
            u64 fw : 1;
            u64 nc : 1;
            u64 data_be : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 data_be : 1;
            u64 nc : 1;
            u64 fw : 1;
            u64 reserved_67_95 : 29;
            u64 length : 16;
            u64 reserved_112_127 : 16;
    #endif
        } s;
    }

.. _`zip_zptr_ctl_s.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_zptr_ctl_s.description`:

Description
-----------

It is the generic format of pointers in ZIP_INST_S.

.. _`zip_inst_s`:

union zip_inst_s
================

.. c:type:: struct zip_inst_s

    ZIP Instruction Structure. Each ZIP instruction has 16 words (they are called IWORD0 to IWORD15 within the structure).

.. _`zip_inst_s.definition`:

Definition
----------

.. code-block:: c

    union zip_inst_s {
        u64 u_reg64[16];
        struct {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 doneint : 1;
            u64 reserved_56_62 : 7;
            u64 totaloutputlength : 24;
            u64 reserved_27_31 : 5;
            u64 exn : 3;
            u64 reserved_23_23 : 1;
            u64 exbits : 7;
            u64 reserved_12_15 : 4;
            u64 sf : 1;
            u64 ss : 2;
            u64 cc : 2;
            u64 ef : 1;
            u64 bf : 1;
            u64 ce : 1;
            u64 reserved_3_3 : 1;
            u64 ds : 1;
            u64 dg : 1;
            u64 hg : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 hg : 1;
            u64 dg : 1;
            u64 ds : 1;
            u64 reserved_3_3 : 1;
            u64 ce : 1;
            u64 bf : 1;
            u64 ef : 1;
            u64 cc : 2;
            u64 ss : 2;
            u64 sf : 1;
            u64 reserved_12_15 : 4;
            u64 exbits : 7;
            u64 reserved_23_23 : 1;
            u64 exn : 3;
            u64 reserved_27_31 : 5;
            u64 totaloutputlength : 24;
            u64 reserved_56_62 : 7;
            u64 doneint : 1;
    #endif
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 historylength : 16;
            u64 reserved_96_111 : 16;
            u64 adlercrc32 : 32;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 adlercrc32 : 32;
            u64 reserved_96_111 : 16;
            u64 historylength : 16;
    #endif
            union zip_zptr_addr_s ctx_ptr_addr;
            union zip_zptr_ctl_s ctx_ptr_ctl;
            union zip_zptr_addr_s his_ptr_addr;
            union zip_zptr_ctl_s his_ptr_ctl;
            union zip_zptr_addr_s inp_ptr_addr;
            union zip_zptr_ctl_s inp_ptr_ctl;
            union zip_zptr_addr_s out_ptr_addr;
            union zip_zptr_ctl_s out_ptr_ctl;
            union zip_zptr_addr_s res_ptr_addr;
            union zip_zptr_ctl_s res_ptr_ctl;
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_817_831 : 15;
            u64 wq_ptr : 49;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 wq_ptr : 49;
            u64 reserved_817_831 : 15;
    #endif
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_882_895 : 14;
            u64 tt : 2;
            u64 reserved_874_879 : 6;
            u64 grp : 10;
            u64 tag : 32;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 tag : 32;
            u64 grp : 10;
            u64 reserved_874_879 : 6;
            u64 tt : 2;
            u64 reserved_882_895 : 14;
    #endif
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_896_959 : 64;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 reserved_896_959 : 64;
    #endif
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_960_1023 : 64;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 reserved_960_1023 : 64;
    #endif
        } s;
    }

.. _`zip_inst_s.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_nptr_s`:

union zip_nptr_s
================

.. c:type:: struct zip_nptr_s

    ZIP Instruction Next-Chunk-Buffer Pointer (NPTR) Structure

.. _`zip_nptr_s.definition`:

Definition
----------

.. code-block:: c

    union zip_nptr_s {
        u64 u_reg64;
        struct {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_49_63 : 15;
            u64 addr : 49;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 addr : 49;
            u64 reserved_49_63 : 15;
    #endif
        } s;
    }

.. _`zip_nptr_s.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_nptr_s.description`:

Description
-----------

ZIP_NPTR structure is used to chain all the zip instruction buffers
together. ZIP instruction buffers are managed (allocated and released) by
the software.

.. _`zip_zptr_s`:

union zip_zptr_s
================

.. c:type:: struct zip_zptr_s

    ZIP Generic Pointer Structure.

.. _`zip_zptr_s.definition`:

Definition
----------

.. code-block:: c

    union zip_zptr_s {
        u64 u_reg64[2];
        struct {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_49_63 : 15;
            u64 addr : 49;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 addr : 49;
            u64 reserved_49_63 : 15;
    #endif
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_112_127 : 16;
            u64 length : 16;
            u64 reserved_67_95 : 29;
            u64 fw : 1;
            u64 nc : 1;
            u64 data_be : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 data_be : 1;
            u64 nc : 1;
            u64 fw : 1;
            u64 reserved_67_95 : 29;
            u64 length : 16;
            u64 reserved_112_127 : 16;
    #endif
        } s;
    }

.. _`zip_zptr_s.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_zptr_s.description`:

Description
-----------

It is the generic format of pointers in ZIP_INST_S.

.. _`zip_zres_s`:

union zip_zres_s
================

.. c:type:: struct zip_zres_s

    ZIP Result Structure

.. _`zip_zres_s.definition`:

Definition
----------

.. code-block:: c

    union zip_zres_s {
        u64 u_reg64[3];
        struct {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 crc32 : 32;
            u64 adler32 : 32;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 adler32 : 32;
            u64 crc32 : 32;
    #endif
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 totalbyteswritten : 32;
            u64 totalbytesread : 32;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 totalbytesread : 32;
            u64 totalbyteswritten : 32;
    #endif
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 totalbitsprocessed : 32;
            u64 doneint : 1;
            u64 reserved_155_158 : 4;
            u64 exn : 3;
            u64 reserved_151_151 : 1;
            u64 exbits : 7;
            u64 reserved_137_143 : 7;
            u64 ef : 1;
            volatile u64 compcode : 8;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            volatile u64 compcode : 8;
            u64 ef : 1;
            u64 reserved_137_143 : 7;
            u64 exbits : 7;
            u64 reserved_151_151 : 1;
            u64 exn : 3;
            u64 reserved_155_158 : 4;
            u64 doneint : 1;
            u64 totalbitsprocessed : 32;
    #endif
        } s;
    }

.. _`zip_zres_s.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_zres_s.description`:

Description
-----------

The ZIP coprocessor writes the result structure after it completes the
invocation. The result structure is exactly 24 bytes, and each invocation of
the ZIP coprocessor produces exactly one result structure.

.. _`zip_cmd_ctl`:

union zip_cmd_ctl
=================

.. c:type:: struct zip_cmd_ctl

    Structure representing the register that controls clock and reset.

.. _`zip_cmd_ctl.definition`:

Definition
----------

.. code-block:: c

    union zip_cmd_ctl {
        u64 u_reg64;
        struct zip_cmd_ctl_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_2_63 : 62;
            u64 forceclk : 1;
            u64 reset : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 reset : 1;
            u64 forceclk : 1;
            u64 reserved_2_63 : 62;
    #endif
        } s;
    }

.. _`zip_cmd_ctl.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_constants`:

union zip_constants
===================

.. c:type:: struct zip_constants

    Data structure representing the register that contains all of the current implementation-related parameters of the zip core in this chip.

.. _`zip_constants.definition`:

Definition
----------

.. code-block:: c

    union zip_constants {
        u64 u_reg64;
        struct zip_constants_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 nexec : 8;
            u64 reserved_49_55 : 7;
            u64 syncflush_capable : 1;
            u64 depth : 16;
            u64 onfsize : 12;
            u64 ctxsize : 12;
            u64 reserved_1_7 : 7;
            u64 disabled : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 disabled : 1;
            u64 reserved_1_7 : 7;
            u64 ctxsize : 12;
            u64 onfsize : 12;
            u64 depth : 16;
            u64 syncflush_capable : 1;
            u64 reserved_49_55 : 7;
            u64 nexec : 8;
    #endif
        } s;
    }

.. _`zip_constants.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_corex_bist_status`:

union zip_corex_bist_status
===========================

.. c:type:: struct zip_corex_bist_status

    Represents registers which have the BIST status of memories in zip cores.

.. _`zip_corex_bist_status.definition`:

Definition
----------

.. code-block:: c

    union zip_corex_bist_status {
        u64 u_reg64;
        struct zip_corex_bist_status_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_53_63 : 11;
            u64 bstatus : 53;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 bstatus : 53;
            u64 reserved_53_63 : 11;
    #endif
        } s;
    }

.. _`zip_corex_bist_status.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_corex_bist_status.description`:

Description
-----------

Each bit is the BIST result of an individual memory
(per bit, 0 = pass and 1 = fail).

.. _`zip_ctl_bist_status`:

union zip_ctl_bist_status
=========================

.. c:type:: struct zip_ctl_bist_status

    Represents register that has the BIST status of memories in ZIP_CTL (instruction buffer, G/S pointer FIFO, input data buffer, output data buffers).

.. _`zip_ctl_bist_status.definition`:

Definition
----------

.. code-block:: c

    union zip_ctl_bist_status {
        u64 u_reg64;
        struct zip_ctl_bist_status_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_9_63 : 55;
            u64 bstatus : 9;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 bstatus : 9;
            u64 reserved_9_63 : 55;
    #endif
        } s;
    }

.. _`zip_ctl_bist_status.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_ctl_bist_status.description`:

Description
-----------

Each bit is the BIST result of an individual memory
(per bit, 0 = pass and 1 = fail).

.. _`zip_ctl_cfg`:

union zip_ctl_cfg
=================

.. c:type:: struct zip_ctl_cfg

    Represents the register that controls the behavior of the ZIP DMA engines.

.. _`zip_ctl_cfg.definition`:

Definition
----------

.. code-block:: c

    union zip_ctl_cfg {
        u64 u_reg64;
        struct zip_ctl_cfg_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_52_63 : 12;
            u64 ildf : 4;
            u64 reserved_36_47 : 12;
            u64 drtf : 4;
            u64 reserved_27_31 : 5;
            u64 stcf : 3;
            u64 reserved_19_23 : 5;
            u64 ldf : 3;
            u64 reserved_2_15 : 14;
            u64 busy : 1;
            u64 reserved_0_0 : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 reserved_0_0 : 1;
            u64 busy : 1;
            u64 reserved_2_15 : 14;
            u64 ldf : 3;
            u64 reserved_19_23 : 5;
            u64 stcf : 3;
            u64 reserved_27_31 : 5;
            u64 drtf : 4;
            u64 reserved_36_47 : 12;
            u64 ildf : 4;
            u64 reserved_52_63 : 12;
    #endif
        } s;
    }

.. _`zip_ctl_cfg.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_ctl_cfg.description`:

Description
-----------

It is recommended to keep default values for normal operation. Changing the
values of the fields may be useful for diagnostics.

.. _`zip_dbg_corex_inst`:

union zip_dbg_corex_inst
========================

.. c:type:: struct zip_dbg_corex_inst

    Represents the registers that reflect the status of the current instruction that the ZIP core is executing or has executed.

.. _`zip_dbg_corex_inst.definition`:

Definition
----------

.. code-block:: c

    union zip_dbg_corex_inst {
        u64 u_reg64;
        struct zip_dbg_corex_inst_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 busy : 1;
            u64 reserved_35_62 : 28;
            u64 qid : 3;
            u64 iid : 32;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 iid : 32;
            u64 qid : 3;
            u64 reserved_35_62 : 28;
            u64 busy : 1;
    #endif
        } s;
    }

.. _`zip_dbg_corex_inst.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_dbg_corex_inst.description`:

Description
-----------

These registers are only for debug use.

.. _`zip_dbg_corex_sta`:

union zip_dbg_corex_sta
=======================

.. c:type:: struct zip_dbg_corex_sta

    Represents registers that reflect the status of the zip cores.

.. _`zip_dbg_corex_sta.definition`:

Definition
----------

.. code-block:: c

    union zip_dbg_corex_sta {
        u64 u_reg64;
        struct zip_dbg_corex_sta_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 busy : 1;
            u64 reserved_37_62 : 26;
            u64 ist : 5;
            u64 nie : 32;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 nie : 32;
            u64 ist : 5;
            u64 reserved_37_62 : 26;
            u64 busy : 1;
    #endif
        } s;
    }

.. _`zip_dbg_corex_sta.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_dbg_corex_sta.description`:

Description
-----------

They are for debug use only.

.. _`zip_dbg_quex_sta`:

union zip_dbg_quex_sta
======================

.. c:type:: struct zip_dbg_quex_sta

    Represets registers that reflect status of the zip instruction queues.

.. _`zip_dbg_quex_sta.definition`:

Definition
----------

.. code-block:: c

    union zip_dbg_quex_sta {
        u64 u_reg64;
        struct zip_dbg_quex_sta_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 busy : 1;
            u64 reserved_56_62 : 7;
            u64 rqwc : 24;
            u64 nii : 32;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 nii : 32;
            u64 rqwc : 24;
            u64 reserved_56_62 : 7;
            u64 busy : 1;
    #endif
        } s;
    }

.. _`zip_dbg_quex_sta.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_dbg_quex_sta.description`:

Description
-----------

They are for debug use only.

.. _`zip_ecc_ctl`:

union zip_ecc_ctl
=================

.. c:type:: struct zip_ecc_ctl

    Represents the register that enables ECC for each individual internal memory that requires ECC.

.. _`zip_ecc_ctl.definition`:

Definition
----------

.. code-block:: c

    union zip_ecc_ctl {
        u64 u_reg64;
        struct zip_ecc_ctl_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_19_63 : 45;
            u64 vmem_cdis : 1;
            u64 vmem_fs : 2;
            u64 reserved_15_15 : 1;
            u64 idf1_cdis : 1;
            u64 idf1_fs : 2;
            u64 reserved_11_11 : 1;
            u64 idf0_cdis : 1;
            u64 idf0_fs : 2;
            u64 reserved_7_7 : 1;
            u64 gspf_cdis : 1;
            u64 gspf_fs : 2;
            u64 reserved_3_3 : 1;
            u64 iqf_cdis : 1;
            u64 iqf_fs : 2;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 iqf_fs : 2;
            u64 iqf_cdis : 1;
            u64 reserved_3_3 : 1;
            u64 gspf_fs : 2;
            u64 gspf_cdis : 1;
            u64 reserved_7_7 : 1;
            u64 idf0_fs : 2;
            u64 idf0_cdis : 1;
            u64 reserved_11_11 : 1;
            u64 idf1_fs : 2;
            u64 idf1_cdis : 1;
            u64 reserved_15_15 : 1;
            u64 vmem_fs : 2;
            u64 vmem_cdis : 1;
            u64 reserved_19_63 : 45;
    #endif
        } s;
    }

.. _`zip_ecc_ctl.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_ecc_ctl.description`:

Description
-----------

For debug purpose, it can also flip one or two bits in the ECC data.

.. _`zip_ecce_int`:

union zip_ecce_int
==================

.. c:type:: struct zip_ecce_int

    Represents the register that contains the status of the ECC interrupt sources.

.. _`zip_ecce_int.definition`:

Definition
----------

.. code-block:: c

    union zip_ecce_int {
        u64 u_reg64;
        struct zip_ecce_int_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_37_63 : 27;
            u64 dbe : 5;
            u64 reserved_5_31 : 27;
            u64 sbe : 5;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 sbe : 5;
            u64 reserved_5_31 : 27;
            u64 dbe : 5;
            u64 reserved_37_63 : 27;
    #endif
        } s;
    }

.. _`zip_ecce_int.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_msix_pbax`:

union zip_msix_pbax
===================

.. c:type:: struct zip_msix_pbax

    Represents the register that is the MSI-X PBA table

.. _`zip_msix_pbax.definition`:

Definition
----------

.. code-block:: c

    union zip_msix_pbax {
        u64 u_reg64;
        struct zip_msix_pbax_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 pend : 64;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 pend : 64;
    #endif
        } s;
    }

.. _`zip_msix_pbax.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_msix_pbax.description`:

Description
-----------

The bit number is indexed by the ZIP_INT_VEC_E enumeration.

.. _`zip_msix_vecx_addr`:

union zip_msix_vecx_addr
========================

.. c:type:: struct zip_msix_vecx_addr

    Represents the register that is the MSI-X vector table, indexed by the ZIP_INT_VEC_E enumeration.

.. _`zip_msix_vecx_addr.definition`:

Definition
----------

.. code-block:: c

    union zip_msix_vecx_addr {
        u64 u_reg64;
        struct zip_msix_vecx_addr_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_49_63 : 15;
            u64 addr : 47;
            u64 reserved_1_1 : 1;
            u64 secvec : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 secvec : 1;
            u64 reserved_1_1 : 1;
            u64 addr : 47;
            u64 reserved_49_63 : 15;
    #endif
        } s;
    }

.. _`zip_msix_vecx_addr.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_msix_vecx_ctl`:

union zip_msix_vecx_ctl
=======================

.. c:type:: struct zip_msix_vecx_ctl

    Represents the register that is the MSI-X vector table, indexed by the ZIP_INT_VEC_E enumeration.

.. _`zip_msix_vecx_ctl.definition`:

Definition
----------

.. code-block:: c

    union zip_msix_vecx_ctl {
        u64 u_reg64;
        struct zip_msix_vecx_ctl_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_33_63 : 31;
            u64 mask : 1;
            u64 reserved_20_31 : 12;
            u64 data : 20;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 data : 20;
            u64 reserved_20_31 : 12;
            u64 mask : 1;
            u64 reserved_33_63 : 31;
    #endif
        } s;
    }

.. _`zip_msix_vecx_ctl.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_done`:

union zip_quex_done
===================

.. c:type:: struct zip_quex_done

    Represents the registers that contain the per-queue instruction done count.

.. _`zip_quex_done.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_done {
        u64 u_reg64;
        struct zip_quex_done_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_20_63 : 44;
            u64 done : 20;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 done : 20;
            u64 reserved_20_63 : 44;
    #endif
        } s;
    }

.. _`zip_quex_done.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_done_ack`:

union zip_quex_done_ack
=======================

.. c:type:: struct zip_quex_done_ack

    Represents the registers on write to which will decrement the per-queue instructiona done count.

.. _`zip_quex_done_ack.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_done_ack {
        u64 u_reg64;
        struct zip_quex_done_ack_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_20_63 : 44;
            u64 done_ack : 20;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 done_ack : 20;
            u64 reserved_20_63 : 44;
    #endif
        } s;
    }

.. _`zip_quex_done_ack.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_done_ena_w1c`:

union zip_quex_done_ena_w1c
===========================

.. c:type:: struct zip_quex_done_ena_w1c

    Represents the register which when written 1 to will disable the DONEINT interrupt for the queue.

.. _`zip_quex_done_ena_w1c.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_done_ena_w1c {
        u64 u_reg64;
        struct zip_quex_done_ena_w1c_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_1_63 : 63;
            u64 done_ena : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 done_ena : 1;
            u64 reserved_1_63 : 63;
    #endif
        } s;
    }

.. _`zip_quex_done_ena_w1c.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_done_ena_w1s`:

union zip_quex_done_ena_w1s
===========================

.. c:type:: struct zip_quex_done_ena_w1s

    Represents the register that when written 1 to will enable the DONEINT interrupt for the queue.

.. _`zip_quex_done_ena_w1s.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_done_ena_w1s {
        u64 u_reg64;
        struct zip_quex_done_ena_w1s_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_1_63 : 63;
            u64 done_ena : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 done_ena : 1;
            u64 reserved_1_63 : 63;
    #endif
        } s;
    }

.. _`zip_quex_done_ena_w1s.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_done_wait`:

union zip_quex_done_wait
========================

.. c:type:: struct zip_quex_done_wait

    Represents the register that specifies the per queue interrupt coalescing settings.

.. _`zip_quex_done_wait.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_done_wait {
        u64 u_reg64;
        struct zip_quex_done_wait_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_48_63 : 16;
            u64 time_wait : 16;
            u64 reserved_20_31 : 12;
            u64 num_wait : 20;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 num_wait : 20;
            u64 reserved_20_31 : 12;
            u64 time_wait : 16;
            u64 reserved_48_63 : 16;
    #endif
        } s;
    }

.. _`zip_quex_done_wait.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_doorbell`:

union zip_quex_doorbell
=======================

.. c:type:: struct zip_quex_doorbell

    Represents doorbell registers for the ZIP instruction queues.

.. _`zip_quex_doorbell.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_doorbell {
        u64 u_reg64;
        struct zip_quex_doorbell_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_20_63 : 44;
            u64 dbell_cnt : 20;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 dbell_cnt : 20;
            u64 reserved_20_63 : 44;
    #endif
        } s;
    }

.. _`zip_quex_doorbell.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_err_int`:

union zip_quex_err_int
======================

.. c:type:: struct zip_quex_err_int

    Represents registers that contain the per-queue error interrupts.

.. _`zip_quex_err_int.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_err_int {
        u64 u_reg64;
        struct zip_quex_err_int_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_5_63 : 59;
            u64 mdbe : 1;
            u64 nwrp : 1;
            u64 nrrp : 1;
            u64 irde : 1;
            u64 dovf : 1;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 dovf : 1;
            u64 irde : 1;
            u64 nrrp : 1;
            u64 nwrp : 1;
            u64 mdbe : 1;
            u64 reserved_5_63 : 59;
    #endif
        } s;
    }

.. _`zip_quex_err_int.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_gcfg`:

union zip_quex_gcfg
===================

.. c:type:: struct zip_quex_gcfg

    Represents the registers that reflect status of the zip instruction queues,debug use only.

.. _`zip_quex_gcfg.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_gcfg {
        u64 u_reg64;
        struct zip_quex_gcfg_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_4_63 : 60;
            u64 iqb_ldwb : 1;
            u64 cbw_sty : 1;
            u64 l2ld_cmd : 2;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 l2ld_cmd : 2;
            u64 cbw_sty : 1;
            u64 iqb_ldwb : 1;
            u64 reserved_4_63 : 60;
    #endif
        } s;
    }

.. _`zip_quex_gcfg.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_map`:

union zip_quex_map
==================

.. c:type:: struct zip_quex_map

    Represents the registers that control how each instruction queue maps to zip cores.

.. _`zip_quex_map.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_map {
        u64 u_reg64;
        struct zip_quex_map_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_2_63 : 62;
            u64 zce : 2;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 zce : 2;
            u64 reserved_2_63 : 62;
    #endif
        } s;
    }

.. _`zip_quex_map.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_sbuf_addr`:

union zip_quex_sbuf_addr
========================

.. c:type:: struct zip_quex_sbuf_addr

    Represents the registers that set the buffer parameters for the instruction queues.

.. _`zip_quex_sbuf_addr.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_sbuf_addr {
        u64 u_reg64;
        struct zip_quex_sbuf_addr_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_49_63 : 15;
            u64 ptr : 42;
            u64 off : 7;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 off : 7;
            u64 ptr : 42;
            u64 reserved_49_63 : 15;
    #endif
        } s;
    }

.. _`zip_quex_sbuf_addr.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_sbuf_addr.description`:

Description
-----------

When quiescent (i.e. outstanding doorbell count is 0), it is safe to rewrite
this register to effectively reset the command buffer state machine.
These registers must be programmed after SW programs the corresponding
ZIP_QUE(0..7)_SBUF_CTL.

.. _`zip_quex_sbuf_ctl`:

union zip_quex_sbuf_ctl
=======================

.. c:type:: struct zip_quex_sbuf_ctl

    Represents the registers that set the buffer parameters for the instruction queues.

.. _`zip_quex_sbuf_ctl.definition`:

Definition
----------

.. code-block:: c

    union zip_quex_sbuf_ctl {
        u64 u_reg64;
        struct zip_quex_sbuf_ctl_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_45_63 : 19;
            u64 size : 13;
            u64 inst_be : 1;
            u64 reserved_24_30 : 7;
            u64 stream_id : 8;
            u64 reserved_12_15 : 4;
            u64 aura : 12;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 aura : 12;
            u64 reserved_12_15 : 4;
            u64 stream_id : 8;
            u64 reserved_24_30 : 7;
            u64 inst_be : 1;
            u64 size : 13;
            u64 reserved_45_63 : 19;
    #endif
        } s;
    }

.. _`zip_quex_sbuf_ctl.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_quex_sbuf_ctl.description`:

Description
-----------

When quiescent (i.e. outstanding doorbell count is 0), it is safe to rewrite
this register to effectively reset the command buffer state machine.
These registers must be programmed before SW programs the corresponding
ZIP_QUE(0..7)_SBUF_ADDR.

.. _`zip_que_ena`:

union zip_que_ena
=================

.. c:type:: struct zip_que_ena

    Represents queue enable register

.. _`zip_que_ena.definition`:

Definition
----------

.. code-block:: c

    union zip_que_ena {
        u64 u_reg64;
        struct zip_que_ena_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_8_63 : 56;
            u64 ena : 8;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 ena : 8;
            u64 reserved_8_63 : 56;
    #endif
        } s;
    }

.. _`zip_que_ena.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_que_ena.description`:

Description
-----------

If a queue is disabled, ZIP_CTL stops fetching instructions from the queue.

.. _`zip_que_pri`:

union zip_que_pri
=================

.. c:type:: struct zip_que_pri

    Represents the register that defines the priority between instruction queues.

.. _`zip_que_pri.definition`:

Definition
----------

.. code-block:: c

    union zip_que_pri {
        u64 u_reg64;
        struct zip_que_pri_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_8_63 : 56;
            u64 pri : 8;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 pri : 8;
            u64 reserved_8_63 : 56;
    #endif
        } s;
    }

.. _`zip_que_pri.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_throttle`:

union zip_throttle
==================

.. c:type:: struct zip_throttle

    Represents the register that controls the maximum number of in-flight X2I data fetch transactions.

.. _`zip_throttle.definition`:

Definition
----------

.. code-block:: c

    union zip_throttle {
        u64 u_reg64;
        struct zip_throttle_s {
    #if defined(__BIG_ENDIAN_BITFIELD)
            u64 reserved_6_63 : 58;
            u64 ld_infl : 6;
    #elif defined(__LITTLE_ENDIAN_BITFIELD)
            u64 ld_infl : 6;
            u64 reserved_6_63 : 58;
    #endif
        } s;
    }

.. _`zip_throttle.members`:

Members
-------

u_reg64
    *undescribed*

s
    *undescribed*

.. _`zip_throttle.description`:

Description
-----------

Writing 0 to this register causes the ZIP module to temporarily suspend NCB
accesses; it is not recommended for normal operation, but may be useful for
diagnostics.

.. This file was automatic generated / don't edit.

