.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/bcm/spu.h

.. _`spu_req_incl_icv`:

spu_req_incl_icv
================

.. c:function:: bool spu_req_incl_icv(enum spu_cipher_mode cipher_mode, bool is_encrypt)

    Return true if SPU request message should include the ICV as a separate buffer.

    :param cipher_mode:
        the cipher mode being requested
    :type cipher_mode: enum spu_cipher_mode

    :param is_encrypt:
        true if encrypting. false if decrypting.
    :type is_encrypt: bool

.. _`spu_req_incl_icv.return`:

Return
------

true if ICV to be included as separate buffer

.. This file was automatic generated / don't edit.

