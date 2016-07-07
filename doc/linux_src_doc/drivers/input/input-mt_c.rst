.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/input-mt.c

.. _`input_mt_init_slots`:

input_mt_init_slots
===================

.. c:function:: int input_mt_init_slots(struct input_dev *dev, unsigned int num_slots, unsigned int flags)

    initialize MT input slots

    :param struct input_dev \*dev:
        input device supporting MT events and finger tracking

    :param unsigned int num_slots:
        number of slots used by the device

    :param unsigned int flags:
        mt tasks to handle in core

.. _`input_mt_init_slots.description`:

Description
-----------

This function allocates all necessary memory for MT slot handling
in the input device, prepares the ABS_MT_SLOT and
ABS_MT_TRACKING_ID events for use and sets up appropriate buffers.
Depending on the flags set, it also performs pointer emulation and
frame synchronization.

May be called repeatedly. Returns -EINVAL if attempting to
reinitialize with a different number of slots.

.. _`input_mt_destroy_slots`:

input_mt_destroy_slots
======================

.. c:function:: void input_mt_destroy_slots(struct input_dev *dev)

    frees the MT slots of the input device

    :param struct input_dev \*dev:
        input device with allocated MT slots

.. _`input_mt_destroy_slots.description`:

Description
-----------

This function is only needed in error path as the input core will
automatically free the MT slots when the device is destroyed.

.. _`input_mt_report_slot_state`:

input_mt_report_slot_state
==========================

.. c:function:: void input_mt_report_slot_state(struct input_dev *dev, unsigned int tool_type, bool active)

    report contact state

    :param struct input_dev \*dev:
        input device with allocated MT slots

    :param unsigned int tool_type:
        the tool type to use in this slot

    :param bool active:
        true if contact is active, false otherwise

.. _`input_mt_report_slot_state.description`:

Description
-----------

Reports a contact via ABS_MT_TRACKING_ID, and optionally
ABS_MT_TOOL_TYPE. If active is true and the slot is currently
inactive, or if the tool type is changed, a new tracking id is
assigned to the slot. The tool type is only reported if the
corresponding absbit field is set.

.. _`input_mt_report_finger_count`:

input_mt_report_finger_count
============================

.. c:function:: void input_mt_report_finger_count(struct input_dev *dev, int count)

    report contact count

    :param struct input_dev \*dev:
        input device with allocated MT slots

    :param int count:
        the number of contacts

.. _`input_mt_report_finger_count.description`:

Description
-----------

Reports the contact count via BTN_TOOL_FINGER, BTN_TOOL_DOUBLETAP,
BTN_TOOL_TRIPLETAP and BTN_TOOL_QUADTAP.

The input core ensures only the KEY events already setup for
this device will produce output.

.. _`input_mt_report_pointer_emulation`:

input_mt_report_pointer_emulation
=================================

.. c:function:: void input_mt_report_pointer_emulation(struct input_dev *dev, bool use_count)

    common pointer emulation

    :param struct input_dev \*dev:
        input device with allocated MT slots

    :param bool use_count:
        report number of active contacts as finger count

.. _`input_mt_report_pointer_emulation.description`:

Description
-----------

Performs legacy pointer emulation via BTN_TOUCH, ABS_X, ABS_Y and
ABS_PRESSURE. Touchpad finger count is emulated if use_count is true.

The input core ensures only the KEY and ABS axes already setup for
this device will produce output.

.. _`input_mt_drop_unused`:

input_mt_drop_unused
====================

.. c:function:: void input_mt_drop_unused(struct input_dev *dev)

    Inactivate slots not seen in this frame

    :param struct input_dev \*dev:
        input device with allocated MT slots

.. _`input_mt_drop_unused.description`:

Description
-----------

Lift all slots not seen since the last call to this function.

.. _`input_mt_sync_frame`:

input_mt_sync_frame
===================

.. c:function:: void input_mt_sync_frame(struct input_dev *dev)

    synchronize mt frame

    :param struct input_dev \*dev:
        input device with allocated MT slots

.. _`input_mt_sync_frame.description`:

Description
-----------

Close the frame and prepare the internal state for a new one.
Depending on the flags, marks unused slots as inactive and performs
pointer emulation.

.. _`input_mt_assign_slots`:

input_mt_assign_slots
=====================

.. c:function:: int input_mt_assign_slots(struct input_dev *dev, int *slots, const struct input_mt_pos *pos, int num_pos, int dmax)

    perform a best-match assignment

    :param struct input_dev \*dev:
        input device with allocated MT slots

    :param int \*slots:
        the slot assignment to be filled

    :param const struct input_mt_pos \*pos:
        the position array to match

    :param int num_pos:
        number of positions

    :param int dmax:
        maximum ABS_MT_POSITION displacement (zero for infinite)

.. _`input_mt_assign_slots.description`:

Description
-----------

Performs a best match against the current contacts and returns
the slot assignment list. New contacts are assigned to unused
slots.

The assignments are balanced so that all coordinate displacements are
below the euclidian distance dmax. If no such assignment can be found,
some contacts are assigned to unused slots.

Returns zero on success, or negative error in case of failure.

.. _`input_mt_get_slot_by_key`:

input_mt_get_slot_by_key
========================

.. c:function:: int input_mt_get_slot_by_key(struct input_dev *dev, int key)

    return slot matching key

    :param struct input_dev \*dev:
        input device with allocated MT slots

    :param int key:
        the key of the sought slot

.. _`input_mt_get_slot_by_key.description`:

Description
-----------

Returns the slot of the given key, if it exists, otherwise
set the key on the first unused slot and return.

If no available slot can be found, -1 is returned.
Note that for this function to work properly, \ :c:func:`input_mt_sync_frame`\  has
to be called at each frame.

.. This file was automatic generated / don't edit.

