.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/irq.h

.. _`irq_common_data`:

struct irq_common_data
======================

.. c:type:: struct irq_common_data

    per irq data shared by all irqchips

.. _`irq_common_data.definition`:

Definition
----------

.. code-block:: c

    struct irq_common_data {
        unsigned int __private state_use_accessors;
    #ifdef CONFIG_NUMA
        unsigned int node;
    #endif
        void *handler_data;
        struct msi_desc *msi_desc;
        cpumask_var_t affinity;
    #ifdef CONFIG_GENERIC_IRQ_EFFECTIVE_AFF_MASK
        cpumask_var_t effective_affinity;
    #endif
    #ifdef CONFIG_GENERIC_IRQ_IPI
        unsigned int ipi_offset;
    #endif
    }

.. _`irq_common_data.members`:

Members
-------

state_use_accessors
    status information for irq chip functions.
    Use accessor functions to deal with it

node
    node index useful for balancing

handler_data
    per-IRQ data for the irq_chip methods

msi_desc
    MSI descriptor

affinity
    IRQ affinity on SMP. If this is an IPI
    related irq, then this is the mask of the
    CPUs to which an IPI can be sent.

effective_affinity
    The effective IRQ affinity on SMP as some irq
    chips do not allow multi CPU destinations.
    A subset of \ ``affinity``\ .

ipi_offset
    Offset of first IPI target cpu in \ ``affinity``\ . Optional.

.. _`irq_data`:

struct irq_data
===============

.. c:type:: struct irq_data

    per irq chip data passed down to chip functions

.. _`irq_data.definition`:

Definition
----------

.. code-block:: c

    struct irq_data {
        u32 mask;
        unsigned int irq;
        unsigned long hwirq;
        struct irq_common_data *common;
        struct irq_chip *chip;
        struct irq_domain *domain;
    #ifdef CONFIG_IRQ_DOMAIN_HIERARCHY
        struct irq_data *parent_data;
    #endif
        void *chip_data;
    }

.. _`irq_data.members`:

Members
-------

mask
    precomputed bitmask for accessing the chip registers

irq
    interrupt number

hwirq
    hardware interrupt number, local to the interrupt domain

common
    point to data shared by all irqchips

chip
    low level interrupt hardware access

domain
    Interrupt translation domain; responsible for mapping
    between hwirq number and linux irq number.

parent_data
    pointer to parent struct irq_data to support hierarchy
    irq_domain

chip_data
    platform-specific per-chip private data for the chip
    methods, to allow shared chip implementations

.. _`irq_chip`:

struct irq_chip
===============

.. c:type:: struct irq_chip

    hardware interrupt chip descriptor

.. _`irq_chip.definition`:

Definition
----------

.. code-block:: c

    struct irq_chip {
        struct device *parent_device;
        const char *name;
        unsigned int (*irq_startup)(struct irq_data *data);
        void (*irq_shutdown)(struct irq_data *data);
        void (*irq_enable)(struct irq_data *data);
        void (*irq_disable)(struct irq_data *data);
        void (*irq_ack)(struct irq_data *data);
        void (*irq_mask)(struct irq_data *data);
        void (*irq_mask_ack)(struct irq_data *data);
        void (*irq_unmask)(struct irq_data *data);
        void (*irq_eoi)(struct irq_data *data);
        int (*irq_set_affinity)(struct irq_data *data, const struct cpumask *dest, bool force);
        int (*irq_retrigger)(struct irq_data *data);
        int (*irq_set_type)(struct irq_data *data, unsigned int flow_type);
        int (*irq_set_wake)(struct irq_data *data, unsigned int on);
        void (*irq_bus_lock)(struct irq_data *data);
        void (*irq_bus_sync_unlock)(struct irq_data *data);
        void (*irq_cpu_online)(struct irq_data *data);
        void (*irq_cpu_offline)(struct irq_data *data);
        void (*irq_suspend)(struct irq_data *data);
        void (*irq_resume)(struct irq_data *data);
        void (*irq_pm_shutdown)(struct irq_data *data);
        void (*irq_calc_mask)(struct irq_data *data);
        void (*irq_print_chip)(struct irq_data *data, struct seq_file *p);
        int (*irq_request_resources)(struct irq_data *data);
        void (*irq_release_resources)(struct irq_data *data);
        void (*irq_compose_msi_msg)(struct irq_data *data, struct msi_msg *msg);
        void (*irq_write_msi_msg)(struct irq_data *data, struct msi_msg *msg);
        int (*irq_get_irqchip_state)(struct irq_data *data, enum irqchip_irq_state which, bool *state);
        int (*irq_set_irqchip_state)(struct irq_data *data, enum irqchip_irq_state which, bool state);
        int (*irq_set_vcpu_affinity)(struct irq_data *data, void *vcpu_info);
        void (*ipi_send_single)(struct irq_data *data, unsigned int cpu);
        void (*ipi_send_mask)(struct irq_data *data, const struct cpumask *dest);
        unsigned long flags;
    }

.. _`irq_chip.members`:

Members
-------

parent_device
    pointer to parent device for irqchip

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
    Set the CPU affinity on SMP machines. If the force
    argument is true, it tells the driver to
    unconditionally apply the affinity setting. Sanity
    checks against the supplied affinity mask are not
    required. This is used for CPU hotplug where the
    target CPU is not yet set in the cpu_online_mask.

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
    function called from core code on suspend once per
    chip, when one or more interrupts are installed

irq_resume
    function called from core code on resume once per chip,
    when one ore more interrupts are installed

irq_pm_shutdown
    function called from core code on shutdown once per chip

irq_calc_mask
    Optional function to set irq_data.mask for special cases

