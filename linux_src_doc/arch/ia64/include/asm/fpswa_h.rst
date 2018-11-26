.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/include/asm/fpswa.h

.. _`fp_state_t`:

typedef fp_state_t
==================

.. c:type:: typedef fp_state_t

    the trap/fault handler

.. _`efi_fpswa_t`:

efi_fpswa_t
===========

.. c:function:: fpswa_ret_t efi_fpswa_t(unsigned long trap_type, void *bundle, unsigned long *ipsr, unsigned long *fsr, unsigned long *isr, unsigned long *preds, unsigned long *ifs, fp_state_t *fp_state)

    library. This function is invoked by the Floating point software assist trap/fault handler.

    :param trap_type:
        *undescribed*
    :type trap_type: unsigned long

    :param bundle:
        *undescribed*
    :type bundle: void \*

    :param ipsr:
        *undescribed*
    :type ipsr: unsigned long \*

    :param fsr:
        *undescribed*
    :type fsr: unsigned long \*

    :param isr:
        *undescribed*
    :type isr: unsigned long \*

    :param preds:
        *undescribed*
    :type preds: unsigned long \*

    :param ifs:
        *undescribed*
    :type ifs: unsigned long \*

    :param fp_state:
        *undescribed*
    :type fp_state: fp_state_t \*

.. _`fpswa_interface_t`:

typedef fpswa_interface_t
=========================

.. c:type:: typedef fpswa_interface_t

    pointer to the interface itself on a call to the assist library

.. This file was automatic generated / don't edit.

