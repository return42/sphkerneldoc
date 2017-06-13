.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/sort.h

.. _`hist_entry`:

struct hist_entry
=================

.. c:type:: struct hist_entry

    histogram entry

.. _`hist_entry.definition`:

Definition
----------

.. code-block:: c

    struct hist_entry {
        struct rb_node rb_node_in;
        struct rb_node rb_node;
        union {unnamed_union};
        struct callchain_root callchain;
    }

.. _`hist_entry.members`:

Members
-------

rb_node_in
    *undescribed*

rb_node
    *undescribed*

{unnamed_union}
    anonymous


callchain
    *undescribed*

.. _`hist_entry.description`:

Description
-----------

@row_offset - offset from the first callchain expanded to appear on screen
\ ``nr_rows``\  - rows expanded in callchain, recalculated on folding/unfolding

.. This file was automatic generated / don't edit.

