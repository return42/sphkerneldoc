.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap1/clock.h

.. _`clkops`:

struct clkops
=============

.. c:type:: struct clkops

    some clock function pointers

.. _`clkops.definition`:

Definition
----------

.. code-block:: c

    struct clkops {
        int (*enable)(struct clk *);
        void (*disable)(struct clk *);
        void (*find_idlest)(struct clk *, void __iomem **, u8 *, u8 *);
        void (*find_companion)(struct clk *, void __iomem **, u8 *);
        void (*allow_idle)(struct clk *);
        void (*deny_idle)(struct clk *);
    }

.. _`clkops.members`:

Members
-------

enable
    fn ptr that enables the current clock in hardware

disable
    fn ptr that enables the current clock in hardware

find_idlest
    function returning the IDLEST register for the clock's IP blk

find_companion
    function returning the "companion" clk reg for the clock

allow_idle
    fn ptr that enables autoidle for the current clock in hardware

deny_idle
    fn ptr that disables autoidle for the current clock in hardware

.. _`clkops.description`:

Description
-----------

A "companion" clk is an accompanying clock to the one being queried
that must be enabled for the IP module connected to the clock to
become accessible by the hardware.  Neither \ ``find_idlest``\  nor
\ ``find_companion``\  should be needed; that information is IP
block-specific; the hwmod code has been created to handle this, but
until hwmod data is ready and drivers have been converted to use PM
runtime calls in place of \ :c:func:`clk_enable`\ /clk_disable(), \ ``find_idlest``\  and
\ ``find_companion``\  must, unfortunately, remain.

.. _`clk`:

struct clk
==========

.. c:type:: struct clk

    OMAP struct clk

.. _`clk.definition`:

Definition
----------

.. code-block:: c

    struct clk {
        struct list_head node;
        const struct clkops *ops;
        const char *name;
        struct clk *parent;
        struct list_head children;
        struct list_head sibling;
        unsigned long rate;
        void __iomem *enable_reg;
        unsigned long (*recalc)(struct clk *);
        int (*set_rate)(struct clk *, unsigned long);
        long (*round_rate)(struct clk *, unsigned long);
        void (*init)(struct clk *);
        u8 enable_bit;
        s8 usecount;
        u8 fixed_div;
        u8 flags;
        u8 rate_offset;
        u8 src_offset;
    #if defined(CONFIG_PM_DEBUG) && defined(CONFIG_DEBUG_FS)
        struct dentry *dent;
    #endif
    }

.. _`clk.members`:

Members
-------

node
    list_head connecting this clock into the full clock list

ops
    struct clkops \* for this clock

name
    the name of the clock in the hardware (used in hwmod data and debug)

parent
    pointer to this clock's parent struct clk

children
    list_head connecting to the child clks' \ ``sibling``\  list_heads

sibling
    list_head connecting this clk to its parent clk's \ ``children``\ 

rate
    current clock rate

enable_reg
    register to write to enable the clock (see \ ``enable_bit``\ )

recalc
    fn ptr that returns the clock's current rate

set_rate
    fn ptr that can change the clock's current rate

round_rate
    fn ptr that can round the clock's current rate

init
    fn ptr to do clock-specific initialization

enable_bit
    bitshift to write to enable/disable the clock (see \ ``enable_reg``\ )

usecount
    number of users that have requested this clock to be enabled

fixed_div
    when > 0, this clock's rate is its parent's rate / \ ``fixed_div``\ 

flags
    see "struct clk.flags possibilities" above

rate_offset
    bitshift for rate selection bitfield (OMAP1 only)

src_offset
    bitshift for source selection bitfield (OMAP1 only)

dent
    *undescribed*

.. _`clk.description`:

Description
-----------

XXX \ ``rate_offset``\ , \ ``src_offset``\  should probably be removed and OMAP1
clock code converted to use clksel.

XXX \ ``usecount``\  is poorly named.  It should be "enable_count" or
something similar.  "users" in the description refers to kernel
code (core code or drivers) that have called \ :c:func:`clk_enable`\  and not
yet called \ :c:func:`clk_disable`\ ; the usecount of parent clocks is also
incremented by the clock code when \ :c:func:`clk_enable`\  is called on child
clocks and decremented by the clock code when \ :c:func:`clk_disable`\  is
called on child clocks.

XXX \ ``clkdm``\ , \ ``usecount``\ , \ ``children``\ , \ ``sibling``\  should be marked for
internal use only.

\ ``children``\  and \ ``sibling``\  are used to optimize parent-to-child clock
tree traversals.  (child-to-parent traversals use \ ``parent``\ .)

XXX The notion of the clock's current rate probably needs to be
separated from the clock's target rate.

.. This file was automatic generated / don't edit.

