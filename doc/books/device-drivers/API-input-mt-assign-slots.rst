
.. _API-input-mt-assign-slots:

=====================
input_mt_assign_slots
=====================

*man input_mt_assign_slots(9)*

*4.6.0-rc1*

perform a best-match assignment


Synopsis
========

.. c:function:: int input_mt_assign_slots( struct input_dev * dev, int * slots, const struct input_mt_pos * pos, int num_pos, int dmax )

Arguments
=========

``dev``
    input device with allocated MT slots

``slots``
    the slot assignment to be filled

``pos``
    the position array to match

``num_pos``
    number of positions

``dmax``
    maximum ABS_MT_POSITION displacement (zero for infinite)


Description
===========

Performs a best match against the current contacts and returns the slot assignment list. New contacts are assigned to unused slots.

The assignments are balanced so that all coordinate displacements are below the euclidian distance dmax. If no such assignment can be found, some contacts are assigned to unused
slots.

Returns zero on success, or negative error in case of failure.
