.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-compr-avail:

======================
struct snd_compr_avail
======================

*man struct snd_compr_avail(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
