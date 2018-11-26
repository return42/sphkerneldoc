.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ti/wlcore/cmd.c

.. _`wl1271_cmd_test`:

wl1271_cmd_test
===============

.. c:function:: int wl1271_cmd_test(struct wl1271 *wl, void *buf, size_t buf_len, u8 answer)

    :param wl:
        wl struct
    :type wl: struct wl1271 \*

    :param buf:
        buffer containing the command, with all headers, must work with dma
    :type buf: void \*

    :param buf_len:
        *undescribed*
    :type buf_len: size_t

    :param answer:
        is answer needed
    :type answer: u8

.. _`wl1271_cmd_interrogate`:

wl1271_cmd_interrogate
======================

.. c:function:: int wl1271_cmd_interrogate(struct wl1271 *wl, u16 id, void *buf, size_t cmd_len, size_t res_len)

    :param wl:
        wl struct
    :type wl: struct wl1271 \*

    :param id:
        acx id
    :type id: u16

    :param buf:
        buffer for the response, including all headers, must work with dma
    :type buf: void \*

    :param cmd_len:
        *undescribed*
    :type cmd_len: size_t

    :param res_len:
        *undescribed*
    :type res_len: size_t

.. _`wlcore_cmd_configure_failsafe`:

wlcore_cmd_configure_failsafe
=============================

.. c:function:: int wlcore_cmd_configure_failsafe(struct wl1271 *wl, u16 id, void *buf, size_t len, unsigned long valid_rets)

    :param wl:
        wl struct
    :type wl: struct wl1271 \*

    :param id:
        acx id
    :type id: u16

    :param buf:
        buffer containing acx, including all headers, must work with dma
    :type buf: void \*

    :param len:
        length of buf
    :type len: size_t

    :param valid_rets:
        bitmap of valid cmd status codes (i.e. return values).
        return the cmd status on success.
    :type valid_rets: unsigned long

.. This file was automatic generated / don't edit.

