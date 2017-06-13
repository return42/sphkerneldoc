.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/irqbypass.h

.. _`irq_bypass_producer`:

struct irq_bypass_producer
==========================

.. c:type:: struct irq_bypass_producer

    IRQ bypass producer definition

.. _`irq_bypass_producer.definition`:

Definition
----------

.. code-block:: c

    struct irq_bypass_producer {
        struct list_head node;
        void *token;
        int irq;
        int (*add_consumer)(struct irq_bypass_producer *, struct irq_bypass_consumer *);
        void (*del_consumer)(struct irq_bypass_producer *, struct irq_bypass_consumer *);
        void (*stop)(struct irq_bypass_producer *);
        void (*start)(struct irq_bypass_producer *);
    }

.. _`irq_bypass_producer.members`:

Members
-------

node
    IRQ bypass manager private list management

token
    opaque token to match between producer and consumer (non-NULL)

irq
    Linux IRQ number for the producer device

add_consumer
    Connect the IRQ producer to an IRQ consumer (optional)

del_consumer
    Disconnect the IRQ producer from an IRQ consumer (optional)

stop
    Perform any quiesce operations necessary prior to add/del (optional)

start
    Perform any startup operations necessary after add/del (optional)

.. _`irq_bypass_producer.description`:

Description
-----------

The IRQ bypass producer structure represents an interrupt source for
participation in possible host bypass, for instance an interrupt vector
for a physical device assigned to a VM.

.. _`irq_bypass_consumer`:

struct irq_bypass_consumer
==========================

.. c:type:: struct irq_bypass_consumer

    IRQ bypass consumer definition

.. _`irq_bypass_consumer.definition`:

Definition
----------

.. code-block:: c

    struct irq_bypass_consumer {
        struct list_head node;
        void *token;
        int (*add_producer)(struct irq_bypass_consumer *, struct irq_bypass_producer *);
        void (*del_producer)(struct irq_bypass_consumer *, struct irq_bypass_producer *);
        void (*stop)(struct irq_bypass_consumer *);
        void (*start)(struct irq_bypass_consumer *);
    }

.. _`irq_bypass_consumer.members`:

Members
-------

node
    IRQ bypass manager private list management

token
    opaque token to match between producer and consumer (non-NULL)

add_producer
    Connect the IRQ consumer to an IRQ producer

del_producer
    Disconnect the IRQ consumer from an IRQ producer

stop
    Perform any quiesce operations necessary prior to add/del (optional)

start
    Perform any startup operations necessary after add/del (optional)

.. _`irq_bypass_consumer.description`:

Description
-----------

The IRQ bypass consumer structure represents an interrupt sink for
participation in possible host bypass, for instance a hypervisor may
support offloads to allow bypassing the host entirely or offload
portions of the interrupt handling to the VM.

.. This file was automatic generated / don't edit.

