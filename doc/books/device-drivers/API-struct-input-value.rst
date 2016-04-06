
.. _API-struct-input-value:

==================
struct input_value
==================

*man struct input_value(9)*

*4.6.0-rc1*

input value representation


Synopsis
========

.. code-block:: c

    struct input_value {
      __u16 type;
      __u16 code;
      __s32 value;
    };


Members
=======

type
    type of value (EV_KEY, EV_ABS, etc)

code
    the value code

value
    the value
