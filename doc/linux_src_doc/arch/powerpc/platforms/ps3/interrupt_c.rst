.. -*- coding: utf-8; mode: rst -*-

===========
interrupt.c
===========


.. _`ps3_private`:

struct ps3_private
==================

.. c:type:: ps3_private

    a per cpu data structure


.. _`ps3_private.definition`:

Definition
----------

.. code-block:: c

  struct ps3_private {
    spinlock_t bmp_lock;
    u64 ppe_id;
    u64 thread_id;
    unsigned long ipi_debug_brk_mask;
    unsigned long ipi_mask;
  };


.. _`ps3_private.members`:

Members
-------

:``bmp_lock``:
    Synchronize access to bmp.

:``ppe_id``:
    HV logical_ppe_id

:``thread_id``:
    HV thread_id

:``ipi_debug_brk_mask``:
    Mask for debug break IPIs

:``ipi_mask``:
    Mask of IPI virqs




.. _`ps3_chip_mask`:

ps3_chip_mask
=============

.. c:function:: void ps3_chip_mask (struct irq_data *d)

    Set an interrupt mask bit in ps3_bmp.

    :param struct irq_data \*d:

        *undescribed*



.. _`ps3_chip_mask.description`:

Description
-----------

Sets ps3_bmp.mask and calls :c:func:`lv1_did_update_interrupt_mask`.



.. _`ps3_chip_unmask`:

ps3_chip_unmask
===============

.. c:function:: void ps3_chip_unmask (struct irq_data *d)

    Clear an interrupt mask bit in ps3_bmp.

    :param struct irq_data \*d:

        *undescribed*



.. _`ps3_chip_unmask.description`:

Description
-----------

Clears ps3_bmp.mask and calls :c:func:`lv1_did_update_interrupt_mask`.



.. _`ps3_chip_eoi`:

ps3_chip_eoi
============

.. c:function:: void ps3_chip_eoi (struct irq_data *d)

    HV end-of-interrupt.

    :param struct irq_data \*d:

        *undescribed*



.. _`ps3_chip_eoi.description`:

Description
-----------

Calls :c:func:`lv1_end_of_interrupt_ext`.



.. _`ps3_virq_setup`:

ps3_virq_setup
==============

.. c:function:: int ps3_virq_setup (enum ps3_cpu_binding cpu, unsigned long outlet, unsigned int *virq)

    virq related setup.

    :param enum ps3_cpu_binding cpu:
        enum ps3_cpu_binding indicating the cpu the interrupt should be
        serviced on.

    :param unsigned long outlet:
        The HV outlet from the various create outlet routines.

    :param unsigned int \*virq:
        The assigned Linux virq.



.. _`ps3_virq_setup.description`:

Description
-----------

Calls :c:func:`irq_create_mapping` to get a virq and sets the chip data to
ps3_private data.



.. _`ps3_virq_destroy`:

ps3_virq_destroy
================

.. c:function:: int ps3_virq_destroy (unsigned int virq)

    virq related teardown.

    :param unsigned int virq:
        The assigned Linux virq.



.. _`ps3_virq_destroy.description`:

Description
-----------

Clears chip data and calls :c:func:`irq_dispose_mapping` for the virq.



.. _`ps3_irq_plug_setup`:

ps3_irq_plug_setup
==================

.. c:function:: int ps3_irq_plug_setup (enum ps3_cpu_binding cpu, unsigned long outlet, unsigned int *virq)

    Generic outlet and virq related setup.

    :param enum ps3_cpu_binding cpu:
        enum ps3_cpu_binding indicating the cpu the interrupt should be
        serviced on.

    :param unsigned long outlet:
        The HV outlet from the various create outlet routines.

    :param unsigned int \*virq:
        The assigned Linux virq.



.. _`ps3_irq_plug_setup.description`:

Description
-----------

Sets up virq and connects the irq plug.



.. _`ps3_irq_plug_destroy`:

ps3_irq_plug_destroy
====================

.. c:function:: int ps3_irq_plug_destroy (unsigned int virq)

    Generic outlet and virq related teardown.

    :param unsigned int virq:
        The assigned Linux virq.



.. _`ps3_irq_plug_destroy.description`:

Description
-----------

