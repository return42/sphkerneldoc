.. -*- coding: utf-8; mode: rst -*-

===============
keypad-ep93xx.h
===============


.. _`ep93xx_keypad_platform_data`:

struct ep93xx_keypad_platform_data
==================================

.. c:type:: ep93xx_keypad_platform_data

    platform specific device structure


.. _`ep93xx_keypad_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct ep93xx_keypad_platform_data {
    struct matrix_keymap_data * keymap_data;
    unsigned int debounce;
    unsigned int prescale;
    unsigned int flags;
  };


.. _`ep93xx_keypad_platform_data.members`:

Members
-------

:``keymap_data``:
    pointer to :c:type:`struct matrix_keymap_data <matrix_keymap_data>`

:``debounce``:
    debounce start count; terminal count is 0xff

:``prescale``:
    row/column counter pre-scaler load value

:``flags``:
    see above


