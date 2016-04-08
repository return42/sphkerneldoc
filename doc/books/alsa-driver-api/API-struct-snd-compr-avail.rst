
.. _API-struct-snd-compr-avail:

======================
struct snd_compr_avail
======================

*man struct snd_compr_avail(9)*

*4.6.0-rc1*

avail descriptor


Synopsis
========

.. code-block:: c

    struct snd_compr_avail {
      __u64 avail;
      struct snd_compr_tstamp tstamp;
    };


Members
=======

avail
    Number of bytes available in ring buffer for writing/reading

tstamp
    timestamp information
