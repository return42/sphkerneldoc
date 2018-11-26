.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/hyperv/hv_init.c

.. _`hyperv_report_panic_msg`:

hyperv_report_panic_msg
=======================

.. c:function:: void hyperv_report_panic_msg(phys_addr_t pa, size_t size)

    report panic message to Hyper-V

    :param pa:
        physical address of the panic page containing the message
    :type pa: phys_addr_t

    :param size:
        size of the message in the page
    :type size: size_t

.. This file was automatic generated / don't edit.

