.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/sparse-keymap.c

.. _`sparse_keymap_entry_from_scancode`:

sparse_keymap_entry_from_scancode
=================================

.. c:function:: struct key_entry *sparse_keymap_entry_from_scancode(struct input_dev *dev, unsigned int code)

    perform sparse keymap lookup

    :param dev:
        Input device using sparse keymap
    :type dev: struct input_dev \*

    :param code:
        Scan code
    :type code: unsigned int

.. _`sparse_keymap_entry_from_scancode.description`:

Description
-----------

This function is used to perform \ :c:type:`struct key_entry <key_entry>`\  lookup in an
input device using sparse keymap.

.. _`sparse_keymap_entry_from_keycode`:

sparse_keymap_entry_from_keycode
================================

.. c:function:: struct key_entry *sparse_keymap_entry_from_keycode(struct input_dev *dev, unsigned int keycode)

    perform sparse keymap lookup

    :param dev:
        Input device using sparse keymap
    :type dev: struct input_dev \*

    :param keycode:
        Key code
    :type keycode: unsigned int

.. _`sparse_keymap_entry_from_keycode.description`:

Description
-----------

This function is used to perform \ :c:type:`struct key_entry <key_entry>`\  lookup in an
input device using sparse keymap.

.. _`sparse_keymap_setup`:

sparse_keymap_setup
===================

.. c:function:: int sparse_keymap_setup(struct input_dev *dev, const struct key_entry *keymap, int (*setup)(struct input_dev *, struct key_entry *))

    set up sparse keymap for an input device

    :param dev:
        Input device
    :type dev: struct input_dev \*

    :param keymap:
        Keymap in form of array of \ :c:type:`struct key_entry <key_entry>`\  structures ending
        with \ ``KE_END``\  type entry
    :type keymap: const struct key_entry \*

    :param int (\*setup)(struct input_dev \*, struct key_entry \*):
        Function that can be used to adjust keymap entries
        depending on device's needs, may be \ ``NULL``\ 

.. _`sparse_keymap_setup.description`:

Description
-----------

The function calculates size and allocates copy of the original
keymap after which sets up input device event bits appropriately.
The allocated copy of the keymap is automatically freed when it
is no longer needed.

.. _`sparse_keymap_report_entry`:

sparse_keymap_report_entry
==========================

.. c:function:: void sparse_keymap_report_entry(struct input_dev *dev, const struct key_entry *ke, unsigned int value, bool autorelease)

    report event corresponding to given key entry

    :param dev:
        Input device for which event should be reported
    :type dev: struct input_dev \*

    :param ke:
        key entry describing event
    :type ke: const struct key_entry \*

    :param value:
        Value that should be reported (ignored by \ ``KE_SW``\  entries)
    :type value: unsigned int

    :param autorelease:
        Signals whether release event should be emitted for \ ``KE_KEY``\ 
        entries right after reporting press event, ignored by all other
        entries
    :type autorelease: bool

.. _`sparse_keymap_report_entry.description`:

Description
-----------

This function is used to report input event described by given
\ :c:type:`struct key_entry <key_entry>`\ .

.. _`sparse_keymap_report_event`:

sparse_keymap_report_event
==========================

.. c:function:: bool sparse_keymap_report_event(struct input_dev *dev, unsigned int code, unsigned int value, bool autorelease)

    report event corresponding to given scancode

    :param dev:
        Input device using sparse keymap
    :type dev: struct input_dev \*

    :param code:
        Scan code
    :type code: unsigned int

    :param value:
        Value that should be reported (ignored by \ ``KE_SW``\  entries)
    :type value: unsigned int

    :param autorelease:
        Signals whether release event should be emitted for \ ``KE_KEY``\ 
        entries right after reporting press event, ignored by all other
        entries
    :type autorelease: bool

.. _`sparse_keymap_report_event.description`:

Description
-----------

This function is used to perform lookup in an input device using sparse
keymap and report corresponding event. Returns \ ``true``\  if lookup was
successful and \ ``false``\  otherwise.

.. This file was automatic generated / don't edit.

