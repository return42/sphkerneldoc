
.. _API-struct-input-mt:

===============
struct input_mt
===============

*man struct input_mt(9)*

*4.6.0-rc1*

state of tracked contacts


Synopsis
========

.. code-block:: c

    struct input_mt {
      int trkid;
      int num_slots;
      int slot;
      unsigned int flags;
      unsigned int frame;
      int * red;
      struct input_mt_slot slots[];
    };


Members
=======

trkid
    stores MT tracking ID for the next contact

num_slots
    number of MT slots the device uses

slot
    MT slot currently being transmitted

flags
    input_mt operation flags

frame
    increases every time ``input_mt_sync_frame`` is called

red
    reduced cost matrix for in-kernel tracking

slots[]
    array of slots holding current values of tracked contacts
