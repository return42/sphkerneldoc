.. -*- coding: utf-8; mode: rst -*-

================
keyboard-spear.h
================


.. _`kbd_platform_data`:

struct kbd_platform_data
========================

.. c:type:: kbd_platform_data

    spear keyboard platform data


.. _`kbd_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct kbd_platform_data {
  };


.. _`kbd_platform_data.members`:

Members
-------




.. _`kbd_platform_data.keymap`:

keymap
------

pointer to keymap data (table and size)



.. _`kbd_platform_data.rep`:

rep
---

enables key autorepeat



.. _`kbd_platform_data.mode`:

mode
----

choose keyboard support(9x9, 6x6, 2x2)



.. _`kbd_platform_data.suspended_rate`:

suspended_rate
--------------

rate at which keyboard would operate in suspended mode

This structure is supposed to be used by platform code to supply
keymaps to drivers that implement keyboards.

