.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/prm.h

.. _`prm_reset_src_map`:

struct prm_reset_src_map
========================

.. c:type:: struct prm_reset_src_map

    map register bitshifts to standard bitshifts

.. _`prm_reset_src_map.definition`:

Definition
----------

.. code-block:: c

    struct prm_reset_src_map {
        s8 reg_shift;
        s8 std_shift;
    }

.. _`prm_reset_src_map.members`:

Members
-------

reg_shift
    bitshift in the PRM reset source register

std_shift
    bitshift equivalent in the standard reset source list

.. _`prm_reset_src_map.description`:

Description
-----------

The fields are signed because -1 is used as a terminator.

.. _`prm_ll_data`:

struct prm_ll_data
==================

.. c:type:: struct prm_ll_data

    fn ptrs to per-SoC PRM function implementations

.. _`prm_ll_data.definition`:

Definition
----------

.. code-block:: c

    struct prm_ll_data {
        u32 (*read_reset_sources)(void);
        bool (*was_any_context_lost_old)(u8 part, s16 inst, u16 idx);
        void (*clear_context_loss_flags_old)(u8 part, s16 inst, u16 idx);
        int (*late_init)(void);
        int (*assert_hardreset)(u8 shift, u8 part, s16 prm_mod, u16 offset);
        int (*deassert_hardreset)(u8 shift, u8 st_shift, u8 part, s16 prm_mod,u16 offset, u16 st_offset);
        int (*is_hardreset_asserted)(u8 shift, u8 part, s16 prm_mod,u16 offset);
        void (*reset_system)(void);
        int (*clear_mod_irqs)(s16 module, u8 regs, u32 wkst_mask);
        u32 (*vp_check_txdone)(u8 vp_id);
        void (*vp_clear_txdone)(u8 vp_id);
    }

.. _`prm_ll_data.members`:

Members
-------

read_reset_sources
    ptr to the SoC PRM-specific get_reset_source impl

was_any_context_lost_old
    ptr to the SoC PRM context loss test fn

clear_context_loss_flags_old
    ptr to the SoC PRM context loss flag clear fn

late_init
    ptr to the late init function

assert_hardreset
    ptr to the SoC PRM hardreset assert impl

deassert_hardreset
    ptr to the SoC PRM hardreset deassert impl

is_hardreset_asserted
    *undescribed*

reset_system
    *undescribed*

clear_mod_irqs
    *undescribed*

vp_check_txdone
    *undescribed*

vp_clear_txdone
    *undescribed*

.. _`prm_ll_data.description`:

Description
-----------

XXX \ ``was_any_context_lost_old``\  and \ ``clear_context_loss_flags_old``\  are
deprecated.

.. This file was automatic generated / don't edit.

