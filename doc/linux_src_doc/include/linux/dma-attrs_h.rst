.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dma-attrs.h

.. _`dma_attrs`:

struct dma_attrs
================

.. c:type:: struct dma_attrs

    an opaque container for DMA attributes \ ``flags``\  - bitmask representing a collection of enum dma_attr

.. _`dma_attrs.definition`:

Definition
----------

.. code-block:: c

    struct dma_attrs {
        unsigned long flags[__DMA_ATTRS_LONGS];
    }

.. _`dma_attrs.members`:

Members
-------

.. _`dma_set_attr`:

dma_set_attr
============

.. c:function:: void dma_set_attr(enum dma_attr attr, struct dma_attrs *attrs)

    set a specific attribute

    :param enum dma_attr attr:
        attribute to set

    :param struct dma_attrs \*attrs:
        struct dma_attrs (may be NULL)

.. _`dma_get_attr`:

dma_get_attr
============

.. c:function:: int dma_get_attr(enum dma_attr attr, struct dma_attrs *attrs)

    check for a specific attribute

    :param enum dma_attr attr:
        attribute to set

    :param struct dma_attrs \*attrs:
        struct dma_attrs (may be NULL)

.. This file was automatic generated / don't edit.

