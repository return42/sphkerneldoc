.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/rawmidi.c

.. _`snd_rawmidi_receive`:

snd_rawmidi_receive
===================

.. c:function:: int snd_rawmidi_receive(struct snd_rawmidi_substream *substream, const unsigned char *buffer, int count)

    receive the input data from the device

    :param struct snd_rawmidi_substream \*substream:
        the rawmidi substream

    :param const unsigned char \*buffer:
        the buffer pointer

    :param int count:
        the data size to read

.. _`snd_rawmidi_receive.description`:

Description
-----------

Reads the data from the internal buffer.

.. _`snd_rawmidi_receive.return`:

Return
------

The size of read data, or a negative error code on failure.

.. _`snd_rawmidi_transmit_empty`:

snd_rawmidi_transmit_empty
==========================

.. c:function:: int snd_rawmidi_transmit_empty(struct snd_rawmidi_substream *substream)

    check whether the output buffer is empty

    :param struct snd_rawmidi_substream \*substream:
        the rawmidi substream

.. _`snd_rawmidi_transmit_empty.return`:

Return
------

1 if the internal output buffer is empty, 0 if not.

.. _`__snd_rawmidi_transmit_peek`:

__snd_rawmidi_transmit_peek
===========================

.. c:function:: int __snd_rawmidi_transmit_peek(struct snd_rawmidi_substream *substream, unsigned char *buffer, int count)

    copy data from the internal buffer

    :param struct snd_rawmidi_substream \*substream:
        the rawmidi substream

    :param unsigned char \*buffer:
        the buffer pointer

    :param int count:
        data size to transfer

.. _`__snd_rawmidi_transmit_peek.description`:

Description
-----------

This is a variant of \ :c:func:`snd_rawmidi_transmit_peek`\  without spinlock.

.. _`snd_rawmidi_transmit_peek`:

snd_rawmidi_transmit_peek
=========================

.. c:function:: int snd_rawmidi_transmit_peek(struct snd_rawmidi_substream *substream, unsigned char *buffer, int count)

    copy data from the internal buffer

    :param struct snd_rawmidi_substream \*substream:
        the rawmidi substream

    :param unsigned char \*buffer:
        the buffer pointer

    :param int count:
        data size to transfer

.. _`snd_rawmidi_transmit_peek.description`:

Description
-----------

Copies data from the internal output buffer to the given buffer.

Call this in the interrupt handler when the midi output is ready,
and call \ :c:func:`snd_rawmidi_transmit_ack`\  after the transmission is
finished.

.. _`snd_rawmidi_transmit_peek.return`:

Return
------

The size of copied data, or a negative error code on failure.

.. _`__snd_rawmidi_transmit_ack`:

__snd_rawmidi_transmit_ack
==========================

.. c:function:: int __snd_rawmidi_transmit_ack(struct snd_rawmidi_substream *substream, int count)

    acknowledge the transmission

    :param struct snd_rawmidi_substream \*substream:
        the rawmidi substream

    :param int count:
        the transferred count

.. _`__snd_rawmidi_transmit_ack.description`:

Description
-----------

This is a variant of \\ :c:func:`__snd_rawmidi_transmit_ack`\  without spinlock.

.. _`snd_rawmidi_transmit_ack`:

snd_rawmidi_transmit_ack
========================

.. c:function:: int snd_rawmidi_transmit_ack(struct snd_rawmidi_substream *substream, int count)

    acknowledge the transmission

    :param struct snd_rawmidi_substream \*substream:
        the rawmidi substream

    :param int count:
        the transferred count

.. _`snd_rawmidi_transmit_ack.description`:

Description
-----------

Advances the hardware pointer for the internal output buffer with
the given size and updates the condition.
Call after the transmission is finished.

.. _`snd_rawmidi_transmit_ack.return`:

Return
------

The advanced size if successful, or a negative error code on failure.

.. _`snd_rawmidi_transmit`:

snd_rawmidi_transmit
====================

.. c:function:: int snd_rawmidi_transmit(struct snd_rawmidi_substream *substream, unsigned char *buffer, int count)

    copy from the buffer to the device

    :param struct snd_rawmidi_substream \*substream:
        the rawmidi substream

    :param unsigned char \*buffer:
        the buffer pointer

    :param int count:
        the data size to transfer

.. _`snd_rawmidi_transmit.description`:

Description
-----------

Copies data from the buffer to the device and advances the pointer.

.. _`snd_rawmidi_transmit.return`:

Return
------

The copied size if successful, or a negative error code on failure.

.. _`snd_rawmidi_new`:

snd_rawmidi_new
===============

.. c:function:: int snd_rawmidi_new(struct snd_card *card, char *id, int device, int output_count, int input_count, struct snd_rawmidi **rrawmidi)

    create a rawmidi instance

    :param struct snd_card \*card:
        the card instance

    :param char \*id:
        the id string

    :param int device:
        the device index

    :param int output_count:
        the number of output streams

    :param int input_count:
        the number of input streams

    :param struct snd_rawmidi \*\*rrawmidi:
        the pointer to store the new rawmidi instance

.. _`snd_rawmidi_new.description`:

Description
-----------

Creates a new rawmidi instance.
Use \ :c:func:`snd_rawmidi_set_ops`\  to set the operators to the new instance.

.. _`snd_rawmidi_new.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_rawmidi_set_ops`:

snd_rawmidi_set_ops
===================

.. c:function:: void snd_rawmidi_set_ops(struct snd_rawmidi *rmidi, int stream, struct snd_rawmidi_ops *ops)

    set the rawmidi operators

    :param struct snd_rawmidi \*rmidi:
        the rawmidi instance

    :param int stream:
        the stream direction, SNDRV_RAWMIDI_STREAM_XXX

    :param struct snd_rawmidi_ops \*ops:
        the operator table

.. _`snd_rawmidi_set_ops.description`:

Description
-----------

Sets the rawmidi operators for the given stream direction.

.. This file was automatic generated / don't edit.

