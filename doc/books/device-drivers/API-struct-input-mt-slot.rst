
.. _API-struct-input-mt-slot:

====================
struct input_mt_slot
====================

*man struct input_mt_slot(9)*

*4.6.0-rc1*

represents the state of an input MT slot


Synopsis
========

.. code-block:: c

    struct input_mt_slot {
      int abs[ABS_MT_LAST - ABS_MT_FIRST + 1];
      unsigned int frame;
      unsigned int key;
    };


Members
=======

abs[ABS_MT_LAST - ABS_MT_FIRST + 1]
    holds current values of ABS_MT axes for this slot

frame
    last frame at which ``input_mt_report_slot_state`` was called

key
    optional driver designation of this slot
