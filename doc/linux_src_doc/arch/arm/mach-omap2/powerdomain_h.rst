.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/powerdomain.h

.. _`powerdomain`:

struct powerdomain
==================

.. c:type:: struct powerdomain

    OMAP powerdomain

.. _`powerdomain.definition`:

Definition
----------

.. code-block:: c

    struct powerdomain {
        const char *name;
        union voltdm;
        const s16 prcm_offs;
        const u8 pwrsts;
        const u8 pwrsts_logic_ret;
        const u8 flags;
        const u8 banks;
        const u8 pwrsts_mem_ret[PWRDM_MAX_MEM_BANKS];
        const u8 pwrsts_mem_on[PWRDM_MAX_MEM_BANKS];
        const u8 prcm_partition;
        struct clockdomain  *pwrdm_clkdms[PWRDM_MAX_CLKDMS];
        struct list_head node;
        struct list_head voltdm_node;
        int state;
        unsigned state_counter[PWRDM_MAX_PWRSTS];
        unsigned ret_logic_off_counter;
        unsigned ret_mem_off_counter[PWRDM_MAX_MEM_BANKS];
        spinlock_t _lock;
        unsigned long _lock_flags;
        const u8 pwrstctrl_offs;
        const u8 pwrstst_offs;
        const u32 logicretstate_mask;
        const u32 mem_on_mask[PWRDM_MAX_MEM_BANKS];
        const u32 mem_ret_mask[PWRDM_MAX_MEM_BANKS];
        const u32 mem_pwrst_mask[PWRDM_MAX_MEM_BANKS];
        const u32 mem_retst_mask[PWRDM_MAX_MEM_BANKS];
        #ifdef CONFIG_PM_DEBUG
        s64 timer;
        s64 state_timer[PWRDM_MAX_PWRSTS];
        #endif
    }

.. _`powerdomain.members`:

Members
-------

name
    Powerdomain name

voltdm
    voltagedomain containing this powerdomain

prcm_offs
    the address offset from CM_BASE/PRM_BASE

pwrsts
    Possible powerdomain power states

pwrsts_logic_ret
    Possible logic power states when pwrdm in RETENTION

flags
    Powerdomain flags

banks
    Number of software-controllable memory banks in this powerdomain

pwrsts_mem_ret
    Possible memory bank pwrstates when pwrdm in RETENTION

pwrsts_mem_on
    Possible memory bank pwrstates when pwrdm in ON

prcm_partition
    (OMAP4 only) the PRCM partition ID containing \ ``prcm_offs``\ 

pwrdm_clkdms
    Clockdomains in this powerdomain

node
    list_head linking all powerdomains

voltdm_node
    list_head linking all powerdomains in a voltagedomain

state
    *undescribed*

ret_logic_off_counter
    *undescribed*

_lock
    spinlock used to serialize powerdomain and some clockdomain ops

_lock_flags
    stored flags when \ ``_lock``\  is taken

pwrstctrl_offs
    (AM33XX only) XXX_PWRSTCTRL reg offset from prcm_offs

pwrstst_offs
    (AM33XX only) XXX_PWRSTST reg offset from prcm_offs

logicretstate_mask
    (AM33XX only) mask for logic retention bitfield
    in \ ``pwrstctrl_offs``\ 

mem_on_mask
    (AM33XX only) mask for mem on bitfield in \ ``pwrstctrl_offs``\ 

mem_ret_mask
    (AM33XX only) mask for mem ret bitfield in \ ``pwrstctrl_offs``\ 

mem_pwrst_mask
    (AM33XX only) mask for mem state bitfield in \ ``pwrstst_offs``\ 

mem_retst_mask
    (AM33XX only) mask for mem retention state bitfield
    in \ ``pwrstctrl_offs``\ 

timer
    *undescribed*

.. _`powerdomain.description`:

Description
-----------

\ ``prcm_partition``\  possible values are defined in mach-omap2/prcm44xx.h.

.. _`pwrdm_ops`:

struct pwrdm_ops
================

.. c:type:: struct pwrdm_ops

    Arch specific function implementations

.. _`pwrdm_ops.definition`:

