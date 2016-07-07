.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ti/wl1251/cmd.c

.. _`wl1251_cmd_send`:

wl1251_cmd_send
===============

.. c:function:: int wl1251_cmd_send(struct wl1251 *wl, u16 id, void *buf, size_t len)

    :param struct wl1251 \*wl:
        wl struct

    :param u16 id:
        command id

    :param void \*buf:
        buffer containing the command, must work with dma

    :param size_t len:
        length of the buffer

.. _`wl1251_cmd_test`:

wl1251_cmd_test
===============

.. c:function:: int wl1251_cmd_test(struct wl1251 *wl, void *buf, size_t buf_len, u8 answer)

    :param struct wl1251 \*wl:
        wl struct

    :param void \*buf:
        buffer containing the command, with all headers, must work with dma

    :param size_t buf_len:
        *undescribed*

    :param u8 answer:
        is answer needed

.. _`wl1251_cmd_interrogate`:

wl1251_cmd_interrogate
======================

.. c:function:: int wl1251_cmd_interrogate(struct wl1251 *wl, u16 id, void *buf, size_t len)

    :param struct wl1251 \*wl:
        wl struct

    :param u16 id:
        acx id

    :param void \*buf:
        buffer for the response, including all headers, must work with dma

    :param size_t len:
        length of buf

.. _`wl1251_cmd_configure`:

wl1251_cmd_configure
====================

.. c:function:: int wl1251_cmd_configure(struct wl1251 *wl, u16 id, void *buf, size_t len)

    :param struct wl1251 \*wl:
        wl struct

    :param u16 id:
        acx id

    :param void \*buf:
        buffer containing acx, including all headers, must work with dma

    :param size_t len:
        length of buf

.. This file was automatic generated / don't edit.

