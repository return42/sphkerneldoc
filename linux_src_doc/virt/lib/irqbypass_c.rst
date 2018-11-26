.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/lib/irqbypass.c

.. _`irq_bypass_register_producer`:

irq_bypass_register_producer
============================

.. c:function:: int irq_bypass_register_producer(struct irq_bypass_producer *producer)

    register IRQ bypass producer

    :param producer:
        pointer to producer structure
    :type producer: struct irq_bypass_producer \*

.. _`irq_bypass_register_producer.description`:

Description
-----------

Add the provided IRQ producer to the list of producers and connect
with any matching token found on the IRQ consumers list.

.. _`irq_bypass_unregister_producer`:

irq_bypass_unregister_producer
==============================

.. c:function:: void irq_bypass_unregister_producer(struct irq_bypass_producer *producer)

    unregister IRQ bypass producer

    :param producer:
        pointer to producer structure
    :type producer: struct irq_bypass_producer \*

.. _`irq_bypass_unregister_producer.description`:

Description
-----------

Remove a previously registered IRQ producer from the list of producers
and disconnect it from any connected IRQ consumer.

.. _`irq_bypass_register_consumer`:

irq_bypass_register_consumer
============================

.. c:function:: int irq_bypass_register_consumer(struct irq_bypass_consumer *consumer)

    register IRQ bypass consumer

    :param consumer:
        pointer to consumer structure
    :type consumer: struct irq_bypass_consumer \*

.. _`irq_bypass_register_consumer.description`:

Description
-----------

Add the provided IRQ consumer to the list of consumers and connect
with any matching token found on the IRQ producer list.

.. _`irq_bypass_unregister_consumer`:

irq_bypass_unregister_consumer
==============================

.. c:function:: void irq_bypass_unregister_consumer(struct irq_bypass_consumer *consumer)

    unregister IRQ bypass consumer

    :param consumer:
        pointer to consumer structure
    :type consumer: struct irq_bypass_consumer \*

.. _`irq_bypass_unregister_consumer.description`:

Description
-----------

Remove a previously registered IRQ consumer from the list of consumers
and disconnect it from any connected IRQ producer.

.. This file was automatic generated / don't edit.

