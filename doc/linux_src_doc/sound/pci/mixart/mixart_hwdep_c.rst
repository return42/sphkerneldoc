.. -*- coding: utf-8; mode: rst -*-

==============
mixart_hwdep.c
==============


.. _`mixart_wait_nice_for_register_value`:

mixart_wait_nice_for_register_value
===================================

.. c:function:: int mixart_wait_nice_for_register_value (struct mixart_mgr *mgr, u32 offset, int is_egal, u32 value, unsigned long timeout)

    :param struct mixart_mgr \*mgr:
        pointer to miXart manager structure

    :param u32 offset:
        unsigned pseudo_register base + offset of value

    :param int is_egal:
        wait for the equal value

    :param u32 value:
        value

    :param unsigned long timeout:
        timeout in centisenconds

