.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/wireless/scan.c

.. _`bss_compare_mode`:

enum bss_compare_mode
=====================

.. c:type:: enum bss_compare_mode

    BSS compare mode

.. _`bss_compare_mode.definition`:

Definition
----------

.. code-block:: c

    enum bss_compare_mode {
        BSS_CMP_REGULAR,
        BSS_CMP_HIDE_ZLEN,
        BSS_CMP_HIDE_NUL
    };

.. _`bss_compare_mode.constants`:

Constants
---------

BSS_CMP_REGULAR
    regular compare mode (for insertion and normal find)

BSS_CMP_HIDE_ZLEN
    find hidden SSID with zero-length mode

BSS_CMP_HIDE_NUL
    find hidden SSID with NUL-ed out mode

.. This file was automatic generated / don't edit.

