.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dax/dax.c

.. _`dax_region`:

struct dax_region
=================

.. c:type:: struct dax_region

    mapping infrastructure for dax devices

.. _`dax_region.definition`:

Definition
----------

.. code-block:: c

    struct dax_region {
        int id;
        struct ida ida;
        void *base;
        struct kref kref;
        struct device *dev;
        unsigned int align;
        struct resource res;
        unsigned long pfn_flags;
    }

.. _`dax_region.members`:

Members
-------

id
    kernel-wide unique region for a memory range

ida
    *undescribed*

base
    linear address corresponding to \ ``res``\ 

kref
    to pin while other agents have a need to do lookups

dev
    parent device backing this region

align
    allocation and mapping alignment for child dax devices

res
    physical address range of the region

pfn_flags
    identify whether the pfns are paged back or not

.. _`dax_dev`:

struct dax_dev
==============

.. c:type:: struct dax_dev

    subdivision of a dax region \ ``region``\  - parent region \ ``dev``\  - device backing the character device \ ``kref``\  - enable this data to be tracked in filp->private_data \ ``alive``\  - !alive + rcu grace period == no new mappings can be established \ ``id``\  - child id in the region \ ``num_resources``\  - number of physical address extents in this device \ ``res``\  - array of physical address ranges

.. _`dax_dev.definition`:

Definition
----------

.. code-block:: c

    struct dax_dev {
        struct dax_region *region;
        struct device *dev;
        struct kref kref;
        bool alive;
        int id;
        int num_resources;
        struct resource res[0];
    }

.. _`dax_dev.members`:

Members
-------

region
    *undescribed*

dev
    *undescribed*

kref
    *undescribed*

alive
    *undescribed*

id
    *undescribed*

num_resources
    *undescribed*

.. This file was automatic generated / don't edit.

