.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/irq_sim.c

.. _`irq_sim_init`:

irq_sim_init
============

.. c:function:: int irq_sim_init(struct irq_sim *sim, unsigned int num_irqs)

    Initialize the interrupt simulator: allocate a range of dummy interrupts.

    :param sim:
        The interrupt simulator object to initialize.
    :type sim: struct irq_sim \*

    :param num_irqs:
        Number of interrupts to allocate
    :type num_irqs: unsigned int

.. _`irq_sim_init.on-success`:

On success
----------

return the base of the allocated interrupt range.

.. _`irq_sim_init.on-failure`:

On failure
----------

a negative errno.

.. _`irq_sim_fini`:

irq_sim_fini
============

.. c:function:: void irq_sim_fini(struct irq_sim *sim)

    Deinitialize the interrupt simulator: free the interrupt descriptors and allocated memory.

    :param sim:
        The interrupt simulator to tear down.
    :type sim: struct irq_sim \*

.. _`devm_irq_sim_init`:

devm_irq_sim_init
=================

.. c:function:: int devm_irq_sim_init(struct device *dev, struct irq_sim *sim, unsigned int num_irqs)

    Initialize the interrupt simulator for a managed device.

    :param dev:
        Device to initialize the simulator object for.
    :type dev: struct device \*

    :param sim:
        The interrupt simulator object to initialize.
    :type sim: struct irq_sim \*

    :param num_irqs:
        Number of interrupts to allocate
    :type num_irqs: unsigned int

.. _`devm_irq_sim_init.on-success`:

On success
----------

return the base of the allocated interrupt range.

.. _`devm_irq_sim_init.on-failure`:

On failure
----------

a negative errno.

.. _`irq_sim_fire`:

irq_sim_fire
============

.. c:function:: void irq_sim_fire(struct irq_sim *sim, unsigned int offset)

    Enqueue an interrupt.

    :param sim:
        The interrupt simulator object.
    :type sim: struct irq_sim \*

    :param offset:
        Offset of the simulated interrupt which should be fired.
    :type offset: unsigned int

.. _`irq_sim_irqnum`:

irq_sim_irqnum
==============

.. c:function:: int irq_sim_irqnum(struct irq_sim *sim, unsigned int offset)

    Get the allocated number of a dummy interrupt.

    :param sim:
        The interrupt simulator object.
    :type sim: struct irq_sim \*

    :param offset:
        Offset of the simulated interrupt for which to retrieve
        the number.
    :type offset: unsigned int

.. This file was automatic generated / don't edit.

