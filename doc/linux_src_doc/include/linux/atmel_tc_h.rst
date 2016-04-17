.. -*- coding: utf-8; mode: rst -*-

==========
atmel_tc.h
==========


.. _`atmel_tcb_config`:

struct atmel_tcb_config
=======================

.. c:type:: atmel_tcb_config

    SoC data for a Timer/Counter Block


.. _`atmel_tcb_config.definition`:

Definition
----------

.. code-block:: c

  struct atmel_tcb_config {
    size_t counter_width;
  };


.. _`atmel_tcb_config.members`:

Members
-------

:``counter_width``:
    size in bits of a timer counter register




.. _`atmel_tc`:

struct atmel_tc
===============

.. c:type:: atmel_tc

    information about a Timer/Counter Block


.. _`atmel_tc.definition`:

Definition
----------

.. code-block:: c

  struct atmel_tc {
    struct platform_device * pdev;
    void __iomem * regs;
    int id;
    const struct atmel_tcb_config * tcb_config;
    int irq[3];
    struct clk * clk[3];
    struct list_head node;
    bool allocated;
  };


.. _`atmel_tc.members`:

Members
-------

:``pdev``:
    physical device

:``regs``:
    mapping through which the I/O registers can be accessed

:``id``:
    block id

:``tcb_config``:
    configuration data from SoC

:``irq[3]``:
    irq for each of the three channels

:``clk[3]``:
    internal clock source for each of the three channels

:``node``:
    list node, for tclib internal use

:``allocated``:
    if already used, for tclib internal use




.. _`atmel_tc.description`:

Description
-----------

On some platforms, each TC channel has its own clocks and IRQs,
while on others, all TC channels share the same clock and IRQ.
Drivers should :c:func:`clk_enable` all the clocks they need even though
all the entries in ``clk`` may point to the same physical clock.
Likewise, drivers should request irqs independently for each
channel, but they must use IRQF_SHARED in case some of the entries
in ``irq`` are actually the same IRQ.

