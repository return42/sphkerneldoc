.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-mm-lantiq.c

.. _`ltq_mm_apply`:

ltq_mm_apply
============

.. c:function:: void ltq_mm_apply(struct ltq_mm *chip)

    write the shadow value to the ebu address.

    :param struct ltq_mm \*chip:
        Pointer to our private data structure.

.. _`ltq_mm_apply.description`:

Description
-----------

Write the shadow value to the EBU to set the gpios. We need to set the
global EBU lock to make sure that PCI/MTD dont break.

.. _`ltq_mm_set`:

ltq_mm_set
==========

.. c:function:: void ltq_mm_set(struct gpio_chip *gc, unsigned offset, int value)

    gpio_chip->set - set gpios.

    :param struct gpio_chip \*gc:
        Pointer to gpio_chip device structure.

    :param unsigned offset:
        *undescribed*

    :param int value:
        *undescribed*

.. _`ltq_mm_set.description`:

Description
-----------

Set the shadow value and call ltq_mm_apply.

.. _`ltq_mm_dir_out`:

ltq_mm_dir_out
==============

.. c:function:: int ltq_mm_dir_out(struct gpio_chip *gc, unsigned offset, int value)

    gpio_chip->dir_out - set gpio direction.

    :param struct gpio_chip \*gc:
        Pointer to gpio_chip device structure.

    :param unsigned offset:
        *undescribed*

    :param int value:
        *undescribed*

.. _`ltq_mm_dir_out.description`:

Description
-----------

Same as ltq_mm_set, always returns 0.

.. _`ltq_mm_save_regs`:

ltq_mm_save_regs
================

.. c:function:: void ltq_mm_save_regs(struct of_mm_gpio_chip *mm_gc)

    Set initial values of GPIO pins

    :param struct of_mm_gpio_chip \*mm_gc:
        pointer to memory mapped GPIO chip structure

.. This file was automatic generated / don't edit.

