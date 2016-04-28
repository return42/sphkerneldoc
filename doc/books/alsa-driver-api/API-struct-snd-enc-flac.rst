.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-enc-flac:

===================
struct snd_enc_flac
===================

*man struct snd_enc_flac(9)*

*4.6.0-rc5*


Synopsis
========

.. code-block:: c

    struct snd_enc_flac {
      __u32 num;
      __u32 gain;
    };


Members
=======

num
    serial number, valid only for OGG formats needs to be set by
    application

gain
    Add replay gain tags


Description
===========

These options were extracted from the FLAC online documentation


at http
=======

//flac.sourceforge.net/documentation_tools_flac.html

To make the API simpler, it is assumed that the user will select quality
profiles. Additional options that affect encoding quality and speed can
be added at a later stage if needed.

By default the Subset format is used by encoders.

TAGS such as pictures, etc, cannot be handled by an offloaded encoder
and are not supported in this API.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
