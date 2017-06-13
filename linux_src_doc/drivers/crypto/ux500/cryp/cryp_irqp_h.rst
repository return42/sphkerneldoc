.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ux500/cryp/cryp_irqp.h

.. _`cryp_register`:

struct cryp_register
====================

.. c:type:: struct cryp_register

    @cr                  - Configuration register \ ``status``\               - Status register \ ``din``\                  - Data input register \ ``din_size``\             - Data input size register \ ``dout``\                 - Data output register \ ``dout_size``\            - Data output size register \ ``dmacr``\                - Dma control register \ ``imsc``\                 - Interrupt mask set/clear register \ ``ris``\                  - Raw interrupt status \ ``mis``\                  - Masked interrupt statu register \ ``key_1_l``\              - Key register 1 L \ ``key_1_r``\              - Key register 1 R \ ``key_2_l``\              - Key register 2 L \ ``key_2_r``\              - Key register 2 R \ ``key_3_l``\              - Key register 3 L \ ``key_3_r``\              - Key register 3 R \ ``key_4_l``\              - Key register 4 L \ ``key_4_r``\              - Key register 4 R \ ``init_vect_0_l``\        - init vector 0 L \ ``init_vect_0_r``\        - init vector 0 R \ ``init_vect_1_l``\        - init vector 1 L \ ``init_vect_1_r``\        - init vector 1 R \ ``cryp_unused1``\         - unused registers \ ``itcr``\                 - Integration test control register \ ``itip``\                 - Integration test input register \ ``itop``\                 - Integration test output register \ ``cryp_unused2``\         - unused registers \ ``periphId0``\            - FE0 CRYP Peripheral Identication Register \ ``periphId1``\            - FE4 \ ``periphId2``\            - FE8 \ ``periphId3``\            - FEC \ ``pcellId0``\             - FF0  CRYP PCell Identication Register \ ``pcellId1``\             - FF4 \ ``pcellId2``\             - FF8 \ ``pcellId3``\             - FFC

.. _`cryp_register.definition`:

Definition
----------

.. code-block:: c

    struct cryp_register {
        u32 cr;
        u32 sr;
        u32 din;
        u32 din_size;
        u32 dout;
        u32 dout_size;
        u32 dmacr;
        u32 imsc;
        u32 ris;
        u32 mis;
        u32 key_1_l;
        u32 key_1_r;
        u32 key_2_l;
        u32 key_2_r;
        u32 key_3_l;
        u32 key_3_r;
        u32 key_4_l;
        u32 key_4_r;
        u32 init_vect_0_l;
        u32 init_vect_0_r;
        u32 init_vect_1_l;
        u32 init_vect_1_r;
        u32 cryp_unused1;
        u32 itcr;
        u32 itip;
        u32 itop;
        u32 cryp_unused2;
        u32 periphId0;
        u32 periphId1;
        u32 periphId2;
        u32 periphId3;
        u32 pcellId0;
        u32 pcellId1;
        u32 pcellId2;
        u32 pcellId3;
    }

.. _`cryp_register.members`:

Members
-------

cr
    *undescribed*

sr
    *undescribed*

din
    *undescribed*

din_size
    *undescribed*

dout
    *undescribed*

dout_size
    *undescribed*

dmacr
    *undescribed*

imsc
    *undescribed*

ris
    *undescribed*

mis
    *undescribed*

key_1_l
    *undescribed*

key_1_r
    *undescribed*

key_2_l
    *undescribed*

key_2_r
    *undescribed*

key_3_l
    *undescribed*

key_3_r
    *undescribed*

key_4_l
    *undescribed*

key_4_r
    *undescribed*

init_vect_0_l
    *undescribed*

init_vect_0_r
    *undescribed*

init_vect_1_l
    *undescribed*

init_vect_1_r
    *undescribed*

cryp_unused1
    *undescribed*

itcr
    *undescribed*

itip
    *undescribed*

itop
    *undescribed*

cryp_unused2
    *undescribed*

periphId0
    *undescribed*

periphId1
    *undescribed*

periphId2
    *undescribed*

periphId3
    *undescribed*

pcellId0
    *undescribed*

pcellId1
    *undescribed*

pcellId2
    *undescribed*

pcellId3
    *undescribed*

.. This file was automatic generated / don't edit.

