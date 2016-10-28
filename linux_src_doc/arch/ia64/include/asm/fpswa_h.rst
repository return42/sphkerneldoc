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

    :param unsigned long trap_type:
        *undescribed*

    :param void \*bundle:
        *undescribed*

    :param unsigned long \*ipsr:
        *undescribed*

    :param unsigned long \*fsr:
        *undescribed*

    :param unsigned long \*isr:
        *undescribed*

    :param unsigned long \*preds:
        *undescribed*

    :param unsigned long \*ifs:
        *undescribed*

    :param fp_state_t \*fp_state:
        *undescribed*

.. _`fpswa_interface_t`:

typedef fpswa_interface_t
=========================

.. c:type:: typedef fpswa_interface_t

    pointer to the interface itself on a call to the assist library

.. This file was automatic generated / don't edit.

