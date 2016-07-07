.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/keyboard-spear.h

.. _`kbd_platform_data`:

struct kbd_platform_data
========================

.. c:type:: struct kbd_platform_data

    spear keyboard platform data

.. _`kbd_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct kbd_platform_data {
        const struct matrix_keymap_data *keymap;
        bool rep;
        unsigned int mode;
        unsigned int suspended_rate;
    }

.. _`kbd_platform_data.members`:

Members
-------

keymap
    *undescribed*

rep
    *undescribed*

mode
    *undescribed*

suspended_rate
    *undescribed*

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

.. This file was automatic generated / don't edit.

