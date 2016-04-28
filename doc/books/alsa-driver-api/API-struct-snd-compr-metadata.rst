.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-compr-metadata:

=========================
struct snd_compr_metadata
=========================

*man struct snd_compr_metadata(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
