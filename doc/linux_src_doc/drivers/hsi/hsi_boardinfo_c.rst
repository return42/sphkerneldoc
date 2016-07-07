.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hsi/hsi_boardinfo.c

.. _`hsi_register_board_info`:

hsi_register_board_info
=======================

.. c:function:: int hsi_register_board_info(struct hsi_board_info const *info, unsigned int len)

    Register HSI clients information

    :param struct hsi_board_info const \*info:
        Array of HSI clients on the board

    :param unsigned int len:
        Length of the array

.. _`hsi_register_board_info.description`:

Description
-----------

HSI clients are statically declared and registered on board files.

HSI clients will be automatically registered to the HSI bus once the
controller and the port where the clients wishes to attach are registered
to it.

Return -errno on failure, 0 on success.

.. This file was automatic generated / don't edit.

