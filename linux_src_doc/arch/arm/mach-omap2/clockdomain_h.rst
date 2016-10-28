.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/clockdomain.h

.. _`clkdm_autodep`:

struct clkdm_autodep
====================

.. c:type:: struct clkdm_autodep

    clkdm deps to add when entering/exiting hwsup mode

.. _`clkdm_autodep.definition`:

Definition
----------

.. code-block:: c

    struct clkdm_autodep {
        union clkdm;
    }

.. _`clkdm_autodep.members`:

Members
-------

clkdm
    clockdomain to add wkdep+sleepdep on - set name member only

.. _`clkdm_autodep.description`:

Description
-----------

A clockdomain that should have wkdeps and sleepdeps added when a
clockdomain should stay active in hwsup mode; and conversely,
removed when the clockdomain should be allowed to go inactive in
hwsup mode.

Autodeps are deprecated and should be removed after
omap_hwmod-based fine-grained module idle control is added.

.. _`clkdm_dep`:

struct clkdm_dep
================

.. c:type:: struct clkdm_dep

    encode dependencies between clockdomains

.. _`clkdm_dep.definition`:

Definition
----------

.. code-block:: c

    struct clkdm_dep {
        const char *clkdm_name;
        struct clockdomain *clkdm;
        s16 wkdep_usecount;
        s16 sleepdep_usecount;
    }

.. _`clkdm_dep.members`:

Members
-------

clkdm_name
    clockdomain name

clkdm
    pointer to the struct clockdomain of \ ``clkdm_name``\ 

wkdep_usecount
    Number of wakeup dependencies causing this clkdm to wake

sleepdep_usecount
    Number of sleep deps that could prevent clkdm from idle

.. _`clkdm_dep.description`:

Description
-----------

Statically defined.  \ ``clkdm``\  is resolved from \ ``clkdm_name``\  at runtime and
should not be pre-initialized.

XXX Should also include hardware (fixed) dependencies.

.. _`clockdomain`:

struct clockdomain
==================

.. c:type:: struct clockdomain

    OMAP clockdomain

.. _`clockdomain.definition`:

Definition
----------

.. code-block:: c

    struct clockdomain {
        const char *name;
        union pwrdm;
        const u16 clktrctrl_mask;
        const u8 flags;
        u8 _flags;
        const u8 dep_bit;
        const u8 prcm_partition;
        const u16 cm_inst;
        const u16 clkdm_offs;
        struct clkdm_dep *wkdep_srcs;
        struct clkdm_dep *sleepdep_srcs;
        int usecount;
        struct list_head node;
    }

.. _`clockdomain.members`:

Members
-------

name
    clockdomain name

pwrdm
    powerdomain containing this clockdomain

clktrctrl_mask
    CLKTRCTRL/AUTOSTATE field mask in CM_CLKSTCTRL reg

flags
    Clockdomain capability flags

_flags
    Flags for use only by internal clockdomain code

dep_bit
    Bit shift of this clockdomain's PM_WKDEP/CM_SLEEPDEP bit

prcm_partition
    (OMAP4 only) PRCM partition ID for this clkdm's registers

cm_inst
    (OMAP4 only) CM instance register offset

clkdm_offs
    (OMAP4 only) CM clockdomain register offset

wkdep_srcs
    Clockdomains that can be told to wake this powerdomain up

sleepdep_srcs
    Clockdomains that can be told to keep this clkdm from inact

usecount
    Usecount tracking

node
    list_head to link all clockdomains together

.. _`clockdomain.description`:

Description
-----------

\ ``prcm_partition``\  should be a macro from mach-omap2/prcm44xx.h (OMAP4 only)
\ ``cm_inst``\  should be a macro ending in \_INST from the OMAP4 CM instance
definitions (OMAP4 only)
\ ``clkdm_offs``\  should be a macro ending in \_CDOFFS from the OMAP4 CM instance
definitions (OMAP4 only)

.. _`clkdm_ops`:

struct clkdm_ops
================

.. c:type:: struct clkdm_ops

    Arch specific function implementations

.. _`clkdm_ops.definition`:

Definition
----------

.. code-block:: c

    struct clkdm_ops {
        int (*clkdm_add_wkdep)(struct clockdomain *clkdm1, struct clockdomain *clkdm2);
        int (*clkdm_del_wkdep)(struct clockdomain *clkdm1, struct clockdomain *clkdm2);
        int (*clkdm_read_wkdep)(struct clockdomain *clkdm1, struct clockdomain *clkdm2);
        int (*clkdm_clear_all_wkdeps)(struct clockdomain *clkdm);
        int (*clkdm_add_sleepdep)(struct clockdomain *clkdm1, struct clockdomain *clkdm2);
        int (*clkdm_del_sleepdep)(struct clockdomain *clkdm1, struct clockdomain *clkdm2);
        int (*clkdm_read_sleepdep)(struct clockdomain *clkdm1, struct clockdomain *clkdm2);
        int (*clkdm_clear_all_sleepdeps)(struct clockdomain *clkdm);
        int (*clkdm_sleep)(struct clockdomain *clkdm);
        int (*clkdm_wakeup)(struct clockdomain *clkdm);
        void (*clkdm_allow_idle)(struct clockdomain *clkdm);
        void (*clkdm_deny_idle)(struct clockdomain *clkdm);
        int (*clkdm_clk_enable)(struct clockdomain *clkdm);
        int (*clkdm_clk_disable)(struct clockdomain *clkdm);
    }

.. _`clkdm_ops.members`:

Members
-------

clkdm_add_wkdep
    Add a wakeup dependency between clk domains

clkdm_del_wkdep
    Delete a wakeup dependency between clk domains

clkdm_read_wkdep
    Read wakeup dependency state between clk domains

clkdm_clear_all_wkdeps
    Remove all wakeup dependencies from the clk domain

clkdm_add_sleepdep
    Add a sleep dependency between clk domains

clkdm_del_sleepdep
    Delete a sleep dependency between clk domains

clkdm_read_sleepdep
    Read sleep dependency state between clk domains

clkdm_clear_all_sleepdeps
    Remove all sleep dependencies from the clk domain

clkdm_sleep
    Force a clockdomain to sleep

clkdm_wakeup
    Force a clockdomain to wakeup

clkdm_allow_idle
    Enable hw supervised idle transitions for clock domain

clkdm_deny_idle
    Disable hw supervised idle transitions for clock domain

clkdm_clk_enable
    Put the clkdm in right state for a clock enable

clkdm_clk_disable
    Put the clkdm in right state for a clock disable

.. This file was automatic generated / don't edit.

