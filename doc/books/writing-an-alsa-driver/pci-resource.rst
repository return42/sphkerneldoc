.. -*- coding: utf-8; mode: rst -*-

.. _pci-resource:

***********************
PCI Resource Management
***********************


.. _pci-resource-example:

Full Code Example
=================

In this section, we'll complete the chip-specific constructor,
destructor and PCI entries. Example code is shown first, below.


.. code-block:: c

      struct mychip {
              struct snd_card *card;
              struct pci_dev *pci;

              unsigned long port;
              int irq;
      };

      static int snd_mychip_free(struct mychip *chip)
      {
              /* disable hardware here if any */
              .... /* (not implemented in this document) */

              /* release the irq */
              if (chip->irq >= 0)
                      free_irq(chip->irq, chip);
              /* release the I/O ports & memory */
              pci_release_regions(chip->pci);
              /* disable the PCI entry */
              pci_disable_device(chip->pci);
              /* release the data */
              kfree(chip);
              return 0;
      }

      /* chip-specific constructor */
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

              /* initialize the PCI entry */
              err = pci_enable_device(pci);
              if (err < 0)
                      return err;
              /* check PCI availability (28bit DMA) */
              if (pci_set_dma_mask(pci, DMA_BIT_MASK(28)) < 0 ||
                  pci_set_consistent_dma_mask(pci, DMA_BIT_MASK(28)) < 0) {
                      printk(KERN_ERR "error to set 28bit mask DMAn");
                      pci_disable_device(pci);
                      return -ENXIO;
              }

              chip = kzalloc(sizeof(*chip), GFP_KERNEL);
              if (chip == NULL) {
                      pci_disable_device(pci);
                      return -ENOMEM;
              }

              /* initialize the stuff */
              chip->card = card;
              chip->pci = pci;
              chip->irq = -1;

              /* (1) PCI resource allocation */
              err = pci_request_regions(pci, "My Chip");
              if (err < 0) {
                      kfree(chip);
                      pci_disable_device(pci);
                      return err;
              }
              chip->port = pci_resource_start(pci, 0);
              if (request_irq(pci->irq, snd_mychip_interrupt,
                              IRQF_SHARED, KBUILD_MODNAME, chip)) {
                      printk(KERN_ERR "cannot grab irq %dn", pci->irq);
                      snd_mychip_free(chip);
                      return -EBUSY;
              }
              chip->irq = pci->irq;

              /* (2) initialization of the chip hardware */
              .... /*   (not implemented in this document) */

              err = snd_device_new(card, SNDRV_DEV_LOWLEVEL, chip, &ops);
              if (err < 0) {
                      snd_mychip_free(chip);
                      return err;
              }

              *rchip = chip;
              return 0;
      }

      /* PCI IDs */
      static struct pci_device_id snd_mychip_ids[] = {
              { PCI_VENDOR_ID_FOO, PCI_DEVICE_ID_BAR,
                PCI_ANY_ID, PCI_ANY_ID, 0, 0, 0, },
              ....
              { 0, }
      };
      MODULE_DEVICE_TABLE(pci, snd_mychip_ids);

      /* pci_driver definition */
      static struct pci_driver driver = {
              .name = KBUILD_MODNAME,
              .id_table = snd_mychip_ids,
              .probe = snd_mychip_probe,
              .remove = snd_mychip_remove,
      };

      /* module initialization */
      static int __init alsa_card_mychip_init(void)
      {
              return pci_register_driver(&driver);
      }

      /* module clean up */
      static void __exit alsa_card_mychip_exit(void)
      {
              pci_unregister_driver(&driver);
      }

      module_init(alsa_card_mychip_init)
      module_exit(alsa_card_mychip_exit)

      EXPORT_NO_SYMBOLS; /* for old kernels only */


.. _pci-resource-some-haftas:

Some Hafta's
============

The allocation of PCI resources is done in the ``probe()`` function, and
usually an extra ``xxx_create()`` function is written for this purpose.

