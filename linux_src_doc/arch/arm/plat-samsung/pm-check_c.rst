.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/pm-check.c

.. _`s3c_pm_runcheck`:

s3c_pm_runcheck
===============

.. c:function:: u32 *s3c_pm_runcheck(struct resource *res, u32 *val)

    helper to check a resource on restore.

    :param res:
        The resource to check
    :type res: struct resource \*

    :param val:
        *undescribed*
    :type val: u32 \*

.. _`s3c_pm_runcheck.description`:

Description
-----------

Called from the \ :c:func:`s3c_pm_check_restore`\  via \ :c:func:`s3c_pm_run_sysram`\ , this
function runs the given memory resource checking it against the stored
CRC to ensure that memory is restored. The function tries to skip as
many of the areas used during the suspend process.

.. _`s3c_pm_check_restore`:

s3c_pm_check_restore
====================

.. c:function:: void s3c_pm_check_restore( void)

    memory check called on resume

    :param void:
        no arguments
    :type void: 

.. _`s3c_pm_check_restore.description`:

Description
-----------

check the CRCs after the restore event and free the memory used
to hold them

.. _`s3c_pm_check_cleanup`:

s3c_pm_check_cleanup
====================

.. c:function:: void s3c_pm_check_cleanup( void)

    free memory resources

    :param void:
        no arguments
    :type void: 

.. _`s3c_pm_check_cleanup.description`:

Description
-----------

Free the resources that where allocated by the suspend
memory check code. We do this separately from the
\ :c:func:`s3c_pm_check_restore`\  function as we cannot call any
functions that might sleep during that resume.

.. This file was automatic generated / don't edit.

