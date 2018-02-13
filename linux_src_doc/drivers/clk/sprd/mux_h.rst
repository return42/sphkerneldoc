.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/sprd/mux.h

.. _`sprd_mux_ssel`:

struct sprd_mux_ssel
====================

.. c:type:: struct sprd_mux_ssel

    Mux clock's source select bits in its register

.. _`sprd_mux_ssel.definition`:

Definition
----------

.. code-block:: c

    struct sprd_mux_ssel {
        u8 shift;
        u8 width;
        const u8 *table;
    }

.. _`sprd_mux_ssel.members`:

Members
-------

shift
    Bit offset of the divider in its register

width
    Width of the divider field in its register

table
    For some mux clocks, not all sources are used on some special
    chips, this matches the value of mux clock's register and the
    sources which are used for this mux clock

.. This file was automatic generated / don't edit.

