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
        struct s;
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
        struct s;
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
        struct s;
    }

.. _`zip_inst_s.members`:

Members
-------

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
        struct s;
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
        struct s;
    }

.. _`zip_zptr_s.members`:

Members
-------

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
        struct s;
    }

.. _`zip_zres_s.members`:

Members
-------

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
        struct zip_cmd_ctl_s s;
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
        struct zip_constants_s s;
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
        struct zip_corex_bist_status_s s;
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
        struct zip_ctl_bist_status_s s;
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
        struct zip_ctl_cfg_s s;
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
        struct zip_dbg_corex_inst_s s;
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
        struct zip_dbg_corex_sta_s s;
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
        struct zip_dbg_quex_sta_s s;
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
        struct zip_ecc_ctl_s s;
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
        struct zip_ecce_int_s s;
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
        struct zip_msix_pbax_s s;
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
        struct zip_msix_vecx_addr_s s;
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
        struct zip_msix_vecx_ctl_s s;
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
        struct zip_quex_done_s s;
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
        struct zip_quex_done_ack_s s;
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
        struct zip_quex_done_ena_w1c_s s;
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
        struct zip_quex_done_ena_w1s_s s;
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
        struct zip_quex_done_wait_s s;
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
        struct zip_quex_doorbell_s s;
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
        struct zip_quex_err_int_s s;
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
        struct zip_quex_gcfg_s s;
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
        struct zip_quex_map_s s;
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
        struct zip_quex_sbuf_addr_s s;
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
        struct zip_quex_sbuf_ctl_s s;
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
        struct zip_que_ena_s s;
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
        struct zip_que_pri_s s;
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
        struct zip_throttle_s s;
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

