.. -*- coding: utf-8; mode: rst -*-

=====
cmd.c
=====


.. _`wl1271_cmd_test`:

wl1271_cmd_test
===============

.. c:function:: int wl1271_cmd_test (struct wl1271 *wl, void *buf, size_t buf_len, u8 answer)

    :param struct wl1271 \*wl:
        wl struct

    :param void \*buf:
        buffer containing the command, with all headers, must work with dma

    :param size_t buf_len:

        *undescribed*

    :param u8 answer:
        is answer needed



.. _`wl1271_cmd_interrogate`:

wl1271_cmd_interrogate
======================

.. c:function:: int wl1271_cmd_interrogate (struct wl1271 *wl, u16 id, void *buf, size_t cmd_len, size_t res_len)

    :param struct wl1271 \*wl:
        wl struct

    :param u16 id:
        acx id

    :param void \*buf:
        buffer for the response, including all headers, must work with dma

    :param size_t cmd_len:

        *undescribed*

    :param size_t res_len:

        *undescribed*



.. _`wlcore_cmd_configure_failsafe`:

wlcore_cmd_configure_failsafe
=============================

.. c:function:: int wlcore_cmd_configure_failsafe (struct wl1271 *wl, u16 id, void *buf, size_t len, unsigned long valid_rets)

    :param struct wl1271 \*wl:
        wl struct

    :param u16 id:
        acx id

    :param void \*buf:
        buffer containing acx, including all headers, must work with dma

    :param size_t len:
        length of buf

    :param unsigned long valid_rets:
        bitmap of valid cmd status codes (i.e. return values).
        return the cmd status on success.

