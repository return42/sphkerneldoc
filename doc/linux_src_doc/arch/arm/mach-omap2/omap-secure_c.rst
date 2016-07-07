.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap-secure.c

.. _`omap_secure_dispatcher`:

omap_secure_dispatcher
======================

.. c:function:: u32 omap_secure_dispatcher(u32 idx, u32 flag, u32 nargs, u32 arg1, u32 arg2, u32 arg3, u32 arg4)

    Routine to dispatch low power secure service routines

    :param u32 idx:
        The HAL API index

    :param u32 flag:
        The flag indicating criticality of operation

    :param u32 nargs:
        Number of valid arguments out of four.

    :param u32 arg1:
        Parameters passed to secure API

    :param u32 arg2:
        *undescribed*

    :param u32 arg3:
        *undescribed*

    :param u32 arg4:
        *undescribed*

.. _`omap_secure_dispatcher.description`:

Description
-----------

Return the non-zero error value on failure.

.. _`rx51_secure_dispatcher`:

rx51_secure_dispatcher
======================

.. c:function:: u32 rx51_secure_dispatcher(u32 idx, u32 process, u32 flag, u32 nargs, u32 arg1, u32 arg2, u32 arg3, u32 arg4)

    Routine to dispatch secure PPA API calls

    :param u32 idx:
        The PPA API index

    :param u32 process:
        Process ID

    :param u32 flag:
        The flag indicating criticality of operation

    :param u32 nargs:
        Number of valid arguments out of four.

    :param u32 arg1:
        Parameters passed to secure API

    :param u32 arg2:
        *undescribed*

    :param u32 arg3:
        *undescribed*

    :param u32 arg4:
        *undescribed*

.. _`rx51_secure_dispatcher.description`:

Description
-----------

Return the non-zero error value on failure.

.. _`rx51_secure_dispatcher.note`:

NOTE
----

rx51_secure_dispatcher differs from omap_secure_dispatcher because
it calling \ :c:func:`omap_smc3`\  instead \ :c:func:`omap_smc2`\  and param[0] is nargs+1

.. _`rx51_secure_update_aux_cr`:

rx51_secure_update_aux_cr
=========================

.. c:function:: u32 rx51_secure_update_aux_cr(u32 set_bits, u32 clear_bits)

    Routine to modify the contents of Auxiliary Control Register

    :param u32 set_bits:
        bits to set in ACR

    :param u32 clear_bits:
        *undescribed*

.. _`rx51_secure_update_aux_cr.description`:

Description
-----------

Return the non-zero error value on failure.

.. _`rx51_secure_rng_call`:

rx51_secure_rng_call
====================

.. c:function:: u32 rx51_secure_rng_call(u32 ptr, u32 count, u32 flag)

    Routine for HW random generator

    :param u32 ptr:
        *undescribed*

    :param u32 count:
        *undescribed*

    :param u32 flag:
        *undescribed*

.. This file was automatic generated / don't edit.

