.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/kempld-core.c

.. _`kempld_read8`:

kempld_read8
============

.. c:function:: u8 kempld_read8(struct kempld_device_data *pld, u8 index)

    read 8 bit register

    :param pld:
        kempld_device_data structure describing the PLD
    :type pld: struct kempld_device_data \*

    :param index:
        register index on the chip
    :type index: u8

.. _`kempld_read8.description`:

Description
-----------

kempld_get_mutex must be called prior to calling this function.

.. _`kempld_write8`:

kempld_write8
=============

.. c:function:: void kempld_write8(struct kempld_device_data *pld, u8 index, u8 data)

    write 8 bit register

    :param pld:
        kempld_device_data structure describing the PLD
    :type pld: struct kempld_device_data \*

    :param index:
        register index on the chip
    :type index: u8

    :param data:
        new register value
    :type data: u8

.. _`kempld_write8.description`:

Description
-----------

kempld_get_mutex must be called prior to calling this function.

.. _`kempld_read16`:

kempld_read16
=============

.. c:function:: u16 kempld_read16(struct kempld_device_data *pld, u8 index)

    read 16 bit register

    :param pld:
        kempld_device_data structure describing the PLD
    :type pld: struct kempld_device_data \*

    :param index:
        register index on the chip
    :type index: u8

.. _`kempld_read16.description`:

Description
-----------

kempld_get_mutex must be called prior to calling this function.

.. _`kempld_write16`:

kempld_write16
==============

.. c:function:: void kempld_write16(struct kempld_device_data *pld, u8 index, u16 data)

    write 16 bit register

    :param pld:
        kempld_device_data structure describing the PLD
    :type pld: struct kempld_device_data \*

    :param index:
        register index on the chip
    :type index: u8

    :param data:
        new register value
    :type data: u16

.. _`kempld_write16.description`:

Description
-----------

kempld_get_mutex must be called prior to calling this function.

.. _`kempld_read32`:

kempld_read32
=============

.. c:function:: u32 kempld_read32(struct kempld_device_data *pld, u8 index)

    read 32 bit register

    :param pld:
        kempld_device_data structure describing the PLD
    :type pld: struct kempld_device_data \*

    :param index:
        register index on the chip
    :type index: u8

.. _`kempld_read32.description`:

Description
-----------

kempld_get_mutex must be called prior to calling this function.

.. _`kempld_write32`:

kempld_write32
==============

.. c:function:: void kempld_write32(struct kempld_device_data *pld, u8 index, u32 data)

    write 32 bit register

    :param pld:
        kempld_device_data structure describing the PLD
    :type pld: struct kempld_device_data \*

    :param index:
        register index on the chip
    :type index: u8

    :param data:
        new register value
    :type data: u32

.. _`kempld_write32.description`:

Description
-----------

kempld_get_mutex must be called prior to calling this function.

.. _`kempld_get_mutex`:

kempld_get_mutex
================

.. c:function:: void kempld_get_mutex(struct kempld_device_data *pld)

    acquire PLD mutex

    :param pld:
        kempld_device_data structure describing the PLD
    :type pld: struct kempld_device_data \*

.. _`kempld_release_mutex`:

kempld_release_mutex
====================

.. c:function:: void kempld_release_mutex(struct kempld_device_data *pld)

    release PLD mutex

    :param pld:
        kempld_device_data structure describing the PLD
    :type pld: struct kempld_device_data \*

.. _`kempld_get_info`:

kempld_get_info
===============

.. c:function:: int kempld_get_info(struct kempld_device_data *pld)

    update device specific information

    :param pld:
        kempld_device_data structure describing the PLD
    :type pld: struct kempld_device_data \*

.. _`kempld_get_info.description`:

Description
-----------

This function calls the configured board specific kempld_get_info_XXXX
function which is responsible for gathering information about the specific
hardware. The information is then stored within the pld structure.

.. This file was automatic generated / don't edit.