Disconnects the irq plug and tears down virq.
Do not call for system bus event interrupts setup with
:c:func:`ps3_sb_event_receive_port_setup`.



.. _`ps3_event_receive_port_setup`:

ps3_event_receive_port_setup
============================

.. c:function:: int ps3_event_receive_port_setup (enum ps3_cpu_binding cpu, unsigned int *virq)

    Setup an event receive port.

    :param enum ps3_cpu_binding cpu:
        enum ps3_cpu_binding indicating the cpu the interrupt should be
        serviced on.

    :param unsigned int \*virq:
        The assigned Linux virq.



.. _`ps3_event_receive_port_setup.description`:

Description
-----------

The virq can be used with :c:func:`lv1_connect_interrupt_event_receive_port` to
arrange to receive interrupts from system-bus devices, or with
:c:func:`ps3_send_event_locally` to signal events.



.. _`ps3_event_receive_port_destroy`:

ps3_event_receive_port_destroy
==============================

.. c:function:: int ps3_event_receive_port_destroy (unsigned int virq)

    Destroy an event receive port.

    :param unsigned int virq:
        The assigned Linux virq.



.. _`ps3_event_receive_port_destroy.description`:

Description
-----------

Since ps3_event_receive_port_destroy destroys the receive port outlet,
SB devices need to call :c:func:`disconnect_interrupt_event_receive_port` before
this.



.. _`ps3_sb_event_receive_port_setup`:

ps3_sb_event_receive_port_setup
===============================

.. c:function:: int ps3_sb_event_receive_port_setup (struct ps3_system_bus_device *dev, enum ps3_cpu_binding cpu, unsigned int *virq)

    Setup a system bus event receive port.

    :param struct ps3_system_bus_device \*dev:
        The system bus device instance.

    :param enum ps3_cpu_binding cpu:
        enum ps3_cpu_binding indicating the cpu the interrupt should be
        serviced on.

    :param unsigned int \*virq:
        The assigned Linux virq.



.. _`ps3_sb_event_receive_port_setup.description`:

Description
-----------

An event irq represents a virtual device interrupt.  The interrupt_id
coresponds to the software interrupt number.



.. _`ps3_io_irq_setup`:

ps3_io_irq_setup
================

.. c:function:: int ps3_io_irq_setup (enum ps3_cpu_binding cpu, unsigned int interrupt_id, unsigned int *virq)

    Setup a system bus io irq.

    :param enum ps3_cpu_binding cpu:
        enum ps3_cpu_binding indicating the cpu the interrupt should be
        serviced on.

    :param unsigned int interrupt_id:
        The device interrupt id read from the system repository.

    :param unsigned int \*virq:
        The assigned Linux virq.



.. _`ps3_io_irq_setup.description`:

Description
-----------

An io irq represents a non-virtualized device interrupt.  interrupt_id
coresponds to the interrupt number of the interrupt controller.



.. _`ps3_vuart_irq_setup`:

ps3_vuart_irq_setup
===================

.. c:function:: int ps3_vuart_irq_setup (enum ps3_cpu_binding cpu, void *virt_addr_bmp, unsigned int *virq)

    Setup the system virtual uart virq.

    :param enum ps3_cpu_binding cpu:
        enum ps3_cpu_binding indicating the cpu the interrupt should be
        serviced on.

    :param void \*virt_addr_bmp:
        The caller supplied virtual uart interrupt bitmap.

    :param unsigned int \*virq:
        The assigned Linux virq.



.. _`ps3_vuart_irq_setup.description`:

Description
-----------

The system supports only a single virtual uart, so multiple calls without
freeing the interrupt will return a wrong state error.



.. _`ps3_spe_irq_setup`:

ps3_spe_irq_setup
=================

.. c:function:: int ps3_spe_irq_setup (enum ps3_cpu_binding cpu, unsigned long spe_id, unsigned int class, unsigned int *virq)

    Setup an spe virq.

    :param enum ps3_cpu_binding cpu:
        enum ps3_cpu_binding indicating the cpu the interrupt should be
        serviced on.

    :param unsigned long spe_id:
        The spe_id returned from :c:func:`lv1_construct_logical_spe`.

    :param unsigned int class:
        The spe interrupt class {0,1,2}.

    :param unsigned int \*virq:
        The assigned Linux virq.

