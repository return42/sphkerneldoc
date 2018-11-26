.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ceph/decode.h

.. _`ceph_start_encoding`:

ceph_start_encoding
===================

.. c:function:: void ceph_start_encoding(void **p, u8 struct_v, u8 struct_compat, u32 struct_len)

    start encoding block

    :param p:
        *undescribed*
    :type p: void \*\*

    :param struct_v:
        current (code) version of the encoding
    :type struct_v: u8

    :param struct_compat:
        oldest code version that can decode it
    :type struct_compat: u8

    :param struct_len:
        length of struct encoding
    :type struct_len: u32

.. _`ceph_start_decoding`:

ceph_start_decoding
===================

.. c:function:: int ceph_start_decoding(void **p, void *end, u8 v, const char *name, u8 *struct_v, u32 *struct_len)

    start decoding block

    :param p:
        *undescribed*
    :type p: void \*\*

    :param end:
        *undescribed*
    :type end: void \*

    :param v:
        current version of the encoding that the code supports
    :type v: u8

    :param name:
        name of the struct (free-form)
    :type name: const char \*

    :param struct_v:
        out param for the encoding version
    :type struct_v: u8 \*

    :param struct_len:
        out param for the length of struct encoding
    :type struct_len: u32 \*

.. _`ceph_start_decoding.description`:

Description
-----------

Validates the length of struct encoding, so unsafe ceph_decode\_\*
variants can be used for decoding.

.. This file was automatic generated / don't edit.

