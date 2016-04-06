
.. _API-struct-hsi-channel:

==================
struct hsi_channel
==================

*man struct hsi_channel(9)*

*4.6.0-rc1*

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
