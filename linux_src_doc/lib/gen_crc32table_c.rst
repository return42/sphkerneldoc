.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/gen_crc32table.c

.. _`crc32init_le_generic`:

crc32init_le_generic
====================

.. c:function:: void crc32init_le_generic(const uint32_t polynomial, uint32_t tab)

    allocate and initialize LE table data

    :param polynomial:
        *undescribed*
    :type polynomial: const uint32_t

    :param tab:
        *undescribed*
    :type tab: uint32_t

.. _`crc32init_le_generic.description`:

Description
-----------

crc is the crc of the byte i; other entries are filled in based on the
fact that crctable[i^j] = crctable[i] ^ crctable[j].

.. _`crc32init_be`:

crc32init_be
============

.. c:function:: void crc32init_be( void)

    allocate and initialize BE table data

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

