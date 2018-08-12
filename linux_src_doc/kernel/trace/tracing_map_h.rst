.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/tracing_map.h

.. _`tracing_map_ops`:

struct tracing_map_ops
======================

.. c:type:: struct tracing_map_ops

    callbacks for tracing_map

.. _`tracing_map_ops.definition`:

Definition
----------

.. code-block:: c

    struct tracing_map_ops {
        int (*elt_alloc)(struct tracing_map_elt *elt);
        void (*elt_free)(struct tracing_map_elt *elt);
        void (*elt_clear)(struct tracing_map_elt *elt);
        void (*elt_init)(struct tracing_map_elt *elt);
    }

.. _`tracing_map_ops.members`:

Members
-------

elt_alloc
    When a tracing_map_elt is allocated, this function, if
    defined, will be called and gives clients the opportunity to
    allocate additional data and attach it to the element
    (tracing_map_elt->private_data is meant for that purpose).
    Element allocation occurs before tracing begins, when the
    \ :c:func:`tracing_map_init`\  call is made by client code.

elt_free
    When a tracing_map_elt is freed, this function is called
    and allows client-allocated per-element data to be freed.

elt_clear
    This callback allows per-element client-defined data to
    be cleared, if applicable.

elt_init
    This callback allows per-element client-defined data to
    be initialized when used i.e. when the element is actually
    claimed by \ :c:func:`tracing_map_insert`\  in the context of the map
    insertion.

.. _`tracing_map_ops.description`:

Description
-----------

The methods in this structure define callback functions for various
operations on a tracing_map or objects related to a tracing_map.

For a detailed description of tracing_map_elt objects please see
the overview of tracing_map data structures at the beginning of
this file.

All the methods below are optional.

.. This file was automatic generated / don't edit.