In the case of PCI devices, you first have to call the
``pci_enable_device()`` function before allocating resources. Also, you
need to set the proper PCI DMA mask to limit the accessed I/O range. In
some cases, you might need to call ``pci_set_master()`` function, too.

Suppose the 28bit mask, and the code to be added would be like:


.. code-block:: c

      err = pci_enable_device(pci);
      if (err < 0)
              return err;
      if (pci_set_dma_mask(pci, DMA_BIT_MASK(28)) < 0 ||
          pci_set_consistent_dma_mask(pci, DMA_BIT_MASK(28)) < 0) {
              printk(KERN_ERR "error to set 28bit mask DMAn");
              pci_disable_device(pci);
              return -ENXIO;
      }


.. _pci-resource-resource-allocation:

Resource Allocation
===================

The allocation of I/O ports and irqs is done via standard kernel
functions. Unlike ALSA ver.0.5.x., there are no helpers for that. And
these resources must be released in the destructor function (see below).
Also, on ALSA 0.9.x, you don't need to allocate (pseudo-)DMA for PCI
like in ALSA 0.5.x.

Now assume that the PCI device has an I/O port with 8 bytes and an
interrupt. Then struct ``mychip`` will have the following fields:


.. code-block:: c

      struct mychip {
              struct snd_card *card;

              unsigned long port;
              int irq;
      };

For an I/O port (and also a memory region), you need to have the
resource pointer for the standard resource management. For an irq, you
have to keep only the irq number (integer). But you need to initialize
this number as -1 before actual allocation, since irq 0 is valid. The
port address and its resource pointer can be initialized as null by
``kzalloc()`` automatically, so you don't have to take care of resetting
them.

The allocation of an I/O port is done like this:


.. code-block:: c

      err = pci_request_regions(pci, "My Chip");
      if (err < 0) {
              kfree(chip);
              pci_disable_device(pci);
              return err;
      }
      chip->port = pci_resource_start(pci, 0);

It will reserve the I/O port region of 8 bytes of the given PCI device.
The returned value, chip->res_port, is allocated via ``kmalloc()`` by
``request_region()``. The pointer must be released via ``kfree()``, but
there is a problem with this. This issue will be explained later.

The allocation of an interrupt source is done like this:


.. code-block:: c

      if (request_irq(pci->irq, snd_mychip_interrupt,
                      IRQF_SHARED, KBUILD_MODNAME, chip)) {
              printk(KERN_ERR "cannot grab irq %dn", pci->irq);
              snd_mychip_free(chip);
              return -EBUSY;
      }
      chip->irq = pci->irq;

where ``snd_mychip_interrupt()`` is the interrupt handler defined
:ref:`later <pcm-interface-interrupt-handler>`. Note that chip->irq
should be defined only when ``request_irq()`` succeeded.

On the PCI bus, interrupts can be shared. Thus, ``IRQF_SHARED`` is used
as the interrupt flag of ``request_irq()``.

The last argument of ``request_irq()`` is the data pointer passed to the
interrupt handler. Usually, the chip-specific record is used for that,
but you can use what you like, too.

I won't give details about the interrupt handler at this point, but at
least its appearance can be explained now. The interrupt handler looks
usually like the following:


.. code-block:: c

      static irqreturn_t snd_mychip_interrupt(int irq, void *dev_id)
      {
              struct mychip *chip = dev_id;
              ....
              return IRQ_HANDLED;
      }

Now let's write the corresponding destructor for the resources above.
The role of destructor is simple: disable the hardware (if already
activated) and release the resources. So far, we have no hardware part,
so the disabling code is not written here.

To release the resources, the “check-and-release” method is a safer way.
For the interrupt, do like this:


.. code-block:: c

      if (chip->irq >= 0)
              free_irq(chip->irq, chip);

Since the irq number can start from 0, you should initialize chip->irq
with a negative value (e.g. -1), so that you can check the validity of
the irq number as above.

When you requested I/O ports or memory regions via
``pci_request_region()`` or ``pci_request_regions()`` like in this
example, release the resource(s) using the corresponding function,
``pci_release_region()`` or ``pci_release_regions()``.


