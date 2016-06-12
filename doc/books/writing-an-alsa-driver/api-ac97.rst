.. -*- coding: utf-8; mode: rst -*-

.. _api-ac97:

******************
API for AC97 Codec
******************


General
=======

The ALSA AC97 codec layer is a well-defined one, and you don't have to
write much code to control it. Only low-level control routines are
necessary. The AC97 codec API is defined in ``<sound/ac97_codec.h>``.


.. _api-ac97-example:

Full Code Example
=================


.. code-block:: c

      struct mychip {
              ....
              struct snd_ac97 *ac97;
              ....
      };

      static unsigned short snd_mychip_ac97_read(struct snd_ac97 *ac97,
                                                 unsigned short reg)
      {
              struct mychip *chip = ac97->private_data;
              ....
              /* read a register value here from the codec */
              return the_register_value;
      }

      static void snd_mychip_ac97_write(struct snd_ac97 *ac97,
                                       unsigned short reg, unsigned short val)
      {
              struct mychip *chip = ac97->private_data;
              ....
              /* write the given register value to the codec */
      }

      static int snd_mychip_ac97(struct mychip *chip)
      {
              struct snd_ac97_bus *bus;
              struct snd_ac97_template ac97;
              int err;
              static struct snd_ac97_bus_ops ops = {
                      .write = snd_mychip_ac97_write,
                      .read = snd_mychip_ac97_read,
              };

              err = snd_ac97_bus(chip->card, 0, &ops, NULL, &bus);
              if (err < 0)
                      return err;
              memset(&ac97, 0, sizeof(ac97));
              ac97.private_data = chip;
              return snd_ac97_mixer(bus, &ac97, &chip->ac97);
      }


.. _api-ac97-constructor:

Constructor
===========

To create an ac97 instance, first call :c:func:`snd_ac97_bus()` with
an ``ac97_bus_ops_t`` record with callback functions.


.. code-block:: c

      struct snd_ac97_bus *bus;
      static struct snd_ac97_bus_ops ops = {
            .write = snd_mychip_ac97_write,
            .read = snd_mychip_ac97_read,
      };

      snd_ac97_bus(card, 0, &ops, NULL, &pbus);

The bus record is shared among all belonging ac97 instances.

And then call :c:func:`snd_ac97_mixer()` with an struct
:c:type:`struct snd_ac97_template` record together with the bus
pointer created above.


.. code-block:: c

      struct snd_ac97_template ac97;
      int err;

      memset(&ac97, 0, sizeof(ac97));
      ac97.private_data = chip;
      snd_ac97_mixer(bus, &ac97, &chip->ac97);

where chip->ac97 is a pointer to a newly created ``ac97_t`` instance. In
this case, the chip pointer is set as the private data, so that the
read/write callback functions can refer to this chip instance. This
instance is not necessarily stored in the chip record. If you need to
change the register values from the driver, or need the suspend/resume
of ac97 codecs, keep this pointer to pass to the corresponding
functions.


.. _api-ac97-callbacks:

Callbacks
=========

The standard callbacks are ``read`` and ``write``. Obviously they
correspond to the functions for read and write accesses to the hardware
low-level codes.

The ``read`` callback returns the register value specified in the
argument.


.. code-block:: c

      static unsigned short snd_mychip_ac97_read(struct snd_ac97 *ac97,
                                                 unsigned short reg)
      {
              struct mychip *chip = ac97->private_data;
              ....
              return the_register_value;
      }

Here, the chip can be cast from ac97->private_data.

Meanwhile, the ``write`` callback is used to set the register value.


.. code-block:: c

      static void snd_mychip_ac97_write(struct snd_ac97 *ac97,
                           unsigned short reg, unsigned short val)

These callbacks are non-atomic like the control API callbacks.

There are also other callbacks: ``reset``, ``wait`` and ``init``.

The ``reset`` callback is used to reset the codec. If the chip requires
a special kind of reset, you can define this callback.

The ``wait`` callback is used to add some waiting time in the standard
initialization of the codec. If the chip requires the extra waiting
time, define this callback.

The ``init`` callback is used for additional initialization of the
codec.


.. _api-ac97-updating-registers:

Updating Registers in The Driver
================================

If you need to access to the codec from the driver, you can call the
following functions: :c:func:`snd_ac97_write()`,
:c:func:`snd_ac97_read()`, :c:func:`snd_ac97_update()` and
:c:func:`snd_ac97_update_bits()`.

Both :c:func:`snd_ac97_write()` and :c:func:`snd_ac97_update()`
functions are used to set a value to the given register (``AC97_XXX``).
The difference between them is that :c:func:`snd_ac97_update()`
doesn't write a value if the given value has been already set, while
:c:func:`snd_ac97_write()` always rewrites the value.


.. code-block:: c

      snd_ac97_write(ac97, AC97_MASTER, 0x8080);
      snd_ac97_update(ac97, AC97_MASTER, 0x8080);

:c:func:`snd_ac97_read()` is used to read the value of the given
register. For example,


.. code-block:: c

      value = snd_ac97_read(ac97, AC97_MASTER);

:c:func:`snd_ac97_update_bits()` is used to update some bits in the
given register.


.. code-block:: c

      snd_ac97_update_bits(ac97, reg, mask, value);

Also, there is a function to change the sample rate (of a given register
such as ``AC97_PCM_FRONT_DAC_RATE``) when VRA or DRA is supported by the
codec: :c:func:`snd_ac97_set_rate()`.


.. code-block:: c

      snd_ac97_set_rate(ac97, AC97_PCM_FRONT_DAC_RATE, 44100);

The following registers are available to set the rate:
``AC97_PCM_MIC_ADC_RATE``, ``AC97_PCM_FRONT_DAC_RATE``,
``AC97_PCM_LR_ADC_RATE``, ``AC97_SPDIF``. When ``AC97_SPDIF`` is
specified, the register is not really changed but the corresponding
IEC958 status bits will be updated.


.. _api-ac97-clock-adjustment:

Clock Adjustment
================

In some chips, the clock of the codec isn't 48000 but using a PCI clock
(to save a quartz!). In this case, change the field bus->clock to the
corresponding value. For example, intel8x0 and es1968 drivers have their
own function to read from the clock.


.. _api-ac97-proc-files:

Proc Files
==========

The ALSA AC97 interface will create a proc file such as
``/proc/asound/card0/codec97#0/ac97#0-0`` and ``ac97#0-0+regs``. You can
refer to these files to see the current status and registers of the
codec.


.. _api-ac97-multiple-codecs:

Multiple Codecs
===============

When there are several codecs on the same card, you need to call
:c:func:`snd_ac97_mixer()` multiple times with ac97.num=1 or
greater. The ``num`` field specifies the codec number.

If you set up multiple codecs, you either need to write different
callbacks for each codec or check ac97->num in the callback routines.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
