.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/ps3/spu.c

.. _`spe_type`:

enum spe_type
=============

.. c:type:: enum spe_type

    Type of spe to create.

.. _`spe_type.definition`:

Definition
----------

.. code-block:: c

    enum spe_type {
        SPE_TYPE_LOGICAL
    };

.. _`spe_type.constants`:

Constants
---------

SPE_TYPE_LOGICAL
    *undescribed*

.. _`spe_type.description`:

Description
-----------

For use with \ :c:func:`lv1_construct_logical_spe`\ .  The current HV does not support
any types other than those listed.

.. _`spe_shadow`:

struct spe_shadow
=================

.. c:type:: struct spe_shadow

    logical spe shadow register area.

.. _`spe_shadow.definition`:

Definition
----------

.. code-block:: c

    struct spe_shadow {
        u8 padding_0140;
        u64 int_status_class0_RW;
        u64 int_status_class1_RW;
        u64 int_status_class2_RW;
        u8 padding_0158;
        u64 mfc_dsisr_RW;
        u8 padding_0618;
        u64 mfc_dar_RW;
        u8 padding_0628;
        u64 mfc_dsipr_R;
        u8 padding_0808;
        u64 mfc_lscrr_R;
        u8 padding_0818;
        u64 mfc_cer_R;
        u8 padding_0c08;
        u64 spe_execution_status;
        u8 padding_0f08;
    }

.. _`spe_shadow.members`:

Members
-------

padding_0140
    *undescribed*

int_status_class0_RW
    *undescribed*

int_status_class1_RW
    *undescribed*

int_status_class2_RW
    *undescribed*

padding_0158
    *undescribed*

mfc_dsisr_RW
    *undescribed*

padding_0618
    *undescribed*

mfc_dar_RW
    *undescribed*

padding_0628
    *undescribed*

mfc_dsipr_R
    *undescribed*

padding_0808
    *undescribed*

mfc_lscrr_R
    *undescribed*

padding_0818
    *undescribed*

mfc_cer_R
    *undescribed*

padding_0c08
    *undescribed*

spe_execution_status
    *undescribed*

padding_0f08
    *undescribed*

.. _`spe_shadow.description`:

Description
-----------

Read-only shadow of spe registers.

.. _`spe_ex_state`:

enum spe_ex_state
=================

.. c:type:: enum spe_ex_state

    Logical spe execution state.

.. _`spe_ex_state.definition`:

Definition
----------

.. code-block:: c

    enum spe_ex_state {
        SPE_EX_STATE_UNEXECUTABLE,
        SPE_EX_STATE_EXECUTABLE,
        SPE_EX_STATE_EXECUTED
    };

.. _`spe_ex_state.constants`:

Constants
---------

SPE_EX_STATE_UNEXECUTABLE
    *undescribed*

SPE_EX_STATE_EXECUTABLE
    *undescribed*

SPE_EX_STATE_EXECUTED
    *undescribed*

.. _`spe_ex_state.description`:

Description
-----------

The execution state (status) of the logical spe as reported in
struct spe_shadow:spe_execution_status.

.. _`priv1_cache`:

struct priv1_cache
==================

.. c:type:: struct priv1_cache

    Cached values of priv1 registers.

.. _`priv1_cache.definition`:

Definition
----------

.. code-block:: c

    struct priv1_cache {
        u64 masks;
        u64 sr1;
        u64 tclass_id;
    }

.. _`priv1_cache.members`:

Members
-------

masks
    Array of cached spe interrupt masks, indexed by class.

sr1
    Cached mfc_sr1 register.

tclass_id
    Cached mfc_tclass_id register.

.. _`spu_pdata`:

struct spu_pdata
================

.. c:type:: struct spu_pdata

    Platform state variables.

.. _`spu_pdata.definition`:

Definition
----------

.. code-block:: c

    struct spu_pdata {
        u64 spe_id;
        u64 resource_id;
        u64 priv2_addr;
        u64 shadow_addr;
        struct spe_shadow __iomem *shadow;
        struct priv1_cache cache;
    }

.. _`spu_pdata.members`:

Members
-------

spe_id
    HV spe id returned by \ :c:func:`lv1_construct_logical_spe`\ .

resource_id
    HV spe resource id returned by
    \ :c:func:`ps3_repository_read_spe_resource_id`\ .

priv2_addr
    lpar address of spe priv2 area returned by
    \ :c:func:`lv1_construct_logical_spe`\ .

shadow_addr
    lpar address of spe register shadow area returned by
    \ :c:func:`lv1_construct_logical_spe`\ .

shadow
    Virtual (ioremap) address of spe register shadow area.

cache
    Cached values of priv1 registers.

.. _`setup_areas`:

setup_areas
===========

.. c:function:: int setup_areas(struct spu *spu)

    Map the spu regions into the address space.

    :param struct spu \*spu:
        *undescribed*

.. _`setup_areas.description`:

Description
-----------

The current HV requires the spu shadow regs to be mapped with the
PTE page protection bits set as read-only (PP=3).  This implementation
uses the low level \__ioremap() to bypass the page protection settings
inforced by \ :c:func:`ioremap_prot`\  to get the needed PTE bits set for the
shadow regs.

.. _`ps3_enable_spu`:

ps3_enable_spu
==============

.. c:function:: void ps3_enable_spu(struct spu_context *ctx)

    Enable SPU run control.

    :param struct spu_context \*ctx:
        *undescribed*

.. _`ps3_enable_spu.description`:

Description
-----------

An outstanding enhancement for the PS3 would be to add a guard to check
for incorrect access to the spu problem state when the spu context is
disabled.  This check could be implemented with a flag added to the spu
context that would inhibit mapping problem state pages, and a routine
to unmap spu problem state pages.  When the spu is enabled with
\ :c:func:`ps3_enable_spu`\  the flag would be set allowing pages to be mapped,
and when the spu is disabled with \ :c:func:`ps3_disable_spu`\  the flag would be
cleared and the mapped problem state pages would be unmapped.

.. This file was automatic generated / don't edit.

