.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dax/dax-private.h

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

.. _`dev_dax`:

struct dev_dax
==============

.. c:type:: struct dev_dax

    instance data for a subdivision of a dax region \ ``region``\  - parent region \ ``dax_dev``\  - core dax functionality \ ``dev``\  - device core \ ``id``\  - child id in the region \ ``num_resources``\  - number of physical address extents in this device \ ``res``\  - array of physical address ranges

.. _`dev_dax.definition`:

Definition
----------

.. code-block:: c

    struct dev_dax {
        struct dax_region *region;
        struct dax_device *dax_dev;
        struct device dev;
        int id;
        int num_resources;
        struct resource res;
    }

.. _`dev_dax.members`:

Members
-------

region
    *undescribed*

dax_dev
    *undescribed*

dev
    *undescribed*

id
    *undescribed*

num_resources
    *undescribed*

res
    *undescribed*

.. This file was automatic generated / don't edit.

