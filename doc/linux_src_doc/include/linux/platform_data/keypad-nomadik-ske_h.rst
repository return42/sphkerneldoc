.. -*- coding: utf-8; mode: rst -*-

====================
keypad-nomadik-ske.h
====================


.. _`ske_keypad_platform_data`:

struct ske_keypad_platform_data
===============================

.. c:type:: ske_keypad_platform_data

    structure for platform specific data


.. _`ske_keypad_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct ske_keypad_platform_data {
    int (* init) (void);
    int (* exit) (void);
    const struct matrix_keymap_data * keymap_data;
    u8 krow;
    u8 kcol;
    u8 debounce_ms;
    bool no_autorepeat;
    bool wakeup_enable;
  };


.. _`ske_keypad_platform_data.members`:

Members
-------

:``init``:
    pointer to keypad init function

:``exit``:
    pointer to keypad deinitialisation function

:``keymap_data``:
    matrix scan code table for keycodes

:``krow``:
    maximum number of rows

:``kcol``:
    maximum number of columns

:``debounce_ms``:
    platform specific debounce time

:``no_autorepeat``:
    flag for auto repetition

:``wakeup_enable``:
    allow waking up the system


