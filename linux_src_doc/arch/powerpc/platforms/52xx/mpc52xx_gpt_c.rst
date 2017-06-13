.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/52xx/mpc52xx_gpt.c

.. _`mpc52xx_gpt_priv`:

struct mpc52xx_gpt_priv
=======================

.. c:type:: struct mpc52xx_gpt_priv

    Private data structure for MPC52xx GPT driver

.. _`mpc52xx_gpt_priv.definition`:

Definition
----------

.. code-block:: c

    struct mpc52xx_gpt_priv {
        struct list_head list;
        struct device *dev;
        struct mpc52xx_gpt __iomem *regs;
        spinlock_t lock;
        struct irq_domain *irqhost;
        u32 ipb_freq;
        u8 wdt_mode;
    #if definedCONFIG_GPIOLIB
        struct gpio_chip gc;
    #endif
    }

.. _`mpc52xx_gpt_priv.members`:

Members
-------

list
    *undescribed*

dev
    pointer to device structure

regs
    virtual address of GPT registers

lock
    spinlock to coordinate between different functions.

irqhost
    Pointer to irq_domain instance; used when IRQ mode is supported

ipb_freq
    *undescribed*

wdt_mode
    only relevant for gpt0: bit 0 (MPC52xx_GPT_CAN_WDT) indicates
    if the gpt may be used as wdt, bit 1 (MPC52xx_GPT_IS_WDT) indicates
    if the timer is actively used as wdt which blocks gpt functions

gc
    gpio_chip instance structure; used when GPIO is enabled

.. _`mpc52xx_gpt_from_irq`:

mpc52xx_gpt_from_irq
====================

.. c:function:: struct mpc52xx_gpt_priv *mpc52xx_gpt_from_irq(int irq)

    Return the GPT device associated with an IRQ number

    :param int irq:
        irq of timer.

.. _`mpc52xx_gpt_start_timer`:

mpc52xx_gpt_start_timer
=======================

.. c:function:: int mpc52xx_gpt_start_timer(struct mpc52xx_gpt_priv *gpt, u64 period, int continuous)

    Set and enable the GPT timer

    :param struct mpc52xx_gpt_priv \*gpt:
        Pointer to gpt private data structure

    :param u64 period:
        period of timer in ns; max. ~130s @ 33MHz IPB clock

    :param int continuous:
        set to 1 to make timer continuous free running

.. _`mpc52xx_gpt_start_timer.description`:

Description
-----------

An interrupt will be generated every time the timer fires

.. _`mpc52xx_gpt_stop_timer`:

mpc52xx_gpt_stop_timer
======================

.. c:function:: int mpc52xx_gpt_stop_timer(struct mpc52xx_gpt_priv *gpt)

    Stop a gpt

    :param struct mpc52xx_gpt_priv \*gpt:
        Pointer to gpt private data structure

.. _`mpc52xx_gpt_stop_timer.description`:

Description
-----------

Returns an error if attempting to stop a wdt

.. _`mpc52xx_gpt_timer_period`:

mpc52xx_gpt_timer_period
========================

.. c:function:: u64 mpc52xx_gpt_timer_period(struct mpc52xx_gpt_priv *gpt)

    Read the timer period

    :param struct mpc52xx_gpt_priv \*gpt:
        Pointer to gpt private data structure

.. _`mpc52xx_gpt_timer_period.description`:

Description
-----------

Returns the timer period in ns

.. This file was automatic generated / don't edit.

