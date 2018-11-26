.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/pm-common.c

.. _`s3c_pm_do_save`:

s3c_pm_do_save
==============

.. c:function:: void s3c_pm_do_save(struct sleep_save *ptr, int count)

    save a set of registers for restoration on resume.

    :param ptr:
        Pointer to an array of registers.
    :type ptr: struct sleep_save \*

    :param count:
        Size of the ptr array.
    :type count: int

.. _`s3c_pm_do_save.description`:

Description
-----------

Run through the list of registers given, saving their contents in the
array for later restoration when we wakeup.

.. _`s3c_pm_do_restore`:

s3c_pm_do_restore
=================

.. c:function:: void s3c_pm_do_restore(const struct sleep_save *ptr, int count)

    restore register values from the save list.

    :param ptr:
        Pointer to an array of registers.
    :type ptr: const struct sleep_save \*

    :param count:
        Size of the ptr array.
    :type count: int

.. _`s3c_pm_do_restore.description`:

Description
-----------

Restore the register values saved from \ :c:func:`s3c_pm_do_save`\ .

Note, we do not use \ :c:func:`S3C_PMDBG`\  in here, as the system may not have
restore the UARTs state yet

.. _`s3c_pm_do_restore_core`:

s3c_pm_do_restore_core
======================

.. c:function:: void s3c_pm_do_restore_core(const struct sleep_save *ptr, int count)

    early restore register values from save list.

    :param ptr:
        *undescribed*
    :type ptr: const struct sleep_save \*

    :param count:
        *undescribed*
    :type count: int

.. _`s3c_pm_do_restore_core.description`:

Description
-----------

This is similar to \ :c:func:`s3c_pm_do_restore`\  except we try and minimise the
side effects of the function in case registers that hardware might need
to work has been restored.

.. _`s3c_pm_do_restore_core.warning`:

WARNING
-------

Do not put any debug in here that may effect memory or use
peripherals, as things may be changing!

.. This file was automatic generated / don't edit.

