.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/crw.c

.. _`crw_register_handler`:

crw_register_handler
====================

.. c:function:: int crw_register_handler(int rsc, crw_handler_t handler)

    register a channel report word handler

    :param rsc:
        reporting source code to handle
    :type rsc: int

    :param handler:
        handler to be registered
    :type handler: crw_handler_t

.. _`crw_register_handler.description`:

Description
-----------

Returns \ ``0``\  on success and a negative error value otherwise.

.. _`crw_unregister_handler`:

crw_unregister_handler
======================

.. c:function:: void crw_unregister_handler(int rsc)

    unregister a channel report word handler

    :param rsc:
        reporting source code to handle
    :type rsc: int

.. This file was automatic generated / don't edit.

