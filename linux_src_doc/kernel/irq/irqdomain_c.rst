.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/irqdomain.c

.. _`__irq_domain_alloc_fwnode`:

\__irq_domain_alloc_fwnode
==========================

.. c:function:: struct fwnode_handle *__irq_domain_alloc_fwnode(unsigned int type, int id, const char *name, void *data)

    Allocate a fwnode_handle suitable for identifying an irq domain

    :param type:
        Type of irqchip_fwnode. See linux/irqdomain.h
    :type type: unsigned int

    :param id:
        Optional user provided id if name != NULL
    :type id: int

    :param name:
        Optional user provided domain name
    :type name: const char \*

    :param data:
        Optional user-provided data
    :type data: void \*

.. _`__irq_domain_alloc_fwnode.description`:

Description
-----------

Allocate a struct irqchip_fwid, and return a poiner to the embedded
fwnode_handle (or NULL on failure).

.. _`__irq_domain_alloc_fwnode.note`:

Note
----

The types IRQCHIP_FWNODE_NAMED and IRQCHIP_FWNODE_NAMED_ID are
solely to transport name information to irqdomain creation code. The
node is not stored. For other types the pointer is kept in the irq
domain struct.

.. _`irq_domain_free_fwnode`:

irq_domain_free_fwnode
======================

.. c:function:: void irq_domain_free_fwnode(struct fwnode_handle *fwnode)

    Free a non-OF-backed fwnode_handle

    :param fwnode:
        *undescribed*
    :type fwnode: struct fwnode_handle \*

.. _`irq_domain_free_fwnode.description`:

Description
-----------

Free a fwnode_handle allocated with irq_domain_alloc_fwnode.

.. _`__irq_domain_add`:

\__irq_domain_add
=================

.. c:function:: struct irq_domain *__irq_domain_add(struct fwnode_handle *fwnode, int size, irq_hw_number_t hwirq_max, int direct_max, const struct irq_domain_ops *ops, void *host_data)

    Allocate a new irq_domain data structure

    :param fwnode:
        firmware node for the interrupt controller
    :type fwnode: struct fwnode_handle \*

    :param size:
        Size of linear map; 0 for radix mapping only
    :type size: int

    :param hwirq_max:
        Maximum number of interrupts supported by controller
    :type hwirq_max: irq_hw_number_t

    :param direct_max:
        Maximum value of direct maps; Use ~0 for no limit; 0 for no
        direct mapping
    :type direct_max: int

    :param ops:
        domain callbacks
    :type ops: const struct irq_domain_ops \*

    :param host_data:
        Controller private data pointer
    :type host_data: void \*

.. _`__irq_domain_add.description`:

Description
-----------

Allocates and initialize and irq_domain structure.
Returns pointer to IRQ domain, or NULL on failure.

.. _`irq_domain_remove`:

irq_domain_remove
=================

.. c:function:: void irq_domain_remove(struct irq_domain *domain)

    Remove an irq domain.

    :param domain:
        domain to remove
    :type domain: struct irq_domain \*

.. _`irq_domain_remove.description`:

Description
-----------

This routine is used to remove an irq domain. The caller must ensure
that all mappings within the domain have been disposed of prior to
use, depending on the revmap type.

.. _`irq_domain_add_simple`:

irq_domain_add_simple
=====================

.. c:function:: struct irq_domain *irq_domain_add_simple(struct device_node *of_node, unsigned int size, unsigned int first_irq, const struct irq_domain_ops *ops, void *host_data)

    Register an irq_domain and optionally map a range of irqs

    :param of_node:
        pointer to interrupt controller's device tree node.
    :type of_node: struct device_node \*

    :param size:
        total number of irqs in mapping
    :type size: unsigned int

    :param first_irq:
        first number of irq block assigned to the domain,
        pass zero to assign irqs on-the-fly. If first_irq is non-zero, then
        pre-map all of the irqs in the domain to virqs starting at first_irq.
    :type first_irq: unsigned int

    :param ops:
        domain callbacks
    :type ops: const struct irq_domain_ops \*

    :param host_data:
        Controller private data pointer
    :type host_data: void \*

.. _`irq_domain_add_simple.description`:

Description
-----------

Allocates an irq_domain, and optionally if first_irq is positive then also
allocate irq_descs and map all of the hwirqs to virqs starting at first_irq.

