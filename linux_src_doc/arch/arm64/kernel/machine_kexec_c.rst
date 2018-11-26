.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kernel/machine_kexec.c

.. _`kexec_image_info`:

kexec_image_info
================

.. c:function::  kexec_image_info( _i)

    For debugging output.

    :param _i:
        *undescribed*
    :type _i: 

.. _`machine_kexec_prepare`:

machine_kexec_prepare
=====================

.. c:function:: int machine_kexec_prepare(struct kimage *kimage)

    Prepare for a kexec reboot.

    :param kimage:
        *undescribed*
    :type kimage: struct kimage \*

.. _`machine_kexec_prepare.description`:

Description
-----------

Called from the core kexec code when a kernel image is loaded.
Forbid loading a kexec kernel if we have no way of hotplugging cpus or cpus
are stuck in the kernel. This avoids a panic once we hit \ :c:func:`machine_kexec`\ .

.. _`kexec_list_flush`:

kexec_list_flush
================

.. c:function:: void kexec_list_flush(struct kimage *kimage)

    Helper to flush the kimage list and source pages to PoC.

    :param kimage:
        *undescribed*
    :type kimage: struct kimage \*

.. _`kexec_segment_flush`:

kexec_segment_flush
===================

.. c:function:: void kexec_segment_flush(const struct kimage *kimage)

    Helper to flush the kimage segments to PoC.

    :param kimage:
        *undescribed*
    :type kimage: const struct kimage \*

.. _`machine_kexec`:

machine_kexec
=============

.. c:function:: void machine_kexec(struct kimage *kimage)

    Do the kexec reboot.

    :param kimage:
        *undescribed*
    :type kimage: struct kimage \*

.. _`machine_kexec.description`:

Description
-----------

Called from the core kexec code for a sys_reboot with LINUX_REBOOT_CMD_KEXEC.

.. _`machine_crash_shutdown`:

machine_crash_shutdown
======================

.. c:function:: void machine_crash_shutdown(struct pt_regs *regs)

    shutdown non-crashing cpus and save registers

    :param regs:
        *undescribed*
    :type regs: struct pt_regs \*

.. This file was automatic generated / don't edit.

