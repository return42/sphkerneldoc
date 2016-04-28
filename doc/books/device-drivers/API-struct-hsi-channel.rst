.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-hsi-channel:

==================
struct hsi_channel
==================

*man struct hsi_channel(9)*

*4.6.0-rc5*

channel resource used by the hsi clients


Synopsis
========

.. code-block:: c

    struct hsi_channel {
      unsigned int id;
      const char * name;
    };


Members
=======

id
    Channel number

name
    Channel name


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
