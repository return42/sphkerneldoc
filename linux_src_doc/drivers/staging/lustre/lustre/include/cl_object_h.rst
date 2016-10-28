.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/cl_object.h

.. _`cl_object_for_each`:

cl_object_for_each
==================

.. c:function::  cl_object_for_each( slice,  obj)

    iterate over all layers of the object \a obj, assigning every layer top-to-bottom to \a slice.

    :param  slice:
        *undescribed*

    :param  obj:
        *undescribed*

.. _`cl_object_for_each_reverse`:

cl_object_for_each_reverse
==========================

.. c:function::  cl_object_for_each_reverse( slice,  obj)

    iterate over all layers of the object \a obj, assigning every layer bottom-to-top to \a slice.

    :param  slice:
        *undescribed*

    :param  obj:
        *undescribed*

.. _`cl_page_debug`:

CL_PAGE_DEBUG
=============

.. c:function::  CL_PAGE_DEBUG( mask,  env,  page,  format,  ...)

    :param  mask:
        *undescribed*

    :param  env:
        *undescribed*

    :param  page:
        *undescribed*

    :param  format:
        *undescribed*

    :param ... :
        variable arguments

.. _`cl_page_header`:

CL_PAGE_HEADER
==============

.. c:function::  CL_PAGE_HEADER( mask,  env,  page,  format,  ...)

    :param  mask:
        *undescribed*

    :param  env:
        *undescribed*

    :param  page:
        *undescribed*

    :param  format:
        *undescribed*

    :param ... :
        variable arguments

.. _`cl_site_stats_print`:

cl_site_stats_print
===================

.. c:function:: int cl_site_stats_print(const struct cl_site *site, struct seq_file *m)

    ll_rd\_\*()-style functions.

    :param const struct cl_site \*site:
        *undescribed*

    :param struct seq_file \*m:
        *undescribed*

.. _`cl_object_same`:

cl_object_same
==============

.. c:function:: int cl_object_same(struct cl_object *o0, struct cl_object *o1)

    :param struct cl_object \*o0:
        *undescribed*

    :param struct cl_object \*o1:
        *undescribed*

.. _`cl_object_refc`:

cl_object_refc
==============

.. c:function:: int cl_object_refc(struct cl_object *clob)

    :param struct cl_object \*clob:
        *undescribed*

.. _`cl_io_is_append`:

cl_io_is_append
===============

.. c:function:: int cl_io_is_append(const struct cl_io *io)

    :param const struct cl_io \*io:
        *undescribed*

.. _`cl_io_is_trunc`:

cl_io_is_trunc
==============

.. c:function:: int cl_io_is_trunc(const struct cl_io *io)

    :param const struct cl_io \*io:
        *undescribed*

.. _`cl_page_list_last`:

cl_page_list_last
=================

.. c:function:: struct cl_page *cl_page_list_last(struct cl_page_list *plist)

    :param struct cl_page_list \*plist:
        *undescribed*

.. _`cl_page_list_for_each`:

cl_page_list_for_each
=====================

.. c:function::  cl_page_list_for_each( page,  list)

    :param  page:
        *undescribed*

    :param  list:
        *undescribed*

.. _`cl_page_list_for_each_safe`:

cl_page_list_for_each_safe
==========================

.. c:function::  cl_page_list_for_each_safe( page,  temp,  list)

    :param  page:
        *undescribed*

    :param  temp:
        *undescribed*

    :param  list:
        *undescribed*

.. This file was automatic generated / don't edit.