.. code-block:: c

      pci_release_regions(chip->pci);

When you requested manually via ``request_region()`` or
``request_mem_region``, you can release it via ``release_resource()``.
Suppose that you keep the resource pointer returned from
``request_region()`` in chip->res_port, the release procedure looks
like:


.. code-block:: c

      release_and_free_resource(chip->res_port);

Don't forget to call ``pci_disable_device()`` before the end.

And finally, release the chip-specific record.


.. code-block:: c

      kfree(chip);

We didn't implement the hardware disabling part in the above. If you
need to do this, please note that the destructor may be called even
before the initialization of the chip is completed. It would be better
to have a flag to skip hardware disabling if the hardware was not
initialized yet.

When the chip-data is assigned to the card using ``snd_device_new()``
with ``SNDRV_DEV_LOWLELVEL`` , its destructor is called at the last.
That is, it is assured that all other components like PCMs and controls
have already been released. You don't have to stop PCMs, etc.
explicitly, but just call low-level hardware stopping.

The management of a memory-mapped region is almost as same as the
management of an I/O port. You'll need three fields like the following:


.. code-block:: c

      struct mychip {
              ....
              unsigned long iobase_phys;
              void __iomem *iobase_virt;
      };

and the allocation would be like below:


.. code-block:: c

      if ((err = pci_request_regions(pci, "My Chip")) < 0) {
              kfree(chip);
              return err;
      }
      chip->iobase_phys = pci_resource_start(pci, 0);
      chip->iobase_virt = ioremap_nocache(chip->iobase_phys,
                                          pci_resource_len(pci, 0));

and the corresponding destructor would be:


.. code-block:: c

      static int snd_mychip_free(struct mychip *chip)
      {
              ....
              if (chip->iobase_virt)
                      iounmap(chip->iobase_virt);
              ....
              pci_release_regions(chip->pci);
              ....
      }


.. _pci-resource-entries:

PCI Entries
===========

So far, so good. Let's finish the missing PCI stuff. At first, we need a
``pci_device_id`` table for this chipset. It's a table of PCI
vendor/device ID number, and some masks.

For example,


.. code-block:: c

      static struct pci_device_id snd_mychip_ids[] = {
              { PCI_VENDOR_ID_FOO, PCI_DEVICE_ID_BAR,
                PCI_ANY_ID, PCI_ANY_ID, 0, 0, 0, },
              ....
              { 0, }
      };
      MODULE_DEVICE_TABLE(pci, snd_mychip_ids);

The first and second fields of the ``pci_device_id`` structure are the
vendor and device IDs. If you have no reason to filter the matching
devices, you can leave the remaining fields as above. The last field of
the ``pci_device_id`` struct contains private data for this entry. You
can specify any value here, for example, to define specific operations
for supported device IDs. Such an example is found in the intel8x0
driver.

The last entry of this list is the terminator. You must specify this
all-zero entry.

Then, prepare the ``pci_driver`` record:


.. code-block:: c

      static struct pci_driver driver = {
              .name = KBUILD_MODNAME,
              .id_table = snd_mychip_ids,
              .probe = snd_mychip_probe,
              .remove = snd_mychip_remove,
      };

The ``probe`` and ``remove`` functions have already been defined in the
previous sections. The ``name`` field is the name string of this device.
Note that you must not use a slash “/” in this string.

And at last, the module entries:


.. code-block:: c

      static int __init alsa_card_mychip_init(void)
      {
              return pci_register_driver(&driver);
      }

      static void __exit alsa_card_mychip_exit(void)
      {
              pci_unregister_driver(&driver);
      }

      module_init(alsa_card_mychip_init)
      module_exit(alsa_card_mychip_exit)

Note that these module entries are tagged with ``__init`` and ``__exit``
prefixes.

Oh, one thing was forgotten. If you have no exported symbols, you need
to declare it in 2.2 or 2.4 kernels (it's not necessary in 2.6 kernels).


.. code-block:: c

      EXPORT_NO_SYMBOLS;

That's all!


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
