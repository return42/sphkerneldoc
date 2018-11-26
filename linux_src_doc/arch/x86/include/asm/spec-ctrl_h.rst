.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/spec-ctrl.h

.. _`x86_spec_ctrl_set_guest`:

x86_spec_ctrl_set_guest
=======================

.. c:function:: void x86_spec_ctrl_set_guest(u64 guest_spec_ctrl, u64 guest_virt_spec_ctrl)

    Set speculation control registers for the guest

    :param guest_spec_ctrl:
        The guest content of MSR_SPEC_CTRL
    :type guest_spec_ctrl: u64

    :param guest_virt_spec_ctrl:
        The guest controlled bits of MSR_VIRT_SPEC_CTRL
        (may get translated to MSR_AMD64_LS_CFG bits)
    :type guest_virt_spec_ctrl: u64

.. _`x86_spec_ctrl_set_guest.description`:

Description
-----------

Avoids writing to the MSR if the content/bits are the same

.. _`x86_spec_ctrl_restore_host`:

x86_spec_ctrl_restore_host
==========================

.. c:function:: void x86_spec_ctrl_restore_host(u64 guest_spec_ctrl, u64 guest_virt_spec_ctrl)

    Restore host speculation control registers

    :param guest_spec_ctrl:
        The guest content of MSR_SPEC_CTRL
    :type guest_spec_ctrl: u64

    :param guest_virt_spec_ctrl:
        The guest controlled bits of MSR_VIRT_SPEC_CTRL
        (may get translated to MSR_AMD64_LS_CFG bits)
    :type guest_virt_spec_ctrl: u64

.. _`x86_spec_ctrl_restore_host.description`:

Description
-----------

Avoids writing to the MSR if the content/bits are the same

.. This file was automatic generated / don't edit.

