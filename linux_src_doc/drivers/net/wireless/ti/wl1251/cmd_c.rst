.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ti/wl1251/cmd.c

.. _`wl1251_cmd_send`:

wl1251_cmd_send
===============

.. c:function:: int wl1251_cmd_send(struct wl1251 *wl, u16 id, void *buf, size_t len)

    :param wl:
        wl struct
    :type wl: struct wl1251 \*

    :param id:
        command id
    :type id: u16

    :param buf:
        buffer containing the command, must work with dma
    :type buf: void \*

    :param len:
        length of the buffer
    :type len: size_t

.. _`wl1251_cmd_test`:

wl1251_cmd_test
===============

.. c:function:: int wl1251_cmd_test(struct wl1251 *wl, void *buf, size_t buf_len, u8 answer)

    :param wl:
        wl struct
    :type wl: struct wl1251 \*

    :param buf:
        buffer containing the command, with all headers, must work with dma
    :type buf: void \*

    :param buf_len:
        *undescribed*
    :type buf_len: size_t

    :param answer:
        is answer needed
    :type answer: u8

.. _`wl1251_cmd_interrogate`:

wl1251_cmd_interrogate
======================

.. c:function:: int wl1251_cmd_interrogate(struct wl1251 *wl, u16 id, void *buf, size_t len)

    :param wl:
        wl struct
    :type wl: struct wl1251 \*

    :param id:
        acx id
    :type id: u16

    :param buf:
        buffer for the response, including all headers, must work with dma
    :type buf: void \*

    :param len:
        length of buf
    :type len: size_t

.. _`wl1251_cmd_configure`:

wl1251_cmd_configure
====================

.. c:function:: int wl1251_cmd_configure(struct wl1251 *wl, u16 id, void *buf, size_t len)

    :param wl:
        wl struct
    :type wl: struct wl1251 \*

    :param id:
        acx id
    :type id: u16

    :param buf:
        buffer containing acx, including all headers, must work with dma
    :type buf: void \*

    :param len:
        length of buf
    :type len: size_t

.. This file was automatic generated / don't edit.

