.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/page-flags.h

.. _`page_has_private`:

page_has_private
================

.. c:function:: int page_has_private(struct page *page)

    Determine if page has private stuff

    :param struct page \*page:
        The page to be checked

.. _`page_has_private.description`:

Description
-----------

Determine if a page has private stuff, indicating that release routines
should be invoked upon it.

.. This file was automatic generated / don't edit.

