.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/attach.c

.. _`ath5k_hw_post`:

ath5k_hw_post
=============

.. c:function:: int ath5k_hw_post(struct ath5k_hw *ah)

    Power On Self Test helper function

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. _`ath5k_hw_init`:

ath5k_hw_init
=============

.. c:function:: int ath5k_hw_init(struct ath5k_hw *ah)

    Check if hw is supported and init the needed structs

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\  associated with the device

.. _`ath5k_hw_init.description`:

Description
-----------

Check if the device is supported, perform a POST and initialize the needed
structs. Returns -ENOMEM if we don't have memory for the needed structs,
-ENODEV if the device is not supported or prints an error msg if something
else went wrong.

.. _`ath5k_hw_deinit`:

ath5k_hw_deinit
===============

.. c:function:: void ath5k_hw_deinit(struct ath5k_hw *ah)

    Free the \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

    :param struct ath5k_hw \*ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 

.. This file was automatic generated / don't edit.

