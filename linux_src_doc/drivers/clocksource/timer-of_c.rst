.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/timer-of.c

.. _`timer_of_irq_exit`:

timer_of_irq_exit
=================

.. c:function:: void timer_of_irq_exit(struct of_timer_irq *of_irq)

    Release the interrupt

    :param struct of_timer_irq \*of_irq:
        an of_timer_irq structure pointer

.. _`timer_of_irq_exit.description`:

Description
-----------

Free the irq resource

.. _`timer_of_irq_init`:

timer_of_irq_init
=================

.. c:function:: int timer_of_irq_init(struct device_node *np, struct of_timer_irq *of_irq)

    Request the interrupt

    :param struct device_node \*np:
        a device tree node pointer

    :param struct of_timer_irq \*of_irq:
        an of_timer_irq structure pointer

.. _`timer_of_irq_init.description`:

Description
-----------

Get the interrupt number from the DT from its definition and
request it. The interrupt is gotten by falling back the following way:

- Get interrupt number by name
- Get interrupt number by index

When the interrupt is per CPU, 'request_percpu_irq()' is called,
otherwise 'request_irq()' is used.

Returns 0 on success, < 0 otherwise

.. _`timer_of_clk_exit`:

timer_of_clk_exit
=================

.. c:function:: void timer_of_clk_exit(struct of_timer_clk *of_clk)

    Release the clock resources

    :param struct of_timer_clk \*of_clk:
        a of_timer_clk structure pointer

.. _`timer_of_clk_exit.description`:

Description
-----------

Disables and releases the refcount on the clk

.. _`timer_of_clk_init`:

timer_of_clk_init
=================

.. c:function:: int timer_of_clk_init(struct device_node *np, struct of_timer_clk *of_clk)

    Initialize the clock resources

    :param struct device_node \*np:
        a device tree node pointer

    :param struct of_timer_clk \*of_clk:
        a of_timer_clk structure pointer

.. _`timer_of_clk_init.description`:

Description
-----------

Get the clock by name or by index, enable it and get the rate

Returns 0 on success, < 0 otherwise

.. _`timer_of_cleanup`:

timer_of_cleanup
================

.. c:function:: void timer_of_cleanup(struct timer_of *to)

    release timer_of ressources

    :param struct timer_of \*to:
        timer_of structure

.. _`timer_of_cleanup.description`:

Description
-----------

Release the ressources that has been used in \ :c:func:`timer_of_init`\ .
This function should be called in init error cases

.. This file was automatic generated / don't edit.

