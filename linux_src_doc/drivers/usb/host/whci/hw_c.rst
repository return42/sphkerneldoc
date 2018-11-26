.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/whci/hw.c

.. _`whc_do_gencmd`:

whc_do_gencmd
=============

.. c:function:: int whc_do_gencmd(struct whc *whc, u32 cmd, u32 params, void *addr, size_t len)

    start a generic command via the WUSBGENCMDSTS register

    :param whc:
        the WHCI HC
    :type whc: struct whc \*

    :param cmd:
        command to start.
    :type cmd: u32

    :param params:
        parameters for the command (the WUSBGENCMDPARAMS register value).
    :type params: u32

    :param addr:
        pointer to any data for the command (may be NULL).
    :type addr: void \*

    :param len:
        length of the data (if any).
    :type len: size_t

.. _`whc_hw_error`:

whc_hw_error
============

.. c:function:: void whc_hw_error(struct whc *whc, const char *reason)

    recover from a hardware error

    :param whc:
        the WHCI HC that broke.
    :type whc: struct whc \*

    :param reason:
        a description of the failure.
    :type reason: const char \*

.. _`whc_hw_error.description`:

Description
-----------

Recover from broken hardware with a full reset.

.. This file was automatic generated / don't edit.

