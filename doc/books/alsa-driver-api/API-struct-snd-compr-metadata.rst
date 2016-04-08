
.. _API-struct-snd-compr-metadata:

=========================
struct snd_compr_metadata
=========================

*man struct snd_compr_metadata(9)*

*4.6.0-rc1*

compressed stream metadata


Synopsis
========

.. code-block:: c

    struct snd_compr_metadata {
      __u32 key;
      __u32 value[8];
    };


Members
=======

key
    key id

value[8]
    key value
