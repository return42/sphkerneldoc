.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/card/mic_device.c

.. _`mic_request_card_irq`:

mic_request_card_irq
====================

.. c:function:: struct mic_irq *mic_request_card_irq(irq_handler_t handler, irq_handler_t thread_fn, const char *name, void *data, int index)

    request an irq.

    :param irq_handler_t handler:
        interrupt handler passed to request_threaded_irq.

    :param irq_handler_t thread_fn:
        thread fn. passed to request_threaded_irq.

    :param const char \*name:
        The ASCII name of the callee requesting the irq.

    :param void \*data:
        private data that is returned back when calling the
        function handler.

    :param int index:
        The doorbell index of the requester.

.. _`mic_request_card_irq.return`:

Return
------

The cookie that is transparent to the caller. Passed
back when calling mic_free_irq. An appropriate error code
is returned on failure. Caller needs to use IS_ERR(return_val)
to check for failure and PTR_ERR(return_val) to obtained the
error code.

.. _`mic_free_card_irq`:

mic_free_card_irq
=================

.. c:function:: void mic_free_card_irq(struct mic_irq *cookie, void *data)

    free irq.

    :param struct mic_irq \*cookie:
        cookie obtained during a successful call to mic_request_threaded_irq

    :param void \*data:
        private data specified by the calling function during the
        mic_request_threaded_irq

.. _`mic_free_card_irq.return`:

Return
------

none.

.. _`mic_next_card_db`:

mic_next_card_db
================

.. c:function:: int mic_next_card_db( void)

    Get the doorbell with minimum usage count.

    :param  void:
        no arguments

.. _`mic_next_card_db.description`:

Description
-----------

Returns the irq index.

.. _`mic_init_irq`:

mic_init_irq
============

.. c:function:: int mic_init_irq( void)

    Initialize irq information.

    :param  void:
        no arguments

.. _`mic_init_irq.description`:

Description
-----------

Returns 0 in success. Appropriate error code on failure.

.. _`mic_uninit_irq`:

mic_uninit_irq
==============

.. c:function:: void mic_uninit_irq( void)

    Uninitialize irq information.

    :param  void:
        no arguments

.. _`mic_uninit_irq.description`:

Description
-----------

None.

.. This file was automatic generated / don't edit.