irq_print_chip
    optional to print special chip info in show_interrupts

irq_request_resources
    optional to request resources before calling
    any other callback related to this irq

irq_release_resources
    optional to release resources acquired with
    irq_request_resources

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

.. _`irq_chip_regs`:

struct irq_chip_regs
====================

.. c:type:: struct irq_chip_regs

    register offsets for struct irq_gci

.. _`irq_chip_regs.definition`:

Definition
----------

.. code-block:: c

    struct irq_chip_regs {
        unsigned long enable;
        unsigned long disable;
        unsigned long mask;
        unsigned long ack;
        unsigned long eoi;
        unsigned long type;
        unsigned long polarity;
    }

.. _`irq_chip_regs.members`:

Members
-------

enable
    Enable register offset to reg_base

disable
    Disable register offset to reg_base

mask
    Mask register offset to reg_base

ack
    Ack register offset to reg_base

eoi
    Eoi register offset to reg_base

type
    Type configuration register offset to reg_base

polarity
    Polarity configuration register offset to reg_base

.. _`irq_chip_type`:

struct irq_chip_type
====================

.. c:type:: struct irq_chip_type

    Generic interrupt chip instance for a flow type

.. _`irq_chip_type.definition`:

Definition
----------

.. code-block:: c

    struct irq_chip_type {
        struct irq_chip chip;
        struct irq_chip_regs regs;
        irq_flow_handler_t handler;
        u32 type;
        u32 mask_cache_priv;
        u32 *mask_cache;
    }

.. _`irq_chip_type.members`:

Members
-------

chip
    The real interrupt chip which provides the callbacks

regs
    Register offsets for this chip

handler
    Flow handler associated with this chip

type
    Chip can handle these flow types

mask_cache_priv
    Cached mask register private to the chip type

mask_cache
    Pointer to cached mask register

.. _`irq_chip_type.description`:

Description
-----------

A irq_generic_chip can have several instances of irq_chip_type when
it requires different functions and register offsets for different
flow types.

.. _`irq_chip_generic`:

struct irq_chip_generic
=======================

.. c:type:: struct irq_chip_generic

    Generic irq chip data structure

.. _`irq_chip_generic.definition`:

Definition
----------

.. code-block:: c

    struct irq_chip_generic {
        raw_spinlock_t lock;
        void __iomem *reg_base;
        u32 (*reg_readl)(void __iomem *addr);
        void (*reg_writel)(u32 val, void __iomem *addr);
        void (*suspend)(struct irq_chip_generic *gc);
        void (*resume)(struct irq_chip_generic *gc);
        unsigned int irq_base;
        unsigned int irq_cnt;
        u32 mask_cache;
        u32 type_cache;
        u32 polarity_cache;
        u32 wake_enabled;
        u32 wake_active;
        unsigned int num_ct;
        void *private;
        unsigned long installed;
        unsigned long unused;
        struct irq_domain *domain;
        struct list_head list;
        struct irq_chip_type chip_types[0];
    }

.. _`irq_chip_generic.members`:

Members
-------

lock
    Lock to protect register and cache data access

reg_base
    Register base address (virtual)

reg_readl
    Alternate I/O accessor (defaults to readl if NULL)

reg_writel
    Alternate I/O accessor (defaults to writel if NULL)

suspend
    Function called from core code on suspend once per
    chip; can be useful instead of irq_chip::suspend to
    handle chip details even when no interrupts are in use

resume
    Function called from core code on resume once per chip;
    can be useful instead of irq_chip::suspend to handle
    chip details even when no interrupts are in use

irq_base
    Interrupt base nr for this chip

irq_cnt
    Number of interrupts handled by this chip

mask_cache
    Cached mask register shared between all chip types

type_cache
    Cached type register

polarity_cache
    Cached polarity register

wake_enabled
    Interrupt can wakeup from suspend

wake_active
    Interrupt is marked as an wakeup from suspend source

num_ct
    Number of available irq_chip_type instances (usually 1)

private
    Private data for non generic chip callbacks

installed
    bitfield to denote installed interrupts

unused
    bitfield to denote unused interrupts

domain
    irq domain pointer

list
    List head for keeping track of instances

chip_types
    Array of interrupt irq_chip_types

.. _`irq_chip_generic.description`:

Description
-----------

Note, that irq_chip_generic can have multiple irq_chip_type
implementations which can be associated to a particular irq line of
an irq_chip_generic instance. That allows to share and protect
state in an irq_chip_generic instance when we need to implement
different flow mechanisms (level/edge) for it.

.. _`irq_gc_flags`:

enum irq_gc_flags
=================

.. c:type:: enum irq_gc_flags

    Initialization flags for generic irq chips

.. _`irq_gc_flags.definition`:

Definition
----------

.. code-block:: c

    enum irq_gc_flags {
        IRQ_GC_INIT_MASK_CACHE,
        IRQ_GC_INIT_NESTED_LOCK,
        IRQ_GC_MASK_CACHE_PER_TYPE,
        IRQ_GC_NO_MASK,
        IRQ_GC_BE_IO
    };

.. _`irq_gc_flags.constants`:

Constants
---------

IRQ_GC_INIT_MASK_CACHE
    Initialize the mask_cache by reading mask reg

IRQ_GC_INIT_NESTED_LOCK
    Set the lock class of the irqs to nested for
    irq chips which need to call \ :c:func:`irq_set_wake`\  on
    the parent irq. Usually GPIO implementations

IRQ_GC_MASK_CACHE_PER_TYPE
    Mask cache is chip type private

IRQ_GC_NO_MASK
    Do not calculate irq_data->mask

IRQ_GC_BE_IO
    Use big-endian register accesses (default: LE)

.. This file was automatic generated / don't edit.

