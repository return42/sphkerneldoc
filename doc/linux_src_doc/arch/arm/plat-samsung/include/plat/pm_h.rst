.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/pm.h

.. _`s3c_pm_debug_smdkled`:

s3c_pm_debug_smdkled
====================

.. c:function:: void s3c_pm_debug_smdkled(u32 set, u32 clear)

    Debug PM suspend/resume via SMDK Board LEDs

    :param u32 set:
        set bits for the state of the LEDs

    :param u32 clear:
        clear bits for the state of the LEDs.

.. _`s3c_pm_configure_extint`:

s3c_pm_configure_extint
=======================

.. c:function:: void s3c_pm_configure_extint( void)

    ensure pins are correctly set for IRQ

    :param  void:
        no arguments

.. _`s3c_pm_configure_extint.description`:

Description
-----------

Setup all the necessary GPIO pins for waking the system on external
interrupt.

.. _`samsung_pm_restore_gpios`:

samsung_pm_restore_gpios
========================

.. c:function:: void samsung_pm_restore_gpios( void)

    restore the state of the gpios after sleep.

    :param  void:
        no arguments

.. _`samsung_pm_restore_gpios.description`:

Description
-----------

Restore the state of the GPIO pins after sleep, which may involve ensuring
that we do not glitch the state of the pins from that the bootloader's
resume code has done.

.. _`samsung_pm_save_gpios`:

samsung_pm_save_gpios
=====================

.. c:function:: void samsung_pm_save_gpios( void)

    save the state of the GPIOs for restoring after sleep.

    :param  void:
        no arguments

.. _`samsung_pm_save_gpios.description`:

Description
-----------

Save the GPIO states for resotration on resume. See \ :c:func:`samsung_pm_restore_gpios`\ .

.. This file was automatic generated / don't edit.

