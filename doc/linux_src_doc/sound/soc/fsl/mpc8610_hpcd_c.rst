.. -*- coding: utf-8; mode: rst -*-

==============
mpc8610_hpcd.c
==============


.. _`mpc8610_hpcd_machine_probe`:

mpc8610_hpcd_machine_probe
==========================

.. c:function:: int mpc8610_hpcd_machine_probe (struct snd_soc_card *card)

    :param struct snd_soc_card \*card:

        *undescribed*



.. _`mpc8610_hpcd_machine_probe.description`:

Description
-----------


This function is used to initialize the board-specific hardware.

Here we program the DMACR and PMUXCR registers.



.. _`mpc8610_hpcd_startup`:

mpc8610_hpcd_startup
====================

.. c:function:: int mpc8610_hpcd_startup (struct snd_pcm_substream *substream)

    :param struct snd_pcm_substream \*substream:

        *undescribed*



.. _`mpc8610_hpcd_startup.description`:

Description
-----------


This function takes board-specific information, like clock frequencies
and serial data formats, and passes that information to the codec and
transport drivers.



.. _`mpc8610_hpcd_machine_remove`:

mpc8610_hpcd_machine_remove
===========================

.. c:function:: int mpc8610_hpcd_machine_remove (struct snd_soc_card *card)

    :param struct snd_soc_card \*card:

        *undescribed*



.. _`mpc8610_hpcd_machine_remove.description`:

Description
-----------


This function is called to remove the sound device for one SSI.  We
de-program the DMACR and PMUXCR register.



.. _`mpc8610_hpcd_probe`:

mpc8610_hpcd_probe
==================

.. c:function:: int mpc8610_hpcd_probe (struct platform_device *pdev)

    :param struct platform_device \*pdev:

        *undescribed*



.. _`mpc8610_hpcd_probe.description`:

Description
-----------


Although this is a machine driver, the SSI node is the "master" node with
respect to audio hardware connections.  Therefore, we create a new ASoC
device for each new SSI node that has a codec attached.



.. _`mpc8610_hpcd_remove`:

mpc8610_hpcd_remove
===================

.. c:function:: int mpc8610_hpcd_remove (struct platform_device *pdev)

    :param struct platform_device \*pdev:

        *undescribed*



.. _`mpc8610_hpcd_remove.description`:

Description
-----------


This function is called when the platform device is removed.



.. _`mpc8610_hpcd_init`:

mpc8610_hpcd_init
=================

.. c:function:: int mpc8610_hpcd_init ( void)

    :param void:
        no arguments



.. _`mpc8610_hpcd_init.description`:

Description
-----------


This function is called when this module is loaded.



.. _`mpc8610_hpcd_exit`:

mpc8610_hpcd_exit
=================

.. c:function:: void __exit mpc8610_hpcd_exit ( void)

    :param void:
        no arguments



.. _`mpc8610_hpcd_exit.description`:

Description
-----------


This function is called when this driver is unloaded.

