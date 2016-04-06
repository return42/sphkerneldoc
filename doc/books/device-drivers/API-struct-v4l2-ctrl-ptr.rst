
.. _API-struct-v4l2-ctrl-ptr:

===================
union v4l2_ctrl_ptr
===================

*man union v4l2_ctrl_ptr(9)*

*4.6.0-rc1*

A pointer to a control value.


Synopsis
========

.. code-block:: c

    union v4l2_ctrl_ptr {
      s32 * p_s32;
      s64 * p_s64;
      u8 * p_u8;
      u16 * p_u16;
      u32 * p_u32;
      char * p_char;
      void * p;
    };


Members
=======

p_s32
    Pointer to a 32-bit signed value.

p_s64
    Pointer to a 64-bit signed value.

p_u8
    Pointer to a 8-bit unsigned value.

p_u16
    Pointer to a 16-bit unsigned value.

p_u32
    Pointer to a 32-bit unsigned value.

p_char
    Pointer to a string.

p
    Pointer to a compound value.