Definition
----------

.. code-block:: c

    struct pwrdm_ops {
        int (*pwrdm_set_next_pwrst)(struct powerdomain *pwrdm, u8 pwrst);
        int (*pwrdm_read_next_pwrst)(struct powerdomain *pwrdm);
        int (*pwrdm_read_pwrst)(struct powerdomain *pwrdm);
        int (*pwrdm_read_prev_pwrst)(struct powerdomain *pwrdm);
        int (*pwrdm_set_logic_retst)(struct powerdomain *pwrdm, u8 pwrst);
        int (*pwrdm_set_mem_onst)(struct powerdomain *pwrdm, u8 bank, u8 pwrst);
        int (*pwrdm_set_mem_retst)(struct powerdomain *pwrdm, u8 bank, u8 pwrst);
        int (*pwrdm_read_logic_pwrst)(struct powerdomain *pwrdm);
        int (*pwrdm_read_prev_logic_pwrst)(struct powerdomain *pwrdm);
        int (*pwrdm_read_logic_retst)(struct powerdomain *pwrdm);
        int (*pwrdm_read_mem_pwrst)(struct powerdomain *pwrdm, u8 bank);
        int (*pwrdm_read_prev_mem_pwrst)(struct powerdomain *pwrdm, u8 bank);
        int (*pwrdm_read_mem_retst)(struct powerdomain *pwrdm, u8 bank);
        int (*pwrdm_clear_all_prev_pwrst)(struct powerdomain *pwrdm);
        int (*pwrdm_enable_hdwr_sar)(struct powerdomain *pwrdm);
        int (*pwrdm_disable_hdwr_sar)(struct powerdomain *pwrdm);
        int (*pwrdm_set_lowpwrstchange)(struct powerdomain *pwrdm);
        int (*pwrdm_wait_transition)(struct powerdomain *pwrdm);
        int (*pwrdm_has_voltdm)(void);
    }

.. _`pwrdm_ops.members`:

Members
-------

pwrdm_set_next_pwrst
    Set the target power state for a pd

pwrdm_read_next_pwrst
    Read the target power state set for a pd

pwrdm_read_pwrst
    Read the current power state of a pd

pwrdm_read_prev_pwrst
    Read the prev power state entered by the pd

pwrdm_set_logic_retst
    Set the logic state in RET for a pd

pwrdm_set_mem_onst
    Set the Memory state in ON for a pd

pwrdm_set_mem_retst
    Set the Memory state in RET for a pd

pwrdm_read_logic_pwrst
    Read the current logic state of a pd

pwrdm_read_prev_logic_pwrst
    Read the previous logic state entered by a pd

pwrdm_read_logic_retst
    Read the logic state in RET for a pd

pwrdm_read_mem_pwrst
    Read the current memory state of a pd

pwrdm_read_prev_mem_pwrst
    Read the previous memory state entered by a pd

pwrdm_read_mem_retst
    Read the memory state in RET for a pd

pwrdm_clear_all_prev_pwrst
    Clear all previous power states logged for a pd

pwrdm_enable_hdwr_sar
    Enable Hardware Save-Restore feature for the pd

pwrdm_disable_hdwr_sar
    Disable Hardware Save-Restore feature for a pd

pwrdm_set_lowpwrstchange
    Enable pd transitions from a shallow to deep sleep

pwrdm_wait_transition
    Wait for a pd state transition to complete

pwrdm_has_voltdm
    Check if a voltdm association is needed

.. _`pwrdm_ops.description`:

Description
-----------

Regarding \ ``pwrdm_set_lowpwrstchange``\ : On the OMAP2 and 3-family
chips, a powerdomain's power state is not allowed to directly
transition from one low-power state (e.g., CSWR) to another
low-power state (e.g., OFF) without first waking up the
powerdomain.  This wastes energy.  So OMAP4 chips support the
ability to transition a powerdomain power state directly from one
low-power state to another.  The function pointed to by
\ ``pwrdm_set_lowpwrstchange``\  is intended to configure the OMAP4
hardware powerdomain state machine to enable this feature.

.. This file was automatic generated / don't edit.

