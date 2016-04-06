
.. _API-input-mt-init-slots:

===================
input_mt_init_slots
===================

*man input_mt_init_slots(9)*

*4.6.0-rc1*

initialize MT input slots


Synopsis
========

.. c:function:: int input_mt_init_slots( struct input_dev * dev, unsigned int num_slots, unsigned int flags )

Arguments
=========

``dev``
    input device supporting MT events and finger tracking

``num_slots``
    number of slots used by the device

``flags``
    mt tasks to handle in core


Description
===========

This function allocates all necessary memory for MT slot handling in the input device, prepares the ABS_MT_SLOT and ABS_MT_TRACKING_ID events for use and sets up appropriate
buffers. Depending on the flags set, it also performs pointer emulation and frame synchronization.

May be called repeatedly. Returns -EINVAL if attempting to reinitialize with a different number of slots.
