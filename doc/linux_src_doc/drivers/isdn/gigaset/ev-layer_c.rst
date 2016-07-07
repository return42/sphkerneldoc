.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/isdn/gigaset/ev-layer.c

.. _`gigaset_handle_modem_response`:

gigaset_handle_modem_response
=============================

.. c:function:: void gigaset_handle_modem_response(struct cardstate *cs)

    process received modem response

    :param struct cardstate \*cs:
        device descriptor structure.

.. _`gigaset_handle_modem_response.description`:

Description
-----------

Called by asyncdata/isocdata if a block of data received from the
device must be processed as a modem command response. The data is
already in the cs structure.

.. This file was automatic generated / don't edit.

