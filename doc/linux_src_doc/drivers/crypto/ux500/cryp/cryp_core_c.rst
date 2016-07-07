.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ux500/cryp/cryp_core.c

.. _`cryp_max_key_size`:

CRYP_MAX_KEY_SIZE
=================

.. c:function::  CRYP_MAX_KEY_SIZE()

    Ericsson SA 2010

.. _`cryp_max_key_size.author`:

Author
------

Shujuan Chen <shujuan.chen\ ``stericsson``\ .com> for ST-Ericsson.

Joakim Bech <joakim.xx.bech\ ``stericsson``\ .com> for ST-Ericsson.

Berne Hebark <berne.herbark\ ``stericsson``\ .com> for ST-Ericsson.

Niklas Hernaeus <niklas.hernaeus\ ``stericsson``\ .com> for ST-Ericsson.

Jonas Linde <jonas.linde\ ``stericsson``\ .com> for ST-Ericsson.

Andreas Westin <andreas.westin\ ``stericsson``\ .com> for ST-Ericsson.

.. _`cryp_max_key_size.license-terms`:

License terms
-------------

GNU General Public License (GPL) version 2

.. _`cryp_driver_data`:

struct cryp_driver_data
=======================

.. c:type:: struct cryp_driver_data

    data specific to the driver.

.. _`cryp_driver_data.definition`:

Definition
----------

.. code-block:: c

    struct cryp_driver_data {
        struct klist device_list;
        struct semaphore device_allocation;
    }

.. _`cryp_driver_data.members`:

Members
-------

device_list
    A list of registered devices to choose from.

device_allocation
    A semaphore initialized with number of devices.

.. _`cryp_ctx`:

struct cryp_ctx
===============

.. c:type:: struct cryp_ctx

    Crypto context

.. _`cryp_ctx.definition`:

Definition
----------

.. code-block:: c

    struct cryp_ctx {
        struct cryp_config config;
        u8 key[CRYP_MAX_KEY_SIZE];
        u32 keylen;
        u8 *iv;
        const u8 *indata;
        u8 *outdata;
        u32 datalen;
        u32 outlen;
        u32 blocksize;
        u8 updated;
        struct cryp_device_context dev_ctx;
        struct cryp_device_data *device;
        u32 session_id;
    }

.. _`cryp_ctx.members`:

Members
-------

config
    Crypto mode.

key
    Key.

keylen
    Length of key.

iv
    Pointer to initialization vector.

indata
    Pointer to indata.

outdata
    Pointer to outdata.

datalen
    Length of indata.

outlen
    Length of outdata.

blocksize
    Size of blocks.

updated
    Updated flag.

dev_ctx
    Device dependent context.

device
    Pointer to the device.

session_id
    *undescribed*

.. _`uint8p_to_uint32_be`:

uint8p_to_uint32_be
===================

.. c:function:: u32 uint8p_to_uint32_be(u8 *in)

    4\*uint8 to uint32 big endian

    :param u8 \*in:
        Data to convert.

.. _`swap_bits_in_byte`:

swap_bits_in_byte
=================

.. c:function:: u8 swap_bits_in_byte(u8 b)

    mirror the bits in a byte

    :param u8 b:
        the byte to be mirrored

.. _`swap_bits_in_byte.the-bits-are-swapped-the-following-way`:

The bits are swapped the following way
--------------------------------------

Byte b include bits 0-7, nibble 1 (n1) include bits 0-3 and
nibble 2 (n2) bits 4-7.

Nibble 1 (n1):
(The "old" (moved) bit is replaced with a zero)
1. Move bit 6 and 7, 4 positions to the left.
2. Move bit 3 and 5, 2 positions to the left.
3. Move bit 1-4, 1 position to the left.

Nibble 2 (n2):
1. Move bit 0 and 1, 4 positions to the right.
2. Move bit 2 and 4, 2 positions to the right.
3. Move bit 3-6, 1 position to the right.

Combine the two nibbles to a complete and swapped byte.

.. _`cryp_algs_register_all`:

cryp_algs_register_all
======================

.. c:function:: int cryp_algs_register_all( void)

    :param  void:
        no arguments

.. _`cryp_algs_unregister_all`:

cryp_algs_unregister_all
========================

.. c:function:: void cryp_algs_unregister_all( void)

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