This is intended to implement the expected behaviour for most
interrupt controllers. If device tree is used, then first_irq will be 0 and
irqs get mapped dynamically on the fly. However, if the controller requires
static virq assignments (non-DT boot) then it will set that up correctly.

.. _`irq_domain_add_legacy`:

irq_domain_add_legacy
=====================

.. c:function:: struct irq_domain *irq_domain_add_legacy(struct device_node *of_node, unsigned int size, unsigned int first_irq, irq_hw_number_t first_hwirq, const struct irq_domain_ops *ops, void *host_data)

    Allocate and register a legacy revmap irq_domain.

    :param of_node:
        pointer to interrupt controller's device tree node.
    :type of_node: struct device_node \*

    :param size:
        total number of irqs in legacy mapping
    :type size: unsigned int

    :param first_irq:
        first number of irq block assigned to the domain
    :type first_irq: unsigned int

    :param first_hwirq:
        first hwirq number to use for the translation. Should normally
        be '0', but a positive integer can be used if the effective
        hwirqs numbering does not begin at zero.
    :type first_hwirq: irq_hw_number_t

    :param ops:
        map/unmap domain callbacks
    :type ops: const struct irq_domain_ops \*

    :param host_data:
        Controller private data pointer
    :type host_data: void \*

.. _`irq_domain_add_legacy.note`:

Note
----

the \ :c:func:`map`\  callback will be called before this function returns
for all legacy interrupts except 0 (which is always the invalid irq for
a legacy controller).

.. _`irq_find_matching_fwspec`:

irq_find_matching_fwspec
========================

.. c:function:: struct irq_domain *irq_find_matching_fwspec(struct irq_fwspec *fwspec, enum irq_domain_bus_token bus_token)

    Locates a domain for a given fwspec

    :param fwspec:
        FW specifier for an interrupt
    :type fwspec: struct irq_fwspec \*

    :param bus_token:
        domain-specific data
    :type bus_token: enum irq_domain_bus_token

.. _`irq_domain_check_msi_remap`:

irq_domain_check_msi_remap
==========================

.. c:function:: bool irq_domain_check_msi_remap( void)

    Check whether all MSI irq domains implement IRQ remapping

    :param void:
        no arguments
    :type void: 

.. _`irq_domain_check_msi_remap.return`:

Return
------

false if any MSI irq domain does not support IRQ remapping,
true otherwise (including if there is no MSI irq domain)

.. _`irq_set_default_host`:

irq_set_default_host
====================

.. c:function:: void irq_set_default_host(struct irq_domain *domain)

    Set a "default" irq domain

    :param domain:
        default domain pointer
    :type domain: struct irq_domain \*

.. _`irq_set_default_host.description`:

Description
-----------

For convenience, it's possible to set a "default" domain that will be used
whenever NULL is passed to \ :c:func:`irq_create_mapping`\ . It makes life easier for
platforms that want to manipulate a few hard coded interrupt numbers that
aren't properly represented in the device-tree.

.. _`irq_create_direct_mapping`:

irq_create_direct_mapping
=========================

.. c:function:: unsigned int irq_create_direct_mapping(struct irq_domain *domain)

    Allocate an irq for direct mapping

    :param domain:
        domain to allocate the irq for or NULL for default domain
    :type domain: struct irq_domain \*

.. _`irq_create_direct_mapping.description`:

Description
-----------

This routine is used for irq controllers which can choose the hardware
interrupt numbers they generate. In such a case it's simplest to use
the linux irq as the hardware interrupt number. It still uses the linear
or radix tree to store the mapping, but the irq controller can optimize
the revmap path by using the hwirq directly.

.. _`irq_create_mapping`:

irq_create_mapping
==================

.. c:function:: unsigned int irq_create_mapping(struct irq_domain *domain, irq_hw_number_t hwirq)

    Map a hardware interrupt into linux irq space

    :param domain:
        domain owning this hardware interrupt or NULL for default domain
    :type domain: struct irq_domain \*

    :param hwirq:
        hardware irq number in that domain space
    :type hwirq: irq_hw_number_t

.. _`irq_create_mapping.description`:

Description
-----------

Only one mapping per hardware interrupt is permitted. Returns a linux
irq number.
If the sense/trigger is to be specified, \ :c:func:`set_irq_type`\  should be called
on the number returned from that call.

.. _`irq_create_strict_mappings`:

irq_create_strict_mappings
==========================

