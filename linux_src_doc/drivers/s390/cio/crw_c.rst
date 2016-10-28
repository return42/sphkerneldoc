.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/crw.c

.. _`crw_register_handler`:

crw_register_handler
====================

.. c:function:: int crw_register_handler(int rsc, crw_handler_t handler)

    register a channel report word handler

    :param int rsc:
        reporting source code to handle

    :param crw_handler_t handler:
        handler to be registered

.. _`crw_register_handler.description`:

Description
-----------

Returns \ ``0``\  on success and a negative error value otherwise.

.. _`crw_unregister_handler`:

crw_unregister_handler
======================

.. c:function:: void crw_unregister_handler(int rsc)

    unregister a channel report word handler

    :param int rsc:
        reporting source code to handle

.. This file was automatic generated / don't edit.

