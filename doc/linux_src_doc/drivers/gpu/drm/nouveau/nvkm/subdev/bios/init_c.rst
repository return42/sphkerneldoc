.. -*- coding: utf-8; mode: rst -*-

======
init.c
======


.. _`init_reserved`:

init_reserved
=============

.. c:function:: void init_reserved (struct nvbios_init *init)

    stub for various unknown/unused single-byte opcodes

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_done`:

init_done
=========

.. c:function:: void init_done (struct nvbios_init *init)

    opcode 0x71

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_done.description`:

Description
-----------




.. _`init_io_restrict_prog`:

init_io_restrict_prog
=====================

.. c:function:: void init_io_restrict_prog (struct nvbios_init *init)

    opcode 0x32

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_repeat`:

init_repeat
===========

.. c:function:: void init_repeat (struct nvbios_init *init)

    opcode 0x33

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_repeat.description`:

Description
-----------




.. _`init_io_restrict_pll`:

init_io_restrict_pll
====================

.. c:function:: void init_io_restrict_pll (struct nvbios_init *init)

    opcode 0x34

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_end_repeat`:

init_end_repeat
===============

.. c:function:: void init_end_repeat (struct nvbios_init *init)

    opcode 0x36

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_end_repeat.description`:

Description
-----------




.. _`init_copy`:

init_copy
=========

.. c:function:: void init_copy (struct nvbios_init *init)

    opcode 0x37

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_not`:

init_not
========

.. c:function:: void init_not (struct nvbios_init *init)

    opcode 0x38

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_not.description`:

Description
-----------




.. _`init_io_flag_condition`:

init_io_flag_condition
======================

.. c:function:: void init_io_flag_condition (struct nvbios_init *init)

    opcode 0x39

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_generic_condition`:

init_generic_condition
======================

.. c:function:: void init_generic_condition (struct nvbios_init *init)

    opcode 0x3a

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_generic_condition.description`:

Description
-----------




.. _`init_io_mask_or`:

init_io_mask_or
===============

.. c:function:: void init_io_mask_or (struct nvbios_init *init)

    opcode 0x3b

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_io_or`:

init_io_or
==========

.. c:function:: void init_io_or (struct nvbios_init *init)

    opcode 0x3c

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_io_or.description`:

Description
-----------




.. _`init_andn_reg`:

init_andn_reg
=============

.. c:function:: void init_andn_reg (struct nvbios_init *init)

    opcode 0x47

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_or_reg`:

init_or_reg
===========

.. c:function:: void init_or_reg (struct nvbios_init *init)

    opcode 0x48

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_or_reg.description`:

Description
-----------




.. _`init_idx_addr_latched`:

init_idx_addr_latched
=====================

.. c:function:: void init_idx_addr_latched (struct nvbios_init *init)

    opcode 0x49

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_io_restrict_pll2`:

init_io_restrict_pll2
=====================

.. c:function:: void init_io_restrict_pll2 (struct nvbios_init *init)

    opcode 0x4a

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_io_restrict_pll2.description`:

Description
-----------




.. _`init_pll2`:

init_pll2
=========

.. c:function:: void init_pll2 (struct nvbios_init *init)

    opcode 0x4b

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_i2c_byte`:

init_i2c_byte
=============

.. c:function:: void init_i2c_byte (struct nvbios_init *init)

    opcode 0x4c

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_i2c_byte.description`:

Description
-----------




.. _`init_zm_i2c_byte`:

init_zm_i2c_byte
================

.. c:function:: void init_zm_i2c_byte (struct nvbios_init *init)

    opcode 0x4d

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_i2c`:

init_zm_i2c
===========

.. c:function:: void init_zm_i2c (struct nvbios_init *init)

    opcode 0x4e

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_i2c.description`:

Description
-----------




.. _`init_tmds`:

init_tmds
=========