.. c:function:: int irq_create_strict_mappings(struct irq_domain *domain, unsigned int irq_base, irq_hw_number_t hwirq_base, int count)

    Map a range of hw irqs to fixed linux irqs

    :param domain:
        domain owning the interrupt range
    :type domain: struct irq_domain \*

    :param irq_base:
        beginning of linux IRQ range
    :type irq_base: unsigned int

    :param hwirq_base:
        beginning of hardware IRQ range
    :type hwirq_base: irq_hw_number_t

    :param count:
        Number of interrupts to map
    :type count: int

.. _`irq_create_strict_mappings.description`:

Description
-----------

This routine is used for allocating and mapping a range of hardware
irqs to linux irqs where the linux irq numbers are at pre-defined
locations. For use by controllers that already have static mappings
to insert in to the domain.

Non-linear users can use \ :c:func:`irq_create_identity_mapping`\  for IRQ-at-a-time
domain insertion.

0 is returned upon success, while any failure to establish a static
mapping is treated as an error.

.. _`irq_dispose_mapping`:

irq_dispose_mapping
===================

.. c:function:: void irq_dispose_mapping(unsigned int virq)

    Unmap an interrupt

    :param virq:
        linux irq number of the interrupt to unmap
    :type virq: unsigned int

.. _`irq_find_mapping`:

irq_find_mapping
================

.. c:function:: unsigned int irq_find_mapping(struct irq_domain *domain, irq_hw_number_t hwirq)

    Find a linux irq from a hw irq number.

    :param domain:
        domain owning this hardware interrupt
    :type domain: struct irq_domain \*

    :param hwirq:
        hardware irq number in that domain space
    :type hwirq: irq_hw_number_t

.. _`irq_domain_xlate_onecell`:

irq_domain_xlate_onecell
========================

.. c:function:: int irq_domain_xlate_onecell(struct irq_domain *d, struct device_node *ctrlr, const u32 *intspec, unsigned int intsize, unsigned long *out_hwirq, unsigned int *out_type)

    Generic xlate for direct one cell bindings

    :param d:
        *undescribed*
    :type d: struct irq_domain \*

    :param ctrlr:
        *undescribed*
    :type ctrlr: struct device_node \*

    :param intspec:
        *undescribed*
    :type intspec: const u32 \*

    :param intsize:
        *undescribed*
    :type intsize: unsigned int

    :param out_hwirq:
        *undescribed*
    :type out_hwirq: unsigned long \*

    :param out_type:
        *undescribed*
    :type out_type: unsigned int \*

.. _`irq_domain_xlate_onecell.description`:

Description
-----------

Device Tree IRQ specifier translation function which works with one cell
bindings where the cell value maps directly to the hwirq number.

.. _`irq_domain_xlate_twocell`:

irq_domain_xlate_twocell
========================

.. c:function:: int irq_domain_xlate_twocell(struct irq_domain *d, struct device_node *ctrlr, const u32 *intspec, unsigned int intsize, irq_hw_number_t *out_hwirq, unsigned int *out_type)

    Generic xlate for direct two cell bindings

    :param d:
        *undescribed*
    :type d: struct irq_domain \*

    :param ctrlr:
        *undescribed*
    :type ctrlr: struct device_node \*

    :param intspec:
        *undescribed*
    :type intspec: const u32 \*

    :param intsize:
        *undescribed*
    :type intsize: unsigned int

    :param out_hwirq:
        *undescribed*
    :type out_hwirq: irq_hw_number_t \*

    :param out_type:
        *undescribed*
    :type out_type: unsigned int \*

.. _`irq_domain_xlate_twocell.description`:

Description
-----------

Device Tree IRQ specifier translation function which works with two cell
bindings where the cell values map directly to the hwirq number
and linux irq flags.

.. _`irq_domain_xlate_onetwocell`:

irq_domain_xlate_onetwocell
===========================

.. c:function:: int irq_domain_xlate_onetwocell(struct irq_domain *d, struct device_node *ctrlr, const u32 *intspec, unsigned int intsize, unsigned long *out_hwirq, unsigned int *out_type)

    Generic xlate for one or two cell bindings

    :param d:
        *undescribed*
    :type d: struct irq_domain \*

    :param ctrlr:
        *undescribed*
    :type ctrlr: struct device_node \*

    :param intspec:
        *undescribed*
    :type intspec: const u32 \*

    :param intsize:
        *undescribed*
    :type intsize: unsigned int

    :param out_hwirq:
        *undescribed*
    :type out_hwirq: unsigned long \*

    :param out_type:
        *undescribed*
    :type out_type: unsigned int \*

