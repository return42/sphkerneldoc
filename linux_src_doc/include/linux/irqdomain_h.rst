.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/irqdomain.h

.. _`irq_fwspec`:

struct irq_fwspec
=================

.. c:type:: struct irq_fwspec

    generic IRQ specifier structure

.. _`irq_fwspec.definition`:

Definition
----------

.. code-block:: c

    struct irq_fwspec {
        struct fwnode_handle *fwnode;
        int param_count;
        u32 param[IRQ_DOMAIN_IRQ_SPEC_PARAMS];
    }

.. _`irq_fwspec.members`:

Members
-------

fwnode
    Pointer to a firmware-specific descriptor

param_count
    Number of device-specific parameters

param
    Device-specific parameters

.. _`irq_fwspec.description`:

Description
-----------

This structure, directly modeled after of_phandle_args, is used to
pass a device-specific description of an interrupt.

.. _`irq_domain_ops`:

struct irq_domain_ops
=====================

.. c:type:: struct irq_domain_ops

    Methods for irq_domain objects

.. _`irq_domain_ops.definition`:

Definition
----------

.. code-block:: c

    struct irq_domain_ops {
        int (*match)(struct irq_domain *d, struct device_node *node, enum irq_domain_bus_token bus_token);
        int (*select)(struct irq_domain *d, struct irq_fwspec *fwspec, enum irq_domain_bus_token bus_token);
        int (*map)(struct irq_domain *d, unsigned int virq, irq_hw_number_t hw);
        void (*unmap)(struct irq_domain *d, unsigned int virq);
        int (*xlate)(struct irq_domain *d, struct device_node *node,const u32 *intspec, unsigned int intsize, unsigned long *out_hwirq, unsigned int *out_type);
    #ifdef CONFIG_IRQ_DOMAIN_HIERARCHY
        int (*alloc)(struct irq_domain *d, unsigned int virq, unsigned int nr_irqs, void *arg);
        void (*free)(struct irq_domain *d, unsigned int virq, unsigned int nr_irqs);
        int (*activate)(struct irq_domain *d, struct irq_data *irqd, bool reserve);
        void (*deactivate)(struct irq_domain *d, struct irq_data *irq_data);
        int (*translate)(struct irq_domain *d, struct irq_fwspec *fwspec, unsigned long *out_hwirq, unsigned int *out_type);
    #endif
    #ifdef CONFIG_GENERIC_IRQ_DEBUGFS
        void (*debug_show)(struct seq_file *m, struct irq_domain *d, struct irq_data *irqd, int ind);
    #endif
    }

.. _`irq_domain_ops.members`:

Members
-------

match
    Match an interrupt controller device node to a host, returns
    1 on a match

select
    *undescribed*

map
    Create or update a mapping between a virtual irq number and a hw
    irq number. This is called only once for a given mapping.

unmap
    Dispose of such a mapping

xlate
    Given a device tree node and interrupt specifier, decode
    the hardware irq number and linux irq type value.

alloc
    *undescribed*

free
    *undescribed*

activate
    *undescribed*

deactivate
    *undescribed*

translate
    *undescribed*

debug_show
    *undescribed*

.. _`irq_domain_ops.description`:

Description
-----------

Functions below are provided by the driver and called whenever a new mapping
is created or an old mapping is disposed. The driver can then proceed to
whatever internal data structures management is required. It also needs
to setup the irq_desc when returning from \ :c:func:`map`\ .

.. _`irq_domain`:

struct irq_domain
=================

.. c:type:: struct irq_domain

    Hardware interrupt number translation object

.. _`irq_domain.definition`:

Definition
----------

.. code-block:: c

    struct irq_domain {
        struct list_head link;
        const char *name;
        const struct irq_domain_ops *ops;
        void *host_data;
        unsigned int flags;
        unsigned int mapcount;
        struct fwnode_handle *fwnode;
        enum irq_domain_bus_token bus_token;
        struct irq_domain_chip_generic *gc;
    #ifdef CONFIG_IRQ_DOMAIN_HIERARCHY
        struct irq_domain *parent;
    #endif
    #ifdef CONFIG_GENERIC_IRQ_DEBUGFS
        struct dentry *debugfs_file;
    #endif
        irq_hw_number_t hwirq_max;
        unsigned int revmap_direct_max_irq;
        unsigned int revmap_size;
        struct radix_tree_root revmap_tree;
        struct mutex revmap_tree_mutex;
        unsigned int linear_revmap[];
    }

.. _`irq_domain.members`:

Members
-------

link
    Element in global irq_domain list.

name
    Name of interrupt domain

ops
    pointer to irq_domain methods

host_data
    private data pointer for use by owner.  Not touched by irq_domain
    core code.

flags
    host per irq_domain flags

mapcount
    The number of mapped interrupts

fwnode
    Pointer to firmware node associated with the irq_domain. Pretty easy
    to swap it for the of_node via the irq_domain_get_of_node accessor

bus_token
    *undescribed*

gc
    Pointer to a list of generic chips. There is a helper function for
    setting up one or more generic chips for interrupt controllers
    drivers using the generic chip library which uses this pointer.

parent
    Pointer to parent irq_domain to support hierarchy irq_domains

debugfs_file
    dentry for the domain debugfs file

hwirq_max
    *undescribed*

revmap_direct_max_irq
    The largest hwirq that can be set for controllers that
    support direct mapping

revmap_size
    Size of the linear map table \ ``linear_revmap``\ []

revmap_tree
    Radix map tree for hwirqs that don't fit in the linear map

revmap_tree_mutex
    *undescribed*

linear_revmap
    Linear table of hwirq->virq reverse mappings

.. _`irq_domain.description`:

Description
-----------

Optional elements

Revmap data, used internally by irq_domain

.. _`irq_domain_add_linear`:

irq_domain_add_linear
=====================

.. c:function:: struct irq_domain *irq_domain_add_linear(struct device_node *of_node, unsigned int size, const struct irq_domain_ops *ops, void *host_data)

    Allocate and register a linear revmap irq_domain.

    :param of_node:
        pointer to interrupt controller's device tree node.
    :type of_node: struct device_node \*

    :param size:
        Number of interrupts in the domain.
    :type size: unsigned int

    :param ops:
        map/unmap domain callbacks
    :type ops: const struct irq_domain_ops \*

    :param host_data:
        Controller private data pointer
    :type host_data: void \*

.. _`irq_linear_revmap`:

irq_linear_revmap
=================

.. c:function:: unsigned int irq_linear_revmap(struct irq_domain *domain, irq_hw_number_t hwirq)

    Find a linux irq from a hw irq number.

    :param domain:
        domain owning this hardware interrupt
    :type domain: struct irq_domain \*

    :param hwirq:
        hardware irq number in that domain space
    :type hwirq: irq_hw_number_t

.. _`irq_linear_revmap.description`:

Description
-----------

This is a fast path alternative to \ :c:func:`irq_find_mapping`\  that can be
called directly by irq controller code to save a handful of
instructions. It is always safe to call, but won't find irqs mapped
using the radix tree.

.. This file was automatic generated / don't edit.

