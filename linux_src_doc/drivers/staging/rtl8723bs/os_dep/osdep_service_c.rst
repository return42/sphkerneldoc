.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8723bs/os_dep/osdep_service.c

.. _`rtw_cbuf_full`:

rtw_cbuf_full
=============

.. c:function:: bool rtw_cbuf_full(struct rtw_cbuf *cbuf)

    test if cbuf is full

    :param struct rtw_cbuf \*cbuf:
        pointer of struct rtw_cbuf

.. _`rtw_cbuf_full.return`:

Return
------

true if cbuf is full

.. _`rtw_cbuf_empty`:

rtw_cbuf_empty
==============

.. c:function:: bool rtw_cbuf_empty(struct rtw_cbuf *cbuf)

    test if cbuf is empty

    :param struct rtw_cbuf \*cbuf:
        pointer of struct rtw_cbuf

.. _`rtw_cbuf_empty.return`:

Return
------

true if cbuf is empty

.. _`rtw_cbuf_push`:

rtw_cbuf_push
=============

.. c:function:: bool rtw_cbuf_push(struct rtw_cbuf *cbuf, void *buf)

    push a pointer into cbuf

    :param struct rtw_cbuf \*cbuf:
        pointer of struct rtw_cbuf

    :param void \*buf:
        pointer to push in

.. _`rtw_cbuf_push.description`:

Description
-----------

Lock free operation, be careful of the use scheme

.. _`rtw_cbuf_push.return`:

Return
------

true push success

.. _`rtw_cbuf_pop`:

rtw_cbuf_pop
============

.. c:function:: void *rtw_cbuf_pop(struct rtw_cbuf *cbuf)

    pop a pointer from cbuf

    :param struct rtw_cbuf \*cbuf:
        pointer of struct rtw_cbuf

.. _`rtw_cbuf_pop.description`:

Description
-----------

Lock free operation, be careful of the use scheme

.. _`rtw_cbuf_pop.return`:

Return
------

pointer popped out

.. _`rtw_cbuf_alloc`:

rtw_cbuf_alloc
==============

.. c:function:: struct rtw_cbuf *rtw_cbuf_alloc(u32 size)

    allocte a rtw_cbuf with given size and do initialization

    :param u32 size:
        size of pointer

.. _`rtw_cbuf_alloc.return`:

Return
------

pointer of srtuct rtw_cbuf, NULL for allocation failure

.. This file was automatic generated / don't edit.

