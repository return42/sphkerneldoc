
.. _API-struct-irq-chip:

===============
struct irq_chip
===============

*man struct irq_chip(9)*

*4.6.0-rc1*

hardware interrupt chip descriptor


Synopsis
========

.. code-block:: c

    struct irq_chip {
      const char * name;
      unsigned int  (* irq_startup) (struct irq_data *data);
      void (* irq_shutdown) (struct irq_data *data);
      void (* irq_enable) (struct irq_data *data);
      void (* irq_disable) (struct irq_data *data);
      void (* irq_ack) (struct irq_data *data);
      void (* irq_mask) (struct irq_data *data);
      void (* irq_mask_ack) (struct irq_data *data);
      void (* irq_unmask) (struct irq_data *data);
      void (* irq_eoi) (struct irq_data *data);
      int (* irq_set_affinity) (struct irq_data *data, const struct cpumask *dest, bool force);
      int (* irq_retrigger) (struct irq_data *data);
      int (* irq_set_type) (struct irq_data *data, unsigned int flow_type);
      int (* irq_set_wake) (struct irq_data *data, unsigned int on);
      void (* irq_bus_lock) (struct irq_data *data);
      void (* irq_bus_sync_unlock) (struct irq_data *data);
      void (* irq_cpu_online) (struct irq_data *data);
      void (* irq_cpu_offline) (struct irq_data *data);
      void (* irq_suspend) (struct irq_data *data);
      void (* irq_resume) (struct irq_data *data);
      void (* irq_pm_shutdown) (struct irq_data *data);
      void (* irq_calc_mask) (struct irq_data *data);
      void (* irq_print_chip) (struct irq_data *data, struct seq_file *p);
      int (* irq_request_resources) (struct irq_data *data);
      void (* irq_release_resources) (struct irq_data *data);
      void (* irq_compose_msi_msg) (struct irq_data *data, struct msi_msg *msg);
      void (* irq_write_msi_msg) (struct irq_data *data, struct msi_msg *msg);
      int (* irq_get_irqchip_state) (struct irq_data *data, enum irqchip_irq_state which, bool *state);
      int (* irq_set_irqchip_state) (struct irq_data *data, enum irqchip_irq_state which, bool state);
      int (* irq_set_vcpu_affinity) (struct irq_data *data, void *vcpu_info);
      void (* ipi_send_single) (struct irq_data *data, unsigned int cpu);
      void (* ipi_send_mask) (struct irq_data *data, const struct cpumask *dest);
      unsigned long flags;
    };


Members
=======

name
    name for /proc/interrupts

irq_startup
    start up the interrupt (defaults to ->enable if NULL)

irq_shutdown
    shut down the interrupt (defaults to ->disable if NULL)

irq_enable
    enable the interrupt (defaults to chip->unmask if NULL)

irq_disable
    disable the interrupt

irq_ack
    start of a new interrupt

irq_mask
    mask an interrupt source

irq_mask_ack
    ack and mask an interrupt source

irq_unmask
    unmask an interrupt source

irq_eoi
    end of interrupt

irq_set_affinity
    set the CPU affinity on SMP machines

irq_retrigger
    resend an IRQ to the CPU

irq_set_type
    set the flow type (IRQ_TYPE_LEVEL/etc.) of an IRQ

irq_set_wake
    enable/disable power-management wake-on of an IRQ

irq_bus_lock
    function to lock access to slow bus (i2c) chips

irq_bus_sync_unlock
    function to sync and unlock slow bus (i2c) chips

irq_cpu_online
    configure an interrupt source for a secondary CPU

irq_cpu_offline
    un-configure an interrupt source for a secondary CPU

irq_suspend
    function called from core code on suspend once per chip, when one or more interrupts are installed

irq_resume
    function called from core code on resume once per chip, when one ore more interrupts are installed

irq_pm_shutdown
    function called from core code on shutdown once per chip

irq_calc_mask
    Optional function to set irq_data.mask for special cases

irq_print_chip
    optional to print special chip info in show_interrupts

irq_request_resources
    optional to request resources before calling any other callback related to this irq

irq_release_resources
    optional to release resources acquired with irq_request_resources

irq_compose_msi_msg
    optional to compose message content for MSI

irq_write_msi_msg
    optional to write message content for MSI

irq_get_irqchip_state
    return the internal state of an interrupt

irq_set_irqchip_state
    set the internal state of a interrupt

irq_set_vcpu_affinity
    optional to target a vCPU in a virtual machine

ipi_send_single
    send a single IPI to destination cpus

ipi_send_mask
    send an IPI to destination cpus in cpumask

flags
    chip specific flags
