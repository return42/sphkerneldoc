.. -*- coding: utf-8; mode: rst -*-

.. _basic-flow:

**************************
Basic Flow for PCI Drivers
**************************


.. _basic-flow-outline:

Outline
=======

The minimum flow for PCI soundcards is as follows:

-  define the PCI ID table (see the section
   :ref:`PCI Entries <pci-resource-entries>`).

-  create :c:func:`probe()` callback.

-  create :c:func:`remove()` callback.

-  create a :c:type:`struct pci_driver` structure containing the
   three pointers above.

-  create an :c:func:`init()` function just calling the
   :c:func:`pci_register_driver()` to register the pci_driver table
   defined above.

-  create an :c:func:`exit()` function to call the
   :c:func:`pci_unregister_driver()` function.


.. _basic-flow-example:

Full Code Example
=================

The code example is shown below. Some parts are kept unimplemented at
this moment but will be filled in the next sections. The numbers in the
comment lines of the :c:func:`snd_mychip_probe()` function refer to
details explained in the following section.


.. code-block:: c

      #include <linux/init.h>
      #include <linux/pci.h>
      #include <linux/slab.h>
      #include <sound/core.h>
      #include <sound/initval.h>

      /* module parameters (see "Module Parameters") */
      /* SNDRV_CARDS: maximum number of cards supported by this module */
      static int index[SNDRV_CARDS] = SNDRV_DEFAULT_IDX;
      static char *id[SNDRV_CARDS] = SNDRV_DEFAULT_STR;
      static bool enable[SNDRV_CARDS] = SNDRV_DEFAULT_ENABLE_PNP;

      /* definition of the chip-specific record */
      struct mychip {
              struct snd_card *card;
              /* the rest of the implementation will be in section
               * "PCI Resource Management"
               */
      };

      /* chip-specific destructor
       * (see "PCI Resource Management")
       */
      static int snd_mychip_free(struct mychip *chip)
      {
              .... /* will be implemented later... */
      }

      /* component-destructor
       * (see "Management of Cards and Components")
       */
      static int snd_mychip_dev_free(struct snd_device *device)
      {
              return snd_mychip_free(device->device_data);
      }

      /* chip-specific constructor
       * (see "Management of Cards and Components")
       */
      static int snd_mychip_create(struct snd_card *card,
                                   struct pci_dev *pci,
                                   struct mychip **rchip)
      {
              struct mychip *chip;
              int err;
              static struct snd_device_ops ops = {
                     .dev_free = snd_mychip_dev_free,
              };

              *rchip = NULL;

              /* check PCI availability here
               * (see "PCI Resource Management")
               */
              ....

              /* allocate a chip-specific data with zero filled */
              chip = kzalloc(sizeof(*chip), GFP_KERNEL);
              if (chip == NULL)
                      return -ENOMEM;

              chip->card = card;

              /* rest of initialization here; will be implemented
               * later, see "PCI Resource Management"
               */
              ....

              err = snd_device_new(card, SNDRV_DEV_LOWLEVEL, chip, &ops);
              if (err < 0) {
                      snd_mychip_free(chip);
                      return err;
              }

              *rchip = chip;
              return 0;
      }

      /* constructor -- see "Constructor" sub-section */
      static int snd_mychip_probe(struct pci_dev *pci,
                                  const struct pci_device_id *pci_id)
      {
              static int dev;
              struct snd_card *card;
              struct mychip *chip;
              int err;

              /* (1) */
              if (dev >= SNDRV_CARDS)
                      return -ENODEV;
              if (!enable[dev]) {
                      dev++;
                      return -ENOENT;
              }

              /* (2) */
              err = snd_card_new(&pci->dev, index[dev], id[dev], THIS_MODULE,
                                 0, &card);
              if (err < 0)
                      return err;

              /* (3) */
              err = snd_mychip_create(card, pci, &chip);
              if (err < 0) {
                      snd_card_free(card);
                      return err;
              }

              /* (4) */
              strcpy(card->driver, "My Chip");
              strcpy(card->shortname, "My Own Chip 123");
              sprintf(card->longname, "%s at 0x%lx irq %i",
                      card->shortname, chip->ioport, chip->irq);

              /* (5) */
              .... /* implemented later */

              /* (6) */
              err = snd_card_register(card);
              if (err < 0) {
                      snd_card_free(card);
                      return err;
              }

              /* (7) */
              pci_set_drvdata(pci, card);
              dev++;
              return 0;
      }

      /* destructor -- see the "Destructor" sub-section */
      static void snd_mychip_remove(struct pci_dev *pci)
      {
              snd_card_free(pci_get_drvdata(pci));
              pci_set_drvdata(pci, NULL);
      }


