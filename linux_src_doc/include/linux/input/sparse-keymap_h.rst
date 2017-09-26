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
        union {
            u16 keycode;
            struct {
                u8 code;
                u8 value;
            } sw;
        } ;
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

keycode
    KEY_* code assigned to a key/button

sw
    *undescribed*

sw.code
    SW_* code assigned to a switch

sw.value
    Value that should be sent in an input even when KE_SW
    switch is toggled. KE_VSW switches ignore this field and
    expect driver to supply value for the event.

code
    Device-specific data identifying the button/switch

value
    *undescribed*

.. _`key_entry.description`:

Description
-----------

This structure defines an entry in a sparse keymap used by some
input devices for which traditional table-based approach is not
suitable.

.. This file was automatic generated / don't edit.