.. c:function:: void init_tmds (struct nvbios_init *init)

    opcode 0x4f

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_tmds_group`:

init_zm_tmds_group
==================

.. c:function:: void init_zm_tmds_group (struct nvbios_init *init)

    opcode 0x50

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_tmds_group.description`:

Description
-----------




.. _`init_cr_idx_adr_latch`:

init_cr_idx_adr_latch
=====================

.. c:function:: void init_cr_idx_adr_latch (struct nvbios_init *init)

    opcode 0x51

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_cr`:

init_cr
=======

.. c:function:: void init_cr (struct nvbios_init *init)

    opcode 0x52

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_cr.description`:

Description
-----------




.. _`init_zm_cr`:

init_zm_cr
==========

.. c:function:: void init_zm_cr (struct nvbios_init *init)

    opcode 0x53

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_cr_group`:

init_zm_cr_group
================

.. c:function:: void init_zm_cr_group (struct nvbios_init *init)

    opcode 0x54

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_cr_group.description`:

Description
-----------




.. _`init_condition_time`:

init_condition_time
===================

.. c:function:: void init_condition_time (struct nvbios_init *init)

    opcode 0x56

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_ltime`:

init_ltime
==========

.. c:function:: void init_ltime (struct nvbios_init *init)

    opcode 0x57

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_ltime.description`:

Description
-----------




.. _`init_zm_reg_sequence`:

init_zm_reg_sequence
====================

.. c:function:: void init_zm_reg_sequence (struct nvbios_init *init)

    opcode 0x58

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_pll_indirect`:

init_pll_indirect
=================

.. c:function:: void init_pll_indirect (struct nvbios_init *init)

    opcode 0x59

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_pll_indirect.description`:

Description
-----------




.. _`init_zm_reg_indirect`:

init_zm_reg_indirect
====================

.. c:function:: void init_zm_reg_indirect (struct nvbios_init *init)

    opcode 0x5a

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_sub_direct`:

init_sub_direct
===============

.. c:function:: void init_sub_direct (struct nvbios_init *init)

    opcode 0x5b

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_sub_direct.description`:

Description
-----------




.. _`init_jump`:

init_jump
=========

.. c:function:: void init_jump (struct nvbios_init *init)

    opcode 0x5c

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_i2c_if`:

init_i2c_if
===========

.. c:function:: void init_i2c_if (struct nvbios_init *init)

    opcode 0x5e

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_i2c_if.description`:

Description
-----------




.. _`init_copy_nv_reg`:

init_copy_nv_reg
================

.. c:function:: void init_copy_nv_reg (struct nvbios_init *init)

    opcode 0x5f

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_index_io`:

init_zm_index_io
================

.. c:function:: void init_zm_index_io (struct nvbios_init *init)

    opcode 0x62

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_index_io.description`:

Description
-----------




.. _`init_compute_mem`:

init_compute_mem
================

.. c:function:: void init_compute_mem (struct nvbios_init *init)

    opcode 0x63

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_reset`:

init_reset
==========

.. c:function:: void init_reset (struct nvbios_init *init)

    opcode 0x65

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_reset.description`:

Description
-----------




.. _`init_configure_mem_clk`:

init_configure_mem_clk
======================

.. c:function:: u16 init_configure_mem_clk (struct nvbios_init *init)

    opcode 0x66

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_configure_clk`:

init_configure_clk
==================

.. c:function:: void init_configure_clk (struct nvbios_init *init)

    opcode 0x67

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_configure_clk.description`:

Description
-----------




.. _`init_configure_preinit`:

init_configure_preinit
======================

.. c:function:: void init_configure_preinit (struct nvbios_init *init)

    opcode 0x68

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_io`:

init_io
=======

.. c:function:: void init_io (struct nvbios_init *init)

    opcode 0x69

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_io.description`:

Description
-----------




.. _`init_sub`:

init_sub
========

.. c:function:: void init_sub (struct nvbios_init *init)

    opcode 0x6b

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_ram_condition`:

init_ram_condition
==================

.. c:function:: void init_ram_condition (struct nvbios_init *init)

    opcode 0x6d

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_ram_condition.description`:

Description
-----------




.. _`init_nv_reg`:

init_nv_reg
===========

.. c:function:: void init_nv_reg (struct nvbios_init *init)

    opcode 0x6e

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_macro`:

init_macro
==========

.. c:function:: void init_macro (struct nvbios_init *init)

    opcode 0x6f

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_macro.description`:

Description
-----------




.. _`init_resume`:

init_resume
===========

.. c:function:: void init_resume (struct nvbios_init *init)

    opcode 0x72

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_strap_condition`:

init_strap_condition
====================

.. c:function:: void init_strap_condition (struct nvbios_init *init)

    opcode 0x73

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_strap_condition.description`:

Description
-----------




.. _`init_time`:

init_time
=========

.. c:function:: void init_time (struct nvbios_init *init)

    opcode 0x74

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_condition`:

init_condition
==============

.. c:function:: void init_condition (struct nvbios_init *init)

    opcode 0x75

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_condition.description`:

Description
-----------




.. _`init_io_condition`:

init_io_condition
=================

.. c:function:: void init_io_condition (struct nvbios_init *init)

    opcode 0x76

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_reg16`:

init_zm_reg16
=============

.. c:function:: void init_zm_reg16 (struct nvbios_init *init)

    opcode 0x77

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_reg16.description`:

Description
-----------




.. _`init_index_io`:

init_index_io
=============

.. c:function:: void init_index_io (struct nvbios_init *init)

    opcode 0x78

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_pll`:

init_pll
========

.. c:function:: void init_pll (struct nvbios_init *init)

    opcode 0x79

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_pll.description`:

Description
-----------




.. _`init_zm_reg`:

init_zm_reg
===========

.. c:function:: void init_zm_reg (struct nvbios_init *init)

    opcode 0x7a

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_ram_restrict_pll`:

init_ram_restrict_pll
=====================

.. c:function:: void init_ram_restrict_pll (struct nvbios_init *init)

    opcde 0x87

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_ram_restrict_pll.description`:

Description
-----------




.. _`init_gpio`:

init_gpio
=========

.. c:function:: void init_gpio (struct nvbios_init *init)

    opcode 0x8e

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_ram_restrict_zm_reg_group`:

init_ram_restrict_zm_reg_group
==============================

.. c:function:: void init_ram_restrict_zm_reg_group (struct nvbios_init *init)

    opcode 0x8f

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_ram_restrict_zm_reg_group.description`:

Description
-----------




.. _`init_copy_zm_reg`:

init_copy_zm_reg
================

.. c:function:: void init_copy_zm_reg (struct nvbios_init *init)

    opcode 0x90

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_reg_group`:

init_zm_reg_group
=================

.. c:function:: void init_zm_reg_group (struct nvbios_init *init)

    opcode 0x91

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_reg_group.description`:

Description
-----------




.. _`init_xlat`:

init_xlat
=========

.. c:function:: void init_xlat (struct nvbios_init *init)

    opcode 0x96

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_mask_add`:

init_zm_mask_add
================

.. c:function:: void init_zm_mask_add (struct nvbios_init *init)

    opcode 0x97

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_mask_add.description`:

Description
-----------




.. _`init_auxch`:

init_auxch
==========

.. c:function:: void init_auxch (struct nvbios_init *init)

    opcode 0x98

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_auxch`:

init_zm_auxch
=============

.. c:function:: void init_zm_auxch (struct nvbios_init *init)

    opcode 0x99

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_zm_auxch.description`:

Description
-----------




.. _`init_i2c_long_if`:

init_i2c_long_if
================

.. c:function:: void init_i2c_long_if (struct nvbios_init *init)

    opcode 0x9a

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_gpio_ne`:

init_gpio_ne
============

.. c:function:: void init_gpio_ne (struct nvbios_init *init)

    opcode 0xa9

    :param struct nvbios_init \*init:

        *undescribed*



.. _`init_gpio_ne.description`:

Description
-----------


