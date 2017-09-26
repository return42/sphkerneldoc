.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/packets-buffer.h

.. _`iso_packets_buffer`:

struct iso_packets_buffer
=========================

.. c:type:: struct iso_packets_buffer

    manages a buffer for many packets

.. _`iso_packets_buffer.definition`:

Definition
----------

.. code-block:: c

    struct iso_packets_buffer {
        struct fw_iso_buffer iso_buffer;
        struct {
            void *buffer;
            unsigned int offset;
        } *packets;
    }

.. _`iso_packets_buffer.members`:

Members
-------

iso_buffer
    the memory containing the packets

packets
    an array, with each element pointing to one packet

.. This file was automatic generated / don't edit.