.. _`irq_domain_xlate_onetwocell.description`:

Description
-----------

Device Tree IRQ specifier translation function which works with either one
or two cell bindings where the cell values map directly to the hwirq number
and linux irq flags.

.. _`irq_domain_xlate_onetwocell.note`:

Note
----

don't use this function unless your interrupt controller explicitly
supports both one and two cell bindings.  For the majority of controllers
the \_onecell() or \_twocell() variants above should be used.

.. _`irq_domain_create_hierarchy`:

irq_domain_create_hierarchy
===========================

.. c:function:: struct irq_domain *irq_domain_create_hierarchy(struct irq_domain *parent, unsigned int flags, unsigned int size, struct fwnode_handle *fwnode, const struct irq_domain_ops *ops, void *host_data)

    Add a irqdomain into the hierarchy

    :param parent:
        Parent irq domain to associate with the new domain
    :type parent: struct irq_domain \*

    :param flags:
        Irq domain flags associated to the domain
    :type flags: unsigned int

    :param size:
        Size of the domain. See below
    :type size: unsigned int

    :param fwnode:
        Optional fwnode of the interrupt controller
    :type fwnode: struct fwnode_handle \*

    :param ops:
        Pointer to the interrupt domain callbacks
    :type ops: const struct irq_domain_ops \*

    :param host_data:
        Controller private data pointer
    :type host_data: void \*

.. _`irq_domain_create_hierarchy.description`:

Description
-----------

If \ ``size``\  is 0 a tree domain is created, otherwise a linear domain.

If successful the parent is associated to the new domain and the
domain flags are set.
Returns pointer to IRQ domain, or NULL on failure.

.. _`irq_domain_get_irq_data`:

irq_domain_get_irq_data
=======================

.. c:function:: struct irq_data *irq_domain_get_irq_data(struct irq_domain *domain, unsigned int virq)

    Get irq_data associated with \ ``virq``\  and \ ``domain``\ 

    :param domain:
        domain to match
    :type domain: struct irq_domain \*

    :param virq:
        IRQ number to get irq_data
    :type virq: unsigned int

.. _`irq_domain_set_hwirq_and_chip`:

irq_domain_set_hwirq_and_chip
=============================

.. c:function:: int irq_domain_set_hwirq_and_chip(struct irq_domain *domain, unsigned int virq, irq_hw_number_t hwirq, struct irq_chip *chip, void *chip_data)

    Set hwirq and irqchip of \ ``virq``\  at \ ``domain``\ 

    :param domain:
        Interrupt domain to match
    :type domain: struct irq_domain \*

    :param virq:
        IRQ number
    :type virq: unsigned int

    :param hwirq:
        The hwirq number
    :type hwirq: irq_hw_number_t

    :param chip:
        The associated interrupt chip
    :type chip: struct irq_chip \*

    :param chip_data:
        The associated chip data
    :type chip_data: void \*

.. _`irq_domain_set_info`:

irq_domain_set_info
===================

.. c:function:: void irq_domain_set_info(struct irq_domain *domain, unsigned int virq, irq_hw_number_t hwirq, struct irq_chip *chip, void *chip_data, irq_flow_handler_t handler, void *handler_data, const char *handler_name)

    Set the complete data for a \ ``virq``\  in \ ``domain``\ 

    :param domain:
        Interrupt domain to match
    :type domain: struct irq_domain \*

    :param virq:
        IRQ number
    :type virq: unsigned int

    :param hwirq:
        The hardware interrupt number
    :type hwirq: irq_hw_number_t

    :param chip:
        The associated interrupt chip
    :type chip: struct irq_chip \*

    :param chip_data:
        The associated interrupt chip data
    :type chip_data: void \*

    :param handler:
        The interrupt flow handler
    :type handler: irq_flow_handler_t

    :param handler_data:
        The interrupt flow handler data
    :type handler_data: void \*

    :param handler_name:
        The interrupt handler name
    :type handler_name: const char \*

.. _`irq_domain_reset_irq_data`:

irq_domain_reset_irq_data
=========================

.. c:function:: void irq_domain_reset_irq_data(struct irq_data *irq_data)

    Clear hwirq, chip and chip_data in \ ``irq_data``\ 

    :param irq_data:
        The pointer to irq_data
    :type irq_data: struct irq_data \*

.. _`irq_domain_free_irqs_common`:

