.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/exynos-combiner.c

.. _`combiner_suspend`:

combiner_suspend
================

.. c:function:: int combiner_suspend( void)

    save interrupt combiner state before suspend

    :param  void:
        no arguments

.. _`combiner_suspend.description`:

Description
-----------

Save the interrupt enable set register for all combiner groups since
the state is lost when the system enters into a sleep state.

.. _`combiner_resume`:

combiner_resume
===============

.. c:function:: void combiner_resume( void)

    restore interrupt combiner state after resume

    :param  void:
        no arguments

.. _`combiner_resume.description`:

Description
-----------

Restore the interrupt enable set register for all combiner groups since
the state is lost when the system enters into a sleep state on suspend.

.. This file was automatic generated / don't edit.

