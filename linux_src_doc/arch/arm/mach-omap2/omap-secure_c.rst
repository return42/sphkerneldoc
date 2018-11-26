.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap-secure.c

.. _`omap_secure_dispatcher`:

omap_secure_dispatcher
======================

.. c:function:: u32 omap_secure_dispatcher(u32 idx, u32 flag, u32 nargs, u32 arg1, u32 arg2, u32 arg3, u32 arg4)

    Routine to dispatch low power secure service routines

    :param idx:
        The HAL API index
    :type idx: u32

    :param flag:
        The flag indicating criticality of operation
    :type flag: u32

    :param nargs:
        Number of valid arguments out of four.
    :type nargs: u32

    :param arg1:
        Parameters passed to secure API
    :type arg1: u32

    :param arg2:
        *undescribed*
    :type arg2: u32

    :param arg3:
        *undescribed*
    :type arg3: u32

    :param arg4:
        *undescribed*
    :type arg4: u32

.. _`omap_secure_dispatcher.description`:

Description
-----------

Return the non-zero error value on failure.

.. _`rx51_secure_dispatcher`:

rx51_secure_dispatcher
======================

.. c:function:: u32 rx51_secure_dispatcher(u32 idx, u32 process, u32 flag, u32 nargs, u32 arg1, u32 arg2, u32 arg3, u32 arg4)

    Routine to dispatch secure PPA API calls

    :param idx:
        The PPA API index
    :type idx: u32

    :param process:
        Process ID
    :type process: u32

    :param flag:
        The flag indicating criticality of operation
    :type flag: u32

    :param nargs:
        Number of valid arguments out of four.
    :type nargs: u32

    :param arg1:
        Parameters passed to secure API
    :type arg1: u32

    :param arg2:
        *undescribed*
    :type arg2: u32

    :param arg3:
        *undescribed*
    :type arg3: u32

    :param arg4:
        *undescribed*
    :type arg4: u32

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

    :param set_bits:
        bits to set in ACR
    :type set_bits: u32

    :param clear_bits:
        *undescribed*
    :type clear_bits: u32

.. _`rx51_secure_update_aux_cr.description`:

Description
-----------

Return the non-zero error value on failure.

.. _`rx51_secure_rng_call`:

rx51_secure_rng_call
====================

.. c:function:: u32 rx51_secure_rng_call(u32 ptr, u32 count, u32 flag)

    Routine for HW random generator

    :param ptr:
        *undescribed*
    :type ptr: u32

    :param count:
        *undescribed*
    :type count: u32

    :param flag:
        *undescribed*
    :type flag: u32

.. This file was automatic generated / don't edit.