.. _basic-flow-constructor:

Constructor
===========

The real constructor of PCI drivers is the :c:func:`probe()` callback.
The :c:func:`probe()` callback and other component-constructors which
are called from the :c:func:`probe()` callback cannot be used with the
``__init`` prefix because any PCI device could be a hotplug device.

In the :c:func:`probe()` callback, the following scheme is often used.


.. _basic-flow-constructor-device-index:

1) Check and increment the device index.
----------------------------------------


.. code-block:: c

      static int dev;
      ....
      if (dev >= SNDRV_CARDS)
              return -ENODEV;
      if (!enable[dev]) {
              dev++;
              return -ENOENT;
      }

where enable[dev] is the module option.

Each time the :c:func:`probe()` callback is called, check the
availability of the device. If not available, simply increment the
device index and returns. dev will be incremented also later
(:ref:`step 7 <basic-flow-constructor-set-pci>`).


.. _basic-flow-constructor-create-card:

2) Create a card instance
-------------------------


.. code-block:: c

      struct snd_card *card;
      int err;
      ....
      err = snd_card_new(&pci->dev, index[dev], id[dev], THIS_MODULE,
                         0, &card);

The details will be explained in the section
:ref:`Management of Cards and Components <card-management-card-instance>`.


.. _basic-flow-constructor-create-main:

3) Create a main component
--------------------------

In this part, the PCI resources are allocated.


.. code-block:: c

      struct mychip *chip;
      ....
      err = snd_mychip_create(card, pci, &chip);
      if (err < 0) {
              snd_card_free(card);
              return err;
      }

The details will be explained in the section
:ref:`PCI Resource Management <pci-resource>`.


.. _basic-flow-constructor-main-component:

4) Set the driver ID and name strings.
--------------------------------------


.. code-block:: c

      strcpy(card->driver, "My Chip");
      strcpy(card->shortname, "My Own Chip 123");
      sprintf(card->longname, "%s at 0x%lx irq %i",
              card->shortname, chip->ioport, chip->irq);

The driver field holds the minimal ID string of the chip. This is used
by alsa-lib's configurator, so keep it simple but unique. Even the same
driver can have different driver IDs to distinguish the functionality of
each chip type.

The shortname field is a string shown as more verbose name. The longname
field contains the information shown in ``/proc/asound/cards``.


.. _basic-flow-constructor-create-other:

5) Create other components, such as mixer, MIDI, etc.
-----------------------------------------------------

Here you define the basic components such as
:ref:`PCM <pcm-interface>`, mixer (e.g. :ref:`AC97 <api-ac97>`),
MIDI (e.g. :ref:`MPU-401 <midi-interface>`), and other interfaces.
Also, if you want a :ref:`proc file <proc-interface>`, define it here,
too.


.. _basic-flow-constructor-register-card:

6) Register the card instance.
------------------------------


.. code-block:: c

      err = snd_card_register(card);
      if (err < 0) {
              snd_card_free(card);
              return err;
      }

Will be explained in the section
:ref:`Management of Cards and Components <card-management-registration>`,
too.


.. _basic-flow-constructor-set-pci:

7) Set the PCI driver data and return zero.
-------------------------------------------


.. code-block:: c

            pci_set_drvdata(pci, card);
            dev++;
            return 0;

In the above, the card record is stored. This pointer is used in the
remove callback and power-management callbacks, too.


.. _basic-flow-destructor:

Destructor
==========

The destructor, remove callback, simply releases the card instance. Then
the ALSA middle layer will release all the attached components
automatically.

It would be typically like the following:


.. code-block:: c

      static void snd_mychip_remove(struct pci_dev *pci)
      {
              snd_card_free(pci_get_drvdata(pci));
              pci_set_drvdata(pci, NULL);
      }

The above code assumes that the card pointer is set to the PCI driver
data.


.. _basic-flow-header-files:

Header Files
============

For the above example, at least the following include files are
necessary.


.. code-block:: c

      #include <linux/init.h>
      #include <linux/pci.h>
      #include <linux/slab.h>
      #include <sound/core.h>
      #include <sound/initval.h>

where the last one is necessary only when module options are defined in
the source file. If the code is split into several files, the files
without module options don't need them.

In addition to these headers, you'll need ``<linux/interrupt.h>`` for
interrupt handling, and ``<asm/io.h>`` for I/O access. If you use the
:c:func:`mdelay()` or :c:func:`udelay()` functions, you'll need to
include ``<linux/delay.h>`` too.

The ALSA interfaces like the PCM and control APIs are defined in other
``<sound/xxx.h>`` header files. They have to be included after
``<sound/core.h>``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
