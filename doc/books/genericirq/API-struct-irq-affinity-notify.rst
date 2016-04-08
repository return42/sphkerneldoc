
.. _API-struct-irq-affinity-notify:

==========================
struct irq_affinity_notify
==========================

*man struct irq_affinity_notify(9)*

*4.6.0-rc1*

context for notification of IRQ affinity changes


Synopsis
========

.. code-block:: c

    struct irq_affinity_notify {
      unsigned int irq;
      struct kref kref;
      struct work_struct work;
      void (* notify) (struct irq_affinity_notify *, const cpumask_t *mask);
      void (* release) (struct kref *ref);
    };


Members
=======

irq
    Interrupt to which notification applies

kref
    Reference count, for internal use

work
    Work item, for internal use

notify
    Function to be called on change. This will be called in process context.

release
    Function to be called on release. This will be called in process context. Once registered, the structure must only be freed when this function is called or later.