irq_domain_free_irqs_common
===========================

.. c:function:: void irq_domain_free_irqs_common(struct irq_domain *domain, unsigned int virq, unsigned int nr_irqs)

    Clear irq_data and free the parent

    :param domain:
        Interrupt domain to match
    :type domain: struct irq_domain \*

    :param virq:
        IRQ number to start with
    :type virq: unsigned int

    :param nr_irqs:
        The number of irqs to free
    :type nr_irqs: unsigned int

.. _`irq_domain_free_irqs_top`:

irq_domain_free_irqs_top
========================

.. c:function:: void irq_domain_free_irqs_top(struct irq_domain *domain, unsigned int virq, unsigned int nr_irqs)

    Clear handler and handler data, clear irqdata and free parent

    :param domain:
        Interrupt domain to match
    :type domain: struct irq_domain \*

    :param virq:
        IRQ number to start with
    :type virq: unsigned int

    :param nr_irqs:
        The number of irqs to free
    :type nr_irqs: unsigned int

.. _`__irq_domain_alloc_irqs`:

\__irq_domain_alloc_irqs
========================

.. c:function:: int __irq_domain_alloc_irqs(struct irq_domain *domain, int irq_base, unsigned int nr_irqs, int node, void *arg, bool realloc, const struct cpumask *affinity)

    Allocate IRQs from domain

    :param domain:
        domain to allocate from
    :type domain: struct irq_domain \*

    :param irq_base:
        allocate specified IRQ nubmer if irq_base >= 0
    :type irq_base: int

    :param nr_irqs:
        number of IRQs to allocate
    :type nr_irqs: unsigned int

    :param node:
        NUMA node id for memory allocation
    :type node: int

    :param arg:
        domain specific argument
    :type arg: void \*

    :param realloc:
        IRQ descriptors have already been allocated if true
    :type realloc: bool

    :param affinity:
        Optional irq affinity mask for multiqueue devices
    :type affinity: const struct cpumask \*

.. _`__irq_domain_alloc_irqs.description`:

Description
-----------

Allocate IRQ numbers and initialized all data structures to support
hierarchy IRQ domains.
Parameter \ ``realloc``\  is mainly to support legacy IRQs.
Returns error code or allocated IRQ number

The whole process to setup an IRQ has been split into two steps.
The first step, \__irq_domain_alloc_irqs(), is to allocate IRQ
descriptor and required hardware resources. The second step,
\ :c:func:`irq_domain_activate_irq`\ , is to program hardwares with preallocated
resources. In this way, it's easier to rollback when failing to
allocate resources.

.. _`irq_domain_push_irq`:

irq_domain_push_irq
===================

.. c:function:: int irq_domain_push_irq(struct irq_domain *domain, int virq, void *arg)

    Push a domain in to the top of a hierarchy.

    :param domain:
        Domain to push.
    :type domain: struct irq_domain \*

    :param virq:
        Irq to push the domain in to.
    :type virq: int

    :param arg:
        Passed to the irq_domain_ops \ :c:func:`alloc`\  function.
    :type arg: void \*

.. _`irq_domain_push_irq.description`:

Description
-----------

For an already existing irqdomain hierarchy, as might be obtained
via a call to \ :c:func:`pci_enable_msix`\ , add an additional domain to the
head of the processing chain.  Must be called before \ :c:func:`request_irq`\ 
has been called.

.. _`irq_domain_pop_irq`:

irq_domain_pop_irq
==================

.. c:function:: int irq_domain_pop_irq(struct irq_domain *domain, int virq)

    Remove a domain from the top of a hierarchy.

    :param domain:
        Domain to remove.
    :type domain: struct irq_domain \*

    :param virq:
        Irq to remove the domain from.
    :type virq: int

.. _`irq_domain_pop_irq.description`:

Description
-----------

Undo the effects of a call to \ :c:func:`irq_domain_push_irq`\ .  Must be
called either before \ :c:func:`request_irq`\  or after \ :c:func:`free_irq`\ .

.. _`irq_domain_free_irqs`:

irq_domain_free_irqs
====================

.. c:function:: void irq_domain_free_irqs(unsigned int virq, unsigned int nr_irqs)

    Free IRQ number and associated data structures

    :param virq:
        base IRQ number
    :type virq: unsigned int

    :param nr_irqs:
        number of IRQs to free
    :type nr_irqs: unsigned int

.. _`irq_domain_alloc_irqs_parent`:

irq_domain_alloc_irqs_parent
============================

.. c:function:: int irq_domain_alloc_irqs_parent(struct irq_domain *domain, unsigned int irq_base, unsigned int nr_irqs, void *arg)

    Allocate interrupts from parent domain

    :param domain:
        *undescribed*
    :type domain: struct irq_domain \*

    :param irq_base:
        Base IRQ number
    :type irq_base: unsigned int

    :param nr_irqs:
        Number of IRQs to allocate
    :type nr_irqs: unsigned int

    :param arg:
        Allocation data (arch/domain specific)
    :type arg: void \*

.. _`irq_domain_alloc_irqs_parent.description`:

Description
-----------

Check whether the domain has been setup recursive. If not allocate
through the parent domain.

.. _`irq_domain_free_irqs_parent`:

irq_domain_free_irqs_parent
===========================

.. c:function:: void irq_domain_free_irqs_parent(struct irq_domain *domain, unsigned int irq_base, unsigned int nr_irqs)

    Free interrupts from parent domain

    :param domain:
        *undescribed*
    :type domain: struct irq_domain \*

    :param irq_base:
        Base IRQ number
    :type irq_base: unsigned int

    :param nr_irqs:
        Number of IRQs to free
    :type nr_irqs: unsigned int

.. _`irq_domain_free_irqs_parent.description`:

Description
-----------

Check whether the domain has been setup recursive. If not free
through the parent domain.

.. _`irq_domain_activate_irq`:

irq_domain_activate_irq
=======================

.. c:function:: int irq_domain_activate_irq(struct irq_data *irq_data, bool reserve)

    Call domain_ops->activate recursively to activate interrupt

    :param irq_data:
        Outermost irq_data associated with interrupt
    :type irq_data: struct irq_data \*

    :param reserve:
        If set only reserve an interrupt vector instead of assigning one
    :type reserve: bool

.. _`irq_domain_activate_irq.description`:

Description
-----------

This is the second step to call domain_ops->activate to program interrupt
controllers, so the interrupt could actually get delivered.

.. _`irq_domain_deactivate_irq`:

irq_domain_deactivate_irq
=========================

.. c:function:: void irq_domain_deactivate_irq(struct irq_data *irq_data)

    Call domain_ops->deactivate recursively to deactivate interrupt

    :param irq_data:
        outermost irq_data associated with interrupt
    :type irq_data: struct irq_data \*

.. _`irq_domain_deactivate_irq.description`:

Description
-----------

It calls domain_ops->deactivate to program interrupt controllers to disable
interrupt delivery.

.. _`irq_domain_hierarchical_is_msi_remap`:

irq_domain_hierarchical_is_msi_remap
====================================

.. c:function:: bool irq_domain_hierarchical_is_msi_remap(struct irq_domain *domain)

    Check if the domain or any parent has MSI remapping support

    :param domain:
        domain pointer
    :type domain: struct irq_domain \*

.. _`irq_domain_get_irq_data`:

irq_domain_get_irq_data
=======================

.. c:function:: struct irq_data *irq_domain_get_irq_data(struct irq_domain *domain, unsigned int virq)

    Get irq_data associated with \ ``virq``\  and \ ``domain``\ 

    :param domain:
        domain to match
    :type domain: struct irq_domain \*

    :param virq:
        IRQ number to get irq_data
    :type virq: unsigned int

.. _`irq_domain_set_info`:

irq_domain_set_info
===================

.. c:function:: void irq_domain_set_info(struct irq_domain *domain, unsigned int virq, irq_hw_number_t hwirq, struct irq_chip *chip, void *chip_data, irq_flow_handler_t handler, void *handler_data, const char *handler_name)

    Set the complete data for a \ ``virq``\  in \ ``domain``\ 

    :param domain:
        Interrupt domain to match
    :type domain: struct irq_domain \*

    :param virq:
        IRQ number
    :type virq: unsigned int

    :param hwirq:
        The hardware interrupt number
    :type hwirq: irq_hw_number_t

    :param chip:
        The associated interrupt chip
    :type chip: struct irq_chip \*

    :param chip_data:
        The associated interrupt chip data
    :type chip_data: void \*

    :param handler:
        The interrupt flow handler
    :type handler: irq_flow_handler_t

    :param handler_data:
        The interrupt flow handler data
    :type handler_data: void \*

    :param handler_name:
        The interrupt handler name
    :type handler_name: const char \*

.. This file was automatic generated / don't edit.

