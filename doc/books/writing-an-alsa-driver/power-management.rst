
.. _power-management:

================
Power Management
================

If the chip is supposed to work with suspend/resume functions, you need to add power-management code to the driver. The additional code for power-management should be ``ifdef``'ed
with ``CONFIG_PM``.

If the driver *fully* supports suspend/resume that is, the device can be properly resumed to its state when suspend was called, you can set the ``SNDRV_PCM_INFO_RESUME`` flag in
the pcm info field. Usually, this is possible when the registers of the chip can be safely saved and restored to RAM. If this is set, the trigger callback is called with
``SNDRV_PCM_TRIGGER_RESUME`` after the resume callback completes.

Even if the driver doesn't support PM fully but partial suspend/resume is still possible, it's still worthy to implement suspend/resume callbacks. In such a case, applications
would reset the status by calling ``snd_pcm_prepare()`` and restart the stream appropriately. Hence, you can define suspend/resume callbacks below but don't set
``SNDRV_PCM_INFO_RESUME`` info flag to the PCM.

Note that the trigger with SUSPEND can always be called when ``snd_pcm_suspend_all`` is called, regardless of the ``SNDRV_PCM_INFO_RESUME`` flag. The ``RESUME`` flag affects only
the behavior of ``snd_pcm_resume()``. (Thus, in theory, ``SNDRV_PCM_TRIGGER_RESUME`` isn't needed to be handled in the trigger callback when no ``SNDRV_PCM_INFO_RESUME`` flag is
set. But, it's better to keep it for compatibility reasons.)

In the earlier version of ALSA drivers, a common power-management layer was provided, but it has been removed. The driver needs to define the suspend/resume hooks according to the
bus the device is connected to. In the case of PCI drivers, the callbacks look like below:


.. code-block:: c

      #ifdef CONFIG_PM
      static int snd_my_suspend(struct pci_dev &#x22C6;pci, pm_message_t state)
      {
              .... /&#x22C6; do things for suspend &#x22C6;/
              return 0;
      }
      static int snd_my_resume(struct pci_dev &#x22C6;pci)
      {
              .... /&#x22C6; do things for suspend &#x22C6;/
              return 0;
      }
      #endif

The scheme of the real suspend job is as follows.

1. Retrieve the card and the chip data.

2. Call ``snd_power_change_state()`` with ``SNDRV_CTL_POWER_D3hot`` to change the power status.

3. Call ``snd_pcm_suspend_all()`` to suspend the running PCM streams.

4. If AC97 codecs are used, call ``snd_ac97_suspend()`` for each codec.

5. Save the register values if necessary.

6. Stop the hardware if necessary.

7. Disable the PCI device by calling ``pci_disable_device()``. Then, call ``pci_save_state()`` at last.

A typical code would be like:


.. code-block:: c

      static int mychip_suspend(struct pci_dev &#x22C6;pci, pm_message_t state)
      {
              /&#x22C6; (1) &#x22C6;/
              struct snd_card &#x22C6;card = pci_get_drvdata(pci);
              struct mychip &#x22C6;chip = card->private_data;
              /&#x22C6; (2) &#x22C6;/
              snd_power_change_state(card, SNDRV_CTL_POWER_D3hot);
              /&#x22C6; (3) &#x22C6;/
              snd_pcm_suspend_all(chip->pcm);
              /&#x22C6; (4) &#x22C6;/
              snd_ac97_suspend(chip->ac97);
              /&#x22C6; (5) &#x22C6;/
              snd_mychip_save_registers(chip);
              /&#x22C6; (6) &#x22C6;/
              snd_mychip_stop_hardware(chip);
              /&#x22C6; (7) &#x22C6;/
              pci_disable_device(pci);
              pci_save_state(pci);
              return 0;
      }

The scheme of the real resume job is as follows.

1. Retrieve the card and the chip data.

2. Set up PCI. First, call ``pci_restore_state()``. Then enable the pci device again by calling ``pci_enable_device()``. Call ``pci_set_master()`` if necessary, too.

3. Re-initialize the chip.

4. Restore the saved registers if necessary.

5. Resume the mixer, e.g. calling ``snd_ac97_resume()``.

6. Restart the hardware (if any).

7. Call ``snd_power_change_state()`` with ``SNDRV_CTL_POWER_D0`` to notify the processes.

A typical code would be like:


.. code-block:: c

      static int mychip_resume(struct pci_dev &#x22C6;pci)
      {
              /&#x22C6; (1) &#x22C6;/
              struct snd_card &#x22C6;card = pci_get_drvdata(pci);
              struct mychip &#x22C6;chip = card->private_data;
              /&#x22C6; (2) &#x22C6;/
              pci_restore_state(pci);
              pci_enable_device(pci);
              pci_set_master(pci);
              /&#x22C6; (3) &#x22C6;/
              snd_mychip_reinit_chip(chip);
              /&#x22C6; (4) &#x22C6;/
              snd_mychip_restore_registers(chip);
              /&#x22C6; (5) &#x22C6;/
              snd_ac97_resume(chip->ac97);
              /&#x22C6; (6) &#x22C6;/
              snd_mychip_restart_chip(chip);
              /&#x22C6; (7) &#x22C6;/
              snd_power_change_state(card, SNDRV_CTL_POWER_D0);
              return 0;
      }

As shown in the above, it's better to save registers after suspending the PCM operations via ``snd_pcm_suspend_all()`` or ``snd_pcm_suspend()``. It means that the PCM streams are
already stopped when the register snapshot is taken. But, remember that you don't have to restart the PCM stream in the resume callback. It'll be restarted via trigger call with
``SNDRV_PCM_TRIGGER_RESUME`` when necessary.

OK, we have all callbacks now. Let's set them up. In the initialization of the card, make sure that you can get the chip data from the card instance, typically via ``private_data``
field, in case you created the chip data individually.


.. code-block:: c

      static int snd_mychip_probe(struct pci_dev &#x22C6;pci,
                                  const struct pci_device_id &#x22C6;pci_id)
      {
              ....
              struct snd_card &#x22C6;card;
              struct mychip &#x22C6;chip;
              int err;
              ....
              err = snd_card_new(&pci->dev, index[dev], id[dev], THIS_MODULE,
                                 0, &card);
              ....
              chip = kzalloc(sizeof(&#x22C6;chip), GFP_KERNEL);
              ....
              card->private_data = chip;
              ....
      }

When you created the chip data with ``snd_card_new()``, it's anyway accessible via ``private_data`` field.


.. code-block:: c

      static int snd_mychip_probe(struct pci_dev &#x22C6;pci,
                                  const struct pci_device_id &#x22C6;pci_id)
      {
              ....
              struct snd_card &#x22C6;card;
              struct mychip &#x22C6;chip;
              int err;
              ....
              err = snd_card_new(&pci->dev, index[dev], id[dev], THIS_MODULE,
                                 sizeof(struct mychip), &card);
              ....
              chip = card->private_data;
              ....
      }

If you need a space to save the registers, allocate the buffer for it here, too, since it would be fatal if you cannot allocate a memory in the suspend phase. The allocated buffer
should be released in the corresponding destructor.

And next, set suspend/resume callbacks to the pci_driver.


.. code-block:: c

      static struct pci_driver driver = {
              .name = KBUILD_MODNAME,
              .id_table = snd_my_ids,
              .probe = snd_my_probe,
              .remove = snd_my_remove,
      #ifdef CONFIG_PM
              .suspend = snd_my_suspend,
              .resume = snd_my_resume,
      #endif
      };


