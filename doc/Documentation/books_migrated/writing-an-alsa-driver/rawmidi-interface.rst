.. -*- coding: utf-8; mode: rst -*-

.. _rawmidi-interface:

*****************
RawMIDI Interface
*****************


.. _rawmidi-interface-overview:

Overview
========

The raw MIDI interface is used for hardware MIDI ports that can be
accessed as a byte stream. It is not used for synthesizer chips that do
not directly understand MIDI.

ALSA handles file and buffer management. All you have to do is to write
some code to move data between the buffer and the hardware.

The rawmidi API is defined in ``<sound/rawmidi.h>``.


.. _rawmidi-interface-constructor:

Constructor
===========

To create a rawmidi device, call the :c:func:`snd_rawmidi_new()`
function:


.. code-block:: c

      struct snd_rawmidi *rmidi;
      err = snd_rawmidi_new(chip->card, "MyMIDI", 0, outs, ins, &rmidi);
      if (err < 0)
              return err;
      rmidi->private_data = chip;
      strcpy(rmidi->name, "My MIDI");
      rmidi->info_flags = SNDRV_RAWMIDI_INFO_OUTPUT |
                          SNDRV_RAWMIDI_INFO_INPUT |
                          SNDRV_RAWMIDI_INFO_DUPLEX;

The first argument is the card pointer, the second argument is the ID
string.

The third argument is the index of this component. You can create up to
8 rawmidi devices.

The fourth and fifth arguments are the number of output and input
substreams, respectively, of this device (a substream is the equivalent
of a MIDI port).

Set the ``info_flags`` field to specify the capabilities of the device.
Set ``SNDRV_RAWMIDI_INFO_OUTPUT`` if there is at least one output port,
``SNDRV_RAWMIDI_INFO_INPUT`` if there is at least one input port, and
``SNDRV_RAWMIDI_INFO_DUPLEX`` if the device can handle output and input
at the same time.

After the rawmidi device is created, you need to set the operators
(callbacks) for each substream. There are helper functions to set the
operators for all the substreams of a device:


.. code-block:: c

      snd_rawmidi_set_ops(rmidi, SNDRV_RAWMIDI_STREAM_OUTPUT, &snd_mymidi_output_ops);
      snd_rawmidi_set_ops(rmidi, SNDRV_RAWMIDI_STREAM_INPUT, &snd_mymidi_input_ops);

The operators are usually defined like this:


.. code-block:: c

      static struct snd_rawmidi_ops snd_mymidi_output_ops = {
              .open =    snd_mymidi_output_open,
              .close =   snd_mymidi_output_close,
              .trigger = snd_mymidi_output_trigger,
      };

These callbacks are explained in the
:ref:`Callbacks <rawmidi-interface-callbacks>` section.

If there are more than one substream, you should give a unique name to
each of them:


.. code-block:: c

      struct snd_rawmidi_substream *substream;
      list_for_each_entry(substream,
                          &rmidi->streams[SNDRV_RAWMIDI_STREAM_OUTPUT].substreams,
                          list {
              sprintf(substream->name, "My MIDI Port %d", substream->number + 1);
      }
      /* same for SNDRV_RAWMIDI_STREAM_INPUT */


.. _rawmidi-interface-callbacks:

Callbacks
=========

In all the callbacks, the private data that you've set for the rawmidi
device can be accessed as substream->rmidi->private_data.

If there is more than one port, your callbacks can determine the port
index from the struct snd_rawmidi_substream data passed to each
callback:


.. code-block:: c

      struct snd_rawmidi_substream *substream;
      int index = substream->number;


.. _rawmidi-interface-op-open:

open callback
-------------


.. code-block:: c

      static int snd_xxx_open(struct snd_rawmidi_substream *substream);

This is called when a substream is opened. You can initialize the
hardware here, but you shouldn't start transmitting/receiving data yet.


.. _rawmidi-interface-op-close:

close callback
--------------


.. code-block:: c

      static int snd_xxx_close(struct snd_rawmidi_substream *substream);

Guess what.

The :c:func:`open()` and :c:func:`close()` callbacks of a rawmidi
device are serialized with a mutex, and can sleep.


.. _rawmidi-interface-op-trigger-out:

trigger callback for output substreams
--------------------------------------


.. code-block:: c

      static void snd_xxx_output_trigger(struct snd_rawmidi_substream *substream, int up);

This is called with a nonzero ``up`` parameter when there is some data
in the substream buffer that must be transmitted.

To read data from the buffer, call
:c:func:`snd_rawmidi_transmit_peek()`. It will return the number of
bytes that have been read; this will be less than the number of bytes
requested when there are no more data in the buffer. After the data have
been transmitted successfully, call
:c:func:`snd_rawmidi_transmit_ack()` to remove the data from the
substream buffer:


.. code-block:: c

      unsigned char data;
      while (snd_rawmidi_transmit_peek(substream, &data, 1) == 1) {
              if (snd_mychip_try_to_transmit(data))
                      snd_rawmidi_transmit_ack(substream, 1);
              else
                      break; /* hardware FIFO full */
      }

If you know beforehand that the hardware will accept data, you can use
the :c:func:`snd_rawmidi_transmit()` function which reads some data
and removes them from the buffer at once:


.. code-block:: c

      while (snd_mychip_transmit_possible()) {
              unsigned char data;
              if (snd_rawmidi_transmit(substream, &data, 1) != 1)
                      break; /* no more data */
              snd_mychip_transmit(data);
      }

If you know beforehand how many bytes you can accept, you can use a
buffer size greater than one with the
:c:func:`snd_rawmidi_transmit*()` functions.

The :c:func:`trigger()` callback must not sleep. If the hardware FIFO
is full before the substream buffer has been emptied, you have to
continue transmitting data later, either in an interrupt handler, or
with a timer if the hardware doesn't have a MIDI transmit interrupt.

The :c:func:`trigger()` callback is called with a zero ``up``
parameter when the transmission of data should be aborted.


.. _rawmidi-interface-op-trigger-in:

trigger callback for input substreams
-------------------------------------


.. code-block:: c

      static void snd_xxx_input_trigger(struct snd_rawmidi_substream *substream, int up);

This is called with a nonzero ``up`` parameter to enable receiving data,
or with a zero ``up`` parameter do disable receiving data.

The :c:func:`trigger()` callback must not sleep; the actual reading of
data from the device is usually done in an interrupt handler.

When data reception is enabled, your interrupt handler should call
:c:func:`snd_rawmidi_receive()` for all received data:


.. code-block:: c

      void snd_mychip_midi_interrupt(...)
      {
              while (mychip_midi_available()) {
                      unsigned char data;
                      data = mychip_midi_read();
                      snd_rawmidi_receive(substream, &data, 1);
              }
      }


.. _rawmidi-interface-op-drain:

drain callback
--------------


.. code-block:: c

      static void snd_xxx_drain(struct snd_rawmidi_substream *substream);

This is only used with output substreams. This function should wait
until all data read from the substream buffer have been transmitted.
This ensures that the device can be closed and the driver unloaded
without losing data.

This callback is optional. If you do not set ``drain`` in the struct
snd_rawmidi_ops structure, ALSA will simply wait for 50 milliseconds
instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
