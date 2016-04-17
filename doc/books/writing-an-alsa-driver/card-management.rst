
.. _card-management:

==================================
Management of Cards and Components
==================================


.. _card-management-card-instance:

Card Instance
=============

For each soundcard, a “card” record must be allocated.

A card record is the headquarters of the soundcard. It manages the whole list of devices (components) on the soundcard, such as PCM, mixers, MIDI, synthesizer, and so on. Also, the
card record holds the ID and the name strings of the card, manages the root of proc files, and controls the power-management states and hotplug disconnections. The component list
on the card record is used to manage the correct release of resources at destruction.

As mentioned above, to create a card instance, call ``snd_card_new()``.


.. code-block:: c

      struct snd_card *card;
      int err;
      err = snd_card_new(&pci->dev, index, id, module, extra_size, &card);

The function takes six arguments: the parent device pointer, the card-index number, the id string, the module pointer (usually ``THIS_MODULE``), the size of extra-data space, and
the pointer to return the card instance. The extra_size argument is used to allocate card->private_data for the chip-specific data. Note that these data are allocated by
``snd_card_new()``.

The first argument, the pointer of struct ``device``, specifies the parent device. For PCI devices, typically &pci-> is passed there.


.. _card-management-component:

Components
==========

After the card is created, you can attach the components (devices) to the card instance. In an ALSA driver, a component is represented as a struct ``snd_device`` object. A
component can be a PCM instance, a control interface, a raw MIDI interface, etc. Each such instance has one component entry.

A component can be created via ``snd_device_new()`` function.


.. code-block:: c

      snd_device_new(card, SNDRV_DEV_XXX, chip, &ops);

This takes the card pointer, the device-level (``SNDRV_DEV_XXX``), the data pointer, and the callback pointers (``&ops``). The device-level defines the type of components and the
order of registration and de-registration. For most components, the device-level is already defined. For a user-defined component, you can use ``SNDRV_DEV_LOWLEVEL``.

This function itself doesn't allocate the data space. The data must be allocated manually beforehand, and its pointer is passed as the argument. This pointer (``chip`` in the above
example) is used as the identifier for the instance.

Each pre-defined ALSA component such as ac97 and pcm calls ``snd_device_new()`` inside its constructor. The destructor for each component is defined in the callback pointers.
Hence, you don't need to take care of calling a destructor for such a component.

If you wish to create your own component, you need to set the destructor function to the dev_free callback in the ``ops``, so that it can be released automatically via
``snd_card_free()``. The next example will show an implementation of chip-specific data.


.. _card-management-chip-specific:

Chip-Specific Data
==================

Chip-specific information, e.g. the I/O port address, its resource pointer, or the irq number, is stored in the chip-specific record.


.. code-block:: c

      struct mychip {
              ....
      };

In general, there are two ways of allocating the chip record.


.. _card-management-chip-specific-snd-card-new:

1. Allocating via snd_card_new().
---------------------------------

As mentioned above, you can pass the extra-data-length to the 5th argument of ``snd_card_new()``, i.e.


.. code-block:: c

      err = snd_card_new(&pci->dev, index[dev], id[dev], THIS_MODULE,
                         sizeof(struct mychip), &card);

struct ``mychip`` is the type of the chip record.

In return, the allocated record can be accessed as


.. code-block:: c

      struct mychip *chip = card->private_data;

With this method, you don't have to allocate twice. The record is released together with the card instance.


.. _card-management-chip-specific-allocate-extra:

2. Allocating an extra device.
------------------------------

After allocating a card instance via ``snd_card_new()`` (with ``0`` on the 4th arg), call ``kzalloc()``.


.. code-block:: c

      struct snd_card *card;
      struct mychip *chip;
      err = snd_card_new(&pci->dev, index[dev], id[dev], THIS_MODULE,
                         0, &card);
      .....
      chip = kzalloc(sizeof(*chip), GFP_KERNEL);

The chip record should have the field to hold the card pointer at least,


.. code-block:: c

      struct mychip {
              struct snd_card *card;
              ....
      };

Then, set the card pointer in the returned chip instance.


.. code-block:: c

      chip->card = card;

Next, initialize the fields, and register this chip record as a low-level device with a specified ``ops``,


.. code-block:: c

      static struct snd_device_ops ops = {
              .dev_free =        snd_mychip_dev_free,
      };
      ....
      snd_device_new(card, SNDRV_DEV_LOWLEVEL, chip, &ops);

``snd_mychip_dev_free()`` is the device-destructor function, which will call the real destructor.


.. code-block:: c

      static int snd_mychip_dev_free(struct snd_device *device)
      {
              return snd_mychip_free(device->device_data);
      }

where ``snd_mychip_free()`` is the real destructor.


.. _card-management-registration:

Registration and Release
========================

After all components are assigned, register the card instance by calling ``snd_card_register()``. Access to the device files is enabled at this point. That is, before
``snd_card_register()`` is called, the components are safely inaccessible from external side. If this call fails, exit the probe function after releasing the card via
``snd_card_free()``.

For releasing the card instance, you can call simply ``snd_card_free()``. As mentioned earlier, all components are released automatically by this call.

For a device which allows hotplugging, you can use ``snd_card_free_when_closed``. This one will postpone the destruction until all devices are closed.
