.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/sprd/div.h

.. _`sprd_div_internal`:

struct sprd_div_internal
========================

.. c:type:: struct sprd_div_internal

    Internal divider description

.. _`sprd_div_internal.definition`:

Definition
----------

.. code-block:: c

    struct sprd_div_internal {
        u8 shift;
        u8 width;
    }

.. _`sprd_div_internal.members`:

Members
-------

shift
    Bit offset of the divider in its register

width
    Width of the divider field in its register

.. _`sprd_div_internal.description`:

Description
-----------

That structure represents a single divider, and is meant to be
embedded in other structures representing the various clock
classes.

.. This file was automatic generated / don't edit.

