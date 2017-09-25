.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/st_fdma.h

.. _`st_fdma_generic_node`:

struct st_fdma_generic_node
===========================

.. c:type:: struct st_fdma_generic_node

    Free running/paced generic node

.. _`st_fdma_generic_node.definition`:

Definition
----------

.. code-block:: c

    struct st_fdma_generic_node {
        u32 length;
        u32 sstride;
        u32 dstride;
    }

.. _`st_fdma_generic_node.members`:

Members
-------

length
    Length in bytes of a line in a 2D mem to mem

sstride
    Stride, in bytes, between source lines in a 2D data move

dstride
    Stride, in bytes, between destination lines in a 2D data move

.. _`st_fdma_hw_node`:

struct st_fdma_hw_node
======================

.. c:type:: struct st_fdma_hw_node

    Node structure used by fdma hw

.. _`st_fdma_hw_node.definition`:

Definition
----------

.. code-block:: c

    struct st_fdma_hw_node {
        u32 next;
        u32 control;
        u32 nbytes;
        u32 saddr;
        u32 daddr;
        union {
            struct st_fdma_generic_node generic;
        } ;
    }

.. _`st_fdma_hw_node.members`:

Members
-------

next
    Pointer to next node

control
    Transfer Control Parameters

nbytes
    Number of Bytes to read

saddr
    Source address

daddr
    Destination address

{unnamed_union}
    anonymous

.. _`st_fdma_hw_node.description`:

Description
-----------

The NODE structures must be aligned to a 32 byte boundary

.. _`st_fdma_sw_node`:

struct st_fdma_sw_node
======================

.. c:type:: struct st_fdma_sw_node

    descriptor structure for link list

.. _`st_fdma_sw_node.definition`:

Definition
----------

.. code-block:: c

    struct st_fdma_sw_node {
        dma_addr_t pdesc;
        struct st_fdma_hw_node *desc;
    }

.. _`st_fdma_sw_node.members`:

Members
-------

pdesc
    Physical address of desc

desc
    *undescribed*

.. This file was automatic generated / don't edit.

