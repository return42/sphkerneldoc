.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ralink/rt2x00/rt2x00debug.h

.. _`rt2x00debugfs_entry_flags`:

enum rt2x00debugfs_entry_flags
==============================

.. c:type:: enum rt2x00debugfs_entry_flags

    Flags for debugfs registry entry

.. _`rt2x00debugfs_entry_flags.definition`:

Definition
----------

.. code-block:: c

    enum rt2x00debugfs_entry_flags {
        RT2X00DEBUGFS_OFFSET
    };

.. _`rt2x00debugfs_entry_flags.constants`:

Constants
---------

RT2X00DEBUGFS_OFFSET
    rt2x00lib should pass the register offset
    as argument when using the callback function \ :c:func:`read`\ /\ :c:func:`write`\ 

.. This file was automatic generated / don't edit.

