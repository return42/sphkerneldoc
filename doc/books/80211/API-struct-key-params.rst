
.. _API-struct-key-params:

=================
struct key_params
=================

*man struct key_params(9)*

*4.6.0-rc1*

key information


Synopsis
========

.. code-block:: c

    struct key_params {
      const u8 * key;
      const u8 * seq;
      int key_len;
      int seq_len;
      u32 cipher;
    };


Members
=======

key
    key material

seq
    sequence counter (IV/PN) for TKIP and CCMP keys, only used with the ``get_key`` callback, must be in little endian, length given by ``seq_len``.

key_len
    length of key material

seq_len
    length of ``seq``.

cipher
    cipher suite selector


Description
===========

Information about a key
