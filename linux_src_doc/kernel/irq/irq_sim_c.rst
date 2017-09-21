.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/irq_sim.c

.. _`irq_sim_init`:

irq_sim_init
============

.. c:function:: int irq_sim_init(struct irq_sim *sim, unsigned int num_irqs)

    Initialize the interrupt simulator: allocate a range of dummy interrupts.

    :param struct irq_sim \*sim:
        The interrupt simulator object to initialize.

    :param unsigned int num_irqs:
        Number of interrupts to allocate

.. _`irq_sim_init.description`:

Description
-----------

Returns 0 on success and a negative error number on failure.

.. _`irq_sim_fini`:

irq_sim_fini
============

.. c:function:: void irq_sim_fini(struct irq_sim *sim)

    Deinitialize the interrupt simulator: free the interrupt descriptors and allocated memory.

    :param struct irq_sim \*sim:
        The interrupt simulator to tear down.

.. _`devm_irq_sim_init`:

devm_irq_sim_init
=================

.. c:function:: int devm_irq_sim_init(struct device *dev, struct irq_sim *sim, unsigned int num_irqs)

    Initialize the interrupt simulator for a managed device.

    :param struct device \*dev:
        Device to initialize the simulator object for.

    :param struct irq_sim \*sim:
        The interrupt simulator object to initialize.

    :param unsigned int num_irqs:
        Number of interrupts to allocate

.. _`devm_irq_sim_init.description`:

Description
-----------

Returns 0 on success and a negative error number on failure.

.. _`irq_sim_fire`:

irq_sim_fire
============

.. c:function:: void irq_sim_fire(struct irq_sim *sim, unsigned int offset)

    Enqueue an interrupt.

    :param struct irq_sim \*sim:
        The interrupt simulator object.

    :param unsigned int offset:
        Offset of the simulated interrupt which should be fired.

.. _`irq_sim_irqnum`:

irq_sim_irqnum
==============

.. c:function:: int irq_sim_irqnum(struct irq_sim *sim, unsigned int offset)

    Get the allocated number of a dummy interrupt.

    :param struct irq_sim \*sim:
        The interrupt simulator object.

    :param unsigned int offset:
        Offset of the simulated interrupt for which to retrieve
        the number.

.. This file was automatic generated / don't edit.

