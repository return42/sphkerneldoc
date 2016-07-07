.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/zynq/pll.c

.. _`zynq_pll`:

struct zynq_pll
===============

.. c:type:: struct zynq_pll


.. _`zynq_pll.definition`:

Definition
----------

.. code-block:: c

    struct zynq_pll {
        struct clk_hw hw;
        void __iomem *pll_ctrl;
        void __iomem *pll_status;
        spinlock_t *lock;
        u8 lockbit;
    }

.. _`zynq_pll.members`:

Members
-------

hw
    Handle between common and hardware-specific interfaces

pll_ctrl
    PLL control register

pll_status
    PLL status register

lock
    Register lock

lockbit
    Indicates the associated PLL_LOCKED bit in the PLL status
    register.

.. _`zynq_pll_round_rate`:

zynq_pll_round_rate
===================

.. c:function:: long zynq_pll_round_rate(struct clk_hw *hw, unsigned long rate, unsigned long *prate)

    Round a clock frequency

    :param struct clk_hw \*hw:
        Handle between common and hardware-specific interfaces

    :param unsigned long rate:
        Desired clock frequency

    :param unsigned long \*prate:
        Clock frequency of parent clock
        Returns frequency closest to \ ``rate``\  the hardware can generate.

.. _`zynq_pll_recalc_rate`:

zynq_pll_recalc_rate
====================

.. c:function:: unsigned long zynq_pll_recalc_rate(struct clk_hw *hw, unsigned long parent_rate)

    Recalculate clock frequency

    :param struct clk_hw \*hw:
        Handle between common and hardware-specific interfaces

    :param unsigned long parent_rate:
        Clock frequency of parent clock
        Returns current clock frequency.

.. _`zynq_pll_is_enabled`:

zynq_pll_is_enabled
===================

.. c:function:: int zynq_pll_is_enabled(struct clk_hw *hw)

    Check if a clock is enabled

    :param struct clk_hw \*hw:
        Handle between common and hardware-specific interfaces
        Returns 1 if the clock is enabled, 0 otherwise.

.. _`zynq_pll_is_enabled.description`:

Description
-----------

Not sure this is a good idea, but since disabled means bypassed for
this clock implementation we say we are always enabled.

.. _`zynq_pll_enable`:

zynq_pll_enable
===============

.. c:function:: int zynq_pll_enable(struct clk_hw *hw)

    Enable clock

    :param struct clk_hw \*hw:
        Handle between common and hardware-specific interfaces
        Returns 0 on success

.. _`zynq_pll_disable`:

zynq_pll_disable
================

.. c:function:: void zynq_pll_disable(struct clk_hw *hw)

    Disable clock

    :param struct clk_hw \*hw:
        Handle between common and hardware-specific interfaces
        Returns 0 on success

.. _`clk_register_zynq_pll`:

clk_register_zynq_pll
=====================

.. c:function:: struct clk *clk_register_zynq_pll(const char *name, const char *parent, void __iomem *pll_ctrl, void __iomem *pll_status, u8 lock_index, spinlock_t *lock)

    Register PLL with the clock framework \ ``name``\         PLL name \ ``parent``\       Parent clock name \ ``pll_ctrl``\     Pointer to PLL control register \ ``pll_status``\   Pointer to PLL status register \ ``lock_index``\   Bit index to this PLL's lock status bit in \ ``pll_status``\  \ ``lock``\         Register lock Returns handle to the registered clock.

    :param const char \*name:
        *undescribed*

    :param const char \*parent:
        *undescribed*

    :param void __iomem \*pll_ctrl:
        *undescribed*

    :param void __iomem \*pll_status:
        *undescribed*

    :param u8 lock_index:
        *undescribed*

    :param spinlock_t \*lock:
        *undescribed*

.. This file was automatic generated / don't edit.

