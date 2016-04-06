.. -*- coding: utf-8; mode: rst -*-

===============
sparse-keymap.c
===============



.. _xref_sparse_keymap_entry_from_scancode:

sparse_keymap_entry_from_scancode
=================================

.. c:function:: struct key_entry * sparse_keymap_entry_from_scancode (struct input_dev * dev, unsigned int code)

    perform sparse keymap lookup

    :param struct input_dev * dev:
        Input device using sparse keymap

    :param unsigned int code:
        Scan code



Description
-----------

This function is used to perform :c:type:`struct key_entry <key_entry>` lookup in an
input device using sparse keymap.




.. _xref_sparse_keymap_entry_from_keycode:

sparse_keymap_entry_from_keycode
================================

.. c:function:: struct key_entry * sparse_keymap_entry_from_keycode (struct input_dev * dev, unsigned int keycode)

    perform sparse keymap lookup

    :param struct input_dev * dev:
        Input device using sparse keymap

    :param unsigned int keycode:
        Key code



Description
-----------

This function is used to perform :c:type:`struct key_entry <key_entry>` lookup in an
input device using sparse keymap.




.. _xref_sparse_keymap_setup:

sparse_keymap_setup
===================

.. c:function:: int sparse_keymap_setup (struct input_dev * dev, const struct key_entry * keymap, int (*setup) (struct input_dev *, struct key_entry *)

    set up sparse keymap for an input device

    :param struct input_dev * dev:
        Input device

    :param const struct key_entry * keymap:
        Keymap in form of array of :c:type:`struct key_entry <key_entry>` structures ending
        	with ``KE_END`` type entry

    :param int (*)(struct input_dev *, struct key_entry *) setup:
        Function that can be used to adjust keymap entries
        	depending on device's deeds, may be ``NULL``



Description
-----------

The function calculates size and allocates copy of the original
keymap after which sets up input device event bits appropriately.
Before destroying input device allocated keymap should be freed
with a call to :c:func:`sparse_keymap_free`.




.. _xref_sparse_keymap_free:

sparse_keymap_free
==================

.. c:function:: void sparse_keymap_free (struct input_dev * dev)

    free memory allocated for sparse keymap

    :param struct input_dev * dev:
        Input device using sparse keymap



Description
-----------

This function is used to free memory allocated by sparse keymap
in an input device that was set up by :c:func:`sparse_keymap_setup`.



NOTE
----

It is safe to cal this function while input device is
still registered (however the drivers should care not to try to
use freed keymap and thus have to shut off interrupts/polling
before freeing the keymap).




.. _xref_sparse_keymap_report_entry:

sparse_keymap_report_entry
==========================

.. c:function:: void sparse_keymap_report_entry (struct input_dev * dev, const struct key_entry * ke, unsigned int value, bool autorelease)

    report event corresponding to given key entry

    :param struct input_dev * dev:
        Input device for which event should be reported

    :param const struct key_entry * ke:
        key entry describing event

    :param unsigned int value:
        Value that should be reported (ignored by ``KE_SW`` entries)

    :param bool autorelease:
        Signals whether release event should be emitted for ``KE_KEY``
        	entries right after reporting press event, ignored by all other
        	entries



Description
-----------

This function is used to report input event described by given
:c:type:`struct key_entry <key_entry>`.




.. _xref_sparse_keymap_report_event:

sparse_keymap_report_event
==========================

.. c:function:: bool sparse_keymap_report_event (struct input_dev * dev, unsigned int code, unsigned int value, bool autorelease)

    report event corresponding to given scancode

    :param struct input_dev * dev:
        Input device using sparse keymap

    :param unsigned int code:
        Scan code

    :param unsigned int value:
        Value that should be reported (ignored by ``KE_SW`` entries)

    :param bool autorelease:
        Signals whether release event should be emitted for ``KE_KEY``
        	entries right after reporting press event, ignored by all other
        	entries



Description
-----------

This function is used to perform lookup in an input device using sparse
keymap and report corresponding event. Returns ``true`` if lookup was
successful and ``false`` otherwise.


