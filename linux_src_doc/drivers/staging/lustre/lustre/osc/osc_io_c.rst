.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/osc/osc_io.c

.. _`osc_io_submit`:

osc_io_submit
=============

.. c:function:: int osc_io_submit(const struct lu_env *env, const struct cl_io_slice *ios, enum cl_req_type crt, struct cl_2queue *queue)

    :cio_io_submit() method for osc layer. Iterates over pages in the in-queue, prepares each for io by calling \ :c:func:`cl_page_prep`\  and then either submits them through \ :c:func:`osc_io_submit_page`\  or, if page is already submitted, changes osc flags through \ :c:func:`osc_set_async_flags`\ .

    :param const struct lu_env \*env:
        *undescribed*

    :param const struct cl_io_slice \*ios:
        *undescribed*

    :param enum cl_req_type crt:
        *undescribed*

    :param struct cl_2queue \*queue:
        *undescribed*

.. _`osc_page_touch_at`:

osc_page_touch_at
=================

.. c:function:: void osc_page_touch_at(const struct lu_env *env, struct cl_object *obj, pgoff_t idx, size_t to)

    new page, if one were missing (i.e., if there were a hole at that place in the file, or accessed page is beyond the current file size).

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_object \*obj:
        *undescribed*

    :param pgoff_t idx:
        *undescribed*

    :param size_t to:
        *undescribed*

.. _`osc_page_touch_at.description`:

Description
-----------

Expand stripe KMS if necessary.

.. _`trunc_check_cb`:

trunc_check_cb
==============

.. c:function:: int trunc_check_cb(const struct lu_env *env, struct cl_io *io, struct osc_page *ops, void *cbdata)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct cl_io \*io:
        *undescribed*

    :param struct osc_page \*ops:
        *undescribed*

    :param void \*cbdata:
        *undescribed*

.. This file was automatic generated / don't edit.

