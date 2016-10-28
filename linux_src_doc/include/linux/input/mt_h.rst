.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/input/mt.h

.. _`input_mt_slot`:

struct input_mt_slot
====================

.. c:type:: struct input_mt_slot

    represents the state of an input MT slot

.. _`input_mt_slot.definition`:

Definition
----------

.. code-block:: c

    struct input_mt_slot {
        int abs[ABS_MT_LAST - ABS_MT_FIRST + 1];
        unsigned int frame;
        unsigned int key;
    }

.. _`input_mt_slot.members`:

Members
-------

abs
    holds current values of ABS_MT axes for this slot

frame
    last frame at which \ :c:func:`input_mt_report_slot_state`\  was called

key
    optional driver designation of this slot

.. _`input_mt`:

struct input_mt
===============

.. c:type:: struct input_mt

    state of tracked contacts

.. _`input_mt.definition`:

Definition
----------

.. code-block:: c

    struct input_mt {
        int trkid;
        int num_slots;
        int slot;
        unsigned int flags;
        unsigned int frame;
        int *red;
        struct input_mt_slot slots[];
    }

.. _`input_mt.members`:

Members
-------

trkid
    stores MT tracking ID for the next contact

num_slots
    number of MT slots the device uses

slot
    MT slot currently being transmitted

flags
    input_mt operation flags

frame
    increases every time \ :c:func:`input_mt_sync_frame`\  is called

red
    reduced cost matrix for in-kernel tracking

slots
    array of slots holding current values of tracked contacts

.. _`input_mt_pos`:

struct input_mt_pos
===================

.. c:type:: struct input_mt_pos

    contact position

.. _`input_mt_pos.definition`:

Definition
----------

.. code-block:: c

    struct input_mt_pos {
        s16 x;
        s16 y;
    }

.. _`input_mt_pos.members`:

Members
-------

x
    horizontal coordinate

y
    vertical coordinate

.. This file was automatic generated / don't edit.

