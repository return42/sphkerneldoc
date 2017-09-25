.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/spu_csa.h

.. _`spu_lscsa`:

struct spu_lscsa
================

.. c:type:: struct spu_lscsa

    Local Store Context Save Area.

.. _`spu_lscsa.definition`:

Definition
----------

.. code-block:: c

    struct spu_lscsa {
        struct spu_reg128 gprs[128];
        struct spu_reg128 fpcr;
        struct spu_reg128 decr;
        struct spu_reg128 decr_status;
        struct spu_reg128 ppu_mb;
        struct spu_reg128 ppuint_mb;
        struct spu_reg128 tag_mask;
        struct spu_reg128 event_mask;
        struct spu_reg128 srr0;
        struct spu_reg128 stopped_status;
        unsigned char ls[LS_SIZE] __attribute__((aligned(65536)));
    }

.. _`spu_lscsa.members`:

Members
-------

gprs
    Array of saved registers.

fpcr
    Saved floating point status control register.

decr
    Saved decrementer value.

decr_status
    Indicates software decrementer status flags.

ppu_mb
    Saved PPU mailbox data.

ppuint_mb
    Saved PPU interrupting mailbox data.

tag_mask
    Saved tag group mask.

event_mask
    Saved event mask.

srr0
    Saved SRR0.

stopped_status
    Conditions to be recreated by restore.

ls
    Saved contents of Local Storage Area.

.. _`spu_lscsa.description`:

Description
-----------

The LSCSA represents state that is primarily saved and
restored by SPU-side code.

.. _`spu_state`:

struct spu_state
================

.. c:type:: struct spu_state


.. _`spu_state.definition`:

Definition
----------

.. code-block:: c

    struct spu_state {
        struct spu_lscsa *lscsa;
        struct spu_problem_collapsed prob;
        struct spu_priv1_collapsed priv1;
        struct spu_priv2_collapsed priv2;
        u64 spu_chnlcnt_RW[32];
        u64 spu_chnldata_RW[32];
        u32 spu_mailbox_data[4];
        u32 pu_mailbox_data[1];
        u64 class_0_dar, class_0_pending;
        u64 class_1_dar, class_1_dsisr;
        unsigned long suspend_time;
        spinlock_t register_lock;
    }

.. _`spu_state.members`:

Members
-------

lscsa
    Local Store Context Save Area.

prob
    Collapsed Problem State Area, w/o pads.

priv1
    Collapsed Privileged 1 Area, w/o pads.

priv2
    Collapsed Privileged 2 Area, w/o pads.

spu_chnlcnt_RW
    Array of saved channel counts.

spu_chnldata_RW
    Array of saved channel data.

spu_mailbox_data
    *undescribed*

pu_mailbox_data
    *undescribed*

class_0_dar
    *undescribed*

class_0_pending
    *undescribed*

class_1_dar
    *undescribed*

class_1_dsisr
    *undescribed*

suspend_time
    Time stamp when decrementer disabled.

register_lock
    *undescribed*

.. _`spu_state.description`:

Description
-----------

Structure representing the whole of the SPU
context save area (CSA).  This struct contains
all of the state necessary to suspend and then
later optionally resume execution of an SPU
context.

The \ ``lscsa``\  region is by far the largest, and is
allocated separately so that it may either be
pinned or mapped to/from application memory, as
appropriate for the OS environment.

.. This file was automatic generated / don't edit.

