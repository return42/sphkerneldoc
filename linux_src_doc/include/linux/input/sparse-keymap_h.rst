.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/input/sparse-keymap.h

.. _`key_entry`:

struct key_entry
================

.. c:type:: struct key_entry

    keymap entry for use in sparse keymap

.. _`key_entry.definition`:

Definition
----------

.. code-block:: c

    struct key_entry {
        int type;
        u32 code;
        union {unnamed_union};
    }

.. _`key_entry.members`:

Members
-------

type
    Type of the key entry (KE_KEY, KE_SW, KE_VSW, KE_END);
    drivers are allowed to extend the list with their own
    private definitions.

code
    Device-specific data identifying the button/switch

{unnamed_union}
    anonymous


.. _`key_entry.description`:

Description
-----------

This structure defines an entry in a sparse keymap used by some
input devices for which traditional table-based approach is not
suitable.

.. This file was automatic generated / don't edit.

