.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/i2c/mpr121_touchkey.h

.. _`mpr121_platform_data`:

struct mpr121_platform_data
===========================

.. c:type:: struct mpr121_platform_data

    platform data for mpr121 sensor

.. _`mpr121_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct mpr121_platform_data {
        const unsigned short *keymap;
        unsigned int keymap_size;
        bool wakeup;
        int vdd_uv;
    }

.. _`mpr121_platform_data.members`:

Members
-------

keymap
    pointer to array of KEY\_\* values representing keymap

keymap_size
    size of the keymap

wakeup
    configure the button as a wake-up source

vdd_uv
    VDD voltage in uV

.. This file was automatic generated / don't edit.

