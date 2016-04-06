
.. _API-struct-rc-scancode-filter:

=========================
struct rc_scancode_filter
=========================

*man struct rc_scancode_filter(9)*

*4.6.0-rc1*

Filter scan codes.


Synopsis
========

.. code-block:: c

    struct rc_scancode_filter {
      u32 data;
      u32 mask;
    };


Members
=======

data
    Scancode data to match.

mask
    Mask of bits of scancode to compare.
