.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/msi.h

.. _`msi_desc`:

struct msi_desc
===============

.. c:type:: struct msi_desc

    Descriptor structure for MSI based interrupts

.. _`msi_desc.definition`:

Definition
----------

.. code-block:: c

    struct msi_desc {
        struct list_head list;
        unsigned int irq;
        unsigned int nvec_used;
        struct device *dev;
        struct msi_msg msg;
        struct cpumask *affinity;
        union {
            struct {
                u32 masked;
                struct {
                    __u8 is_msix : 1;
                    __u8 multiple : 3;
                    __u8 multi_cap : 3;
                    __u8 maskbit : 1;
                    __u8 is_64 : 1;
                    __u16 entry_nr;
                    unsigned default_irq;
                } msi_attrib;
                union {
                    u8 mask_pos;
                    void __iomem *mask_base;
                } ;
            } ;
            struct platform_msi_desc platform;
            struct fsl_mc_msi_desc fsl_mc;
        } ;
    }

.. _`msi_desc.members`:

Members
-------

list
    List head for management

irq
    The base interrupt number

nvec_used
    The number of vectors used

dev
    Pointer to the device which uses this descriptor

msg
    The last set MSI message cached for reuse

affinity
    Optional pointer to a cpu affinity mask for this descriptor

{unnamed_union}
    anonymous

{unnamed_struct}
    anonymous

masked
    [PCI MSI/X] Mask bits

msi_attrib
    *undescribed*

{unnamed_union}
    anonymous

mask_pos
    [PCI MSI]   Mask register position

mask_base
    [PCI MSI-X] Mask register base address

platform
    [platform]  Platform device specific msi descriptor data

fsl_mc
    [fsl-mc]    FSL MC device specific msi descriptor data

.. _`msi_domain_ops`:

struct msi_domain_ops
=====================

.. c:type:: struct msi_domain_ops

    MSI interrupt domain callbacks

.. _`msi_domain_ops.definition`:

Definition
----------

.. code-block:: c

    struct msi_domain_ops {
        irq_hw_number_t (*get_hwirq)(struct msi_domain_info *info, msi_alloc_info_t *arg);
        int (*msi_init)(struct irq_domain *domain,struct msi_domain_info *info,unsigned int virq, irq_hw_number_t hwirq, msi_alloc_info_t *arg);
        void (*msi_free)(struct irq_domain *domain,struct msi_domain_info *info, unsigned int virq);
        int (*msi_check)(struct irq_domain *domain,struct msi_domain_info *info, struct device *dev);
        int (*msi_prepare)(struct irq_domain *domain,struct device *dev, int nvec, msi_alloc_info_t *arg);
        void (*msi_finish)(msi_alloc_info_t *arg, int retval);
        void (*set_desc)(msi_alloc_info_t *arg, struct msi_desc *desc);
        int (*handle_error)(struct irq_domain *domain, struct msi_desc *desc, int error);
    }

.. _`msi_domain_ops.members`:

Members
-------

get_hwirq
    Retrieve the resulting hw irq number

msi_init
    Domain specific init function for MSI interrupts

msi_free
    Domain specific function to free a MSI interrupts

msi_check
    Callback for verification of the domain/info/dev data

msi_prepare
    Prepare the allocation of the interrupts in the domain

msi_finish
    Optional callback to finalize the allocation

set_desc
    Set the msi descriptor for an interrupt

handle_error
    Optional error handler if the allocation fails

.. _`msi_domain_ops.description`:

Description
-----------

\ ``get_hwirq``\ , \ ``msi_init``\  and \ ``msi_free``\  are callbacks used by
\ :c:func:`msi_create_irq_domain`\  and related interfaces

\ ``msi_check``\ , \ ``msi_prepare``\ , \ ``msi_finish``\ , \ ``set_desc``\  and \ ``handle_error``\ 
are callbacks used by \ :c:func:`msi_domain_alloc_irqs`\  and related
interfaces which are based on msi_desc.

.. _`msi_domain_info`:

struct msi_domain_info
======================

.. c:type:: struct msi_domain_info

    MSI interrupt domain data

.. _`msi_domain_info.definition`:

Definition
----------

.. code-block:: c

    struct msi_domain_info {
        u32 flags;
        struct msi_domain_ops *ops;
        struct irq_chip *chip;
        void *chip_data;
        irq_flow_handler_t handler;
        void *handler_data;
        const char *handler_name;
        void *data;
    }

.. _`msi_domain_info.members`:

Members
-------

flags
    Flags to decribe features and capabilities

ops
    The callback data structure

chip
    Optional: associated interrupt chip

chip_data
    Optional: associated interrupt chip data

handler
    Optional: associated interrupt flow handler

handler_data
    Optional: associated interrupt flow handler data

handler_name
    Optional: associated interrupt flow handler name

data
    Optional: domain specific data

.. This file was automatic generated / don't edit.

