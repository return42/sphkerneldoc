.. -*- coding: utf-8; mode: rst -*-

====
hw.c
====


.. _`whc_do_gencmd`:

whc_do_gencmd
=============

.. c:function:: int whc_do_gencmd (struct whc *whc, u32 cmd, u32 params, void *addr, size_t len)

    start a generic command via the WUSBGENCMDSTS register

    :param struct whc \*whc:
        the WHCI HC

    :param u32 cmd:
        command to start.

    :param u32 params:
        parameters for the command (the WUSBGENCMDPARAMS register value).

    :param void \*addr:
        pointer to any data for the command (may be NULL).

    :param size_t len:
        length of the data (if any).



.. _`whc_hw_error`:

whc_hw_error
============

.. c:function:: void whc_hw_error (struct whc *whc, const char *reason)

    recover from a hardware error

    :param struct whc \*whc:
        the WHCI HC that broke.

    :param const char \*reason:
        a description of the failure.



.. _`whc_hw_error.description`:

Description
-----------

Recover from broken hardware with a full reset.

