.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/mixart/mixart_hwdep.c

.. _`mixart_wait_nice_for_register_value`:

mixart_wait_nice_for_register_value
===================================

.. c:function:: int mixart_wait_nice_for_register_value(struct mixart_mgr *mgr, u32 offset, int is_egal, u32 value, unsigned long timeout)

    :param mgr:
        pointer to miXart manager structure
    :type mgr: struct mixart_mgr \*

    :param offset:
        unsigned pseudo_register base + offset of value
    :type offset: u32

    :param is_egal:
        wait for the equal value
    :type is_egal: int

    :param value:
        value
    :type value: u32

    :param timeout:
        timeout in centisenconds
    :type timeout: unsigned long

.. This file was automatic generated / don't edit.

