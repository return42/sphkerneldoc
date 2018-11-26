.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mux/driver.h

.. _`mux_control_ops`:

struct mux_control_ops
======================

.. c:type:: struct mux_control_ops

    Mux controller operations for a mux chip.

.. _`mux_control_ops.definition`:

Definition
----------

.. code-block:: c

    struct mux_control_ops {
        int (*set)(struct mux_control *mux, int state);
    }

.. _`mux_control_ops.members`:

Members
-------

set
    Set the state of the given mux controller.

.. _`mux_control`:

struct mux_control
==================

.. c:type:: struct mux_control

    Represents a mux controller.

.. _`mux_control.definition`:

Definition
----------

.. code-block:: c

    struct mux_control {
        struct semaphore lock;
        struct mux_chip *chip;
        int cached_state;
        unsigned int states;
        int idle_state;
    }

.. _`mux_control.members`:

Members
-------

lock
    Protects the mux controller state.

chip
    The mux chip that is handling this mux controller.

cached_state
    The current mux controller state, or -1 if none.

states
    The number of mux controller states.

idle_state
    The mux controller state to use when inactive, or one
    of MUX_IDLE_AS_IS and MUX_IDLE_DISCONNECT.

.. _`mux_control.description`:

Description
-----------

Mux drivers may only change \ ``states``\  and \ ``idle_state``\ , and may only do so
between allocation and registration of the mux controller. Specifically,
\ ``cached_state``\  is internal to the mux core and should never be written by
mux drivers.

.. _`mux_chip`:

struct mux_chip
===============

.. c:type:: struct mux_chip

    Represents a chip holding mux controllers.

.. _`mux_chip.definition`:

Definition
----------

.. code-block:: c

    struct mux_chip {
        unsigned int controllers;
        struct mux_control *mux;
        struct device dev;
        int id;
        const struct mux_control_ops *ops;
    }

.. _`mux_chip.members`:

Members
-------

controllers
    Number of mux controllers handled by the chip.

mux
    Array of mux controllers that are handled.

dev
    Device structure.

id
    Used to identify the device internally.

ops
    Mux controller operations.

.. _`mux_chip_priv`:

mux_chip_priv
=============

.. c:function:: void *mux_chip_priv(struct mux_chip *mux_chip)

    Get the extra memory reserved by \ :c:func:`mux_chip_alloc`\ .

    :param mux_chip:
        The mux-chip to get the private memory from.
    :type mux_chip: struct mux_chip \*

.. _`mux_chip_priv.return`:

Return
------

Pointer to the private memory reserved by the allocator.

.. _`mux_control_get_index`:

mux_control_get_index
=====================

.. c:function:: unsigned int mux_control_get_index(struct mux_control *mux)

    Get the index of the given mux controller

    :param mux:
        The mux-control to get the index for.
    :type mux: struct mux_control \*

.. _`mux_control_get_index.return`:

Return
------

The index of the mux controller within the mux chip the mux
controller is a part of.

.. This file was automatic generated / don't edit.

